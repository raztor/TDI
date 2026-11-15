"""Receive only configured Cerro Seguro nodes and confirm committed SOS events."""
import logging
import math
import time
from meshtastic.protobuf import telemetry_pb2
from google.protobuf.message import DecodeError
from protocol import acknowledgement, parse_sos

LOG = logging.getLogger(__name__)
BROADCAST = 0xffffffff
METRICS = ("temperature", "relative_humidity", "barometric_pressure", "gas_resistance")


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


class Receiver:
    def __init__(self, store, allowed_nodes, station_node, channel=0):
        self.store = store
        self.allowed_nodes = set(allowed_nodes)
        self.station_node = station_node
        self.channel = channel

    def process(self, packet):
        node = packet.get("from")
        if node not in self.allowed_nodes or packet.get("channel", 0) != self.channel:
            return False
        destination = packet.get("to")
        decoded = packet.get("decoded", {})
        if not isinstance(decoded, dict):
            return False
        port = decoded.get("portnum")
        if port in (1, "TEXT_MESSAGE_APP"):
            if destination != self.station_node:
                return False
            text = decoded.get("text")
            if text is None:
                try:
                    text = decoded.get("payload", b"").decode("ascii")
                except (UnicodeError, AttributeError):
                    return False
            event_id = parse_sos(text)
            if event_id is None:
                return False
            # The transaction commits before the outbox can be transmitted.
            self.store.record_sos(node, event_id, self.channel)
            LOG.info("SOS registrado nodo=!%08x evento=%s", node, event_id)
            return True
        if port not in (67, "TELEMETRY_APP") or destination not in (self.station_node, BROADCAST):
            return False
        packet_id = packet.get("id")
        if not isinstance(packet_id, int) or isinstance(packet_id, bool) or not 0 < packet_id <= BROADCAST:
            return False
        telemetry = telemetry_pb2.Telemetry()
        try:
            telemetry.ParseFromString(decoded.get("payload", b""))
        except (TypeError, ValueError, DecodeError):
            return False
        if not telemetry.HasField("environment_metrics"):
            return False
        env = telemetry.environment_metrics
        metrics = {name: getattr(env, name) for name in METRICS if env.HasField(name)}
        if not metrics or not all(finite(value) for value in metrics.values()):
            return False
        captured = telemetry.time if telemetry.time > 0 else None
        rssi, snr = packet.get("rxRssi"), packet.get("rxSnr")
        self.store.record_measurement(node, packet_id, metrics, captured,
                                      rssi if finite(rssi) else None, snr if finite(snr) else None)
        return True

    def flush_acks(self, interface, now=None):
        now = time.time() if now is None else now
        for row in self.store.pending_acks(now):
            try:
                interface.sendText(acknowledgement(row["event_id"]),
                                   destinationId=row["node"], channelIndex=row["channel"],
                                   wantAck=False, wantResponse=False)
            except Exception as error:
                self.store.ack_failed(row, error, now)
                LOG.warning("ACK pendiente nodo=!%08x: %s", row["node"], error)
            else:
                self.store.ack_enqueued(row["node"], row["event_id"])
                LOG.info("ACK encolado nodo=!%08x evento=%s", row["node"], row["event_id"])

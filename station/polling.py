"""Nonblocking requests for environmental readings during bench tests."""
import logging
import time
from meshtastic.protobuf import portnums_pb2, telemetry_pb2

LOG = logging.getLogger(__name__)


class EnvironmentPoller:
    def __init__(self, nodes, channel, interval):
        if interval < 0:
            raise ValueError("The polling interval cannot be negative")
        self.nodes = tuple(nodes)
        self.channel = channel
        self.interval = interval
        self.next_poll = 0

    def poll(self, interface, now=None):
        now = time.monotonic() if now is None else now
        if not self.interval or now < self.next_poll:
            return
        self.next_poll = now + self.interval
        request = telemetry_pb2.Telemetry()
        request.environment_metrics.CopyFrom(telemetry_pb2.EnvironmentMetrics())
        for node in self.nodes:
            try:
                interface.sendData(request, destinationId=node,
                                   portNum=portnums_pb2.PortNum.TELEMETRY_APP,
                                   wantResponse=True, wantAck=False,
                                   channelIndex=self.channel)
                LOG.info("Telemetría solicitada nodo=!%08x intervalo=%ss", node, self.interval)
            except Exception:
                LOG.exception("No se pudo solicitar telemetría nodo=!%08x", node)

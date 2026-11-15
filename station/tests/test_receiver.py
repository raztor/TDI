import sqlite3
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from meshtastic.protobuf import telemetry_pb2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from protocol import acknowledgement, parse_sos
from receiver import Receiver, BROADCAST
from store import Store

RAK = 0x12345678
STATION = 0x87654321
EVENT = "0123456789abcdef00000001"


def sos(**changes):
    packet = {"from": RAK, "to": STATION, "channel": 0, "id": 100,
              "decoded": {"portnum": "TEXT_MESSAGE_APP", "text": f"CS1|SOS|{EVENT}"}}
    packet.update(changes)
    return packet


class Radio:
    def __init__(self, database=None, fail=False):
        self.messages = []
        self.database = database
        self.fail = fail

    def sendText(self, text, **kwargs):
        if self.fail:
            raise OSError("USB disconnected")
        # A separate connection proves the alert is committed before transmission.
        if self.database:
            with sqlite3.connect(self.database) as db:
                assert db.execute("SELECT count(*) FROM alerts").fetchone()[0] == 1
        self.messages.append((text, kwargs))


class StationTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.path = Path(self.temp.name) / "station.sqlite3"
        self.store = Store(self.path)
        self.receiver = Receiver(self.store, {RAK}, STATION)

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_strict_protocol(self):
        self.assertEqual(parse_sos(f"CS1|SOS|{EVENT}"), EVENT)
        for text in ("SOS", f"CS1|SOS|{EVENT}\n", f"CS1|ACK|{EVENT}|REGISTRADO",
                     f"CS1|SOS|{EVENT.upper()}", "CS1|SOS|bad", None):
            self.assertIsNone(parse_sos(text))
        self.assertEqual(acknowledgement(EVENT), f"CS1|ACK|{EVENT}|REGISTRADO")

    def test_commit_before_ack(self):
        radio = Radio(self.path)
        self.assertTrue(self.receiver.process(sos()))
        self.assertEqual(radio.messages, [])
        self.receiver.flush_acks(radio)
        self.assertEqual(len(radio.messages), 1)
        text, kwargs = radio.messages[0]
        self.assertEqual(text, acknowledgement(EVENT))
        self.assertEqual(kwargs["destinationId"], RAK)
        self.assertFalse(kwargs["wantAck"])

    def test_duplicate_reconfirms_without_duplicate_alert(self):
        radio = Radio()
        self.receiver.process(sos())
        self.receiver.flush_acks(radio)
        self.receiver.process(sos(id=101))
        self.receiver.flush_acks(radio)
        self.assertEqual(len(radio.messages), 2)
        row = self.store.db.execute("SELECT * FROM alerts").fetchall()
        self.assertEqual(len(row), 1)
        self.assertEqual(row[0]["reception_count"], 2)

    def test_wrong_source_destination_and_channel_ignored(self):
        for packet in (sos(**{"from": 123}), sos(to=BROADCAST), sos(to=123), sos(channel=1)):
            self.assertFalse(self.receiver.process(packet))
        self.assertEqual(self.store.db.execute("SELECT count(*) FROM alerts").fetchone()[0], 0)
        self.assertEqual(self.store.pending_acks(), [])

    def test_storage_failure_never_creates_ack(self):
        self.store.db.execute("PRAGMA query_only=ON")
        with self.assertRaises(sqlite3.OperationalError):
            self.receiver.process(sos())
        self.assertEqual(self.store.pending_acks(), [])

    def test_outbox_survives_restart(self):
        self.receiver.process(sos())
        self.store.close()
        self.store = Store(self.path)
        self.receiver = Receiver(self.store, {RAK}, STATION)
        radio = Radio(self.path)
        self.receiver.flush_acks(radio)
        self.assertEqual(len(radio.messages), 1)
        self.assertEqual(self.store.pending_acks(), [])

    def test_usb_failure_retains_pending_ack_with_backoff(self):
        self.receiver.process(sos())
        self.receiver.flush_acks(Radio(fail=True), now=100)
        self.assertEqual(self.store.pending_acks(now=101), [])
        self.assertEqual(len(self.store.pending_acks(now=102)), 1)
        radio = Radio()
        self.receiver.flush_acks(radio, now=102)
        self.assertEqual(len(radio.messages), 1)

    def test_telemetry_proto_and_duplicates(self):
        value = telemetry_pb2.Telemetry(time=123456)
        value.environment_metrics.temperature = 0.0
        value.environment_metrics.relative_humidity = 50
        packet = {"from": RAK, "to": BROADCAST, "id": 123, "rxRssi": -100,
                  "rxSnr": -2.5, "decoded": {"portnum": "TELEMETRY_APP", "payload": value.SerializeToString()}}
        self.assertTrue(self.receiver.process(packet))
        self.assertTrue(self.receiver.process(packet))
        rows = self.store.db.execute("SELECT * FROM measurements").fetchall()
        self.assertEqual(len(rows), 1)
        self.assertIn('"temperature": 0.0', rows[0]["metrics"])
        self.assertEqual(rows[0]["captured_epoch"], 123456)
        self.assertEqual(self.store.pending_acks(), [])

    def test_malformed_telemetry_and_nonfinite_values(self):
        packet = {"from": RAK, "to": STATION, "id": 124,
                  "decoded": {"portnum": 67, "payload": b"\xff"}}
        self.assertFalse(self.receiver.process(packet))
        value = telemetry_pb2.Telemetry()
        value.environment_metrics.temperature = float("nan")
        packet["decoded"]["payload"] = value.SerializeToString()
        self.assertFalse(self.receiver.process(packet))
        self.assertEqual(self.store.db.execute("SELECT count(*) FROM measurements").fetchone()[0], 0)

    def test_missing_sensor_time_is_not_replaced_with_reception_time(self):
        value = telemetry_pb2.Telemetry()
        value.environment_metrics.temperature = 18.5
        packet = {"from": RAK, "to": STATION, "id": 125,
                  "decoded": {"portnum": 67, "payload": value.SerializeToString()}}
        self.receiver.process(packet)
        row = self.store.db.execute("SELECT * FROM measurements").fetchone()
        self.assertIsNone(row["captured_epoch"])
        self.assertIsNotNone(row["received_at"])


if __name__ == "__main__":
    unittest.main()

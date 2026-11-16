from pathlib import Path
import sys
import unittest
from meshtastic.protobuf import portnums_pb2, telemetry_pb2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from polling import EnvironmentPoller


class Radio:
    def __init__(self):
        self.requests = []

    def sendData(self, request, **kwargs):
        self.requests.append((request.SerializeToString(), kwargs))


class PollingTests(unittest.TestCase):
    def test_requests_readings_every_120_seconds_without_inventing_metrics(self):
        radio = Radio()
        poller = EnvironmentPoller([0x12345678], 0, 120)
        for now in (100, 101, 219.999):
            poller.poll(radio, now=now)
        self.assertEqual(len(radio.requests), 1)
        poller.poll(radio, now=220)
        self.assertEqual(len(radio.requests), 2)
        payload, options = radio.requests[0]
        request = telemetry_pb2.Telemetry.FromString(payload)
        self.assertTrue(request.HasField("environment_metrics"))
        self.assertEqual(request.environment_metrics.ListFields(), [])
        self.assertEqual(options["destinationId"], 0x12345678)
        self.assertEqual(options["channelIndex"], 0)
        self.assertEqual(options["portNum"], portnums_pb2.PortNum.TELEMETRY_APP)
        self.assertTrue(options["wantResponse"])
        self.assertFalse(options["wantAck"])

    def test_disabled_polling_does_not_transmit(self):
        radio = Radio()
        EnvironmentPoller([0x12345678], 0, 0).poll(radio, now=100)
        self.assertEqual(radio.requests, [])


if __name__ == "__main__":
    unittest.main()

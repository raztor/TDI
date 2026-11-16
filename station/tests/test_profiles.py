from pathlib import Path
import unittest
import yaml
from google.protobuf.json_format import ParseDict
from meshtastic.protobuf import clientonly_pb2, config_pb2


class ProfileTests(unittest.TestCase):
    def test_profiles_match_pinned_sdk_and_network(self):
        root = Path(__file__).resolve().parents[2]
        for path in (root / "firmware/config").glob("*.yaml"):
            with self.subTest(profile=path.name):
                profile = clientonly_pb2.DeviceProfile()
                ParseDict(yaml.safe_load(path.read_text()), profile)
                self.assertEqual(profile.config.lora.region, config_pb2.Config.LoRaConfig.ANZ)
                self.assertEqual(profile.config.lora.channel_num, 20)
                self.assertTrue(profile.config.lora.tx_enabled)
                self.assertEqual(profile.config.device.role, config_pb2.Config.DeviceConfig.CLIENT_MUTE)
                self.assertFalse(profile.config.power.is_power_saving)
                self.assertFalse(profile.module_config.mqtt.enabled)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Install the Cerro Seguro overlay into a pinned Meshtastic checkout."""
import argparse
from pathlib import Path
import shutil
import subprocess

UPSTREAM_COMMIT = "54e0d8d0ab2ff56b3a9ce967e53f79e49af560fb"
UPSTREAM_TAG = "v2.7.26.54e0d8d"
FRAMEWORK_COMMIT = "9ddcbc9568b12f102f9e88bd4d1b88ea789213a4"


def node_id(value):
    try:
        number = int(value[1:], 16) if value.startswith("!") else int(value, 0)
    except ValueError as error:
        raise argparse.ArgumentTypeError("Use !1234abcd or 0x1234abcd") from error
    if not 0 <= number < 0xffffffff:
        raise argparse.ArgumentTypeError("A unicast NodeID is required")
    return number


def prepare(args):
    upstream = args.upstream.resolve()
    commit = subprocess.check_output(["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True).strip()
    if commit != UPSTREAM_COMMIT:
        raise SystemExit(f"Expected Meshtastic {UPSTREAM_TAG} at {UPSTREAM_COMMIT}; found {commit}")
    modules = upstream / "src/modules/Modules.cpp"
    text = modules.read_text()
    include = '#ifdef CERRO_SEGURO_SOS\n#include "CerroSeguroModule.h"\n#endif\n'
    instantiate = '#ifdef CERRO_SEGURO_SOS\n    new CerroSeguroModule();\n#endif\n'
    if include not in text:
        text = include + text
    if instantiate not in text:
        anchor = "void setupModules()\n{\n"
        if text.count(anchor) != 1:
            raise SystemExit("Unsupported Modules.cpp layout")
        text = text.replace(anchor, anchor + instantiate, 1)
    modules.write_text(text)
    for name in ("CerroSeguroModule.cpp", "CerroSeguroModule.h", "SosState.h", "SosProtocol.h"):
        shutil.copy2(Path(__file__).parent / name, upstream / "src/modules" / name)
    variant = upstream / "variants/nrf52840/cerroseguro"
    variant.mkdir(exist_ok=True)
    (variant / "platformio.ini").write_text(f"""[env:cerroseguro-rak4631]
extends = env:rak4631
platform_packages =
  platformio/framework-arduinoadafruitnrf52 @ https://github.com/meshtastic/Adafruit_nRF52_Arduino#{FRAMEWORK_COMMIT}
  platformio/toolchain-gccarmnoneeabi @ 1.90301.200702
build_flags = ${{env:rak4631.build_flags}}
  -DCERRO_SEGURO_SOS=1
  -DCS_STATION_NODE=0x{args.station_node:08x}UL
  -DCS_SOS_PIN={args.sos_pin}
  -DCS_CHANNEL={args.channel}
  -DCS_ACK_TIMEOUT_MS={args.ack_timeout_ms}UL
  -DCS_MAX_ATTEMPTS={args.max_attempts}
""")
    print(f"Prepared {upstream}; environment cerroseguro-rak4631; station !{args.station_node:08x}")
    if not args.station_node:
        print("Station is unset: SOS stays disabled until a real destination is configured and rebuilt.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path)
    parser.add_argument("--station-node", type=node_id, default=0)
    parser.add_argument("--sos-pin", type=int, choices=(4, 10, 21), default=10)
    parser.add_argument("--channel", type=int, choices=range(8), default=0)
    parser.add_argument("--ack-timeout-ms", type=int, default=60000)
    parser.add_argument("--max-attempts", type=int, choices=range(1, 6), default=3)
    args = parser.parse_args()
    if not 1000 <= args.ack_timeout_ms < 0x80000000:
        parser.error("--ack-timeout-ms must be between 1000 and 2147483647")
    prepare(args)

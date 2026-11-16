import argparse
import errno
import importlib.util
from pathlib import Path
import signal
import sqlite3
import subprocess
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("iniciar", ROOT / "tools/iniciar.py")
iniciar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iniciar)
sys.path.insert(0, str(ROOT / "station"))
from store import Store


def port(device, vid=None, pid=None, description="", manufacturer="", product=""):
    return SimpleNamespace(device=device, vid=vid, pid=pid, description=description,
                           manufacturer=manufacturer, product=product)


def options(database):
    return argparse.Namespace(port=None, list_ports=False, database=database,
                              dashboard_port=8765, poll_seconds=120,
                              rak_node=None, no_browser=True)


class PortTests(unittest.TestCase):
    def test_heltec_with_rak_and_bluetooth_connected(self):
        ports = [port("/dev/cu.Bluetooth-Incoming-Port"),
                 port("/dev/cu.usbmodemRAK", 0x239A, 0x8029, "RAK4631"),
                 port("/dev/cu.usbserial-0001", 0x10C4, 0xEA60, "CP2102 USB UART")]
        self.assertEqual(iniciar.select_port(ports), "/dev/cu.usbserial-0001")

    def test_no_device_does_not_fall_back_to_rak(self):
        with self.assertRaisesRegex(iniciar.StartupError, "No se detectó"):
            iniciar.select_port([port("/dev/cu.usbmodemRAK", 0x239A, 0x8029, "RAK4631")])

    def test_ambiguous_usb_requires_explicit_selection(self):
        ports = [port(f"/dev/cu.usbserial-{i}", 0x10C4, 0xEA60) for i in (1, 2)]
        with self.assertRaisesRegex(iniciar.StartupError, "--port"):
            iniciar.select_port(ports)

    def test_named_heltec_and_duplicate_macos_aliases(self):
        ports = [port("/dev/tty.usbserial-1", description="Heltec"),
                 port("/dev/cu.usbserial-1", description="Heltec"),
                 port("/dev/cu.usbserial-2", 0x10C4, 0xEA60)]
        self.assertEqual(iniciar.select_port(ports), "/dev/cu.usbserial-1")

    def test_explicit_port_and_missing_path(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "usbserial"
            path.touch()
            self.assertEqual(iniciar.select_port([], str(path)), str(path))
        with self.assertRaisesRegex(iniciar.StartupError, "No existe"):
            iniciar.select_port([], str(path))


class LifecycleTests(unittest.TestCase):
    def test_web_port_reports_busy_and_permission_errors_separately(self):
        cases = [(OSError(errno.EADDRINUSE, "in use"), "está ocupado"),
                 (PermissionError(errno.EPERM, "denied"), "No se pudo habilitar")]
        for error, message in cases:
            with self.subTest(error=error), patch.object(iniciar.socket, "socket") as factory:
                factory.return_value.__enter__.return_value.bind.side_effect = error
                with self.assertRaisesRegex(iniciar.StartupError, message):
                    iniciar.check_http_port(8765)

    def test_database_waits_for_real_station_schema(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "station.sqlite3"
            self.assertFalse(iniciar.database_ready(path))
            self.assertFalse(path.exists())
            with sqlite3.connect(path):
                pass
            self.assertFalse(iniciar.database_ready(path))
            store = Store(path)
            try:
                self.assertTrue(iniciar.database_ready(path))
            finally:
                store.close()

    def test_second_process_failure_stops_first(self):
        station = Mock()
        with TemporaryDirectory() as tmp, \
             patch.object(iniciar, "usb_ports", return_value=[]), \
             patch.object(iniciar, "select_port", return_value="/dev/cu.test"), \
             patch.object(iniciar, "check_http_port"), \
             patch.object(iniciar, "wait_ready"), \
             patch.object(iniciar.subprocess, "Popen", side_effect=[station, OSError("fallo")]), \
             patch.object(iniciar, "stop_children") as stop:
            with self.assertRaises(OSError):
                iniciar.launch(options(Path(tmp) / "db.sqlite3"))
            stop.assert_called_once_with([("La estación USB", station)])

    def test_child_exit_stops_peer_and_uses_shared_database(self):
        station, dashboard = Mock(), Mock()
        station.poll.return_value = 1
        with TemporaryDirectory() as tmp, \
             patch.object(iniciar, "usb_ports", return_value=[]), \
             patch.object(iniciar, "select_port", return_value="/dev/cu.test"), \
             patch.object(iniciar, "check_http_port"), \
             patch.object(iniciar, "wait_ready"), \
             patch.object(iniciar.subprocess, "Popen", side_effect=[station, dashboard]) as spawn, \
             patch.object(iniciar, "stop_children") as stop:
            args = options(Path(tmp) / "db.sqlite3")
            with self.assertRaisesRegex(iniciar.StartupError, "se detuvo"):
                iniciar.launch(args)
            commands = [call.args[0] for call in spawn.call_args_list]
            for command in commands:
                self.assertEqual(command[command.index("--database") + 1], str(args.database.resolve()))
            self.assertEqual(commands[0][commands[0].index("--telemetry-poll-seconds") + 1], "120")
            self.assertEqual(commands[1][commands[1].index("--expected-interval") + 1], "120")
            self.assertTrue(all(call.kwargs["start_new_session"] for call in spawn.call_args_list))
            stop.assert_called_once_with([("La estación USB", station), ("El dashboard", dashboard)])

    def test_interrupt_during_startup_cleans_up(self):
        station = Mock()
        with TemporaryDirectory() as tmp, \
             patch.object(iniciar, "usb_ports", return_value=[]), \
             patch.object(iniciar, "select_port", return_value="/dev/cu.test"), \
             patch.object(iniciar, "check_http_port"), \
             patch.object(iniciar, "wait_ready", side_effect=KeyboardInterrupt), \
             patch.object(iniciar.subprocess, "Popen", return_value=station), \
             patch.object(iniciar, "stop_children") as stop:
            self.assertEqual(iniciar.launch(options(Path(tmp) / "db.sqlite3")), 0)
            stop.assert_called_once_with([("La estación USB", station)])

    def test_shutdown_reaps_owned_processes_and_leaves_other_process(self):
        processes = [subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"],
                                     start_new_session=True, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL) for _ in range(3)]
        try:
            iniciar.stop_children([("one", processes[0]), ("two", processes[1])])
            self.assertIsNotNone(processes[0].poll())
            self.assertIsNotNone(processes[1].poll())
            self.assertIsNone(processes[2].poll())
        finally:
            for process in processes:
                if process.poll() is None:
                    process.kill()
                process.wait()

    def test_stubborn_child_is_killed_after_timeout(self):
        child = Mock(pid=12345)
        child.poll.return_value = None
        child.wait.side_effect = [subprocess.TimeoutExpired("test", 8), 0]
        with patch.object(iniciar.os, "killpg") as kill:
            iniciar.stop_children([("test", child)])
        self.assertEqual([call.args for call in kill.call_args_list],
                         [(12345, signal.SIGINT), (12345, signal.SIGKILL)])


if __name__ == "__main__":
    unittest.main()

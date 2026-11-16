#!/usr/bin/env python3
"""Inicia y supervisa la estación Heltec USB y el dashboard local."""
import argparse
import errno
import os
from pathlib import Path
import signal
import socket
import sqlite3
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen
import webbrowser

ROOT = Path(__file__).resolve().parents[1]
RAK_NODE = "!1630f9c9"


class StartupError(Exception):
    pass


def usb_ports():
    from serial.tools import list_ports
    return list(list_ports.comports())


def port_label(port):
    identity = ""
    if port.vid is not None and port.pid is not None:
        identity = f" [{port.vid:04x}:{port.pid:04x}]"
    return f"{port.device} — {port.description or 'USB serie'}{identity}"


def select_port(ports, explicit=None):
    if explicit:
        if not Path(explicit).exists():
            raise StartupError(f"No existe el puerto {explicit}.")
        return explicit
    named, compatible = {}, {}
    for port in ports:
        description = " ".join(str(getattr(port, name, "") or "")
                               for name in ("description", "manufacturer", "product")).lower()
        # En macOS se usa cu.*; tty.* puede ser un alias del mismo dispositivo.
        device = port.device.replace("/dev/tty.", "/dev/cu.", 1)
        if "heltec" in description:
            named[device] = port
        # Heltec V3/V3.2 integra CP2102. No seleccionar el USB nativo del RAK.
        elif (port.vid, port.pid) == (0x10C4, 0xEA60) or "cp210" in description:
            compatible[device] = port
    candidates = named if named else compatible
    if len(candidates) == 1:
        return next(iter(candidates))
    if candidates:
        choices = "\n".join(f"  {port_label(p)}" for p in candidates.values())
        raise StartupError("Hay varios puertos compatibles; indica el Heltec con --port.\n"
                           f"{choices}\nEjemplo: ./iniciar.sh --port /dev/cu.usbserial-0001")
    visible = "\n".join(f"  {port_label(p)}" for p in ports) or "  Ninguno"
    raise StartupError("No se detectó el Heltec. Conéctalo con un cable USB de datos.\n"
                       f"Puertos disponibles:\n{visible}\n"
                       "Si su adaptador no se identifica, utiliza --port /dev/cu.…")


def check_http_port(port):
    try:
        with socket.socket() as probe:
            probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            probe.bind(("127.0.0.1", port))
    except OSError as error:
        if error.errno == errno.EADDRINUSE:
            raise StartupError(f"El puerto web {port} está ocupado. "
                               "Detén el dashboard anterior o usa --dashboard-port 8766.") from error
        raise StartupError(f"No se pudo habilitar el puerto web {port}: {error}") from error


def database_ready(path):
    if not path.is_file():
        return False
    try:
        with sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True, timeout=0.2) as db:
            tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        return {"measurements", "alerts", "ack_outbox", "station_status"} <= tables
    except sqlite3.Error:
        return False


def check_children(children):
    for name, child in children:
        status = child.poll()
        if status is not None:
            raise StartupError(f"{name} se detuvo (código {status}). Revisa el error mostrado arriba.")


def wait_ready(predicate, children, description, timeout=60):
    deadline = time.monotonic() + timeout
    while True:
        check_children(children)
        if predicate():
            return
        if time.monotonic() >= deadline:
            raise StartupError(f"Tiempo agotado esperando {description}.")
        time.sleep(0.2)


def http_ready(url):
    try:
        with urlopen(url, timeout=0.5) as response:
            return response.status == 200
    except (URLError, OSError):
        return False


def stop_children(children):
    # Cada hijo tiene su propia sesión; las señales solo alcanzan estos procesos.
    for _, child in children:
        if child.poll() is None:
            try:
                os.killpg(child.pid, signal.SIGINT)
            except ProcessLookupError:
                pass
    deadline = time.monotonic() + 8
    for _, child in children:
        try:
            child.wait(timeout=max(0, deadline - time.monotonic()))
        except subprocess.TimeoutExpired:
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            child.wait()


def launch(args):
    ports = usb_ports()
    if args.list_ports:
        print("\n".join(port_label(p) for p in ports) or "No hay puertos serie disponibles.")
        return 0
    device = select_port(ports, args.port)
    check_http_port(args.dashboard_port)
    database = args.database.expanduser()
    if not database.is_absolute():
        database = ROOT / database
    database = database.resolve()
    children = []
    previous = {}

    def interrupted(signum, frame):
        raise KeyboardInterrupt

    try:
        for sig in (signal.SIGINT, signal.SIGTERM):
            previous[sig] = signal.signal(sig, interrupted)
        print(f"Puerto seleccionado: {device}\nBase de datos: {database}", flush=True)
        station = [sys.executable, "-u", str(ROOT / "station/main.py"), "--port", device,
                   "--channel", "0", "--telemetry-poll-seconds", str(args.poll_seconds),
                   "--database", str(database)]
        for node in args.rak_node or [RAK_NODE]:
            station.extend(["--rak-node", node])
        children.append(("La estación USB", subprocess.Popen(station, cwd=ROOT, start_new_session=True)))
        print("Iniciando recepción USB y esperando la base de datos...", flush=True)
        wait_ready(lambda: database_ready(database), children, "la base de datos")
        dashboard = [sys.executable, "-u", str(ROOT / "dashboard/server.py"),
                     "--database", str(database), "--expected-interval", str(args.poll_seconds),
                     "--port", str(args.dashboard_port)]
        children.append(("El dashboard", subprocess.Popen(dashboard, cwd=ROOT, start_new_session=True)))
        url = f"http://127.0.0.1:{args.dashboard_port}"
        wait_ready(lambda: http_ready(url), children, "el dashboard", timeout=15)
        print(f"Dashboard disponible: {url}\nSondeo: {args.poll_seconds} s. Ctrl+C detiene ambos servicios.\n"
              "La conexión de radio se confirma en el log de la estación y en el estado USB del dashboard.", flush=True)
        if not args.no_browser:
            try:
                webbrowser.open(url)
            except webbrowser.Error:
                print(f"Abre el navegador en {url}", flush=True)
        while True:
            check_children(children)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nDeteniendo estación y dashboard...", flush=True)
        return 0
    finally:
        # Un segundo Ctrl+C no debe interrumpir el cierre y dejar un hijo abierto.
        for sig in previous:
            signal.signal(sig, signal.SIG_IGN)
        try:
            stop_children(children)
        finally:
            for sig, handler in previous.items():
                signal.signal(sig, handler)


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Debe ser mayor que cero")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", help="Puerto USB manual; por defecto detecta Heltec/CP210x")
    parser.add_argument("--rak-node", action="append", help=f"Nodo autorizado; por defecto {RAK_NODE}")
    parser.add_argument("--database", type=Path, default=Path("station-data/cerroseguro.sqlite3"))
    parser.add_argument("--poll-seconds", type=positive, default=120)
    parser.add_argument("--dashboard-port", type=positive, default=8765)
    parser.add_argument("--no-browser", action="store_true", help="No abrir el navegador automáticamente")
    parser.add_argument("--list-ports", action="store_true", help="Mostrar puertos y salir sin iniciar servicios")
    args = parser.parse_args()
    if args.dashboard_port > 65535:
        parser.error("El puerto web debe estar entre 1 y 65535")
    try:
        return launch(args)
    except (StartupError, OSError, ImportError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

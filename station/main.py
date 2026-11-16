#!/usr/bin/env python3
"""Cerro Seguro USB receiver and persistent acknowledgement service."""
import argparse
import logging
from pathlib import Path
import queue
import threading
import time
from meshtastic.serial_interface import SerialInterface
from pubsub import pub
from receiver import Receiver
from store import Store

LOG = logging.getLogger("cerroseguro")


def node_id(value):
    try:
        node = int(value[1:], 16) if value.startswith("!") else int(value, 0)
    except ValueError as error:
        raise argparse.ArgumentTypeError("Use !1234abcd or 0x1234abcd") from error
    if not 0 < node < 0xffffffff:
        raise argparse.ArgumentTypeError("A unicast NodeID is required")
    return node


def run(args):
    args.database.parent.mkdir(parents=True, exist_ok=True)
    store = Store(args.database)
    incoming = queue.Queue(maxsize=256)
    disconnected = threading.Event()
    interface = None
    active_radio = [None]

    def on_receive(packet, interface):
        try:
            incoming.put_nowait((packet, interface))
        except queue.Full:
            LOG.error("Cola de recepción llena: paquete descartado; SOS sin ACK será reintentado por el emisor")

    def on_lost(interface):
        if interface is active_radio[0]:
            disconnected.set()

    pub.subscribe(on_receive, "meshtastic.receive")
    pub.subscribe(on_lost, "meshtastic.connection.lost")
    try:
        while True:
            if interface is None:
                disconnected.clear()
                try:
                    interface = SerialInterface(devPath=args.port, noNodes=True, timeout=20)
                    active_radio[0] = interface
                    own_node = interface.myInfo.my_node_num
                    if own_node in args.rak_node:
                        raise ValueError("La LILYGO y el RAK deben tener NodeID diferentes")
                    receiver = Receiver(store, args.rak_node, own_node, args.channel)
                    LOG.info("Estación !%08x conectada; base=%s", own_node, args.database)
                except Exception:
                    LOG.exception("No se pudo conectar la estación por USB; reintento en 5 s")
                    if interface is not None:
                        interface.close()
                    interface = None
                    active_radio[0] = None
                    time.sleep(5)
                    continue
            if disconnected.is_set():
                active_radio[0] = None
                interface.close()
                interface = None
                continue
            try:
                packet, source_interface = incoming.get(timeout=0.5)
            except queue.Empty:
                pass
            else:
                if source_interface is interface:
                    try:
                        receiver.process(packet)
                    except Exception:
                        LOG.exception("No se pudo procesar o guardar el paquete; no se confirma el SOS")
            try:
                receiver.flush_acks(interface)
            except Exception:
                LOG.exception("No se pudo actualizar la cola persistente de ACK")
    except KeyboardInterrupt:
        LOG.info("Estación detenida")
    finally:
        pub.unsubscribe(on_receive, "meshtastic.receive")
        pub.unsubscribe(on_lost, "meshtastic.connection.lost")
        if interface is not None:
            interface.close()
        store.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True, help="Puerto USB de la LILYGO, por ejemplo COM4")
    parser.add_argument("--rak-node", required=True, type=node_id, action="append")
    parser.add_argument("--channel", type=int, choices=range(8), default=0)
    parser.add_argument("--database", type=Path, default=Path("station-data/cerroseguro.sqlite3"))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run(parser.parse_args())

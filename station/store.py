"""Persistent alerts, telemetry and a transactional acknowledgement outbox."""
from datetime import datetime, timezone
import json
import sqlite3
import time


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


class Store:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=FULL")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS alerts (
                node INTEGER NOT NULL, event_id TEXT NOT NULL,
                first_received_at TEXT NOT NULL, last_received_at TEXT NOT NULL,
                reception_count INTEGER NOT NULL DEFAULT 1,
                PRIMARY KEY (node, event_id)
            );
            CREATE TABLE IF NOT EXISTS ack_outbox (
                node INTEGER NOT NULL, event_id TEXT NOT NULL, channel INTEGER NOT NULL,
                pending INTEGER NOT NULL DEFAULT 1, attempts INTEGER NOT NULL DEFAULT 0,
                next_attempt REAL NOT NULL DEFAULT 0, last_error TEXT,
                enqueued_at TEXT,
                PRIMARY KEY (node, event_id),
                FOREIGN KEY (node, event_id) REFERENCES alerts(node, event_id)
            );
            CREATE TABLE IF NOT EXISTS measurements (
                node INTEGER NOT NULL, packet_id INTEGER NOT NULL,
                received_at TEXT NOT NULL, captured_epoch INTEGER,
                metrics TEXT NOT NULL, rssi REAL, snr REAL,
                PRIMARY KEY (node, packet_id)
            );
            CREATE TABLE IF NOT EXISTS station_status (
                id INTEGER PRIMARY KEY CHECK(id=1),
                state TEXT NOT NULL, updated_at TEXT NOT NULL,
                station_node INTEGER, port TEXT NOT NULL,
                poll_seconds INTEGER NOT NULL, last_error TEXT
            );
        """)

    def close(self):
        self.db.close()

    def station_status(self, state, station_node, port, poll_seconds, error=None):
        with self.db:
            self.db.execute("""
                INSERT INTO station_status VALUES (1,?,?,?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET state=excluded.state,
                updated_at=excluded.updated_at,station_node=excluded.station_node,
                port=excluded.port,poll_seconds=excluded.poll_seconds,
                last_error=excluded.last_error
            """, (state, utc_now(), station_node, port, poll_seconds, error))

    def record_sos(self, node, event_id, channel):
        now = utc_now()
        with self.db:
            self.db.execute("""
                INSERT INTO alerts(node,event_id,first_received_at,last_received_at)
                VALUES (?,?,?,?) ON CONFLICT(node,event_id) DO UPDATE SET
                last_received_at=excluded.last_received_at,
                reception_count=reception_count+1
            """, (node, event_id, now, now))
            self.db.execute("""
                INSERT INTO ack_outbox(node,event_id,channel) VALUES (?,?,?)
                ON CONFLICT(node,event_id) DO UPDATE SET
                pending=1, channel=excluded.channel, next_attempt=0
            """, (node, event_id, channel))

    def record_measurement(self, node, packet_id, metrics, captured_epoch=None, rssi=None, snr=None):
        with self.db:
            self.db.execute("""
                INSERT OR IGNORE INTO measurements VALUES (?,?,?,?,?,?,?)
            """, (node, packet_id, utc_now(), captured_epoch,
                  json.dumps(metrics, allow_nan=False, sort_keys=True), rssi, snr))

    def pending_acks(self, now=None):
        return self.db.execute("""
            SELECT * FROM ack_outbox WHERE pending=1 AND next_attempt<=?
            ORDER BY next_attempt, node, event_id LIMIT 10
        """, (time.time() if now is None else now,)).fetchall()

    def ack_enqueued(self, node, event_id):
        with self.db:
            self.db.execute("""
                UPDATE ack_outbox SET pending=0, attempts=attempts+1,
                enqueued_at=?,last_error=NULL WHERE node=? AND event_id=?
            """, (utc_now(), node, event_id))

    def ack_failed(self, row, error, now):
        delay = min(60, 2 ** min(row["attempts"] + 1, 6))
        with self.db:
            self.db.execute("""
                UPDATE ack_outbox SET attempts=attempts+1,next_attempt=?,last_error=?
                WHERE node=? AND event_id=?
            """, (now + delay, str(error), row["node"], row["event_id"]))

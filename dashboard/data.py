"""Read-only telemetry queries and independent operator reviews."""
from datetime import datetime, timezone
from contextlib import contextmanager
import json
import math
from pathlib import Path
import sqlite3
from statistics import median


def stamp(value):
    return datetime.fromisoformat(value).timestamp() if value else None


def finite(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value)


def node_id(number):
    return f"!{number:08x}"


class DashboardData:
    def __init__(self, database, expected_interval=120):
        self.database = Path(database).resolve()
        self.expected_interval = expected_interval
        if not self.database.is_file():
            raise ValueError("No existe la base de la estación; iniciar station/main.py primero")
        with self.connect(write=True) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS alert_reviews (
                node INTEGER NOT NULL,event_id TEXT NOT NULL,reviewed_at TEXT NOT NULL,
                PRIMARY KEY(node,event_id),
                FOREIGN KEY(node,event_id) REFERENCES alerts(node,event_id))""")

    @contextmanager
    def connect(self, write=False):
        mode = "rw" if write else "ro"
        db = sqlite3.connect(f"{self.database.as_uri()}?mode={mode}", uri=True, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    def _rows(self, db, since, until, node):
        sql = "SELECT * FROM measurements WHERE received_at>=? AND received_at<=?"
        args = [since, until]
        if node is not None:
            sql += " AND node=?"
            args.append(node)
        # Bound the browser response; CSV uses the complete selected range.
        sql += " ORDER BY received_at DESC LIMIT 20001"
        rows = db.execute(sql, args).fetchall()
        return rows[:20000], len(rows) > 20000

    @staticmethod
    def measurement(row):
        raw = json.loads(row["metrics"])
        capture = row["captured_epoch"]
        # Unsynchronised Meshtastic devices can report uptime as an epoch.
        if capture is not None and capture < 1577836800:
            capture = None
        return {"node": node_id(row["node"]), "packet_id": row["packet_id"],
                "received_at": row["received_at"], "captured_epoch": capture,
                "temperature": raw.get("temperature") if finite(raw.get("temperature")) else None,
                "humidity": raw.get("relative_humidity") if finite(raw.get("relative_humidity")) else None,
                "rssi": row["rssi"], "snr": row["snr"]}

    def snapshot(self, since, until, node=None, now=None):
        now = datetime.now(timezone.utc).timestamp() if now is None else now
        with self.connect() as db:
            nodes = [{"id": node_id(r["node"]), "first_received_at": r["first_at"],
                      "last_received_at": r["last_at"], "measurements": r["n"]}
                     for r in db.execute("""SELECT node,MIN(received_at) first_at,
                        MAX(received_at) last_at,COUNT(*) n FROM measurements GROUP BY node""")]
            rows, truncated = self._rows(db, since, until, node)
            readings = [self.measurement(row) for row in reversed(rows)]
            where, args = (" WHERE node=?", (node,)) if node is not None else ("", ())
            latest_row = db.execute("SELECT * FROM measurements" + where +
                                    " ORDER BY received_at DESC LIMIT 1", args).fetchone()
            latest = self.measurement(latest_row) if latest_row else None
            alerts = []
            alert_rows = db.execute("""SELECT a.*,o.pending,o.attempts,o.enqueued_at,o.last_error,
                r.reviewed_at FROM alerts a LEFT JOIN ack_outbox o USING(node,event_id)
                LEFT JOIN alert_reviews r USING(node,event_id)""" +
                (" WHERE a.node=?" if node is not None else "") +
                " ORDER BY a.first_received_at DESC LIMIT 500", args)
            for row in alert_rows:
                item = dict(row)
                item["node"] = node_id(item["node"])
                item["ack_state"] = ("pending" if item["pending"] else "queued") if item["pending"] is not None else "unknown"
                alerts.append(item)
            counts = db.execute("""SELECT COUNT(*) total,
                COALESCE(SUM(r.reviewed_at IS NULL),0) unreviewed FROM alerts a
                LEFT JOIN alert_reviews r USING(node,event_id)""" +
                (" WHERE a.node=?" if node is not None else ""), args).fetchone()
            tables = {r["name"] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            status_row = db.execute("SELECT * FROM station_status WHERE id=1").fetchone() if "station_status" in tables else None
        status = dict(status_row) if status_row else None
        if status:
            age = max(0, now - stamp(status["updated_at"]))
            status["heartbeat_age_seconds"] = round(age, 1)
            status["live"] = age <= 15 and status["state"] == "connected"
            if status["station_node"] is not None:
                status["station_node"] = node_id(status["station_node"])
        temps = [r["temperature"] for r in readings if r["temperature"] is not None]
        # Compare successive samples of the same node only.
        groups = {}
        for reading in readings:
            groups.setdefault(reading["node"], []).append(reading)
        gaps = [stamp(b["received_at"]) - stamp(a["received_at"])
                for group in groups.values() for a,b in zip(group, group[1:])]
        interval = status["poll_seconds"] if status and status["poll_seconds"] > 0 else self.expected_interval
        freshness = max(0, now-stamp(latest["received_at"])) if latest else None
        stats = {"samples": len(readings), "min": min(temps) if temps else None,
                 "max": max(temps) if temps else None,
                 "mean": sum(temps)/len(temps) if temps else None,
                 "delta": temps[-1]-temps[0] if len(temps)>1 and len(groups)==1 else None,
                 "median_interval_seconds": median(gaps) if gaps else None}
        return {"generated_at": datetime.fromtimestamp(now, timezone.utc).isoformat(),
                "timezone": "America/Santiago", "nodes": nodes, "latest": latest,
                "readings": readings, "truncated": truncated, "statistics": stats,
                "alerts": alerts, "alert_counts": dict(counts), "station": status,
                "freshness": {"age_seconds": freshness, "stale_after_seconds": interval*3,
                              "state": "missing" if latest is None else "stale" if freshness>interval*3 else "fresh"},
                "expected_interval_seconds": interval}

    def review(self, node, event_id, reviewed=True):
        with self.connect(write=True) as db:
            if not db.execute("SELECT 1 FROM alerts WHERE node=? AND event_id=?", (node,event_id)).fetchone():
                raise LookupError("Alerta inexistente")
            if reviewed:
                db.execute("INSERT OR IGNORE INTO alert_reviews VALUES (?,?,?)",
                           (node, event_id, datetime.now(timezone.utc).isoformat(timespec="milliseconds")))
            else:
                db.execute("DELETE FROM alert_reviews WHERE node=? AND event_id=?",(node,event_id))

    def export_rows(self, since, until, node=None):
        # Stream CSV without loading the entire historical dataset into RAM.
        with self.connect() as db:
            query = "SELECT * FROM measurements WHERE received_at>=? AND received_at<=?"
            args = [since,until]
            if node is not None:
                query += " AND node=?"
                args.append(node)
            for row in db.execute(query + " ORDER BY received_at", args):
                yield self.measurement(row)

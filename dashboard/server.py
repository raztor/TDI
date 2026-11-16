#!/usr/bin/env python3
"""Local dashboard for the station database; never opens a serial port."""
import argparse
import csv
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, urlparse
from data import DashboardData

STATIC = Path(__file__).parent / "static"


def parse_node(value):
    if not re.fullmatch(r"![0-9a-fA-F]{8}", value or ""):
        raise ValueError("NodeID inválido")
    node = int(value[1:],16)
    if node in (0,0xffffffff):
        raise ValueError("NodeID inválido")
    return node


def parse_date(value):
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None:
        raise ValueError("La fecha debe incluir zona horaria")
    return date.astimezone(timezone.utc)


def selection(query):
    now = datetime.now(timezone.utc)
    end = parse_date(query["until"][0]) if query.get("until") else now
    if query.get("since"):
        start = parse_date(query["since"][0])
    else:
        hours = float(query.get("hours", [24])[0])
        if not 0 < hours <= 24*366:
            raise ValueError("Selecciona entre 0 y 8784 horas")
        start = end-timedelta(hours=hours)
    if start > end or (end-start).days > 366:
        raise ValueError("Rango de fechas inválido; máximo 366 días")
    node = parse_node(query["node"][0]) if query.get("node") else None
    return start.isoformat(timespec="milliseconds"), end.isoformat(timespec="milliseconds"), node


class Handler(BaseHTTPRequestHandler):
    def start_response(self, status, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; object-src 'none'; frame-ancestors 'none'")

    def reply(self, status, data):
        body = json.dumps(data, ensure_ascii=False, allow_nan=False).encode()
        self.start_response(status,"application/json; charset=utf-8")
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        request = urlparse(self.path)
        try:
            if request.path in ("/api/dashboard", "/api/export.csv"):
                since, until, node = selection(parse_qs(request.query))
                if request.path.endswith(".csv"):
                    self.start_response(200,"text/csv; charset=utf-8")
                    self.send_header("Content-Disposition",'attachment; filename="cerro-seguro-lecturas.csv"')
                    self.end_headers()
                    output=io.StringIO()
                    fields=["node","packet_id","received_at","captured_epoch","temperature","humidity","rssi","snr"]
                    writer=csv.DictWriter(output,fieldnames=fields)
                    writer.writeheader()
                    self.wfile.write(output.getvalue().encode('utf-8-sig'))
                    for row in self.server.data.export_rows(since,until,node):
                        output.seek(0);output.truncate(0)
                        writer.writerow(row)
                        self.wfile.write(output.getvalue().encode())
                else:
                    self.reply(200,self.server.data.snapshot(since,until,node))
                return
            assets={"/":("index.html","text/html"),"/app.js":("app.js","application/javascript"),"/style.css":("style.css","text/css")}
            if request.path not in assets:
                self.reply(404,{"error":"Recurso inexistente"});return
            name,kind=assets[request.path]
            body=(STATIC/name).read_bytes()
            self.start_response(200,kind+"; charset=utf-8")
            self.send_header("Content-Length",str(len(body)))
            self.end_headers();self.wfile.write(body)
        except (ValueError,OverflowError) as error:
            self.reply(400,{"error":str(error)})
        except (BrokenPipeError,ConnectionResetError):
            pass
        except Exception:
            self.log_error("No se pudo consultar la base de datos")
            self.reply(503,{"error":"No se pudo consultar la estación. Reintenta en unos segundos."})

    def do_POST(self):
        if self.path != "/api/alerts/review":
            self.reply(404,{"error":"Recurso inexistente"});return
        origin=self.headers.get("Origin")
        if origin and origin != "http://"+self.headers.get("Host",""):
            self.reply(403,{"error":"Origen no permitido"});return
        try:
            length=int(self.headers.get("Content-Length",0))
            if not 0 < length <= 2048 or self.headers.get("Content-Type","").split(';')[0] != "application/json":
                raise ValueError("Se requiere un cuerpo JSON válido")
            payload=json.loads(self.rfile.read(length))
            node=parse_node(payload.get("node"))
            event=payload.get("event_id","")
            if not re.fullmatch(r"[0-9a-f]{24}",event):
                raise ValueError("Identificador de evento inválido")
            reviewed=payload.get("reviewed",True)
            if not isinstance(reviewed,bool):
                raise ValueError("La revisión debe ser true o false")
            self.server.data.review(node,event,reviewed)
            self.reply(200,{"reviewed":reviewed})
        except LookupError as error:
            self.reply(404,{"error":str(error)})
        except (ValueError,TypeError,AttributeError) as error:
            self.reply(400,{"error":str(error)})
        except Exception:
            self.reply(503,{"error":"No se pudo guardar la revisión"})


def make_server(database, port=8765, expected_interval=120):
    server=ThreadingHTTPServer(("127.0.0.1",port),Handler)
    server.data=DashboardData(database,expected_interval)
    return server


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database",type=Path,default=Path("station-data/cerroseguro.sqlite3"))
    parser.add_argument("--port",type=int,default=8765)
    parser.add_argument("--expected-interval",type=int,default=120)
    args=parser.parse_args()
    if args.expected_interval<=0:
        parser.error("El intervalo esperado debe ser positivo")
    server=make_server(args.database,args.port,args.expected_interval)
    print(f"Cerro Seguro: http://127.0.0.1:{server.server_port}",flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()

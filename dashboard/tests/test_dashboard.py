from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
import sys
from tempfile import TemporaryDirectory
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'station'))
sys.path.insert(0,str(ROOT/'dashboard'))
from store import Store
from data import DashboardData
from server import make_server

NODE=0x1630f9c9
EVENT='0123456789abcdef00000001'


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory()
        self.path=Path(self.temp.name)/'station.sqlite3'
        s=Store(self.path)
        s.record_measurement(NODE,1,{'temperature':0.0,'relative_humidity':40},446,-70,6)
        s.record_measurement(NODE,2,{'temperature':10.0,'relative_humidity':50},1794744120,-71,5)
        s.db.execute("UPDATE measurements SET received_at='2026-11-15T12:00:00.000+00:00' WHERE packet_id=1")
        s.db.execute("UPDATE measurements SET received_at='2026-11-15T12:02:00.000+00:00' WHERE packet_id=2")
        s.db.commit()
        s.record_sos(NODE,EVENT,0)
        s.ack_enqueued(NODE,EVENT)
        s.station_status('connected',0x849c7328,'TEST',120)
        s.db.execute("UPDATE station_status SET updated_at='2026-11-15T12:02:00.000+00:00'")
        s.db.commit();s.close()
        self.data=DashboardData(self.path)

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self,now='2026-11-15T12:02:05+00:00'):
        return self.data.snapshot('2026-11-15T11:00:00.000+00:00','2026-11-15T13:00:00.000+00:00',NODE,
                                  datetime.fromisoformat(now).timestamp())


class DataTests(Fixture):
    def test_real_statistics_and_zero_temperature(self):
        d=self.snapshot()
        self.assertEqual(d['statistics']['mean'],5)
        self.assertEqual(d['statistics']['delta'],10)
        self.assertEqual(d['statistics']['median_interval_seconds'],120)
        self.assertEqual(d['readings'][0]['temperature'],0)
        self.assertIsNone(d['readings'][0]['captured_epoch'])
        self.assertEqual(d['readings'][1]['captured_epoch'],1794744120)
        self.assertTrue(d['station']['live'])

    def test_stale_data_and_station_heartbeat_are_independent(self):
        d=self.snapshot('2026-11-15T12:03:00+00:00')
        self.assertFalse(d['station']['live'])
        self.assertEqual(d['freshness']['state'],'fresh')
        self.assertEqual(self.snapshot('2026-11-15T12:09:00+00:00')['freshness']['state'],'stale')

    def test_historical_window_and_node_filter(self):
        d=self.data.snapshot('2026-11-15T11:59:00.000+00:00','2026-11-15T12:01:00.000+00:00',NODE)
        self.assertEqual(d['statistics']['samples'],1)
        self.assertEqual(d['statistics']['mean'],0)
        # Current-condition cards retain the latest actual reading.
        self.assertEqual(d['latest']['temperature'],10)
        self.assertEqual(self.data.snapshot('2026-11-15','2026-11-16',123)['statistics']['samples'],0)

    def test_operator_review_persists_and_does_not_change_ack(self):
        self.assertEqual(self.snapshot()['alert_counts']['unreviewed'],1)
        self.data.review(NODE,EVENT)
        self.data.review(NODE,EVENT)
        reopened=DashboardData(self.path)
        d=reopened.snapshot('2026-11-15','2026-11-16',NODE)
        self.assertEqual(d['alert_counts']['unreviewed'],0)
        self.assertEqual(d['alerts'][0]['ack_state'],'queued')
        self.data.review(NODE,EVENT,False)
        self.assertEqual(self.snapshot()['alert_counts']['unreviewed'],1)
        with self.assertRaises(LookupError):self.data.review(NODE,'f'*24)

    def test_concurrent_writer_remains_usable_and_csv_has_all_rows(self):
        rows=list(self.data.export_rows('2026-11-15','2026-11-16',NODE))
        self.assertEqual(len(rows),2)
        s=Store(self.path)
        s.record_measurement(NODE,3,{'temperature':20})
        s.close()
        self.assertEqual(self.snapshot()['latest']['temperature'],20)


class HTTPTests(Fixture):
    def setUp(self):
        super().setUp()
        self.server=make_server(self.path,0)
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True)
        self.thread.start()
        self.url=f'http://127.0.0.1:{self.server.server_port}'

    def tearDown(self):
        self.server.shutdown();self.server.server_close();self.thread.join()
        super().tearDown()

    def test_html_json_and_csv_are_served(self):
        with urlopen(self.url) as r:
            self.assertEqual(r.status,200)
            self.assertIn('Cerro Seguro',r.read().decode())
            self.assertIn("default-src 'self'",r.headers['Content-Security-Policy'])
        with urlopen(self.url+'/api/dashboard?since=2026-11-15T00:00:00Z&until=2026-11-16T00:00:00Z&node=!1630f9c9') as r:
            self.assertEqual(json.load(r)['statistics']['samples'],2)
        with urlopen(self.url+'/api/export.csv?since=2026-11-15T00:00:00Z&until=2026-11-16T00:00:00Z') as r:
            text=r.read().decode('utf-8-sig')
            self.assertEqual(len(text.strip().splitlines()),3)
            self.assertIn('temperature',text)

    def test_invalid_ranges_nodes_and_paths(self):
        for path,code in [('/api/dashboard?hours=nan',400),('/api/dashboard?node=invalid',400),
                          ('/api/dashboard?since=2026-11-15',400),('/../../station/store.py',404)]:
            with self.subTest(path=path),self.assertRaises(HTTPError) as e:urlopen(self.url+path)
            self.assertEqual(e.exception.code,code)

    def test_review_api_and_cross_origin_rejection(self):
        body=json.dumps({'node':'!1630f9c9','event_id':EVENT,'reviewed':True}).encode()
        request=Request(self.url+'/api/alerts/review',data=body,headers={'Content-Type':'application/json'},method='POST')
        with urlopen(request) as r:self.assertTrue(json.load(r)['reviewed'])
        self.assertEqual(self.snapshot()['alert_counts']['unreviewed'],0)
        request.add_header('Origin','http://another-site.example')
        with self.assertRaises(HTTPError) as e:urlopen(request)
        self.assertEqual(e.exception.code,403)


if __name__=='__main__':unittest.main()

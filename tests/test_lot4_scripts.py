"""Calculation scripts added in LOT 4: hand-checked values and error handling."""
import json
import math
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT, load_module, run_script

REORDER = load_module(ROOT / "restock-alert" / "scripts" / "reorder.py", "lot4_reorder")
SOS = load_module(ROOT / "share-of-shelf" / "scripts" / "sos.py", "lot4_sos")
MAP = load_module(ROOT / "minimum-advertised-price" / "scripts" / "map_check.py", "lot4_map")
PRICE = load_module(ROOT / "walmart-price-tracker" / "scripts" / "price_index.py", "lot4_price")
FEED = load_module(ROOT / "ecommerce-feed-management" / "scripts" / "feed_check.py", "lot4_feed")
UPTIME = load_module(ROOT / "api-monitoring" / "scripts" / "uptime.py", "lot4_uptime")


class Reorder(unittest.TestCase):
    def test_textbook_values(self):
        # d=10/day, sd=3, L=16 days, no lead-time variability, 95% -> Z=1.645
        r = REORDER.analyze(REORDER.SkuInput(sku="A", daily_demand=10, demand_std=3, lead_time_days=16, on_hand=150))
        sigma = 3 * math.sqrt(16)                      # 12
        self.assertEqual(r["safety_stock"], math.ceil(1.6449 * sigma))          # 20
        self.assertEqual(r["reorder_point"], math.ceil(160 + 1.6449 * sigma))   # 180
        self.assertEqual(r["status"], "REORDER NOW")
        self.assertAlmostEqual(r["stockout_risk"], 1 - REORDER.NORMAL.cdf((150 - 160) / 12), places=3)
        self.assertEqual(r["days_of_cover"], 15.0)

    def test_lead_time_variability_and_moq(self):
        r = REORDER.analyze(REORDER.SkuInput(sku="B", daily_demand=10, demand_std=0, lead_time_days=10,
                                             lead_time_std_days=2, on_hand=0, moq=500, order_multiple=50))
        self.assertEqual(r["safety_stock"], math.ceil(1.6449 * 20))  # sigma = d * sL = 20
        self.assertGreaterEqual(r["order_quantity"], 500)
        self.assertEqual(r["order_quantity"] % 50, 0)

    def test_history_and_ok_status(self):
        r = REORDER.analyze(REORDER.SkuInput(sku="C", sales_history=[2, 4, 3, 3], lead_time_days=7, on_hand=500))
        self.assertEqual(r["daily_demand"], 3)
        self.assertEqual(r["status"], "OK")
        self.assertEqual(r["order_quantity"], 0)

    def test_invalid_input(self):
        r = run_script(ROOT / "restock-alert", "reorder.py", '{"sku": "X", "lead_time_days": 5}')
        self.assertEqual(r.returncode, 1)
        self.assertIn("daily_demand or sales_history", r.stdout)
        r = run_script(ROOT / "restock-alert", "reorder.py", '{"sku": "X", "daily_demand": 1, "lead_time_days": 5, "bogus": 1}')
        self.assertIn("unknown field(s): bogus", r.stdout)


class ShareOfShelf(unittest.TestCase):
    def test_counts_and_weighting(self):
        data = {"brand": "A", "top_n": 4, "results": [
            {"keyword": "k", "rank": 1, "brand": "A", "sponsored": True},
            {"keyword": "k", "rank": 2, "brand": "B", "sponsored": False},
            {"keyword": "k", "rank": 3, "brand": "A", "sponsored": False},
            {"keyword": "k", "rank": 4, "brand": "C", "sponsored": False},
            {"keyword": "k", "rank": 5, "brand": "A", "sponsored": False},   # beyond top_n, ignored
        ]}
        m = SOS.analyze(data)["overall"]
        self.assertEqual(m["listings"], 4)
        self.assertAlmostEqual(m["share_of_shelf"], 0.5)
        self.assertAlmostEqual(m["organic_share"], 1 / 3)
        self.assertAlmostEqual(m["paid_share"], 1.0)
        self.assertAlmostEqual(m["weighted_share"], (1 + 1 / 3) / (1 + 1 / 2 + 1 / 3 + 1 / 4))
        self.assertTrue(m["top3_presence"])

    def test_missing_field(self):
        with self.assertRaises(ValueError):
            SOS.analyze({"brand": "A", "results": [{"keyword": "k", "brand": "A"}]})


class MapCheck(unittest.TestCase):
    def test_violations_severity_and_steps(self):
        data = {"map_prices": {"S": 100.0}, "observations": [
            {"sku": "S", "seller": "X", "price": 97}, {"sku": "S", "seller": "X", "price": 90},
            {"sku": "S", "seller": "X", "price": 80}, {"sku": "S", "seller": "Y", "price": 99.995},
            {"sku": "S", "seller": "Z", "price": 100}, {"sku": "T", "seller": "Z", "price": 1}]}
        r = MAP.check(data)
        self.assertEqual([v["severity"] for v in r["violations"]], ["minor", "major", "severe"])
        self.assertEqual(r["sellers"][0]["seller"], "X")
        self.assertEqual(r["sellers"][0]["next_step"], MAP.STEPS[3])
        self.assertEqual(r["skus_without_map"], ["T"])  # tolerance keeps Y compliant
        self.assertAlmostEqual(r["compliance_rate"], 0.5)


class PriceIndex(unittest.TestCase):
    def test_landed_price_index_and_changes(self):
        rows = PRICE.analyze({"items": [{"item_id": "1", "my_price": 20, "my_shipping": 0,
                                         "competitors": [{"seller": "a", "price": 18, "shipping": 2}, {"seller": "b", "price": 25}],
                                         "history": [{"date": "2026-01-01", "price": 22}, {"date": "2026-01-05", "price": 20}]}]})
        r = rows[0]
        self.assertEqual(r["lowest_landed"], 20.0)
        self.assertEqual(r["index_vs_lowest"], 100.0)
        self.assertEqual(r["median_landed"], 22.5)
        self.assertEqual(r["position"], "below market")  # 20 / 22.5 = 88.9
        self.assertEqual(r["price_changes"][0]["change_pct"], -9.1)


class FeedCheck(unittest.TestCase):
    def test_gtin_check_digit(self):
        self.assertTrue(FEED.gtin_valid("4006381333931"))   # EAN-13 example with valid check digit
        self.assertTrue(FEED.gtin_valid("036000291452"))    # UPC-A example
        self.assertFalse(FEED.gtin_valid("4006381333932"))
        self.assertFalse(FEED.gtin_valid("12345"))

    def test_demo_feed_findings(self):
        r = FEED.analyze(FEED.DEMO)
        self.assertEqual(r["products"], 3)
        self.assertEqual(r["with_errors"], 2)
        self.assertIn("duplicate id", r["error_types"])
        self.assertIn("invalid availability", r["error_types"])

    def test_csv_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "feed.csv"
            path.write_text("id,title,description,link,image_link,availability,price,brand,mpn\n"
                            "A,Good title,Desc,https://x.com/a,https://x.com/a.jpg,in_stock,10.00 USD,Acme,M1\n")
            r = run_script(ROOT / "ecommerce-feed-management", "feed_check.py", str(path), "--json")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertEqual(json.loads(r.stdout)["with_errors"], 0)


class Uptime(unittest.TestCase):
    def test_error_budget(self):
        r = UPTIME.analyze({"period_days": 30, "slo": 0.999,
                            "incidents": [{"start": "2026-01-01T00:00:00", "end": "2026-01-01T00:30:00"}]})
        self.assertAlmostEqual(r["error_budget_minutes"], 43.2)
        self.assertEqual(r["downtime_minutes"], 30.0)
        self.assertEqual(r["mttr_minutes"], 30.0)
        self.assertTrue(r["slo_met"])

    def test_percentiles_nearest_rank(self):
        self.assertEqual(UPTIME.percentile(list(range(1, 101)), 95), 95)
        self.assertEqual(UPTIME.percentile([5], 99), 5)

    def test_bad_incident(self):
        with self.assertRaises(ValueError):
            UPTIME.analyze({"incidents": [{"start": "2026-01-02T00:00:00", "end": "2026-01-01T00:00:00"}]})


if __name__ == "__main__":
    unittest.main()

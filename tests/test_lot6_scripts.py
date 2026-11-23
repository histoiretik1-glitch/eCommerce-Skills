"""Platform calculation scripts added in LOT 6: hand-checked values and error handling."""
import json
import math
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT, load_module, run_script

SOLD = load_module(ROOT / "ebay-product-research" / "scripts" / "sold_analysis.py", "lot6_sold")
PL = load_module(ROOT / "ebay-advertising" / "scripts" / "promoted_listings.py", "lot6_pl")
WC = load_module(ROOT / "walmart-advertising-strategy" / "scripts" / "connect_report.py", "lot6_wc")
AB = load_module(ROOT / "shopify-ab-testing" / "scripts" / "ab_test.py", "lot6_ab")
KPI = load_module(ROOT / "shopify-analytics-guide" / "scripts" / "orders_kpis.py", "lot6_kpi")
LIVE = load_module(ROOT / "tiktok-live-selling" / "scripts" / "live_metrics.py", "lot6_live")
TITLE = load_module(ROOT / "ebay-seo" / "scripts" / "title_check.py", "lot6_title")


class EbaySoldAnalysis(unittest.TestCase):
    DATA = {"item": "Test lens", "period_days": 30, "active_listings": 15,
            "sold": [{"price": 100}, {"price": 110, "shipping": 10}, {"price": 140}, {"price": 160}, {"price": 170, "shipping": 10}],
            "final_value_rate": 0.136, "per_order_fee": 0.40, "item_cost": 50, "shipping_cost": 10}

    def test_hand_checked(self):
        r = SOLD.analyze(self.DATA)
        self.assertEqual(r["sell_through_rate"], 0.25)            # 5 / (5 + 15)
        self.assertEqual((r["sold_total_q1"], r["sold_total_median"], r["sold_total_q3"]), (120, 140, 160))
        self.assertEqual(r["fee_at_median"], 19.44)               # 0.136 * 140 + 0.40
        self.assertEqual(r["net_per_sale_at_median"], 60.56)      # 140 - 19.44 - 50 - 10
        self.assertEqual(r["sales_per_day"], 0.17)
        self.assertEqual(r["competition"], "high supply vs demand")

    def test_rejects_percent_rate_and_missing_fees(self):
        with self.assertRaises(ValueError):
            SOLD.analyze({**self.DATA, "final_value_rate": 13.6})
        bad = dict(self.DATA)
        del bad["per_order_fee"]
        with self.assertRaises(ValueError):
            SOLD.analyze(bad)

    def test_cli(self):
        p = run_script(ROOT / "ebay-product-research", "sold_analysis.py", json.dumps(self.DATA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("25.0%", p.stdout)
        self.assertEqual(run_script(ROOT / "ebay-product-research", "sold_analysis.py").returncode, 2)


class EbayPromotedListings(unittest.TestCase):
    def test_break_even_and_actions(self):
        r = PL.analyze({"price_total": 50, "profit_before_ads": 10, "conversion_rate": 0.02, "listings": [
            {"listing": "A", "campaign": "general", "ad_rate": 0.25, "clicks": 100, "impressions": 4000, "sold": 2, "sales": 100, "ad_fees": 25},
            {"listing": "B", "campaign": "priority", "clicks": 50, "impressions": 2000, "sold": 0, "sales": 0, "ad_fees": 12},
            {"listing": "C", "campaign": "general", "ad_rate": 0.05, "clicks": 80, "impressions": 3000, "sold": 3, "sales": 150, "ad_fees": 7.5}]})
        self.assertEqual(r["break_even_ad_rate"], 0.2)
        self.assertEqual(r["max_cpc_priority"], 0.2)
        a, b, c = r["listings"]
        self.assertEqual((a["roas"], a["profit_after_ads"]), (4.0, -5.0))
        self.assertIn("below break-even", a["action"])
        self.assertIn("pause", b["action"])
        self.assertEqual((c["ctr"], c["conversion"], c["profit_after_ads"]), (0.0267, 0.0375, 22.5))
        self.assertTrue(c["action"].startswith("keep"))

    def test_unknown_field(self):
        with self.assertRaises(ValueError):
            PL.analyze({"price_total": 50, "profit_before_ads": 10, "listings": [{"cost": 3}]})


class WalmartConnect(unittest.TestCase):
    def test_decisions(self):
        rows = [{"keyword": "k1", "clicks": 100, "impressions": 5000, "ad_spend": 50, "attributed_sales": 500, "units": 10},
                {"keyword": "k2", "clicks": 100, "ad_spend": 200, "attributed_sales": 500},
                {"keyword": "k3", "clicks": 10, "ad_spend": 8, "attributed_sales": 0},
                {"keyword": "k4", "clicks": 50, "ad_spend": 40, "attributed_sales": 0},
                {"keyword": "k5", "clicks": 60, "ad_spend": 25, "attributed_sales": 100}]
        r = WC.analyze({"margin_before_ads": 0.30, "rows": rows})
        self.assertEqual(r["summary"]["target_acos"], 0.2)        # 2/3 of 30%
        self.assertEqual(r["summary"]["target_roas"], 5.0)
        self.assertEqual([x["decision"] for x in r["rows"]],
                         ["raise bid / scale", "lower bid", "collect more data", "pause or add as negative keyword", "keep"])
        k1 = r["rows"][0]
        self.assertEqual((k1["ctr"], k1["cpc"], k1["conversion"], k1["roas"], k1["acos"]), (0.02, 0.5, 0.1, 10.0, 0.1))
        self.assertEqual(r["summary"]["total_spend"], 323.0)
        self.assertEqual(r["summary"]["total_acos"], round(323 / 1100, 4))

    def test_margin_must_be_fraction(self):
        with self.assertRaises(ValueError):
            WC.analyze({"margin_before_ads": 30, "rows": []})


class ShopifyAbTest(unittest.TestCase):
    def test_sample_size_textbook(self):
        # 5% -> 6%, alpha 0.05 two-sided, power 0.8: about 8,158 per group (standard reference value)
        r = AB.plan({"baseline_rate": 0.05, "min_relative_lift": 0.2, "daily_sessions": 1000})
        self.assertTrue(8150 <= r["sessions_per_variant"] <= 8165, r)
        self.assertEqual(r["days"], math.ceil(r["total_sessions"] / 1000))
        short = AB.plan({"baseline_rate": 0.05, "min_relative_lift": 0.5, "daily_sessions": 100000})
        self.assertEqual(short["days"], 14)  # floor of two weekly cycles

    def test_z_test(self):
        r = AB.analyze({"control": {"sessions": 10000, "orders": 200}, "variant": {"sessions": 10000, "orders": 250}})
        se = math.sqrt(0.0225 * 0.9775 * (2 / 10000))
        self.assertAlmostEqual(r["z"], round(0.005 / se, 3), places=3)   # 2.384
        self.assertAlmostEqual(r["p_value"], 0.0171, places=3)
        self.assertTrue(r["significant"])
        self.assertEqual(r["srm_p_value"], 1.0)
        self.assertLess(r["ci95_difference"][0], 0.005)

    def test_srm_detected(self):
        r = AB.analyze({"control": {"sessions": 10000, "orders": 200}, "variant": {"sessions": 9000, "orders": 200}})
        self.assertTrue(r["srm_detected"])
        p = run_script(ROOT / "shopify-ab-testing", "ab_test.py",
                       json.dumps({"mode": "analyze", "control": {"sessions": 10000, "orders": 200},
                                   "variant": {"sessions": 9000, "orders": 200}}))
        self.assertIn("STOP", p.stdout)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            AB.analyze({"control": {"sessions": 10, "orders": 20}, "variant": {"sessions": 10, "orders": 1}})
        self.assertEqual(run_script(ROOT / "shopify-ab-testing", "ab_test.py", '{"mode": "x"}').returncode, 1)


class ShopifyOrdersKpis(unittest.TestCase):
    CSV = ("Name,Email,Financial Status,Created at,Subtotal,Total,Discount Amount,Refunded Amount,Lineitem name\n"
           "#1001,a@x.com,paid,2026-09-03 10:00:00 -0400,90,100,10,0,Mug\n"
           "#1001,,,,,,,,Spoon\n"
           "#1002,b@x.com,paid,2026-09-20 10:00:00 -0400,50,60,0,0,Mug\n"
           "#1003,A@x.com,partially_refunded,2026-10-02 10:00:00 -0400,40,50,0,20,Bowl\n"
           "#1004,c@x.com,voided,2026-10-05 10:00:00 -0400,30,35,0,0,Cup\n"
           "#1005,,paid,2026-10-09 10:00:00 -0400,80,90,0,0,Tray\n")

    def test_kpis(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "orders.csv"
            path.write_text(self.CSV, encoding="utf-8")
            k = KPI.kpis(KPI.load_orders(path))
            p = run_script(ROOT / "shopify-analytics-guide", "orders_kpis.py", str(path))
        self.assertEqual((k["orders"], k["excluded_voided"]), (4, 1))
        self.assertEqual((k["gross_revenue"], k["refunds"], k["net_revenue"]), (300.0, 20.0, 280.0))
        self.assertEqual(k["aov"], 75.0)
        self.assertEqual(k["aov_merchandise"], 65.0)                            # (90 + 50 + 40 + 80) / 4
        self.assertEqual((k["customers"], k["orders_without_email"]), (2, 1))   # a@ and A@ are the same customer
        self.assertEqual(k["repeat_customer_rate"], 0.5)
        self.assertEqual(k["discount_rate"], round(10 / 270, 4))
        self.assertEqual(k["revenue_by_month"], {"2026-09": 160.0, "2026-10": 140.0})
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn("@", p.stdout)  # emails never printed

    def test_not_an_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.csv"
            path.write_text("a,b\n1,2\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                KPI.load_orders(path)


class TiktokLive(unittest.TestCase):
    def test_metrics_and_ranking(self):
        r = LIVE.analyze({"sessions": [
            {"date": "d1", "start_hour": 12, "duration_min": 60, "views": 8000, "orders": 20, "gmv": 800},
            {"date": "d2", "start_hour": 19, "duration_min": 120, "views": 10000, "orders": 50, "gmv": 2000,
             "product_impressions": 5000, "product_clicks": 400, "comments": 600, "new_followers": 90}]})
        top, low = r["sessions"]
        self.assertEqual(top["date"], "d2")
        self.assertEqual((top["gpm"], top["gmv_per_hour"], top["product_ctr"], top["click_to_order"], top["aov"]),
                         (200.0, 1000.0, 0.08, 0.125, 40.0))
        self.assertEqual((top["comments_per_1k_views"], top["followers_per_hour"]), (60.0, 45.0))
        self.assertEqual(low["gpm"], 100.0)
        self.assertIsNone(low["product_ctr"])
        self.assertEqual(r["medians"]["gpm"], 150.0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            LIVE.analyze({"sessions": [{"date": "d", "duration_min": 0, "views": 10, "orders": 1, "gmv": 5}]})
        with self.assertRaises(ValueError):
            LIVE.analyze({"sessions": [{"date": "d", "views": 10, "orders": 1, "gmv": 5, "likes": 3}]})


class EbayTitleCheck(unittest.TestCase):
    def test_flags_problems(self):
        r = TITLE.check({"title": "VINTAGE CAMERA canon ae1 program WORKS GREAT!! L@@K camera",
                         "keywords": ["35mm", "film camera"], "specifics": {"Brand": "Canon", "Color": ""},
                         "recommended_specifics": ["Brand", "Color", "Format", "Model"]})
        self.assertFalse(r["pass"])
        self.assertEqual(r["missing_keywords"], ["35mm", "film camera"])
        self.assertEqual(r["repeated_words"], ["camera"])
        self.assertEqual(r["all_caps"], ["VINTAGE", "CAMERA", "WORKS"])
        self.assertIn("l@@k", r["filler_or_symbols"])
        self.assertIn("!", r["filler_or_symbols"])
        self.assertEqual(r["empty_recommended_specifics"], ["Color", "Format", "Model"])
        self.assertEqual(r["specifics_completion"], 0.25)

    def test_clean_title_and_length(self):
        title = "Canon AE-1 Program 35mm SLR Film Camera Body Black Tested Working"
        r = TITLE.check({"title": title, "keywords": ["canon ae-1", "35mm", "film camera"]})
        self.assertTrue(r["pass"], r["issues"])
        self.assertEqual((r["length"], r["unused_characters"]), (65, 15))
        long = TITLE.check({"title": "x" * 81})
        self.assertIn("over the 80 limit", long["issues"][0])

    def test_unknown_field(self):
        self.assertEqual(run_script(ROOT / "ebay-seo", "title_check.py", '{"title": "a", "tags": []}').returncode, 1)


if __name__ == "__main__":
    unittest.main()

"""Cross-platform calculation scripts added in LOT 7: hand-checked values and error handling."""
import json
import math
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT, load_module, run_script

SALES = load_module(ROOT / "sales-tracking-tool" / "scripts" / "sales_report.py", "lot7_sales")
COH = load_module(ROOT / "ecommerce-customer-retention" / "scripts" / "cohorts.py", "lot7_cohorts")
SHIP = load_module(ROOT / "ecommerce-shipping-rates" / "scripts" / "shipping_quote.py", "lot7_ship")
RET = load_module(ROOT / "ecommerce-returns-management" / "scripts" / "returns_cost.py", "lot7_returns")
SUB = load_module(ROOT / "ecommerce-subscription-model" / "scripts" / "subscription_economics.py", "lot7_sub")
DROP = load_module(ROOT / "dropshipping-product-research" / "scripts" / "dropship_score.py", "lot7_drop")
REV = load_module(ROOT / "ecommerce-ab-testing" / "scripts" / "revenue_test.py", "lot7_rev")
BUCK = load_module(ROOT / "google-shopping-optimization" / "scripts" / "product_buckets.py", "lot7_buckets")


def write(tmp, name, text):
    p = Path(tmp) / name
    p.write_text(text, encoding="utf-8")
    return p


class SalesReport(unittest.TestCase):
    CSV = ("date,channel,sku,units,revenue,cost,fees,ad_spend\n"
           "2026-09-01,amazon,A,10,200,60,30,10\n2026-09-15,shopify,A,5,100,30,3,0\n"
           "2026-10-01,amazon,B,4,40,30,6,20\n2026-10-02,shopify,A,10,200,60,6,4\n")

    def test_channels_skus_growth(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = SALES.report_data(SALES.load(write(tmp, "s.csv", self.CSV), "month"), 10)
        self.assertEqual(d["by_channel"]["amazon"]["revenue"], 240.0)
        self.assertEqual(d["by_channel"]["amazon"]["contribution"], 84.0)        # 240 - 90 - 36 - 30
        self.assertEqual(d["by_channel"]["shopify"]["contribution_margin"], round(197 / 300, 4))
        self.assertEqual(d["last_period_growth"], round((240 - 300) / 300, 4))
        self.assertEqual(d["loss_making_skus"], ["B"])                          # 40 - 30 - 6 - 20 < 0
        self.assertEqual(d["top_skus"]["A"]["asp"], 20.0)

    def test_weeks_and_missing_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = SALES.report_data(SALES.load(write(tmp, "s.csv", self.CSV), "week"), 10)
            self.assertEqual(d["periods"][0], "2026-W36")
            with self.assertRaises(ValueError):
                SALES.load(write(tmp, "bad.csv", "date,sku,units\n2026-01-01,A,1\n"), "month")


class Cohorts(unittest.TestCase):
    CSV = ("customer_id,order_date,revenue\nA,2026-01-05,10\nA,2026-02-03,20\nB,2026-01-20,30\n"
           "C,2026-02-10,40\nC,2026-02-25,5\nC,2026-04-01,15\n")

    def test_matrix(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = COH.analyze(COH.load(write(tmp, "o.csv", self.CSV)), months=3)
        jan, feb = r["cohorts"]["2026-01"], r["cohorts"]["2026-02"]
        self.assertEqual(jan["customers"], 2)
        self.assertEqual(jan["active_share_by_month"], [1.0, 0.5, 0.0, 0.0])
        self.assertEqual(jan["cumulative_revenue_per_customer"][-1], 30.0)       # (10 + 20 + 30) / 2
        self.assertEqual(feb["active_share_by_month"], [1.0, 0.0, 1.0])         # April = M2, last month in data
        self.assertEqual(r["repeat_purchase_rate"], round(2 / 3, 4))
        self.assertEqual(r["median_days_to_second_order"], 22)                 # A: 29 days, C: 15 days

    def test_bad_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                COH.load(write(tmp, "x.csv", "id,date\n1,2026-01-01\n"))


class Shipping(unittest.TestCase):
    def test_dim_weight(self):
        r = SHIP.quote({"package": {"length": 14, "width": 10, "height": 6, "weight": 2.2}, "order_value": 50,
                        "carriers": [{"name": "A", "dim_divisor": 139, "rates": [[3, 9.0], [7, 14.0], [10, 18.0]]},
                                     {"name": "B", "dim_divisor": 166, "rates": [[3, 8.0], [6, 13.0]]}]})
        a, b = r["quotes"]
        self.assertEqual((a["dim_weight"], a["billable_weight"], a["price"]), (6.04, 7, 14.0))   # 840 / 139
        self.assertEqual((b["billable_weight"], b["price"]), (6, 13.0))                         # 840 / 166 = 5.06
        self.assertEqual(r["cheapest"], "B")
        self.assertEqual(b["share_of_order"], 0.26)
        self.assertEqual(a["max_box_volume_without_dim"], 417.0)                               # 3 lb x 139

    def test_metric_and_over_table(self):
        r = SHIP.quote({"package": {"length": 40, "width": 30, "height": 20, "weight": 3.2, "unit": "cm/kg"},
                        "carriers": [{"name": "EU", "dim_divisor": 5000, "rates": [[4, 7.0], [5, 8.0]]}]})
        q = r["quotes"][0]
        self.assertEqual((q["dim_weight"], q["billable_weight"], q["price"]), (4.8, 5.0, 8.0))
        r2 = SHIP.quote({"package": {"length": 60, "width": 40, "height": 40, "weight": 1, "unit": "cm/kg"},
                         "carriers": [{"name": "EU", "dim_divisor": 5000, "rates": [[5, 8.0]]}]})
        self.assertIsNone(r2["quotes"][0]["price"])


class Returns(unittest.TestCase):
    def test_costs(self):
        r = RET.analyze({"skus": [{"sku": "D", "units_sold": 400, "units_returned": 72, "price": 59, "unit_cost": 18,
                                   "return_shipping": 7.5, "processing_cost": 3, "resellable_share": 0.8,
                                   "reasons": {"too small": 30, "changed mind": 24, "not as pictured": 18}}]})
        s = r["skus"][0]
        self.assertEqual((s["return_rate"], s["cost_per_return"], s["returns_cost"]), (0.18, 14.1, 1015.2))
        self.assertEqual(s["net_margin"], 12432.8)                     # 328 x 41 - 1015.2
        self.assertEqual((s["top_reason"], s["top_reason_share"]), ("too small", round(30 / 72, 4)))
        self.assertTrue(s["alert"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            RET.analyze({"skus": [{"sku": "X", "units_sold": 5, "units_returned": 6, "price": 1, "unit_cost": 1}]})


class Subscription(unittest.TestCase):
    def test_economics(self):
        r = SUB.analyze({"price": 32, "cogs": 9.5, "fulfillment": 6, "payment_fee_rate": 0.03, "monthly_churn": 0.09,
                         "cac": 45, "horizon_months": 24})
        self.assertEqual(r["contribution_per_order"], 15.54)            # 32 x 0.97 - 15.5
        self.assertEqual(r["cac_payback_months"], 4)
        expected = sum(15.54 * 0.91 ** m for m in range(24))
        self.assertAlmostEqual(r["ltv_capped"], round(expected, 2), places=1)
        self.assertEqual(r["ltv_uncapped"], round(15.54 / 0.09, 2))
        self.assertEqual(r["max_churn_for_ltv_cac_3"], round(15.54 / 135, 4))

    def test_churn_fraction(self):
        with self.assertRaises(ValueError):
            SUB.analyze({"price": 32, "cogs": 9, "monthly_churn": 9, "cac": 45})


class Dropship(unittest.TestCase):
    def test_score(self):
        rows = DROP.evaluate({"products": [{"name": "mat", "price": 40, "supplier_cost": 12, "shipping_cost": 4,
                                            "shipping_days": 6, "return_risk": "low", "expected_cpa": 10}]})
        r = rows[0]
        contrib = 40 - 16 - (40 * 0.029 + 0.30) - 1.2
        self.assertEqual(r["max_cpa"], round(contrib, 2))
        self.assertEqual(r["break_even_roas"], round(40 / contrib, 2))
        self.assertEqual(r["score"], 100.0)                              # margin 60%, fast, low risk, profitable
        self.assertEqual(r["verdict"], "test")

    def test_reject_and_bad_risk(self):
        r = DROP.evaluate({"products": [{"name": "x", "price": 10, "supplier_cost": 9, "shipping_cost": 3}]})[0]
        self.assertTrue(r["verdict"].startswith("reject"))
        with self.assertRaises(ValueError):
            DROP.evaluate({"products": [{"name": "x", "price": 10, "supplier_cost": 1, "return_risk": "none"}]})


class RevenueTest(unittest.TestCase):
    def test_welch_and_bonferroni(self):
        r = REV.analyze({"variants": [
            {"name": "A", "visitors": 12000, "conversions": 312, "revenue": 18720, "revenue_sd": 14.2},
            {"name": "B", "visitors": 11950, "conversions": 345, "revenue": 19320, "revenue_sd": 13.6},
            {"name": "C", "visitors": 12030, "conversions": 360, "revenue": 21240, "revenue_sd": 15.1}]})
        self.assertEqual(r["adjusted_alpha"], 0.025)
        b = r["variants"][0]
        se = math.sqrt(14.2 ** 2 / 12000 + 13.6 ** 2 / 11950)
        z = (19320 / 11950 - 1.56) / se
        self.assertAlmostEqual(b["rpv_p"], round(2 * (1 - REV.N.cdf(abs(z))), 4), places=4)
        self.assertEqual(b["decision"], "no significant difference")

    def test_revenue_sq_and_winner(self):
        # 10,000 visitors each; control mean 1.0 sd ~5, variant mean 1.5 -> clear winner
        r = REV.analyze({"variants": [
            {"name": "A", "visitors": 10000, "conversions": 200, "revenue": 10000, "revenue_sq": 10000 * (25 + 1)},
            {"name": "B", "visitors": 10000, "conversions": 260, "revenue": 15000, "revenue_sq": 10000 * (25 + 2.25)}]})
        self.assertEqual(r["variants"][0]["decision"], "winner on revenue")
        with self.assertRaises(ValueError):
            REV.analyze({"variants": [{"name": "A", "visitors": 10, "conversions": 1, "revenue": 5},
                                      {"name": "B", "visitors": 10, "conversions": 1, "revenue": 5}]})


class ProductBuckets(unittest.TestCase):
    def test_buckets(self):
        r = BUCK.bucket({"target_roas": 4, "min_clicks": 100, "products": [
            {"id": "h", "clicks": 820, "cost": 410, "conversions": 41, "conv_value": 2050},
            {"id": "s", "clicks": 150, "cost": 90, "conversions": 6, "conv_value": 390},
            {"id": "v", "clicks": 640, "cost": 352, "conversions": 18, "conv_value": 720},
            {"id": "z", "clicks": 35, "cost": 17.5, "conversions": 1, "conv_value": 24}]})
        self.assertEqual([p["bucket"] for p in r["products"]], ["hero", "sidekick", "villain", "zombie"])
        self.assertEqual(r["products"][0]["roas"], 5.0)
        self.assertEqual(r["buckets"]["villain"]["roas"], round(720 / 352, 2))

    def test_cli(self):
        p = run_script(ROOT / "google-shopping-optimization", "product_buckets.py", json.dumps({"target_roas": 3, "products": []}))
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertEqual(run_script(ROOT / "google-shopping-optimization", "product_buckets.py", "{}").returncode, 1)


if __name__ == "__main__":
    unittest.main()

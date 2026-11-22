"""supply-chain-optimization, brand-protection and review-checker: platform awareness + Amazon regression."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT, golden, load_module, run_script, strip_dates

SC = ROOT / "supply-chain-optimization"
BP = ROOT / "brand-protection"
RC = ROOT / "review-checker"

SC_INPUT = {"product_cost": 5, "supplier_payment_days": 0, "production_days": 20,
            "shipping_cost_per_unit": 0.6, "shipping_days": 30, "selling_price": 19.99,
            "fulfillment_fee": 3.5, "storage_fee": 0.2, "ad_spend_ratio": 0.08,
            "inventory_days": 40, "has_long_term_storage": True}


class SupplyChain(unittest.TestCase):
    def test_amazon_output_unchanged(self):
        r = run_script(SC / "supply-chain-optimization-amazon", "calculator.py")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual(r.stdout, golden("supply_chain_amazon_default.txt"))

    def test_platform_defaults_from_folder(self):
        expected = {"amazon": (14, "FBA Fulfillment"), "shopify": (3, "3PL Fulfillment"),
                    "tiktok": (15, "FBT/Fulfillment"), "walmart": (14, "WFS Fulfillment")}
        for platform, (payout, label) in expected.items():
            d = SC / f"supply-chain-optimization-{platform}"
            m = load_module(d / "scripts" / "calculator.py", f"sc_{platform}")
            data = m.input_from_dict(SC_INPUT)
            self.assertEqual(data.platform, platform)
            self.assertEqual(data.payout_days, payout)
            r = run_script(d, "calculator.py", json.dumps(SC_INPUT))
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn(label, r.stdout)
            if platform != "amazon":
                self.assertNotIn("FBA", r.stdout, platform)

    def test_optional_platform_fees_reduce_profit(self):
        d = SC / "supply-chain-optimization-tiktok"
        m = load_module(d / "scripts" / "calculator.py", "sc_tiktok_fees")
        base = m.calculate_cost_breakdown(m.input_from_dict(SC_INPUT))
        fees = m.calculate_cost_breakdown(m.input_from_dict({**SC_INPUT, "referral_fee_rate": 0.08,
                                                              "affiliate_commission_rate": 0.15}))
        self.assertAlmostEqual(base["net_profit"] - fees["net_profit"], 19.99 * 0.23, places=1)

    def test_unknown_field_rejected(self):
        r = run_script(SC / "supply-chain-optimization-walmart", "calculator.py",
                       json.dumps({**SC_INPUT, "bogus": 1}))
        self.assertEqual(r.returncode, 1)
        self.assertIn("unknown field(s): bogus", r.stdout)

    def test_reports_generate_for_every_platform(self):
        for platform in ("amazon", "shopify", "tiktok", "walmart"):
            with tempfile.TemporaryDirectory() as tmp:
                d = Path(tmp) / f"supply-chain-optimization-{platform}"
                shutil.copytree(SC / d.name, d)
                for script, out in (("report_doc.py", "supply_chain_report.md"),
                                    ("report_html.py", "supply_chain_report.html")):
                    r = run_script(d, script, cwd=d / "scripts")
                    self.assertEqual(r.returncode, 0, r.stderr)
                    self.assertTrue((d / "scripts" / out).exists())
                md = (d / "scripts" / "supply_chain_report.md").read_text()
                if platform != "amazon":
                    self.assertNotIn("Amazon", md.split("Powered by")[0], platform)


class BrandProtection(unittest.TestCase):
    def test_amazon_outputs_unchanged(self):
        d = BP / "brand-protection-amazon"
        cases = {"all": [], "complaint": ["complaint"], "cease": ["cease"], "testbuy": ["testbuy"],
                 "map": ["map"], "zh": ["--zh"]}
        for name, args in cases.items():
            r = run_script(d, "templates.py", *args)
            self.assertEqual(strip_dates(r.stdout), strip_dates(golden(f"bp_templates_amazon_{name}.txt")), name)
        for lang, args in (("en", []), ("zh", ["--zh"])):
            r = run_script(d, "detector.py", *args)
            self.assertEqual(strip_dates(r.stdout), strip_dates(golden(f"bp_detector_amazon_{lang}.txt")), lang)

    def test_other_platforms_use_their_own_channel(self):
        channels = {"ebay": "VeRO", "shopify": "DMCA", "tiktok": "IP Protection Center", "walmart": "Brand Portal"}
        for platform, channel in channels.items():
            d = BP / f"brand-protection-{platform}"
            for script in ("templates.py", "detector.py"):
                out = run_script(d, script).stdout
                self.assertIn(channel, out, f"{platform} {script}")
                self.assertNotIn("Amazon", out, f"{platform} {script}")
                self.assertNotIn("Brand Registry", out, f"{platform} {script}")

    def test_documented_subcommands_produce_output(self):
        for platform, cmds in {"ebay": ["vero", "cease-desist", "testbuy"], "shopify": ["dmca", "platform-report"],
                               "tiktok": ["ip-report", "seller-complaint", "content-takedown"],
                               "walmart": ["brand-portal"], "amazon": ["cease-desist"]}.items():
            for cmd in cmds:
                r = run_script(BP / f"brand-protection-{platform}", "templates.py", cmd)
                self.assertEqual(r.returncode, 0, f"{platform} {cmd}")
                self.assertGreater(len(r.stdout.splitlines()), 20, f"{platform} {cmd}")

    def test_unknown_template_is_an_error(self):
        r = run_script(BP / "brand-protection-ebay", "templates.py", "nope")
        self.assertEqual(r.returncode, 1)
        self.assertIn("unknown template", r.stdout)


class ReviewChecker(unittest.TestCase):
    def test_amazon_output_unchanged(self):
        d = RC / "amazon-review-checker"
        self.assertEqual(run_script(d, "analyzer.py").stdout, golden("review_amazon_en.txt"))
        self.assertEqual(run_script(d, "analyzer.py", "--zh").stdout, golden("review_amazon_zh.txt"))

    def test_id_label_per_platform(self):
        for platform, label in (("amazon", "**ASIN**"), ("ebay", "**eBay Item ID**"), ("walmart", "**Walmart Item ID**")):
            out = run_script(RC / f"{platform}-review-checker", "analyzer.py").stdout
            self.assertIn(label, out)

    def test_walmart_alias_is_analyzed_not_replaced_by_demo(self):
        reviews = [{"content": "Solid storage bins, sturdy lids", "rating": 5, "date": "2026-01-02", "wfs_verified": True},
                   {"content": "Broke after a week", "rating": 1, "date": "2026-01-09", "wfs_verified": False}]
        r = run_script(RC / "walmart-review-checker", "analyzer.py", json.dumps(reviews))
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("Received free product", r.stdout)  # demo data marker

    def test_bad_json_fails_instead_of_using_demo_data(self):
        r = run_script(RC / "ebay-review-checker", "analyzer.py", '[{"content": "x", "nope": 1}]')
        self.assertEqual(r.returncode, 1)
        self.assertIn("unknown field(s): nope", r.stdout)
        r = run_script(RC / "ebay-review-checker", "analyzer.py", "[not json")
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()

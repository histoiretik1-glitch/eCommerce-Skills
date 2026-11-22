"""profit-margin-calculator: platform fee models, aliases, Amazon regression."""
import unittest

from helpers import ROOT, golden, load_module, run_script

FAMILY = ROOT / "profit-margin-calculator"
PLATFORMS = ("amazon", "shopify", "tiktok", "walmart")


def skill(platform):
    return FAMILY / f"profit-margin-calculator-{platform}"


def calc(platform):
    return load_module(skill(platform) / "scripts" / "calculator.py", f"profit_calc_{platform}")


class AmazonRegression(unittest.TestCase):
    """Amazon output must stay byte-identical to the pre-2.0 script (golden files)."""

    def test_default_report_unchanged(self):
        r = run_script(skill("amazon"), "calculator.py")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, golden("profit_amazon_default.txt"))

    def test_json_report_unchanged(self):
        r = run_script(skill("amazon"), "calculator.py",
                       '{"selling_price": 29.99, "product_cost": 6, "fba_fulfillment_fee": 5.5}')
        self.assertEqual(r.stdout, golden("profit_amazon_example.txt"))

    def test_documented_fba_fee_alias(self):
        r = run_script(skill("amazon"), "calculator.py",
                       '{"selling_price": 29.99, "product_cost": 6, "fba_fee": 5.5}')
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual(r.stdout, golden("profit_amazon_example.txt"))


class FeeModels(unittest.TestCase):
    def test_platform_detected_from_folder(self):
        for p in PLATFORMS:
            self.assertEqual(calc(p).detect_platform(), p)

    def test_shopify_has_no_commission_and_plan_payment_fees(self):
        m = calc("shopify")
        costs = m.calculate_costs(m.ProductInput(selling_price=100, product_cost=20))
        self.assertEqual(costs.referral_fee, 0)
        self.assertAlmostEqual(costs.payment_fee, 3.20)  # basic: 2.9% + $0.30
        grow = m.calculate_costs(m.ProductInput(selling_price=100, shopify_plan="grow"))
        self.assertAlmostEqual(grow.payment_fee, 3.00)   # 2.7% + $0.30
        third_party = m.calculate_costs(m.ProductInput(selling_price=100, uses_shopify_payments=False))
        self.assertAlmostEqual(third_party.payment_fee, 5.20)  # + 2% Shopify fee on Basic

    def test_tiktok_referral_and_affiliate(self):
        m = calc("tiktok")
        costs = m.calculate_costs(m.ProductInput(selling_price=100, affiliate_commission_rate=0.2,
                                                 affiliate_order_share=0.5))
        self.assertAlmostEqual(costs.referral_fee, 8.0)     # conservative US default
        self.assertAlmostEqual(costs.affiliate_fee, 10.0)   # 20% on half the orders
        jewelry = m.calculate_costs(m.ProductInput(selling_price=100, category="jewelry"))
        self.assertAlmostEqual(jewelry.referral_fee, 5.0)
        custom = m.calculate_costs(m.ProductInput(selling_price=100, referral_fee_rate=0.06))
        self.assertAlmostEqual(custom.referral_fee, 6.0)

    def test_tiktok_other_region_requires_explicit_rate(self):
        m = calc("tiktok")
        with self.assertRaises(ValueError):
            m.calculate_costs(m.ProductInput(selling_price=10, region="UK"))
        ok = m.calculate_costs(m.ProductInput(selling_price=10, region="UK", referral_fee_rate=0.09))
        self.assertAlmostEqual(ok.referral_fee, 0.90)

    def test_walmart_apparel_price_tiers(self):
        m = calc("walmart")
        rate = lambda price: m.get_referral_fee_rate("apparel", None, "walmart", price)
        self.assertEqual(rate(12), 0.05)
        self.assertEqual(rate(18), 0.10)
        self.assertEqual(rate(30), 0.15)
        self.assertEqual(m.get_referral_fee_rate("electronics", None, "walmart", 50), 0.08)

    def test_amazon_rates_unchanged(self):
        m = calc("amazon")
        self.assertEqual(m.get_referral_fee_rate("default"), 0.15)
        self.assertEqual(m.get_referral_fee_rate("electronics"), 0.08)

    def test_pricing_suggestions_hit_target_margin(self):
        for p in PLATFORMS:
            m = calc(p)
            product = m.ProductInput(selling_price=40, product_cost=10, fba_fulfillment_fee=4,
                                     ad_spend_ratio=0.1, affiliate_commission_rate=0.1 if p == "tiktok" else 0)
            for s in m.calculate_pricing_suggestions(product):
                check = m.ProductInput(**{**product.__dict__, "selling_price": s.suggested_price})
                margin = m.calculate_costs(check).net_margin
                self.assertAlmostEqual(margin, s.target_margin, delta=0.01, msg=p)


class InputHandling(unittest.TestCase):
    def test_documented_aliases(self):
        m = calc("tiktok")
        prod = m.product_from_dict({"selling_price": 10, "creator_commission_rate": 0.15, "fbt_fee": 3})
        self.assertEqual(prod.affiliate_commission_rate, 0.15)
        self.assertEqual(prod.fba_fulfillment_fee, 3)
        w = calc("walmart").product_from_dict({"selling_price": 10, "wfs_fee": 4.95})
        self.assertEqual(w.fba_fulfillment_fee, 4.95)

    def test_unknown_field_is_a_clear_error(self):
        r = run_script(skill("shopify"), "calculator.py", '{"selling_price": 10, "bogus": 1}')
        self.assertEqual(r.returncode, 1)
        self.assertIn("unknown field(s): bogus", r.stdout)

    def test_unknown_platform_rejected(self):
        with self.assertRaises(ValueError):
            calc("amazon").ProductInput(platform="etsy")

    def test_platform_labels_in_reports(self):
        expected = {"amazon": "FBA Fulfillment", "shopify": "Payment Processing",
                    "tiktok": "Affiliate Commission", "walmart": "WFS Fulfillment"}
        for p, label in expected.items():
            r = run_script(skill(p), "calculator.py")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn(label, r.stdout, p)
        shopify = run_script(skill("shopify"), "calculator.py").stdout
        self.assertNotIn("FBA", shopify)
        self.assertNotIn("Referral Fee", shopify)


if __name__ == "__main__":
    unittest.main()

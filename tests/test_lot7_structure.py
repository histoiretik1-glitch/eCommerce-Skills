"""The 29 cross-platform skills enriched in LOT 7: structure, no generic template left, no duplication
with the platform-specific skills, explicit hand-offs to neighbours, honest examples."""
import re
import unittest

from helpers import ROOT
from similarity import content_lines

GENERIC = [
    "affiliate-marketing-strategy", "competitor-price-tracker", "conversion-rate-optimization",
    "dropshipping-product-research", "ecommerce-ab-testing", "ecommerce-branding", "ecommerce-business-plan",
    "ecommerce-checkout-optimization", "ecommerce-customer-retention", "ecommerce-keyword-research",
    "ecommerce-landing-page", "ecommerce-personalization", "ecommerce-returns-management", "ecommerce-shipping-rates",
    "ecommerce-subscription-model", "ecommerce-video-marketing", "google-shopping-optimization", "influencer-outreach",
    "market-gap-analysis", "multichannel-ecommerce", "omnichannel-ecommerce", "product-launch-strategy",
    "product-page-seo", "product-title-optimization", "review-monitoring", "sales-tracking-tool", "shoppable-video",
    "social-media-monitor", "woocommerce-seo",
]
SECTIONS = ["Role and Scope", "Capabilities", "Principles and Constraints", "Data Needed", "Workflow",
            "Calculations and Tools", "Worked Example", "Example Requests", "Output Format", "Quality Checks",
            "Data Reliability"]
# Superficial template text that LOT 7 replaced; it must not come back in these skills
TEMPLATE = ["## How This Skill Works", "Collect information from the user's message",
            "Structured recommendations with actionable steps, benchmarks, and platform-specific guidance",
            "- Start with a summary of findings"]
SCRIPTS = {"sales-tracking-tool": "sales_report.py", "ecommerce-customer-retention": "cohorts.py",
           "ecommerce-shipping-rates": "shipping_quote.py", "ecommerce-returns-management": "returns_cost.py",
           "ecommerce-subscription-model": "subscription_economics.py", "dropshipping-product-research": "dropship_score.py",
           "ecommerce-ab-testing": "revenue_test.py", "google-shopping-optimization": "product_buckets.py"}
SAMPLES = {"sales-tracking-tool": "synthetic_sales.csv", "ecommerce-customer-retention": "synthetic_orders.csv"}
MAX_SHARED_WITH_ANY_SKILL = 0.15
PATHS = {p.parent.name: p for p in ROOT.rglob("SKILL.md") if "node_modules" not in p.parts and ".git" not in p.parts}
ALL_SKILLS = set(PATHS)


def text(name):
    return PATHS[name].read_text(encoding="utf-8")


def section(t, title):
    return t.split(f"\n## {title}\n", 1)[1].split("\n## ", 1)[0]


def new_content(name):
    t = text(name)
    start = t.index("## Principles and Constraints")
    ends = [t.find(h, start) for h in ("## Other Skills", "## Installation")]
    ends = [e for e in ends if e != -1]
    return t[start:min(ends) if ends else len(t)]


class Structure(unittest.TestCase):
    def test_sections_present_and_ordered(self):
        for name in GENERIC:
            headings = re.findall(r"^## (.+?)\s*$", text(name), re.M)
            with self.subTest(skill=name):
                for s in SECTIONS:
                    self.assertIn(s, headings)
                positions = [headings.index(s) for s in SECTIONS]
                self.assertEqual(positions, sorted(positions), "sections out of order")

    def test_method_requests_checks(self):
        for name in GENERIC:
            t = text(name)
            with self.subTest(skill=name):
                self.assertGreaterEqual(len(re.findall(r"^\d+\. ", section(t, "Workflow"), re.M)), 7)
                quotes = re.findall(r'^- "(.+)"$', section(t, "Example Requests"), re.M)
                self.assertGreaterEqual(len(quotes), 3)
                self.assertFalse(any("[" in q for q in quotes), "example requests must not be templates")
                self.assertGreaterEqual(len(re.findall(r"^- ", section(t, "Quality Checks"), re.M)), 5)
                self.assertGreaterEqual(len(re.findall(r"^- ", section(t, "Calculations and Tools"), re.M)), 4,
                                        "formulas expected")
                self.assertRegex(section(t, "Calculations and Tools"), r"[=÷×]")

    def test_generic_template_text_removed(self):
        for name in GENERIC:
            t = text(name)
            with self.subTest(skill=name):
                for snippet in TEMPLATE:
                    self.assertNotIn(snippet, t)


class Complementarity(unittest.TestCase):
    def test_hands_off_to_existing_neighbours(self):
        for name in GENERIC:
            principles = section(text(name), "Principles and Constraints")
            refs = set(re.findall(r"`([a-z0-9-]+)`", principles)) & ALL_SKILLS
            with self.subTest(skill=name):
                self.assertGreaterEqual(len(refs - {name}), 2, "name the neighbouring skills to use instead")

    def test_no_content_duplicated_from_any_other_skill(self):
        others = {n: set(content_lines(text(n))) for n in ALL_SKILLS}
        offenders = []
        for name in GENERIC:
            mine = set(content_lines(new_content(name)))
            for other, lines in others.items():
                if other == name:
                    continue
                ratio = len(mine & lines) / len(mine)
                if ratio >= MAX_SHARED_WITH_ANY_SKILL:
                    offenders.append(f"{name} ~ {other}: {ratio:.0%}")
        self.assertEqual(offenders, [])


class HonestData(unittest.TestCase):
    def test_reliability_and_examples(self):
        for name in GENERIC:
            t = text(name)
            rel = section(t, "Data Reliability")
            with self.subTest(skill=name):
                self.assertIn("[verified]", rel)
                self.assertIn("[estimate]", rel)
                self.assertRegex(rel, r"\*\*Verified:\*\*")
                self.assertRegex(rel, r"\*\*Estimates:\*\*")
                self.assertRegex(section(t, "Worked Example").lstrip(), r"^\*Illustrative example")
                self.assertIn("November 2026", section(t, "Principles and Constraints") + rel)

    def test_scripts_documented_and_samples_synthetic(self):
        for name, script in SCRIPTS.items():
            with self.subTest(skill=name):
                self.assertTrue((ROOT / name / "scripts" / script).exists())
                self.assertRegex(text(name), rf"python3 scripts/{re.escape(script)} ['e]")
        for name, sample in SAMPLES.items():
            with self.subTest(sample=sample):
                self.assertTrue((ROOT / name / "examples" / sample).exists())
                self.assertIn("**synthetic test data**", text(name))


if __name__ == "__main__":
    unittest.main()

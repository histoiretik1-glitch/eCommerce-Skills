"""The 15 platform skills enriched in LOT 6: structure, platform rules, honest examples, no copied content."""
import itertools
import re
import unittest

from helpers import ROOT
from similarity import content_lines

PLATFORM_SKILLS = {
    "ebay": ["ebay-advertising", "ebay-product-research", "ebay-seller-guide", "ebay-seller-tools", "ebay-seo"],
    "walmart": ["walmart-advertising-strategy", "walmart-listing-optimization", "walmart-seller-guide", "walmart-seller-tools"],
    "shopify": ["shopify-ab-testing", "shopify-analytics-guide", "shopify-conversion-optimization", "shopify-seo",
                "shopify-store-setup"],
    "tiktok": ["tiktok-live-selling"],
}
ALL = [s for skills in PLATFORM_SKILLS.values() for s in skills]
SECTIONS = ["Role and Scope", "Capabilities", "Platform Rules and Constraints", "Data Needed", "Workflow",
            "Calculations and Tools", "Worked Example", "Example Requests", "Output Format", "Quality Checks",
            "Data Reliability"]
SCRIPTS = {"ebay-product-research": "sold_analysis.py", "ebay-advertising": "promoted_listings.py",
           "ebay-seo": "title_check.py", "walmart-advertising-strategy": "connect_report.py",
           "shopify-ab-testing": "ab_test.py", "shopify-analytics-guide": "orders_kpis.py",
           "tiktok-live-selling": "live_metrics.py"}
PLATFORM_WORDS = {"ebay": "eBay", "walmart": "Walmart", "shopify": "Shopify", "tiktok": "TikTok"}
MAX_SHARED = 0.15  # share of content lines two of these skills may have in common (headings and the reliability rule)


def text(name):
    return (ROOT / name / "SKILL.md").read_text(encoding="utf-8")


def section(t, title):
    return t.split(f"\n## {title}\n", 1)[1].split("\n## ", 1)[0]


def new_content(name):
    t = text(name)
    start = t.index("## Platform Rules and Constraints")
    end = t.index("## Other Skills") if "## Other Skills" in t else t.index("## Installation")
    return t[start:end]


class Structure(unittest.TestCase):
    def test_sections_present_and_ordered(self):
        for name in ALL:
            headings = re.findall(r"^## (.+?)\s*$", text(name), re.M)
            with self.subTest(skill=name):
                for s in SECTIONS:
                    self.assertIn(s, headings)
                positions = [headings.index(s) for s in SECTIONS]
                self.assertEqual(positions, sorted(positions), "sections out of order")

    def test_workflow_steps_and_concrete_requests(self):
        for name in ALL:
            t = text(name)
            with self.subTest(skill=name):
                self.assertGreaterEqual(len(re.findall(r"^\d+\. ", section(t, "Workflow"), re.M)), 7)
                quotes = re.findall(r'^- "(.+)"$', section(t, "Example Requests"), re.M)
                self.assertGreaterEqual(len(quotes), 3)
                self.assertFalse(any("[" in q for q in quotes), "example requests must not be templates")

    def test_quality_checks_and_output_are_lists(self):
        for name in ALL:
            t = text(name)
            with self.subTest(skill=name):
                self.assertGreaterEqual(len(re.findall(r"^- ", section(t, "Quality Checks"), re.M)), 5)
                self.assertGreaterEqual(len(re.findall(r"^(?:\d+\.|-) ", section(t, "Output Format"), re.M)), 4)


class PlatformSpecific(unittest.TestCase):
    def test_rules_are_platform_specific_dated_and_flagged(self):
        for platform, skills in PLATFORM_SKILLS.items():
            for name in skills:
                rules = section(text(name), "Platform Rules and Constraints")
                with self.subTest(skill=name):
                    self.assertIn(PLATFORM_WORDS[platform], rules)
                    self.assertIn("November 2026", rules, "rules must state when they were reviewed")
                    self.assertIn("[check]", rules, "changeable figures must be flagged for re-checking")
                    self.assertGreaterEqual(len(re.findall(r"^- ", rules, re.M)), 6)
                    others = [w for p, w in PLATFORM_WORDS.items() if p != platform]
                    mentions = sum(rules.count(w) for w in others)
                    self.assertLessEqual(mentions, 2, "rules section is about another platform")

    def test_data_needed_names_platform_sources(self):
        for platform, skills in PLATFORM_SKILLS.items():
            for name in skills:
                table = section(text(name), "Data Needed")
                with self.subTest(skill=name):
                    self.assertGreaterEqual(table.count("\n|"), 6)
                    self.assertRegex(table, r"Seller Hub|Seller Center|Ad Center|Analytics|Search Console|admin|"
                                            r"Reports|Orders|eBay|Walmart|Shopify")

    def test_no_content_copied_between_platform_skills(self):
        lines = {n: set(content_lines(new_content(n))) for n in ALL}
        offenders = []
        for a, b in itertools.combinations(ALL, 2):
            ratio = len(lines[a] & lines[b]) / min(len(lines[a]), len(lines[b]))
            if ratio >= MAX_SHARED:
                offenders.append(f"{a} / {b}: {ratio:.0%}")
        self.assertEqual(offenders, [])


class HonestData(unittest.TestCase):
    def test_reliability_section(self):
        for name in ALL:
            rel = section(text(name), "Data Reliability")
            with self.subTest(skill=name):
                self.assertIn("[verified]", rel)
                self.assertIn("[estimate]", rel)
                self.assertRegex(rel, r"\*\*Verified:\*\*")
                self.assertRegex(rel, r"\*\*Estimates:\*\*")

    def test_worked_examples_are_labelled_illustrative(self):
        for name in ALL:
            ex = section(text(name), "Worked Example")
            with self.subTest(skill=name):
                self.assertRegex(ex.lstrip(), r"^\*Illustrative example", "invented figures must be labelled as such")

    def test_scripts_documented_with_runnable_example(self):
        for name, script in SCRIPTS.items():
            with self.subTest(skill=name):
                self.assertTrue((ROOT / name / "scripts" / script).exists())
                self.assertRegex(text(name), rf"python3 scripts/{re.escape(script)} ['e]")

    def test_sample_data_is_marked_synthetic(self):
        t = text("shopify-analytics-guide")
        self.assertIn("**synthetic test data**", t)
        csv = (ROOT / "shopify-analytics-guide" / "examples" / "synthetic_orders_export.csv").read_text(encoding="utf-8")
        emails = re.findall(r"[\w.]+@([\w.]+)", csv)
        self.assertTrue(emails and all(d == "example.com" for d in emails), "sample emails must use example.com")


if __name__ == "__main__":
    unittest.main()

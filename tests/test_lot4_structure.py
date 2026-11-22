"""The skills enriched in LOT 4 keep the full professional structure."""
import re
import unittest

from helpers import ROOT

ENRICHED = [
    "api-monitoring", "customer-feedback-analysis", "domain-monitoring", "ecommerce-feed-management",
    "file-integrity-monitoring", "inventory-tracking-software", "localization-testing", "minimum-advertised-price",
    "online-reputation-management", "public-status-page", "restock-alert", "share-of-shelf", "shopify-page-speed",
    "synthetic-monitoring", "visual-regression-testing", "walmart-price-tracker",
]
REQUIRED_SECTIONS = ["Role and Scope", "Data Needed", "Workflow", "Calculations and Tools", "Example Requests",
                     "Output Format", "Quality Checks", "Data Reliability"]
SCRIPTS = {"restock-alert": "reorder.py", "share-of-shelf": "sos.py", "minimum-advertised-price": "map_check.py",
           "walmart-price-tracker": "price_index.py", "ecommerce-feed-management": "feed_check.py",
           "api-monitoring": "uptime.py"}


class EnrichedSkills(unittest.TestCase):
    def test_required_sections_present_and_ordered(self):
        for name in ENRICHED:
            text = (ROOT / name / "SKILL.md").read_text(encoding="utf-8")
            headings = re.findall(r"^## (.+?)\s*$", text, re.M)
            with self.subTest(skill=name):
                for section in REQUIRED_SECTIONS:
                    self.assertIn(section, headings)
                positions = [headings.index(s) for s in REQUIRED_SECTIONS]
                self.assertEqual(positions, sorted(positions), "sections out of order")

    def test_workflow_has_steps_and_examples_are_concrete(self):
        for name in ENRICHED:
            text = (ROOT / name / "SKILL.md").read_text(encoding="utf-8")
            workflow = text.split("## Workflow", 1)[1].split("\n## ", 1)[0]
            examples = text.split("## Example Requests", 1)[1].split("\n## ", 1)[0]
            with self.subTest(skill=name):
                self.assertGreaterEqual(len(re.findall(r"^\d+\. ", workflow, re.M)), 5)
                quotes = re.findall(r'^- "(.+)"$', examples, re.M)
                self.assertGreaterEqual(len(quotes), 3)
                self.assertFalse(any("[" in q for q in quotes), "examples must not be templates with placeholders")

    def test_data_reliability_distinguishes_verified_and_estimates(self):
        for name in ENRICHED:
            text = (ROOT / name / "SKILL.md").read_text(encoding="utf-8")
            section = text.split("## Data Reliability", 1)[1].split("\n## ", 1)[0]
            with self.subTest(skill=name):
                self.assertIn("[verified]", section)
                self.assertIn("[estimate]", section)
                self.assertRegex(section, r"\*\*Verified\*\*")

    def test_scripts_documented_with_runnable_example(self):
        for name, script in SCRIPTS.items():
            text = (ROOT / name / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=name):
                self.assertTrue((ROOT / name / "scripts" / script).exists())
                self.assertRegex(text, rf"python3 scripts/{re.escape(script)} '")


if __name__ == "__main__":
    unittest.main()

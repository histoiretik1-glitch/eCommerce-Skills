"""tools/validate_plugin.py must accept the repository and reject each class of defect."""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT

VALIDATOR = ROOT / "tools" / "validate_plugin.py"


def run_validator(root: Path):
    return subprocess.run([sys.executable, str(root / "tools" / "validate_plugin.py"), "--expected", "162"],
                          capture_output=True, text=True, timeout=120)


class Validator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = Path(cls.tmp.name) / "repo"
        shutil.copytree(ROOT, cls.copy, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def mutate(self, rel, old, new):
        """Apply one change to the copy, run the validator, restore the file."""
        path = self.copy / rel
        original = path.read_text(encoding="utf-8")
        self.assertIn(old, original, f"test setup: '{old[:40]}' not in {rel}")
        path.write_text(original.replace(old, new, 1), encoding="utf-8")
        try:
            return run_validator(self.copy)
        finally:
            path.write_text(original, encoding="utf-8")

    def assertRejected(self, result, message):
        self.assertEqual(result.returncode, 1, result.stdout[-400:])
        self.assertIn(message, result.stdout)

    def test_repository_is_valid(self):
        r = run_validator(ROOT)
        self.assertEqual(r.returncode, 0, r.stdout[-1500:])
        self.assertIn("162 skills on disk, 162 referenced", r.stdout)

    def test_rejects_description_without_use_when(self):
        rel = "etsy-star-seller/SKILL.md"
        text = (self.copy / rel).read_text()
        desc = re.search(r"^description: (.*)$", text, re.M).group(1)
        self.assertRejected(self.mutate(rel, desc, '"Etsy Star Seller guide for sellers who want the badge and more sales."'),
                            "no 'Use when' sentence")

    def test_rejects_platform_missing_from_description(self):
        rel = "shopify-tax-compliance/SKILL.md"
        self.assertRejected(self.mutate(rel, '"Shopify tax setup and compliance.', '"Tax setup and compliance.'),
                            "should name the platform (shopify)")

    def test_rejects_long_description(self):
        rel = "etsy-star-seller/SKILL.md"
        self.assertRejected(self.mutate(rel, 'description: "Etsy Star Seller guide.',
                                        'description: "Etsy Star Seller guide.' + " Use when." * 120),
                            "(max 500)")

    def test_rejects_legacy_install_command(self):
        rel = "ebay-seo/SKILL.md"
        self.assertRejected(self.mutate(rel, "## Installation\n", "## Installation\n\n```\nclawhub install ebay-seo\n```\n"),
                            "legacy install command")

    def test_rejects_missing_installation_section(self):
        rel = "ebay-seo/SKILL.md"
        self.assertRejected(self.mutate(rel, "## Installation\n", "## Setup\n"),
                            "exactly one '## Installation' section")

    def test_rejects_wrong_skill_in_install_command(self):
        rel = "ebay-seo/SKILL.md"
        self.assertRejected(self.mutate(rel, "--skill ebay-seo -g", "--skill ebay-seller-guide -g"),
                            "--skill ebay-seo -g")

    def test_rejects_unknown_skill_reference(self):
        rel = "ecommerce-ppc-strategy-planner/SKILL.md"
        self.assertRejected(self.mutate(rel, "**tiktok-shop-ads**", "**tiktok-ads-ecommerce**"),
                            "references unknown skill `tiktok-ads-ecommerce`")


if __name__ == "__main__":
    unittest.main()

"""LOT 5 final audit: library quality gate, metadata, scripts, honest outputs, trigger suite."""
import json
import re
import subprocess
import sys
import unittest

from helpers import ROOT, load_module, run_script

AUDIT = load_module(ROOT / "tools" / "audit_library.py", "lot5_audit")
REPORT = AUDIT.audit()

# Skills that are still topic lists without a step-by-step method (audit E2).
# This list may only shrink: when a skill is enriched, remove it from here.
# LOT 6 removed the 15 platform skills (eBay, Walmart, Shopify, TikTok LIVE): 44 -> 29; LOT 7 the 29 generic ones: 29 -> 0.
KNOWN_TO_IMPROVE = set()  # emptied in LOT 7: all 162 skills meet the quality bar


class LibraryQualityGate(unittest.TestCase):
    def test_every_other_skill_is_validated(self):
        to_improve = {s["name"]: s["missing"] for s in REPORT["skills"] if s["status"] != "validated"}
        unexpected = {k: v for k, v in to_improve.items() if k not in KNOWN_TO_IMPROVE}
        self.assertEqual(unexpected, {}, "skills that dropped below the quality bar")
        fixed = sorted(KNOWN_TO_IMPROVE - set(to_improve))
        self.assertEqual(fixed, [], "these skills are now validated: remove them from KNOWN_TO_IMPROVE")

    def test_counts(self):
        self.assertEqual(len(REPORT["skills"]), 162)
        self.assertEqual(REPORT["summary"]["validated"], 162 - len(KNOWN_TO_IMPROVE))


class Metadata(unittest.TestCase):
    def test_manifest_versions_and_entries(self):
        meta = REPORT["meta"]
        self.assertTrue(meta["versions_match"], "metadata.version must equal the plugin version")
        self.assertTrue(meta["manifest_matches_disk"])
        self.assertEqual(meta["manifest_entries"], 162)
        self.assertRegex(meta["plugin_version"], r"^\d+\.\d+\.\d+$")


class Scripts(unittest.TestCase):
    SCRIPTS = sorted(p for p in ROOT.rglob("scripts/*.py") if "node_modules" not in p.parts)

    def test_scripts_compile(self):
        self.assertGreaterEqual(len(self.SCRIPTS), 40)
        for p in self.SCRIPTS:
            with self.subTest(script=str(p.relative_to(ROOT))):
                compile(p.read_text(encoding="utf-8"), str(p), "exec")

    def test_scripts_use_standard_library_only(self):
        for p in self.SCRIPTS:
            with self.subTest(script=str(p.relative_to(ROOT))):
                self.assertEqual(AUDIT.script_imports(p), [], "third-party import: add a dependency policy first")


class HonestOutputs(unittest.TestCase):
    """Scripts that can fall back to demo data must say so, and must analyze real input when given."""

    def test_demo_is_labelled(self):
        cases = [(ROOT / "brand-monitoring", "monitor.py", ["Acme"]), (ROOT / "etsy-seo", "analyzer.py", []),
                 (ROOT / "product-differentiation" / "product-differentiation-tiktok", "analyzer.py", [])]
        for skill, script, args in cases:
            with self.subTest(skill=skill.name):
                out = run_script(skill, script, *args).stdout
                self.assertIn("DEMO DATA", out)

    def test_brand_monitoring_analyzes_given_mentions(self):
        data = {"brand": "Zeta", "mentions": [{"content": "Zeta kettle broke after a week, terrible", "platform": "reddit"},
                                              {"content": "Zeta kettle is great", "platform": "news"}]}
        out = run_script(ROOT / "brand-monitoring", "monitor.py", json.dumps(data)).stdout
        self.assertNotIn("DEMO DATA", out)
        self.assertRegex(out, r"Total Mentions \| 2 \|")
        bad = run_script(ROOT / "brand-monitoring", "monitor.py", '{"brand": "Z", "mentions": [{"text": "x"}]}')
        self.assertEqual(bad.returncode, 1)

    def test_etsy_seo_analyzes_given_listing(self):
        weak = {"title": "Ring", "tags": ["ring"], "description": "Ring.", "category": "Jewelry"}
        strong = {"title": "Personalized Birthstone Ring, Dainty Sterling Silver Stacking Ring, Custom Gift for Mom",
                  "tags": ["birthstone ring", "personalized ring", "stacking ring", "dainty ring", "sterling silver ring",
                           "gift for mom", "custom ring", "minimalist ring", "birthday gift", "mothers day gift",
                           "name ring", "promise ring", "gift for her"],
                  "description": "Personalized birthstone ring in sterling silver. " * 20, "category": "jewelry"}
        out_weak = run_script(ROOT / "etsy-seo", "analyzer.py", json.dumps(weak)).stdout
        out_strong = run_script(ROOT / "etsy-seo", "analyzer.py", json.dumps(strong)).stdout
        self.assertNotIn("DEMO DATA", out_weak)
        self.assertIn("**Listing**: Ring", out_weak)          # the given listing, not the demo bracelet
        self.assertNotIn("Bracelet", out_weak)
        score = lambda o: int(re.search(r"SEO Score: (\d+)/100", o).group(1))
        self.assertGreater(score(out_strong), score(out_weak))
        bad = run_script(ROOT / "etsy-seo", "analyzer.py", '{"titel": "typo"}')
        self.assertEqual(bad.returncode, 1)

    def test_product_differentiation_analyzes_given_reviews(self):
        data = {"my_product": {"name": "Kettle X", "price": 39.0, "rating": 4.2, "review_count": 80},
                "competitors": [{"name": "Kettle Y", "price": 45.0, "rating": 3.9, "review_count": 300}],
                "competitor_reviews": {"negative": ["The lid leaks water everywhere", "Lid leaks after a month", "Too loud when boiling"]}}
        out = run_script(ROOT / "product-differentiation" / "product-differentiation-amazon", "analyzer.py", json.dumps(data)).stdout
        self.assertNotIn("DEMO DATA", out)
        self.assertIn("Kettle", out)
        self.assertNotIn("Earbuds", out)  # demo product must not appear


class TriggerSuite(unittest.TestCase):
    def test_cases_reference_existing_skills_and_folders_are_generated(self):
        data = json.loads((ROOT / "evals" / "trigger_cases.json").read_text(encoding="utf-8"))
        names = {s["name"] for s in REPORT["skills"]}
        ids = set()
        for case in data["cases"]:
            for skill in case["expect"]:
                self.assertIn(skill, names, case["id"])
            ids.add(case["id"])
            folder = ROOT / "evals" / f"trigger-{case['id']}"
            self.assertTrue((folder / "prompt.md").exists(), f"run tools/make_trigger_evals.py ({case['id']})")
            self.assertIn(case["prompt"], (folder / "prompt.md").read_text(encoding="utf-8"))
        on_disk = {p.name[len("trigger-"):] for p in (ROOT / "evals").glob("trigger-*")}
        self.assertEqual(on_disk, ids, "evals/trigger-* folders out of sync with trigger_cases.json")
        self.assertTrue(any(not c["expect"] for c in data["cases"]), "keep at least one negative case")


class InstallCheckScript(unittest.TestCase):
    def test_check_install_is_valid_python_and_documented(self):
        path = ROOT / "tools" / "check_install.py"
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
        workflow = (ROOT / ".github" / "workflows" / "validate-plugin.yml").read_text(encoding="utf-8")
        self.assertIn("tools/check_install.py", workflow)


if __name__ == "__main__":
    unittest.main()

"""Every `python3 scripts/...` example documented in a SKILL.md must run, and shared scripts must stay in sync."""
import filecmp
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from helpers import ROOT

# Examples that cannot run offline or are illustrative on purpose
SKIP = {}  # every documented example runs offline since LOT 5

# Script families: the same file must be identical in every member folder
FAMILIES = {
    "profit-margin-calculator": ["calculator.py"],
    "supply-chain-optimization": ["calculator.py", "report_doc.py", "report_html.py"],
    "brand-protection": ["detector.py", "templates.py"],
    "product-differentiation": ["analyzer.py"],
    "review-checker": ["analyzer.py", "parser.py", "report_html.py"],
}

_CMD = re.compile(r"(python3 scripts/[\w.-]+\.py(?: '[\[{].*?[\]}]'| [^\n'`]*)?)", re.S)


def code_blocks(text):
    """Contents of fenced code blocks, parsed line by line (any language tag)."""
    block, inside = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            if inside:
                yield "\n".join(block)
                block = []
            inside = not inside
        elif inside:
            block.append(line)


def documented_examples():
    for skill_md in sorted(ROOT.rglob("SKILL.md")):
        if any(part in ("node_modules", ".git") for part in skill_md.parts):
            continue
        text = skill_md.read_text(encoding="utf-8")
        for block in code_blocks(text):
            for cmd in _CMD.findall(block):
                yield skill_md.parent, " ".join(cmd.split()) if "'" not in cmd else cmd.strip()


class DocumentedExamples(unittest.TestCase):
    def test_examples_run(self):
        ran = 0
        for skill_dir, cmd in documented_examples():
            if skill_dir.name in SKIP:
                continue
            with self.subTest(skill=skill_dir.name, cmd=cmd[:80]):
                with tempfile.TemporaryDirectory() as tmp:
                    work = Path(tmp) / skill_dir.name
                    shutil.copytree(skill_dir, work)  # scripts may write report files
                    args = shlex.split(cmd)
                    args[0] = sys.executable
                    r = subprocess.run(args, cwd=work, capture_output=True, text=True, timeout=60,
                                       stdin=subprocess.DEVNULL)
                    self.assertEqual(r.returncode, 0, r.stdout[-500:] + r.stderr[-500:])
                    self.assertNotRegex(r.stdout, r"^Error:", r.stdout[:300])
                    self.assertNotIn("Traceback", r.stderr)
                ran += 1
        self.assertGreater(ran, 40)


class SharedScriptsInSync(unittest.TestCase):
    def test_family_copies_identical(self):
        for family, scripts in FAMILIES.items():
            members = sorted(p for p in (ROOT / family).iterdir() if p.is_dir())
            self.assertGreaterEqual(len(members), 3, family)
            for script in scripts:
                reference = members[0] / "scripts" / script
                for member in members[1:]:
                    with self.subTest(family=family, script=script, member=member.name):
                        self.assertTrue(filecmp.cmp(reference, member / "scripts" / script, shallow=False),
                                        f"{member.name}/scripts/{script} differs from {members[0].name}: "
                                        "edit one copy, then copy it to every member of the family")


if __name__ == "__main__":
    unittest.main()

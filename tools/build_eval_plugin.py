#!/usr/bin/env python3
"""Build a standard plugin folder for `claude plugin eval` from this repository.

The repository publishes its plugin through .claude-plugin/marketplace.json
(`strict: false`, skills listed by path), which `claude plugin eval` does not
load from the repository root. This script creates, in a target folder:

  <out>/.claude-plugin/plugin.json   name/version/description from marketplace.json
  <out>/skills/<skill-name>          symlink to each skill folder listed in the manifest
  <out>/evals                        copy of the repository's evals/ cases (results are written there)

Usage:
  python3 tools/build_eval_plugin.py /tmp/ecommerce-skills-eval
  claude plugin eval /tmp/ecommerce-skills-eval --trust-plugin --no-publish --runs 1 --ablation none

Standard library only. Nothing in the repository is modified.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def build(out: Path) -> int:
    manifest = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = manifest["plugins"][0]
    if out.exists():
        shutil.rmtree(out)
    (out / ".claude-plugin").mkdir(parents=True)
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": plugin["name"], "version": plugin["version"], "description": plugin["description"],
    }, indent=2), encoding="utf-8")
    skills = out / "skills"
    skills.mkdir()
    for rel in plugin["skills"]:
        src = (ROOT / rel).resolve()
        (skills / src.name).symlink_to(src, target_is_directory=True)
    shutil.copytree(ROOT / "evals", out / "evals", ignore=shutil.ignore_patterns("results"))
    return len(plugin["skills"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    n = build(Path(sys.argv[1]).resolve())
    print(f"Built eval plugin with {n} skills at {sys.argv[1]}")

#!/usr/bin/env python3
"""Generate evals/trigger-<id>/ case folders from evals/trigger_cases.json.

Each case: prompt.md (Skill tool only, 4 turns, 1 run) and graders/skill.md, a
deterministic `tool_used` grader on the Skill tool. A case with an empty
"expect" list asserts that no plugin skill is used.

Usage: python3 tools/make_trigger_evals.py   (then see evals/trigger_cases.json for how to run)
Standard library only.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
PLUGIN = "ecommerce-skills"


def main():
    data = json.loads((EVALS / "trigger_cases.json").read_text(encoding="utf-8"))
    for old in EVALS.glob("trigger-*"):
        shutil.rmtree(old)
    for case in data["cases"]:
        d = EVALS / f"trigger-{case['id']}"
        (d / "graders").mkdir(parents=True)
        tags = ", ".join(["trigger"] + case.get("tags", []))
        (d / "prompt.md").write_text(
            f"---\nmax_turns: 4\nallowed_tools: [Skill]\nruns: 1\ntags: [{tags}]\n---\n\n{case['prompt']}\n",
            encoding="utf-8")
        if case["expect"]:
            alt = "|".join(case["expect"])
            grader = (f"---\ntype: tool_used\ntool: Skill\n"
                      f"input_match: '\"skill\"\\s*:\\s*\"(?:{PLUGIN}:)?(?:{alt})\"'\nmin: 1\n---\n")
        else:
            grader = (f"---\ntype: tool_used\ntool: Skill\n"
                      f"input_match: '\"skill\"\\s*:\\s*\"{PLUGIN}:'\nmin: 0\nmax: 0\n---\n")
        (d / "graders" / "skill.md").write_text(grader, encoding="utf-8")
    print(f"Wrote {len(data['cases'])} trigger cases in {EVALS}")


if __name__ == "__main__":
    main()

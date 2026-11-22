#!/usr/bin/env python3
"""Write the "Role and Scope" section of every grouped skill from tools/skill_groups.json.

Usage:
  python3 tools/apply_skill_groups.py          # update SKILL.md files
  python3 tools/apply_skill_groups.py --check  # exit 1 if a section is missing or outdated

The section sits between HTML comment markers, right after the skill's title
and intro paragraph, so it is regenerated in place. Standard library only.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "tools" / "skill_groups.json"
START = "<!-- role-and-scope:start (generated from tools/skill_groups.json) -->"
END = "<!-- role-and-scope:end -->"
BLOCK = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n*", re.S)


def load_registry():
    groups = json.loads(REGISTRY.read_text(encoding="utf-8"))["groups"]
    roles, neighbours, titles = {}, {}, {}
    for gid, group in groups.items():
        for name, role in group["members"].items():
            if name in roles and roles[name] != role:
                raise SystemExit(f"{name}: different roles in two groups ({gid})")
            roles[name] = role
            titles.setdefault(name, []).append(group["title"])
            neighbours.setdefault(name, [])
            for other in group["members"]:
                if other != name and other not in neighbours[name]:
                    neighbours[name].append(other)
    return roles, neighbours, titles


def section(name, roles, neighbours, titles):
    lines = [START, "## Role and Scope", "",
             f"**This skill:** {roles[name]}", "",
             f"Part of: {', '.join(titles[name])}. For neighbouring jobs, use the matching skill instead:", ""]
    lines += [f"- `{other}` — {roles[other]}" for other in neighbours[name]]
    lines += ["", END, "", ""]
    return "\n".join(lines)


def skill_paths():
    return {p.parent.name: p for p in ROOT.rglob("SKILL.md")
            if ".git" not in p.parts and "node_modules" not in p.parts}


def render(text, block):
    """Return text with the generated block placed after the H1 title and its intro paragraph."""
    text = BLOCK.sub("", text)
    if not block:
        return text
    m = re.search(r"^# .+\n", text, re.M)
    pos = m.end() if m else 0
    nxt = re.compile(r"^## ", re.M).search(text, pos)
    pos = nxt.start() if nxt else len(text)
    return text[:pos] + block + text[pos:]


def main():
    check = "--check" in sys.argv
    roles, neighbours, titles = load_registry()
    paths = skill_paths()
    missing = sorted(set(roles) - set(paths))
    if missing:
        print("Unknown skills in registry: " + ", ".join(missing))
        return 1
    problems = []
    for name, path in sorted(paths.items()):
        text = path.read_text(encoding="utf-8")
        block = section(name, roles, neighbours, titles) if name in roles else ""
        new = render(text, block)
        if new != text:
            if check:
                problems.append(name)
            else:
                path.write_text(new, encoding="utf-8")
    if check:
        if problems:
            print("Role and Scope section missing or outdated: " + ", ".join(problems))
            print("Run: python3 tools/apply_skill_groups.py")
            return 1
        print(f"OK: {len(roles)} grouped skills have an up-to-date Role and Scope section")
    else:
        print(f"Updated Role and Scope sections ({len(roles)} grouped skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

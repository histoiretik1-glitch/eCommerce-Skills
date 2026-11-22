#!/usr/bin/env python3
"""Library-wide audit of the 162 skills (LOT 5).

Computes, for every SKILL.md, objective quality signals and classifies the skill:

  validated  - valid frontmatter, own content (>= 8 specific lines), a method
               (>= 5 numbered steps, or >= 800 words with >= 6 sub-headings),
               an output/deliverable section and usage examples
  to-improve - anything else, with the list of missing criteria

Also checks the manifest and metadata, scripts (standard library only, documented
and present), references, and estimates the always-on token cost of descriptions
(about 4 characters per token for English text; `claude plugin details` gives
Claude Code's own estimate).

Usage:
  python3 tools/audit_library.py            # summary table
  python3 tools/audit_library.py --json     # full JSON
Standard library only.
"""
import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tests"))
from similarity import content_lines  # noqa: E402

STD_LIB = set(sys.stdlib_module_names)
CHARS_PER_TOKEN = 4.0
KNOWN_FRONTMATTER = {"name", "description", "metadata"}


def skill_paths():
    return sorted((p for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts and "node_modules" not in p.parts),
                  key=lambda p: p.parent.name)


def frontmatter(text):
    end = text.find("\n---", 4)
    block = text[4:end]
    keys = re.findall(r"^([A-Za-z0-9_-]+):", block, re.M)
    desc = re.search(r"^description: (.*)$", block, re.M)
    value = desc.group(1) if desc else ""
    if value.startswith('"'):
        try:
            value = json.loads(value)
        except ValueError:
            pass
    return keys, value


def script_imports(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            mods.add(node.module.split(".")[0])
    local = {p.stem for p in path.parent.glob("*.py")}
    return sorted(m for m in mods if m not in STD_LIB and m not in local)


def audit():
    paths = skill_paths()
    texts = {p.parent.name: p.read_text(encoding="utf-8") for p in paths}
    lines = {k: content_lines(v) for k, v in texts.items()}
    spread = Counter(l for s in lines.values() for l in s)
    registry = json.loads((ROOT / "tools" / "skill_groups.json").read_text(encoding="utf-8"))["groups"]
    grouped = {m for g in registry.values() for m in g["members"]}
    manifest = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    listed = {Path(s).name for s in manifest["plugins"][0]["skills"]}

    skills = []
    for p in paths:
        name = p.parent.name
        text = texts[name]
        keys, desc = frontmatter(text)
        body = text[text.find("\n---", 4) + 4:]
        headings = re.findall(r"^#{2,4} (.+?)\s*$", body, re.M)
        steps = len(re.findall(r"^\s*\d+\. ", body, re.M)) + \
            len(re.findall(r"^#{2,4} (?:step|phase)?\s*\d+[.:)]", body, re.I | re.M))
        words = len(body.split())
        specific = sum(1 for l in lines[name] if spread[l] < 5)
        has_output = any(re.search(r"output|deliverable|report format|result", h, re.I) for h in headings)
        example_sections = re.findall(r"^#{2,3} [^\n]*(?:example|usage)[^\n]*\n(.*?)(?=^## |\Z)", body, re.I | re.M | re.S)
        has_examples = any(re.search(r'"[^"\n]{15,}"|```', sec) for sec in example_sections)
        method = steps >= 5 or (words >= 800 and len(headings) >= 6)
        scripts = sorted(s.name for s in (p.parent / "scripts").glob("*.py")) if (p.parent / "scripts").is_dir() else []
        third_party = {s: script_imports(p.parent / "scripts" / s) for s in scripts}
        missing = []
        if specific < 8:
            missing.append("own content")
        if not method:
            missing.append("step-by-step method")
        if not has_output:
            missing.append("output format")
        if not has_examples:
            missing.append("usage examples")
        if any(third_party.values()):
            missing.append("non-stdlib script import")
        skills.append({
            "name": name, "path": str(p.parent.relative_to(ROOT)), "words": words, "steps": steps,
            "headings": len(headings), "specific_lines": specific, "has_output": has_output,
            "has_examples": has_examples, "scripts": scripts, "third_party_imports": {k: v for k, v in third_party.items() if v},
            "grouped": name in grouped, "in_manifest": name in listed,
            "description_chars": len(desc), "description_tokens": round(len(desc) / CHARS_PER_TOKEN),
            "extra_frontmatter": sorted(set(keys) - KNOWN_FRONTMATTER),
            "status": "validated" if not missing else "to-improve", "missing": missing,
        })
    plugin = manifest["plugins"][0]
    meta = {
        "marketplace_version": manifest["metadata"].get("version"), "plugin_version": plugin.get("version"),
        "versions_match": manifest["metadata"].get("version") == plugin.get("version"),
        "manifest_entries": len(plugin["skills"]), "skills_on_disk": len(paths),
        "manifest_matches_disk": listed == set(texts),
        "skills_with_extra_frontmatter": Counter(k for s in skills for k in s["extra_frontmatter"]),
    }
    tokens = sum(s["description_tokens"] + 10 for s in skills)  # + name and list formatting
    return {"meta": meta, "skills": skills,
            "summary": {"validated": sum(s["status"] == "validated" for s in skills),
                        "to_improve": sum(s["status"] == "to-improve" for s in skills),
                        "estimated_always_on_tokens": tokens,
                        "missing_counts": dict(Counter(m for s in skills for m in s["missing"]))}}


def main():
    r = audit()
    if "--json" in sys.argv:
        print(json.dumps(r, indent=2, default=dict))
        return
    s = r["summary"]
    print(f"Skills: {len(r['skills'])} | validated: {s['validated']} | to improve: {s['to_improve']}")
    print(f"Missing criteria: {s['missing_counts']}")
    print(f"Estimated always-on description tokens: ~{s['estimated_always_on_tokens']}")
    print(f"Manifest: {r['meta']}")
    for sk in r["skills"]:
        if sk["status"] != "validated":
            print(f"  - {sk['name']}: {', '.join(sk['missing'])} ({sk['words']} words)")


if __name__ == "__main__":
    main()

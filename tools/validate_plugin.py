#!/usr/bin/env python3
"""Validate the Claude Code plugin packaging of this repository.

Checks:
  * every SKILL.md starts with YAML frontmatter containing `name` and `description`
  * `name` matches the skill's folder name (lowercase, digits, hyphens; max 64 chars)
  * skill names are unique
  * .claude-plugin/marketplace.json references exactly the skill folders on disk
  * relative `scripts/...` files and Markdown links mentioned in SKILL.md exist
  * when PyYAML is installed: every frontmatter block is valid YAML and
    `name` / `description` are non-empty strings (strict mode)

Usage:
  python3 tools/validate_plugin.py                 # validate only
  python3 tools/validate_plugin.py --expected 162  # also require exactly 162 skills
  python3 tools/validate_plugin.py --write         # also regenerate the skills list in marketplace.json

Uses only the Python standard library; PyYAML is optional and enables strict YAML checks.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "marketplace.json"
try:
    import yaml  # optional, enables strict YAML parsing
except ImportError:
    yaml = None

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def skill_dirs():
    return sorted(
        p.parent for p in ROOT.rglob("SKILL.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    )


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)  # top-level keys only
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def main():
    errors = []
    dirs = skill_dirs()
    seen = {}
    for d in dirs:
        rel = d.relative_to(ROOT)
        text = (d / "SKILL.md").read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        if yaml is not None:
            try:
                strict = yaml.safe_load(text[4:text.find("\n---", 4)])
            except yaml.YAMLError as exc:
                errors.append(f"{rel}: invalid YAML frontmatter: {str(exc).splitlines()[0]}")
                continue
            if not isinstance(strict, dict):
                errors.append(f"{rel}: frontmatter is not a YAML mapping")
                continue
            for key in ("name", "description"):
                if not isinstance(strict.get(key), str) or not strict[key].strip():
                    errors.append(f"{rel}: `{key}` must be a non-empty string")
        name = fm.get("name", "").strip("\"'")
        desc = fm.get("description", "").strip("\"'")
        if not name:
            errors.append(f"{rel}: missing `name`")
        elif name != d.name:
            errors.append(f"{rel}: name `{name}` does not match folder `{d.name}`")
        elif not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: invalid name `{name}`")
        if not desc:
            errors.append(f"{rel}: missing `description`")
        if name in seen:
            errors.append(f"{rel}: duplicate name `{name}` (also {seen[name]})")
        seen[name] = rel
        for ref in set(re.findall(r"(?<![\w/.])((?:scripts|references|assets)/[\w./-]+\.\w+)", text)):
            if not (d / ref).exists():
                errors.append(f"{rel}: referenced file `{ref}` not found")
        for link in set(re.findall(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)", text)):
            if not (d / link).exists():
                errors.append(f"{rel}: broken relative link `{link}`")

    on_disk = ["./" + d.relative_to(ROOT).as_posix() for d in dirs]
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        plugin = manifest["plugins"][0]
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(f"FAILED: cannot read {MANIFEST.relative_to(ROOT)}: {exc}")
        return 1
    if "--write" in sys.argv:
        plugin["skills"] = on_disk
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"marketplace.json: skills list regenerated ({len(on_disk)} entries)")
    listed = plugin.get("skills", [])
    for s in sorted(set(on_disk) - set(listed)):
        errors.append(f"marketplace.json: skill folder not referenced: {s}")
    for s in sorted(set(listed) - set(on_disk)):
        errors.append(f"marketplace.json: referenced path has no SKILL.md: {s}")
    if len(listed) != len(set(listed)):
        errors.append("marketplace.json: duplicate entries in skills list")

    if "--expected" in sys.argv:
        expected = int(sys.argv[sys.argv.index("--expected") + 1])
        if len(dirs) != expected:
            errors.append(f"expected {expected} skills, found {len(dirs)} SKILL.md files")

    if errors:
        print("\n".join(errors))
        print(f"\nFAILED: {len(errors)} problem(s)")
        return 1
    mode = "strict YAML" if yaml is not None else "basic frontmatter parser"
    print(f"OK: {len(dirs)} skills on disk, {len(listed)} referenced in marketplace.json, all valid ({mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Extract the 'functional' lines of a SKILL.md, used to prove that no content is lost.

Functional lines are list items, numbered steps and table rows outside the
Installation section. Lines that appear in 5 or more SKILL.md files are
template boilerplate and are ignored. Standard library only.
"""
import re
from collections import Counter

BOILERPLATE_MIN_FILES = 5
_INSTALL = re.compile(r"^## Install(?:ation)?[ \t]*\n.*?(?=^## |\Z)", re.S | re.M)
_ITEM = re.compile(r"^\s*(?:[-*]|\d+\.|\|)\s*(.+?)\s*\|?\s*$")


def normalize(line):
    line = re.sub(r"[*_`>]", "", line)
    return re.sub(r"\s+", " ", line).strip().lower()


def candidate_lines(text):
    body = text[text.find("\n---", 4) + 4:] if text.startswith("---") else text
    body = _INSTALL.sub("", body)
    out = []
    for raw in body.splitlines():
        m = _ITEM.match(raw)
        if not m:
            continue
        norm = normalize(m.group(1))
        if len(norm) < 12 or set(norm) <= set("-|: "):
            continue
        out.append(norm)
    return out


def functional_lines(texts_by_skill):
    """{skill: text} -> {skill: sorted unique functional lines}"""
    per_skill = {name: set(candidate_lines(t)) for name, t in texts_by_skill.items()}
    spread = Counter(line for lines in per_skill.values() for line in lines)
    return {name: sorted(l for l in lines if spread[l] < BOILERPLATE_MIN_FILES)
            for name, lines in per_skill.items()}

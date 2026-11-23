#!/usr/bin/env python3
"""
eBay listing title and item specifics check (before you revise a listing).

Input:
  {"title": "Canon AE-1 Program 35mm SLR Film Camera Body Black Tested Working",
   "keywords": ["canon ae-1", "35mm", "film camera"],        # buyer search terms that must appear
   "specifics": {"Brand": "Canon", "Model": "AE-1 Program", "Type": "SLR", "Color": ""},
   "recommended_specifics": ["Brand", "Model", "Type", "Color", "Format", "Country/Region of Manufacture"],
   "max_length": 80}                                          # eBay's title limit; check it for your site

Checks (each is a stated rule, not an eBay ranking formula):
  - length <= max_length, and how many characters are left unused
  - every keyword phrase appears in the title (case-insensitive)
  - repeated words (wasted characters), words in ALL CAPS longer than 3 letters
  - symbols and filler that eBay's guidance discourages: "!", "*", "L@@K", "WOW", "AWESOME", "NR"
  - recommended item specifics left empty (they power the search filters buyers click)

Usage:
  python3 scripts/title_check.py '<json>'
  python3 scripts/title_check.py '<json>' --json
Standard library only.
"""
import json
import re
import sys
from collections import Counter

FILLER = ["l@@k", "wow", "awesome", "nr", "must see", "rare!!!"]
ALLOWED = {"title", "keywords", "specifics", "recommended_specifics", "max_length"}


def check(d):
    unknown = sorted(set(d) - ALLOWED)
    if unknown or "title" not in d:
        raise ValueError(f"need title; unknown field(s): {unknown}")
    title = d["title"].strip()
    limit = int(d.get("max_length", 80))
    low = title.lower()
    words = re.findall(r"[a-z0-9][a-z0-9\-./]*", low)
    repeated = sorted(w for w, c in Counter(words).items() if c > 1 and len(w) > 2)
    caps = [w for w in title.split() if len(w) > 3 and w.isupper() and w.isalpha()]
    filler = [f for f in FILLER if re.search(rf"(?<![a-z0-9]){re.escape(f)}(?![a-z0-9])", low)]
    symbols = sorted(set(re.findall(r"[!*~#$%^]", title)))
    missing_kw = [k for k in d.get("keywords", []) if k.lower() not in low]
    specifics = d.get("specifics", {})
    empty = [s for s in d.get("recommended_specifics", []) if not str(specifics.get(s, "")).strip()]
    rec = d.get("recommended_specifics", [])
    issues = []
    if len(title) > limit:
        issues.append(f"title is {len(title)} characters, over the {limit} limit")
    if missing_kw:
        issues.append(f"missing buyer keywords: {', '.join(missing_kw)}")
    if repeated:
        issues.append(f"repeated words: {', '.join(repeated)}")
    if caps:
        issues.append(f"ALL CAPS words: {', '.join(caps)}")
    if filler or symbols:
        issues.append(f"filler/symbols: {', '.join(filler + symbols)}")
    if empty:
        issues.append(f"empty recommended specifics: {', '.join(empty)}")
    return {"title": title, "length": len(title), "unused_characters": max(limit - len(title), 0),
            "missing_keywords": missing_kw, "repeated_words": repeated, "all_caps": caps,
            "filler_or_symbols": filler + symbols, "empty_recommended_specifics": empty,
            "specifics_completion": round((len(rec) - len(empty)) / len(rec), 3) if rec else None,
            "issues": issues, "pass": not issues}


def report(r):
    lines = [f"Title: {r['title']}", f"Length: {r['length']} ({r['unused_characters']} characters unused)"]
    if r["specifics_completion"] is not None:
        lines.append(f"Recommended specifics filled: {r['specifics_completion']*100:.0f}%")
    lines.append("Result: PASS" if r["pass"] else "Issues:")
    lines += [f"- {i}" for i in r["issues"]]
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = check(json.loads(args[0]))
    except (ValueError, TypeError, AttributeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Product feed check - validate a product feed against Google Merchant Center basics.

Checks (Google Merchant Center product data specification as commonly published;
confirm the current spec, which changes and differs by country and category):
  errors   : missing required attribute (id, title, description, link, image_link, availability, price),
             duplicate id, invalid availability value, invalid price format, non-http(s) link,
             invalid GTIN check digit
  warnings : title longer than 150 characters, description longer than 5,000 characters,
             id longer than 50 characters, no gtin and no mpn, missing brand, image link not https,
             condition missing when it is not "new"

Input: a CSV or TSV file path, or a JSON list of products (attribute names as in the spec).
Usage:
  python3 scripts/feed_check.py                  # demo data
  python3 scripts/feed_check.py products.csv
  python3 scripts/feed_check.py '<json list>' --json
Standard library only.
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

REQUIRED = ("id", "title", "description", "link", "image_link", "availability", "price")
AVAILABILITY = {"in_stock", "out_of_stock", "preorder", "backorder"}
PRICE_RE = re.compile(r"^\d+(\.\d{1,2})? [A-Z]{3}$")

DEMO = [
    {"id": "SKU-1", "title": "Stainless Steel Water Bottle 750 ml - Blue", "description": "Double-wall insulated bottle.",
     "link": "https://example.com/p/bottle", "image_link": "https://example.com/i/bottle.jpg",
     "availability": "in_stock", "price": "24.99 USD", "brand": "Acme", "gtin": "4006381333931"},
    {"id": "SKU-2", "title": "Bottle", "description": "", "link": "example.com/p/2",
     "image_link": "http://example.com/i/2.jpg", "availability": "in stock", "price": "$19.99", "gtin": "4006381333932"},
    {"id": "SKU-1", "title": "Duplicate id product", "description": "x", "link": "https://example.com/p/3",
     "image_link": "https://example.com/i/3.jpg", "availability": "out_of_stock", "price": "9.99 USD", "mpn": "AC-3"},
]


def gtin_valid(code: str) -> bool:
    """GS1 mod-10 check digit for GTIN-8/12/13/14."""
    if not code.isdigit() or len(code) not in (8, 12, 13, 14):
        return False
    digits = [int(c) for c in code]
    body, check = digits[:-1], digits[-1]
    total = sum(d * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return (10 - total % 10) % 10 == check


def check_product(p, seen):
    errors, warnings = [], []
    pid = str(p.get("id", "")).strip()
    for attr in REQUIRED:
        if not str(p.get(attr, "")).strip():
            errors.append(f"missing {attr}")
    if pid:
        if pid in seen:
            errors.append("duplicate id")
        seen.add(pid)
        if len(pid) > 50:
            warnings.append("id longer than 50 characters")
    av = str(p.get("availability", "")).strip()
    if av and av not in AVAILABILITY:
        errors.append(f"invalid availability '{av}' (use {', '.join(sorted(AVAILABILITY))})")
    price = str(p.get("price", "")).strip()
    if price and not PRICE_RE.match(price):
        errors.append(f"invalid price format '{price}' (expected like '24.99 USD')")
    for attr in ("link", "image_link"):
        v = str(p.get(attr, "")).strip()
        if v and not v.startswith(("http://", "https://")):
            errors.append(f"{attr} is not a full http(s) URL")
        elif attr == "image_link" and v.startswith("http://"):
            warnings.append("image_link not https")
    gtin = str(p.get("gtin", "")).strip()
    if gtin and not gtin_valid(gtin):
        errors.append(f"invalid GTIN '{gtin}' (check digit or length)")
    if not gtin and not str(p.get("mpn", "")).strip():
        warnings.append("no gtin and no mpn")
    if not str(p.get("brand", "")).strip():
        warnings.append("missing brand")
    if len(str(p.get("title", ""))) > 150:
        warnings.append("title longer than 150 characters")
    if len(str(p.get("description", ""))) > 5000:
        warnings.append("description longer than 5,000 characters")
    cond = str(p.get("condition", "")).strip()
    if cond and cond not in ("new", "refurbished", "used"):
        errors.append(f"invalid condition '{cond}'")
    return {"id": pid or "(no id)", "errors": errors, "warnings": warnings}


def load(arg):
    if arg is None:
        return DEMO
    if arg.lstrip().startswith("["):
        return json.loads(arg)
    path = Path(arg)
    text = path.read_text(encoding="utf-8-sig")
    delim = "\t" if path.suffix.lower() in (".tsv", ".txt") or "\t" in text.splitlines()[0] else ","
    return list(csv.DictReader(text.splitlines(), delimiter=delim))


def analyze(products):
    seen = set()
    rows = [check_product(p, seen) for p in products]
    err = Counter(e.split(" '")[0] for r in rows for e in r["errors"])
    warn = Counter(w for r in rows for w in r["warnings"])
    return {"products": len(rows), "with_errors": sum(1 for r in rows if r["errors"]),
            "with_warnings": sum(1 for r in rows if r["warnings"]),
            "error_types": dict(err.most_common()), "warning_types": dict(warn.most_common()), "rows": rows}


def format_report(r):
    out = [f"Feed check: {r['products']} products, {r['with_errors']} with errors, {r['with_warnings']} with warnings", "",
           "| Issue | Type | Products |", "|-------|------|----------|"]
    out += [f"| {k} | error | {v} |" for k, v in r["error_types"].items()]
    out += [f"| {k} | warning | {v} |" for k, v in r["warning_types"].items()]
    out += ["", "| Product id | Errors | Warnings |", "|------------|--------|----------|"]
    out += [f"| {x['id']} | {'; '.join(x['errors']) or '-'} | {'; '.join(x['warnings']) or '-'} |"
            for x in r["rows"] if x["errors"] or x["warnings"]]
    out.append("\nRules follow the published Google Merchant Center basics; Merchant Center diagnostics remain the reference.")
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        r = analyze(load(args[0] if args else None))
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else format_report(r))


if __name__ == "__main__":
    main()

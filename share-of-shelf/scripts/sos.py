#!/usr/bin/env python3
"""
Share of Shelf - digital shelf visibility of a brand in marketplace search results.

Input: the search results the seller collected (one row per listing shown), per keyword:
  {"brand": "Acme", "top_n": 20,
   "results": [{"keyword": "steel water bottle", "rank": 1, "brand": "Acme", "sponsored": true}, ...]}

Metrics per keyword and overall (all are counts on the collected results, not estimates):
  share_of_shelf   = brand listings / all listings in the top N
  organic_share    = brand organic listings / organic listings in the top N
  paid_share       = brand sponsored listings / sponsored listings in the top N
  weighted_share   = sum(1/rank for brand listings) / sum(1/rank for all listings)
                     (position weighting by 1/rank is a convention: top positions count more)
  top3_presence    = brand has at least one listing in positions 1-3
Competitor table: the same share for every brand present.

Usage:
  python3 scripts/sos.py                 # demo data
  python3 scripts/sos.py '<json>'        # your data
  python3 scripts/sos.py '<json>' --json
Standard library only.
"""
import json
import sys
from collections import defaultdict

DEMO = {
    "brand": "Acme",
    "top_n": 10,
    "results": [
        {"keyword": "steel water bottle", "rank": r, "brand": b, "sponsored": s}
        for r, b, s in [(1, "Acme", True), (2, "Hydra", False), (3, "Acme", False), (4, "Flowr", True),
                        (5, "Hydra", False), (6, "Generic", False), (7, "Acme", False), (8, "Flowr", False),
                        (9, "Hydra", True), (10, "Other", False)]
    ] + [
        {"keyword": "insulated bottle 1l", "rank": r, "brand": b, "sponsored": s}
        for r, b, s in [(1, "Hydra", True), (2, "Hydra", False), (3, "Flowr", False), (4, "Acme", True),
                        (5, "Other", False), (6, "Generic", False), (7, "Flowr", False), (8, "Hydra", False),
                        (9, "Other", False), (10, "Acme", False)]
    ],
}


def _share(rows, brand, predicate=lambda r: True):
    pool = [r for r in rows if predicate(r)]
    if not pool:
        return None
    return sum(1 for r in pool if r["brand"].lower() == brand.lower()) / len(pool)


def _weighted(rows, brand):
    total = sum(1 / r["rank"] for r in rows)
    mine = sum(1 / r["rank"] for r in rows if r["brand"].lower() == brand.lower())
    return mine / total if total else None


def metrics(rows, brand):
    return {
        "listings": len(rows),
        "share_of_shelf": _share(rows, brand),
        "organic_share": _share(rows, brand, lambda r: not r.get("sponsored", False)),
        "paid_share": _share(rows, brand, lambda r: r.get("sponsored", False)),
        "weighted_share": _weighted(rows, brand),
        "top3_presence": any(r["brand"].lower() == brand.lower() and r["rank"] <= 3 for r in rows),
    }


def analyze(data):
    brand = data["brand"]
    top_n = int(data.get("top_n", 20))
    rows = []
    for r in data["results"]:
        missing = {"keyword", "rank", "brand"} - set(r)
        if missing:
            raise ValueError(f"result row missing {', '.join(sorted(missing))}: {r}")
        if int(r["rank"]) < 1:
            raise ValueError(f"rank must be >= 1: {r}")
        if int(r["rank"]) <= top_n:
            rows.append({**r, "rank": int(r["rank"])})
    by_kw = defaultdict(list)
    for r in rows:
        by_kw[r["keyword"]].append(r)
    brands = sorted({r["brand"] for r in rows}, key=str.lower)
    return {
        "brand": brand, "top_n": top_n,
        "keywords": {kw: metrics(rs, brand) for kw, rs in sorted(by_kw.items())},
        "overall": metrics(rows, brand),
        "competitors": sorted(({"brand": b, "share_of_shelf": _share(rows, b), "weighted_share": _weighted(rows, b)}
                               for b in brands), key=lambda x: -x["weighted_share"]),
    }


def pct(v):
    return "n/a" if v is None else f"{v*100:.1f}%"


def format_report(res):
    out = [f"Share of shelf for {res['brand']} (top {res['top_n']} results per keyword)", "",
           "| Keyword | Listings | Share | Organic | Paid | Weighted | In top 3 |",
           "|---------|----------|-------|---------|------|----------|----------|"]
    for kw, m in list(res["keywords"].items()) + [("ALL KEYWORDS", res["overall"])]:
        out.append(f"| {kw} | {m['listings']} | {pct(m['share_of_shelf'])} | {pct(m['organic_share'])} | "
                   f"{pct(m['paid_share'])} | {pct(m['weighted_share'])} | {'yes' if m['top3_presence'] else 'no'} |")
    out += ["", "| Brand | Share | Weighted |", "|-------|-------|----------|"]
    out += [f"| {c['brand']} | {pct(c['share_of_shelf'])} | {pct(c['weighted_share'])} |" for c in res["competitors"]]
    out += ["", "Counts come from the collected results (verified for that date, location and account); "
            "results vary by user, location and time, so compare snapshots taken the same way."]
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        res = analyze(json.loads(args[0]) if args else DEMO)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(res, indent=2) if "--json" in sys.argv else format_report(res))


if __name__ == "__main__":
    main()

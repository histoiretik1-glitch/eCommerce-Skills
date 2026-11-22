#!/usr/bin/env python3
"""
MAP check - find Minimum Advertised Price violations in observed prices.

Input:
  {"map_prices": {"SKU-1": 49.99},
   "tolerance": 0.01,                       # absolute $ tolerance (rounding), default 0.01
   "severity_thresholds": [0.05, 0.15],     # % below MAP: < 5% minor, 5-15% major, > 15% severe (policy choice)
   "observations": [{"sku": "SKU-1", "seller": "ShopX", "channel": "Amazon", "price": 44.99,
                     "date": "2026-11-20", "url": "https://..."}]}

Output: violations with gap ($ and %), severity, repeat offenders (count of violating
observations per seller) and the next enforcement step according to the number of
recorded violations (1st notice, 2nd warning, 3rd+ escalation: the brand's own policy decides).

Usage:
  python3 scripts/map_check.py            # demo data
  python3 scripts/map_check.py '<json>'
  python3 scripts/map_check.py '<json>' --json
Standard library only.
"""
import json
import sys
from collections import Counter, defaultdict

DEMO = {
    "map_prices": {"BLENDER-PRO": 129.99, "BLENDER-MINI": 59.99},
    "observations": [
        {"sku": "BLENDER-PRO", "seller": "KitchenDeals", "channel": "Amazon", "price": 119.99, "date": "2026-11-18"},
        {"sku": "BLENDER-PRO", "seller": "KitchenDeals", "channel": "Walmart", "price": 109.00, "date": "2026-11-19"},
        {"sku": "BLENDER-PRO", "seller": "HomeStore", "channel": "Own site", "price": 129.99, "date": "2026-11-19"},
        {"sku": "BLENDER-MINI", "seller": "BargainHub", "channel": "eBay", "price": 57.99, "date": "2026-11-20"},
        {"sku": "BLENDER-MINI", "seller": "HomeStore", "channel": "Own site", "price": 64.99, "date": "2026-11-20"},
    ],
}

STEPS = {1: "Send first MAP notice", 2: "Send written warning", 3: "Escalate per policy (e.g. pause supply / remove authorization)"}


def check(data):
    maps = data["map_prices"]
    tol = float(data.get("tolerance", 0.01))
    minor, major = data.get("severity_thresholds", [0.05, 0.15])
    violations, unknown = [], []
    for o in data["observations"]:
        for key in ("sku", "seller", "price"):
            if key not in o:
                raise ValueError(f"observation missing '{key}': {o}")
        if o["sku"] not in maps:
            unknown.append(o["sku"])
            continue
        map_price = float(maps[o["sku"]])
        price = float(o["price"])
        if price < map_price - tol:
            gap = map_price - price
            pct = gap / map_price
            severity = "minor" if pct < minor else "major" if pct <= major else "severe"
            violations.append({**o, "map": map_price, "gap": round(gap, 2), "gap_pct": round(pct, 4), "severity": severity})
    counts = Counter(v["seller"] for v in violations)
    by_seller = defaultdict(list)
    for v in violations:
        by_seller[v["seller"]].append(v)
    sellers = []
    for seller, n in counts.most_common():
        sellers.append({"seller": seller, "violations": n,
                        "channels": sorted({v.get("channel", "?") for v in by_seller[seller]}),
                        "worst_gap_pct": max(v["gap_pct"] for v in by_seller[seller]),
                        "next_step": STEPS[min(n, 3)]})
    return {"observations": len(data["observations"]), "violations": violations, "sellers": sellers,
            "compliance_rate": round(1 - len(violations) / len(data["observations"]), 4) if data["observations"] else None,
            "skus_without_map": sorted(set(unknown))}


def format_report(r):
    out = [f"MAP check: {len(r['violations'])} violation(s) in {r['observations']} observation(s) "
           f"(compliance {r['compliance_rate']*100:.1f}%)", "",
           "| SKU | Seller | Channel | Price | MAP | Gap | Severity | Date |",
           "|-----|--------|---------|-------|-----|-----|----------|------|"]
    for v in r["violations"]:
        out.append(f"| {v['sku']} | {v['seller']} | {v.get('channel', '')} | ${float(v['price']):.2f} | ${v['map']:.2f} | "
                   f"-${v['gap']:.2f} ({v['gap_pct']*100:.1f}%) | {v['severity']} | {v.get('date', '')} |")
    out += ["", "| Seller | Violations | Channels | Worst gap | Next step |", "|--------|------------|----------|-----------|-----------|"]
    out += [f"| {s['seller']} | {s['violations']} | {', '.join(s['channels'])} | {s['worst_gap_pct']*100:.1f}% | {s['next_step']} |"
            for s in r["sellers"]]
    if r["skus_without_map"]:
        out.append(f"\nNo MAP defined for: {', '.join(r['skus_without_map'])}")
    out.append("\nPrices are as observed (keep screenshots with date and URL as evidence); "
               "severity thresholds and enforcement steps are policy choices, not legal advice.")
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        r = check(json.loads(args[0]) if args else DEMO)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else format_report(r))


if __name__ == "__main__":
    main()

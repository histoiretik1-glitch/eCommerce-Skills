#!/usr/bin/env python3
"""
Google Shopping / Performance Max product segmentation from a product performance report.

Input (rows from Google Ads > Products report or Merchant Center performance, one period):
  {"target_roas": 4.0, "min_clicks": 100,
   "products": [{"id": "SKU-1", "title": "Linen apron", "clicks": 820, "cost": 410.0,
                 "conversions": 41, "conv_value": 2050.0}]}

Buckets (a common segmentation for splitting asset groups / campaigns; thresholds are inputs):
  hero      ROAS >= target and conversions >= 10           -> own asset group, raise budget
  sidekick  ROAS >= target and conversions < 10            -> keep, more data
  villain   ROAS < target and clicks >= min_clicks         -> lower tROAS priority, fix price/feed/page, or exclude
  zombie    clicks < min_clicks                            -> low visibility: check feed title, price, disapprovals
ROAS = conv_value / cost; CPC = cost / clicks; CVR = conversions / clicks
Usage:
  python3 scripts/product_buckets.py '<json>' [--json]
Standard library only.
"""
import json
import sys


def bucket(d):
    target, min_clicks = float(d["target_roas"]), float(d.get("min_clicks", 100))
    out = []
    for p in d["products"]:
        clicks, cost = float(p.get("clicks", 0)), float(p.get("cost", 0))
        conv, value = float(p.get("conversions", 0)), float(p.get("conv_value", 0))
        roas = value / cost if cost else None
        if clicks < min_clicks:
            b = "zombie"
        elif roas is not None and roas >= target:
            b = "hero" if conv >= 10 else "sidekick"
        else:
            b = "villain"
        out.append({**p, "roas": round(roas, 2) if roas is not None else None,
                    "cpc": round(cost / clicks, 2) if clicks else None,
                    "cvr": round(conv / clicks, 4) if clicks else None, "bucket": b})
    order = {"hero": 0, "sidekick": 1, "villain": 2, "zombie": 3}
    out.sort(key=lambda x: (order[x["bucket"]], -(x["roas"] or 0)))
    totals = {}
    for p in out:
        t = totals.setdefault(p["bucket"], {"products": 0, "cost": 0.0, "conv_value": 0.0})
        t["products"] += 1
        t["cost"] += float(p.get("cost", 0))
        t["conv_value"] += float(p.get("conv_value", 0))
    for t in totals.values():
        t["roas"] = round(t["conv_value"] / t["cost"], 2) if t["cost"] else None
        t["cost"], t["conv_value"] = round(t["cost"], 2), round(t["conv_value"], 2)
    return {"target_roas": target, "products": out, "buckets": totals}


def report(r):
    lines = ["| Product | Clicks | Cost | Conv. | Value | ROAS | CPC | CVR | Bucket |", "|---|---|---|---|---|---|---|---|---|"]
    for p in r["products"]:
        lines.append(f"| {p.get('title') or p['id']} | {p.get('clicks', 0):g} | ${float(p.get('cost', 0)):,.2f} | {p.get('conversions', 0):g} | "
                     f"${float(p.get('conv_value', 0)):,.2f} | {p['roas'] if p['roas'] is not None else '-'} | "
                     f"{'-' if p['cpc'] is None else '$%.2f' % p['cpc']} | {'-' if p['cvr'] is None else '%.1f%%' % (p['cvr']*100)} | {p['bucket']} |")
    lines.append("\nBucket totals: " + "; ".join(f"{b} {t['products']} products, cost ${t['cost']:,.2f}, ROAS {t['roas']}"
                                                for b, t in r["buckets"].items()))
    lines.append(f"Target ROAS {r['target_roas']}. Conversion value follows your Google Ads conversion settings and attribution model.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = bucket(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
TikTok Shop LIVE session metrics - compare sessions from the LIVE dashboard.

Input: one row per LIVE session, copied from TikTok Shop Seller Center / LIVE Manager
(names of fields may differ slightly in your dashboard):
  {"sessions": [{"date": "2026-11-18", "start_hour": 19, "duration_min": 120,
                 "views": 15400, "avg_view_seconds": 48, "product_impressions": 9800,
                 "product_clicks": 610, "orders": 92, "gmv": 2760.0,
                 "new_followers": 140, "comments": 830}]}

Metrics per session:
  GPM                = GMV / views x 1000           (GMV per 1,000 views, TikTok's LIVE efficiency metric)
  GMV per hour       = GMV / (duration_min / 60)
  product CTR        = product_clicks / product_impressions
  click-to-order     = orders / product_clicks
  orders per 1k views= orders / views x 1000
  comments per 1k views, followers per hour, AOV = GMV / orders
The report ranks sessions by GPM and shows the median of each metric, so the seller can
see which start hours, durations or formats work best.

Usage:
  python3 scripts/live_metrics.py '<json>'
  python3 scripts/live_metrics.py '<json>' --json
Standard library only. No demo mode.
"""
import json
import statistics
import sys

FIELDS = {"date", "start_hour", "duration_min", "views", "avg_view_seconds", "product_impressions",
          "product_clicks", "orders", "gmv", "new_followers", "comments", "label"}
REQUIRED = {"date", "duration_min", "views", "orders", "gmv"}


def metrics(s):
    bad = sorted(set(s) - FIELDS)
    missing = sorted(REQUIRED - set(s))
    if bad or missing:
        raise ValueError(f"session {s.get('date', '?')}: missing {missing}, unknown {bad}")
    views, gmv, orders = float(s["views"]), float(s["gmv"]), float(s["orders"])
    hours = float(s["duration_min"]) / 60
    if views <= 0 or hours <= 0:
        raise ValueError("views and duration_min must be > 0")
    clicks, imps = float(s.get("product_clicks", 0)), float(s.get("product_impressions", 0))
    return {**s, "gpm": round(gmv / views * 1000, 2), "gmv_per_hour": round(gmv / hours, 2),
            "product_ctr": round(clicks / imps, 4) if imps else None,
            "click_to_order": round(orders / clicks, 4) if clicks else None,
            "orders_per_1k_views": round(orders / views * 1000, 2),
            "comments_per_1k_views": round(float(s.get("comments", 0)) / views * 1000, 1),
            "followers_per_hour": round(float(s.get("new_followers", 0)) / hours, 1),
            "aov": round(gmv / orders, 2) if orders else None}


def analyze(d):
    rows = sorted((metrics(s) for s in d["sessions"]), key=lambda r: -r["gpm"])
    if not rows:
        raise ValueError("no sessions")
    med = {k: statistics.median([r[k] for r in rows if r[k] is not None])
           for k in ("gpm", "gmv_per_hour", "orders_per_1k_views") if any(r[k] is not None for r in rows)}
    return {"sessions": rows, "medians": med}


def report(r):
    pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
    lines = ["| Date | Start | Duration | Views | GMV | GPM | GMV/h | Product CTR | Click→order | AOV |",
             "|------|-------|----------|-------|-----|-----|-------|-------------|-------------|-----|"]
    for s in r["sessions"]:
        lines.append(f"| {s['date']} | {s.get('start_hour', '-')}h | {s['duration_min']} min | {s['views']:,} | ${s['gmv']:,.2f} | "
                     f"${s['gpm']} | ${s['gmv_per_hour']:,.2f} | {pct(s['product_ctr'])} | {pct(s['click_to_order'])} | "
                     f"{'-' if s['aov'] is None else '$%.2f' % s['aov']} |")
    lines.append(f"\nMedians: GPM ${r['medians'].get('gpm')}, GMV/hour ${r['medians'].get('gmv_per_hour')}, "
                 f"orders per 1k views {r['medians'].get('orders_per_1k_views')}")
    lines.append("Computed from the session figures you provided (verified from your LIVE dashboard for those dates).")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = analyze(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError, statistics.StatisticsError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

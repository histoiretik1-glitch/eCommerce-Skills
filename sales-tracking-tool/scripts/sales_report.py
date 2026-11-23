#!/usr/bin/env python3
"""
Multichannel sales report - revenue, units, contribution margin by channel, SKU and period
from one CSV that merges the order exports of every channel.

CSV columns (one row per order line or per day/SKU/channel aggregate):
  date (YYYY-MM-DD), channel, sku, units, revenue            required
  cost, fees, ad_spend                                       optional (0 if absent)
    cost     = landed product cost of the units
    fees     = marketplace / payment / fulfilment fees
    ad_spend = advertising attributed to that row (or put channel-level ad spend on a row with sku "ADS")

Metrics:
  contribution = revenue - cost - fees - ad_spend; contribution margin = contribution / revenue
  average selling price = revenue / units; share of revenue per channel
  period growth = (last period - previous period) / previous period, periods = month (default) or ISO week

Usage:
  python3 scripts/sales_report.py sales.csv [--period week] [--top 10] [--json]
Standard library only. No demo mode: it only reads the file you give.
"""
import csv
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

REQUIRED = ("date", "channel", "sku", "units", "revenue")
MONEY = ("revenue", "cost", "fees", "ad_spend")


def num(v):
    v = (v or "").replace(",", "").replace("$", "").strip()
    return float(v) if v else 0.0


def period_key(date, period):
    d = dt.date.fromisoformat(date.strip()[:10])
    if period == "week":
        y, w, _ = d.isocalendar()
        return f"{y}-W{w:02d}"
    return f"{d.year}-{d.month:02d}"


def load(path, period):
    rows = list(csv.DictReader(Path(path).read_text(encoding="utf-8-sig").splitlines()))
    if not rows:
        raise ValueError("empty file")
    missing = [c for c in REQUIRED if c not in rows[0]]
    if missing:
        raise ValueError(f"missing column(s): {', '.join(missing)}")
    out = []
    for i, r in enumerate(rows, start=2):
        try:
            out.append({"period": period_key(r["date"], period), "channel": r["channel"].strip(), "sku": r["sku"].strip(),
                        "units": num(r["units"]), **{k: num(r.get(k)) for k in MONEY}})
        except ValueError as e:
            raise ValueError(f"line {i}: {e}")
    return out


def summarize(rows, key):
    agg = defaultdict(lambda: {"units": 0.0, **{k: 0.0 for k in MONEY}})
    for r in rows:
        a = agg[r[key]]
        a["units"] += r["units"]
        for k in MONEY:
            a[k] += r[k]
    total = sum(a["revenue"] for a in agg.values()) or 1
    out = {}
    for k, a in agg.items():
        contrib = a["revenue"] - a["cost"] - a["fees"] - a["ad_spend"]
        out[k] = {"units": round(a["units"], 2), "revenue": round(a["revenue"], 2), "contribution": round(contrib, 2),
                  "contribution_margin": round(contrib / a["revenue"], 4) if a["revenue"] else None,
                  "asp": round(a["revenue"] / a["units"], 2) if a["units"] else None,
                  "share_of_revenue": round(a["revenue"] / total, 4)}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["revenue"]))


def report_data(rows, top):
    periods = sorted({r["period"] for r in rows})
    by_period = summarize(rows, "period")
    growth = None
    if len(periods) >= 2:
        last, prev = by_period[periods[-1]]["revenue"], by_period[periods[-2]]["revenue"]
        growth = round((last - prev) / prev, 4) if prev else None
    skus = summarize([r for r in rows if r["sku"].upper() != "ADS"], "sku")
    return {"periods": periods, "by_channel": summarize(rows, "channel"),
            "by_period": dict(sorted(by_period.items())), "last_period_growth": growth,
            "top_skus": dict(list(skus.items())[:top]),
            "loss_making_skus": [k for k, v in skus.items() if v["contribution"] < 0]}


def table(title, data):
    pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
    lines = [f"### {title}", "", "| Key | Units | Revenue | Contribution | Margin | ASP | Share |", "|---|---|---|---|---|---|---|"]
    for k, v in data.items():
        lines.append(f"| {k} | {v['units']:g} | ${v['revenue']:,.2f} | ${v['contribution']:,.2f} | {pct(v['contribution_margin'])} | "
                     f"{'-' if v['asp'] is None else '$%.2f' % v['asp']} | {pct(v['share_of_revenue'])} |")
    return lines


def report(d):
    lines = table("By channel", d["by_channel"]) + [""] + table("By period", d["by_period"]) + [""] + table("Top SKUs", d["top_skus"])
    if d["last_period_growth"] is not None:
        lines.append(f"\nRevenue growth {d['periods'][-2]} -> {d['periods'][-1]}: {d['last_period_growth']*100:+.1f}%"
                     " (a partial last period understates growth: compare complete periods only)")
    if d["loss_making_skus"]:
        lines.append("Loss-making SKUs after cost, fees and ads: " + ", ".join(d["loss_making_skus"]))
    lines.append("\nComputed from the file you provided; contribution excludes overheads (salaries, rent, software).")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    period = "week" if "--period" in sys.argv and "week" in sys.argv else "month"
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 10
    args = [a for a in args if a not in ("week", "month", str(top))]
    try:
        d = report_data(load(args[0], period), top)
    except (ValueError, OSError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(d, indent=2) if "--json" in sys.argv else report(d))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Walmart Connect Sponsored Products report analysis - keyword and item decisions.

Input: rows exported from Walmart Connect (Ad Center) for one period, plus the seller's
margin before ads (price - item cost - referral fee - WFS/fulfillment - returns):
  {"margin_before_ads": 0.30,          # fraction of the sale price (from profit-margin-calculator-walmart)
   "target_acos": 0.20,                # optional: target ad cost of sale; default = 2/3 of the margin
   "min_clicks": 20,                   # optional: minimum clicks before judging a row (default 20)
   "rows": [{"keyword": "storage bins", "match": "phrase", "impressions": 18000, "clicks": 260,
             "ad_spend": 182.0, "attributed_sales": 980.0, "units": 38}]}

Metrics per row: CTR, CPC, conversion (units / clicks), ROAS (sales / spend), ACoS (spend / sales).
  break-even ACoS = margin_before_ads     (above it, every attributed sale loses money)
  target ROAS     = 1 / target_acos
Decision rules (stated, not Walmart rules):
  clicks < min_clicks                      -> "collect more data"
  no sales and clicks >= min_clicks        -> "pause or add as negative keyword"
  ACoS > break-even                        -> "lower bid"
  ACoS <= target ACoS                      -> "raise bid / scale"
  otherwise                                -> "keep"

Usage:
  python3 scripts/connect_report.py '<json>'
  python3 scripts/connect_report.py '<json>' --json
Standard library only. No demo mode.
"""
import json
import sys

ALLOWED = {"margin_before_ads", "target_acos", "min_clicks", "rows"}
ROW = {"keyword", "item", "match", "campaign", "impressions", "clicks", "ad_spend", "attributed_sales", "units"}


def analyze(d):
    unknown = sorted(set(d) - ALLOWED)
    if unknown or "margin_before_ads" not in d or "rows" not in d:
        raise ValueError(f"need margin_before_ads and rows; unknown: {unknown}")
    margin = float(d["margin_before_ads"])
    if not 0 < margin < 1:
        raise ValueError("margin_before_ads must be a fraction between 0 and 1")
    target = float(d.get("target_acos", margin * 2 / 3))
    min_clicks = int(d.get("min_clicks", 20))
    out = []
    totals = {"ad_spend": 0.0, "attributed_sales": 0.0, "clicks": 0.0, "impressions": 0.0, "units": 0.0}
    for r in d["rows"]:
        bad = sorted(set(r) - ROW)
        if bad:
            raise ValueError(f"unknown row field(s): {bad}. Allowed: {', '.join(sorted(ROW))}")
        imp, clicks = float(r.get("impressions", 0)), float(r.get("clicks", 0))
        spend, sales, units = float(r.get("ad_spend", 0)), float(r.get("attributed_sales", 0)), float(r.get("units", 0))
        for k, v in (("ad_spend", spend), ("attributed_sales", sales), ("clicks", clicks), ("impressions", imp), ("units", units)):
            totals[k] += v
        acos = spend / sales if sales else None
        if clicks < min_clicks:
            decision = "collect more data"
        elif sales == 0:
            decision = "pause or add as negative keyword"
        elif acos > margin:
            decision = "lower bid"
        elif acos <= target:
            decision = "raise bid / scale"
        else:
            decision = "keep"
        out.append({**r, "ctr": round(clicks / imp, 4) if imp else None, "cpc": round(spend / clicks, 2) if clicks else None,
                    "conversion": round(units / clicks, 4) if clicks else None, "roas": round(sales / spend, 2) if spend else None,
                    "acos": round(acos, 4) if acos is not None else None, "decision": decision})
    t = totals
    summary = {"break_even_acos": margin, "target_acos": round(target, 4), "target_roas": round(1 / target, 2),
               "total_spend": round(t["ad_spend"], 2), "total_sales": round(t["attributed_sales"], 2),
               "total_roas": round(t["attributed_sales"] / t["ad_spend"], 2) if t["ad_spend"] else None,
               "total_acos": round(t["ad_spend"] / t["attributed_sales"], 4) if t["attributed_sales"] else None}
    return {"summary": summary, "rows": out}


def report(r):
    s = r["summary"]
    pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
    lines = [f"Walmart Connect — break-even ACoS {pct(s['break_even_acos'])}, target ACoS {pct(s['target_acos'])} "
             f"(target ROAS {s['target_roas']}); total spend ${s['total_spend']:.2f}, sales ${s['total_sales']:.2f}, "
             f"ROAS {s['total_roas']}, ACoS {pct(s['total_acos'])}", "",
             "| Keyword / item | Match | Clicks | CTR | CPC | Conversion | ROAS | ACoS | Decision |",
             "|----------------|-------|--------|-----|-----|------------|------|------|----------|"]
    for x in r["rows"]:
        lines.append(f"| {x.get('keyword') or x.get('item', '')} | {x.get('match', '')} | {x.get('clicks', 0):g} | {pct(x['ctr'])} | "
                     f"{'-' if x['cpc'] is None else '$%.2f' % x['cpc']} | {pct(x['conversion'])} | {x['roas'] if x['roas'] is not None else '-'} | "
                     f"{pct(x['acos'])} | {x['decision']} |")
    lines.append("\nAttributed sales follow Walmart Connect's attribution model for the exported period; "
                 "decision thresholds are the rules stated in the script, not Walmart rules.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = analyze(json.loads(args[0]))
    except (ValueError, TypeError, ZeroDivisionError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

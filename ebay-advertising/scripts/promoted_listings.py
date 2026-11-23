#!/usr/bin/env python3
"""
eBay Promoted Listings - break-even ad rate (General, cost per sale) and max cost per
click (Priority, cost per click), plus performance of listings from the seller's report.

Input:
  {"price_total": 45.0,                # typical sale total (item + shipping) charged to the buyer
   "profit_before_ads": 9.5,           # profit per sale after item cost, eBay fees and shipping, before ads
   "conversion_rate": 0.02,            # optional: clicks -> sales, for the Priority max CPC
   "listings": [                       # optional: rows from the Promoted Listings report
     {"listing": "Vintage lens 50mm", "campaign": "general", "ad_rate": 0.06,
      "impressions": 12000, "clicks": 240, "sold": 6, "sales": 270.0, "ad_fees": 16.2}]}

Formulas:
  General (cost per sale): the ad fee = ad rate x sale total, charged only on attributed sales.
      break-even ad rate = profit_before_ads / price_total
  Priority (cost per click): you pay per click.
      max CPC = conversion_rate x profit_before_ads
  Per listing: CTR = clicks / impressions, conversion = sold / clicks,
               ROAS = sales / ad_fees, ad cost of sale = ad_fees / sales,
               profit after ads = sold x profit_before_ads - ad_fees

Usage:
  python3 scripts/promoted_listings.py '<json>'
  python3 scripts/promoted_listings.py '<json>' --json
Standard library only. No demo mode.
"""
import json
import sys

ALLOWED = {"price_total", "profit_before_ads", "conversion_rate", "listings"}
ROW = {"listing", "campaign", "ad_rate", "impressions", "clicks", "sold", "sales", "ad_fees"}


def analyze(d):
    unknown = sorted(set(d) - ALLOWED)
    if unknown or "price_total" not in d or "profit_before_ads" not in d:
        raise ValueError(f"need price_total and profit_before_ads; unknown: {unknown}")
    price, profit = float(d["price_total"]), float(d["profit_before_ads"])
    if price <= 0:
        raise ValueError("price_total must be > 0")
    out = {"break_even_ad_rate": round(profit / price, 4)}
    if d.get("conversion_rate") is not None:
        out["max_cpc_priority"] = round(float(d["conversion_rate"]) * profit, 2)
    rows = []
    for r in d.get("listings", []):
        bad = sorted(set(r) - ROW)
        if bad:
            raise ValueError(f"unknown listing field(s): {bad}. Allowed: {', '.join(sorted(ROW))}")
        imp, clicks, sold = float(r.get("impressions", 0)), float(r.get("clicks", 0)), float(r.get("sold", 0))
        sales, fees = float(r.get("sales", 0)), float(r.get("ad_fees", 0))
        profit_after = sold * profit - fees
        if sold == 0 and fees > 0:
            action = "pause or fix the listing (spend without sales)"
        elif r.get("campaign") == "general" and r.get("ad_rate") is not None and float(r["ad_rate"]) > out["break_even_ad_rate"]:
            action = "lower the ad rate below break-even"
        elif profit_after > 0:
            action = "keep; test a slightly higher rate/bid for more visibility"
        else:
            action = "reduce rate/bid"
        rows.append({**r, "ctr": round(clicks / imp, 4) if imp else None,
                     "conversion": round(sold / clicks, 4) if clicks else None,
                     "roas": round(sales / fees, 2) if fees else None,
                     "ad_cost_of_sale": round(fees / sales, 4) if sales else None,
                     "profit_after_ads": round(profit_after, 2), "action": action})
    out["listings"] = rows
    return out


def report(r):
    lines = [f"Break-even General ad rate: {r['break_even_ad_rate']*100:.1f}% of the sale total"]
    if "max_cpc_priority" in r:
        lines.append(f"Max Priority CPC at your conversion rate: ${r['max_cpc_priority']:.2f}")
    if r["listings"]:
        lines += ["", "| Listing | Campaign | CTR | Conversion | ROAS | Ad cost of sale | Profit after ads | Action |",
                  "|---------|----------|-----|------------|------|-----------------|------------------|--------|"]
        pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
        for x in r["listings"]:
            lines.append(f"| {x.get('listing', '')} | {x.get('campaign', '')} | {pct(x['ctr'])} | {pct(x['conversion'])} | "
                         f"{x['roas'] if x['roas'] is not None else '-'} | {pct(x['ad_cost_of_sale'])} | ${x['profit_after_ads']:.2f} | {x['action']} |")
    lines.append("\nBased on the figures you entered and your Promoted Listings report (verified for that period).")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = analyze(json.loads(args[0]))
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

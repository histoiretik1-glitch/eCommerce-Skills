#!/usr/bin/env python3
"""
eBay sold-listing analysis - sell-through rate, sold price distribution and net proceeds.

Input: data the seller collected from eBay Seller Hub > Research (Terapeak) or from
eBay search with the "Sold items" / "Completed items" filters, for one product:
  {"item": "Canon AE-1 film camera",
   "period_days": 90,
   "active_listings": 140,                       # listings currently live for the same product
   "sold": [{"price": 165.0, "shipping": 0}, {"price": 149.99, "shipping": 12.5}, ...],
   "final_value_rate": 0.136,                    # YOUR category rate from eBay's fee page (required)
   "per_order_fee": 0.40,                        # YOUR per-order fee from eBay's fee page (required)
   "item_cost": 70.0, "shipping_cost": 12.0}     # your landed cost and label cost per sale

Metrics:
  sell_through_rate = sold count / (sold count + active listings)     (Terapeak-style STR)
  sales_per_day     = sold count / period_days
  sold total        = price + shipping paid by the buyer; quartiles and median
  final value fee   = final_value_rate x sold total + per_order_fee   (eBay charges the
                      percentage on the total amount of the sale; sales tax is ignored here)
  net per sale      = median sold total - final value fee - item_cost - shipping_cost

Usage:
  python3 scripts/sold_analysis.py '<json>'
  python3 scripts/sold_analysis.py '<json>' --json
Standard library only. There is no demo mode: the script only analyzes data you provide.
"""
import json
import statistics
import sys

REQUIRED = ("item", "period_days", "active_listings", "sold", "final_value_rate", "per_order_fee")
OPTIONAL = ("item_cost", "shipping_cost")


def analyze(d):
    missing = [k for k in REQUIRED if k not in d]
    unknown = sorted(set(d) - set(REQUIRED) - set(OPTIONAL))
    if missing or unknown:
        raise ValueError(f"missing: {missing}; unknown: {unknown}. Required: {', '.join(REQUIRED)}")
    if not 0 <= float(d["final_value_rate"]) < 0.5:
        raise ValueError("final_value_rate must be a fraction, e.g. 0.136 for 13.6%")
    totals = sorted(float(s["price"]) + float(s.get("shipping", 0)) for s in d["sold"])
    if len(totals) < 2:
        raise ValueError("give at least 2 sold listings")
    n, active = len(totals), int(d["active_listings"])
    q1, median, q3 = statistics.quantiles(totals, n=4, method="inclusive")
    fvf = float(d["final_value_rate"]) * median + float(d["per_order_fee"])
    net = median - fvf - float(d.get("item_cost", 0)) - float(d.get("shipping_cost", 0))
    str_ = n / (n + active)
    return {
        "item": d["item"], "sold": n, "active_listings": active, "period_days": d["period_days"],
        "sell_through_rate": round(str_, 3), "sales_per_day": round(n / float(d["period_days"]), 2),
        "sold_total_min": totals[0], "sold_total_q1": round(q1, 2), "sold_total_median": round(median, 2),
        "sold_total_q3": round(q3, 2), "sold_total_max": totals[-1],
        "fee_at_median": round(fvf, 2), "net_per_sale_at_median": round(net, 2),
        "net_margin_at_median": round(net / median, 3),
        "competition": "high supply vs demand" if str_ < 0.4 else "balanced" if str_ < 0.6 else "demand exceeds supply",
    }


def report(r):
    return "\n".join([
        f"eBay sold analysis — {r['item']} ({r['period_days']} days)", "",
        "| Metric | Value |", "|--------|-------|",
        f"| Sold / active listings | {r['sold']} / {r['active_listings']} |",
        f"| Sell-through rate | {r['sell_through_rate']*100:.1f}% ({r['competition']}) |",
        f"| Sales per day | {r['sales_per_day']} |",
        f"| Sold total (price + shipping): min / Q1 / median / Q3 / max | ${r['sold_total_min']:.2f} / ${r['sold_total_q1']:.2f} / "
        f"${r['sold_total_median']:.2f} / ${r['sold_total_q3']:.2f} / ${r['sold_total_max']:.2f} |",
        f"| eBay fees at median | ${r['fee_at_median']:.2f} |",
        f"| Net per sale at median | ${r['net_per_sale_at_median']:.2f} ({r['net_margin_at_median']*100:.1f}%) |",
        "", "Figures come only from the sold and active listings you provided (verified for that search date); "
            "fee rates are the ones you entered — check them on eBay's current fee page for your category.",
    ])


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

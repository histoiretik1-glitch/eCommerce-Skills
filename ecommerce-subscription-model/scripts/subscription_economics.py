#!/usr/bin/env python3
"""
Subscription unit economics: contribution per order, retention curve, LTV, LTV:CAC and CAC payback.

Input:
  {"price": 32.0,                  # subscription price per order (after the subscribe discount)
   "one_time_price": 36.0,         # optional: price of the same product bought once
   "orders_per_month": 1,          # 1 = monthly; 0.5 = every two months
   "cogs": 9.5, "fulfillment": 6.0, "payment_fee_rate": 0.03,
   "monthly_churn": 0.09,          # share of active subscribers cancelling each month (from your data)
   "cac": 45.0,                    # acquisition cost per new subscriber
   "horizon_months": 24}           # optional cap for the LTV (default 36)

Formulas:
  contribution per order = price x (1 - payment_fee_rate) - cogs - fulfillment
  monthly contribution   = contribution per order x orders_per_month
  survival after m months= (1 - churn)^m;   expected lifetime (uncapped) = 1 / churn months
  LTV (capped)           = sum over m=0..horizon-1 of monthly contribution x (1 - churn)^m
  CAC payback            = first month where cumulative expected contribution >= CAC
  max churn for LTV:CAC = 3 (uncapped) = monthly contribution / (3 x CAC)
  discount cost          = (one_time_price - price) per order, vs extra orders from retention
Usage:
  python3 scripts/subscription_economics.py '<json>' [--json]
Standard library only. Churn is assumed constant; real churn is usually higher in the first months.
"""
import json
import sys

ALLOWED = {"price", "one_time_price", "orders_per_month", "cogs", "fulfillment", "payment_fee_rate", "monthly_churn",
           "cac", "horizon_months"}


def analyze(d):
    unknown = sorted(set(d) - ALLOWED)
    if unknown:
        raise ValueError(f"unknown field(s): {unknown}")
    churn = float(d["monthly_churn"])
    if not 0 < churn < 1:
        raise ValueError("monthly_churn must be a fraction between 0 and 1, e.g. 0.09")
    per_order = float(d["price"]) * (1 - float(d.get("payment_fee_rate", 0))) - float(d["cogs"]) - float(d.get("fulfillment", 0))
    monthly = per_order * float(d.get("orders_per_month", 1))
    horizon = int(d.get("horizon_months", 36))
    cac = float(d["cac"])
    ltv, cum, payback = 0.0, 0.0, None
    for m in range(horizon):
        cum += monthly * (1 - churn) ** m
        if payback is None and cum >= cac:
            payback = m + 1
    ltv = cum
    out = {"contribution_per_order": round(per_order, 2), "monthly_contribution": round(monthly, 2),
           "expected_lifetime_months": round(1 / churn, 1),
           "survival": {f"month_{m}": round((1 - churn) ** m, 3) for m in (1, 3, 6, 12)},
           "ltv_capped": round(ltv, 2), "horizon_months": horizon, "ltv_uncapped": round(monthly / churn, 2),
           "ltv_to_cac": round(ltv / cac, 2) if cac else None, "cac_payback_months": payback,
           "max_churn_for_ltv_cac_3": round(monthly / (3 * cac), 4) if cac else None}
    if d.get("one_time_price") is not None:
        out["discount_per_order"] = round(float(d["one_time_price"]) - float(d["price"]), 2)
    return out


def report(r):
    s = r["survival"]
    lines = [
        "| Metric | Value |", "|---|---|",
        f"| Contribution per order / per month | ${r['contribution_per_order']:.2f} / ${r['monthly_contribution']:.2f} |",
        f"| Expected lifetime (1/churn) | {r['expected_lifetime_months']} months |",
        f"| Still subscribed after 1 / 3 / 6 / 12 months | {s['month_1']*100:.0f}% / {s['month_3']*100:.0f}% / {s['month_6']*100:.0f}% / {s['month_12']*100:.0f}% |",
        f"| LTV over {r['horizon_months']} months (uncapped) | ${r['ltv_capped']:.2f} (${r['ltv_uncapped']:.2f}) |",
        f"| LTV:CAC | {r['ltv_to_cac']} |",
        f"| CAC payback | {r['cac_payback_months'] or 'not within horizon'} months |",
        f"| Max monthly churn for LTV:CAC 3 | {r['max_churn_for_ltv_cac_3']*100:.1f}% |",
    ]
    if "discount_per_order" in r:
        lines.append(f"| Subscribe discount given per order | ${r['discount_per_order']:.2f} |")
    lines.append("\nConstant churn assumed: replace it with your measured month-by-month retention when you have 6+ months of data.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = analyze(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

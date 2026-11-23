#!/usr/bin/env python3
"""
Cost of returns per SKU and the main return reasons.

Input:
  {"return_rate_alert": 0.10,
   "skus": [{"sku": "DRESS-M", "units_sold": 400, "units_returned": 72, "price": 59.0, "unit_cost": 18.0,
             "return_shipping": 7.5, "processing_cost": 3.0, "resellable_share": 0.8,
             "reasons": {"too small": 30, "not as pictured": 18, "changed mind": 24}}]}

Per SKU:
  return rate          = units_returned / units_sold
  cost per return      = return_shipping + processing_cost + (1 - resellable_share) x unit_cost
                         (the refunded price is not a cost: the sale is reversed)
  returns cost         = units_returned x cost per return
  margin before returns= (units_sold x (price - unit_cost))
  net margin           = (units_sold - units_returned) x (price - unit_cost) - returns cost
  returns cost as % of revenue kept, top reason share
Usage:
  python3 scripts/returns_cost.py '<json>' [--json]
Standard library only. Shipping to the customer and marketplace fee refunds are not modelled.
"""
import json
import sys

FIELDS = {"sku", "units_sold", "units_returned", "price", "unit_cost", "return_shipping", "processing_cost",
          "resellable_share", "reasons"}


def analyze(d):
    alert = float(d.get("return_rate_alert", 0.10))
    out, reasons_all = [], {}
    for s in d["skus"]:
        bad = sorted(set(s) - FIELDS)
        if bad:
            raise ValueError(f"unknown field(s) {bad}")
        sold, ret = float(s["units_sold"]), float(s["units_returned"])
        if sold <= 0 or ret > sold:
            raise ValueError(f"{s.get('sku')}: units_returned must be <= units_sold > 0")
        price, cost = float(s["price"]), float(s["unit_cost"])
        resell = float(s.get("resellable_share", 1))
        per_return = float(s.get("return_shipping", 0)) + float(s.get("processing_cost", 0)) + (1 - resell) * cost
        returns_cost = ret * per_return
        kept = sold - ret
        net = kept * (price - cost) - returns_cost
        reasons = s.get("reasons", {})
        total_r = sum(reasons.values())
        top = max(reasons, key=reasons.get) if reasons else None
        for k, v in reasons.items():
            reasons_all[k] = reasons_all.get(k, 0) + v
        out.append({"sku": s["sku"], "return_rate": round(ret / sold, 4), "cost_per_return": round(per_return, 2),
                    "returns_cost": round(returns_cost, 2), "margin_before_returns": round(sold * (price - cost), 2),
                    "net_margin": round(net, 2), "returns_cost_share_of_kept_revenue": round(returns_cost / (kept * price), 4) if kept else None,
                    "top_reason": top, "top_reason_share": round(reasons[top] / total_r, 4) if top else None,
                    "alert": ret / sold > alert})
    out.sort(key=lambda x: -x["returns_cost"])
    return {"return_rate_alert": alert, "skus": out, "reasons": dict(sorted(reasons_all.items(), key=lambda kv: -kv[1]))}


def report(r):
    pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
    lines = ["| SKU | Return rate | Cost/return | Returns cost | Margin before | Net margin | Top reason | Alert |",
             "|---|---|---|---|---|---|---|---|"]
    for s in r["skus"]:
        lines.append(f"| {s['sku']} | {pct(s['return_rate'])} | ${s['cost_per_return']:.2f} | ${s['returns_cost']:,.2f} | "
                     f"${s['margin_before_returns']:,.2f} | ${s['net_margin']:,.2f} | {s['top_reason'] or '-'} ({pct(s['top_reason_share'])}) | "
                     f"{'ABOVE ' + pct(r['return_rate_alert']) if s['alert'] else ''} |")
    if r["reasons"]:
        lines.append("\nReasons across SKUs: " + ", ".join(f"{k} {v}" for k, v in r["reasons"].items()))
    lines.append("Computed from the figures you entered (verified for their period); reason labels are as customers chose them.")
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

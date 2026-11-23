#!/usr/bin/env python3
"""
Shipping quote comparison with dimensional (volumetric) weight, plus shipping cost as a
share of order value. Works for any carrier: you enter the carriers' rate tables.

Input:
  {"package": {"length": 14, "width": 10, "height": 6, "weight": 2.2, "unit": "in/lb"},
   "order_value": 48.0,
   "carriers": [
     {"name": "Carrier A Ground", "dim_divisor": 139, "rates": [[1, 8.10], [2, 9.05], [3, 9.85], [5, 11.40]]},
     {"name": "Carrier B Economy", "dim_divisor": 166, "rates": [[1, 7.60], [2, 8.70], [3, 9.90], [5, 12.30]]}]}

  unit "in/lb": dimensions in inches, weight in pounds, weight rounded UP to the next whole pound
  unit "cm/kg": dimensions in centimetres, weight in kg, rounded UP to the next 0.5 kg
  dim_divisor: from the carrier's current rate guide (commonly 139 or 166 in/lb, 5000 or 6000 cm/kg)
  rates: [max billable weight, price] rows for ONE zone/service, sorted by weight (from the carrier)

  dimensional weight = L x W x H / divisor; billable weight = max(actual, dimensional), rounded up
  max box volume without dim weight = rounded actual weight x divisor (cubic in or cm)

Usage:
  python3 scripts/shipping_quote.py '<json>' [--json]
Standard library only. Prices are the ones you enter: the script does not know carrier tariffs.
"""
import json
import math
import sys


def round_up(w, unit):
    return math.ceil(w) if unit == "in/lb" else math.ceil(w * 2) / 2


def quote(d):
    p = d["package"]
    unit = p.get("unit", "in/lb")
    if unit not in ("in/lb", "cm/kg"):
        raise ValueError('unit must be "in/lb" or "cm/kg"')
    volume = float(p["length"]) * float(p["width"]) * float(p["height"])
    actual = float(p["weight"])
    out = []
    for c in d["carriers"]:
        dim = volume / float(c["dim_divisor"])
        billable = round_up(max(actual, dim), unit)
        rows = sorted((float(w), float(price)) for w, price in c["rates"])
        price = next((pr for w, pr in rows if billable <= w), None)
        # largest box volume whose dim weight stays at or below the rounded actual weight
        max_volume = round_up(actual, unit) * float(c["dim_divisor"])
        out.append({"carrier": c["name"], "dim_weight": round(dim, 2), "billable_weight": billable,
                    "max_box_volume_without_dim": round(max_volume, 1),
                    "dim_applies": dim > actual, "price": price,
                    "share_of_order": round(price / float(d["order_value"]), 4) if price is not None and d.get("order_value") else None})
    priced = [o for o in out if o["price"] is not None]
    best = min(priced, key=lambda o: o["price"])["carrier"] if priced else None
    return {"actual_weight": actual, "unit": unit, "quotes": out, "cheapest": best}


def report(r):
    u = "lb" if r["unit"] == "in/lb" else "kg"
    lines = ["| Carrier | Dim weight | Billable | Dim weight applies | Price | % of order |", "|---|---|---|---|---|---|"]
    for q in r["quotes"]:
        lines.append(f"| {q['carrier']} | {q['dim_weight']} {u} | {q['billable_weight']} {u} | {'yes' if q['dim_applies'] else 'no'} | "
                     f"{'over table' if q['price'] is None else '$%.2f' % q['price']} | "
                     f"{'-' if q['share_of_order'] is None else '%.1f%%' % (q['share_of_order']*100)} |")
    v = "in³" if r["unit"] == "in/lb" else "cm³"
    lines.append("\nLargest box that avoids dimensional weight: " + ", ".join(
        f"{q['carrier']} {q['max_box_volume_without_dim']:g} {v}" for q in r["quotes"]))
    lines.append(f"Actual weight {r['actual_weight']} {u}. Cheapest: {r['cheapest']}. "
                 "Rates are those you entered: confirm them in each carrier's current rate guide and your negotiated rates.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = quote(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, ZeroDivisionError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

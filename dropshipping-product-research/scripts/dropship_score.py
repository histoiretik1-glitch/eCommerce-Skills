#!/usr/bin/env python3
"""
Dropshipping product screening: unit economics, break-even ROAS / max CPA and a stated score.

Input:
  {"payment_fee_rate": 0.029, "payment_fee_fixed": 0.30, "platform_fee_rate": 0.0,
   "products": [{"name": "Dog cooling mat", "price": 39.99, "supplier_cost": 11.20, "shipping_cost": 4.80,
                 "shipping_days": 9, "return_risk": "low", "expected_cpa": 14.0}]}

  return_risk: "low" | "medium" | "high"  (sizing, fragility, electronics -> higher)
  expected_cpa: optional, your ad cost per purchase from tests or similar products

Formulas:
  landed cost          = supplier_cost + shipping_cost
  fees                 = price x (payment_fee_rate + platform_fee_rate) + payment_fee_fixed
  contribution before ads = price - landed cost - fees - return allowance
      return allowance = price x {low: 3%, medium: 8%, high: 15%}   (stated assumption, replace with your data)
  max CPA (break-even) = contribution before ads;  break-even ROAS = price / contribution before ads
  profit per order at expected CPA = contribution before ads - expected_cpa
Score (0-100, this skill's weights, not an industry standard):
  40 x min(gross margin % / 60%, 1) + 25 x shipping speed (<=7 days 1, <=12 days 0.6, else 0.2)
  + 20 x return risk (low 1, medium 0.5, high 0) + 15 x (1 if profit at expected CPA > 0 else 0; 0.5 if CPA unknown)
Usage:
  python3 scripts/dropship_score.py '<json>' [--json]
Standard library only.
"""
import json
import sys

RETURN_ALLOWANCE = {"low": 0.03, "medium": 0.08, "high": 0.15}
RETURN_SCORE = {"low": 1, "medium": 0.5, "high": 0}


def evaluate(d):
    pr, pf, plat = float(d.get("payment_fee_rate", 0.029)), float(d.get("payment_fee_fixed", 0.30)), float(d.get("platform_fee_rate", 0))
    out = []
    for p in d["products"]:
        risk = p.get("return_risk", "medium")
        if risk not in RETURN_ALLOWANCE:
            raise ValueError(f"{p.get('name')}: return_risk must be low, medium or high")
        price = float(p["price"])
        landed = float(p["supplier_cost"]) + float(p.get("shipping_cost", 0))
        fees = price * (pr + plat) + pf
        contrib = price - landed - fees - price * RETURN_ALLOWANCE[risk]
        gm = (price - landed) / price
        days = float(p.get("shipping_days", 14))
        speed = 1 if days <= 7 else 0.6 if days <= 12 else 0.2
        cpa = p.get("expected_cpa")
        profit = contrib - float(cpa) if cpa is not None else None
        ads = 0.5 if profit is None else (1 if profit > 0 else 0)
        score = 40 * min(gm / 0.6, 1) + 25 * speed + 20 * RETURN_SCORE[risk] + 15 * ads
        out.append({"name": p["name"], "landed_cost": round(landed, 2), "gross_margin": round(gm, 4),
                    "contribution_before_ads": round(contrib, 2), "max_cpa": round(contrib, 2),
                    "break_even_roas": round(price / contrib, 2) if contrib > 0 else None,
                    "profit_at_expected_cpa": round(profit, 2) if profit is not None else None,
                    "score": round(score, 1),
                    "verdict": "reject: no margin for ads" if contrib <= 0 else
                               "test" if score >= 70 else "test only with a clear angle" if score >= 50 else "skip"})
    return sorted(out, key=lambda x: -x["score"])


def money(v):
    return "-" if v is None else f"-${-v:.2f}" if v < 0 else f"${v:.2f}"


def report(rows):
    lines = ["| Product | Landed cost | Gross margin | Max CPA | Break-even ROAS | Profit at expected CPA | Score | Verdict |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['name']} | ${r['landed_cost']:.2f} | {r['gross_margin']*100:.1f}% | ${r['max_cpa']:.2f} | "
                     f"{r['break_even_roas'] or '-'} | {money(r['profit_at_expected_cpa'])} | "
                     f"{r['score']} | {r['verdict']} |")
    lines.append("\nReturn allowances and score weights are this script's stated assumptions; replace them with your own data.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = evaluate(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, ZeroDivisionError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

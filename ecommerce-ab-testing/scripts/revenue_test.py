#!/usr/bin/env python3
"""
A/B/n test read-out on conversion AND revenue per visitor, for any channel (site, email, ads,
marketplace experiments) from summary statistics.

Input:
  {"alpha": 0.05,
   "variants": [
     {"name": "control", "visitors": 12000, "conversions": 312, "revenue": 18720.0, "revenue_sq": 1650000.0},
     {"name": "B", "visitors": 11950, "conversions": 345, "revenue": 19320.0, "revenue_sq": 1590000.0}]}

  The first variant is the control. revenue_sq = sum over visitors of revenue^2 (0 for non-buyers);
  most analytics exports do not give it: compute it from order-level data (sum of order value squared,
  per visitor) or give "revenue_sd" (standard deviation of revenue per visitor) instead.

Tests (each variant vs control):
  conversion: two-proportion z-test
  revenue per visitor (RPV): Welch test on means, normal approximation (valid for large samples, n >= 1000)
  multiple variants: Bonferroni correction, alpha / (number of variants - 1)
Usage:
  python3 scripts/revenue_test.py '<json>' [--json]
Standard library only.
"""
import json
import math
import statistics
import sys

N = statistics.NormalDist()


def rpv_stats(v):
    n, rev = float(v["visitors"]), float(v["revenue"])
    mean = rev / n
    if "revenue_sd" in v:
        sd = float(v["revenue_sd"])
    elif "revenue_sq" in v:
        var = (float(v["revenue_sq"]) - n * mean ** 2) / (n - 1)
        if var < 0:
            raise ValueError(f"{v['name']}: revenue_sq too small for this revenue")
        sd = math.sqrt(var)
    else:
        raise ValueError(f"{v['name']}: give revenue_sq or revenue_sd")
    return n, mean, sd


def analyze(d):
    vs = d["variants"]
    if len(vs) < 2:
        raise ValueError("give a control and at least one variant")
    alpha = float(d.get("alpha", 0.05))
    adj = alpha / (len(vs) - 1)
    c = vs[0]
    n1, x1 = float(c["visitors"]), float(c["conversions"])
    p1 = x1 / n1
    _, m1, s1 = rpv_stats(c)
    out = []
    for v in vs[1:]:
        n2, x2 = float(v["visitors"]), float(v["conversions"])
        p2 = x2 / n2
        pool = (x1 + x2) / (n1 + n2)
        z_c = (p2 - p1) / math.sqrt(pool * (1 - pool) * (1 / n1 + 1 / n2))
        _, m2, s2 = rpv_stats(v)
        se = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
        z_r = (m2 - m1) / se
        pc, prv = 2 * (1 - N.cdf(abs(z_c))), 2 * (1 - N.cdf(abs(z_r)))
        zc = N.inv_cdf(1 - adj / 2)
        out.append({"variant": v["name"], "conversion": round(p2, 5), "conversion_lift": round((p2 - p1) / p1, 4),
                    "conversion_p": round(pc, 4), "rpv": round(m2, 3), "rpv_lift": round((m2 - m1) / m1, 4),
                    "rpv_p": round(prv, 4), "rpv_ci": [round(m2 - m1 - zc * se, 3), round(m2 - m1 + zc * se, 3)],
                    "aov": round(float(v["revenue"]) / x2, 2) if x2 else None,
                    "decision": ("winner on revenue" if prv < adj and m2 > m1 else
                                 "loser on revenue" if prv < adj else
                                 "conversion up, revenue unproven" if pc < adj and p2 > p1 else "no significant difference")})
    return {"alpha": alpha, "adjusted_alpha": round(adj, 4), "control": {"conversion": round(p1, 5), "rpv": round(m1, 3),
            "aov": round(float(c["revenue"]) / x1, 2) if x1 else None}, "variants": out}


def report(r):
    c = r["control"]
    lines = [f"Control: conversion {c['conversion']*100:.2f}%, RPV ${c['rpv']:.3f}, AOV ${c['aov']}. "
             f"Significance threshold per comparison: {r['adjusted_alpha']} (Bonferroni)", "",
             "| Variant | Conversion | Lift | p | RPV | RPV lift | p | RPV diff CI | AOV | Decision |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for v in r["variants"]:
        lines.append(f"| {v['variant']} | {v['conversion']*100:.2f}% | {v['conversion_lift']*100:+.1f}% | {v['conversion_p']} | "
                     f"${v['rpv']:.3f} | {v['rpv_lift']*100:+.1f}% | {v['rpv_p']} | [{v['rpv_ci'][0]:+.3f}, {v['rpv_ci'][1]:+.3f}] | "
                     f"${v['aov']} | {v['decision']} |")
    lines.append("\nRevenue test uses a normal approximation: only valid for large samples; revenue is skewed, so check a few "
                 "very large orders are not driving the result.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        r = analyze(json.loads(args[0]))
    except (ValueError, KeyError, TypeError, ZeroDivisionError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

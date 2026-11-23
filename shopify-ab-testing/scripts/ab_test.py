#!/usr/bin/env python3
"""
A/B test statistics for Shopify experiments (theme, product page, price or offer tests).

Two modes:
  plan:    {"mode": "plan", "baseline_rate": 0.025, "min_relative_lift": 0.15,
            "alpha": 0.05, "power": 0.8, "daily_sessions": 1800, "variants": 2}
           -> sessions needed per variant and estimated duration in days
  analyze: {"mode": "analyze", "control": {"sessions": 10400, "orders": 262},
            "variant": {"sessions": 10350, "orders": 301}, "alpha": 0.05,
            "expected_split": 0.5}
           -> conversion rates, absolute and relative lift, two-sided p-value (two-proportion
              z-test), 95% confidence interval of the difference, and a sample ratio mismatch
              (SRM) check on the traffic split (chi-square, p < 0.001 = broken split)

Formulas:
  n per variant = (z_{1-a/2} * sqrt(2 p_bar (1 - p_bar)) + z_{1-b} * sqrt(p1 (1-p1) + p2 (1-p2)))^2 / (p2 - p1)^2
  z = (p2 - p1) / sqrt(p_pool (1 - p_pool) (1/n1 + 1/n2)),  p-value = 2 (1 - Phi(|z|))
  CI = (p2 - p1) +/- z_{0.975} sqrt(p1 (1-p1)/n1 + p2 (1-p2)/n2)

Usage:
  python3 scripts/ab_test.py '<json>'
  python3 scripts/ab_test.py '<json>' --json
Standard library only.
"""
import json
import math
import statistics
import sys

N = statistics.NormalDist()


def plan(d):
    p1 = float(d["baseline_rate"])
    p2 = p1 * (1 + float(d["min_relative_lift"]))
    alpha, power = float(d.get("alpha", 0.05)), float(d.get("power", 0.8))
    if not (0 < p1 < 1 and 0 < p2 < 1):
        raise ValueError("rates must be between 0 and 1")
    za, zb = N.inv_cdf(1 - alpha / 2), N.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    n = (za * math.sqrt(2 * p_bar * (1 - p_bar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    n = math.ceil(n)
    out = {"mode": "plan", "baseline_rate": p1, "target_rate": round(p2, 5), "sessions_per_variant": n,
           "total_sessions": n * int(d.get("variants", 2))}
    if d.get("daily_sessions"):
        days = math.ceil(out["total_sessions"] / float(d["daily_sessions"]))
        out["days"] = max(days, 14)  # run at least two full weeks to cover weekday effects
        out["days_note"] = "at least 14 days to cover two full weekly cycles"
    return out


def analyze(d):
    c, v = d["control"], d["variant"]
    n1, x1, n2, x2 = float(c["sessions"]), float(c["orders"]), float(v["sessions"]), float(v["orders"])
    if min(n1, n2) <= 0 or x1 > n1 or x2 > n2:
        raise ValueError("sessions must be > 0 and orders <= sessions")
    p1, p2 = x1 / n1, x2 / n2
    pool = (x1 + x2) / (n1 + n2)
    se_pool = math.sqrt(pool * (1 - pool) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se_pool if se_pool else 0.0
    p_value = 2 * (1 - N.cdf(abs(z)))
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    zc = N.inv_cdf(0.975)
    split = float(d.get("expected_split", 0.5))
    exp1, exp2 = (n1 + n2) * split, (n1 + n2) * (1 - split)
    chi2 = (n1 - exp1) ** 2 / exp1 + (n2 - exp2) ** 2 / exp2
    srm_p = math.erfc(math.sqrt(chi2 / 2))  # chi-square with 1 degree of freedom
    alpha = float(d.get("alpha", 0.05))
    return {"mode": "analyze", "control_rate": round(p1, 5), "variant_rate": round(p2, 5),
            "absolute_lift": round(p2 - p1, 5), "relative_lift": round((p2 - p1) / p1, 4) if p1 else None,
            "z": round(z, 3), "p_value": round(p_value, 4), "significant": p_value < alpha,
            "ci95_difference": [round(p2 - p1 - zc * se, 5), round(p2 - p1 + zc * se, 5)],
            "srm_p_value": round(srm_p, 5), "srm_detected": srm_p < 0.001}


def report(r):
    if r["mode"] == "plan":
        s = (f"Plan: baseline {r['baseline_rate']*100:.2f}% -> detect {r['target_rate']*100:.2f}%: "
             f"{r['sessions_per_variant']:,} sessions per variant ({r['total_sessions']:,} total)")
        if "days" in r:
            s += f", about {r['days']} days ({r['days_note']})"
        return s
    verdict = ("STOP: traffic split is broken (SRM), results are not trustworthy" if r["srm_detected"]
               else "significant" if r["significant"] else "not significant: keep the control or keep collecting data")
    return "\n".join([
        f"Control {r['control_rate']*100:.2f}% vs variant {r['variant_rate']*100:.2f}% "
        f"(lift {r['absolute_lift']*100:+.2f} pts, {r['relative_lift']*100:+.1f}%)",
        f"p-value {r['p_value']} | 95% CI of the difference [{r['ci95_difference'][0]*100:+.2f}, {r['ci95_difference'][1]*100:+.2f}] pts",
        f"SRM check p-value {r['srm_p_value']} | Verdict: {verdict}",
    ])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        d = json.loads(args[0])
        r = plan(d) if d.get("mode") == "plan" else analyze(d) if d.get("mode") == "analyze" else None
        if r is None:
            raise ValueError('mode must be "plan" or "analyze"')
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

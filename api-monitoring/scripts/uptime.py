#!/usr/bin/env python3
"""
Uptime / SLO calculator - availability, error budget, latency percentiles and MTTR.

Input (from the seller's monitoring tool exports):
  {"period_days": 30, "slo": 0.999,
   "checks": [{"ok": true, "latency_ms": 180}, ...],                 # optional: synthetic or health checks
   "incidents": [{"start": "2026-11-03T10:00:00", "end": "2026-11-03T10:42:00", "service": "checkout"}]}

Metrics:
  availability (checks)  = ok checks / all checks
  error budget (minutes) = (1 - slo) * period_days * 1440
  downtime (minutes)     = sum of incident durations
  budget used            = downtime / error budget
  availability (time)    = 1 - downtime / period minutes
  MTTR                   = mean incident duration
  latency p50 / p95 / p99 from successful checks (nearest-rank method)

Usage:
  python3 scripts/uptime.py
  python3 scripts/uptime.py '<json>'
  python3 scripts/uptime.py '<json>' --json
Standard library only.
"""
import json
import math
import sys
from datetime import datetime

DEMO = {
    "period_days": 30, "slo": 0.999,
    "checks": [{"ok": True, "latency_ms": l} for l in (120, 135, 150, 160, 180, 210, 240, 300, 450, 900)] * 100
              + [{"ok": False, "latency_ms": None}] * 3,
    "incidents": [{"start": "2026-11-03T10:00:00", "end": "2026-11-03T10:22:00", "service": "payments API"},
                  {"start": "2026-11-17T02:10:00", "end": "2026-11-17T02:18:00", "service": "inventory webhook"}],
}


def percentile(values, p):
    """Nearest-rank percentile."""
    if not values:
        return None
    ordered = sorted(values)
    k = max(1, math.ceil(p / 100 * len(ordered)))
    return ordered[k - 1]


def analyze(data):
    period_min = float(data.get("period_days", 30)) * 1440
    slo = float(data.get("slo", 0.999))
    if not 0 < slo < 1:
        raise ValueError("slo must be between 0 and 1 (e.g. 0.999)")
    budget = (1 - slo) * period_min
    durations = []
    for inc in data.get("incidents", []):
        start, end = datetime.fromisoformat(inc["start"]), datetime.fromisoformat(inc["end"])
        if end < start:
            raise ValueError(f"incident ends before it starts: {inc}")
        durations.append((end - start).total_seconds() / 60)
    downtime = sum(durations)
    checks = data.get("checks", [])
    ok = [c for c in checks if c.get("ok")]
    lat = [float(c["latency_ms"]) for c in ok if c.get("latency_ms") is not None]
    return {
        "period_days": data.get("period_days", 30), "slo": slo,
        "checks": len(checks), "check_availability": round(len(ok) / len(checks), 5) if checks else None,
        "downtime_minutes": round(downtime, 1), "time_availability": round(1 - downtime / period_min, 5),
        "error_budget_minutes": round(budget, 1), "budget_used": round(downtime / budget, 3) if budget else None,
        "budget_left_minutes": round(budget - downtime, 1),
        "incidents": len(durations), "mttr_minutes": round(sum(durations) / len(durations), 1) if durations else None,
        "latency_p50_ms": percentile(lat, 50), "latency_p95_ms": percentile(lat, 95), "latency_p99_ms": percentile(lat, 99),
        "slo_met": downtime <= budget,
    }


def format_report(r):
    pct = lambda v: "n/a" if v is None else f"{v*100:.3f}%"
    lines = [
        f"Availability over {r['period_days']} days (SLO {r['slo']*100:.2f}%)", "",
        "| Metric | Value |", "|--------|-------|",
        f"| Availability (time, from incidents) | {pct(r['time_availability'])} |",
        f"| Availability (checks) | {pct(r['check_availability'])} over {r['checks']} checks |",
        f"| Downtime | {r['downtime_minutes']} min in {r['incidents']} incident(s) |",
        f"| Error budget | {r['error_budget_minutes']} min, used {r['budget_used']*100:.0f}%, left {r['budget_left_minutes']} min |",
        f"| MTTR | {r['mttr_minutes']} min |",
        f"| Latency p50 / p95 / p99 | {r['latency_p50_ms']} / {r['latency_p95_ms']} / {r['latency_p99_ms']} ms |",
        f"| SLO met | {'yes' if r['slo_met'] else 'NO'} |",
        "", "Figures are computed from the exported checks and incidents (verified for that data); "
            "gaps in monitoring coverage are not visible here.",
    ]
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        r = analyze(json.loads(args[0]) if args else DEMO)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else format_report(r))


if __name__ == "__main__":
    main()

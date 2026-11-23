#!/usr/bin/env python3
"""
Customer retention cohorts from an order list (any platform).

CSV columns: customer_id, order_date (YYYY-MM-DD...), revenue
  - customer_id: email hash, customer number or any stable id (do not paste raw emails if not needed)
  - one row per order (several rows of the same order must be summed beforehand)

Outputs:
  - cohort table: customers acquired per first-order month and the % of them who ordered again
    in month +1, +2, ... (month index = calendar months after the first order month)
  - repeat purchase rate = customers with 2+ orders / customers
  - median days between first and second order
  - cumulative revenue per customer by cohort (a historical LTV, not a forecast)

Usage:
  python3 scripts/cohorts.py orders.csv [--months 6] [--json]
Standard library only. Recent cohorts have fewer months of history: their empty cells are not zeros.
"""
import csv
import datetime as dt
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path


def month_index(d):
    return d.year * 12 + d.month - 1


def label(idx):
    return f"{idx // 12}-{idx % 12 + 1:02d}"


def load(path):
    rows = list(csv.DictReader(Path(path).read_text(encoding="utf-8-sig").splitlines()))
    if not rows or not {"customer_id", "order_date", "revenue"} <= set(rows[0]):
        raise ValueError("columns customer_id, order_date and revenue are required")
    orders = defaultdict(list)
    for i, r in enumerate(rows, start=2):
        cid = r["customer_id"].strip()
        if not cid:
            continue
        try:
            d = dt.date.fromisoformat(r["order_date"].strip()[:10])
            rev = float((r["revenue"] or "0").replace(",", "").replace("$", ""))
        except ValueError as e:
            raise ValueError(f"line {i}: {e}")
        orders[cid].append((d, rev))
    if not orders:
        raise ValueError("no orders")
    return {c: sorted(v) for c, v in orders.items()}


def analyze(orders, months=6):
    last_month = max(month_index(o[-1][0]) for o in orders.values())
    cohorts = defaultdict(list)
    for cid, o in orders.items():
        cohorts[month_index(o[0][0])].append(cid)
    table = {}
    for start, members in sorted(cohorts.items()):
        n = len(members)
        active, revenue = [], []
        for k in range(0, months + 1):
            if start + k > last_month:
                break
            buyers = sum(1 for c in members if any(month_index(d) == start + k for d, _ in orders[c]))
            active.append(round(buyers / n, 4))
            cum = sum(r for c in members for d, r in orders[c] if month_index(d) <= start + k)
            revenue.append(round(cum / n, 2))
        table[label(start)] = {"customers": n, "active_share_by_month": active, "cumulative_revenue_per_customer": revenue}
    repeaters = [o for o in orders.values() if len(o) >= 2]
    gaps = [(o[1][0] - o[0][0]).days for o in repeaters]
    return {"customers": len(orders), "orders": sum(len(o) for o in orders.values()),
            "repeat_purchase_rate": round(len(repeaters) / len(orders), 4),
            "median_days_to_second_order": statistics.median(gaps) if gaps else None,
            "cohorts": table}


def report(r):
    lines = [f"Customers {r['customers']}, orders {r['orders']}, repeat purchase rate {r['repeat_purchase_rate']*100:.1f}%, "
             f"median days to 2nd order {r['median_days_to_second_order']}", ""]
    width = max(len(c["active_share_by_month"]) for c in r["cohorts"].values())
    lines.append("| Cohort | Customers | " + " | ".join(f"M{k}" for k in range(width)) + " | Revenue/customer to date |")
    lines.append("|---|---|" + "---|" * width + "---|")
    for name, c in r["cohorts"].items():
        cells = [f"{v*100:.0f}%" for v in c["active_share_by_month"]] + [""] * (width - len(c["active_share_by_month"]))
        lines.append(f"| {name} | {c['customers']} | " + " | ".join(cells) + f" | ${c['cumulative_revenue_per_customer'][-1]:,.2f} |")
    lines.append("\nM0 is the first-order month (100% by definition). Blank cells: month not reached yet, not zero retention.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    months = int(sys.argv[sys.argv.index("--months") + 1]) if "--months" in sys.argv else 6
    args = [a for a in args if a != str(months)]
    try:
        r = analyze(load(args[0]), months)
    except (ValueError, OSError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(r, indent=2) if "--json" in sys.argv else report(r))


if __name__ == "__main__":
    main()

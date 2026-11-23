#!/usr/bin/env python3
"""
Shopify order export KPIs - revenue, AOV, repeat customers and monthly trend from the
CSV exported in Shopify admin (Orders > Export > "Plain CSV file").

Shopify's order export has one row per line item; order-level columns (Email, Total,
Discount Amount, Financial Status, Created at...) are filled on the first row of each
order. The script groups rows by the "Name" column (order number, e.g. #1001).

Columns used: Name, Email, Created at, Financial Status, Subtotal, Total, Discount Amount,
Refunded Amount (optional). Orders with Financial Status "voided" are excluded; refunded
amounts are subtracted from net revenue.

KPIs:
  orders, gross revenue (sum of Total), refunds, net revenue
  AOV (order total) = gross revenue / orders   (includes shipping and taxes)
  AOV (merchandise) = sum of Subtotal / orders (after discounts, before shipping and taxes;
                      the closest figure to the AOV shown in Shopify Analytics)
  customers = distinct emails; repeat customer rate = customers with 2+ orders / customers
  orders per customer, discount rate = discount amount / (subtotal + discount amount)
  revenue by month (YYYY-MM)

Usage:
  python3 scripts/orders_kpis.py orders_export.csv
  python3 scripts/orders_kpis.py orders_export.csv --json
Standard library only. Customer emails are only counted, never printed.
"""
import csv
import json
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path


def num(v):
    try:
        return float(str(v).replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def load_orders(path):
    text = Path(path).read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(text.splitlines()))
    if not rows or "Name" not in rows[0]:
        raise ValueError("not a Shopify order export (no 'Name' column)")
    orders = OrderedDict()
    for row in rows:
        name = row.get("Name", "").strip()
        if not name:
            continue
        if name not in orders:  # first row of the order carries the order-level fields
            orders[name] = row
    return orders


def kpis(orders):
    kept = {k: o for k, o in orders.items() if o.get("Financial Status", "").strip().lower() != "voided"}
    if not kept:
        raise ValueError("no orders after excluding voided ones")
    gross = sum(num(o.get("Total")) for o in kept.values())
    refunds = sum(num(o.get("Refunded Amount")) for o in kept.values())
    subtotal = sum(num(o.get("Subtotal")) for o in kept.values())
    discount = sum(num(o.get("Discount Amount")) for o in kept.values())
    per_customer = Counter(o.get("Email", "").strip().lower() for o in kept.values() if o.get("Email", "").strip())
    months = defaultdict(float)
    for o in kept.values():
        months[o.get("Created at", "")[:7]] += num(o.get("Total"))
    n = len(kept)
    customers = len(per_customer)
    return {
        "orders": n, "excluded_voided": len(orders) - n, "gross_revenue": round(gross, 2), "refunds": round(refunds, 2),
        "net_revenue": round(gross - refunds, 2), "aov": round(gross / n, 2),
        "aov_merchandise": round(subtotal / n, 2),
        "customers": customers, "orders_without_email": n - sum(per_customer.values()),
        "repeat_customer_rate": round(sum(1 for c in per_customer.values() if c >= 2) / customers, 4) if customers else None,
        "orders_per_customer": round(sum(per_customer.values()) / customers, 2) if customers else None,
        "discount_rate": round(discount / (subtotal + discount), 4) if subtotal + discount else None,
        "revenue_by_month": dict(sorted((m, round(v, 2)) for m, v in months.items() if m)),
    }


def report(k):
    pct = lambda v: "-" if v is None else f"{v*100:.1f}%"
    lines = ["| KPI | Value |", "|-----|-------|",
             f"| Orders (voided excluded) | {k['orders']} ({k['excluded_voided']} voided) |",
             f"| Gross / refunds / net revenue | ${k['gross_revenue']:,.2f} / ${k['refunds']:,.2f} / ${k['net_revenue']:,.2f} |",
             f"| AOV: order total / merchandise (subtotal) | ${k['aov']:,.2f} / ${k['aov_merchandise']:,.2f} |",
             f"| Customers (by email) | {k['customers']} ({k['orders_without_email']} orders without email) |",
             f"| Repeat customer rate | {pct(k['repeat_customer_rate'])} |",
             f"| Orders per customer | {k['orders_per_customer']} |",
             f"| Discount rate | {pct(k['discount_rate'])} |", "", "| Month | Revenue |", "|-------|---------|"]
    lines += [f"| {m} | ${v:,.2f} |" for m, v in k["revenue_by_month"].items()]
    lines.append("\nComputed from your order export (verified for the exported period). Shopify's own reports may differ "
                 "slightly (they use net sales definitions, time zones and include/exclude test orders differently).")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    try:
        k = kpis(load_orders(args[0]))
    except (ValueError, OSError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(k, indent=2) if "--json" in sys.argv else report(k))


if __name__ == "__main__":
    main()

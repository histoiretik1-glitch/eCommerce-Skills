#!/usr/bin/env python3
"""
Restock Alert - reorder point, safety stock and stock-out risk per SKU.

Formulas (standard inventory theory, continuous review with optional review period):
  d      = average daily demand (units/day)
  sd     = standard deviation of daily demand
  L, sL  = lead time in days and its standard deviation
  R      = review period in days (0 for continuous review)
  Z      = normal quantile of the target service level (cycle service level)
  sigma  = sqrt((L + R) * sd^2 + d^2 * sL^2)       demand variability over the protection period
  SS     = Z * sigma                                  safety stock
  ROP    = d * (L + R) + SS                           reorder point
  IP     = on_hand + on_order - backorders            inventory position
  risk   = P(demand over L + R > IP) = 1 - Phi((IP - d * (L + R)) / sigma)
  order  = order-up-to level (ROP + d * cover_days) - IP, rounded up to MOQ / multiple

Usage:
  python3 scripts/reorder.py                      # demo data
  python3 scripts/reorder.py '<json list of SKUs>'
  python3 scripts/reorder.py '<json>' --json      # machine-readable output

Each SKU: sku, and either daily_demand (+ optional demand_std) or sales_history (list of daily units);
lead_time_days; optional lead_time_std_days, on_hand, on_order, backorders, service_level (0.5-0.999,
default 0.95), review_period_days, cover_days (default 30), moq, order_multiple.
Standard library only.
"""
import json
import math
import statistics
import sys
from dataclasses import dataclass, field, fields
from typing import List, Optional

NORMAL = statistics.NormalDist()


@dataclass
class SkuInput:
    sku: str
    lead_time_days: float
    daily_demand: Optional[float] = None
    demand_std: Optional[float] = None
    sales_history: List[float] = field(default_factory=list)
    lead_time_std_days: float = 0.0
    on_hand: float = 0.0
    on_order: float = 0.0
    backorders: float = 0.0
    service_level: float = 0.95
    review_period_days: float = 0.0
    cover_days: float = 30.0
    moq: float = 0.0
    order_multiple: float = 1.0

    def __post_init__(self):
        if self.sales_history:
            if len(self.sales_history) < 2:
                raise ValueError(f"{self.sku}: sales_history needs at least 2 days")
            self.daily_demand = statistics.mean(self.sales_history)
            self.demand_std = statistics.stdev(self.sales_history)
        if self.daily_demand is None:
            raise ValueError(f"{self.sku}: give daily_demand or sales_history")
        if self.demand_std is None:
            self.demand_std = 0.0
        if not 0.5 <= self.service_level < 1:
            raise ValueError(f"{self.sku}: service_level must be between 0.5 and 0.999")
        if self.lead_time_days <= 0 or self.daily_demand < 0:
            raise ValueError(f"{self.sku}: lead_time_days must be > 0 and daily_demand >= 0")


def analyze(s: SkuInput) -> dict:
    d, sd = s.daily_demand, s.demand_std
    period = s.lead_time_days + s.review_period_days
    sigma = math.sqrt(period * sd ** 2 + d ** 2 * s.lead_time_std_days ** 2)
    z = NORMAL.inv_cdf(s.service_level)
    safety_stock = z * sigma
    reorder_point = d * period + safety_stock
    position = s.on_hand + s.on_order - s.backorders
    if sigma > 0:
        risk = 1 - NORMAL.cdf((position - d * period) / sigma)
    else:
        risk = 0.0 if position >= d * period else 1.0
    cover = s.on_hand / d if d > 0 else math.inf
    order_up_to = reorder_point + d * s.cover_days
    qty = 0.0
    if position <= reorder_point:
        qty = max(order_up_to - position, s.moq)
        if s.order_multiple > 1:
            qty = math.ceil(qty / s.order_multiple) * s.order_multiple
        qty = math.ceil(qty)
    if position <= reorder_point:
        status = "REORDER NOW"
    elif cover < period + 7:
        status = "WATCH"
    else:
        status = "OK"
    return {
        "sku": s.sku, "daily_demand": round(d, 2), "demand_std": round(sd, 2),
        "lead_time_days": s.lead_time_days, "service_level": s.service_level, "z": round(z, 3),
        "safety_stock": math.ceil(safety_stock), "reorder_point": math.ceil(reorder_point),
        "inventory_position": position, "days_of_cover": None if math.isinf(cover) else round(cover, 1),
        "stockout_risk": round(risk, 3), "order_quantity": int(qty), "status": status,
    }


def sku_from_dict(data: dict) -> SkuInput:
    allowed = {f.name for f in fields(SkuInput)}
    unknown = sorted(set(data) - allowed)
    if unknown:
        raise ValueError(f"unknown field(s): {', '.join(unknown)}. Allowed: {', '.join(sorted(allowed))}")
    return SkuInput(**data)


DEMO = [
    {"sku": "MUG-BLUE", "sales_history": [12, 9, 15, 11, 10, 14, 13, 8, 12, 16, 11, 10, 9, 14],
     "lead_time_days": 21, "lead_time_std_days": 4, "on_hand": 260, "on_order": 0, "moq": 200},
    {"sku": "MUG-RED", "daily_demand": 3, "demand_std": 1.5, "lead_time_days": 21, "on_hand": 400},
]


def format_table(rows: List[dict]) -> str:
    lines = ["| SKU | Daily demand | Safety stock | Reorder point | Position | Days of cover | Stock-out risk | Order qty | Status |",
             "|-----|--------------|--------------|---------------|----------|---------------|----------------|-----------|--------|"]
    for r in rows:
        lines.append(f"| {r['sku']} | {r['daily_demand']} ± {r['demand_std']} | {r['safety_stock']} | {r['reorder_point']} | "
                     f"{r['inventory_position']:g} | {r['days_of_cover']} | {r['stockout_risk']*100:.1f}% | {r['order_quantity']} | {r['status']} |")
    lines.append("")
    lines.append("Inputs are the seller's data (verified); service level, demand and lead-time variability are assumptions to state in the report.")
    return "\n".join(lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        data = json.loads(args[0]) if args else DEMO
        if isinstance(data, dict):
            data = [data]
        rows = [analyze(sku_from_dict(d)) for d in data]
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(rows, indent=2) if "--json" in sys.argv else format_table(rows))


if __name__ == "__main__":
    main()

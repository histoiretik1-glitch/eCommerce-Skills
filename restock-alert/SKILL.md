---
name: restock-alert
description: "Restock alert and replenishment calculator. Computes per SKU the reorder point, safety stock for a chosen service level, days of cover, stock-out risk and the order quantity (respecting MOQ and case packs) from sales history and supplier lead time, with a script. Use when a seller on Amazon, Shopify, Walmart, Etsy or TikTok Shop asks when to reorder, how much safety stock to keep, how much to order, or which SKUs are about to run out."
nexscope:
  name: "Restock Alert"
  category: "Supply Chain & Logistics"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "inventory"
    - "restock"
    - "supply-chain"
    - "alerts"
  model: "any"
  tokens: "~2000"
  keywords:
    - "restock alert"
---

# Restock Alert

AI-powered restock alert and replenishment planning skill. Calculates optimal reorder points, safety stock levels, and stockout risk scores to prevent lost sales from inventory gaps.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Reorder points, safety stock and stock-out risk for replenishment decisions.

Part of: Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `inventory-tracking-software` — Designing the inventory tracking system: monitoring, alerts and multi-channel sync.
- `shopify-inventory-management` — Managing stock in Shopify across locations.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Daily units sold per SKU (60-90 days) | Amazon Business Reports / Inventory reports, Shopify Analytics, Walmart Seller Center, TikTok Shop Seller Center, Etsy Stats |
| On-hand stock and stock in transit / on order | FBA inventory, Shopify inventory, WFS, 3PL, purchase orders |
| Supplier lead time (order to available-to-sell) and its variability | Past purchase orders: order date → received date (+ FBA/WFS check-in time) |
| MOQ, case pack, cost of a stock-out vs cost of holding | Supplier terms, margins |
| Planned promotions, seasonality, viral content | Marketing calendar (`tiktok-shop-inventory` for viral spikes) |

## Workflow

1. **Clean the sales history**: remove days with stock-outs (they hide demand) and one-off spikes, or handle them separately.
2. **Lead time** = from placing the order to stock being sellable; for FBA or WFS include inbound transit and check-in.
3. **Service level** per SKU class: e.g. 97-99% for A items (best sellers), 90-95% for C items (`warehouse-optimization` for ABC classes).
4. **Run the calculator** for every SKU (see below).
5. **Act on status**: REORDER NOW → place the suggested order; WATCH → check open POs and promotions; OK → no action.
6. **Adjust for known events**: add the extra units expected from promotions or seasonality on top of the calculated quantity, and say so.
7. **Review weekly** for A items, monthly for the rest; update lead times from new POs.

## Calculations and Tools

`scripts/reorder.py` (standard formulas, documented in the script):

- σ = √((L + R) × σd² + d² × σL²), safety stock = Z × σ, reorder point = d × (L + R) + safety stock
- stock-out risk = probability that demand over the lead time exceeds the inventory position (normal approximation)
- order quantity = (reorder point + d × cover days) − inventory position, rounded up to MOQ / case pack

```bash
python3 scripts/reorder.py '[{"sku": "MUG-BLUE", "sales_history": [12, 9, 15, 11, 10, 14, 13], "lead_time_days": 21, "lead_time_std_days": 4, "on_hand": 260, "moq": 200, "service_level": 0.97}]'
```

Add `--json` for machine-readable output.

## Example Requests

- "Which of my 40 Amazon SKUs need reordering this week? Here's my sales and inventory export."
- "My supplier takes 30-45 days. How much safety stock should I keep for my best seller at 98% service level?"
- "Calculate reorder points for my Shopify store from the last 90 days of sales."

## Output Format

```
RESTOCK REPORT — [date]
| SKU | Daily demand | Safety stock | Reorder point | Position | Days of cover | Stock-out risk | Order qty | Status |
Assumptions: service levels, lead times, demand period, adjustments for promotions
Orders to place now: [...]
```

## Quality Checks

- Demand excludes stock-out days; the period used is stated.
- Lead time includes inbound and check-in for FBA/WFS.
- Every order quantity respects MOQ and case pack and is checked against cash and storage limits.
- SKUs with fewer than ~30 days of history are flagged as low-confidence.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: sales, stock and purchase-order data from the seller's exports.
- **Estimates**: future demand (based on the past), demand and lead-time variability, service-level choice, promotion uplifts. The report must label them.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill restock-alert -g
```

## Usage

**Input:**
SKU data, sales velocity, lead times, storage costs

**Output:**
Restock alert rules, safety stock calculations, reorder timing windows, stockout risk scores

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up restock alert for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*

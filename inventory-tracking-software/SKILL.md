---
name: inventory-tracking-software
description: "Inventory tracking system design and tool selection. Defines the inventory data model (SKUs, locations, statuses), the source of truth, multi-channel stock sync between Amazon, Shopify, Walmart, Etsy and TikTok Shop, reconciliation checks, accuracy metrics and alert rules, and compares inventory software options by business size. Use when a business asks which inventory management software to use, how to stop overselling across channels, or how to set up reliable inventory tracking and sync."
nexscope:
  name: "Inventory Tracking Software"
  category: "Supply Chain & Logistics"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "inventory"
    - "stock-management"
    - "monitoring"
    - "supply-chain"
  model: "any"
  tokens: "~2000"
  keywords:
    - "inventory tracking software"
---

# Inventory Tracking Software

AI-powered inventory tracking and monitoring skill for e-commerce businesses. Designs inventory monitoring systems, low-stock alerts, reorder point calculations, and multi-channel sync strategies.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Designing the inventory tracking system: monitoring, alerts and multi-channel sync.

Part of: Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `restock-alert` — Reorder points, safety stock and stock-out risk for replenishment decisions.
- `shopify-inventory-management` — Managing stock in Shopify across locations.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Channels and where stock is held (own warehouse, FBA, WFS, FBT, 3PL, stores) | Seller accounts, 3PL contracts |
| SKU count, variants, bundles/kits | Catalog exports |
| Current tools (spreadsheets, apps, ERP) and pain points (oversells, stock-outs, manual work) | Team |
| Order volume per day and peaks | Order reports |
| Count history and adjustments | Inventory reports |

## Workflow

1. **Source of truth**: choose one system that owns available-to-sell quantities (inventory app, ERP or the main platform); every channel reads from it.
2. **Data model**: one SKU per sellable variant, mapped to each channel's identifier (ASIN/FNSKU, Shopify variant, Walmart item ID, TikTok SKU, Etsy listing variation); bundles as components; stock by location and status (on hand, reserved, in transit, damaged).
3. **Sync rules**: update frequency per channel, safety buffer per channel to absorb sync delay, what happens when stock hits the buffer (pause listing vs show out of stock).
4. **Fulfillment-network stock** (FBA, WFS, FBT): track separately; it cannot be shared with other channels in real time.
5. **Reconciliation**: daily comparison of quantities in the source of truth and in each channel; alert on differences above a threshold.
6. **Counting**: cycle counts (A items more often), adjustments with reason codes.
7. **Tool selection**: spreadsheet (very small catalogs), platform-native inventory (single channel), multichannel inventory apps, ERP (high volume, manufacturing). Compare on channel connectors, sync speed, bundles, cost and support.
8. **Alerts**: low stock (thresholds from `restock-alert`), sync failures (`api-monitoring`), oversell events.

## Calculations and Tools

- **Inventory record accuracy** = SKUs whose counted quantity matches the system (within tolerance) ÷ SKUs counted.
- **Oversell rate** = orders cancelled for lack of stock ÷ total orders.
- **Channel buffer** ≈ average daily sales on the channel × sync delay in days (+ margin); an estimate to tune.
- **Sync lag** = time between a sale and the updated quantity on the other channels (measure with a test order).

## Example Requests

- "We oversell on Amazon and Shopify every weekend. How should we set up inventory sync?"
- "Which inventory software fits a brand selling on Shopify, Amazon FBA and TikTok Shop with 300 SKUs?"
- "Design our inventory tracking: locations, statuses and daily reconciliation."

## Output Format

```
INVENTORY TRACKING DESIGN — [Business]
Source of truth: [...]   SKU mapping table: | SKU | Amazon | Shopify | Walmart | TikTok | Etsy |
Sync rules: | Channel | Frequency | Buffer | Out-of-stock behaviour |
Reconciliation and alerts; tool shortlist with pros/cons and cost; rollout plan
```

## Quality Checks

- Every channel identifier is mapped to exactly one internal SKU.
- Fulfillment-network stock is not counted as available for other channels.
- Tool recommendations state what was compared and that prices must be confirmed with vendors.
- Accuracy and oversell metrics come from measured data, with the period stated.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: counts, order and cancellation data, measured sync lag.
- **Estimates**: buffers, expected reduction in oversells, vendor features and prices (confirm with vendors).

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill inventory-tracking-software -g
```

## Usage

**Input:**
SKU list, sales velocity data, platform(s), warehouse info

**Output:**
Inventory monitoring framework, low-stock alert rules, reorder point calculations, multi-channel sync strategy

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up inventory tracking software for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*

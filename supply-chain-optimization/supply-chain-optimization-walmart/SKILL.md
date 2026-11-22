---
name: supply-chain-optimization-walmart
version: 1.0.0
description: "Walmart Marketplace supply chain bottleneck analyzer. Computes margins after Walmart referral fees, WFS fulfillment and storage, inventory days and cash cycle against Walmart benchmarks, ranks the top 3 bottlenecks and proposes cost reduction actions; optional Markdown/HTML report. Use when a Walmart seller asks about WFS costs, cash flow, aged inventory, restocking or landed cost."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — Walmart 📦

Supply chain bottleneck analyzer for Walmart Marketplace sellers. Diagnose cash flow, inventory, WFS costs, and referral fees.

## Workflow

1. **Collect data**: product cost and supplier payment terms, production and shipping days, landed shipping cost, selling price, WFS fulfillment and storage costs, referral fee, ad spend, inventory days.
2. **Run the diagnosis**: `python3 scripts/calculator.py '<json>'` (see Script Usage); the Walmart benchmarks and payout delay apply by default.
3. **Read the metrics**: gross and net margin, shipping ratio, inventory days and cash cycle against the benchmarks.
4. **Rank the bottlenecks**: the script returns the top 3; confirm them with the seller's context.
5. **Plan actions**: cost reductions, payment terms, reorder timing, aged-stock clearance; estimate the effect of each.
6. **Optional report**: `python3 scripts/report_doc.py` or `python3 scripts/report_html.py` for a shareable document.

## Output Format

```
SUPPLY CHAIN DIAGNOSIS — Walmart — [Product]
| Metric | Value | Benchmark | Status |        (gross margin, shipping ratio, inventory days, cash cycle, net margin)
Cost breakdown per unit (with platform fees)
Top 3 bottlenecks: problem → impact → actions
Action plan: [action, owner, expected effect, verified/estimate]
```

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill supply-chain-optimization-walmart -g
```

## Platform Characteristics

| Feature | Walmart | vs Amazon |
|---------|---------|-----------|
| Fulfillment | WFS (Walmart Fulfillment Services) | FBA |
| Commission | 6-15% (by category) | 8-15% |
| Payment cycle | 14-21 days | 14 days |
| Storage fees | Lower | Higher |
| Long-term storage | No extra fee | Yes |

## Cost Structure (Walmart)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping
├── WFS Fulfillment Fee (similar to FBA)
├── WFS Storage Fee (lower than FBA)
├── Referral Fee (6-15%)
├── Advertising (Walmart Connect)
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "walmart": {
        "gross_margin": {
            "healthy": 0.35,    # Walmart commission lower, benchmark can be lower
            "warning": 0.25,
            "danger": 0.15
        },
        "shipping_ratio": {
            "healthy": 0.06,    # WFS shipping slightly higher
            "warning": 0.10,
            "danger": 0.15
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 100,     # Payment cycle slightly longer
            "warning": 130,
            "danger": 160
        },
        "net_margin": {
            "healthy": 0.18,
            "warning": 0.10,
            "danger": 0.05
        }
    }
}
```

## API Integration

### Walmart Marketplace API

```bash
export WALMART_CLIENT_ID="xxx"
export WALMART_CLIENT_SECRET="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Orders API |
| Inventory | Inventory API |
| Fee Reports | Reports API |

## Usage Flow

Same 4-step process as Amazon version:

1. Business profile collection
2. Supply chain data collection
3. Bottleneck diagnosis
4. Cost reduction plan output

## Input Data

```
**Sales (Walmart-specific)**
• Average Selling Price: $___
• WFS Fulfillment Fee: $___/unit
• Referral Fee Rate: ___%
• Walmart Connect Ad Spend Ratio: ___%

**Inventory**
• Current Inventory Days: ___ days
• (Walmart has no long-term storage fees)
```

## Script Usage

`scripts/calculator.py` (plus `report_doc.py` and `report_html.py`) is shared by the four supply-chain-optimization skills. The platform comes from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder. It sets the benchmarks, the payout delay used in the cash cycle (14 days by default, override with `payout_days`), the fulfillment labels and the aged-stock advice.

```bash
python3 scripts/calculator.py '{"product_cost": 6, "supplier_payment_days": 0, "production_days": 25, "shipping_cost_per_unit": 1.2, "shipping_days": 35, "selling_price": 24.99, "wfs_fee": 4.95, "storage_fee": 0.25, "ad_spend_ratio": 0.08, "inventory_days": 55, "has_long_term_storage": false, "referral_fee_rate": 0.15}'
```

Required fields: `product_cost`, `supplier_payment_days`, `production_days`, `shipping_cost_per_unit`, `shipping_days`, `selling_price`, `fba_fee` (aliases `fulfillment_fee`, `wfs_fee`, `fbt_fee`), `storage_fee`, `ad_spend_ratio`, `inventory_days`, `has_long_term_storage`. Optional: `referral_fee_rate`, `affiliate_commission_rate`, `payout_days`, `daily_sales`, `current_inventory`. An unknown field stops the script with the list of accepted fields.

## vs Amazon Comparison

| Item | Amazon | Walmart |
|------|--------|---------|
| Fulfillment | FBA | WFS |
| Storage fees | High | Low |
| Long-term storage | Yes | No |
| Commission | 8-15% | 6-15% |
| Payment cycle | 14 days | 14-21 days |
| Traffic | High | Medium |

## Key Advantages

- **No long-term storage fees** — Better for slow-moving inventory
- **Lower referral fees** — 6-15% vs Amazon's 8-15%
- **Lower storage costs** — WFS storage cheaper than FBA
- **Growing marketplace** — Less competition than Amazon

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**


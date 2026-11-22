---
name: supply-chain-optimization-shopify
version: 1.0.0
description: "Shopify/DTC supply chain bottleneck analyzer. Computes margins, 3PL fulfillment and shipping ratios, inventory days and cash conversion cycle (fast Shopify payouts) against DTC benchmarks, ranks the top 3 bottlenecks and proposes cost reduction actions; optional Markdown/HTML report. Use when a Shopify or DTC brand asks about cash flow, 3PL costs, inventory levels, supplier payment terms or landed cost."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — Shopify/DTC 📦

Supply chain bottleneck analyzer for Shopify and Direct-to-Consumer stores. Diagnose cash flow, inventory, shipping, and customer acquisition costs.

## Output Format

```
SUPPLY CHAIN DIAGNOSIS — Shopify/DTC — [Product]
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill supply-chain-optimization-shopify -g
```

## Platform Characteristics

| Feature | Shopify/DTC | vs Amazon |
|---------|-------------|-----------|
| Fulfillment | Self-select (ShipBob/self) | FBA |
| Platform fee | None | 8-15% |
| Payment fee | 2.9% + $0.30 | Included in fee |
| Payment cycle | 2-3 days | 14 days |
| Traffic cost | High (self-built) | Low (platform) |
| Data ownership | Full | Limited |

## Cost Structure (Shopify/DTC)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping (to warehouse)
├── 3PL Storage Fee (e.g., ShipBob)
├── 3PL Fulfillment Fee
├── Payment Processing (2.9% + $0.30)
├── Shopify Subscription (allocated)
├── Advertising (Meta/Google/TikTok) ← Key Cost
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "shopify": {
        "gross_margin": {
            "healthy": 0.60,    # DTC needs high margin for ads
            "warning": 0.50,
            "danger": 0.40
        },
        "shipping_ratio": {
            "healthy": 0.08,    # 3PL fees
            "warning": 0.12,
            "danger": 0.18
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 45,      # Fast payment
            "warning": 70,
            "danger": 100
        },
        "net_margin": {
            "healthy": 0.20,
            "warning": 0.12,
            "danger": 0.05
        },
        # DTC-specific metrics
        "cac": {               # Customer Acquisition Cost
            "healthy": 0.25,   # CAC < 25% of price
            "warning": 0.35,
            "danger": 0.50
        },
        "ltv_cac_ratio": {     # LTV/CAC
            "healthy": 3.0,    # LTV > 3x CAC
            "warning": 2.0,
            "danger": 1.0
        },
        "ad_spend_ratio": {    # Ad spend ratio
            "healthy": 0.25,
            "warning": 0.35,
            "danger": 0.45
        }
    }
}
```

## DTC-Specific Costs

### Advertising Costs (Critical!)

```
Meta Ads (Facebook/Instagram): CPM $10-30
Google Ads: CPC $1-5
TikTok Ads: CPM $5-15
Influencer Marketing: Variable

DTC ad spend typically 20-40% of revenue
```

### 3PL Logistics Costs

```
Common 3PL Options:
├── ShipBob
├── Deliverr
├── ShipMonk
└── Red Stag

Fee Structure:
├── Receiving: $2-5/case
├── Storage: $0.5-1/cubic ft/month
├── Pick & Pack: $2-4/order
└── Shipping: By weight/zone
```

### Payment Processing Fees

```
Shopify Payments: 2.9% + $0.30
PayPal: 2.9% + $0.30
Stripe: 2.9% + $0.30

High AOV: Ratio acceptable
Low AOV: Erodes profit
```

## Input Data

```
**Sales (Shopify-specific)**
• Average Selling Price: $___
• Average Order Value (AOV): $___
• Payment Fee: 2.9% + $0.30

**Logistics (3PL)**
• 3PL Fulfillment Fee: $___/order
• 3PL Storage Fee: $___/unit/month
• Receiving Fee: $___/case

**Marketing (Critical!)**
• Ad Spend Ratio: ___%
• Customer Acquisition Cost (CAC): $___
• Customer Lifetime Value (LTV): $___
• Repeat Purchase Rate: ___%
```

## API Integration

### Shopify Admin API

```bash
export SHOPIFY_STORE_URL="xxx.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Orders API |
| Products | Products API |
| Inventory | Inventory API |
| Customers | Customers API |

### 3PL API (e.g., ShipBob)

```bash
export SHIPBOB_API_TOKEN="xxx"
```

## Script Usage

`scripts/calculator.py` (plus `report_doc.py` and `report_html.py`) is shared by the four supply-chain-optimization skills. The platform comes from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder. It sets the benchmarks, the payout delay used in the cash cycle (3 days by default, override with `payout_days`), the fulfillment labels and the aged-stock advice.

```bash
python3 scripts/calculator.py '{"product_cost": 12, "supplier_payment_days": 30, "production_days": 20, "shipping_cost_per_unit": 1.0, "shipping_days": 25, "selling_price": 49.99, "fulfillment_fee": 4.5, "storage_fee": 0.3, "ad_spend_ratio": 0.25, "inventory_days": 50, "has_long_term_storage": false}'
```

Required fields: `product_cost`, `supplier_payment_days`, `production_days`, `shipping_cost_per_unit`, `shipping_days`, `selling_price`, `fba_fee` (aliases `fulfillment_fee`, `wfs_fee`, `fbt_fee`), `storage_fee`, `ad_spend_ratio`, `inventory_days`, `has_long_term_storage`. Optional: `referral_fee_rate`, `affiliate_commission_rate`, `payout_days`, `daily_sales`, `current_inventory`. An unknown field stops the script with the list of accepted fields.

## Bottleneck Diagnosis Focus

DTC-specific bottlenecks:

1. **High CAC** → Low ad efficiency, acquisition cost eating profit
2. **LTV/CAC < 3** → Customer value insufficient to support CAC
3. **High 3PL costs** → Poor logistics choice
4. **Low repeat rate** → Reliant on new customers, high cost
5. **Low gross margin** → Cannot support ad spend

## DTC Health Formula

```
Net Profit = Price - Product Cost - Shipping - Payment Fee - Ad Spend - Ops Cost

DTC Golden Ratios:
├── Gross Margin > 60%
├── Ad Spend < 30%
├── Shipping < 15%
├── Net Margin > 15%
└── LTV/CAC > 3
```

## vs Amazon Comparison

| Item | Amazon | Shopify/DTC |
|------|--------|-------------|
| Platform fee | 8-15% | 0% |
| Payment fee | Included | 2.9% + $0.30 |
| Payment cycle | 14 days | 2-3 days |
| Ad spend | 10-20% | 20-40% |
| Traffic | Platform | Self-built |
| Margin need | 40%+ | 60%+ |
| Data | Limited | Full ownership |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**



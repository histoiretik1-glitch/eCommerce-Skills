---
name: multichannel-ecommerce
description: "Manage e-commerce operations across multiple marketplaces and channels. Inventory sync, order routing, listing management, and unified analytics for Amazon, Shopify, Walmart, eBay, Etsy, and TikTok Shop. Use when the user asks for help selling on several marketplaces at once, syncing inventory, routing orders or syndicating listings."
---

# Multichannel E-Commerce Management

Manage e-commerce operations across multiple marketplaces and channels. Inventory sync, order routing, listing management, and unified analytics for Amazon, Shopify, Walmart, eBay, Etsy, and TikTok Shop.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Operations: inventory sync, order routing and listing syndication across channels.

Part of: Selling on several channels. For neighbouring jobs, use the matching skill instead:

- `omnichannel-ecommerce` — Strategy: which channels to sell on and how to keep brand and customer experience consistent.

<!-- role-and-scope:end -->

## Capabilities

- Multichannel management platform comparison (ChannelAdvisor, Sellbrite, LitCommerce)
- Inventory synchronization and oversell prevention
- Centralized order management and fulfillment routing
- Product listing syndication and adaptation by channel
- Pricing strategy across marketplaces
- Unified analytics and reporting
- Returns and customer service management across channels
- Scaling strategy: when and how to add new channels

## Principles and Constraints

Operating rules for selling the same catalogue on several channels, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with each channel or tool.

- **One master record per product:** a master SKU with all identifiers (GTIN, MPN, channel IDs such as ASIN, Walmart item ID, eBay item number) in one system (inventory/order management system or PIM); channels are fed from it.
- **Oversells cost more than lost sales:** out-of-stock cancellations count against seller performance on Amazon, eBay, Walmart and TikTok Shop; inventory must sync faster than you sell, with buffers for slow channels.
- **Each channel keeps its own content rules:** title lengths, required attributes, image rules and prohibited claims differ; adapt from the master content, do not copy one listing everywhere.
- **Fulfilment constraints:** marketplaces require valid tracking and on-time delivery; Amazon Multi-Channel Fulfillment can ship non-Amazon orders, but some marketplaces forbid Amazon-branded packaging or carriers on their orders **[check: e.g. Walmart rules, MCF unbranded packaging]**.
- **Price consistency:** large price differences between channels can trigger marketplace pricing rules (e.g. Walmart's reasonable-price checks) and MAP conflicts.
- **Integrations:** use official APIs or approved integrations (e.g. Walmart Solution Providers); tools such as Rithum (ChannelAdvisor), Sellbrite, Linnworks or LitCommerce are examples, chosen by catalogue size and channels.
- **Scope:** this skill is operations. Which channels to choose and how to keep the brand consistent is `omnichannel-ecommerce`; channel-specific tools are `ebay-seller-tools` and `walmart-seller-tools`; stock policies `restock-alert` and `inventory-tracking-software`.

## Data Needed

| Data | Where |
|------|-------|
| Catalogue with identifiers and channel IDs | Store/ERP exports, marketplace inventory reports |
| Stock per location and per channel allocation | Inventory system, FBA/WFS reports |
| Orders per hour/day per channel (peak and average) | Channel order reports |
| Sync delay of the current set-up (minutes from sale to stock update elsewhere) | Test orders, tool logs |
| Oversells, cancellations and late shipments per channel | Marketplace performance dashboards |
| Fees and fulfilment costs per channel | Fee schedules, invoices |

## Workflow

1. **Build the master catalogue** with identifiers and channel IDs; fix duplicates and missing GTINs.
2. **Measure sync delay** with test orders on each channel (time until stock decreases elsewhere).
3. **Set channel buffers** per SKU from the oversell formula; zero buffer only for real-time integrations.
4. **Design order routing:** which location fulfils which channel (own warehouse, 3PL, FBA/MCF, WFS), cut-off times, carrier rules per marketplace.
5. **Syndicate listings** from master content with channel adaptations (titles, attributes, images); keep a channel requirements sheet.
6. **Set pricing rules** per channel from channel costs (fees, fulfilment) with floors, and check consistency and MAP.
7. **Choose or confirm the tool** by catalogue size, channels, order volume and integration status; run a pilot on 20–50 SKUs.
8. **Run weekly operations reviews:** oversells, late shipments, sync errors, listing errors, channel contribution; fix the root cause each time.

## Calculations and Tools

- **Oversell exposure per SKU** = sales per hour across other channels × sync delay (hours).
- **Channel buffer (units)** = ceil(oversell exposure × safety factor), safety factor 1.5–2 in peaks (working rule); remove for one-of-a-kind items only with real-time sync.
- **Channel contribution** = revenue − COGS − channel fees − fulfilment − ad spend − returns; compare per order and in total (`sales_report.py` in `sales-tracking-tool`).
- **Price floor per channel** = (COGS + fulfilment + fixed fee + minimum profit) ÷ (1 − fee rate).
- **Oversell rate** = cancelled orders for no stock ÷ orders, per channel.

## Worked Example

*Illustrative example with invented figures.* A home-goods brand sells on Shopify, Amazon (FBA) and Walmart (seller-fulfilled), 15-minute sync delay.

- Best-seller sells 12 units/hour across Shopify and Amazon at peak → exposure on Walmart = 12 × 0.25 = 3 units → buffer = ceil(3 × 1.5) = **5 units** hidden from Walmart.
- Walmart price floor with a 15% referral fee, $9 COGS, $6.20 shipping and $3 minimum profit: (9 + 6.20 + 3) ÷ 0.85 = **$21.41**.
- Last month: 7 Walmart oversell cancellations out of 410 orders (1.7%); with the buffer the expected oversells drop to near zero (to be measured).

## Example Requests

- "Set up multichannel selling across Amazon, Shopify and Walmart with one inventory."
- "What is the best multichannel management tool for 800 SKUs and about 3,000 orders a month?"
- "How do I prevent overselling when selling the same items on 4 marketplaces?"

## Output Format

1. Master catalogue checklist and identifier gaps.
2. Sync and buffer table per SKU group and channel.
3. Routing rules (location, carrier, cut-off) per channel.
4. Channel requirements sheet and pricing floors.
5. Tool comparison and pilot plan; weekly operations dashboard (oversells, late shipments, sync errors, contribution).

## Quality Checks

- Sync delay measured, not assumed.
- Buffers computed per SKU from sales rate and delay.
- Every channel's fulfilment and packaging rules respected.
- Price floors from real channel costs; MAP and marketplace price rules checked.
- Weekly review records root causes and fixes.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** order rates, measured sync delays, fees and performance metrics with dates.
- **Estimates:** peak sales rates for future events, oversell reduction, tool time savings.
- Channel rules were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill multichannel-ecommerce -g
```

## Usage

Ask your AI agent:

- "Set up multichannel selling across Amazon, Shopify, and Walmart."
- "What is the best multichannel management tool for my business size?"
- "How do I prevent overselling when selling on 4 marketplaces?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

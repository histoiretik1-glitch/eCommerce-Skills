---
name: tiktok-shop-fulfillment
description: "TikTok Shop fulfillment model decision and setup. Compares Fulfilled by TikTok (FBT), seller fulfillment with TikTok shipping labels, and third-party warehouses on cost, speed, control and metrics, then sets handling times, warehouse and return addresses and a performance checklist. Use when a TikTok Shop seller asks whether to use FBT, how to set up fulfillment, how to meet dispatch and delivery requirements, or why late dispatch or cancellations are hurting the shop."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Fulfillment

Choose and run the fulfillment model that keeps TikTok Shop orders on time at an acceptable cost.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Choosing and running the fulfillment model (FBT, self, 3PL) and dispatch performance.

Part of: TikTok Shop operations. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-shipping` — Shipping templates, carriers, shipping prices and delivery promise.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-customer-service` — Buyer messages, disputes and service metrics on TikTok Shop.
- `tiktok-shop-reviews` — Ratings and reviews on TikTok Shop.

<!-- role-and-scope:end -->

## When to Use

- Choosing between FBT, self-fulfillment and a 3PL
- Late dispatch, invalid tracking or seller-caused cancellations are rising
- Preparing for a viral spike or a campaign
- Setting up warehouses, handling times and return addresses

For carriers, shipping templates and rates, see `tiktok-shop-shipping`.

## Fulfillment Models

| Model | Strengths | Weaknesses | Best when |
|-------|-----------|------------|-----------|
| Fulfilled by TikTok (FBT, where available) | TikTok handles storage, pick/pack, shipping; often better delivery promise | Inbound requirements, storage and fulfillment fees, less packaging control | Steady sellers, fast-moving SKUs |
| Seller fulfillment (own warehouse, TikTok shipping labels or own carrier) | Control, custom packaging, no inbound | Seller owns dispatch performance; peaks are hard | Low volume, custom or fragile items |
| Third-party warehouse (3PL) integrated with TikTok Shop | Scales, multi-channel inventory | Integration and per-order fees | Selling on several channels |

## Inputs to Collect

Orders per day (average and peak), product size/weight, current fulfillment cost per order, dispatch and delivery metrics from Seller Center, channels sold on, packaging needs.

## Workflow

1. **Cost per order** for each option: storage + pick/pack + packaging + shipping + returns handling. Use the FBT rate card from Seller Center; it changes.
2. **Speed and reliability**: handling time you can actually meet at peak, carrier scan rates, delivery time to main regions.
3. **Metrics risk**: TikTok Shop tracks fulfillment performance (late dispatch, valid tracking, seller-fault cancellations, on-time delivery; names and thresholds in Seller Center). Pick the model that keeps these under threshold at peak.
4. **Set up**: warehouse and return addresses, handling time, ship-from regions, product dimensions and weights (wrong weights cause shipping fee adjustments).
5. **Peak plan**: forecast with `tiktok-shop-inventory`, extra packing staff, cut-off times, buffer stock in the right warehouse.
6. **Weekly control**: metrics vs thresholds, late orders by cause (stock-out, carrier, cut-off missed).

## Output Format

```
FULFILLMENT RECOMMENDATION — [Shop]
Option comparison: cost/order | handling time | delivery time | control | risk
Recommended model: [...] because [...]
Setup checklist: [...]
Peak readiness plan: [...]
KPIs to watch weekly: [...]
```

## Related Skills

`tiktok-shop-shipping`, `tiktok-shop-inventory`, `tiktok-shop-returns`, `supply-chain-optimization-tiktok`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-fulfillment -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

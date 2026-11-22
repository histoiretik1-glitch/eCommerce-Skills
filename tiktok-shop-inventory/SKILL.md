---
name: tiktok-shop-inventory
description: "TikTok Shop inventory planning for viral demand. Forecasts sales from the creator and content pipeline, sizes stock for viral spikes and campaigns, splits stock between FBT and own warehouse, and plans the exit when a trend fades. Use when a TikTok Shop seller asks how much stock to prepare for a viral video, a big creator or a campaign, or what to do with stock after the trend."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Inventory

Keep enough stock to ride a viral spike without being stuck with inventory once the trend fades.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Stock planning for viral demand on TikTok Shop.

Part of: TikTok Shop operations, Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-fulfillment` — Choosing and running the fulfillment model (FBT, self, 3PL) and dispatch performance.
- `tiktok-shop-shipping` — Shipping templates, carriers, shipping prices and delivery promise.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-customer-service` — Buyer messages, disputes and service metrics on TikTok Shop.
- `tiktok-shop-reviews` — Ratings and reviews on TikTok Shop.
- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `restock-alert` — Reorder points, safety stock and stock-out risk for replenishment decisions.
- `inventory-tracking-software` — Designing the inventory tracking system: monitoring, alerts and multi-channel sync.
- `shopify-inventory-management` — Managing stock in Shopify across locations.

<!-- role-and-scope:end -->

## When to Use

- Planning a reorder or first production run
- A video is going viral or a big creator is about to post
- Preparing for a campaign or Flash Deal
- Stock is aging after a trend

## Inputs to Collect

Daily units sold (last 30-90 days), supplier lead time (production + shipping + FBT inbound), minimum order quantity, current stock by warehouse, upcoming creator posts, LIVEs and campaigns, cost of a stock-out vs cost of holding stock.

## Workflow

1. **Baseline demand.** Average daily units without spikes (remove viral days from the average).
2. **Spike scenarios.** Estimate a spike from past viral days (e.g. 3×, 10× baseline for N days) and from the creator pipeline (expected views × click rate × conversion rate).
3. **Safety stock and reorder point.**
   - Safety stock ≈ Z × σ(daily demand) × √(lead time), with Z ≈ 1.65 for ~95% service level.
   - Reorder point = baseline daily demand × lead time + safety stock.
   - Add a *spike buffer* only for confirmed pipeline (booked creators, campaigns), not hopes.
4. **Split stock.** Allocate between FBT and own warehouse by expected order location and fees; reserve units for Flash Deals and campaigns.
5. **Trend exit.** Watch the 7-day sales trend: if it falls for two weeks, stop reorders, then clear with bundles, vouchers or creator pushes before stock ages.
6. **Weekly review.** Days of cover, sell-through, stock-out days, aged stock.

## Quick Table

| Metric | Formula | Target |
|--------|---------|--------|
| Days of cover | Stock ÷ average daily units | ≥ lead time + buffer |
| Sell-through (30 days) | Units sold ÷ (units sold + ending stock) | Rising or stable |
| Stock-out days | Days with zero stock | 0 during campaigns |

The `warehouse-optimization` skill covers safety stock and ABC analysis in more depth; `supply-chain-optimization-tiktok` diagnoses cash-cycle impact.

## Output Format

1. Demand baseline and spike scenarios
2. Safety stock, reorder point and order quantity per SKU
3. Allocation by warehouse and campaign reservations
4. Trend-exit rules
5. Weekly inventory dashboard

## Related Skills

`warehouse-optimization`, `supply-chain-optimization-tiktok`, `tiktok-shop-fulfillment`, `tiktok-shop-trending-products`.

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-inventory -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

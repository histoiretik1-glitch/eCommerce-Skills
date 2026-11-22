---
name: tiktok-shop-inventory
description: "TikTok Shop inventory planning for viral demand. Forecasts sales from content and creator pipeline, sets safety stock and reorder points for normal days and viral spikes, plans FBT inbound stock and campaign reservations, and manages stock after the trend fades. Use when a TikTok Shop seller asks how much stock to order, how to prepare for a viral video or campaign, how to avoid stock-outs or overstock, or when to reorder."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Inventory

Keep enough stock to ride a viral spike without being stuck with inventory once the trend fades.

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

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

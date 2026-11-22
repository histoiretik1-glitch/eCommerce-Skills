---
name: tiktok-shop-trending-products
description: "TikTok Shop trend spotting. Finds rising products, formats and sounds from TikTok Creative Center, top-selling shop lists, hashtags and competitor shops, separates durable trends from short spikes, and times entry and exit. Use when a seller asks what is trending on TikTok Shop now, which viral products to jump on, whether a trend is too late to enter, or how to plan seasonal TikTok Shop products."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Trending Products

Spot TikTok Shop trends early enough to profit, and tell lasting demand from a two-week spike.

## When to Use

- Looking for products or angles that are rising right now
- Deciding whether it is too late to enter a viral product
- Planning seasonal products and content

To validate a specific product idea in depth, use `tiktok-shop-product-research`.

## Sources to Check

- **TikTok Creative Center** (public): trending hashtags, songs, creators and top ads/products by region and period.
- **TikTok Shop**: best-seller and trending lists in the app, the Shop tab, search suggestions.
- **Competitor shops and creators**: products they push repeatedly, new launches, LIVE best-sellers.
- **Third-party analytics tools** (paid) for shop GMV estimates, if the seller has access.
- **Outside signals**: search trends, Amazon Movers & Shakers, Reddit/Pinterest for the same need.

## Trend Classification

| Type | Signs | Strategy |
|------|-------|----------|
| Spike | Explodes in days, one sound/format, many identical sellers | Enter only with stock on hand and fast content; plan exit |
| Wave | Several creators and formats over weeks, rising searches | Enter with differentiated offer; scale content |
| Durable | Solves a lasting need, steady sales over months | Build brand, listings and reviews |
| Seasonal | Same period each year | Prepare stock and content 4-8 weeks before |

## Workflow

1. Collect 10-20 candidates from the sources above for the seller's category and region.
2. For each, note: first seen date, number of creators and shops, price range, engagement trend, complaints in comments.
3. Classify (spike, wave, durable, seasonal) and estimate the remaining window.
4. Check stock and lead time: if the supplier cannot deliver before the window closes, skip.
5. Pass the best 3 to `tiktok-shop-product-research` for scoring and unit economics.
6. Define exit signals: falling 7-day sales, price war, creators moving on.

## Output Format

1. Trend list with classification and estimated window
2. Top 3 opportunities with entry angle (how to differentiate)
3. Timing plan: order date, content start, campaign dates
4. Exit signals and stop-loss rules

## Related Skills

`tiktok-shop-product-research`, `tiktok-shop-content-strategy`, `tiktok-shop-inventory`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

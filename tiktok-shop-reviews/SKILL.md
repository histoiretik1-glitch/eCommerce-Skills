---
name: tiktok-shop-reviews
description: "TikTok Shop ratings and reviews strategy. Increases the number and quality of product reviews within policy, responds to negative reviews, mines reviews for product and listing fixes, and reuses positive reviews and buyer content as social proof. Use when a TikTok Shop seller asks how to get more reviews, raise a product rating, respond to bad reviews, or use reviews in videos and listings."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Reviews

Build trustworthy social proof on TikTok Shop and use review feedback to improve the product.

## When to Use

- New products with few or no reviews
- Product or shop rating falling
- Negative reviews need answers
- Turning reviews and buyer videos into content

## Policy Boundaries

Never offer money, discounts or gifts in exchange for reviews or for changing a review, never write fake reviews, and never ask only happy buyers to review. These breach TikTok Shop policy and can lead to penalties. Asking all buyers for honest feedback, through allowed channels, is fine.

## Inputs to Collect

Rating and review count per product, recent negative reviews, top complaint themes, time from delivery to review, current packaging inserts and messages.

## Workflow

1. **Increase review volume (within policy).**
   - Deliver on time and as described: most reviews follow delivery.
   - Clear, friendly packaging insert asking for honest feedback (no incentive).
   - Creator samples and seeding produce early content and organic buyers.
2. **Respond to negative reviews** (where replies are available): acknowledge, explain the fix, invite the buyer to contact support; no arguing, no requests to edit the review.
3. **Mine reviews.** Group the last 50-200 reviews into themes (quality, size, shipping, expectations); feed fixes to the listing, supplier and creators. The `product-review-analysis` skill structures this.
4. **Reuse social proof.** Feature real ratings and buyer quotes in videos and on images (accurately), and ask creators to show genuine results.
5. **Track** rating, review count, share of photo/video reviews and the main complaint themes monthly.

## Negative Review Reply Template

```
Thank you for the honest feedback, [Name]. We're sorry the [issue].
We've [action taken, e.g. updated the size guide / changed the packaging].
Please message us with your order number so we can make it right.
```

## Output Format

1. Review health snapshot per product
2. Compliant actions to raise review volume
3. Replies to current negative reviews
4. Top themes and the fixes they imply
5. Monthly tracking table

## Related Skills

`product-review-analysis`, `tiktok-shop-customer-service`, `tiktok-shop-conversion`, `review-monitoring`.

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-reviews -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

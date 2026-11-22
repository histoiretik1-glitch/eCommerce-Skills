---
name: tiktok-shop-promotions
description: "TikTok Shop promotion planning. Chooses between product discounts, Flash Deals, seller vouchers, bundle and multi-buy deals, free shipping and platform campaigns, checks each against margin and creator commission, and builds a promotion calendar. Use when a TikTok Shop seller asks which promotion to run, how deep a discount can go, how to prepare for a TikTok Shop campaign or sale event, or why a promotion did not work."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Promotions

Plan TikTok Shop promotions that create urgency and traffic without selling at a loss once creator commissions and fees are paid.

## When to Use

- Choosing the right promotion tool for a goal (launch, clearance, campaign, basket size)
- Preparing a platform campaign or seasonal sale
- Checking whether a discount is profitable
- Reviewing a promotion that underperformed

## Promotion Tools (names as in Seller Center; availability varies by region)

| Tool | Best for | Watch out for |
|------|----------|---------------|
| Product discount | Everyday price, launch price | Stacking with vouchers |
| Flash Deal | Short urgency windows, LIVE sessions | Stock reserved for the deal; deepest price |
| Seller vouchers / coupons | Targeted offers (new buyers, followers, LIVE viewers) | Voucher codes shared outside the target |
| Bundle / Buy more save more | Raising average order value | Margin on the cheapest item |
| Free shipping / shipping discounts | Conversion on low-price items | Real shipping cost per order |
| Platform campaigns | Large traffic events | Registration deadlines, minimum discount and stock requirements |

## Inputs to Collect

Goal of the promotion, product cost and current price, referral fee, creator commission, stock available, dates (and campaign registration deadlines), past promotion results.

## Workflow

1. **Set one goal per promotion**: new buyers, GMV peak, clearance, or basket size. The goal picks the tool.
2. **Compute the discount ceiling.** Maximum discount = price − break-even price at the highest creator commission you pay. Use `profit-margin-calculator-tiktok` with the promotional price.
3. **Check stacking.** List every discount that can apply at once (product discount + voucher + platform subsidy + creator code) and compute the worst-case price.
4. **Plan stock.** Reserve stock for Flash Deals and campaigns; a sold-out deal wastes the traffic it bought.
5. **Coordinate content.** Brief creators and schedule LIVE sessions inside the promotion window; promotions without content get little traffic.
6. **Measure.** Compare GMV, orders, new buyers, average order value and net margin against the 2 weeks before.

## Promotion Calendar Template

| Dates | Event | Tool | Products | Discount | Stock reserved | Content plan |
|-------|-------|------|----------|----------|----------------|--------------|

## Output Format

1. Recommended promotion mix with the reason for each tool
2. Discount ceiling per product (with assumptions)
3. Worst-case stacked price check
4. Calendar for the next 4-8 weeks
5. KPIs and the review date

## Related Skills

`tiktok-shop-pricing`, `tiktok-live-selling`, `tiktok-shop-affiliate-program`, `tiktok-shop-inventory`.

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-promotions -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

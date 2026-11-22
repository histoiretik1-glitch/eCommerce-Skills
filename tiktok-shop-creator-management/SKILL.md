---
name: tiktok-shop-creator-management
description: "TikTok Shop creator (affiliate) roster management. Organizes creators into tiers, tracks samples and content, sets briefs, approval, commissions and bonuses, and runs monthly reviews to decide who to keep, scale or drop. Use whenever a TikTok Shop seller works with many creators, has lost track of samples or posts, needs a creator brief, or decides which creators to keep."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Creator Management

Run a repeatable process for the creators who sell a shop's products: who to work with, how to brief them, how to pay them and when to scale or stop.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Running an existing creator roster: tiers, briefs, sample tracking, monthly reviews.

Part of: TikTok creators and affiliates. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-affiliate-program` — Setting up the TikTok Shop affiliate program: open and targeted collaborations, commission rates, samples.
- `tiktok-creator-marketplace` — Paid branded-content campaigns through TikTok's creator marketplace: briefs, negotiation, deliverables.
- `tiktok-influencer-marketing` — Overall creator and UGC strategy on TikTok: goals, creator mix, outreach and ROI.

<!-- role-and-scope:end -->

## When to Use

- The shop works with more than a handful of creators
- Samples go out but few videos come back
- Commission costs grow faster than GMV
- A creator brief, contract terms or review process is needed

For finding and recruiting new creators, use `tiktok-shop-affiliate-program` and `tiktok-creator-marketplace`.

## Inputs to Collect

Current creator list (handle, followers, category, commission, samples sent, videos posted, GMV, refunds), product margins, budget for samples and fixed fees, team capacity.

## Workflow

1. **Tier the roster** from the last 30-60 days:
   - *Core*: consistent GMV and conversion → higher commission, early access, exclusive vouchers.
   - *Growth*: promising content, low volume → more samples, briefs on proven angles.
   - *Test*: new creators → one product, one sample, 2-week window.
   - *Inactive*: samples received, no content → follow up once, then stop.
2. **Brief.** One page per product: key benefits, the 3 hooks that convert best, mandatory claims to avoid (see `tiktok-shop-compliance`), required disclosure, product link, voucher code, posting window.
3. **Samples.** Track request date, ship date, delivery, content deadline and result; ask for content within an agreed window (e.g. 14 days).
4. **Approval.** For paid or fixed-fee content, review before posting for accuracy and policy; for commission-only creators, give guidance rather than strict approval.
5. **Compensation.** Base commission by tier, bonuses for GMV milestones, fixed fees only for proven creators; check every rate with `profit-margin-calculator-tiktok`.
6. **Monthly review.** GMV, orders, refund rate, content count and cost per order per creator; move creators between tiers.

## Tracking Sheet Columns

Creator | Tier | Category | Products | Commission | Samples sent | Videos | LIVEs | GMV | Refund rate | Cost per order | Next action

## Output Format

1. Tiered roster with recommended action per creator
2. Product brief(s)
3. Commission and bonus structure with margin check
4. Sample and content tracking template
5. Review cadence and KPIs

## Related Skills

`tiktok-shop-affiliate-program`, `tiktok-creator-marketplace`, `tiktok-influencer-marketing`, `tiktok-shop-content-strategy`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Example Requests

- "We sent samples to 80 TikTok creators and only 20 posted. How do we organize follow-up?"
- "Write a one-page creator brief for our new TikTok Shop product."
- "Which of our TikTok creators should get a higher commission tier this month?"

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-creator-management -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

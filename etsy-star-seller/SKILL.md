---
name: etsy-star-seller
description: "Etsy Star Seller guide. Explains the Star Seller criteria (message response time, on-time shipping with tracking, review ratings), checks the shop's numbers and builds a plan to reach or keep the badge. Use when an Etsy seller asks how to become or stay a Star Seller."
metadata:
  nexscope:
    category: etsy
---

# Etsy Star Seller

Star Seller achievement guide — response time, shipping tracking, 5-star ratings, maintaining status.

Reach or keep the Etsy Star Seller badge, which signals reliable service to buyers.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Reaching and keeping the Etsy Star Seller badge (messages, shipping, reviews).

Part of: Etsy selling. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shop-setup` — Opening a new Etsy shop: account, policies, payments, first listings and launch checklist.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.
- `etsy-multi-shop` — Deciding on and running more than one Etsy shop.
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.

<!-- role-and-scope:end -->

## When to Use

- The shop is close to the badge but misses one criterion
- The badge was lost after a busy month
- Setting up routines so the badge stays

## Criteria (confirm current values in the Star Seller dashboard)

Etsy evaluates shops monthly over the previous 3 months. Commonly published thresholds:

| Criterion | Typical requirement |
|-----------|---------------------|
| Message responsiveness | Reply to 95% of first messages within 24 hours |
| On-time shipping with tracking | 95% of orders shipped on time with tracking or delivery confirmation |
| Great reviews | 95% of reviews rated 5 stars |
| Minimum activity | At least 5 orders and $300 in sales in the period |

## Inputs to Collect

The shop's current Star Seller dashboard numbers, processing times, carriers and how tracking is added, typical message volume, recent reviews under 5 stars.

## Workflow

1. **Find the gap.** Compare each criterion with its threshold and count how many orders, messages or reviews the shop can still miss this period.
2. **Messages.** Mobile notifications, saved replies for common questions, a clear FAQ in listings so fewer messages are needed.
3. **Shipping.** Realistic processing times; buy labels on Etsy or add tracking the same day; mark orders shipped only with a valid tracking number.
4. **Reviews.** Fix the causes of 4-star and lower reviews (expectations, packaging, delays) with `etsy-review-strategy`; reach out to unhappy buyers before they review.
5. **Busy periods.** Increase processing time before holidays, turn on vacation mode if needed rather than shipping late.

## Output Format

1. Scorecard per criterion with the margin left
2. Root causes of the weakest criterion
3. Routine (daily, weekly) to keep the badge
4. Holiday-season adjustments

## Example Requests

- "I'm at 93% on-time shipping. What do I change to get Star Seller next month?"
- "Help me with etsy star seller for my Etsy shop"
- "What are the best practices for etsy star seller?"

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-star-seller -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

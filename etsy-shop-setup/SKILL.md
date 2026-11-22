---
name: etsy-shop-setup
description: "Etsy shop setup guide. Takes a new seller from account creation to first sales: shop policies, payments, branding basics, first listings and SEO foundations. Use when someone asks how to open an Etsy shop or what to do before launching (for the complete selling guide use `etsy-seller-guide`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy Shop Setup

Etsy shop launch guide — policies, branding, first listings, SEO foundation, payment setup.

Take a new seller from zero to a shop that is ready to sell, with the foundations that later SEO, pricing and Star Seller work depend on.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Opening a new Etsy shop: account, policies, payments, first listings and launch checklist.

Part of: Etsy selling. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.
- `etsy-multi-shop` — Deciding on and running more than one Etsy shop.
- `etsy-star-seller` — Reaching and keeping the Etsy Star Seller badge (messages, shipping, reviews).
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.

<!-- role-and-scope:end -->

## When to Use

- Opening a first Etsy shop
- Re-launching an inactive shop
- Checking that a new shop is complete before promoting it

## Inputs to Collect

What the seller makes (handmade, vintage, craft supplies, digital), country and currency, production capacity per week, shipping origin, brand name ideas, budget for listing fees and first ads.

## Workflow

1. **Eligibility and category.** Check that the products fit Etsy's creativity standards (made, designed, handpicked or sourced by the seller) and are not prohibited.
2. **Account and payments.** Shop name (check availability and trademarks), Etsy Payments with bank details, tax and identity verification, billing card.
3. **Shop policies.** Processing time, returns and exchanges, cancellations, privacy; keep them short and consistent with what the seller can deliver.
4. **Shipping profiles.** Create profiles per product size before listing (see `etsy-shipping-strategy`).
5. **First listings.** Start with 10-20 listings so the shop looks established and has more chances in search; use `etsy-keyword-research` and `etsy-seo-tags` for titles and tags, `etsy-listing-photography` for images.
6. **Shop presentation.** Banner, icon, About section and announcement (see `etsy-shop-branding`).
7. **Launch checks.** Test a listing preview on mobile, verify shipping prices at checkout, set up order notifications, plan the first week of promotion.

## Fees to Budget

Etsy fees and limits below are the commonly published values in 2026; confirm them in Etsy's Fees & Payments Policy and Seller Handbook before relying on them, as they differ by country and change.

| Fee | Typical value |
|-----|---------------|
| Listing fee | $0.20 per listing, renews after 4 months or when the item sells |
| Transaction fee | 6.5% of the item price plus shipping and gift wrap |
| Payment processing | Varies by country (e.g. about 3% + $0.25 in the US) |
| Offsite Ads | 12-15% on attributed sales (see `etsy-offsite-ads`) |

## Launch Checklist

☐ Policies complete ☐ Payments verified ☐ Shipping profiles ☐ 10+ listings with 13 tags each ☐ Photos on every listing ☐ About section ☐ Mobile preview checked

## Output Format

1. Setup plan with the steps above, marked done / to do
2. Fee budget for the first 3 months
3. First 10 listing ideas with target keywords
4. First-week promotion plan

## Example Requests

- "I make ceramic mugs and want to open my Etsy shop next month. What do I need to do first?"
- "Help me with etsy shop setup for my Etsy shop"
- "What are the best practices for etsy shop setup?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-shop-setup -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

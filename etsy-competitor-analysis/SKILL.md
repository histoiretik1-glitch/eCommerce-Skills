---
name: etsy-competitor-analysis
description: "Etsy competitor analysis. Studies competing Etsy shops and best-selling listings: prices, titles and tags, photos, reviews, shipping and shop policies, then finds gaps to differentiate. Use when an Etsy seller asks who their competitors are, why another shop sells more, or how to stand out in their Etsy niche."
metadata:
  nexscope:
    category: etsy
---

# Etsy Competitor Analysis

Competitor research — pricing comparison, bestseller analysis, differentiation strategy.

Learn from the Etsy shops and listings that win the same searches, and find where to stand out.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Studying competing Etsy shops and listings to find gaps.

Part of: Etsy listings and search. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-seo` — Full SEO audit and scoring of an Etsy listing (title, tags, description) with the analyzer script.
- `etsy-keyword-research` — Finding the search phrases Etsy buyers use, before writing titles and tags.
- `etsy-seo-tags` — Writing the 13 tags and filling attributes of an Etsy listing.
- `etsy-product-description` — Writing the description text of an Etsy listing.
- `etsy-listing-photography` — Photos and video of an Etsy listing.

<!-- role-and-scope:end -->

## When to Use

- Entering a niche on Etsy
- A competitor outsells the shop on the same products
- Planning prices, photos or new products from market evidence

## Inputs to Collect

The seller's product and main search phrases, 5-10 competing shops or listings (from Etsy search, Bestseller and Popular badges), the seller's own prices and reviews.

## What to Compare

| Area | What to record |
|------|----------------|
| Search position | Rank on 3-5 main phrases |
| Price | Item price, shipping price, free shipping, sales and coupons |
| Listing | Title structure, tags visible, photos and video, description depth |
| Social proof | Review count and rating, recent review themes, Star Seller badge |
| Offer | Variations, personalization, bundles, gift options, processing time |
| Shop | Number of listings, sections, branding, sales count shown |

## Workflow

1. Search the main phrases as a buyer and list the top shops and listings.
2. Fill the comparison table for 5-10 competitors.
3. Read their negative reviews: recurring complaints are opportunities (quality, sizing, delays, packaging).
4. Identify the gap: price position, missing variations, better photos, faster shipping, stronger personalization, niche style.
5. Turn the gap into 3-5 actions, each linked to a skill (`etsy-pricing-strategy`, `etsy-listing-photography`, `etsy-seo`, `etsy-custom-orders`).

Third-party tools (EverBee, eRank…) can estimate competitors' sales; treat their numbers as estimates.

## Output Format

1. Competitor table
2. Review-based complaint themes
3. Positioning gap and differentiation angle
4. Action plan with priorities

For multi-platform competitor analysis, use `ecommerce-competitor-analysis`.

## Example Requests

- "Compare my shop with the top 5 Etsy shops selling personalized cutting boards."
- "Help me with etsy competitor analysis for my Etsy shop"
- "What are the best practices for etsy competitor analysis?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-competitor-analysis -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

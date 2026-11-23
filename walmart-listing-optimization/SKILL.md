---
name: walmart-listing-optimization
description: "Optimize Walmart Marketplace product listings for search visibility and conversion. Covers Walmart SEO, content quality scoring, rich media, and Walmart-specific listing requirements. Use when a Walmart seller asks to improve listing quality score, Walmart search ranking, item attributes, images or rich media."
metadata:
  nexscope:
    emoji: "🏪"
    category: walmart
---

# Walmart Listing Optimization 🏪

Optimize Walmart Marketplace product listings for search visibility and conversion. Covers Walmart SEO, content quality scoring, rich media, and Walmart-specific listing requirements.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Walmart item content: product name, key features, attributes, images and Listing Quality score.

Part of: Walmart listings and ads. For neighbouring jobs, use the matching skill instead:

- `walmart-seller-guide` — How to sell on Walmart Marketplace, from application to scaling.
- `walmart-advertising-strategy` — Walmart Connect Sponsored Products and Brands: campaigns, bids, ACoS and ROAS.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill walmart-listing-optimization -g
```

## Usage

```
Optimize my Walmart listing for a kitchen knife set. I already sell it on Amazon and want to adapt the listing for Walmart's algorithm.
```

## Capabilities

- Walmart Content Quality Score optimization
- Title, description, and attribute optimization for Walmart search
- Rich media and shelf description recommendations
- Category-specific attribute completion
- Walmart vs Amazon listing difference guide
- Pro Seller badge qualification checklist
- Walmart Connect ad readiness assessment

## How This Skill Works

**Step 1:** Collect information from the user's message — product, platform, current situation, and goals.

**Step 2:** Ask one follow-up with all remaining questions using multiple-choice format. Allow shorthand answers (e.g., "1b 2c 3a").

**Step 3:** Research and analyze using the frameworks and methodology below.

**Step 4:** Deliver structured, actionable output with specific recommendations, not vague advice.

## Platform Rules and Constraints

Walmart Marketplace content rules (Seller Center > Listing Quality dashboard and Walmart's category style guides) at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in the current style guide for the item's category.

- **Listing Quality score** in Seller Center combines content and discoverability (title, description, key features, images, attributes), ratings and reviews, competitive price and shipping speed, and post-purchase issues **[check]**. Each item shows the attributes and fixes Walmart expects.
- **Product name (title):** Walmart's style guides recommend a concise name built as Brand + defining qualities + item name + pack/count/size, generally 50–75 characters **[check]**. No promotional words ("best", "sale", "free shipping"), no special characters, no keyword lists.
- **Key features:** 3 to 10 bullet points **[check]**; **description** of at least about 150 words with no HTML beyond what Walmart allows, no links or contact details.
- **Images:** main image on a white background showing the item only; at least 4 images recommended, high resolution (Walmart recommends 2000 × 2000 px, minimum around 1500 × 1500 px for zoom **[check]**).
- **Attributes:** required and recommended attributes depend on the product type; they drive search facets and the Listing Quality score.
- **Product identifiers:** GTIN/UPC must match the GS1 record of the brand; Walmart matches offers to an existing item page when the GTIN exists, and the item page content may then be controlled by the brand or Walmart.
- **Rich media:** enhanced content (videos, comparison charts, 360° views) is available to brand owners through Walmart Brand Portal or approved content partners **[check]**.
- **Prohibited content:** competitor names, unverifiable claims, prohibited product claims (e.g. medical claims on non-medical items).

## Data Needed

| Data | Where |
|------|-------|
| Listing Quality score and issues per item | Seller Center > Listing Quality dashboard (download the report) |
| Current title, key features, description, images, attributes | Seller Center > Items, or the item page |
| Required/recommended attributes for the product type | Item spec / style guide for the category (Seller Center > Item setup) |
| Buyer search terms | Walmart search autocomplete, competing item pages, search term report from Ad Center |
| Price, shipping speed, Buy Box status | Seller Center > Pricing, item page |
| Ratings and review count | Item page / Listing Quality dashboard |

## Workflow

1. **Export the Listing Quality report** and sort items by sales potential (traffic or revenue) and lowest score: fix the items that matter first.
2. **Check the item page ownership:** if the GTIN matches an existing page, you may only control your offer; content changes then go through the brand or a content correction request.
3. **Rewrite the product name** with Brand + key qualifiers + item name + size/count, within the style guide length, using the most common buyer phrase from autocomplete.
4. **Write 5–8 key features** each starting with the benefit, then the fact (material, dimension, compatibility, warranty), with no repeated claim.
5. **Write the description** (150+ words): use case, what is included, care, specifications; no links, no contact details.
6. **Complete every required and recommended attribute** for the product type; attributes feed facets such as size, colour and material.
7. **Upgrade images** to at least 4 compliant images (white-background main, scale, detail, in-use) and add rich media if you are the brand.
8. **Fix the offer:** price competitiveness and shipping speed (WFS or 2-day eligible) also count in the score; then resubmit and track the score weekly.

## Calculations and Tools

- **Attribute completion** = filled recommended attributes ÷ recommended attributes for the product type.
- **Content checklist score** (this skill's checklist, not Walmart's formula): 1 point each for title within the style-guide length, 3+ key features, description ≥ 150 words, 4+ images, all required attributes, ≥ 80% recommended attributes, white-background main image, no prohibited words → out of 8.
- **Priority** = item sales (or traffic) × (100 − Listing Quality score) to rank the fix list.
- **Title length** = characters including spaces; count with `len()` or any editor.

## Worked Example

*Illustrative example with invented figures.* An 8-piece kitchen knife set copied from Amazon has a 200-character title with keyword lists, 2 images and 40% of recommended attributes.

- New product name: "Acme 8-Piece Kitchen Knife Set with Block, Stainless Steel, Black" (65 characters).
- 6 key features (blade material, block material, dishwasher guidance, included pieces, warranty, sharpener), 180-word description, 5 images, attributes completed to 90%.
- Checklist score: 2/8 before → 8/8 after. Report the Listing Quality score before and after from the dashboard, with dates; do not predict a specific score.

## Example Requests

- "Adapt my Amazon listing for an 8-piece kitchen knife set to Walmart's style guide: product name, key features, description and attributes."
- "Here is my Walmart Listing Quality report: which 20 items should I fix first and what is missing on each?"
- "My Walmart item shows content I didn't write. Why, and how do I request a correction?"

## Output Format

- Start with a summary of findings
- Include specific data points and benchmarks where available
- Provide prioritized action items
- Mark estimates with ⚠️ when based on incomplete data
- End with concrete next steps

Deliverable for each item:

1. Current vs proposed product name (with character count), key features and description.
2. Attribute table: attribute, required/recommended, current value, proposed value.
3. Image plan: current images, missing image types, compliance issues.
4. Offer fixes (price competitiveness, shipping speed / WFS) and the item's Listing Quality score with date.
5. Fix list for the catalogue, ranked by the priority formula.

## Quality Checks

- Product name follows the category style guide order and length; no promotional words or special characters.
- Every claim in key features is verifiable from the product or packaging.
- GTIN matches the brand's GS1 record; no new item page created for an existing GTIN.
- All required attributes filled with valid values; recommended attribute completion stated.
- Images meet the main-image and resolution rules; image rights belong to the seller or brand.
- Score changes reported from the Listing Quality dashboard with dates, not predicted.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Listing Quality scores and issues from the seller's dashboard export, attribute requirements from the category item spec, with the date.
- **Estimates:** expected score or sales change, keyword popularity inferred from autocomplete.
- Style-guide limits were reviewed in November 2026 and vary by category; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

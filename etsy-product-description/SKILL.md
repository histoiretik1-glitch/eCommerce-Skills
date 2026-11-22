---
name: etsy-product-description
description: "Etsy product description writing. Writes Etsy listing descriptions that answer buyer questions (materials, size, personalization, shipping, care), use keywords naturally and are easy to scan on mobile. Use when an Etsy seller asks to write or improve a listing description (for titles and tags use `etsy-seo` and `etsy-seo-tags`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy Product Description

Product description writing — keyword integration, benefit-focused copy, FAQ, formatting.

Write Etsy listing descriptions that answer buyer questions, reduce messages and returns, and support search with natural keywords.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Writing the description text of an Etsy listing.

Part of: Etsy listings and search. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-seo` — Full SEO audit and scoring of an Etsy listing (title, tags, description) with the analyzer script.
- `etsy-keyword-research` — Finding the search phrases Etsy buyers use, before writing titles and tags.
- `etsy-seo-tags` — Writing the 13 tags and filling attributes of an Etsy listing.
- `etsy-listing-photography` — Photos and video of an Etsy listing.
- `etsy-competitor-analysis` — Studying competing Etsy shops and listings to find gaps.

<!-- role-and-scope:end -->

## When to Use

- New listing without a description, or a one-line description
- Many buyer questions or "not as described" complaints
- Rewriting descriptions after a keyword map (`etsy-keyword-research`)

## Inputs to Collect

Product details (materials, dimensions, weight, colors, variations, personalization options), care instructions, production and shipping times, what is included, the main buyer phrase, common questions from messages and reviews.

## Structure

1. **First 1-2 sentences**: what it is, who it is for, the main benefit, using the main keyword phrase naturally (this part shows in previews and helps search).
2. **Details** (short bullet list): materials, size, colors, what's included.
3. **Personalization / options**: how to order, what to write in the personalization box, proof process if any (`etsy-custom-orders`).
4. **Processing and shipping**: production time, shipping method, gift options.
5. **Care and use**.
6. **FAQ**: 3-5 questions taken from real messages and reviews.
7. **Shop link line**: invite to see related sections.

## Rules

- Accurate and specific: every claim must match the photos and the product.
- Scannable on mobile: short paragraphs, bullet lists.
- No keyword stuffing; write for the buyer first.
- Measurements in the units the main buyers use (and both if selling internationally).

## Output Format

The full description, ready to paste, plus a short list of the questions it now answers and the keywords used.

## Example Requests

- "Rewrite the description of my linen apron listing so buyers stop asking about sizes."
- "Help me with etsy product description for my Etsy shop"
- "What are the best practices for etsy product description?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-product-description -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

---
name: etsy-seo-tags
description: "Etsy tags and attributes optimization. Writes the 13 Etsy tags (up to 20 characters each) and fills listing attributes so they cover different long-tail searches without repeating the title. Use when an Etsy seller asks which tags to use or how to fill attributes (for keyword discovery use `etsy-keyword-research`; for a full listing audit use `etsy-seo`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy SEO Tags

Etsy tag optimization — 13-tag strategy, attribute optimization, search ranking factors.

Write the 13 tags and the attributes of an Etsy listing so it can match as many relevant searches as possible.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Writing the 13 tags and filling attributes of an Etsy listing.

Part of: Etsy listings and search. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-seo` — Full SEO audit and scoring of an Etsy listing (title, tags, description) with the analyzer script.
- `etsy-keyword-research` — Finding the search phrases Etsy buyers use, before writing titles and tags.
- `etsy-product-description` — Writing the description text of an Etsy listing.
- `etsy-listing-photography` — Photos and video of an Etsy listing.
- `etsy-competitor-analysis` — Studying competing Etsy shops and listings to find gaps.

<!-- role-and-scope:end -->

## When to Use

- Writing tags for a new listing
- Rewriting tags of listings with few search views
- Checking tags and attributes after a keyword map is ready (`etsy-keyword-research`)

## Etsy Rules (confirm in the Seller Handbook)

- **13 tags** per listing, **up to 20 characters** each; multi-word phrases are allowed and recommended.
- **Attributes** (color, material, occasion, style…) also help matching, so tags do not need to repeat them.
- Category choice matters: the category itself acts as a search signal.

## Workflow

1. Start from the keyword map; if there is none, list the main buyer phrases first.
2. Fill **all attributes** that apply, and pick the most specific category.
3. Write 13 tags:
   - Use all 13 slots.
   - Each tag is a **phrase buyers type**, max 20 characters (shorten words if needed, keep meaning).
   - Cover **different angles**: product type, material, style, occasion, recipient, use, size.
   - Do not waste tags on single generic words, misspellings, or words already covered by attributes and category.
   - Repeat the most important title phrases in tags.
4. Check each tag length and duplicates; the analyzer of the `etsy-seo` skill (`python3 etsy-seo/scripts/analyzer.py`, from the plugin root) can score the result.
5. Review after 30-60 days with search terms in Etsy Stats; replace tags that bring no visits.

## Output Format

```
TAGS — [Listing]
| # | Tag (≤20 chars) | Length | Angle |
| 1 | personalized mug | 16 | product |
...
Attributes to fill: [...]
Category: [...]
Tags replaced and why: [...]
```

## Example Requests

- "Write 13 tags for my personalized birth flower necklace."
- "Help me with etsy seo tags for my Etsy shop"
- "What are the best practices for etsy seo tags?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-seo-tags -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

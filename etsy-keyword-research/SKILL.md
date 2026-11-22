---
name: etsy-keyword-research
description: "Etsy keyword research. Finds the words Etsy buyers search for using Etsy search suggestions, competitor listings and seasonal terms, and groups them into long-tail phrases for titles and tags. Use when an Etsy seller asks which keywords to target or how buyers search for their product (to write the 13 tags use `etsy-seo-tags`; for a full listing SEO audit use `etsy-seo`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy Keyword Research

Etsy search optimization — long-tail keywords, tag research, competitor analysis, seasonal trends.

Find the exact phrases Etsy buyers type, before writing titles, tags and descriptions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Finding the search phrases Etsy buyers use, before writing titles and tags.

Part of: Etsy listings and search. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-seo` — Full SEO audit and scoring of an Etsy listing (title, tags, description) with the analyzer script.
- `etsy-seo-tags` — Writing the 13 tags and filling attributes of an Etsy listing.
- `etsy-product-description` — Writing the description text of an Etsy listing.
- `etsy-listing-photography` — Photos and video of an Etsy listing.
- `etsy-competitor-analysis` — Studying competing Etsy shops and listings to find gaps.

<!-- role-and-scope:end -->

## When to Use

- New listing or new product line
- Listings get few views from Etsy search
- Preparing seasonal or gift listings

## Inputs to Collect

Product, materials, style, occasion and recipient, current titles and tags, search terms already shown in Etsy Stats.

## Sources

- **Etsy search bar suggestions** (autocomplete) for the product, plus "for [recipient]", "[occasion]", "[material]", "[style]".
- **Search results**: titles and visible tags of top listings and Bestseller items for the phrase.
- **Etsy Stats search terms** for the seller's own listings.
- **Third-party Etsy keyword tools** (eRank, EverBee, Marmalead…) if the seller uses them, for volume and competition estimates.

## Workflow

1. **Seed list.** Write 10-20 descriptive words: what it is, material, style, color, size, occasion, recipient.
2. **Expand.** Collect autocomplete phrases for each seed; keep phrases a buyer would really type.
3. **Qualify.** For each phrase, note relevance (exact match to the product), competition (number of results, strength of top listings) and intent (gift, occasion, style).
4. **Prioritize long-tail.** Prefer specific 2-4 word phrases where the product can rank ("personalized leather dog collar") over very broad ones ("dog collar").
5. **Map.** Main phrase → start of title; 12 more phrases → tags (`etsy-seo-tags`); supporting words → description (`etsy-product-description`); attributes → fill in the listing.
6. **Seasonal set.** Separate list of occasion phrases with the month to add them (`etsy-seasonal-strategy`).

## Output Format

```
KEYWORD MAP — [Product]
Primary phrase: ...
| Phrase | Relevance | Competition | Intent | Use in (title/tag/description) |
Seasonal phrases: [phrase → month]
```

Hand the map to `etsy-seo-tags` (tags) and `etsy-seo` (title and full audit).

## Example Requests

- "Find the best search phrases for my handmade leather dog collars on Etsy."
- "Help me with etsy keyword research for my Etsy shop"
- "What are the best practices for etsy keyword research?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-keyword-research -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

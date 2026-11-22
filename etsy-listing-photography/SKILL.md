---
name: etsy-listing-photography
description: "Etsy listing photography guide. Plans the image set for an Etsy listing (main thumbnail, scale, detail, lifestyle, packaging, video), with lighting, backgrounds, phone settings and editing for handmade and vintage items. Use when an Etsy seller asks how to take better product photos or why their thumbnails get few clicks."
metadata:
  nexscope:
    category: etsy
---

# Etsy Listing Photography

Product photography for Etsy — composition, lighting, backgrounds, editing, lifestyle shots, 360 views.

Plan and shoot Etsy listing images that win the click in search results and answer buyer questions on the listing page.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Photos and video of an Etsy listing.

Part of: Etsy listings and search. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-seo` — Full SEO audit and scoring of an Etsy listing (title, tags, description) with the analyzer script.
- `etsy-keyword-research` — Finding the search phrases Etsy buyers use, before writing titles and tags.
- `etsy-seo-tags` — Writing the 13 tags and filling attributes of an Etsy listing.
- `etsy-product-description` — Writing the description text of an Etsy listing.
- `etsy-competitor-analysis` — Studying competing Etsy shops and listings to find gaps.

<!-- role-and-scope:end -->

## When to Use

- Thumbnails get views but few clicks, or many questions about size and look
- Shooting a new product line
- Making the shop's photos consistent

## Etsy Specifics (confirm current limits in the Seller Handbook)

- The **first photo is the search thumbnail**; it is cropped in search, so keep the product centered.
- Use high-resolution images (at least about 2000 px on the shortest side) so zoom works.
- Listings can include several photos and a short **video (5-15 seconds)**; use the photo slots available.

## Image Plan per Listing

| # | Image | Purpose |
|---|-------|---------|
| 1 | Clean hero shot, product centered | Wins the click in search |
| 2 | In use / lifestyle | Shows the result and the buyer's life |
| 3 | Scale (in hand, on a person, next to a common object) | Prevents size surprises |
| 4 | Details and texture | Shows quality and materials |
| 5 | Variations / colors | Reduces questions |
| 6 | Personalization example | Shows what the buyer will get |
| 7 | Packaging / gift | Supports gift buyers |
| Video | 5-15 s of the product in use | More engagement on the listing |

## Workflow

1. Pick one background and lighting style for the whole shop (natural window light or a simple light box).
2. Shoot the hero image first; check it at thumbnail size on a phone next to competitors' thumbnails.
3. Shoot the rest of the plan; keep colors true (no heavy filters).
4. Edit: straighten, crop, correct white balance and exposure.
5. Test: change only the first photo of one listing and compare clicks over 2-4 weeks in Etsy Stats.

## Output Format

1. Image plan per listing
2. Setup and lighting instructions for the seller's space and phone
3. Editing checklist
4. Thumbnail test plan

For Shopify product photos and file optimization, see `shopify-product-photography-guide`.

## Example Requests

- "My thumbnails get few clicks. Plan the photos for my beeswax candle listing."
- "Help me with etsy listing photography for my Etsy shop"
- "What are the best practices for etsy listing photography?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-listing-photography -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

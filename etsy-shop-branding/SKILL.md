---
name: etsy-shop-branding
description: "Etsy shop branding. Creates a consistent shop identity on Etsy: shop name, banner, logo, shop announcement and About section, photo style and packaging. Use when an Etsy seller asks how to make their shop look more professional or build a recognizable brand on Etsy."
metadata:
  nexscope:
    category: etsy
---

# Etsy Shop Branding

Shop branding — banner design, logo, brand story, cohesive listing photography, packaging.

Give an Etsy shop a recognizable, trustworthy identity that buyers remember and that makes listings look like one collection.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.

Part of: Etsy selling, Brand and business planning. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shop-setup` — Opening a new Etsy shop: account, policies, payments, first listings and launch checklist.
- `etsy-multi-shop` — Deciding on and running more than one Etsy shop.
- `etsy-star-seller` — Reaching and keeping the Etsy Star Seller badge (messages, shipping, reviews).
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.
- `ecommerce-branding` — Brand positioning, voice, visual identity and trademark clearance across channels.
- `ecommerce-business-plan` — Business plan for a new online business: market sizing, unit economics, cash flow.
- `ecommerce-growth-strategy` — Growth priorities for an existing business: unit economics, growth levers and roadmap.
- `tiktok-shop-branding` — Building a recognizable brand on TikTok: identity, content pillars, community.

<!-- role-and-scope:end -->

## When to Use

- The shop looks unfinished or inconsistent
- Rebranding or narrowing the shop's niche
- Preparing packaging and inserts

## Inputs to Collect

Products and price range, target buyer, what makes the maker different (story, materials, process), current shop name, banner, icon, About section, 5 best listing photos, packaging photos.

## Workflow

1. **Positioning sentence.** "Handmade [product] for [buyer] who want [benefit], made with [differentiator]." Every brand element should support it.
2. **Name and visual identity.** Shop name that is easy to spell and search; a simple logo readable at icon size; 2-3 brand colors and one photo style.
3. **Shop page.**
   - Banner: shows the products or the maker, not only text.
   - Announcement: current offer, processing times, what's new.
   - About section: maker story, process photos, why buy here.
   - Sections: group listings by product type or occasion.
4. **Listing consistency.** Same background and lighting across thumbnails (see `etsy-listing-photography`), consistent title structure and tone of voice.
5. **Unboxing.** Packaging, thank-you card (no review incentives, see `etsy-review-strategy`), care instructions, a reason to come back.
6. **Check.** View the shop on mobile as a new buyer: is it clear within 5 seconds what the shop sells and why it is different?

## Output Format

1. Positioning sentence and tone-of-voice guidelines
2. Shop page copy (announcement, About, section names)
3. Visual guidelines (colors, photo style, thumbnail rules)
4. Packaging and insert plan
5. Before/after checklist

## Example Requests

- "My Etsy shop looks messy. Help me write an About section and pick a consistent photo style."
- "Help me with etsy shop branding for my Etsy shop"
- "What are the best practices for etsy shop branding?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-shop-branding -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*

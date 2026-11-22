---
name: shopify-landing-page-builder
description: "Shopify landing page creation. Builds a new page for a campaign, product launch or seasonal promotion on Shopify with Online Store 2.0 templates and sections (or a page builder app), including the page outline, copy for each block, mobile layout and UTM tracking. Use when a Shopify store owner needs to create a new page for ads, email or influencer traffic (to review an existing page use `ecommerce-landing-page`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Landing Page Builder

High-converting landing pages — campaign pages, collection pages, seasonal promos, A/B testing.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Building a new campaign or seasonal landing page on Shopify.

Part of: Conversion and landing pages. For neighbouring jobs, use the matching skill instead:

- `conversion-rate-optimization` — Platform-independent CRO: funnel analysis, heuristics and testing roadmap.
- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.
- `ecommerce-landing-page` — Auditing an existing landing or product page for conversion.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Build new Shopify landing pages for campaigns, launches and seasonal promotions that convert ad and email traffic.

## Inputs to Collect

Campaign goal and offer, traffic source (ads, email, influencers), target product(s) or collection, brand assets, theme (Online Store 2.0 sections) or page builder app, deadline.

## Workflow

1. **One goal per page**: one offer and one main call to action that matches the ad or email that brings the visitor.
2. **Build method**: a new page template with theme sections (Online Store 2.0) for most needs; a page builder app (PageFly, GemPages, Shogun…) only when sections are not enough, keeping speed in mind.
3. **Page outline**:
   - Hero: headline with the offer, product image or video, CTA
   - Benefits (3-5) and how it works
   - Social proof: reviews, UGC, press
   - Offer details: price, bundle, guarantee, delivery
   - FAQ and final CTA
4. **Mobile first**: most campaign traffic is mobile; sticky CTA, fast images.
5. **Tracking**: UTM parameters, conversion events, a discount code or URL unique to the campaign.
6. **Test**: one variant at a time (headline, hero, offer) with `shopify-ab-testing`.

## Output Format

1. Page outline with copy for each section
2. Build instructions (template and sections or builder)
3. Tracking setup
4. Test plan

To audit an existing page, use `ecommerce-landing-page`.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-landing-page-builder -g
```

## Example Requests

- "Help me with shopify landing page builder for my Shopify store"
- "What are the best practices for shopify landing page builder?"
- "Audit my current shopify landing page builder setup and suggest improvements"
- "Create a step-by-step shopify landing page builder implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

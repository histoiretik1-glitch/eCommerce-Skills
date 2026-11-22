---
name: shopify-theme-optimization
description: "Shopify theme choice and tuning. Compares Online Store 2.0 themes (such as Dawn) with the current one, decides keep or switch given custom Liquid code, and tunes sections, app blocks, fonts and mobile layout. Use whenever a Shopify store owner asks which theme to choose, whether to switch themes, or how to clean up or customize theme code (for a full speed fix plan use `shopify-speed-optimization`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Theme Optimization

Theme speed and UX optimization — Core Web Vitals, Liquid code, image loading, mobile responsiveness.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Choosing and tuning the Shopify theme itself: Liquid code, sections, mobile UX.

Part of: Shopify store speed. For neighbouring jobs, use the matching skill instead:

- `shopify-speed-optimization` — Full speed audit of a Shopify store and the prioritized fix plan (apps, images, scripts, theme).
- `shopify-page-speed` — Measuring Core Web Vitals and diagnosing which pages and elements are slow.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Choose, configure and tune the Shopify theme itself for speed, mobile UX and conversion.

## When to Use

- Choosing or switching a Shopify theme
- The theme is slow, cluttered or hard to use on mobile
- Customizing Liquid code or sections without breaking performance

## Inputs to Collect

Current theme and version (Online Store 2.0 or older), customizations made in code, installed apps that inject into the theme, store type (catalog size, product types), brand guidelines.

## Workflow

1. **Theme fit**: an Online Store 2.0 theme (sections and app blocks on every page) is easier to maintain; check the theme's demo speed and features against the store's needs (filters, mega menu, variant display).
2. **Update**: keep the theme on a recent version; customizations made directly in code make updates harder, so document them.
3. **Layout and UX**: clear header and search, sticky add-to-cart on mobile, readable fonts, fewer home page sections, product page with images, price, variants, reviews and delivery information above the fold.
4. **Code quality**: remove unused sections and snippets, avoid loading app code globally when it is needed on one template, use theme app blocks instead of pasted code, limit custom fonts.
5. **Media**: responsive images with explicit width and height (prevents layout shift), video only where it sells.
6. **Test** on real phones and with PageSpeed Insights before publishing a new theme version (use an unpublished theme copy).

## Output Format

1. Theme recommendation or keep/switch decision
2. UX changes per template (home, collection, product, cart)
3. Code clean-up list
4. Publishing checklist (duplicate theme, test, publish)

Shopify admin menus, app names and plan features change; confirm in the Shopify Help Center before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-theme-optimization -g
```

## Example Requests

- "Help me with shopify theme optimization for my Shopify store"
- "What are the best practices for shopify theme optimization?"
- "Audit my current shopify theme optimization setup and suggest improvements"
- "Create a step-by-step shopify theme optimization implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

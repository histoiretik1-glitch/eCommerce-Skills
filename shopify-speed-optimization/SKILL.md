---
name: shopify-speed-optimization
description: "Shopify store speed fix plan. Audits everything that slows a Shopify store (apps and their scripts, images, third-party tags, theme sections), ranks the fixes by effort and impact and plans the clean-up. Use when a Shopify store is slow and the owner wants a prioritized action plan (to measure Core Web Vitals use `shopify-page-speed`; to change or tune the theme use `shopify-theme-optimization`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Speed Optimization

Store speed audit — lazy loading, image compression, app bloat removal, theme code optimization.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Full speed audit of a Shopify store and the prioritized fix plan (apps, images, scripts, theme).

Part of: Shopify store speed. For neighbouring jobs, use the matching skill instead:

- `shopify-page-speed` — Measuring Core Web Vitals and diagnosing which pages and elements are slow.
- `shopify-theme-optimization` — Choosing and tuning the Shopify theme itself: Liquid code, sections, mobile UX.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Run a complete speed audit of a Shopify store and turn it into a prioritized fix plan.

## Inputs to Collect

Store URL, theme name and version, installed apps (and which load scripts on the storefront), main templates (home, collection, product), Shopify's web performance report and a PageSpeed Insights run for the home and a product page.

## Workflow

1. **Baseline**: Core Web Vitals (LCP, INP, CLS) from real users in Shopify's web performance report, plus lab scores from PageSpeed Insights on mobile. `shopify-page-speed` details the measurement.
2. **Find the weight**: list third-party scripts by app (Chrome DevTools Network or the PageSpeed "third-party" audit); each app embed or snippet costs time.
3. **Apps**: remove unused apps and their leftover code; replace several single-purpose apps by one; prefer apps that use theme app extensions.
4. **Images**: right-size images (Shopify serves responsive sizes when the theme uses `image_url` with widths and `srcset`), lazy-load below-the-fold images, preload only the hero image.
5. **Theme**: heavy sliders, autoplay videos and large font files on the home page; theme-level fixes go to `shopify-theme-optimization`.
6. **Other scripts**: tag managers, chat widgets, pixels: load them after interaction where possible.
7. **Re-measure** after each batch of changes; real-user metrics need weeks to update.

## Priority Matrix

| Fix | Effort | Typical impact |
|-----|--------|----------------|
| Remove unused apps and leftover code | Low | High |
| Compress and right-size hero and product images | Low | High |
| Defer chat/review widgets | Medium | Medium |
| Replace a heavy theme section | Medium | Medium |
| Change theme | High | High |

## Output Format

1. Baseline metrics per template
2. Ranked list of what slows the store (apps, images, scripts, theme)
3. Fix plan with effort, expected impact and owner
4. Re-measurement plan

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-speed-optimization -g
```

## Example Requests

- "Help me with shopify speed optimization for my Shopify store"
- "What are the best practices for shopify speed optimization?"
- "Audit my current shopify speed optimization setup and suggest improvements"
- "Create a step-by-step shopify speed optimization implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

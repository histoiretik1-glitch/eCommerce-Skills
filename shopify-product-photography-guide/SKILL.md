---
name: shopify-product-photography-guide
description: "Shopify product photography guide. DIY setup, lighting, backgrounds, editing, lifestyle and 360 images for Shopify product pages, with image sizes and file optimization for page speed. Use when a Shopify store owner asks how to take or improve product photos."
metadata:
  nexscope:
    category: shopify
---

# Shopify Product Photography Guide

DIY product photography — setup, lighting, backgrounds, editing, lifestyle shots, 360 views.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Shoot and prepare product photos that make Shopify product pages convert and load fast.

## Inputs to Collect

Products and their size and materials, available space, phone or camera, budget for lights and backdrops, theme's image ratio (square or portrait), brand style.

## Workflow

1. **Shot list per product**: white or neutral background hero, angles, detail/texture, scale (in hand or on a person), lifestyle in use, variants, packaging, 360 or short video for complex products.
2. **Setup**: window light or two soft lights, a white sweep or foam board reflectors, tripod, fixed white balance.
3. **Consistency**: same ratio, background and framing for all products so collection grids look clean (match the theme's aspect ratio, square is common).
4. **Editing**: crop, straighten, remove dust, correct color to match the real product; no misleading retouching.
5. **Export for Shopify**: high resolution (square around 2048 px is a common recommendation) but compressed files, descriptive file names, alt text for each image.
6. **Upload**: hero first, variant images assigned to variants, video on the product page.

## Output Format

1. Shot list per product
2. Equipment list for the budget
3. Lighting and camera settings
4. Editing and export checklist

For Etsy listing photos, see `etsy-listing-photography`.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-product-photography-guide -g
```

## Example Requests

- "Help me with shopify product photography guide for my Shopify store"
- "What are the best practices for shopify product photography guide?"
- "Audit my current shopify product photography guide setup and suggest improvements"
- "Create a step-by-step shopify product photography guide implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

---
name: shopify-google-channel
description: "Shopify to Google connection. Installs and configures the Google & YouTube app, verifies the store in Merchant Center, syncs products with GTINs, brands and shipping settings, fixes product disapprovals and turns on free listings across Google. Use when a Shopify store owner wants products to appear on Google or has Merchant Center sync errors (for ad campaign strategy use `google-shopping-optimization`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Google Channel

Google integration — Shopping feed, Performance Max, free listings, Merchant Center optimization.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Connecting a Shopify store to Google with the Google & YouTube channel and Merchant Center.

Part of: Google Shopping and product feeds. For neighbouring jobs, use the matching skill instead:

- `google-shopping-optimization` — Google Shopping and Performance Max campaign strategy, bids and ROAS.
- `ecommerce-feed-management` — Monitoring and fixing product feeds for any channel (sync errors, missing SKUs, attributes).

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Connect a Shopify store to Google with the Google & YouTube app and keep the Merchant Center feed healthy.

## Inputs to Collect

Google Merchant Center and Google Ads accounts, markets, catalog size, product data quality (GTINs, brands, categories), current Merchant Center errors or warnings.

## Workflow

1. **Install the Google & YouTube app** and connect Merchant Center (verify and claim the store domain) and Google Ads.
2. **Product sync**: map products and variants; fill GTIN/barcode, brand, product category, condition, shipping and tax settings for each market.
3. **Fix diagnostics** in Merchant Center: disapproved products, price or availability mismatches, missing identifiers, image problems, policy issues.
4. **Free listings**: make sure products show in free listings across Google surfaces.
5. **Performance Max** from the app or Google Ads: start with best sellers, a realistic ROAS target and the conversion tracking in place. Campaign strategy, bids and structure belong to `google-shopping-optimization`.
6. **Monitor** sync status and Merchant Center diagnostics weekly; feed errors silently cut traffic.

## Output Format

1. Connection and verification checklist
2. Product data fixes (by error type)
3. Free listings and Performance Max launch steps
4. Weekly monitoring checklist

For feeds on several channels, see `ecommerce-feed-management`.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-google-channel -g
```

## Example Requests

- "Help me with shopify google channel for my Shopify store"
- "What are the best practices for shopify google channel?"
- "Audit my current shopify google channel setup and suggest improvements"
- "Create a step-by-step shopify google channel implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

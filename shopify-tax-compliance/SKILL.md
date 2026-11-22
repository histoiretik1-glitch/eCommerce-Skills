---
name: shopify-tax-compliance
description: "Shopify tax setup and compliance. Configures sales tax, VAT/GST, duties, tax-exempt customers and tax reports in Shopify. Use when a Shopify store owner asks how to charge or report taxes correctly in Shopify (general guidance, not legal or tax advice)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Tax Compliance

Tax setup and compliance — sales tax, VAT, duty collection, tax-exempt customers, reporting.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Configure taxes in Shopify so the store charges, records and reports them correctly. General guidance, not tax or legal advice.

## Inputs to Collect

Where the business is registered, where it has sales tax nexus or VAT/GST registrations, markets sold to, product types (some have special rates or exemptions), B2B customers, current Shopify tax settings and any tax app.

## Workflow

1. **Registrations first**: Shopify calculates and collects tax only where the merchant is registered; registering is the merchant's job (with an accountant).
2. **United States**: add each state registration in Settings → Taxes and duties; Shopify Tax (where available) calculates rates by address and product category; monitor nexus thresholds by state.
3. **EU / UK / other VAT and GST**: register (EU One-Stop Shop for cross-border B2C sales if applicable), enter registration numbers, decide whether prices include tax per market.
4. **Product tax categories and overrides** for products with special rates.
5. **Duties and import taxes** for international orders (see `shopify-international`).
6. **Tax-exempt customers**: mark B2B or exempt customers and keep their certificates.
7. **Reporting**: use Shopify's tax reports for filing; reconcile with payouts; keep records.

## Output Format

1. Registration checklist by region
2. Shopify tax settings to configure
3. Product categories and overrides
4. Filing and reporting routine

Always have the setup reviewed by a tax professional. Shopify admin menus, app names and plan features change; confirm in the Shopify Help Center before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-tax-compliance -g
```

## Example Requests

- "Help me with shopify tax compliance for my Shopify store"
- "What are the best practices for shopify tax compliance?"
- "Audit my current shopify tax compliance setup and suggest improvements"
- "Create a step-by-step shopify tax compliance implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

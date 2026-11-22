---
name: localization-testing
description: "Localization and international QA for online stores. Tests each target market for translation quality and completeness, currency and number formats, price rounding, tax display (VAT-inclusive vs added), duties, shipping options, payment methods, legal pages and checkout, with a test matrix and pass/fail criteria. Use when a store launches or audits a country, language or currency, or customers abroad report wrong prices, untranslated text or checkout problems."
nexscope:
  name: "Localization Testing"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "localization"
    - "i18n"
    - "testing"
    - "international"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "localization testing"
---

# Localization Testing

AI-powered localization and internationalization testing skill for e-commerce sites. Designs multi-language QA frameworks, currency validation checks, shipping info verification, and regional compliance audits.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Testing translations, currencies, prices, taxes, shipping and legal information per country.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Markets: countries, languages, currencies, domains/subfolders | Platform market settings (e.g. Shopify Markets) |
| Prices per market and rounding rules | Platform pricing settings |
| Tax and duty setup per market | Tax settings, accountant |
| Shipping zones and rates, payment methods per market | Platform settings |
| Translation source (human, app, machine) | Translation app / agency |
| Legal requirements per market (returns, imprint, cookie consent) | Legal advice |

## Workflow

1. **Build the test matrix**: markets × key pages (home, collection, product, cart, checkout, account, emails, legal pages).
2. **Language**: no untranslated strings (search for source-language words), correct terminology, no truncated text (some languages run longer than English), right-to-left layout if relevant.
3. **Formats**: currency symbol and position, decimal and thousands separators, dates, units (cm/inch, kg/lb), sizes.
4. **Prices and taxes**: correct converted or fixed prices, rounding, VAT-inclusive display where customers expect it, duties shown or collected as configured.
5. **Shipping and payments**: available methods, delivery estimates, local payment methods appear and work in test mode.
6. **Legal and trust**: returns policy, terms, privacy, required notices, customer service language.
7. **Emails and notifications** in the right language and currency.
8. **Retest** after every catalog, app or theme change that touches text.

## Calculations and Tools

- **Expected formats** can be generated with the browser's standard `Intl` API to compare against the store:

```javascript
new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(1234.5)  // "1.234,50 €"
new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' }).format(1234.5)  // "£1,234.50"
```

- **Price check**: displayed price = base price × exchange rate (or fixed market price), rounded with the market's rule, plus VAT when displayed tax-inclusive. Record expected vs displayed for each test product.

## Example Requests

- "We're launching our Shopify store in Germany and France. Build a localization test checklist."
- "Customers in Canada see US prices at checkout. What should we test?"
- "Check our product pages for untranslated text and wrong currency formats in Spanish."

## Output Format

```
LOCALIZATION TEST REPORT — [Market]
| Page / flow | Check | Expected | Observed | Pass/Fail | Severity |
Price checks: | Product | Base | Expected local price | Displayed | OK? |
Blocking issues before launch: [...]
```

## Quality Checks

- Every market is tested from that market (VPN or platform preview) and in its currency.
- Checkout is tested to the payment step in test mode for each market.
- Expected values (formats, tax rules) cite their source; legal points are marked "to confirm with counsel".
- Machine-translated key pages (product, checkout, policies) are reviewed by a fluent speaker.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: observed values captured during the tests (with screenshots).
- **To confirm**: tax and legal requirements per country (they change; confirm with an accountant or lawyer); typical text expansion rates are estimates.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill localization-testing -g
```

## Usage

**Input:**
Multi-language site URL(s), target markets, supported languages/currencies

**Output:**
Localization test plan, translation quality checklist, currency/pricing validation, shipping info audit, regional compliance check

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up localization testing for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*

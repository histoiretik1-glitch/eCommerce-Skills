---
name: shopify-store-setup
description: "Step-by-step Shopify store setup guide. From account creation to first sale — theme selection, product uploads, payment and shipping configuration, domain setup, and launch checklist. Use when the user asks for help creating a new Shopify store, choosing plan and theme, configuring payments, shipping, domain and launch checklist."
---

# Shopify Store Setup

Step-by-step Shopify store setup guide. From account creation to first sale — theme selection, product uploads, payment and shipping configuration, domain setup, and launch checklist.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Launching a new Shopify store: plan, payments, theme, products, shipping, taxes, domain.

Part of: Shopify setup, analytics and conversion. For neighbouring jobs, use the matching skill instead:

- `shopify-analytics-guide` — Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.
- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.
- `shopify-ab-testing` — Running A/B tests on a Shopify store with Shopify tools and apps.

<!-- role-and-scope:end -->

## Capabilities

- Shopify plan comparison and selection
- Theme selection and customization strategy
- Product catalog setup: titles, descriptions, images, variants
- Payment gateway configuration (Shopify Payments, PayPal, etc.)
- Shipping zones, rates, and carrier setup
- Tax configuration by region
- Domain connection and email setup
- Pre-launch checklist and soft launch strategy

## Platform Rules and Constraints

Shopify setup rules at the last review of this skill (November 2026, Shopify Help Center and pricing page). Plan names, prices and rates change by country: items marked **[check]** must be confirmed on shopify.com/pricing for the seller's country.

- **Plans:** Starter, Basic, Grow (named "Shopify" in some countries), Advanced and Plus **[check]**. Plans differ in card processing rates, third-party transaction fees, staff accounts, reports, shipping discounts and calculated carrier rates.
- **Third-party payment providers:** if Shopify Payments is available but not used, Shopify charges a transaction fee on each order on top of the provider's fees (2% / 1% / 0.6% on Basic / Grow / Advanced at last review **[check]**). Shopify Payments availability depends on the country and business type.
- **Free trial and password page:** the store is password-protected during the trial; you must pick a paid plan to remove the password and take orders.
- **Required store information:** legal business name and address, contact information page, and policies (refund, privacy, terms of service, shipping) in Settings > Policies; Shopify can generate templates but they must be reviewed for your country.
- **Taxes:** Shopify calculates sales tax, VAT and GST from the registrations you enter (Settings > Taxes and duties); it does not register or file for you. US sellers collect only where they have nexus and are registered; EU sellers selling cross-border to consumers use the OSS scheme above the EU threshold.
- **Shipping:** shipping profiles (general and custom) contain zones and rates: flat, weight- or price-based, or carrier-calculated (calculated rates depend on plan **[check]**). Shopify Shipping labels are available in some countries.
- **Domains:** buy through Shopify or connect a third-party domain (A record to Shopify's IP and CNAME www to shops.myshopify.com **[check]**); set one primary domain; SSL is automatic.
- **Markets:** selling to several countries uses Shopify Markets (currencies, languages, duties) **[check: features by plan]**.

## Data Needed

| Data | Why |
|------|-----|
| Country of the business, legal entity, bank account | Shopify Payments eligibility and payouts |
| Expected monthly sales and order count for 12 months | Plan choice (rates vs subscription) |
| Catalogue: products, variants, photos, weights, SKUs, barcodes | Product setup and shipping rates |
| Shipping origin, package sizes, carriers, destination countries | Shipping profiles and rates |
| Tax registrations (states, VAT numbers) | Tax settings |
| Domain name and email provider | Domain connection and sender email |

## Workflow

1. **Choose the plan** with the break-even formula below using 12-month sales estimates; start on the lowest plan that has the features you need now.
2. **Set store details:** legal name, address, currency, time zone, units, order ID format, staff accounts with limited permissions.
3. **Activate payments:** Shopify Payments (identity and bank verification), then Shop Pay and express wallets; add PayPal if your buyers expect it; check payout schedule.
4. **Pick and set up the theme:** a free Online Store 2.0 theme (e.g. Dawn) unless a paid theme solves a specific need; configure header, navigation, homepage sections, product template, cart type; check mobile first.
5. **Add products:** title, description, media, price and compare-at price, cost per item (for profit reports), SKU, barcode, weight, variants, inventory tracking; organise collections (automated rules where possible). Use the product CSV import for more than 20 products.
6. **Configure shipping and taxes:** shipping profiles and zones, rates and free-shipping threshold, package sizes; tax registrations and tax-inclusive pricing where required.
7. **Legal and trust:** policies, contact page, cookie/consent banner where required (EU/UK), customer accounts setting, notification emails with your branding and sender domain.
8. **Pre-launch checklist and test:** connect the domain, place test orders (Bogus Gateway or test mode, then a real low-value order refunded), check emails, taxes, shipping costs per zone, mobile checkout; remove the password page; connect Google & YouTube and Meta channels if planned.

## Calculations and Tools

- **Monthly cost of a plan** = subscription + card rate × online sales + fixed fee per transaction × orders (+ third-party transaction fee × sales if not using Shopify Payments).
- **Plan break-even sales** between a cheaper plan A and a higher plan B = (subscription B − subscription A) ÷ (card rate A − card rate B), ignoring per-transaction fixed fees.
- **Free-shipping threshold**: set it where the margin on the extra basket covers the average shipping cost: threshold ≥ shipping cost ÷ gross margin % added to the current AOV as a first test (heuristic).
- **Product price check** = price − cost per item − payment fees − shipping subsidy − returns allowance > 0 for every product.

## Worked Example

*Illustrative example with invented plan figures (read the real ones on Shopify's pricing page for your country):* plan A costs $39/month with a 2.9% card rate, plan B $105/month with 2.7%. Break-even = (105 − 39) ÷ (0.029 − 0.027) = **$33,000 of online card sales per month**. A new store expecting $8,000/month stays on plan A until sales approach that level, unless it needs a feature only plan B has.

## Example Requests

- "Walk me through setting up a new Shopify store in France for handmade candles: plan, payments, taxes, shipping and launch checklist."
- "Which Shopify plan should I choose if I expect $8,000 a month in sales the first year and $40,000 the second?"
- "Set up Shopify shipping for a 1.2 kg parcel shipped from the US to the US and Canada, with free shipping over a threshold."

## Output Format

1. Plan recommendation with the cost comparison table (verified rates with date).
2. Setup checklist by area (store details, payments, theme, products, shipping, taxes, legal, domain), each with status and owner.
3. Shipping profile table: zones, rates, conditions, free-shipping threshold.
4. Launch test log: test orders, emails, tax and shipping verification per zone.

## Quality Checks

- Plan prices and rates taken from Shopify's pricing page for the seller's country, with date.
- Tax settings match the seller's actual registrations; no advice to collect tax where the seller is not registered.
- Every product has cost per item, weight and SKU set.
- Policies and contact page published; legal texts reviewed for the seller's country.
- At least one real test order placed and refunded before launch; mobile checkout tested.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** plan prices and rates from Shopify's pricing page for the seller's country on a stated date, the seller's costs and carrier rates.
- **Estimates:** first-year sales, order count, free-shipping threshold effect.
- Plan names and fee structures were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-store-setup -g
```

## Usage

Ask your AI agent:

- "Walk me through setting up a new Shopify store from scratch."
- "Which Shopify theme is best for a fashion brand?"
- "Set up my shipping rates and payment options on Shopify."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

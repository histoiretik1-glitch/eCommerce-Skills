---
name: minimum-advertised-price
description: "Minimum Advertised Price (MAP) policy and enforcement for brands. Drafts a MAP policy (scope, prices, exceptions, enforcement steps), monitors advertised prices across Amazon, Walmart, eBay, Shopify stores and other sites, flags violations by severity and repeat offender with a script, and prepares notices and escalation. Use when a brand asks how to create or enforce a MAP policy, why resellers undercut its prices, or how to check and document MAP violations."
nexscope:
  name: "Minimum Advertised Price"
  category: "Pricing & Profitability"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "MAP"
    - "pricing"
    - "compliance"
    - "brand-protection"
  model: "any"
  tokens: "~2000"
  keywords:
    - "minimum advertised price"
    - "map enforcement"
    - "map violation monitoring"
---

# Minimum Advertised Price

AI-powered MAP (Minimum Advertised Price) policy and enforcement skill. Helps brands create MAP policies, monitor violations across channels, manage dealer compliance, and design enforcement workflows.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** MAP policy and enforcement: policy document, violation checks across channels and escalation steps.

Part of: Pricing. For neighbouring jobs, use the matching skill instead:

- `competitor-price-analysis` — One-off analysis of competitor prices and positioning.
- `competitor-price-tracker` — Ongoing tracking of competitor prices with alerts.
- `competitive-pricing-strategy` — Price architecture and response rules against competitors.
- `dynamic-pricing-ecommerce` — Automated repricing rules with floors, ceilings and guardrails.
- `price-optimization-tool` — Choosing a price from unit economics, elasticity and price tests.
- `walmart-price-tracker` — Walmart-specific price tracking and repricing.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Products and their MAP prices | Brand price list |
| Authorized resellers and channels | Distribution agreements |
| Observed advertised prices with seller, channel, date, URL and screenshot | Manual checks, price monitoring tools, `competitor-price-tracker` |
| Current policy and past notices | Legal / sales team |

## Workflow

1. **Legal frame first**: in the US, MAP policies are usually unilateral policies about advertised prices; in the EU and some other regions, minimum price restrictions can be treated as resale price maintenance. Have counsel approve the policy before use.
2. **Policy content**: products covered, MAP per product, what counts as "advertised" (listing price, cart price, coupons), allowed exceptions (clearance, bundles, dated promotions), monitoring, enforcement steps, effective date.
3. **Monitor** advertised prices on all channels on a fixed schedule; keep evidence (screenshot, URL, date, seller).
4. **Check** observations against MAP with the script; separate authorized resellers from unknown sellers (unknown sellers often need IP/authorization action instead, see `brand-protection-amazon` and the other brand-protection skills).
5. **Enforce consistently**: same step for the same violation count, documented: notice → warning → escalation defined in the policy.
6. **Review** monthly: compliance rate, repeat offenders, channels with most violations.

## Calculations and Tools

`scripts/map_check.py` compares observed prices with MAP:

```bash
python3 scripts/map_check.py '{"map_prices": {"BLENDER-PRO": 129.99}, "observations": [{"sku": "BLENDER-PRO", "seller": "KitchenDeals", "channel": "Amazon", "price": 119.99, "date": "2026-11-18"}]}'
```

- Gap % = (MAP − observed price) ÷ MAP; severity bands (default < 5%, 5-15%, > 15%) are a policy choice.
- Compliance rate = observations at or above MAP ÷ all observations.
- Next step follows the seller's violation count (1st notice, 2nd warning, 3rd escalation).

## Example Requests

- "Draft a MAP policy for our kitchen appliance brand sold through 40 resellers."
- "Here are this week's reseller prices on Amazon and Walmart. Which ones break our MAP?"
- "A reseller keeps advertising below MAP. What should our escalation look like?"

## Output Format

```
MAP REPORT — [period]
Compliance rate: X% over N observations
| SKU | Seller | Channel | Price | MAP | Gap | Severity | Date | Evidence |
| Seller | Violations | Next step |
Policy updates needed: [...]
```

## Quality Checks

- Every violation has evidence (URL, date, screenshot) and the MAP in force on that date.
- Unknown or unauthorized sellers are routed to brand-protection actions, not MAP notices.
- Notices are consistent with the policy wording; the policy is marked "for legal review".
- Coupon or cart-only prices are handled as the policy defines.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: observed prices with evidence; MAP list from the brand.
- **Not legal advice**: enforceability depends on jurisdiction and contracts; confirm with counsel.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill minimum-advertised-price -g
```

## Usage

**Input:**
Brand name, product line, distribution channels, current pricing policy

**Output:**
MAP policy document, violation monitoring plan, dealer compliance checklist, enforcement escalation procedures

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up minimum advertised price for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*

---
name: brand-protection-walmart
version: 1.0.0
author: Nexscope AI
description: "Walmart brand protection toolkit. Detect unauthorized sellers, counterfeits, and MAP violations. Includes Walmart Brand Portal reporting, WFS seller monitoring, and complaint templates. No API key required. Use when a brand owner asks about unauthorized Walmart sellers, counterfeits, MAP violations, or how to report infringement in Walmart Brand Portal."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — Walmart 🛡️

Protect your brand from unauthorized sellers and counterfeit products on Walmart Marketplace.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill brand-protection-walmart -g
```

## Features

- **Unauthorized Seller Detection** — Find sellers without authorization
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Review-based fake detection
- **Trademark Abuse** — Listing title/description infringement
- **Walmart Brand Portal** — Official reporting templates
- **WFS Monitoring** — Track fulfillment-verified sellers

## Walmart-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Unauthorized Sellers | Seller ID monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Review keyword analysis | 🔴 High |
| Trademark | Title pattern matching | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Immediate threat | Report within 24h |
| ⚠️ Medium | Potential concern | Investigate further |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "trademark_number": "US12345678",
  "brand_portal_enrolled": true,
  "authorized_sellers": ["seller_id_1", "seller_id_2"],
  "protected_item_ids": ["123456789"],
  "min_price": 29.99
}
```

## Usage

### Detection

```bash
python3 scripts/detector.py
```

### Generate Complaint Templates

```bash
# Walmart Brand Portal report
python3 scripts/templates.py brand-portal

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Test buy guide
python3 scripts/templates.py testbuy
```

## Script Notes

- `scripts/detector.py` and `scripts/templates.py` are shared by the five brand-protection skills. They use this skill's platform by default (Walmart Brand Portal); `--platform=amazon|ebay|shopify|tiktok|walmart` overrides it.
- `detector.py` runs on built-in demo data to show the report format. For a real case, collect the seller's listings, sellers and prices, then apply the same checks and action plan in the conversation.
- `templates.py` sub-commands: `complaint` (aliases `vero`, `dmca`, `platform-report`, `ip-report`, `seller-complaint`, `content-takedown`, `brand-portal`), `cease` (`cease-desist`), `testbuy`, `map`, or `all`. Replace the demo brand, seller and listing IDs with the user's data before sending anything.
- `--zh` (Chinese wording) is available for Amazon only.

## Output Example

```
🛡️ Walmart Brand Protection Report

Brand: YourBrand
Items Monitored: 10
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Item: 123456789
├── 2 unauthorized sellers detected
├── Lowest price: $17.99 (MAP: $29.99)
└── Action: File Brand Portal complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ COUNTERFEIT SIGNALS

Reviews mentioning "fake": 4
Reviews mentioning "not original": 1
Recommendation: Order test buy
```

## Walmart Brand Portal

Walmart's Brand Portal allows brand owners to:
- Report counterfeit listings
- Remove unauthorized sellers
- Monitor brand health metrics

## Action Workflow

```
Monitor Walmart Listings
      ↓
Detect Violation
      ↓
Collect Evidence
      ↓
File Brand Portal Report
      ↓
Track Resolution
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

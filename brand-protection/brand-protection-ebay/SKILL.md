---
name: brand-protection-ebay
version: 1.0.0
description: "eBay brand protection toolkit. Detect unauthorized sellers, counterfeits, and VeRO violations. Includes price monitoring, trademark abuse detection, VeRO complaint templates, and enforcement guides. No API key required. Use when a brand owner asks about unauthorized eBay sellers, counterfeit listings, or how to file a VeRO notice."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — eBay 🛡️

Protect your brand from unauthorized sellers and counterfeits on eBay.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill brand-protection-ebay -g
```

## Features

- **Unauthorized Seller Detection** — Find sellers without authorization
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Feedback-based fake detection
- **Trademark Abuse** — Listing title/description infringement
- **VeRO Complaint Templates** — eBay's rights owner program
- **Enforcement Guide** — Step-by-step takedown process

## eBay-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Unauthorized Sellers | Seller ID monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Feedback keyword analysis | 🔴 High |
| Trademark | Title pattern matching | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Immediate threat | File VeRO within 24h |
| ⚠️ Medium | Potential concern | Monitor and investigate |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "trademark_number": "US12345678",
  "vero_enrolled": true,
  "authorized_sellers": ["seller_id_1", "seller_id_2"],
  "protected_item_ids": ["123456789012"],
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
# VeRO complaint
python3 scripts/templates.py vero

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Test buy guide
python3 scripts/templates.py testbuy
```

## Script Notes

- `scripts/detector.py` and `scripts/templates.py` are shared by the five brand-protection skills. They use this skill's platform by default (eBay VeRO Program (NOCI)); `--platform=amazon|ebay|shopify|tiktok|walmart` overrides it.
- `detector.py` runs on built-in demo data to show the report format. For a real case, collect the seller's listings, sellers and prices, then apply the same checks and action plan in the conversation.
- `templates.py` sub-commands: `complaint` (aliases `vero`, `dmca`, `platform-report`, `ip-report`, `seller-complaint`, `content-takedown`, `brand-portal`), `cease` (`cease-desist`), `testbuy`, `map`, or `all`. Replace the demo brand, seller and listing IDs with the user's data before sending anything.
- `--zh` (Chinese wording) is available for Amazon only.

## Output Example

```
🛡️ eBay Brand Protection Report

Brand: YourBrand
Items Monitored: 8
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Item: 123456789012
├── Unauthorized seller detected
├── Price: $15.99 (MAP: $29.99)
└── Action: File VeRO complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ COUNTERFEIT SIGNALS

Feedback mentioning "fake": 3
Feedback mentioning "not genuine": 2
Recommendation: Order test buy
```

## VeRO Program

eBay's Verified Rights Owner Program allows brand owners to:
- Report counterfeit listings
- Remove trademark violations
- Protect intellectual property

## Action Workflow

```
Monitor Listings
      ↓
Detect Violation
      ↓
Collect Evidence
      ↓
File VeRO Complaint
      ↓
Track Removal
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

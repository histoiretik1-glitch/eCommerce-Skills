---
name: brand-protection-shopify
version: 1.0.0
author: Nexscope AI
description: "Shopify/DTC brand protection toolkit. Detect counterfeit stores, unauthorized resellers, and trademark violations. Includes DMCA takedown templates, domain monitoring, and social media infringement detection. No API key required. Use when a brand owner asks about copycat or counterfeit websites, unauthorized resellers, or how to send a DMCA or Shopify IP report."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — Shopify/DTC 🛡️

Protect your brand from counterfeit stores and unauthorized resellers in the DTC space.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection-shopify -g
```

## Features

- **Counterfeit Store Detection** — Find fake stores copying your brand
- **Domain Monitoring** — Track similar/typosquatting domains
- **Social Media Infringement** — Detect unauthorized ads/posts
- **Trademark Abuse** — Logo and brand name misuse
- **DMCA Takedown Templates** — Copyright infringement removal
- **Cease & Desist Letters** — Legal notice templates

## DTC-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Fake Stores | Domain + content matching | 🔴 High |
| Unauthorized Resellers | Price/image tracking | 🔴 High |
| Social Ads | Ad library monitoring | ⚠️ Medium |
| Trademark | Logo/name detection | 🔴 High |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Active infringement | DMCA within 24h |
| ⚠️ Medium | Potential concern | Investigate further |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "official_domain": "yourbrand.com",
  "trademark_number": "US12345678",
  "logo_url": "https://yourbrand.com/logo.png",
  "social_handles": {
    "instagram": "@yourbrand",
    "facebook": "yourbrand",
    "tiktok": "@yourbrand"
  }
}
```

## Usage

### Detection

```bash
python3 scripts/detector.py
```

### Generate Takedown Templates

```bash
# DMCA takedown
python3 scripts/templates.py dmca

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Platform report (Shopify)
python3 scripts/templates.py platform-report
```

## Script Notes

- `scripts/detector.py` and `scripts/templates.py` are shared by the five brand-protection skills. They use this skill's platform by default (Shopify's IP infringement report plus DMCA/trademark notices to the store's host and registrar); `--platform=amazon|ebay|shopify|tiktok|walmart` overrides it.
- `detector.py` runs on built-in demo data to show the report format. For a real case, collect the seller's listings, sellers and prices, then apply the same checks and action plan in the conversation.
- `templates.py` sub-commands: `complaint` (aliases `vero`, `dmca`, `platform-report`, `ip-report`, `seller-complaint`, `content-takedown`, `brand-portal`), `cease` (`cease-desist`), `testbuy`, `map`, or `all`. Replace the demo brand, seller and listing IDs with the user's data before sending anything.
- `--zh` (Chinese wording) is available for Amazon only.

## Output Example

```
🛡️ Shopify/DTC Brand Protection Report

Brand: YourBrand
Official Domain: yourbrand.com
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Fake Store Detected:
├── Domain: your-brand-sale.com
├── Copying: Product images, descriptions
└── Action: File DMCA + domain complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ SOCIAL MEDIA INFRINGEMENT

Instagram: 2 unauthorized ads detected
Facebook: 1 fake page found
Recommendation: Report to platforms
```

## Takedown Templates Included

| Template | Use Case |
|----------|----------|
| DMCA Takedown | Hosting provider removal |
| Cease & Desist | Direct legal notice |
| Platform Report | Shopify abuse report |
| Social Report | Instagram/Facebook/TikTok |
| Domain Complaint | Registrar abuse report |

## Action Workflow

```
Monitor Web/Social
      ↓
Detect Infringement
      ↓
Document Evidence
      ↓
Send DMCA/C&D
      ↓
Report to Platforms
      ↓
Track Resolution
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

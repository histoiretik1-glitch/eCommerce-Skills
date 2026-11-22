---
name: ebay-review-checker
version: 1.0.0
description: "eBay review and feedback authenticity analyzer. Detect fake reviews, suspicious seller feedback patterns, and buyer manipulation. Includes time clustering detection, content similarity analysis, and eBay-specific red flag identification. Use when a eBay seller or buyer asks whether a product's reviews are fake or manipulated, wants to audit a competitor's reviews, or needs evidence of suspicious review patterns."
metadata: {"nexscope":{"emoji":"🔍","category":"ecommerce"}}
---

# eBay Review Checker 🔍

Review and feedback authenticity analyzer for eBay — detect fake reviews, suspicious patterns, and feedback manipulation.

## Workflow

1. **Collect reviews** of the eBay product: text, rating, date, and verified-purchase status where the platform shows it (export, copy-paste or CSV).
2. **Choose the depth**: with text only, content checks run; dates enable time clustering; verified status enables the verified-purchase ratio.
3. **Run the analyzer**: `python3 scripts/analyzer.py '<json list of reviews>'` (fields `content`, `rating`, `date`, `verified_purchase`; invalid fields stop the script with an error).
4. **Read the dimensions**: content similarity, time clustering, rating distribution, verified ratio, length and incentive keywords; note which ones drive the score.
5. **Check the flagged reviews** by hand before drawing conclusions; a high score is a signal, not proof.
6. **Act**: for your own listing, fix the causes; for a competitor's, report suspicious reviews through the platform's reporting tools with the evidence.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ebay-review-checker -g
```

## Features

- **Seller Feedback Analysis** — Analyze seller feedback authenticity
- **Buyer Feedback Patterns** — Detect suspicious buyer behavior
- **eBay-specific Red Flags** — Platform-specific warning signs
- **Progressive Analysis** — More data = deeper insights

## eBay-Specific Detection

| Signal | Description |
|--------|-------------|
| Feedback timing | Clustered feedback in short periods |
| Generic comments | "A+++" or "Great seller" patterns |
| Account age | New accounts leaving multiple feedbacks |
| Transaction patterns | Unusual buying/selling patterns |

## Risk Levels

| Score | Level | Description |
|-------|-------|-------------|
| 70-100 | ✅ Low Risk | Feedback appears authentic |
| 50-69 | ⚠️ Medium Risk | Some concerns found |
| 30-49 | 🔴 High Risk | Multiple red flags |
| 0-29 | 💀 Critical | Likely manipulated feedback |

## Usage

### Paste Feedback

```
Check this seller feedback:

Positive - Great seller, fast shipping! A+++
Positive - Excellent transaction, thank you!
Positive - Perfect! Would buy again.
Negative - Item never arrived.
```

### JSON Input

```bash
python3 scripts/analyzer.py '[
  {"content": "A+++ seller!", "rating": "positive", "date": "2024-01-15"},
  {"content": "Fast shipping", "rating": "positive", "date": "2024-01-15"}
]'
```

## Output Example

```
📊 eBay Feedback Authenticity Report

Seller: example_seller
Feedback Count: 50
Analysis Level: L3

━━━━━━━━━━━━━━━━━━━━━━━━

Authenticity Score: 72/100 ✅

Low Risk - Feedback appears authentic.

━━━━━━━━━━━━━━━━━━━━━━━━

Detection Results

✅ Time Clustering: Normal
⚠️ Generic Comments: 15% (slightly high)
✅ Account Diversity: Good
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

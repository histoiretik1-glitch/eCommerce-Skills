---
name: product-differentiation-amazon
version: 1.0.0
author: Nexscope AI
description: "Amazon product differentiation strategy tool. Analyze competitor weaknesses, extract pain points from negative reviews, identify unique selling points from positive reviews, and generate actionable differentiation strategies. Progressive L1-L4 analysis depth. Use when a Amazon seller asks how to stand out from competitors, which weaknesses or review complaints to exploit, or what unique selling points and positioning to use."
metadata: {"nexscope":{"emoji":"🎯","category":"ecommerce"}}
---

# Product Differentiation — Amazon 🎯

Develop winning product differentiation strategies by analyzing competitor reviews and market positioning.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill product-differentiation-amazon -g
```

## Features

- **Competitor Matrix** — Side-by-side product comparison
- **Pain Point Mining** — Extract issues from negative reviews
- **USP Extraction** — Identify selling points from positive reviews
- **Differentiation Opportunities** — Find gaps in the market
- **Positioning Strategy** — Market positioning recommendations
- **Action Plan** — Prioritized improvement roadmap

## Progressive Analysis Levels

| Level | Required Data | Unlocked Analysis |
|-------|---------------|-------------------|
| **L1 Basic** | Product info | Basic comparison matrix |
| **L2 Pain Points** | + Competitor negative reviews | Pain point analysis |
| **L3 USP** | + Your positive reviews | Selling point extraction |
| **L4 Complete** | + Market data | Full strategy & action plan |

## Analysis Dimensions

| Dimension | Method | Output |
|-----------|--------|--------|
| Feature Gap | Competitor comparison | Missing features list |
| Pain Points | Negative review NLP | Top complaints ranked |
| Selling Points | Positive review NLP | Key USPs identified |
| Price Position | Price-value mapping | Positioning quadrant |
| Quality Signals | Review sentiment | Quality perception score |

## Usage

### Interactive Mode

```bash
python3 scripts/analyzer.py
```

### With Parameters

```bash
python3 scripts/analyzer.py '{"my_product": {"name": "Wireless Earbuds Pro", "price": 49.99, "rating": 4.3, "review_count": 150, "features": ["feature A", "feature B"], "asin": "B08MYASIN1"}, "competitors": [{"name": "Competitor A", "price": 59.99, "rating": 4.1, "review_count": 500, "asin": "B08COMP1"}], "competitor_reviews": {"negative": ["Broke after two weeks", "Battery life is terrible", "Too expensive for this quality"]}, "my_reviews": {"positive": ["Great quality", "Fast shipping, well packaged"]}}'
```

Fields: `my_product` (required: name, price, rating, review_count, features…), `competitors` (list), `competitor_reviews` and `my_reviews` (`positive`, `negative`, `neutral` lists of review texts). Paste real competitor reviews: the script analyzes only what it is given; without input it shows a demo, labelled as such.

### Demo Mode

```bash
python3 scripts/analyzer.py --demo
```

## Input Example

```json
{
  "your_product": {
    "asin": "B08XXXXXX1",
    "title": "Wireless Earbuds Pro",
    "price": 49.99,
    "rating": 4.2,
    "features": ["Bluetooth 5.0", "30h battery", "IPX5"]
  },
  "competitors": [
    {
      "asin": "B08XXXXXX2",
      "title": "Competitor Earbuds A",
      "price": 39.99,
      "rating": 4.0
    }
  ],
  "negative_reviews": [...],
  "positive_reviews": [...]
}
```

## Output Example

```
🎯 Product Differentiation Report

Product: Wireless Earbuds Pro
Category: Electronics
Competitors Analyzed: 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 COMPETITOR COMPARISON MATRIX

Feature         | You  | Comp A | Comp B | Comp C
─────────────────────────────────────────────────
Bluetooth       | 5.0  | 5.0    | 4.2    | 5.0
Battery Life    | 30h  | 24h    | 20h    | 28h
Water Resist    | IPX5 | IPX4   | None   | IPX5
Noise Cancel    | ❌   | ❌     | ❌     | ✅
Price           | $50  | $40    | $30    | $70

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😤 TOP PAIN POINTS (from competitor reviews)

1. 🔴 Battery dies quickly (mentioned 45x)
2. 🔴 Poor Bluetooth connection (mentioned 32x)
3. 🟡 Uncomfortable fit (mentioned 28x)
4. 🟡 Case quality issues (mentioned 15x)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ YOUR UNIQUE SELLING POINTS

1. ⭐ Superior battery life (30h vs avg 24h)
2. ⭐ Better water resistance (IPX5)
3. ⭐ Stable connection (highlighted in reviews)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 DIFFERENTIATION OPPORTUNITIES

1. Add noise cancellation (gap in mid-range)
2. Improve comfort messaging
3. Highlight battery advantage in listing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ACTION PLAN

Priority | Action                    | Impact
─────────────────────────────────────────────
HIGH     | Update listing bullets    | +15% CVR
HIGH     | Add battery comparison    | +10% CVR
MEDIUM   | Request comfort reviews   | +5% rating
LOW      | Consider ANC version      | New SKU
```

## Strategy Framework

```
Competitor Analysis
      ↓
Pain Point Mining
      ↓
USP Identification
      ↓
Gap Analysis
      ↓
Positioning Strategy
      ↓
Action Plan
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

---
name: brand-monitoring
version: 1.0.0
author: Nexscope AI
description: "Brand mention analysis for e-commerce brands. Analyzes mentions collected from Reddit, news, YouTube, social media and the web (the script does not fetch them itself) for sentiment, platform split, engagement, influential posts and crisis signals, with a monitoring workflow and alert rules. Use when a brand asks what people say about it online, wants sentiment tracking or early warning of a PR crisis from mentions it has gathered or can search for."
metadata: {"nexscope":{"emoji":"📡","category":"ecommerce"}}
---

# Brand Monitoring 📡

Track brand mentions across social media platforms and analyze sentiment.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Tracking brand mentions across Reddit, news, YouTube and the web with sentiment and crisis alerts (script).

Part of: Brand and social listening. For neighbouring jobs, use the matching skill instead:

- `social-media-monitor` — Social listening on social networks: mentions, trends and competitor activity.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill brand-monitoring -g
```

## Features

- **Mention Monitoring** — Track brand mentions across platforms
- **Sentiment Analysis** — Positive/negative/neutral classification
- **Trend Tracking** — Monitor mention volume changes
- **Crisis Detection** — Alerts for negative spikes or crisis keywords
- **Competitor Comparison** — Share of voice analysis
- **Keyword Extraction** — Identify trending topics
- **Report Generation** — Weekly/monthly reports

## Supported Platforms

| Platform | Method | Stability |
|----------|--------|-----------|
| Reddit | Public JSON API | ⚠️ Rate limited |
| Google News | RSS Feed | ✅ Stable |
| DuckDuckGo | Instant Answer API | ✅ Stable |
| YouTube | HTML/RSS | ⚠️ Unstable |

## Analysis Dimensions

| Dimension | Method | Output |
|-----------|--------|--------|
| Volume | Mention count | Trend graph |
| Sentiment | NLP analysis | Sentiment score |
| Sources | Platform breakdown | Source distribution |
| Keywords | Topic extraction | Word cloud |
| Competitors | Share of voice | Comparison chart |

## Data Source (read first)

`scripts/monitor.py` **does not fetch live data** (the collectors in `scripts/scrapers.py` are not connected). It analyzes the mentions you give it: sentiment, platform split, engagement, influential posts and crisis keywords.

1. Collect real mentions first: web search for the brand name, Reddit and news searches, social and review exports.
2. Pass them as JSON:

```bash
python3 scripts/monitor.py '{"brand": "Acme", "mentions": [{"content": "Acme bottle leaked in my bag, very disappointed", "platform": "reddit", "url": "https://reddit.com/r/example", "date": "2026-11-20T10:00:00", "engagement": 42}, {"content": "Love my Acme bottle, keeps water cold all day", "platform": "news", "date": "2026-11-21T09:00:00", "engagement": 5}]}'
```

3. Without `mentions`, the script prints a **demo report labelled DEMO DATA**: never present it as real monitoring results.

## Usage

### Basic Monitoring

```bash
python3 scripts/monitor.py "YourBrand"
```

### With Competitors

```bash
python3 scripts/monitor.py '{
  "brand": "YourBrand",
  "competitors": ["CompA", "CompB"],
  "platforms": ["reddit", "google_news"]
}'
```

### Demo Mode

```bash
python3 scripts/monitor.py --demo
```

## Output Example

```
📡 Brand Monitoring Report

Brand: YourBrand
Period: Last 7 days
Platforms: Reddit, Google News, YouTube

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 MENTION OVERVIEW

Total Mentions: 127
├── Reddit: 82 (65%)
├── Google News: 35 (28%)
└── YouTube: 10 (8%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😊 SENTIMENT ANALYSIS

Positive: 45% ████████░░
Neutral:  38% ███████░░░
Negative: 17% ███░░░░░░░

Overall Score: 7.2/10 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 TREND (7 days)

Mon ████████ 25
Tue ██████ 18
Wed ███████ 21
Thu █████████ 28
Fri ████████ 22
Sat ███ 8
Sun ██ 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 TRENDING KEYWORDS

1. quality (32x)
2. shipping (28x)
3. customer service (22x)
4. price (18x)
5. recommended (15x)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ ALERTS

🔴 Negative spike on Thursday (+40%)
   Related to: shipping delays
   Recommendation: Monitor and respond
```

## Crisis Detection

| Alert Level | Trigger | Action |
|-------------|---------|--------|
| 🟢 Normal | < 20% negative | Continue monitoring |
| 🟡 Warning | 20-40% negative | Investigate sources |
| 🔴 Crisis | > 40% negative | Immediate response needed |

## Monitoring Workflow

```
Set up brand keywords
      ↓
Monitor platforms
      ↓
Analyze sentiment
      ↓
Detect anomalies
      ↓
Generate alerts
      ↓
Weekly report
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

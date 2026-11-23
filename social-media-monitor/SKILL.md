---
name: social-media-monitor
description: "Monitor social media mentions, trends, and competitor activity for e-commerce brands. Set up listening workflows across Reddit, TikTok, Instagram, Twitter/X, and YouTube. Use when a brand wants to track social mentions, trends or competitor activity on social networks (for broader brand monitoring with sentiment and crisis alerts use `brand-monitoring`)."
metadata:
  nexscope:
    emoji: "📱"
    category: ecommerce
---

# Social Media Monitor 📱

Monitor social media mentions, trends, and competitor activity for e-commerce brands. Set up listening workflows across Reddit, TikTok, Instagram, Twitter/X, and YouTube.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Social listening on social networks: mentions, trends and competitor activity.

Part of: Brand and social listening. For neighbouring jobs, use the matching skill instead:

- `brand-monitoring` — Tracking brand mentions across Reddit, news, YouTube and the web with sentiment and crisis alerts (script).

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill social-media-monitor -g
```

## Usage

```
Set up social media monitoring for my skincare brand. I want to track mentions on TikTok, Instagram, and Reddit. Also monitor 3 competitors.
```

## Capabilities

- Social listening keyword and hashtag setup
- Platform-specific monitoring strategy (Reddit, TikTok, Instagram, Twitter, YouTube)
- Sentiment tracking methodology
- Competitor social media activity tracking
- Influencer mention detection
- Crisis detection and response framework
- UGC (user-generated content) discovery for marketing

## Principles and Constraints

Social listening rules, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with each platform or tool.

- **Data access is limited by platform APIs:** X (Twitter) API access is paid and tiered **[check]**; Reddit restricted free API access in 2023 **[check]**; Instagram exposes hashtags and mentions of business accounts but not all public posts; TikTok offers research and business APIs under conditions **[check]**. Listening tools (examples: Brandwatch, Talkwalker, Sprout Social, Brand24, Mention) work within these limits, so coverage is never complete: state it.
- **Respect terms and privacy:** use official APIs and licensed tools; do not scrape behind logins or store personal data beyond what you need; GDPR applies to EU users' personal data.
- **Automated sentiment is approximate:** sarcasm, slang and mixed opinions confuse classifiers; validate a sample by hand before reporting sentiment.
- **Engaging with posts:** reply from official accounts, disclose employee or agency affiliation, never astroturf.
- **Scope:** social networks only. Web, news and marketplace brand mentions are `brand-monitoring`; crisis and reputation response `online-reputation-management`; reviews `review-monitoring`.

## Data Needed

| Data | Where |
|------|-------|
| Brand names, product names, common misspellings, handles, hashtags | Brand team |
| Competitors and their handles/products | Market research |
| Category and problem keywords customers use | Reviews, search terms, community posts |
| Platforms where customers talk (by audience) | Analytics, surveys |
| Tool access and its coverage per platform | Listening tool documentation |
| Baseline volume and sentiment (8–12 weeks) | Tool history |

## Workflow

1. **Define goals:** brand health, crisis detection, competitor intelligence, UGC discovery, product feedback; each needs different queries and alerts.
2. **Build Boolean queries:** brand + misspellings, product names, handles; exclude noise (homonyms, job posts) with NOT terms; one query per goal.
3. **Choose platforms and tools** by where the audience talks and what the APIs allow; document coverage gaps.
4. **Set baselines** from 8–12 weeks of history: weekly mention volume, share of voice vs competitors, sentiment split (hand-validated sample).
5. **Set alerts:** volume spike (z-score), negative-sentiment share above baseline, crisis keywords (recall, unsafe, scam, lawsuit), high-reach accounts mentioning the brand.
6. **Route and respond:** customer issues to support, product feedback to product team, UGC to marketing (ask for rights before reuse), crises to the reputation owner.
7. **Report weekly:** volume, share of voice, sentiment, top themes and posts, competitor moves; monthly deeper themes.
8. **Tune queries monthly:** add new slang and product names, remove noise sources.

## Calculations and Tools

- **Share of voice** = brand mentions ÷ (brand + competitor mentions) in the same query scope and period.
- **Net sentiment** = (positive − negative) ÷ (positive + negative) mentions, after hand-validating a sample.
- **Classifier accuracy** = correctly labelled mentions ÷ mentions in a hand-checked sample of at least 100.
- **Spike z-score** = (today's mentions − mean of the last 28 days) ÷ standard deviation; |z| > 3 triggers an alert (working rule).
- **Engagement-weighted reach** = sum of engagements on posts mentioning the brand (to rank which posts matter).

## Worked Example

*Illustrative example with invented figures.* A skincare brand monitors TikTok, Instagram and Reddit, plus 3 competitors.

- Last 4 weeks: 1,240 brand mentions vs 3,100 for competitors → share of voice = 1,240 ÷ 4,340 = **28.6%**.
- Hand-check of 120 mentions: the tool labelled 87 correctly (72.5% accuracy); "sick" and "obsessed" were misread as negative → added to custom sentiment rules.
- Friday: 410 mentions vs a 28-day mean of 44 (sd 12) → z ≈ 30.5; cause: a creator's video about a rash after use → routed to the reputation owner and product safety within the hour.

## Example Requests

- "Set up social media monitoring for my skincare brand on TikTok, Instagram and Reddit, and track 3 competitors."
- "Build Boolean queries for our brand name, which is also a common word."
- "Our mentions jumped tenfold today. How do I find out why and who should respond?"

## Output Format

1. Goals, platforms, tools and coverage limits.
2. Query set (Boolean) with exclusions.
3. Baseline metrics and alert rules with thresholds and owners.
4. Weekly report template (volume, share of voice, sentiment, themes, top posts, competitor moves).
5. Response routing table.

## Quality Checks

- Coverage limits per platform stated in every report.
- Sentiment validated on a hand-checked sample; accuracy reported.
- Queries tested for noise before alerts go live.
- UGC reused only with the creator's permission.
- Alerts have owners and response times.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** mention counts and posts from the tool with query and date, hand-checked samples.
- **Estimates:** automated sentiment beyond the checked sample, reach figures modelled by tools, causes of spikes before investigation.
- API access rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

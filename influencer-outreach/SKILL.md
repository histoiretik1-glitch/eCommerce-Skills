---
name: influencer-outreach
description: "Find, contact, and manage influencer partnerships for e-commerce brands. Outreach templates, negotiation tactics, contract frameworks, and relationship management across Instagram, TikTok, YouTube, and more. Use when the user asks for help finding influencers, writing outreach messages, negotiating rates, drafting contracts or managing creator partnerships."
---

# Influencer Outreach

Find, contact, and manage influencer partnerships for e-commerce brands. Outreach templates, negotiation tactics, contract frameworks, and relationship management across Instagram, TikTok, YouTube, and more.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Finding, contacting and contracting influencers on any platform.

Part of: Influencers, Affiliate and creator partnerships. For neighbouring jobs, use the matching skill instead:

- `tiktok-influencer-marketing` — Overall creator and UGC strategy on TikTok: goals, creator mix, outreach and ROI.
- `affiliate-marketing-strategy` — Commission-based affiliate programmes: commission ceiling, terms, networks, incrementality.
- `tiktok-shop-affiliate-program` — Setting up the TikTok Shop affiliate program: open and targeted collaborations, commission rates, samples.

<!-- role-and-scope:end -->

## Capabilities

- Influencer discovery by platform, niche, and audience demographics
- Outreach email and DM templates (cold and warm)
- Rate negotiation frameworks and pricing benchmarks
- Campaign brief creation and content guidelines
- Contract templates covering usage rights and deliverables
- Performance tracking and reporting
- Long-term ambassador program design
- Micro-influencer vs macro-influencer strategy

## Principles and Constraints

Rules for paid and gifted creator partnerships on any platform, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with each platform or counsel.

- **Disclosure:** creators must disclose paid or gifted content clearly (FTC Endorsement Guides in the US; ASA/CAP and CMA in the UK; national rules in the EU). Use the platform's paid-partnership label as well as a clear "#ad". The brand is responsible for briefing and checking it.
- **Rights are separate from the post:** organic posting does not give you the right to reuse the video in ads; negotiate usage rights (channels, duration, territories) and whitelisting/partnership ads access (Meta partnership ads, TikTok Spark Ads) explicitly, with an end date.
- **Contracts:** deliverables, dates, approval rounds, claims the creator may and may not make, disclosure duty, exclusivity (category and duration), payment terms, cancellation, content ownership and takedown.
- **Product claims** made by creators are your claims: no health or performance claims you cannot substantiate.
- **Vetting:** check audience location and authenticity (sudden follower spikes, engagement concentrated on a few posts, generic comments).
- **Scope:** this skill finds, contacts and contracts creators on any platform. Choosing TikTok collaboration models is `tiktok-influencer-marketing`; TikTok Creator Marketplace campaigns `tiktok-creator-marketplace`; commission-only partners `affiliate-marketing-strategy`.

## Data Needed

| Data | Where |
|------|-------|
| Campaign goal (awareness, content for ads, sales), budget, timing | Marketing plan |
| Target audience: country, age, interests | Customer data |
| Creator shortlist: platform, followers, average views of the last 10–20 posts, engagement, audience demographics | Creator profiles, media kits, creator tools |
| Past creator results: views, clicks, codes used, sales, content reused in ads | Tracking links, discount codes, ad accounts |
| Product margin and AOV | Finance |

## Workflow

1. **Set the goal and the success metric:** cost per 1,000 views, cost per acquisition, or cost per usable ad asset; this decides the creator tier and the deal type.
2. **Build a long list** (3× the number you need): hashtags and keywords, competitors' tagged posts, creators already mentioning you, creator marketplaces.
3. **Vet each creator:** average views (not followers), engagement rate on recent posts, audience country and age split (ask for screenshots), brand safety, past sponsored content performance.
4. **Price the deal** from expected views (CPM) and the rights requested; gifted-only for micro creators who opt in, fee + commission for proven sellers.
5. **Send personalised outreach:** why them (a specific post), what you offer, the deliverable, the rights, the budget range; follow up twice at most.
6. **Brief and contract:** product facts, must-say and must-not-say lists, disclosure, timeline, approval round, usage rights and whitelisting terms.
7. **Track every creator** with a unique link and code; collect views, clicks, sales; record content you can reuse.
8. **Review and keep the best:** rank by the success metric, propose ambassador terms (monthly retainer, higher commission) to the top performers.

## Calculations and Tools

- **Engagement rate (by views)** = (likes + comments + shares) ÷ average views of recent posts; by followers only as a secondary view.
- **Effective CPM** = fee ÷ expected views × 1,000, where expected views = median views of the last 10–20 posts.
- **CPA** = (fee + product cost + shipping + commission) ÷ attributed orders; compare with paid social CPA.
- **Maximum fee for a sales goal** = expected orders × (contribution per order − target CPA margin).
- **Rights premium**: price usage rights as an addition (e.g. a share of the fee per month of paid usage), stated in the contract.

## Worked Example

*Illustrative example with invented figures.* A supplement brand considers a fitness creator with 50,000 followers whose last 15 videos have a median of 18,000 views; quote $600 for one video plus 30 days of Spark Ads rights.

- Effective CPM = 600 ÷ 18,000 × 1,000 = **$33.33**; the brand's paid TikTok CPM is around $9, so the organic post alone is expensive.
- The deal makes sense only for the reusable asset: if the video runs as a Spark Ad and replaces $1,000 of creative production, value = rights + organic reach.
- Counter-offer: $450 + 10% commission on code sales + 30 days of ad rights; success metric: CPA of the Spark Ad vs current best creative.

## Example Requests

- "Write outreach emails to 10 fitness influencers for my supplement brand."
- "What should I pay a TikTok creator with 50,000 followers whose videos get about 18,000 views?"
- "Create a contract template for influencer partnerships with usage rights and disclosure."

## Output Format

1. Goal, metric and budget split by creator tier.
2. Vetted shortlist table: creator, platform, median views, engagement, audience fit, price, effective CPM, rights.
3. Outreach messages (first contact and follow-up) personalised per creator.
4. Brief and contract checklist.
5. Tracking plan and results scorecard (views, clicks, codes, sales, CPA, reusable assets).

## Quality Checks

- Pricing based on median recent views, not follower count.
- Audience location and authenticity checked before contracting.
- Contracts state disclosure, rights, duration and approval process.
- Every creator has a unique link/code; results compared with paid channels on the same metric.
- No unsubstantiated product claims in briefs.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** creator metrics from screenshots or platform tools with date, tracked results of past campaigns.
- **Estimates:** expected views and sales, market rate ranges, value of reusable content.
- Disclosure and platform rules were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill influencer-outreach -g
```

## Usage

Ask your AI agent:

- "Write outreach emails for 10 fitness influencers for my supplement brand."
- "What should I pay a TikTok creator with 50K followers?"
- "Create a contract template for influencer partnerships."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

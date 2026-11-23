---
name: tiktok-live-selling
description: "Master TikTok live selling for e-commerce. Plan live sessions, engage audiences, pin products, handle real-time sales, and optimize GPM (GMV per mille) for maximum live revenue. Use when the user asks for help planning or improving TikTok Shop LIVE sessions, scripts, product pinning, engagement or GPM."
---

# TikTok Live Selling

Master TikTok live selling for e-commerce. Plan live sessions, engage audiences, pin products, handle real-time sales, and optimize GPM (GMV per mille) for maximum live revenue.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Planning and running TikTok Shop LIVE sessions.

Part of: TikTok content, brand and LIVE, Video commerce. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-content-strategy` — Short-video content plan for TikTok Shop: formats, hooks, calendar.
- `tiktok-shop-branding` — Building a recognizable brand on TikTok: identity, content pillars, community.
- `tiktok-shop-ads` — Paid TikTok Shop ads (Product, Video and LIVE Shopping Ads).
- `ecommerce-video-marketing` — Overall video marketing strategy across channels.
- `shoppable-video` — Shoppable and live-shopping video with product tagging on several platforms.

<!-- role-and-scope:end -->

## Capabilities

- Live selling session planning and scheduling
- Equipment and setup requirements
- Audience engagement techniques during live streams
- Product pinning and showcase management
- Real-time sales tactics: flash deals, bundles, giveaways
- GPM optimization and benchmarking
- Multi-host and guest collaboration strategy
- Post-live analytics and iteration

## Platform Rules and Constraints

TikTok Shop LIVE rules at the last review of this skill (November 2026), from TikTok Shop Seller Center / Seller University and TikTok's LIVE and Community Guidelines. They differ by country; items marked **[check]** must be confirmed in Seller University for the seller's market.

- **Who can sell in LIVE:** the shop's official account and linked accounts, and affiliate creators who meet TikTok Shop's requirements (in the US at last review: 18+ and at least 1,000 followers for creators **[check]**). Accounts with LIVE restrictions or policy violations lose access.
- **Products** must be listed and approved in the shop and added to the LIVE showcase before the session; pin the product being presented so viewers can buy from the pinned card.
- **LIVE-only promotions:** flash deals and LIVE-exclusive discounts are created in Seller Center (Promotions) for a time window **[check]**; the displayed price must be the price charged.
- **Content rules:** no misleading claims, no fake countdowns or fake "only 2 left", no directing buyers to pay off TikTok, no prohibited or restricted products, follow the Community Guidelines (e.g. minors on camera, dangerous demonstrations). Repeated violations lead to LIVE bans and shop penalties.
- **Shipping commitments still apply:** orders taken in LIVE must ship within the shop's handling time; late dispatch affects the Shop Performance Score.
- **Metrics:** LIVE analytics (LIVE dashboard / LIVE Manager in Seller Center) report views, viewers, average viewing duration, product impressions and clicks, orders, GMV and GPM **[check: names per market]**.
- **Paid traffic** for LIVE (LIVE Shopping Ads / GMV Max for LIVE) is covered by `tiktok-shop-ads`.

## Data Needed

| Data | Where |
|------|-------|
| Per-session metrics: date, start time, duration, views, viewers, average viewing duration, product impressions, product clicks, orders, GMV, new followers, comments | Seller Center > Analytics > LIVE (or LIVE Manager), exported per session |
| Products to feature, price, margin, stock | Seller Center product list, `profit-margin-calculator-tiktok` |
| Promotions planned (flash deals, vouchers) | Seller Center > Promotions |
| Host availability, equipment, set | Team schedule |
| Audience active hours | TikTok analytics > Followers (activity by hour) |

## Workflow

1. **Set the goal and product line-up:** 1 hero product (best margin and demand), 3–6 supporting products, 1 add-on for bundles; check stock covers the forecast (orders per hour × duration).
2. **Prepare promotions** in Seller Center (flash deal windows, LIVE-exclusive vouchers) and verify the prices displayed.
3. **Script the run of show** in 15–20 minute loops: hook and offer (1 min), demonstration and proof (5–8 min), objections and Q&A (3–5 min), call to action with the pinned product (1–2 min), repeat for the next product; new viewers arrive throughout, so repeat the offer every loop.
4. **Set up the technical side:** stable connection (wired or strong Wi-Fi), lighting on the product, external microphone, phone on a tripod at eye level, products within reach, a moderator to pin products and answer comments.
5. **Schedule** at the hours when followers are active; announce the LIVE with 1–3 short videos and a LIVE event the day before.
6. **Run the session:** pin each product while presenting it, reply to comments by name, show the product in use, state stock and price truthfully, use the flash deal at a planned moment.
7. **After the session:** export the metrics and run `live_metrics.py` across sessions; clip the best moments into short videos.
8. **Iterate weekly:** change one variable at a time (start time, duration, hero product, offer, host) and compare GPM and click-to-order with the median of past sessions.

## Calculations and Tools

- **GPM** (GMV per mille) = GMV ÷ views × 1,000.
- **GMV per hour** = GMV ÷ duration in hours.
- **Product CTR** = product clicks ÷ product impressions; **click-to-order** = orders ÷ product clicks.
- **Orders per 1,000 views** = orders ÷ views × 1,000; **AOV** = GMV ÷ orders.
- **Stock check**: units needed ≈ expected orders per hour × hours × units per order × 1.2 safety factor (heuristic).
- **Contribution per session** = GMV × margin after fees − promotion cost − host cost.

```bash
python3 scripts/live_metrics.py '{"sessions": [{"date": "2026-11-18", "start_hour": 19, "duration_min": 120, "views": 15400, "avg_view_seconds": 48, "product_impressions": 9800, "product_clicks": 610, "orders": 92, "gmv": 2760.0, "new_followers": 140, "comments": 830}, {"date": "2026-11-20", "start_hour": 13, "duration_min": 90, "views": 6100, "product_impressions": 3900, "product_clicks": 180, "orders": 21, "gmv": 588.0, "new_followers": 35, "comments": 210}]}'
```

## Worked Example

*Illustrative example with invented figures.* Two sessions: an evening session (19h, 120 min) with 15,400 views and $2,760 GMV, and a lunchtime session (13h, 90 min) with 6,100 views and $588 GMV.

- Evening: GPM = 2,760 ÷ 15,400 × 1,000 = **$179.22**, GMV per hour $1,380, product CTR 6.2%, click-to-order 15.1%.
- Lunchtime: GPM **$96.39**, GMV per hour $392, product CTR 4.6%, click-to-order 11.7%.
- Decision: keep evening slots; test a lunchtime session with the evening's hero product before dropping the slot (one variable at a time).

## Example Requests

- "Plan my first 2-hour TikTok Shop LIVE for a skincare brand: product line-up, run of show, flash deal timing and team roles."
- "Here are the metrics of my last 6 TikTok LIVE sessions. Which start time and duration give the best GPM?"
- "My LIVE gets views but few product clicks. What should I change in the script and product pinning?"

## Output Format

1. Session plan: goal, products (hero, supporting, add-on), promotions with time windows, stock check.
2. Run of show in timed loops with talking points and pin moments.
3. Team and equipment checklist.
4. Post-LIVE table per session (from the script) with medians and the best/worst sessions.
5. Next test: the single variable to change and the success metric.

## Quality Checks

- Every promoted price exists in Seller Center for the stated window; no fake scarcity or countdowns.
- Products in the showcase are approved and in stock for the forecast.
- Sessions compared on GPM and click-to-order, not on views alone.
- At least 3 sessions per variant before concluding on a start time or format.
- Script and claims comply with TikTok Shop's LIVE policies for the seller's country.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** session metrics exported from the seller's LIVE analytics for stated dates.
- **Estimates:** expected orders per hour, stock needs, category GPM benchmarks, effect of a new start time.
- LIVE eligibility and promotion rules were reviewed in November 2026 and vary by country; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-live-selling -g
```

## Usage

Ask your AI agent:

- "Plan my first TikTok live selling session."
- "How do I increase engagement and sales during TikTok lives?"
- "What GPM should I target for my product category?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*

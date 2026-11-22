"""Heuristic check that skill descriptions are distinctive enough to route typical requests.

Claude chooses skills with the model, not with this ranking. The test is a
regression guard: it ranks all descriptions against sample user requests with
TF-IDF and requires the intended skill in the top 3. A description edit that
makes a skill indistinguishable from its neighbours fails here.
"""
import math
import re
import unittest
from collections import Counter
from pathlib import Path

from helpers import ROOT

STOP = set("""a an and are as at be by can do for from has have how i in is it its my of on or our should
the their them this to use user wants what when where which who why will with you your asks ask help
seller sellers store stores shop shops ecommerce e commerce skill skills sell selling get make more""".split())

# (request, expected skill)
REQUESTS = [
    ("How do I become an Etsy Star Seller and keep the badge?", "etsy-star-seller"),
    ("Should I opt out of Etsy Offsite Ads fees?", "etsy-offsite-ads"),
    ("Which 13 tags should I use on my Etsy listing?", "etsy-seo-tags"),
    ("Price my handmade candles on Etsy so fees don't eat my profit", "etsy-pricing-strategy"),
    ("I want to sell printable planners as Etsy digital downloads", "etsy-digital-products"),
    ("Set up Printify print on demand for my Etsy shop", "etsy-print-on-demand"),
    ("Holiday Christmas seasonal calendar for my Etsy shop", "etsy-seasonal-strategy"),
    ("Configure sales tax and VAT in Shopify", "shopify-tax-compliance"),
    ("Move my store from WooCommerce to Shopify without losing SEO redirects", "shopify-migration"),
    ("Set up wholesale B2B price lists on Shopify", "shopify-wholesale-channel"),
    ("Recover abandoned checkouts on my Shopify store with emails and SMS", "shopify-cart-abandonment"),
    ("Which Shopify apps should I install and which slow my store?", "shopify-app-recommendations"),
    ("Sell in Europe with Shopify Markets multi-currency and translations", "shopify-international"),
    ("Set up a loyalty points and VIP tiers program on Shopify", "shopify-loyalty-program"),
    ("Connect Shopify to Google Merchant Center and fix feed errors", "shopify-google-channel"),
    ("Sync my Shopify catalog to Facebook Shop and Instagram Shopping", "shopify-facebook-instagram-shop"),
    ("What price should I charge on TikTok Shop with creator commission?", "tiktok-shop-pricing"),
    ("Plan Flash Deals and vouchers for a TikTok Shop campaign", "tiktok-shop-promotions"),
    ("My TikTok Shop video was removed for a policy violation, can I appeal?", "tiktok-shop-compliance"),
    ("Should I use Fulfilled by TikTok FBT or ship myself?", "tiktok-shop-fulfillment"),
    ("How much stock should I order before a viral TikTok video?", "tiktok-shop-inventory"),
    ("TikTok Shop return rate is too high, how do I handle refund requests?", "tiktok-shop-returns"),
    ("What is trending on TikTok Shop right now?", "tiktok-shop-trending-products"),
    ("Respond faster to TikTok Shop buyer messages with templates", "tiktok-shop-customer-service"),
    ("Tier my TikTok Shop creators, track samples and write a creator brief", "tiktok-shop-creator-management"),
    ("Is this TikTok Shop product profitable after referral fee and affiliate commission?", "profit-margin-calculator-tiktok"),
    ("Calculate my Amazon FBA profit margin and break-even price", "profit-margin-calculator-amazon"),
    ("Shopify Payments fees and max affordable CAC for my DTC product", "profit-margin-calculator-shopify"),
    ("Walmart WFS fees and referral fee profit calculation", "profit-margin-calculator-walmart"),
    ("Report a counterfeit seller to eBay VeRO", "brand-protection-ebay"),
    ("Report infringement in Walmart Brand Portal", "brand-protection-walmart"),
    ("Are the reviews on this Walmart product fake?", "walmart-review-checker"),
    ("Improve my Walmart listing quality score", "walmart-listing-optimization"),
    ("Cassini eBay search ranking for my listings", "ebay-seo"),
    ("Which country should I expand to, and what about VAT IOSS?", "cross-border-ecommerce"),
    ("Build a 90-day growth roadmap with unit economics", "ecommerce-growth-strategy"),
    ("Monitor competitor prices and alert me on price drops", "competitor-price-tracker"),
    ("Compare UPS FedEx USPS shipping rates and free shipping threshold", "ecommerce-shipping-rates"),
    ("Write a business plan with financial projections for my online store", "ecommerce-business-plan"),
    ("Track brand mentions on Reddit and news with sentiment alerts", "brand-monitoring"),
    ("Find an underserved niche competitors miss", "market-gap-analysis"),
    ("Google Shopping Performance Max ROAS bidding strategy", "google-shopping-optimization"),
    ("Set up abandoned cart and welcome email flows in Klaviyo for Shopify", "shopify-email-flows"),
    ("Monitor my store's SSL certificate expiry and DNS", "domain-monitoring"),
]


def tokens(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 1 and w not in STOP]


def load_descriptions():
    out = {}
    for skill_md in ROOT.rglob("SKILL.md"):
        if "node_modules" in skill_md.parts:
            continue
        text = skill_md.read_text(encoding="utf-8")
        m = re.search(r"^description: (.*)$", text, re.M)
        name = skill_md.parent.name
        out[name] = tokens(m.group(1)) + tokens(name.replace("-", " ")) * 2
    return out


class DescriptionRouting(unittest.TestCase):
    def test_requests_rank_intended_skill_in_top_3(self):
        docs = load_descriptions()
        self.assertEqual(len(docs), 162)
        df = Counter(w for d in docs.values() for w in set(d))
        n = len(docs)
        idf = {w: math.log(n / c) for w, c in df.items()}
        vectors = {}
        for name, toks in docs.items():
            tf = Counter(toks)
            vec = {w: c * idf[w] for w, c in tf.items()}
            norm = math.sqrt(sum(v * v for v in vec.values()))
            vectors[name] = {w: v / norm for w, v in vec.items()}
        misses = []
        for request, expected in REQUESTS:
            self.assertIn(expected, docs, expected)
            q = Counter(t for t in tokens(request) if t in idf)
            ranked = sorted(vectors, key=lambda s: -sum(q[w] * idf[w] * vectors[s].get(w, 0) for w in q))
            if expected not in ranked[:3]:
                misses.append(f"{request!r}: expected {expected}, got {ranked[:3]}")
        self.assertEqual(misses, [], "\n".join(misses))


if __name__ == "__main__":
    unittest.main()

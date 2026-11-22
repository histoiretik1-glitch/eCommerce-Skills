#!/usr/bin/env python3
"""
Walmart price tracker - price position against competing offers and price changes over time.

Input (prices the seller collected from Walmart.com / Seller Center; landed = price + shipping):
  {"items": [{"item_id": "123", "name": "Storage bins 3-pack", "my_price": 24.99, "my_shipping": 0,
              "competitors": [{"seller": "A", "price": 23.49, "shipping": 0}, ...],
              "history": [{"date": "2026-11-01", "price": 25.99}, {"date": "2026-11-15", "price": 24.99}]}],
   "band": [97, 103]}     # price index band considered "at market" (policy choice), default 97-103

Metrics per item:
  my_landed, lowest_landed, median_landed (competitors)
  index_vs_lowest = my_landed / lowest_landed * 100      (100 = same as the cheapest offer)
  index_vs_median = my_landed / median_landed * 100
  rank            = position of my landed price among all offers (1 = cheapest)
  position        = below / at / above market according to the band on index_vs_median
  price changes   = changes in "history" with % and date of the last change

Walmart does not publish an exact Buy Box formula; price including shipping is one factor
among others (e.g. shipping speed, seller performance). Treat recommendations as hypotheses to test.

Usage:
  python3 scripts/price_index.py
  python3 scripts/price_index.py '<json>'
  python3 scripts/price_index.py '<json>' --json
Standard library only.
"""
import json
import statistics
import sys

DEMO = {"items": [
    {"item_id": "559912345", "name": "Storage bins 3-pack", "my_price": 24.99, "my_shipping": 0,
     "competitors": [{"seller": "BinsCo", "price": 23.49, "shipping": 0},
                     {"seller": "HomeGoods", "price": 22.99, "shipping": 2.99},
                     {"seller": "ValueMart", "price": 26.50, "shipping": 0}],
     "history": [{"date": "2026-11-01", "price": 26.99}, {"date": "2026-11-10", "price": 25.99},
                 {"date": "2026-11-18", "price": 24.99}]},
    {"item_id": "559998765", "name": "Drawer organizer", "my_price": 14.99, "my_shipping": 0,
     "competitors": [{"seller": "OrgPro", "price": 16.99, "shipping": 0},
                     {"seller": "TidyUp", "price": 15.49, "shipping": 0}]},
]}


def analyze_item(item, band):
    if "item_id" not in item or "my_price" not in item:
        raise ValueError(f"item needs item_id and my_price: {item}")
    mine = float(item["my_price"]) + float(item.get("my_shipping", 0))
    comps = [float(c["price"]) + float(c.get("shipping", 0)) for c in item.get("competitors", [])]
    res = {"item_id": item["item_id"], "name": item.get("name", ""), "my_landed": round(mine, 2),
           "offers": len(comps) + 1}
    if comps:
        lowest, median = min(comps), statistics.median(comps)
        idx_med = mine / median * 100
        res.update({
            "lowest_landed": round(lowest, 2), "median_landed": round(median, 2),
            "index_vs_lowest": round(mine / lowest * 100, 1), "index_vs_median": round(idx_med, 1),
            "rank": sorted(comps + [mine]).index(mine) + 1,
            "gap_to_lowest": round(mine - lowest, 2),
            "position": "below market" if idx_med < band[0] else "above market" if idx_med > band[1] else "at market",
        })
    else:
        res["position"] = "no competing offer collected"
    hist = sorted(item.get("history", []), key=lambda h: h["date"])
    changes = []
    for prev, cur in zip(hist, hist[1:]):
        if float(cur["price"]) != float(prev["price"]):
            changes.append({"date": cur["date"], "from": float(prev["price"]), "to": float(cur["price"]),
                            "change_pct": round((float(cur["price"]) - float(prev["price"])) / float(prev["price"]) * 100, 1)})
    res["price_changes"] = changes
    return res


def analyze(data):
    band = data.get("band", [97, 103])
    return [analyze_item(i, band) for i in data["items"]]


def format_report(rows):
    out = ["| Item | My landed | Lowest | Median | Index vs lowest | Index vs median | Rank | Position | Last change |",
           "|------|-----------|--------|--------|-----------------|-----------------|------|----------|-------------|"]
    for r in rows:
        last = r["price_changes"][-1] if r["price_changes"] else None
        last_txt = f"{last['date']} {last['change_pct']:+.1f}%" if last else "-"
        out.append(f"| {r['name'] or r['item_id']} | ${r['my_landed']:.2f} | ${r.get('lowest_landed', 0):.2f} | "
                   f"${r.get('median_landed', 0):.2f} | {r.get('index_vs_lowest', '-')} | {r.get('index_vs_median', '-')} | "
                   f"{r.get('rank', '-')}/{r['offers']} | {r['position']} | {last_txt} |")
    out.append("\nPrices are as collected (verified for that date); Walmart's Buy Box logic is not published, "
               "so price moves are hypotheses to test, not guarantees.")
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    try:
        rows = analyze(json.loads(args[0]) if args else DEMO)
    except (ValueError, KeyError, TypeError, ZeroDivisionError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(json.dumps(rows, indent=2) if "--json" in sys.argv else format_report(rows))


if __name__ == "__main__":
    main()

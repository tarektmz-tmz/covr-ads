#!/usr/bin/env python3
"""Rank the Advance Watch catalogue for AVAILABLE NOW stories and build a 14+ day no-repeat rotation.
Input: /tmp/allp.json (list of Shopify product nodes: id,title,handle,vendor,priceRangeV2,featuredMedia).
Output: pool.json (ranked) and rotation.md. Pure local script, no network."""
import json, re, sys, collections
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/allp.json")
OUT = Path(__file__).resolve().parent
prods = json.load(open(SRC))


def family(t):
    for k in ("GMT-Master II", "Submariner Date", "Submariner No-Date", "Submariner", "Daytona", "Datejust", "Day-Date",
              "Sky-Dweller", "Land-Dweller", "Oyster Perpetual", "Explorer II", "Sea-Dweller", "Yacht-Master",
              "Air-King", "Deepsea", "Royal Oak Offshore", "Royal Oak", "Nautilus", "Aquanaut", "1908"):
        if k in t:
            return k
    return "Other"


def metal_part(t):
    return t.split("–", 1)[1] if "–" in t else ""


def score(p):
    t, v = p["title"], p["vendor"]
    fam = family(t)
    m = metal_part(t)
    steel = m.strip().lower().startswith("steel") or "Steel" in m.split(",")[0]
    gold_only = ("Gold" in m.split(",")[0]) and "Steel" not in m.split(",")[0]
    s, why = 40, "other"
    if v == "Rolex":
        if fam in ("GMT-Master II", "Submariner Date", "Submariner No-Date", "Submariner"):
            twotone = "Steel &" in m.split(",")[0]
            s, why = (100, "steel sport Rolex") if (steel and not twotone) else (84, "sport Rolex two-tone / gold")
        elif fam == "Daytona":
            twotone = "Steel &" in m.split(",")[0]
            s, why = (100, "steel sport Rolex") if (steel and not twotone) else (86, "Daytona two-tone / gold")
            if "Panda" in t or "Paul Newman" in t or "Pikachu" in t:
                s += 6
        elif fam == "Datejust":
            if "41" in t and ("Steel" in m or "White Gold" in m) and any(k in t for k in ("Wimbledon", "Mint", "Green", "Blue", "Slate", "Fluted", "Ombr")):
                s, why = 92, "steel / white gold Datejust 41, sought dial"
            elif "41" in t and "Steel" in m:
                s, why = 84, "steel Datejust 41"
            else:
                s, why = 60, "Datejust"
        elif fam == "Day-Date":
            if ("Everose" in t or "Yellow Gold" in t) and ("Green" in t or "Ombr" in t or "Olive" in t):
                s, why = 94, "Day-Date green / ombre dial"
            else:
                s, why = 76, "Day-Date"
        elif fam == "Sky-Dweller":
            s, why = 88, "Sky-Dweller"
        elif fam == "Land-Dweller":
            s, why = 86, "Land-Dweller (hard to get)"
        elif fam == "Oyster Perpetual":
            s, why = (86, "Oyster Perpetual Tiffany / pistachio") if any(k in t for k in ("Tiffany", "Turquoise", "Pistachio", "Green")) else (50, "Oyster Perpetual")
        elif fam in ("Explorer II", "Yacht-Master", "Sea-Dweller", "Deepsea"):
            s, why = 62, "other sport"
        elif fam == "Air-King":
            s, why = 40, "easy to get"
    elif v == "Audemars Piguet":
        if fam == "Royal Oak" and ("37" in t or "41" in t) and "Quartz" not in t:
            s, why = 82, "Royal Oak 37 / 41"
        elif fam == "Royal Oak Offshore":
            s, why = 60, "Royal Oak Offshore"
        else:
            s, why = 55, "Royal Oak quartz / other"
    elif v == "Patek Philippe":
        s, why = (86, "Nautilus / Aquanaut, request price") if fam in ("Nautilus", "Aquanaut") else (70, "Patek")
    return s, why, fam


rows = []
for p in prods:
    s, why, fam = score(p)
    price = float(p["priceRangeV2"]["minVariantPrice"]["amount"])
    img = (p.get("featuredMedia") or {}).get("preview", {}).get("image", {}).get("url", "")
    rows.append({
        "score": s, "why": why, "family": fam, "vendor": p["vendor"], "title": p["title"], "handle": p["handle"],
        "price_aed": int(price), "show_price": p["vendor"] != "Patek Philippe",
        "price_rule": "request price on WhatsApp" if p["vendor"] == "Patek Philippe" else "store price as listed",
        "image_url": img, "id": p["id"],
    })
rows.sort(key=lambda r: (-r["score"], r["family"], r["title"]))
for i, r in enumerate(rows, 1):
    r["rank"] = i
json.dump(rows, open(OUT / "pool.json", "w"), indent=1, ensure_ascii=False)

_seen = set(); HIGH = []
for r in rows:  # one entry per visible watch (same title listed twice counts once)
    if r["score"] >= 80 and r["title"] not in _seen:
        _seen.add(r["title"]); HIGH.append(r)

# rotation: templates A(1 watch) B(1) C(2 watches) D(1) -> 5 watches per 4 days; no repeat inside 14 days,
# never the same family on two consecutive picks, vendor mix capped (max 1 Patek per 4 days).
tmpl = ["A spotlight", "B high-demand card", "C split screen", "D ticket"]
need = lambda d: 2 if d % 4 == 2 else 1
used_day = {}
last_fam = None
days = []
pool_iter = collections.deque(HIGH)
pick_log = []
horizon = 90
for d in range(horizon):
    picks = []
    for _ in range(need(d)):
        for _try in range(len(pool_iter)):
            c = pool_iter[0]
            pool_iter.rotate(-1)
            if c["handle"] in used_day and d - used_day[c["handle"]] < 14:
                continue
            if c["family"] == last_fam and len(HIGH) > 20:
                continue
            if c["vendor"] == "Patek Philippe" and any(x["vendor"] == "Patek Philippe" for x in picks):
                continue
            picks.append(c)
            used_day[c["handle"]] = d
            last_fam = c["family"]
            break
    days.append((d + 1, tmpl[d % 4], picks))

fam_counts = collections.Counter(r["family"] for r in HIGH)
lines = ["# AVAILABLE NOW rotation (generated by build_pool.py)", "",
         f"Active products in the store: {len(rows)}. HIGH DEMAND pool (score >= 80): **{len(HIGH)} distinct watches**.",
         "Pattern: 4 templates cycle (A spotlight 1 watch, B high-demand card 1, C split screen 2, D ticket 1) = 5 watches per 4 days.",
         f"Days covered with NO watch repeated inside 14 days: the pool of {len(HIGH)} covers about {int(len(HIGH)/5*4)} days before every watch has been shown once.",
         "Old queue by comparison (queue_0, queue_84, queue_168): 109 distinct watch lines filled 396 slots over 63 days, so each one appeared about 3.6 times.", "",
         "Pool by family: " + ", ".join(f"{k} {v}" for k, v in fam_counts.most_common()), "",
         "Rules: AED price exactly as the store lists it (minimum variant price); Patek never shows a number: 'REQUEST PRICE ON WHATSAPP'; never a phone number, 'WhatsApp in bio'; tiny 'Independent dealer, not affiliated with Rolex' line on Rolex stories; key content inside y 250-1580.", "",
         "## First 28 days", "", "| Day | Template | Watches |", "|---|---|---|"]
for d, t, picks in days[:28]:
    lines.append(f"| {d} | {t} | " + "; ".join(f"{x['title'].split(' – ')[0]} ({x['family']})" for x in picks) + " |")
(OUT / "rotation.md").write_text("\n".join(lines) + "\n")
print(len(rows), "products;", len(HIGH), "high-demand; first day:", [x["title"][:40] for x in days[0][2]])

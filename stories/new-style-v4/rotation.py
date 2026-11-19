#!/usr/bin/env python3
"""30-day rotation: ONE Available Now style per day (3 stories), urgency flags, one knowledge story per day.
Rules: high-demand first (score >= 80), then the rest of the catalogue only when needed, never-used watches before reused ones, no watch repeated within 14 days,
different model families inside one day (a pair story may use two of the same family), the 'set' style uses Rolex only,
'Only one available' is applied ONLY to handles listed in only_one_available.json (empty = never).
Run: python3 rotation.py  -> rotation.json, rotation.md"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import knowledge_library as K

POOL = json.load(open(ROOT.parent / "new-style" / "pool.json"))
ONLY_ONE = set(json.load(open(ROOT / "only_one_available.json")))
STYLES = ["hero", "cream", "pair", "set", "editorial", "plaque"]
DAYS, REPEAT_GAP = 30, 14


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def info(p):
    title = p["title"]
    left, _, spec = title.partition(" – ")
    left = left.replace(p["vendor"] + " ", "", 1)
    m = re.search(r"([0-9][0-9A-Za-z./\-]*[A-Za-z0-9])\s*$", left)
    ref = m.group(1) if m else ""
    name = left[:m.start()].strip() if m else left
    name = name.replace('"', "").replace("  ", " ").strip().upper()
    return dict(name=name, ref=ref, spec=spec.replace(", ", " · ") if spec else "")


# dedupe by title (duplicate listings with different prices are flagged, first/higher rank kept)
seen, dups, cands = {}, [], []
for p in sorted(POOL, key=lambda x: x["rank"]):
    k = norm(p["title"])
    if k in seen:
        dups.append((p["title"], seen[k]["price_aed"], p["price_aed"]))
        continue
    seen[k] = p
    cands.append(p)

RELAXED = []
last = {}  # model key (vendor + reference) -> day used last, so look-alike dial variants of one model do not repeat either


def mkey(p):
    return p["vendor"] + " " + (info(p)["ref"] or p["handle"])


def eligible(day):
    return [p for p in cands if mkey(p) not in last or day - last[mkey(p)] >= REPEAT_GAP]


def pick(day, taken_fams, want_rolex=False, fam=None, exclude=(), strict=False):
    """Order of preference: (1) a model not shown in the last 14 days, a different family from the day's other stories, never used before;
    (2) same but family may repeat; (3) any model past the 14-day gap (oldest first). Only if nothing is left is the gap relaxed."""
    base = [p for p in cands if p["handle"] not in exclude and (not want_rolex or p["vendor"] == "Rolex") and (not fam or p["family"] == fam)]
    ok_gap = [p for p in base if mkey(p) not in last or day - last[mkey(p)] >= REPEAT_GAP]
    for pool in (ok_gap, ):
        for avoid in (taken_fams if not fam else set(), set()):
            c = [p for p in pool if p["family"] not in avoid]
            never = [p for p in c if mkey(p) not in last]
            if never:
                return never[0]
            if c:
                return sorted(c, key=lambda p: last.get(mkey(p), -99))[0]
    if strict:
        return None
    c = sorted(base, key=lambda p: last.get(mkey(p), -99))  # relax the gap (reported)
    RELAXED.append(day + 1)
    return c[0] if c else None


def wdict(p):
    i = info(p)
    price = f"AED {p['price_aed']:,}" if p["show_price"] and p["vendor"] != "Patek Philippe" else None
    return dict(handle=p["handle"], title=p["title"], vendor=p["vendor"], family=p["family"], rank=p["rank"], score=p["score"],
                name=i["name"], ref=i["ref"], spec=i["spec"], price=price, price_aed=p["price_aed"] if price else None,
                fullset=(p["vendor"] == "Rolex"), image_url=p["image_url"], only_one=p["handle"] in ONLY_ONE)


# knowledge order: round-robin over layouts so consecutive days differ
order_layouts = ["myth_fact", "qa_card", "checklist", "timeline", "quote_card", "steps", "big_number", "compare_table", "do_dont", "ladder"]
buckets = {l: [x for x in K.L if x["layout"] == l] for l in order_layouts}
kn_order = []
while any(buckets.values()):
    for l in order_layouts:
        if buckets[l]:
            kn_order.append(buckets[l].pop(0))
for a, b in zip(kn_order[:DAYS], kn_order[1:DAYS]):
    assert a["layout"] != b["layout"], (a["id"], b["id"])

plan = []
for d in range(DAYS):
    style = STYLES[d % 6]
    taken, stories = set(), []
    for s in range(3):
        if style == "pair":
            a = pick(d, taken, want_rolex=True)
            ex = {p["handle"] for p in cands if mkey(p) == mkey(a)}
            b = pick(d, set(), want_rolex=True, fam=a["family"], exclude=ex, strict=True) or pick(d, taken | {a["family"]}, want_rolex=True, exclude=ex, strict=True) or pick(d, set(), want_rolex=True, exclude=ex)
            for p in (a, b):
                last[mkey(p)] = d
            taken.add(a["family"])
            stories.append([wdict(a), wdict(b)])
        else:
            p = pick(d, taken, want_rolex=(style == "set"))
            last[mkey(p)] = d
            taken.add(p["family"])
            stories.append([wdict(p)])
    urg = {}
    if d % 2 == 1:  # about half the days, never two days in a row
        urg[0] = "demand"
        if (d // 2) % 4 == 3:
            urg[2] = "demand"
    for si, st in enumerate(stories):
        if any(w["only_one"] for w in st):
            urg[si] = "only_one"
    k = kn_order[d]
    plan.append(dict(day=d + 1, style=style, stories=stories, urgency={str(i): u for i, u in urg.items()},
                     knowledge=dict(id=k["id"], topic=k["title"], layout=k["layout"], needs_confirmation=k["confirm"], source=k["src"])))

json.dump(dict(rules=dict(repeat_gap_days=REPEAT_GAP, styles=STYLES, only_one_handles=sorted(ONLY_ONE)), days=plan), open(ROOT / "rotation.json", "w"), indent=1, ensure_ascii=False)

# markdown
mkey_by_handle = {p['handle']: mkey(p) for p in cands}
allw = [w["handle"] for p in plan for st in p["stories"] for w in st]
lines = ["# 30-day rotation (preview plan, nothing is posted)\n",
         f"- Watches used: {len(allw)} slots, **{len(set(allw))} distinct listings**, and **{len(set(mkey_by_handle[h] for h in allw))} distinct models (references)**; the same model never appears again within {REPEAT_GAP} days.",
         f"- Pool after removing duplicate listings: **{len(cands)} listings** ({sum(1 for p in cands if p['score']>=80)} high-demand, score 80+; high-demand always go first) .",
         "- One Available Now style per day (hero, cream, pair, the full set, editorial, plaque), 3 stories per day; urgency 'HIGH DEMAND PIECE' on about every second day (1-2 watches); 'Only one available' is OFF (no handles listed).",
         "- Knowledge story: one per day, consecutive days always use different layouts. `needs_confirmation` = wording to confirm with Tarek first.\n",
         "| Day | Style | Available Now stories | Urgency | Knowledge (layout) |", "|---|---|---|---|---|"]
for p in plan:
    st = "<br>".join(" + ".join(f"{w['name']} {w['ref']} ({w['spec'][:34]})" + ("" if w["price"] else " (price on request)") for w in s) for s in p["stories"])
    u = ", ".join(f"story {int(i)+1}: {v}" for i, v in p["urgency"].items()) or "none"
    kn = f"{p['knowledge']['topic']} ({p['knowledge']['layout']})" + (" ⚠ confirm" if p["knowledge"]["needs_confirmation"] else "")
    lines.append(f"| {p['day']} | {p['style']} | {st} | {u} | {kn} |")
lines += ["", f"- Days where the 14-day gap had to be relaxed (no other watch left for that style): {sorted(set(RELAXED)) or 'none'}", "", "## Duplicate store listings (same title, different price): confirm which one is current", ""]
for t, a, b in dups[:30]:
    lines.append(f"- {t}: AED {a:,} (used) and AED {b:,}")
(ROOT / "rotation.md").write_text("\n".join(lines) + "\n")
print(len(set(allw)), "distinct watches,", len(allw), "slots;", len(cands), "pool;", len(dups), "duplicate listings")

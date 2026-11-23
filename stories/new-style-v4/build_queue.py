#!/usr/bin/env python3
"""Build the 30-day story queue (start 2026-11-20): Available Now days and Knowledge days alternate, 3 stories per day.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 build_queue.py   (needs network once to fetch cutouts; cached in assets/)
Outputs: queue/*.jpg, queue_v2.json, calendar.md (+ previews/sheet_*.jpg)."""
import json, re, subprocess, sys, datetime, collections
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_v4 as B
import knowledge_library_v2 as K2

ROOT = B.ROOT
Q = ROOT / "queue"
Q.mkdir(exist_ok=True)
START = datetime.date(2026, 11, 19)
DAYS = 30
EXCLUDE_REFS = set()  # listing 2 duplicates deleted from the store; listing 1 (brand new) kept
pool = json.load(open(ROOT.parent / "new-style" / "pool.json"))


def parse(x):
    t = x["title"].replace(x["vendor"] + " ", "", 1)
    left, _, right = t.partition(" – ")
    nick = re.search(r'"([^"]+)"', left)
    ref = re.search(r"(\d{4}[A-Z/0-9]*-\d{3}|\d{5,6}[A-Z]*)\s*$", left.replace(nick.group(0), "").strip() if nick else left)
    base = re.sub(r'"[^"]+"|\s*(\d{4}[A-Z/0-9]*-\d{3}|\d{5,6}[A-Z]*)\s*$', "", left).strip()
    base = re.sub(r"\s+", " ", base)
    parts = [p.strip().replace(" Dial", "") for p in right.split(",") if p.strip()]
    short = {"Submariner Date": "SUBMARINER", "Submariner No-Date": "SUB NO-DATE", "Oyster Perpetual 31": "OYSTER PERP. 31", "Oyster Perpetual 36": "OYSTER PERP. 36",
             "Oyster Perpetual 41": "OYSTER PERP. 41", "GMT-Master II": "GMT-MASTER II"}
    name = nick.group(1).upper() if nick else short.get(base, base.upper())
    if nick and x["family"] == "Daytona" and len(name) <= 5:
        name = "DAYTONA " + name
    if nick and x["family"] == "GMT-Master II":
        name = name + " GMT"
    parts = [{"Steel & Yellow Gold": "Yellow Rolesor", "Steel & White Gold": "White Rolesor", "Steel & Everose Gold": "Everose Rolesor"}.get(p, p) for p in parts]
    if x["vendor"] != "Rolex":
        name = base.replace("Patek Philippe ", "").upper()
        base = "Patek Philippe"
    spec = " · ".join(([base] if (nick or x["vendor"] != "Rolex") else []) + parts)
    while len(spec) > 28 and " · " in spec:
        spec = spec.rsplit(" · ", 1)[0]
    pretty_fam = {"Submariner Date": "SUBMARINER", "Oyster Perpetual": "OYSTER PERPETUAL"}.get(x["family"], x["family"].upper())
    return dict(name=name, ref=ref.group(1) if ref else "", spec=spec, vendor=x["vendor"], fullset=x["vendor"] == "Rolex",
                price=("AED {:,}".format(x["price_aed"]) if x["show_price"] and x["price_aed"] else None), family=x["family"], fam_label=pretty_fam,
                score=x["score"], title=x["title"], img_url=x["image_url"], pid=re.sub(r"\W", "", x["handle"]), rank=x.get("rank"))


def cutout(w):
    out = ROOT / "assets" / f"q_{w['pid']}.png"
    if not out.exists():
        tmp = ROOT / "assets" / f"_tmp_{w['pid']}"
        subprocess.run(["curl", "-sSL", "-o", str(tmp), w["img_url"]], check=True)
        im = Image.open(tmp).convert("RGBA")
        bb = im.getchannel("A").getbbox()
        im.crop(bb).save(out)
        tmp.unlink()
    w["img"] = out.name


# ------------------------------------------------------------------ choose watches
seen, cands = set(), []
for x in sorted(pool, key=lambda x: (-x["score"], x.get("rank", 0))):
    w = parse(x)
    if w["ref"] in EXCLUDE_REFS or x["score"] < 84:
        continue
    if x["vendor"] == "Rolex" and not x["show_price"]:
        continue
    key = (w["name"], w["ref"], w["spec"])
    if key in seen:
        continue
    seen.add(key)
    cands.append(w)
patek = [parse(x) for x in pool if x["vendor"] == "Patek Philippe" and x["family"] in ("Nautilus", "Aquanaut") and not x["show_price"]]
patek = [w for w in patek if "Travel" not in w["title"] and "Chronograph" not in w["title"]][:3]
byfam = collections.defaultdict(list)
for w in cands:
    byfam[w["family"]].append(w)
TOP = ["Daytona", "GMT-Master II", "Submariner Date"]
ORDER = ["Daytona", "Datejust", "GMT-Master II", "Day-Date", "Submariner Date", "Sky-Dweller", "Land-Dweller", "Oyster Perpetual", "Datejust", "Daytona"]
# Datejust variety: spread dial colours / metals by interleaving
def take(fam, used_names):
    for w in byfam[fam]:
        if id(w) in used_names:
            continue
        return w
    return None


def pick_stories(styles):
    """Returns list of 15 days; each day: list of 3 story dicts (kind available)."""
    used = set()
    days = []
    fam_i = 0
    patek_i = 0
    for d in range(15):
        style = styles[d % 6]
        day = []
        # story 1 always a top-demand family, rotating
        fams = [TOP[d % 3]]
        others = [f for f in ORDER if f not in TOP]
        fams.append(others[(2 * d) % len(others)])
        fams.append(others[(2 * d + 1) % len(others)])
        if style in ("cream", "editorial") and d in (3, 4, 10, 11, 8) and patek_i < len(patek):
            fams[2] = "PATEK"
        n_cards = 3
        for k in range(n_cards):
            fam = fams[k]
            if fam == "PATEK":
                w = patek[patek_i]; patek_i += 1
                day.append([w]); continue
            if style == "pair":
                grp = []
                if fam == "Oyster Perpetual":
                    fam = "Datejust"
                for _ in range(2):
                    w = take(fam, used)
                    if w is None:
                        fam = TOP[0]; w = take(fam, used)
                    used.add(id(w)); grp.append(w)
                day.append(grp)
            else:
                w = take(fam, used)
                if w is None:
                    w = take("Daytona", used)
                used.add(id(w)); day.append([w])
        days.append((style, day))
    return days


STYLES = ["hero", "cream", "pair", "set", "editorial", "plaque"]
plan = pick_stories(STYLES)
FN = dict(hero=B.st1_hero, cream=B.st2_cream, set=B.st4_set, editorial=B.st5_editorial, plaque=B.st6_plaque)

# ------------------------------------------------------------------ choose knowledge stories (45 of the new library)
lib = [x for x in K2.L if not x["confirm"]]
confirm_items = [x for x in K2.L if x["confirm"]]
kdays, used_ids, prev_layouts = [], set(), set()
fam_cnt = 0
import random
rnd = random.Random(7)
for d in range(15):
    day, lay, grps = [], set(), collections.Counter()
    for k in range(3):
        best, bs = None, 1e9
        for x in lib:
            if x["id"] in used_ids or x["layout"] in lay:
                continue
            s = rnd.random() * 0.5
            s += 3 if x["layout"] in prev_layouts else 0
            s += 4 * grps[x["grp"]]
            s += {"family": 0, "fake": 0.3, "buy": 0.3, "gmt": 0.6, "tech": 0.2, "guide": 0.1}[x["grp"]]
            if s < bs:
                best, bs = x, s
        used_ids.add(best["id"]); lay.add(best["layout"]); grps[best["grp"]] += 1; day.append(best)
    prev_layouts = lay
    kdays.append(day)

# ------------------------------------------------------------------ render
jobs, manifest, cal = [], [], []
ai = ki = 0
for d in range(DAYS):
    date = START + datetime.timedelta(days=d)
    ds = date.isoformat()
    if d % 2 == 0:
        style, day = plan[ai]
        urg_idx = set()
        if ai % 3 == 1:
            urg_idx.add(0)
        for n, grp in enumerate(day, 1):
            for w in grp:
                if "img" not in w:
                    cutout(w)
            urgency = "demand" if (n - 1) in urg_idx and grp[0]["vendor"] == "Rolex" and grp[0]["family"] in TOP else None
            nm = f"{ds}_{n}"
            if style == "pair":
                B.st3_pair(grp[0], grp[1], headline=(grp[0]["fam_label"] if grp[0]["family"]==grp[1]["family"] else "ROLEX"), urgency=urgency, name=nm)
            else:
                FN[style](grp[0], urgency=urgency, name=nm)
            jobs.append(dict(html=f"templates/{nm}.html", out=f"queue/{nm}.jpg"))
            manifest.append(dict(date=ds, n=n, kind="available", style=style, urgency=urgency, file=f"queue/{nm}.jpg",
                                 watches=[dict(title=w["title"], ref=w["ref"], price=w["price"]) for w in grp]))
        cal.append((ds, "Available Now", style, [" + ".join(w["name"] for w in g) for g in day], "demand band on story " + ", ".join(str(i + 1) for i in sorted(urg_idx)) if urg_idx else "-"))
        ai += 1
    else:
        day = kdays[ki]
        for n, x in enumerate(day, 1):
            nm = f"{ds}_{n}"
            B.KN[x["layout"]](x, B.TPL, nm)
            jobs.append(dict(html=f"templates/{nm}.html", out=f"queue/{nm}.jpg"))
            manifest.append(dict(date=ds, n=n, kind="knowledge", layout=x["layout"], id=x["id"], title=x["title"], source=x["src"], file=f"queue/{nm}.jpg"))
        cal.append((ds, "Knowledge", "-", [f"{x['eyebrow']} · {x['title']} ({x['layout']})" for x in day], "-"))
        ki += 1
rep = B.render(jobs)
json.dump(manifest, open(ROOT / "queue_v2.json", "w"), indent=1, ensure_ascii=False)
json.dump(dict(unused_knowledge=[x["id"] for x in lib if x["id"] not in used_ids], needs_confirmation=[x["id"] for x in confirm_items]),
          open(ROOT / "queue_reserve.json", "w"), indent=1)
with open(ROOT / "calendar.md", "w") as f:
    f.write("# 30-day story calendar (3 stories a day, Available Now and Knowledge days alternate)\n\n| Date | Day type | Style | Stories | Urgency |\n|---|---|---|---|---|\n")
    for ds, kind, style, items, urg in cal:
        f.write(f"| {ds} | {kind} | {style} | {'<br>'.join(items)} | {urg} |\n")
print("rendered", len(jobs), "warnings", len(rep), "knowledge used", len(used_ids), "reserve", len(lib) - len(used_ids))

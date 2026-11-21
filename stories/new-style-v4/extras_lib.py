import json, re, subprocess, sys
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parent
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
                score=x["score"], title=x["title"], img_url=x["image_url"], pid=re.sub(r"\W", "", x["handle"])[:40], rank=x.get("rank"))


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


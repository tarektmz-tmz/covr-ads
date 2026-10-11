"""Download every product image listed in data/products.json.

Usage:  python3 scripts/download_images.py
Output: images/<product>/<file>  (shared lifestyle photos are saved once per product)
No extra packages needed.
"""
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "products.json").read_text(encoding="utf-8"))

for product in data["products"]:
    folder = ROOT / "images" / re.sub(r"[^a-z0-9]+", "-", product["title"].lower()).strip("-")
    folder.mkdir(parents=True, exist_ok=True)
    for i, img in enumerate(product["images"], 1):
        name = img["url"].split("/")[-1].split("?")[0]
        target = folder / f"{i:02d}_{name}"
        if target.exists():
            continue
        print("downloading", target.relative_to(ROOT))
        req = urllib.request.Request(img["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            target.write_bytes(r.read())

print("done ->", ROOT / "images")

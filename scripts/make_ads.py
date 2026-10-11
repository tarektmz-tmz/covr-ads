"""Turn one photo into Facebook/Instagram ad images in the three Meta sizes.

Usage:
  pip install pillow
  python3 scripts/make_ads.py images/total-black/04_20251111131525217.jpg \
      --headline "All black. Nothing catches the light." \
      --sub 'Total Black padel racket cover · $199' \
      --cta "Shop now · padelcovr.com" \
      --name total-black-player

Output: ads/<name>_square.jpg (1080x1080, feed)
        ads/<name>_portrait.jpg (1080x1350, feed - best for mobile)
        ads/<name>_story.jpg (1080x1920, stories/reels)

Optional: --style band puts the text on a cream band under the photo (best for light studio shots).
          --focus 0.3 moves the crop up (0 = top, 0.5 = centre, 1 = bottom).
          --font path/to/your-brand-font.ttf
"""
import argparse
import pathlib

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SIZES = {"square": (1080, 1080), "portrait": (1080, 1350), "story": (1080, 1920)}
CREAM = (245, 240, 230)
INK = (17, 17, 17)

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Didot.ttc",  # macOS
    "/System/Library/Fonts/Helvetica.ttc",
    "C:/Windows/Fonts/georgia.ttf",  # Windows
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",  # Linux
]


def load_font(path, size):
    for p in [path] + FONT_CANDIDATES:
        if p and pathlib.Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


def wrap(draw, text, font, max_w):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= max_w:
            line = test
        else:
            lines.append(line)
            line = word
    return lines + [line] if line else lines


def text_blocks(draw, w, margin, headline, sub, cta, font_path, reserve=0):
    f_head = load_font(font_path, 64 if w == 1080 else 70)
    f_small = load_font(font_path, 34)
    blocks = []
    if headline:
        lines = wrap(draw, headline, f_head, w - 2 * margin - reserve)
        blocks += [(line, f_head, 30 if i == len(lines) - 1 else 12) for i, line in enumerate(lines)]
    if sub:
        blocks.append((sub, f_small, 18))
    if cta:
        blocks.append((cta.upper(), f_small, 0))
    return [(t, f, draw.textbbox((0, 0), t, font=f)[3] + gap) for t, f, gap in blocks]


def make(photo, size, headline, sub, cta, font_path, focus, style="overlay"):
    w, h = size
    margin = 72
    safe = 220 if h == 1920 else 0  # keep clear of the Stories reply bar

    if style == "band":
        # Clean photo on top, cream band with dark text below. Best for light studio shots.
        probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        blocks = text_blocks(probe, w, margin, headline, sub, cta, font_path, reserve=150)  # room for the logo
        band = sum(bh for _, _, bh in blocks) + 2 * 64 + safe
        img = Image.new("RGB", size, CREAM)
        img.paste(ImageOps.fit(photo, (w, h - band), Image.LANCZOS, centering=(0.5, focus)).convert("RGB"), (0, 0))
        draw = ImageDraw.Draw(img)
        y = h - band + 64
        for text, font, bh in blocks:
            draw.text((margin, y), text, font=font, fill=INK)
            y += bh
        logo = load_font(font_path, 40)
        draw.text((w - margin - draw.textlength("COVR", font=logo), h - band + 64), "COVR", font=logo, fill=INK)
        return img

    img = ImageOps.fit(photo, size, Image.LANCZOS, centering=(0.5, focus)).convert("RGB")

    # Dark gradient at the bottom so text stays readable on any photo.
    shade = Image.new("L", (1, h))
    start = int(h * 0.55)
    for y in range(h):
        shade.putpixel((0, y), 0 if y < start else int(190 * (y - start) / (h - start)))
    img = Image.composite(Image.new("RGB", size, (0, 0, 0)), img, shade.resize(size))

    draw = ImageDraw.Draw(img)
    blocks = text_blocks(draw, w, margin, headline, sub, cta, font_path)
    y = h - safe - 80 - sum(bh for _, _, bh in blocks)
    for text, font, bh in blocks:
        draw.text((margin, y), text, font=font, fill=CREAM)
        y += bh

    # Small wordmark top-left.
    draw.text((margin, margin - 10), "COVR", font=load_font(font_path, 40), fill=CREAM)
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("--headline", default="")
    ap.add_argument("--sub", default="")
    ap.add_argument("--cta", default="Shop now · padelcovr.com")
    ap.add_argument("--name", default=None)
    ap.add_argument("--font", default=None)
    ap.add_argument("--focus", type=float, default=0.5)
    ap.add_argument("--style", choices=["overlay", "band"], default="overlay",
                    help="overlay: text on the photo (dark photos). band: text on a cream band below (light studio photos)")
    a = ap.parse_args()

    photo = ImageOps.exif_transpose(Image.open(a.photo))
    name = a.name or pathlib.Path(a.photo).stem
    out = ROOT / "ads"
    out.mkdir(exist_ok=True)
    for label, size in SIZES.items():
        path = out / f"{name}_{label}.jpg"
        make(photo, size, a.headline, a.sub, a.cta, a.font, a.focus, a.style).save(path, quality=92)
        print("saved", path.relative_to(ROOT))


if __name__ == "__main__":
    main()

"""Turn 3-5 photos into a short video ad (slow zoom, crossfades, text, end card).

Needs: pip install pillow   +   ffmpeg (Mac: brew install ffmpeg | Windows: winget install ffmpeg)

Usage:
  python3 scripts/make_video.py \
      --slide "images/total-black/04_20251111131525217.jpg|All black." \
      --slide "images/total-black/05_KEEPMECLOSER_20251111_131342_0000.png|Black leather. Black hardware." \
      --slide "images/total-black/07_IMG_6008_JPG.jpg|Built for real play." \
      --end 'Total Black|Handmade padel racket cover · $199' \
      --name total-black-video

Each --slide is "photo|text" (text optional). Optional: --style band (cream text band, best for light studio photos), --format portrait (1080x1350 feed)
instead of the default story (1080x1920 Stories/Reels), --seconds 3 per slide, --music song.mp3.
Output: ads/<name>_<format>.mp4
"""
import argparse
import pathlib
import subprocess

from PIL import Image, ImageDraw, ImageOps

from make_ads import CREAM, INK, load_font, wrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMATS = {"story": (1080, 1920), "portrait": (1080, 1350), "square": (1080, 1080)}
FPS = 30
FADE = 0.5  # seconds of crossfade between slides
ZOOM = 0.08  # each photo slowly zooms in by 8%


def gradient(size, start=0.55, strength=170):
    w, h = size
    col = Image.new("L", (1, h))
    for y in range(h):
        col.putpixel((0, y), 0 if y < h * start else int(strength * (y - h * start) / (h * (1 - start))))
    return col.resize(size)


def text_layer(size, text, font_path, big=True):
    """Transparent overlay with COVR wordmark and the slide text near the bottom."""
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((72, 62), "COVR", font=load_font(font_path, 40), fill=CREAM)
    if text:
        font = load_font(font_path, 72 if big else 60)
        lines = wrap(d, text, font, w - 144)
        line_h = d.textbbox((0, 0), "Ag", font=font)[3] + 14
        y = h - (330 if h == 1920 else 120) - line_h * len(lines)
        for line in lines:
            d.text((72, y), line, font=font, fill=CREAM)
            y += line_h
    return layer


def band_layer(size, band, text, font_path):
    """Cream band at the bottom with dark slide text and the COVR wordmark."""
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rectangle((0, h - band, w, h), fill=CREAM)
    logo = load_font(font_path, 40)
    d.text((w - 72 - d.textlength("COVR", font=logo), h - band + 64), "COVR", font=logo, fill=INK)
    if text:
        font = load_font(font_path, 66)
        line_h = d.textbbox((0, 0), "Ag", font=font)[3] + 14
        y = h - band + 56
        for line in wrap(d, text, font, w - 144 - 150):
            d.text((72, y), line, font=font, fill=INK)
            y += line_h
    return layer


def end_card(size, headline, sub, font_path):
    w, h = size
    img = Image.new("RGB", size, (17, 17, 17))
    d = ImageDraw.Draw(img)
    f_logo, f_head, f_small = load_font(font_path, 110), load_font(font_path, 64), load_font(font_path, 36)
    items = [("COVR", f_logo, 70), (headline, f_head, 24), (sub, f_small, 70), ("SHOP NOW · PADELCOVR.COM", f_small, 0)]
    items = [i for i in items if i[0]]
    total = sum(d.textbbox((0, 0), t, font=f)[3] + g for t, f, g in items)
    y = (h - total) // 2
    for t, f, g in items:
        d.text(((w - d.textlength(t, font=f)) / 2, y), t, font=f, fill=CREAM)
        y += d.textbbox((0, 0), t, font=f)[3] + g
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slide", action="append", required=True, help='"photo|text"')
    ap.add_argument("--end", default="", help='"headline|subline" for the final card')
    ap.add_argument("--format", choices=FORMATS, default="story")
    ap.add_argument("--seconds", type=float, default=3.0)
    ap.add_argument("--music", default=None)
    ap.add_argument("--font", default=None)
    ap.add_argument("--name", default="covr-video")
    ap.add_argument("--style", choices=["overlay", "band"], default="overlay",
                    help="band: text on a cream band under the photo (best for light studio shots)")
    a = ap.parse_args()

    size = FORMATS[a.format]
    shade = gradient(size)
    black = Image.new("RGB", size, (0, 0, 0))

    # Each slide is a function t (0..1) -> frame.
    slides = []
    for spec in a.slide:
        photo_path, _, text = spec.partition("|")
        band = (480 if size[1] == 1920 else 260) if a.style == "band" else 0  # story band includes reply-bar space
        area = (size[0], size[1] - band)
        big = ImageOps.fit(ImageOps.exif_transpose(Image.open(photo_path)).convert("RGB"),
                           (int(area[0] * (1 + ZOOM)), int(area[1] * (1 + ZOOM))), Image.LANCZOS)
        if band:
            overlay = band_layer(size, band, text.strip(), a.font)
        else:
            overlay = text_layer(size, text.strip(), a.font)

        def frame(t, big=big, overlay=overlay, area=area, band=band):
            z = 1 + ZOOM * (1 - t)  # crop shrinks over time = zoom in
            cw, ch = int(big.width / z), int(big.height / z)
            x, y = (big.width - cw) // 2, (big.height - ch) // 2
            photo = big.crop((x, y, x + cw, y + ch)).resize(area, Image.BILINEAR)
            if band:
                img = Image.new("RGB", size, CREAM)
                img.paste(photo, (0, 0))
            else:
                img = Image.composite(black, photo, shade)
            img.paste(overlay, (0, 0), overlay)
            return img

        slides.append(frame)

    headline, _, sub = a.end.partition("|")
    card = end_card(size, headline.strip(), sub.strip(), a.font)
    slides.append(lambda t: card)

    out = ROOT / "ads"
    out.mkdir(exist_ok=True)
    path = out / f"{a.name}_{a.format}.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{size[0]}x{size[1]}", "-r", str(FPS), "-i", "-"]
    if a.music:
        cmd += ["-i", a.music, "-shortest", "-af", "afade=t=out:st=%f:d=1" % (len(slides) * a.seconds - 1)]
    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", str(path)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    per = int(a.seconds * FPS)
    fade = int(FADE * FPS)
    for i, slide in enumerate(slides):
        for f in range(per):
            img = slide(f / per)
            if i + 1 < len(slides) and f >= per - fade:  # crossfade into the next slide
                img = Image.blend(img, slides[i + 1](0), (f - (per - fade)) / fade)
            ff.stdin.write(img.tobytes())
    ff.stdin.close()
    ff.wait()
    print("saved", path.relative_to(ROOT), f"({len(slides) * a.seconds:.0f}s)")


if __name__ == "__main__":
    main()

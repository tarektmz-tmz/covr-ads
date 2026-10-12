"""COVR product film, 9:16 Reel, in the style of the SanDisk reference (dark stage, warm rim light,
slow macro moves, one feature per shot, thin type). Built only from the real studio photo cutout,
so the product is never redrawn.

Usage: python3 scripts/make_reel.py [navy]  -> ads/reel/covr-reel-<colour>.mp4
"""
import math
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "creative" / "fonts"
W, H, FPS = 1080, 1920, 30
GOLD = (217, 169, 112)
CREAM = (243, 237, 227)

COLOUR = sys.argv[1] if len(sys.argv) > 1 else "navy"
OFFER = {"was": "$249", "now": "$199", "line": "20% off with code COV20 · ends 26 Oct"}

# Detail positions in the ORIGINAL 2000x2000 packshot (navy). Cutout offset is subtracted below.
OFFSET = (362, 207)
P = {
    "crest": (965, 1460), "zip": (1000, 1072), "pull": (580, 1180), "collar": (970, 300),
    "dring": (935, 545), "piping": (1420, 1180), "centre": (965, 1030),
}


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


F_HEAD = font("Inter-300.ttf", 74)
F_SUB = font("Inter-400.ttf", 38)
F_BIG = font("Inter-300.ttf", 150)
F_SERIF = font("InstrumentSerif-400.ttf", 150)
F_PRICE = font("Montserrat-800.ttf", 96)


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


# ---------- stage: cutout on a dark backdrop with a warm rim glow ----------
cut = Image.open(ROOT / f"media/cut/pack-{COLOUR}.png").convert("RGBA")
PAD = 900
SW, SH = cut.width + 2 * PAD, cut.height + 2 * PAD


def to_stage(p):
    return (p[0] - OFFSET[0] + PAD, p[1] - OFFSET[1] + PAD)


def build_stage(glow_strength):
    yy, xx = np.mgrid[0:SH, 0:SW]
    cx, cy = SW / 2, SH * 0.48
    r = np.sqrt(((xx - cx) / SW) ** 2 + ((yy - cy) / SH) ** 2)
    base = np.clip(26 - r * 40, 6, 26)
    bg = np.dstack([base * 1.05, base * 0.95, base * 0.9]).astype("uint8")
    stage = Image.fromarray(bg, "RGB").convert("RGBA")
    a = cut.getchannel("A")
    glow_mask = Image.new("L", (SW, SH), 0)
    glow_mask.paste(a, (PAD, PAD))
    glow_mask = glow_mask.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(90))
    glow = Image.new("RGBA", (SW, SH), (255, 140, 60, 0))
    glow.putalpha(glow_mask.point(lambda v: int(v * glow_strength)))
    stage.alpha_composite(glow)
    shadow = Image.new("L", (SW, SH), 0)
    shadow.paste(a, (PAD + 10, PAD + 30))
    shadow = shadow.filter(ImageFilter.GaussianBlur(25))
    stage.alpha_composite(Image.merge("RGBA", [Image.new("L", (SW, SH), 0)] * 3 + [shadow.point(lambda v: int(v * .6))]))
    stage.alpha_composite(cut, (PAD, PAD))
    return stage.convert("RGB")


STAGE_SOFT = build_stage(0.35)
STAGE_HOT = build_stage(0.85)

VIGNETTE = None


def vignette():
    global VIGNETTE
    if VIGNETTE is None:
        yy, xx = np.mgrid[0:H, 0:W]
        r = np.sqrt(((xx - W / 2) / (W * .75)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2)
        VIGNETTE = Image.fromarray((np.clip(1 - (r - .55) * 1.4, .25, 1) * 255).astype("uint8"), "L")
    return VIGNETTE


def camera(stage, cx, cy, zoom):
    """zoom = output pixels per stage pixel."""
    cw, ch = W / zoom, H / zoom
    box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
    img = stage.transform((W, H), Image.EXTENT, box, Image.BICUBIC)
    black = Image.new("RGB", (W, H), (8, 7, 6))
    return Image.composite(img, black, vignette())


def sweep(img, t, angle=-25, strength=0.22):
    """A soft diagonal light band moving across the frame."""
    band = Image.new("L", (W * 2, H * 2), 0)
    d = ImageDraw.Draw(band)
    x = int(-W * .5 + t * W * 2.2)
    d.rectangle([x, 0, x + 260, H * 2], fill=255)
    band = band.filter(ImageFilter.GaussianBlur(120)).rotate(angle, center=(W, H)).crop((W // 2, H // 2, W // 2 + W, H // 2 + H))
    light = Image.new("RGB", (W, H), (255, 236, 210))
    return Image.composite(light, img, band.point(lambda v: int(v * strength)))


def text(img, lines, y, a, align="left", x=90):
    """lines: [(text, font, colour)], fades with alpha a and drifts up slightly."""
    if a <= 0:
        return img
    shade = Image.new("L", (W, H), 0)
    hh = sum(f.size * 1.25 for _, f, _ in lines)
    ImageDraw.Draw(shade).rectangle([0, y - 90, W, y + hh + 90], fill=200)
    shade = shade.filter(ImageFilter.GaussianBlur(70)).point(lambda v: int(v * a))
    img = Image.composite(Image.new("RGB", (W, H), (8, 7, 6)), img, shade)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    yy = y + (1 - a) * 24
    for t, f, col in lines:
        tw = d.textlength(t, font=f)
        xx = (W - tw) / 2 if align == "center" else x
        d.text((xx, yy), t, font=f, fill=col + (int(255 * a),))
        yy += f.size * 1.25
    out = img.convert("RGBA")
    out.alpha_composite(layer)
    return out.convert("RGB")


def fade_in_out(t, dur, fin=.5, fout=.4):
    return min(ease(t / fin), ease((dur - t) / fout))


# ---------- shots: (duration, render(t)) ----------
def lerp(a, b, t):
    return a + (b - a) * ease(t)


def macro(point_a, point_b, z0, z1, stage=STAGE_SOFT):
    (ax, ay), (bx, by) = to_stage(point_a), to_stage(point_b)
    return lambda t, d: camera(stage, lerp(ax, bx, t / d), lerp(ay, by, t / d), lerp(z0, z1, t / d))


def s_crest(t, d):
    img = macro((930, 1430), (1000, 1490), 1.85, 2.15)(t, d)
    return sweep(img, t / d, strength=.18)


def s_edge(t, d):
    img = macro((1330, 760), (1360, 1420), 1.75, 1.75)(t, d)
    img = sweep(img, t / d)
    return text(img, [("Every stitch, considered.", F_HEAD, CREAM), ("Cotton canvas. Leather piping.", F_SUB, (190, 180, 168))], 1500, fade_in_out(t, d))


def s_collar(t, d):
    img = macro((940, 330), (990, 380), 2.0, 1.85)(t, d)
    return text(img, [("Open back.", F_HEAD, CREAM), ("Lets your grip breathe after play.", F_SUB, (190, 180, 168))], 1560, fade_in_out(t, d))


def s_pocket(t, d):
    img = macro((700, 980), (1250, 960), 2.3, 2.3)(t, d)
    img = sweep(img, t / d, strength=.15)
    return text(img, [("Phone. Keys. Cards.", F_HEAD, CREAM), ("Front zip pocket.", F_SUB, (190, 180, 168))], 330, fade_in_out(t, d))


def s_dring(t, d):
    img = macro((935, 600), (935, 520), 2.0, 2.7)(t, d)
    return text(img, [("Clip it on.", F_HEAD, CREAM), ("D-ring for a COVR ball pouch.", F_SUB, (190, 180, 168))], 1560, fade_in_out(t, d))


def s_reveal(t, d):
    cx, cy = to_stage(P["centre"])
    z = lerp(0.48, 0.62, t / d)
    img = camera(STAGE_HOT, cx, cy + lerp(260, 0, t / d), z)
    dark = Image.new("RGB", (W, H), (8, 7, 6))
    return Image.blend(dark, img, ease(t / 1.2))


def s_measure(t, d):
    cx, cy = to_stage(P["centre"])
    img = camera(STAGE_SOFT, cx + 120, cy, 0.5)
    a = fade_in_out(t, d, fin=.6)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(layer)
    col = (200, 190, 175, int(230 * a))
    top, bot, left, right = 520, 1350, 245, 845           # cover extents at this camera
    k = ease(min(1, t / 1.2))
    lx = right + 70
    dr.line([(lx, top), (lx, top + (bot - top) * k)], fill=col, width=2)
    for yv in (top, bot):
        dr.line([(lx - 14, yv), (lx + 14, yv)], fill=col, width=2)
    by = bot + 70
    dr.line([(left, by), (left + (right - left) * k, by)], fill=col, width=2)
    for xv in (left, right):
        dr.line([(xv, by - 14), (xv, by + 14)], fill=col, width=2)
    dr.text((lx + 26, (top + bot) / 2 - 24), "39 cm", font=F_SUB, fill=col)
    dr.text(((left + right) / 2 - 45, by + 22), "29 cm", font=F_SUB, fill=col)
    out = img.convert("RGBA")
    out.alpha_composite(layer)
    return text(out.convert("RGB"), [("Fits most standard", F_HEAD, CREAM), ("padel rackets.", F_HEAD, CREAM)], 1560, a)


def s_hero(t, d):
    cx, cy = to_stage(P["centre"])
    img = camera(STAGE_HOT, cx, cy - 40, lerp(0.54, 0.58, t / d))
    img = sweep(img, t / d, strength=.12)
    a = fade_in_out(t, d, fin=.5, fout=.3)
    img = text(img, [("Cotton. Leather.", F_HEAD, CREAM), ("Waterproof lining.", F_HEAD, CREAM)], 250, a, align="center")
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(layer)
    pa = ease((t - 1.0) / .5)
    if pa > 0:
        was_w = dr.textlength(OFFER["was"], font=F_SUB)
        now_w = dr.textlength(OFFER["now"], font=F_PRICE)
        x0 = (W - (was_w + 30 + now_w)) / 2
        y = 1480
        dr.text((x0, y + 52), OFFER["was"], font=F_SUB, fill=(170, 160, 150, int(255 * pa)))
        dr.line([(x0 - 4, y + 72), (x0 + was_w + 4, y + 72)], fill=(170, 160, 150, int(255 * pa)), width=3)
        dr.text((x0 + was_w + 30, y), OFFER["now"], font=F_PRICE, fill=GOLD + (int(255 * pa),))
        lw = dr.textlength(OFFER["line"], font=F_SUB)
        dr.text(((W - lw) / 2, y + 140), OFFER["line"], font=F_SUB, fill=(210, 200, 188, int(255 * pa)))
    out = img.convert("RGBA")
    out.alpha_composite(layer)
    return out.convert("RGB")


def s_end(t, d):
    img = Image.new("RGB", (W, H), (8, 7, 6))
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse([W / 2 - 330, H / 2 - 200, W / 2 + 330, H / 2 + 140], fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    img = Image.composite(Image.new("RGB", (W, H), (120, 60, 25)), img, glow.point(lambda v: int(v * .55 * ease(t / .8))))
    a = ease(t / .6)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(layer)
    word, sp = "COVR", 40
    total = sum(dr.textlength(c, font=F_SERIF) for c in word) + sp * 3
    x = (W - total) / 2
    for c in word:
        dr.text((x, H / 2 - 150), c, font=F_SERIF, fill=CREAM + (int(255 * a),))
        x += dr.textlength(c, font=F_SERIF) + sp
    for line, yy in [("Handmade padel racket covers", H / 2 + 60), ("padelcovr.com", H / 2 + 110)]:
        lw = dr.textlength(line, font=F_SUB)
        dr.text(((W - lw) / 2, yy), line, font=F_SUB, fill=(200, 190, 178, int(255 * ease((t - .4) / .6))))
    img = img.convert("RGBA")
    img.alpha_composite(layer)
    return img.convert("RGB")


SHOTS = [(2.4, s_crest), (2.6, s_edge), (2.6, s_collar), (2.6, s_pocket), (2.4, s_dring),
         (2.6, s_reveal), (3.0, s_measure), (3.6, s_hero), (2.6, s_end)]
XF = 0.35  # crossfade seconds


def main():
    out = ROOT / "ads" / "reel"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"covr-reel-{COLOUR}.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
                           "-preset", "slow", "-movflags", "+faststart", str(path)], stdin=subprocess.PIPE)
    total = 0
    for i, (dur, fn) in enumerate(SHOTS):
        n = int(dur * FPS)
        nxt = SHOTS[i + 1] if i + 1 < len(SHOTS) else None
        for f in range(n):
            t = f / FPS
            frame = fn(t, dur)
            if nxt and t > dur - XF:
                frame = Image.blend(frame, nxt[1](0, nxt[0]), (t - (dur - XF)) / XF)
            ff.stdin.write(frame.tobytes())
            total += 1
    ff.stdin.close()
    ff.wait()
    print("saved", path.relative_to(ROOT), f"{total / FPS:.1f}s")


if __name__ == "__main__":
    if "--stills" in sys.argv:
        out = ROOT / "ads" / "reel"
        out.mkdir(parents=True, exist_ok=True)
        for i, (dur, fn) in enumerate(SHOTS):
            fn(dur * .55, dur).save(out / f"_still_{i:02d}.jpg", quality=88)
        print("stills saved")
    else:
        main()

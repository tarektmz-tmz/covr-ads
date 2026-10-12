#!/usr/bin/env python3
"""'Sorry, padel girls' low-stock ad: Baby Pink + Sky Denim gift-box photo, brightened and pinked.
Outputs 1080x1350 (feed) and 1080x1920 (story) to ads/girls/."""
import os, numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
ROSE = (212, 92, 126); INK = (58, 38, 46)
F9 = P('creative/fonts/Montserrat-900.ttf'); F6 = P('creative/fonts/Inter-600.ttf') if os.path.exists(P('creative/fonts/Inter-600.ttf')) else P('creative/fonts/Inter-500.ttf'); F4 = P('creative/fonts/Inter-400.ttf')

def enhance(im, wall_box=(150, 700, 100, 700), shift=True):
    a = np.asarray(im).astype(np.float32) / 255
    # white balance: make the plaster wall a clean, slightly blush white
    y0, y1, x0, x1 = wall_box
    wall = a[y0:y1, x0:x1].reshape(-1, 3).mean(0)
    a = a * (np.array([0.93, 0.90, 0.90]) / wall)
    # exposure + soft S-curve
    a = np.clip(a, 0, 1) ** 0.94
    a = a + 0.10 * (a - 0.5) * (1 - np.abs(2 * a - 1))
    # vibrance: push already-coloured pixels (pink cover, blue denim) more than neutrals
    l = a.mean(2, keepdims=True); sat = a.max(2, keepdims=True) - a.min(2, keepdims=True)
    a = l + (a - l) * (1 + 0.22 * np.clip(sat * 4, 0, 1))
    # blush in the highlights
    # blush the neutral surfaces (walls, floor, tissue) - the pinky look
    neutral = np.clip(1 - sat * 6, 0, 1) * np.clip((l - 0.35) / 0.4, 0, 1)
    a = a * (1 - 0.16 * neutral) + np.array([0.99, 0.86, 0.89]) * l * 1.04 * 0.16 * neutral
    a = np.clip(a, 0, 1)
    # coral -> true Baby Pink: rotate warm reds toward rose, soften saturation a little
    if not shift:
        out = Image.fromarray((a * 255).astype(np.uint8))
        return finish(out)
    import colorsys
    hsv = np.asarray(Image.fromarray((a * 255).astype(np.uint8)).convert('HSV')).astype(np.float32)
    h, s_, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    m = ((h < 18) | (h > 240)) & (s_ > 60)
    w = np.clip((s_ - 60) / 60, 0, 1) * m
    h2 = np.where(h < 18, h - 12 * w, h)  # wrap into magenta side
    h2 = np.mod(h2, 256)
    s2 = s_ * (1 - 0.12 * w); v2 = np.minimum(255, v * (1 + 0.04 * w))
    a = np.asarray(Image.fromarray(np.stack([h2, s2, v2], -1).astype(np.uint8), 'HSV').convert('RGB')).astype(np.float32) / 255
    out = Image.fromarray((a * 255).astype(np.uint8))
    return finish(out)

def finish(out):
    # clarity + crisp detail
    out = out.filter(ImageFilter.UnsharpMask(radius=6, percent=25, threshold=2))
    out = out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=55, threshold=2))
    # soft dreamy bloom on highlights
    b = np.asarray(out).astype(np.float32)
    glow = np.asarray(Image.fromarray(np.clip((b - 200) * 3, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(28))).astype(np.float32)
    b = np.clip(b + glow * 0.07, 0, 255)
    return Image.fromarray(b.astype(np.uint8))

def italic_text(txt, font, fill, shear=0.18):
    d = ImageDraw.Draw(Image.new('L', (1, 1)))
    w = int(d.textlength(txt, font=font)) + 60; h = int(font.size * 1.35)
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ImageDraw.Draw(lay).text((20, 0), txt, font=font, fill=fill)
    return lay.transform((w + int(h * shear), h), Image.AFFINE, (1, shear, -h * shear, 0, 1, 0), Image.BICUBIC)

def build(W, H, crop_box, head_y, pill_y, name, src='media/IMG_0628.JPG', sub="We're running out of Baby Pink & Sky Denim...", wall=(150, 700, 100, 700), shift=True, wash=170):
    src = ImageOps.exif_transpose(Image.open(P(src))).convert('RGB')
    img = enhance(src.crop(crop_box), wall, shift).resize((W, H), Image.LANCZOS).convert('RGBA')
    # soft blush wash at the top for the headline
    g = np.zeros((H, W, 4), np.uint8); t = np.clip(1 - np.arange(H) / (head_y + 330), 0, 1) ** 1.6
    g[..., 0], g[..., 1], g[..., 2] = 253, 240, 243
    if wash > 200:
        yy = np.arange(H); t = np.clip(1 - (yy - (head_y + 175)) / 190, 0, 1) ** 1.3
    g[..., 3] = (np.minimum(1, t * 1.25) * wash)[:, None].astype(np.uint8)
    img = Image.alpha_composite(img, Image.fromarray(g, 'RGBA'))
    d = ImageDraw.Draw(img)
    head = italic_text('SORRY, PADEL GIRLS', ImageFont.truetype(F9, 80), ROSE + (255,))
    sh = italic_text('SORRY, PADEL GIRLS', ImageFont.truetype(F9, 80), (255, 255, 255, 200)).filter(ImageFilter.GaussianBlur(6))
    x = (W - head.width) // 2
    img.alpha_composite(sh, (x, head_y + 3)); img.alpha_composite(head, (x, head_y))
    f = ImageFont.truetype(F6, 42); s = sub
    w = d.textlength(s, font=f); d.text(((W - w) / 2, head_y + 112), s, font=f, fill=INK)
    if pill_y is None:
        out = P('ads/girls', name); img.convert('RGB').save(out, quality=95); print(out); return
    # pill: Only 2 Baby Pink & 3 Sky Denim left.
    fb = ImageFont.truetype(F6, 38); fr = ImageFont.truetype(F4, 38)
    parts = [('Only ', fr), ('2 Baby Pink', fb), (' & ', fr), ('3 Sky Denim', fb), (' left.', fr)]
    tw = sum(d.textlength(t, font=ff) for t, ff in parts)
    px0 = (W - tw) / 2 - 46
    shp = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(shp).rounded_rectangle((px0, pill_y + 8, px0 + tw + 92, pill_y + 94), radius=46, fill=(120, 40, 70, 60))
    img.alpha_composite(shp.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((px0, pill_y, px0 + tw + 92, pill_y + 88), radius=44, fill=(255, 255, 255, 245))
    x = px0 + 46
    for t, ff in parts:
        d.text((x, pill_y + 20), t, font=ff, fill=INK); x += d.textlength(t, font=ff)
    out = P('ads/girls', name); img.convert('RGB').save(out, quality=95); print(out)

if __name__ == '__main__':
    os.makedirs(P('ads/girls'), exist_ok=True)
    # source is 1536x2730
    build(1080, 1350, (0, 520, 1536, 2440), 70, 1210, 'sorry-padel-girls-pink-blue-4x5.jpg')
    build(1080, 1920, (0, 0, 1536, 2730), 260, 1560, 'sorry-padel-girls-pink-blue-9x16.jpg')
    bp = dict(src='media/baby-pink-dress-hold.jpg', sub="We're running out of Baby Pink...", wall=(40, 400, 30, 300), shift=False, wash=235)
    build(1080, 1350, (0, 250, 1125, 1656), 70, None, 'sorry-padel-girls-baby-pink-4x5.jpg', **bp)
    build(1080, 1920, (0, 0, 1125, 2000), 250, None, 'sorry-padel-girls-baby-pink-9x16.jpg', **bp)

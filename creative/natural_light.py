#!/usr/bin/env python3
"""Warm natural-light edit of the gift-box photo (IMG_0628): golden window light, soft shadows.
Outputs ads/girls/giftbox-natural-light-9x16.jpg and -4x5.jpg"""
import os, numpy as np
from PIL import Image, ImageOps, ImageFilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

def blur(a, r):
    return np.asarray(Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255

def white_box(im):
    """Recolour the black gift box white (keeps its shading); gold COVR becomes dark lettering."""
    from scipy import ndimage as nd
    a = np.asarray(im).astype(np.float32)
    L = a @ np.array([0.299, 0.587, 0.114])
    dark = L < 80
    dark[:1100] = False; dark[2200:] = False; dark[:, 1150:] = False
    lab, n = nd.label(dark); sz = nd.sum(dark, lab, range(1, n + 1))
    box = np.isin(lab, [i + 1 for i, v in enumerate(sz) if v > 20000])
    box = nd.binary_fill_holes(nd.binary_closing(box, iterations=4))
    # pick up thin dark edges/corners left next to the box
    near = nd.binary_dilation(box, iterations=26)
    box |= near & (L < 105)
    box = nd.binary_fill_holes(nd.binary_closing(box, iterations=3))
    # smooth the outline so edges stay crisp and straight, not torn
    box = blur(box.astype(np.float32), 2.5) > 0.5
    r, b = a[..., 0], a[..., 2]
    gold = box & ((r - b) > 35) & (L > 70)
    gold_s = np.clip(((r - b) - 30) / 30, 0, 1) * np.clip((L - 60) / 50, 0, 1) * box
    lo, hi = np.percentile(L[box & ~gold], [5, 97])
    norm = np.clip((L - lo) / (hi - lo), 0, 1)
    white = np.array([242, 240, 236], np.float32)
    nb = white * (0.78 + 0.24 * norm)[..., None]
    ink = np.array([46, 40, 38], np.float32)
    nb = nb * (1 - gold_s[..., None]) + ink * gold_s[..., None]
    alpha = blur(box.astype(np.float32), 1.0)[..., None]
    # soft contact shadow on the floor so the white box stands out
    sh = np.roll(box, 18, axis=0).astype(np.float32)
    sh = blur(sh, 22) * (1 - box)
    a = a * (1 - 0.30 * sh[..., None])
    out = a * (1 - alpha) + nb * alpha
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

def grade(im):
    a = np.asarray(im).astype(np.float32) / 255
    H, W = a.shape[:2]
    # 1) warm white balance (cool grey studio light -> late-afternoon sun)
    wall = a[150:700, 100:700].reshape(-1, 3).mean(0)
    a = a * (np.array([0.95, 0.925, 0.88]) / wall)
    # 2) tone: lift blacks a touch, soft S-curve, gentle highlight roll-off
    a = 0.035 + a * 0.965
    a = np.clip(a, 0, 1)
    a = a + 0.08 * (a - 0.5) * (1 - np.abs(2 * a - 1))
    l = a.mean(2, keepdims=True)
    # 3) window light: soft diagonal sun patches + window-frame shadows across the scene
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    u = (xx * 0.62 + yy * 0.78) / max(H, W)  # diagonal coordinate (light from upper left)
    beams = np.zeros((H, W), np.float32)
    for c, w in [(0.30, 0.055), (0.47, 0.04), (0.66, 0.05)]:
        beams += np.clip(1 - np.abs(u - c) / w, 0, 1) ** 0.6   # flatter-topped sun patches
    beams = np.clip(beams, 0, 1)
    v = (xx * -0.78 + yy * 0.62) / max(H, W)
    bars = (np.cos(2 * np.pi * v * 3.0) > -0.75).astype(np.float32)   # window-frame bars
    light = blur(beams * bars, 7)
    # sun lands mostly on walls/floor around the products, fading lower down
    light *= np.clip(1.25 - yy / H, 0.35, 1)[...]
    fall = np.clip(1.06 - 0.22 * ((xx / W) * 0.6 + (yy / H) * 0.4), 0.86, 1.06)
    a = a * fall[..., None] * 0.95
    sun = np.array([1.0, 0.95, 0.87])
    a = a * (1 + light[..., None] * (sun * 1.13 - 1 + 0.05))
    # 4) soft shadow side (right/bottom) cooled slightly for depth
    sh = blur(np.clip((xx / W - 0.55) * 1.5, 0, 1) * np.clip(yy / H, 0, 1), 60)
    a = a * (1 - 0.05 * sh[..., None]) + np.array([0.82, 0.80, 0.80]) * 0.05 * sh[..., None] * l
    # 5) colour: gentle vibrance for the covers, warm highlights
    l = a.mean(2, keepdims=True); sat = a.max(2, keepdims=True) - a.min(2, keepdims=True)
    a = l + (a - l) * (1 + 0.18 * np.clip(sat * 4, 0, 1))
    a = np.clip(a, 0, 1)
    out = Image.fromarray((a * 255).astype(np.uint8))
    out = out.filter(ImageFilter.UnsharpMask(radius=4, percent=22, threshold=2))
    out = out.filter(ImageFilter.UnsharpMask(radius=1.1, percent=45, threshold=2))
    # 6) bloom + fine grain
    b = np.asarray(out).astype(np.float32)
    glow = np.asarray(Image.fromarray(np.clip((b - 205) * 3, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(30))).astype(np.float32)
    b = b + glow * np.array([0.10, 0.08, 0.05])
    hl = np.clip((b.mean(2, keepdims=True) - 170) / 85, 0, 1)
    b = b * (1 - 0.10 * hl) + np.array([236, 228, 214]) * 0.10 * hl
    b = b * np.array([0.965, 0.95, 0.925])
    b += np.random.default_rng(1).normal(0, 2.2, b.shape[:2])[..., None]
    return Image.fromarray(np.clip(b, 0, 255).astype(np.uint8))

if __name__ == '__main__':
    src = ImageOps.exif_transpose(Image.open(P('media/IMG_0628.JPG'))).convert('RGB')  # 1536x2730
    src = white_box(src)
    g = grade(src)
    os.makedirs(P('ads/girls'), exist_ok=True)
    g.crop((240, 520, 1380, 2547)).resize((1080, 1920), Image.LANCZOS).save(P('ads/girls/giftbox-natural-light-9x16.jpg'), quality=95)
    g.crop((60, 700, 1476, 2470)).resize((1080, 1350), Image.LANCZOS).save(P('ads/girls/giftbox-natural-light-4x5.jpg'), quality=95)
    print('ok')

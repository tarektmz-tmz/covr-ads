# Builds the 1/3/5-bag bundle photos from one identical bag cutout.
import sys
from PIL import Image, ImageDraw, ImageFilter

S = 1200
BG_TOP, BG_BOTTOM = (251, 246, 240), (236, 224, 210)

bag = Image.open(sys.argv[1]).convert('RGBA')
bag = bag.crop(bag.getbbox())


def background():
    bg = Image.new('RGB', (S, S))
    d = ImageDraw.Draw(bg)
    for y in range(S):
        t = y / S
        d.line([(0, y), (S, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM)))
    return bg.convert('RGBA')


def place(canvas, height, cx, bottom):
    """Paste the bag scaled to `height`, centred on cx, standing on `bottom`, with a soft floor shadow."""
    w = round(bag.width * height / bag.height)
    b = bag.resize((w, height), Image.LANCZOS)
    shadow = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).ellipse([cx - w * 0.48, bottom - height * 0.035, cx + w * 0.48, bottom + height * 0.035], fill=(60, 35, 15, 90))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(height * 0.025)))
    canvas.alpha_composite(b, (round(cx - w / 2), bottom - height))


def build(layout, out):
    c = background()
    for height, cx, bottom in layout:
        place(c, height, cx, bottom)
    c.convert('RGB').save(out, quality=92)


out = sys.argv[2]
# 1 bag
build([(900, 600, 1050)], f'{out}/ceylora-bundle-1.jpg')
# 3 bags side by side; the middle one drawn last so it sits in front
build([(700, 330, 1000), (700, 870, 1000), (760, 600, 1050)], f'{out}/ceylora-bundle-3.jpg')
# 5 bags: 3 at the back, 2 in front
build([(520, 250, 780), (520, 600, 780), (520, 950, 780), (600, 410, 1100), (600, 790, 1100)], f'{out}/ceylora-bundle-5.jpg')
print('done')

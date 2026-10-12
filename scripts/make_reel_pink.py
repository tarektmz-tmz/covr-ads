#!/usr/bin/env python3
"""COVR "Padel girls" Reel: Baby Pink + Sky Denim, girly pink styling, 1080x1920.

Voiceover (Kokoro TTS), bright synthesised music, whooshes and sparkles.
Reuses helpers from make_reel2.py.  Usage: python3 scripts/make_reel_pink.py [--voice af_bella]
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_reel2 as R

W, H, FPS, SR = R.W, R.H, R.FPS, R.SR
P = R.P
ROSE = (194, 87, 122)
DEEP = (120, 44, 70)
SKYINK = (52, 86, 128)
BLUSH = ((250, 226, 232), (241, 196, 208))
SKY = ((226, 238, 250), (199, 219, 240))
F_BOLD = P('creative/fonts/Montserrat-800.ttf')
F_SANS = P('creative/fonts/Inter-500.ttf')

SHOTS = [
    ("Okay, padel girls... this one's for you.", dict(img='images/baby-pink/04_IMG_4343_JPG.jpg', a=(0.5, 0.47, 0.98), b=(0.5, 0.45, 0.74)), ['PADEL GIRLS,', "THIS ONE'S FOR YOU"], 'photo'),
    ("Baby Pink. Blush cotton twill, with white leather.", dict(pack='media/cut/pack-baby-pink.png', bg=BLUSH), ['BABY PINK', 'Blush cotton twill · white leather'], ROSE),
    ("And Sky Denim, in soft blue denim, with natural leather.", dict(pack='media/cut/pack-sky-denim.png', bg=SKY), ['SKY DENIM', 'Sky-blue denim · natural leather'], SKYINK),
    ("A gold zip, an embroidered crest, and a pocket for your phone.", dict(img='images/baby-pink/02_IMG_4346.jpg', a=(0.56, 0.60, 0.60), b=(0.50, 0.70, 0.40)), ['GOLD ZIP · CREST', 'PHONE POCKET'], 'photo'),
    ("Carry it by the handle, or on your shoulder.", dict(img='images/baby-pink/06_IMG_6008_JPG.jpg', a=(0.62, 0.55, 0.86), b=(0.73, 0.62, 0.62)), ['CARRY IT', 'YOUR WAY'], 'photo'),
    ("Plus a free matching ball pouch, with every cover.", dict(pack='media/cut/pouch-baby-pink.png', bg=BLUSH, small=True), ['+ FREE BALL POUCH', 'with every cover'], ROSE),
    ("Gift it... or keep it for yourself.", dict(img='media/IMG_0628.JPG', a=(0.5, 0.70, 0.62), b=(0.47, 0.74, 0.48)), ['GIFT IT.', 'OR KEEP IT.'], 'photo'),
    ("Twenty percent off, with code C O V twenty. Only a few left.", dict(end=True), None, None),
]

def grad(c1, c2):
    t = np.linspace(0, 1, H)[:, None, None]
    return (np.array(c1)[None, None] * (1 - t) + np.array(c2)[None, None] * t) * np.ones((1, W, 1))

def sparkles(img, t, seed, n=9, color=(255, 255, 255)):
    rng = np.random.default_rng(seed)
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(n):
        x, y = rng.uniform(80, W - 80), rng.uniform(420, 1500)
        ph = rng.uniform(0, 1); sp = rng.uniform(0.6, 1.1)
        a = max(0.0, np.sin(np.pi * ((t * sp + ph) % 1.0))) ** 3
        r = rng.uniform(10, 22) * (0.6 + 0.4 * a)
        al = int(230 * a)
        if al < 8: continue
        d.polygon([(x, y - r), (x + r * 0.22, y - r * 0.22), (x + r, y), (x + r * 0.22, y + r * 0.22), (x, y + r), (x - r * 0.22, y + r * 0.22), (x - r, y), (x - r * 0.22, y - r * 0.22)], fill=color + (al,))
    lay = lay.filter(ImageFilter.GaussianBlur(0.8))
    return Image.alpha_composite(img.convert('RGBA'), lay).convert('RGB')

def text_block(img, lines, style, alpha, y0=250):
    if not lines or alpha <= 0: return img
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    y = y0
    for i, ln in enumerate(lines):
        big = (i == 0) or style == 'photo'
        f = ImageFont.truetype(F_BOLD if big else F_SANS, 104 if (big and len(ln) < 13) else (84 if big else 46))
        w = d.textlength(ln, font=f); x = (W - w) / 2
        if style == 'photo':
            fill = (255, 255, 255, int(255 * alpha)); ds.text((x, y + 4), ln, font=f, fill=DEEP + (int(170 * alpha),))
        else:
            fill = (style if big else DEEP) + (int(255 * alpha),)
        d.text((x, y), ln, font=f, fill=fill)
        y += (f.size * 1.18) if big else 70
    sh = sh.filter(ImageFilter.GaussianBlur(9))
    out = Image.alpha_composite(img.convert('RGBA'), sh)
    return Image.alpha_composite(out, lay).convert('RGB')

def pack_frame(spec, t, dur):
    bg = grad(*spec['bg'])
    img = Image.fromarray(bg.astype(np.uint8))
    cut = Image.open(P(spec['pack'])).convert('RGBA')
    size = 820 if spec.get('small') else 1080
    s = size * (0.97 + 0.06 * R.ease(min(1, t / dur)))
    c = cut.copy(); c.thumbnail((int(s), int(s)), Image.LANCZOS)
    fy = 8 * np.sin(2 * np.pi * t / 2.6)
    x = (W - c.width) // 2; y = int(640 + (1080 - c.height) / 2 + fy)
    # soft shadow
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((W / 2 - c.width * 0.36, y + c.height - 30, W / 2 + c.width * 0.36, y + c.height + 30), fill=(120, 60, 80, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(26))
    img = Image.alpha_composite(img.convert('RGBA'), sh)
    img.alpha_composite(c, (x, y))
    return sparkles(img.convert('RGB'), t, hash(spec['pack']) % 1000)

def end_card(t):
    img = Image.fromarray(grad(*BLUSH).astype(np.uint8)).convert('RGBA')
    a = min(1, t * 2.5)
    for k, (f, dx) in enumerate([('media/cut/pack-baby-pink.png', -230), ('media/cut/pack-sky-denim.png', 230)]):
        c = Image.open(P(f)).convert('RGBA'); c.thumbnail((560, 560), Image.LANCZOS)
        fy = 6 * np.sin(2 * np.pi * (t / 2.4 + k * 0.5))
        img.alpha_composite(c, (int(W / 2 + dx - c.width / 2), int(560 + fy)))
    d = ImageDraw.Draw(img)
    def ct(y, s, f, col):
        w = d.textlength(s, font=f); d.text(((W - w) / 2, y), s, font=f, fill=col + (int(255 * a),))
    ct(260, 'BABY PINK & SKY DENIM', ImageFont.truetype(F_SANS, 44), DEEP)
    ct(330, '20% OFF', ImageFont.truetype(F_BOLD, 170), ROSE)
    ct(1170, 'CODE COV20 · UNTIL 26 OCT', ImageFont.truetype(F_BOLD, 52), DEEP)
    # pill like the brand's stock ad
    f = ImageFont.truetype(F_SANS, 44); s = 'Only a few left.'
    w = d.textlength(s, font=f)
    d.rounded_rectangle(((W - w) / 2 - 44, 1290, (W + w) / 2 + 44, 1390), radius=50, fill=(255, 255, 255, int(235 * a)))
    ct(1312, s, f, DEEP)
    ct(1450, 'padelcovr.com', ImageFont.truetype(F_SANS, 40), DEEP)
    return sparkles(img.convert('RGB'), t, 77, n=12)

# ---- bright music ----
def music(total):
    n = int(total * SR); out = np.zeros(n); t = np.arange(n) / SR
    bpm = 104; beat = 60 / bpm; bar = 4 * beat
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    chords = [[60, 64, 67, 72], [55, 59, 62, 67], [57, 60, 64, 69], [53, 57, 60, 65]]  # C G Am F
    for i in range(int(total / bar) + 1):
        ch = chords[i % 4]; s0 = i * bar
        # pad
        s = int(s0 * SR); e = min(n, int((s0 + bar + 0.5) * SR))
        if s >= n: break
        tt = np.arange(e - s) / SR; env = np.minimum(1, tt / 0.4) * np.exp(-np.maximum(0, tt - bar) * 4)
        for m in ch[:3]:
            out[s:e] += 0.025 * env * np.sin(2 * np.pi * hz(m) * tt)
        out[s:e] += 0.05 * env * np.sin(2 * np.pi * hz(ch[0] - 24) * tt)
        # pluck arpeggio in 8ths
        for j in range(8):
            m = ch[[0, 1, 2, 3, 2, 1, 2, 3][j]] + 12
            ps = int((s0 + j * beat / 2) * SR); L = int(0.45 * SR)
            if ps + L > n: break
            pt = np.arange(L) / SR
            out[ps:ps + L] += 0.06 * np.exp(-pt * 9) * (np.sin(2 * np.pi * hz(m) * pt) + 0.25 * np.sin(4 * np.pi * hz(m) * pt))
    for k in range(int(total / beat)):
        tk = k * beat
        if tk < 1.6: continue
        s = int(tk * SR); L = int(0.25 * SR)
        if s + L > n: break
        tt = np.arange(L) / SR
        if k % 2 == 0:
            f = 55 + 60 * np.exp(-tt * 35)
            out[s:s + L] += 0.2 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 12)
        else:  # soft clap
            nz = np.random.default_rng(k).normal(0, 1, L); nz = np.diff(nz, prepend=0)
            out[s:s + L] += 0.05 * nz * np.exp(-tt * 25)
    out = np.convolve(out, np.ones(4) / 4, mode='same')
    return out * np.minimum(1, t / 0.8) * np.minimum(1, (total - t) / 1.8)

def chime(dur=0.9):
    L = int(dur * SR); tt = np.arange(L) / SR; out = np.zeros(L)
    for f, d0 in [(1568, 0), (2093, 0.09), (2637, 0.18)]:
        s = int(d0 * SR); x = tt[: L - s]
        out[s:] += 0.05 * np.exp(-x * 5) * np.sin(2 * np.pi * f * x)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='af_bella')
    ap.add_argument('--out', default=P('ads/reel/covr-reel-padel-girls.mp4'))
    args = ap.parse_args()
    import soundfile as sf
    from kokoro_onnx import Kokoro
    tmp = tempfile.mkdtemp(prefix='reelpink_')
    k = Kokoro('/root/kokoro/kokoro-v1.0.onnx', '/root/kokoro/voices-v1.0.bin')
    vo, lens = [], []
    for i, (line, *_r) in enumerate(SHOTS):
        a, sr = k.create(line, voice=args.voice, speed=1.0, lang='en-us')
        f = os.path.join(tmp, f'vo{i}.wav'); sf.write(f, a, sr); vo.append(f); lens.append(len(a) / sr)
    lead = 0.3
    durs = [lead + L + (1.8 if SHOTS[i][1].get('end') else 0.55) for i, L in enumerate(lens)]
    starts = np.cumsum([0] + durs[:-1]); total = float(sum(durs))
    print('total', round(total, 2))
    fd = os.path.join(tmp, 'f'); os.makedirs(fd)
    XF = 6; idx = 0; tail = None; stills = []
    for si, ((line, spec, lines, style), dur) in enumerate(zip(SHOTS, durs)):
        nf = int(round(dur * FPS))
        kb = R.KenBurns(spec['img'], spec['a'], spec['b']) if 'img' in spec else None
        if kb:
            kb.im.thumbnail((2600, 2600), Image.LANCZOS)
        buf = []
        for i in range(nf):
            t = i / FPS
            if kb:
                img = kb.frame(i / max(1, nf - 1))
                arr = np.asarray(img).astype(np.float32)
                arr = arr * 0.93 + np.array([22, 8, 14])  # soft pink lift
                # top gradient for text
                g = np.clip(1 - np.linspace(0, 1, H) / 0.38, 0, 1)[:, None, None] ** 1.5
                arr = arr * (1 - 0.32 * g) + np.array([120, 44, 70]) * 0.32 * g
                img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
            elif spec.get('end'):
                img = end_card(t)
            else:
                img = pack_frame(spec, t, dur)
            if lines:
                ta = min(1, i / 8) * min(1, (nf - i) / 6)
                img = text_block(img, lines, style, ta)
            if tail is not None and i < XF:
                img = Image.blend(tail[i], img, (i + 1) / (XF + 1))
            if si < len(SHOTS) - 1 and i >= nf - XF:
                buf.append(img)
                if i == nf - 1: tail = buf
                continue
            img.save(os.path.join(fd, f'{idx:05d}.jpg'), quality=95); idx += 1
            if i == nf // 2: stills.append(img)
    total_v = idx / FPS
    n = int(total_v * SR)
    v = np.zeros(n)
    for f, s in zip(vo, starts):
        a, sr = sf.read(f)
        if sr != SR: a = np.interp(np.arange(int(len(a) * SR / sr)) * sr / SR, np.arange(len(a)), a)
        i0 = int((s + lead) * SR); a = a[: max(0, n - i0)]; v[i0:i0 + len(a)] += a
    m = music(total_v)
    env = np.convolve(np.abs(v), np.ones(int(0.25 * SR)) / int(0.25 * SR), mode='same')
    mix = v + m * (1 - 0.5 * np.clip(env / 0.02, 0, 1))
    w = R.whoosh(0.45)
    for c in starts[1:]:
        i0 = int((c - 0.22) * SR)
        if i0 + len(w) < n: mix[i0:i0 + len(w)] += w * 0.8
    ch = chime()
    for si, (_, spec, _, _) in enumerate(SHOTS):
        if 'pack' in spec or spec.get('end'):
            i0 = int((starts[si] + 0.15) * SR)
            if i0 + len(ch) < n: mix[i0:i0 + len(ch)] += ch
    mix = mix / np.abs(mix).max() * 0.89
    wav = os.path.join(tmp, 'mix.wav'); sf.write(wav, np.stack([mix, mix], 1), SR)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(fd, '%05d.jpg'), '-i', wav,
                    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k',
                    '-shortest', '-movflags', '+faststart', args.out], check=True)
    print('wrote', args.out, idx)

if __name__ == '__main__':
    main()

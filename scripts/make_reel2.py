#!/usr/bin/env python3
"""COVR Reel v2: 1080x1920 product film with voiceover, music and sound effects.

Real 4K footage + full-resolution studio/lifestyle photos (no heavy upscaling),
Kokoro TTS voiceover (local model in /root/kokoro), synthesised music + SFX.
Usage: python3 scripts/make_reel2.py [--voice af_heart] [--out ads/reel/covr-reel-v2.mp4] [--stills]
"""
import argparse, json, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter

W, H, FPS, SR = 1080, 1920, 30, 48000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
CREAM = (245, 240, 230)
FONT_SERIF = P('creative/fonts/InstrumentSerif-400.ttf')
FONT_SANS = P('creative/fonts/Inter-500.ttf')
CLIP = P('media/latte-clip-IMG_1681.mov')

# (voiceover line, caption, shot spec)
SHOTS = [
    ("Your racket goes everywhere you go.", "Everywhere you go.", dict(clip=(0.2, None))),
    ("Give it something worth carrying.", "Worth carrying.", dict(img='media/coffee-mocha-steps-edited-full.jpg', a=(0.5, 0.60, 0.80), b=(0.5, 0.64, 0.62))),
    ("Handmade in Bali, in cotton, with leather piping all around the edge.", "Handmade in Bali", dict(img='images/latte/02_KEV0489.jpg', a=(0.47, 0.50, 0.78), b=(0.50, 0.55, 0.56))),
    ("An embroidered crest on the front.", "Embroidered crest", dict(img='images/latte/01_4.jpg', a=(0.5, 0.60, 0.62), b=(0.5, 0.76, 0.34))),
    ("A front pocket for your phone and keys.", "Front zip pocket", dict(img='images/latte/05_KEV0100.jpg', a=(0.48, 0.48, 0.74), b=(0.50, 0.40, 0.56))),
    ("A thirty-six centimetre zip that follows the curve.", "36 cm zip around the curve", dict(img='images/mocha/06_KEV0199.jpg', a=(0.60, 0.42, 0.58), b=(0.55, 0.50, 0.76), sfx='zip')),
    ("The grip stays out, above a leather collar.", "Grip out. Leather collar.", dict(img='images/latte/04_KEV0093.jpg', a=(0.33, 0.36, 0.62), b=(0.30, 0.31, 0.50))),
    ("Carry it by the handle, or on the shoulder strap.", "Handle or shoulder strap", dict(clip=(3.6, None))),
    ("Ten colourways. And a free ball pouch with every cover.", None, dict(colours=True)),
    ("Cover. Twenty percent off with code C O V twenty, until the twenty-sixth of October.", None, dict(end=True)),
]
COLOURS = ['navy', 'ginger', 'total-black', 'baby-pink', 'ash', 'latte', 'sky-denim', 'coffee', 'vanilla-cream', 'mocha']

def ease(t):
    return t * t * (3 - 2 * t)

def font(path, size):
    return ImageFont.truetype(path, size)

def caption(img, text, alpha=1.0, y=1270, size=88):
    if not text or alpha <= 0:
        return img
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font(FONT_SERIF, size)
    w = d.textlength(text, font=f)
    x = (W - w) / 2
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x, y + 3), text, font=f, fill=(0, 0, 0, int(150 * alpha)))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    d.text((x, y), text, font=f, fill=CREAM + (int(255 * alpha),))
    out = Image.alpha_composite(img.convert('RGBA'), sh)
    return Image.alpha_composite(out, lay).convert('RGB')

def vignette():
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.75)) ** 2)
    v = 1 - 0.28 * np.clip(r - 0.35, 0, 1) ** 1.5
    g = np.clip((yy - H * 0.55) / (H * 0.45), 0, 1) ** 1.6  # darken lower area for captions
    return (v * (1 - 0.38 * g))[..., None]
VIG = None

def grade(arr):
    return np.clip(arr * VIG, 0, 255)

class KenBurns:
    def __init__(self, path, a, b):
        im = ImageOps.exif_transpose(Image.open(P(path))).convert('RGB')
        self.im = im
        self.a, self.b = a, b
    def frame(self, t):
        cx = self.a[0] + (self.b[0] - self.a[0]) * ease(t)
        cy = self.a[1] + (self.b[1] - self.a[1]) * ease(t)
        h = self.a[2] + (self.b[2] - self.a[2]) * ease(t)
        IW, IH = self.im.size
        ch = h * IH
        cw = ch * W / H
        if cw > IW:
            cw = IW; ch = cw * H / W
        x0 = min(max(cx * IW - cw / 2, 0), IW - cw)
        y0 = min(max(cy * IH - ch / 2, 0), IH - ch)
        return self.im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))

def clip_frames(start, n, tmp):
    d = os.path.join(tmp, f'clip_{start}')
    os.makedirs(d, exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(start), '-i', CLIP, '-frames:v', str(n),
                    '-vf', f'fps={FPS},scale={W}:{H}:flags=lanczos', '-q:v', '2', os.path.join(d, '%04d.jpg')], check=True)
    fs = sorted(os.listdir(d))
    return [os.path.join(d, f) for f in fs]

def colour_frames(n_total):
    """Quick cut through the 10 colourways, then the pouch photo."""
    packs = []
    for c in COLOURS:
        im = Image.open(P('media/packshots', c + '.jpg')).convert('RGB')
        im = ImageOps.fit(im, (1500, 1500))
        bg = Image.new('RGB', (W, H), (238, 233, 224))
        im = im.resize((1240, 1240), Image.LANCZOS)
        bg.paste(im, ((W - 1240) // 2, 300))
        packs.append(bg)
    per = 7  # frames per colour
    pouch = KenBurns('media/latte-pouch-front.jpg', (0.5, 0.52, 0.96), (0.58, 0.55, 0.78))
    n_pack = per * len(packs)
    out = []
    for i in range(n_total):
        if i < n_pack:
            img = packs[i // per]
            out.append(('pack', img, '10 colourways'))
        else:
            t = (i - n_pack) / max(1, n_total - n_pack - 1)
            out.append(('pouch', pouch.frame(t), 'Free ball pouch with every cover'))
    return out, n_pack

def end_card(t):
    img = Image.new('RGB', (W, H), (18, 15, 13))
    d = ImageDraw.Draw(img)
    a = min(1, t * 3)
    col = lambda c, k=1.0: tuple(int(18 + (v - 18) * a * k) for v in c)
    pk = Image.open(P('media/packshots/latte.jpg')).convert('RGB').resize((760, 760), Image.LANCZOS)
    m = Image.new('L', pk.size, 0)
    ImageDraw.Draw(m).ellipse((0, 0, 760, 760), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(60))
    s = 0.96 + 0.04 * ease(min(1, t))
    pk2 = pk.resize((int(760 * s), int(760 * s)), Image.LANCZOS)
    m2 = m.resize(pk2.size)
    dark = Image.new('RGB', pk2.size, (18, 15, 13))
    pk2 = Image.composite(pk2, dark, m2)
    pk2 = Image.blend(dark, pk2, a)
    img.paste(pk2, ((W - pk2.width) // 2, 330))
    f1 = font(FONT_SERIF, 150); f2 = font(FONT_SANS, 40); f3 = font(FONT_SERIF, 74); f4 = font(FONT_SANS, 34)
    def ctext(y, s, f, c):
        w = d.textlength(s, font=f); d.text(((W - w) / 2, y), s, font=f, fill=c)
    ctext(150, 'COVR', f1, col(CREAM))
    ctext(1150, '$249', f3, col((150, 140, 128)))
    w = d.textlength('$249', font=f3); d.line(((W - w) / 2 - 6, 1198, (W + w) / 2 + 6, 1198), fill=col((150, 140, 128)), width=4)
    ctext(1245, '20% off with code COV20', f3, col(CREAM))
    ctext(1360, 'UNTIL 26 OCTOBER', f2, col((200, 170, 120)))
    ctext(1440, 'padelcovr.com', f4, col((200, 192, 180)))
    return img

# ---------------- audio -----------------
def tone(freq, dur, sr=SR):
    t = np.arange(int(dur * sr)) / sr
    return t, freq

def music(total):
    n = int(total * SR); t = np.arange(n) / SR
    out = np.zeros(n)
    bpm = 84; beat = 60 / bpm
    chords = [[57, 60, 64, 69], [53, 57, 60, 65], [48, 52, 55, 60], [55, 59, 62, 67]]  # Am F C G
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    bar = beat * 4
    for i in range(int(total / bar) + 1):
        ch = chords[i % 4]; s = int(i * bar * SR); e = min(n, int((i + 1) * bar * SR) + int(0.6 * SR))
        if s >= n: break
        tt = np.arange(e - s) / SR
        env = np.minimum(1, tt / 0.8) * np.exp(-np.maximum(0, tt - bar) * 3)
        for m in ch:
            f = hz(m)
            out[s:e] += 0.05 * env * (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt + 0.3) + 0.12 * np.sin(2 * np.pi * 3 * f * tt))
        # soft bass
        fb = hz(ch[0] - 12)
        out[s:e] += 0.07 * env * np.sin(2 * np.pi * fb * tt)
    # soft kick + muted hat after the intro
    for k in range(int(total / beat)):
        tk = k * beat
        if tk < 2.0: continue
        s = int(tk * SR); L = int(0.35 * SR)
        if s + L > n: break
        tt = np.arange(L) / SR
        f = 50 + 70 * np.exp(-tt * 30)
        out[s:s + L] += 0.22 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 9)
        sh = int((tk + beat / 2) * SR); Lh = int(0.06 * SR)
        if sh + Lh < n:
            nz = np.random.default_rng(k).normal(0, 1, Lh)
            nz = np.diff(nz, prepend=0)
            out[sh:sh + Lh] += 0.025 * nz * np.exp(-np.arange(Lh) / SR * 60)
    # gentle low-pass via moving average for warmth
    k = np.ones(6) / 6
    out = np.convolve(out, k, mode='same')
    fade = np.minimum(1, t / 1.0) * np.minimum(1, (total - t) / 2.0)
    return out * fade

def whoosh(dur=0.5):
    L = int(dur * SR); tt = np.arange(L) / SR
    nz = np.random.default_rng(7).normal(0, 1, L)
    # sweep: progressively wider moving average = falling cutoff
    out = np.zeros(L)
    for i, w in enumerate(np.linspace(2, 40, 8)):
        seg = slice(i * L // 8, (i + 1) * L // 8)
        out[seg] = np.convolve(nz, np.ones(int(w)) / int(w), mode='same')[seg]
    env = np.sin(np.pi * tt / dur) ** 2
    return 0.18 * out * env

def zip_sound(dur=1.2):
    L = int(dur * SR); out = np.zeros(L); rng = np.random.default_rng(3)
    t = 0.0
    while t < dur - 0.02:
        s = int(t * SR); l = int(0.008 * SR)
        out[s:s + l] += rng.normal(0, 1, l) * np.exp(-np.arange(l) / SR * 400)
        t += 0.011 + 0.006 * rng.random()
    env = np.minimum(1, np.arange(L) / SR / 0.1) * np.minimum(1, (dur - np.arange(L) / SR) / 0.2)
    return 0.12 * np.convolve(out * env, [0.5, 0.5], mode='same')

def mix_audio(vo_files, starts, cuts, zip_at, total, out_wav):
    import soundfile as sf
    n = int(total * SR)
    vo = np.zeros(n)
    for f, s in zip(vo_files, starts):
        a, sr = sf.read(f)
        if a.ndim > 1: a = a.mean(1)
        if sr != SR:
            a = np.interp(np.arange(int(len(a) * SR / sr)) * sr / SR, np.arange(len(a)), a)
        i = int(s * SR); a = a[: max(0, n - i)]
        vo[i:i + len(a)] += a * 0.95
    mus = music(total)
    # duck music under voice
    env = np.convolve(np.abs(vo), np.ones(int(0.25 * SR)) / int(0.25 * SR), mode='same')
    duck = 1 - 0.55 * np.clip(env / 0.02, 0, 1)
    sfx = np.zeros(n)
    w = whoosh()
    for c in cuts:
        i = int((c - 0.25) * SR)
        if 0 <= i and i + len(w) < n: sfx[i:i + len(w)] += w
    if zip_at is not None:
        z = zip_sound(); i = int(zip_at * SR); sfx[i:i + len(z)] += z[: n - i]
    mixd = vo + mus * duck * 0.9 + sfx
    mixd = mixd / max(1e-6, np.abs(mixd).max()) * 0.89
    sf.write(out_wav, np.stack([mixd, mixd], 1), SR)

# ---------------- main -----------------
def main():
    global VIG
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='af_heart')
    ap.add_argument('--out', default=P('ads/reel/covr-reel-v2.mp4'))
    ap.add_argument('--stills', action='store_true')
    args = ap.parse_args()
    VIG = vignette()
    tmp = tempfile.mkdtemp(prefix='reel2_')

    from kokoro_onnx import Kokoro
    import soundfile as sf
    k = Kokoro('/root/kokoro/kokoro-v1.0.onnx', '/root/kokoro/voices-v1.0.bin')
    vo_files, vo_lens = [], []
    for i, (line, _, _) in enumerate(SHOTS):
        a, sr = k.create(line, voice=args.voice, speed=0.92, lang='en-us')
        f = os.path.join(tmp, f'vo{i}.wav'); sf.write(f, a, sr)
        vo_files.append(f); vo_lens.append(len(a) / sr)

    lead = 0.35
    durs = []
    for i, L in enumerate(vo_lens):
        extra = 0.75
        if SHOTS[i][2].get('colours'): extra = 1.0
        if SHOTS[i][2].get('end'): extra = 1.6
        durs.append(lead + L + extra)
    starts = np.cumsum([0] + durs[:-1])
    total = float(sum(durs))
    print('total', round(total, 2), 's')

    frames_dir = os.path.join(tmp, 'frames'); os.makedirs(frames_dir)
    XF = 8  # crossfade frames
    prev_tail = None
    idx = 0
    stills = []
    zip_at = None
    for si, ((line, cap, spec), dur, st) in enumerate(zip(SHOTS, durs, starts)):
        nf = int(round(dur * FPS))
        if spec.get('sfx') == 'zip': zip_at = st + lead + 0.4
        if 'clip' in spec:
            fs = clip_frames(spec['clip'][0], nf, tmp)
            get = lambda i, fs=fs: Image.open(fs[min(i, len(fs) - 1)]).convert('RGB')
        elif 'img' in spec:
            kb = KenBurns(spec['img'], spec['a'], spec['b'])
            get = lambda i, kb=kb, nf=nf: kb.frame(i / max(1, nf - 1))
        elif spec.get('colours'):
            cf, n_pack = colour_frames(nf)
            get = lambda i, cf=cf: cf[i][1]
        else:
            get = lambda i, nf=nf: end_card(i / FPS)
        for i in range(nf):
            img = get(i)
            arr = np.asarray(img).astype(np.float32)
            if not spec.get('end'):
                arr = grade(arr)
            img = Image.fromarray(arr.astype(np.uint8))
            c = cap
            if spec.get('colours'):
                c = cf[i][2]
            if c:
                ta = min(1, i / 10) * min(1, (nf - i) / 8)
                img = caption(img, c, ta, size=84 if len(c) > 20 else 96)
            if prev_tail is not None and i < XF:
                a = (i + 1) / (XF + 1)
                img = Image.blend(prev_tail[i], img, a)
            if i >= nf - XF and si < len(SHOTS) - 1:
                prev_tail_buf = prev_tail_buf if i > nf - XF else []
                prev_tail_buf.append(img)
                if i == nf - 1: prev_tail = prev_tail_buf
                continue  # tail frames are blended into the next shot
            img.save(os.path.join(frames_dir, f'{idx:05d}.jpg'), quality=95); idx += 1
            if i == nf // 2: stills.append(img)
        if si == len(SHOTS) - 1:
            pass
    wav = os.path.join(tmp, 'mix.wav')
    cuts = list(starts[1:])
    mix_audio(vo_files, [s + lead for s in starts], cuts, zip_at, idx / FPS, wav)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(frames_dir, '%05d.jpg'), '-i', wav,
                    '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
                    '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', args.out], check=True)
    if args.stills:
        sd = os.path.splitext(args.out)[0] + '-stills'; os.makedirs(sd, exist_ok=True)
        for i, s in enumerate(stills): s.save(os.path.join(sd, f'{i:02d}.jpg'), quality=88)
    print('wrote', args.out, idx, 'frames')

if __name__ == '__main__':
    main()

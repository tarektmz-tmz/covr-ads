"""Generate unbranded Bali loft Instagram stories (1080x1920) as HTML, render with Chromium."""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
CHROME = "/opt/pw-browsers/chromium"

CSS = """
@font-face { font-family: 'Play'; font-weight: 400; src: url('fonts/Playfair-Regular.ttf'); }
@font-face { font-family: 'Play'; font-weight: 500; src: url('fonts/Playfair-Medium.ttf'); }
@font-face { font-family: 'Play'; font-style: italic; src: url('fonts/Playfair-Italic.ttf'); }
@font-face { font-family: 'Inter'; font-weight: 400; src: url('file:///usr/share/fonts/opentype/inter/Inter-Regular.otf'); }
@font-face { font-family: 'Inter'; font-weight: 500; src: url('file:///usr/share/fonts/opentype/inter/Inter-Medium.otf'); }
@font-face { font-family: 'Inter'; font-weight: 600; src: url('file:///usr/share/fonts/opentype/inter/Inter-SemiBold.otf'); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; }
body { background: #F1EBE1; color: #1E1712; font-family: 'Inter', sans-serif; font-variant-numeric: lining-nums; -webkit-font-smoothing: antialiased; }
.story { position: relative; width: 1080px; height: 1920px; }
.top { position: absolute; top: 205px; left: 64px; right: 64px; display: flex; justify-content: space-between; font-weight: 500; font-size: 24px; letter-spacing: 0.2em; text-transform: uppercase; color: #5E5248; }
figure { position: absolute; left: 64px; top: 270px; width: 952px; height: 1060px; background-size: cover; background-repeat: no-repeat; }
.kicker { position: absolute; left: 64px; top: 1378px; font-weight: 500; font-size: 24px; letter-spacing: 0.18em; color: #5E5248; text-transform: uppercase; }
h1 { position: absolute; left: 62px; top: 1420px; font-family: 'Play'; font-weight: 500; font-size: 96px; line-height: 1.05; }
.tag { position: absolute; left: 64px; top: 1546px; font-size: 38px; line-height: 1.35; color: #3A2F27; }

/* finale */
.dark { background: #17110D; color: #F4EEE6; }
.dark .top, .dark .label { color: #C9BCA9; }
.hero { position: absolute; left: 0; top: 0; width: 1080px; height: 760px; background-size: cover; background-position: 50% 60%; opacity: 0.38; }
.hero::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(23,17,13,0.6) 0%, rgba(23,17,13,0.25) 35%, #17110D 100%); }
.label { font-weight: 500; font-size: 24px; letter-spacing: 0.18em; text-transform: uppercase; }
.price { position: absolute; left: 64px; top: 300px; }
.price .amt { font-family: 'Play'; font-weight: 500; font-size: 170px; line-height: 1.05; margin-top: 10px; }
.price .sub { font-weight: 500; font-size: 27px; letter-spacing: 0.08em; text-transform: uppercase; margin-top: 18px; color: #EDE4D8; }
.plan { position: absolute; left: 64px; right: 64px; top: 680px; }
.plan .head { padding-bottom: 20px; border-bottom: 1px solid #5A4B3F; color: #F4EEE6; }
.row { display: flex; align-items: center; height: 80px; border-bottom: 1px solid #33281F; font-variant-numeric: tabular-nums lining-nums; }
.row .st { flex: 1; font-size: 34px; }
.row .st small { font-size: 22px; color: #A99A86; margin-left: 12px; }
.row .pc { width: 120px; text-align: right; font-weight: 500; font-size: 30px; color: #D6B98C; }
.row .am { width: 230px; text-align: right; font-weight: 600; font-size: 36px; }
.row.total { border-bottom: none; height: 92px; }
.row.total .st { font-weight: 600; font-size: 38px; }
.row.total .am { font-size: 40px; }
.extra { position: absolute; left: 64px; right: 64px; top: 1440px; padding: 26px 30px; border: 1px solid #5A4B3F; display: flex; justify-content: space-between; align-items: center; }
.extra .t { font-weight: 600; font-size: 32px; }
.extra .d { font-size: 22px; color: #C9BCA9; margin-top: 10px; }
.extra .v { font-weight: 600; font-size: 40px; color: #D6B98C; }
.cta { position: absolute; left: 64px; right: 64px; top: 1600px; display: flex; justify-content: space-between; align-items: baseline; }
.cta .t { font-family: 'Play'; font-style: italic; font-size: 40px; }
.cta .w { font-weight: 600; font-size: 26px; letter-spacing: 0.12em; text-transform: uppercase; color: #D6B98C; }
"""

PHOTO_STORIES = [
    dict(cls="cover", img="exterior.jpg", pos="62% 50%", kicker="One-bedroom loft &nbsp;·&nbsp; Bali",
         title="Tropical Loft Living", tag="A private one-bedroom loft<br>with its own pool and garden."),
    dict(cls="", img="living.jpg", pos="52% 50%", kicker="01 &nbsp;·&nbsp; Living room",
         title="Light &amp; Ease", tag="Designed around light,<br>proportion and ease."),
    dict(cls="", img="bedroom.jpg", pos="34% 50%", kicker="02 &nbsp;·&nbsp; The bedroom",
         title="The Retreat", tag="A private retreat above<br>the rhythm of the island."),
    dict(cls="", img="bathroom.jpg", pos="64% 50%", kicker="03 &nbsp;·&nbsp; The bathroom",
         title="The Ritual", tag="Designed around ritual,<br>light and natural texture."),
]

PLAN = [
    ("Reservation", "", "10%", "$17,000"),
    ("Land transfer", "Ownership", "30%", "$51,000"),
    ("Construction start", "", "25%", "$42,500"),
    ("Month 4", "Milestone", "11%", "$18,700"),
    ("Month 7", "Milestone", "11%", "$18,700"),
    ("Month 10", "Milestone", "10%", "$17,000"),
    ("Month 14", "Handover", "3%", "$5,100"),
]

TOTAL = len(PHOTO_STORIES) + 1


def page(body, cls=""):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>' \
           f'<body class="{cls}"><div class="story">{body}</div></body></html>'


def photo_story(i, s):
    body = f"""<div class="top"><span>Bali &nbsp;·&nbsp; For sale</span><span>0{i} / 0{TOTAL}</span></div>
<figure style="background-image:url('src/{s['img']}'); background-position:{s['pos']}"></figure>
<div class="kicker">{s['kicker']}</div>
<h1>{s['title']}</h1><p class="tag">{s['tag']}</p>"""
    return page(body, s["cls"])


def price_story():
    rows = "".join(
        f'<div class="row"><div class="st">{name}'
        f'{f"<small>{note}</small>" if note else ""}</div><div class="pc">{pc}</div><div class="am">{am}</div></div>'
        for name, note, pc, am in PLAN)
    body = f"""<div class="hero" style="background-image:url('src/aerial.jpg')"></div>
<div class="top"><span>Bali &nbsp;·&nbsp; For sale</span><span>0{TOTAL} / 0{TOTAL}</span></div>
<div class="price"><div class="label">Purchase price</div><div class="amt">$170,000</div>
<div class="sub">30 + 30 year leasehold &nbsp;·&nbsp; Land included</div></div>
<div class="plan"><div class="head label">14-month payment plan</div>{rows}
</div>
<div class="extra"><div><div class="t">Rental-ready package</div>
<div class="d">Furniture &amp; decor · TV · Kitchen appliances</div></div><div class="v">+$10,000</div></div>
<div class="cta"><div class="t">Private viewings by appointment</div><div class="w">DM for details</div></div>"""
    return page(body, "dark")


def render(name, html):
    path = os.path.join(HERE, name + ".html")
    with open(path, "w") as f:
        f.write(html)
    png = os.path.join(OUT, name + ".png")
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", "--window-size=1080,1920", "--virtual-time-budget=3000",
                    f"--screenshot={png}", "file://" + path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return png


if __name__ == "__main__":
    for i, s in enumerate(PHOTO_STORIES, 1):
        print(render(f"story-0{i}", photo_story(i, s)))
    print(render(f"story-0{TOTAL}", price_story()))

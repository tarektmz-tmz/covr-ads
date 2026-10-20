"""Generate Cemagi Atelier Instagram stories (1080x1920) as HTML, render with Chromium."""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
CHROME = "/opt/pw-browsers/chromium"

CSS = """
@font-face { font-family: 'Italiana'; src: url('fonts/Italiana.ttf'); }
@font-face { font-family: 'Corm'; font-style: italic; src: url('fonts/CormorantItalic.ttf'); }
@font-face { font-family: 'InterL'; src: url('file:///usr/share/fonts/opentype/inter/Inter-Light.otf'); }
@font-face { font-family: 'InterR'; src: url('file:///usr/share/fonts/opentype/inter/Inter-Regular.otf'); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; }
body { background: #F1EBE1; color: #1E1712; font-family: 'Italiana', serif; -webkit-font-smoothing: antialiased; }
.story { position: relative; width: 1080px; height: 1920px; }
.logo { position: absolute; top: 196px; left: 64px; font-family: 'Italiana'; font-size: 40px; line-height: 0.95; letter-spacing: 0.02em; }
.logo span { display: block; padding-left: 64px; }
.count { position: absolute; top: 214px; right: 64px; font-family: 'InterR'; font-size: 21px; letter-spacing: 0.34em; color: #7A6E62; }
figure { position: absolute; left: 64px; top: 310px; width: 952px; height: 1040px; background-size: cover; background-repeat: no-repeat; }
.kicker { position: absolute; left: 64px; top: 1400px; font-family: 'InterR'; font-size: 21px; letter-spacing: 0.34em; color: #7A6E62; text-transform: uppercase; }
h1 { position: absolute; left: 60px; top: 1438px; font-weight: 400; font-size: 100px; line-height: 1; letter-spacing: 0.01em; text-transform: uppercase; }
.tag { position: absolute; left: 64px; top: 1560px; font-family: 'Corm'; font-style: italic; font-size: 44px; line-height: 1.15; color: #3A2F27; }
.rule { position: absolute; right: 64px; top: 1413px; width: 300px; height: 1px; background: #CFC6BA; }

/* cover */
.cover h1 { font-size: 118px; top: 1418px; }
.cover .tag { top: 1556px; }

/* finale */
.dark { background: #17110D; color: #F1EBE1; }
.dark .count, .dark .kicker, .dark .label { color: #A99A86; }
.hero { position: absolute; left: 0; top: 0; width: 1080px; height: 760px; background-size: cover; background-position: 50% 60%; opacity: 0.42; }
.hero::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(23,17,13,0.55) 0%, rgba(23,17,13,0.2) 35%, #17110D 100%); }
.label { font-family: 'InterR'; font-size: 21px; letter-spacing: 0.34em; text-transform: uppercase; }
.price { position: absolute; left: 64px; top: 330px; }
.price .amt { font-size: 196px; line-height: 1; margin-top: 18px; letter-spacing: 0.005em; }
.price .sub { font-family: 'InterL'; font-size: 23px; letter-spacing: 0.2em; text-transform: uppercase; margin-top: 22px; color: #E3D9CB; }
.plan { position: absolute; left: 64px; right: 64px; top: 700px; }
.plan .head { display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 20px; border-bottom: 1px solid #4A3D33; }
.row { display: flex; align-items: baseline; height: 76px; border-bottom: 1px solid #2E241D; padding-top: 18px; }
.row .n { width: 62px; font-family: 'InterR'; font-size: 19px; letter-spacing: 0.12em; color: #8C7D6B; }
.row .st { flex: 1; font-size: 37px; }
.row .st small { font-family: 'InterL'; font-size: 18px; letter-spacing: 0.2em; color: #8C7D6B; text-transform: uppercase; margin-left: 14px; }
.row .pc { width: 110px; text-align: right; font-family: 'InterL'; font-size: 24px; color: #C9B08A; }
.row .am { width: 210px; text-align: right; font-size: 39px; }
.row.total { border-bottom: none; height: 84px; }
.row.total .st, .row.total .am { font-size: 44px; }
.extra { position: absolute; left: 64px; right: 64px; top: 1418px; padding: 26px 30px; border: 1px solid #4A3D33; display: flex; justify-content: space-between; align-items: center; }
.extra .t { font-size: 34px; }
.extra .d { font-family: 'InterL'; font-size: 18px; letter-spacing: 0.16em; text-transform: uppercase; color: #A99A86; margin-top: 10px; }
.extra .v { font-size: 50px; color: #C9B08A; }
.cta { position: absolute; left: 64px; right: 64px; top: 1580px; display: flex; justify-content: space-between; align-items: baseline; }
.cta .t { font-family: 'Corm'; font-style: italic; font-size: 42px; }
.cta .w { font-family: 'InterR'; font-size: 22px; letter-spacing: 0.16em; color: #E3D9CB; }
"""

PHOTO_STORIES = [
    dict(cls="cover", img="exterior.jpg", pos="62% 50%", kicker="One bedroom loft &nbsp;·&nbsp; Cemagi, Bali",
         title="Cemagi Atelier", tag="A private one-bedroom loft<br>in the heart of Cemagi."),
    dict(cls="", img="living.jpg", pos="52% 50%", kicker="01 &nbsp;·&nbsp; Living room",
         title="Light &amp; Ease", tag="Designed around light,<br>proportion and ease."),
    dict(cls="", img="bedroom.jpg", pos="34% 50%", kicker="02 &nbsp;·&nbsp; The bedroom",
         title="The Retreat", tag="A private retreat above<br>the rhythm of Cemagi."),
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

LOGO = '<div class="logo">CEMAGI<span>ATELIER</span></div>'
TOTAL = len(PHOTO_STORIES) + 1


def page(body, cls=""):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>' \
           f'<body class="{cls}"><div class="story">{body}</div></body></html>'


def photo_story(i, s):
    body = f"""{LOGO}<div class="count">0{i} / 0{TOTAL}</div>
<figure style="background-image:url('src/{s['img']}'); background-position:{s['pos']}"></figure>
<div class="kicker">{s['kicker']}</div><div class="rule"></div>
<h1>{s['title']}</h1><p class="tag">{s['tag']}</p>"""
    return page(body, s["cls"])


def price_story():
    rows = "".join(
        f'<div class="row"><div class="n">0{k}</div><div class="st">{name}'
        f'{f"<small>{note}</small>" if note else ""}</div><div class="pc">{pc}</div><div class="am">{am}</div></div>'
        for k, (name, note, pc, am) in enumerate(PLAN, 1))
    body = f"""<div class="hero" style="background-image:url('src/aerial.jpg')"></div>
{LOGO}<div class="count">0{TOTAL} / 0{TOTAL}</div>
<div class="price"><div class="label">Purchase price</div><div class="amt">$170,000</div>
<div class="sub">30 + 30 year leasehold &nbsp;·&nbsp; Land included</div></div>
<div class="plan"><div class="head"><div class="label" style="color:#E3D9CB">14-month payment plan</div>
<div class="label">Construction period</div></div>{rows}
<div class="row total"><div class="n"></div><div class="st">Total</div><div class="pc">100%</div><div class="am">$170,000</div></div></div>
<div class="extra"><div><div class="t">Rental-ready package</div>
<div class="d">Decoration · Interior · TV · Kitchen appliances</div></div><div class="v">+$10,000</div></div>
<div class="cta"><div class="t">Private viewings by appointment</div><div class="w">WA +62 822 6631 9896</div></div>"""
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

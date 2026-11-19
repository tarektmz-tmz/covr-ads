#!/usr/bin/env python3
"""Round 4 story system: Inter + the store palette (navy, gold, cream), website look, big readable type.
 - 6 AVAILABLE NOW styles, ONE style per day (full watch inside the frame, 'Full set' line on every Rolex story)
 - urgency overlays (demand = rare, only-one = OFF by default)
 - 43 KNOWLEDGE stories in 10 layouts (website look)
Run: NODE_PATH=/opt/node22/lib/node_modules python3 build_v4.py  (previews)   |  python3 build_v4.py library  (all 43 knowledge stories)
Safe zone: key content stays inside y 250 to 1580 (urgency adds a 70 px shift, so layouts end by y 1510)."""
import json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
TPL, PRE, LIB = ROOT / "templates", ROOT / "previews", ROOT / "library"
for d in (TPL, PRE, LIB):
    d.mkdir(exist_ok=True)

NAVY, NAVY2, GOLD, GOLDL, CREAM, INK, MUT = "#0b1a33", "#112448", "#c9a24b", "#e3c47a", "#f6f2ea", "#16181d", "#5d6370"
FULLSET = "Full set: official Rolex box, papers and tag"
LEGAL_R = "Independent dealer · Not affiliated with Rolex · WhatsApp in bio"
LEGAL_P = "Independent dealer · Not affiliated with the brand · WhatsApp in bio"

CSS = """
@font-face{font-family:'Inter';src:url('../fonts/Inter.ttf');font-weight:100 900;font-style:normal}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000}
#s{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Inter',sans-serif;color:CREAM;letter-spacing:-.01em}
.a{position:absolute}.c{left:0;right:0;text-align:center}
.bar{position:absolute;height:10px;background:linear-gradient(90deg,GOLD,GOLDL);border-radius:6px}
.legal{position:absolute;left:0;right:0;text-align:center;font-size:30px;line-height:1.35;font-weight:500;letter-spacing:.02em}
.dark{background:radial-gradient(1000px 1000px at 50% 38%,#1d3b70 0%,NAVY 55%,#060d1c 100%)}
.flat{background:linear-gradient(180deg,NAVY2 0%,NAVY 100%)}
.cream{background:linear-gradient(160deg,CREAM 0%,#ebe3d2 100%)}
.rays{position:absolute;left:50%;top:50%;width:2200px;height:2200px;transform:translate(-50%,-50%);
 background:repeating-conic-gradient(from 0deg,rgba(227,196,122,.10) 0deg 5deg,transparent 5deg 15deg);
 -webkit-mask-image:radial-gradient(circle,#000 0,transparent 55%)}
.eyebrow{position:absolute;font-size:36px;letter-spacing:.22em;text-transform:uppercase;font-weight:700;color:GOLD}
.pill{display:inline-block;border-radius:999px;background:GOLD;color:NAVY;font-weight:700;letter-spacing:.03em;padding:14px 40px 18px;font-size:46px;line-height:1}
.pillo{display:inline-block;border-radius:999px;border:4px solid GOLD;color:GOLDL;font-weight:700;letter-spacing:.03em;padding:12px 36px 16px;font-size:44px;line-height:1}
.tick{display:inline-block;width:48px;height:48px;border-radius:50%;border:4px solid GOLD;position:relative;vertical-align:middle;flex:none}
.tick:after{content:'';position:absolute;left:14px;top:6px;width:11px;height:22px;border:solid GOLD;border-width:0 5px 5px 0;transform:rotate(45deg)}
.card{border-radius:36px}
""".replace("NAVY2", NAVY2).replace("NAVY", NAVY).replace("GOLDL", GOLDL).replace("GOLD", GOLD).replace("CREAM", CREAM)


def page(name, cls, body, folder=None, bg=""):
    out = (folder or TPL) / f"{name}.html"
    out.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
                   f"<body><div id='s' class='{cls}' style=\"{bg}\">{body}</div></body></html>")
    return name


def fit(img, x, y, w, h, extra=""):
    return (f"<div class='a' style='left:{x}px;top:{y}px;width:{w}px;height:{h}px;display:flex;align-items:center;justify-content:center'>"
            f"<img src='../assets/{img}' style='max-width:100%;max-height:100%;object-fit:contain;{extra}'></div>")


def fs_line(x, y, size=38, color=CREAM, tick=True, w=None, center=False):
    t = "<span class='tick' style='width:{0}px;height:{0}px'></span>".format(int(size * 1.2)) if tick else ""
    wid = f"width:{w}px;" if w else ""
    just = "justify-content:center;" if center else ""
    return (f"<div class='a' style='left:{x}px;top:{y}px;{wid}display:flex;align-items:center;gap:16px;{just}font-size:{size}px;"
            f"font-weight:600;color:{color};line-height:1.15'>{t}<span>{FULLSET}</span></div>")


def price_txt(w):
    return w["price"] if w.get("price") else "PRICE ON REQUEST"


def cta(w):
    return "DM to order" if w.get("price") else "Request price on WhatsApp"


def legal(w):
    return LEGAL_R if w["vendor"] == "Rolex" else LEGAL_P


def wrap(content, urgency):
    """urgency: None | 'demand' | 'only_one'. Adds a 70 px shift + band at the top."""
    if not urgency:
        return content
    if urgency == "demand":
        band = (f"<div class='a' style='left:0;right:0;top:250px;height:76px;background:linear-gradient(90deg,{GOLD},{GOLDL},{GOLD});"
                f"display:flex;align-items:center;justify-content:center;font-size:35px;font-weight:800;letter-spacing:.07em;color:{NAVY}'>"
                f"HIGH DEMAND PIECE · DM TO SOURCE YOURS NOW</div>")
    else:
        band = (f"<div class='a' style='left:0;right:0;top:250px;height:76px;background:{CREAM};border-top:5px solid {GOLD};border-bottom:5px solid {GOLD};"
                f"display:flex;align-items:center;justify-content:center;font-size:35px;font-weight:800;letter-spacing:.07em;color:{NAVY}'>"
                f"ONLY ONE AVAILABLE · DM TO SOURCE YOURS NOW</div>")
    return f"<div class='a' style='inset:0;transform:translateY(84px)'>{content}</div>{band}"


# ================================================================= AVAILABLE NOW styles
def st1_hero(w, urgency=None, name="st1_hero", folder=None):
    c = f"""
<div class='rays' style='top:860px'></div>
<div class='bar' style='left:80px;top:262px;width:200px'></div>
<div class='a' style='left:80px;top:292px;font-size:118px;font-weight:800;line-height:.95;letter-spacing:-.03em'>AVAILABLE<br><span style='color:{GOLDL}'>NOW</span></div>
<div class='a' style='right:80px;top:312px;text-align:right;font-size:52px;font-weight:700;color:{GOLDL};line-height:1.15'>HIGH<br>DEMAND</div>
{fit(w['img'],150,520,780,610,f"-webkit-box-reflect:below 0 linear-gradient(transparent 72%,rgba(255,255,255,.2));filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))")}
<div class='a' style='left:80px;top:1150px;font-size:88px;font-weight:800;letter-spacing:-.03em;white-space:nowrap'>{w['name']}</div>
<div class='a' style='left:80px;top:1252px;font-size:40px;font-weight:500;color:{GOLDL}'>Ref. {w['ref']} · {w['spec']}</div>
<div class='a' style='left:80px;top:1308px;font-size:92px;font-weight:800;letter-spacing:-.02em'>{price_txt(w)}</div>
<div class='a' style='right:80px;top:1330px'><span class='pill'>{cta(w)}</span></div>
{fs_line(80,1442,38,CREAM) if w['fullset'] else ''}
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>{legal(w)}</div>"""
    return page(name, "dark", wrap(c, urgency), folder)


def st2_cream(w, urgency=None, name="st2_cream", folder=None):
    FSCARD = ("<div class='a card' style='left:110px;top:880px;width:440px;padding:26px 30px 30px;background:#fff;border:2px solid #ebe5d8'>"
              "<div style='font-size:40px;font-weight:800;color:%s;line-height:1.15'>Full set:</div>"
              "<div style='font-size:40px;font-weight:600;color:%s;line-height:1.2;margin-top:6px'>official Rolex box, papers and tag</div></div>" % (NAVY, MUT)) if w['fullset'] else ''
    c = f"""
<div class='a' style='left:110px;top:262px;font-size:52px;font-weight:800;letter-spacing:.16em;color:{GOLD}'>HIGH DEMAND</div>
<div class='a' style='left:110px;top:332px;font-size:124px;font-weight:900;line-height:.92;letter-spacing:-.05em;color:{NAVY}'>AVAILABLE<br><span style='color:{GOLD};font-size:206px;line-height:.9'>NOW</span></div>
{fit(w['img'],585,480,400,680,f"filter:drop-shadow(0 40px 36px rgba(11,26,51,.32))")}
<div class='a' style='left:110px;top:700px;width:440px;font-size:42px;font-weight:600;line-height:1.25;color:{MUT}'>Ref. {w['ref']}<br>{w['spec']}</div>
{FSCARD}
<div class='a' style='left:110px;top:1170px;font-size:100px;font-weight:900;letter-spacing:-.04em;color:{NAVY};white-space:nowrap'>{w['name']}</div>
<div class='a' style='left:110px;top:1288px;font-size:88px;font-weight:900;letter-spacing:-.03em;color:{NAVY}'>{price_txt(w)}</div>
<div class='a' style='left:110px;top:1400px'><span class='pill'>{cta(w)}</span></div>
<div class='legal' style='top:1640px;color:{MUT}'>{legal(w)}</div>"""
    return page(name, "cream", f"<div class='a' style='left:0;top:0;width:60px;height:1920px;background:{NAVY}'></div>" + wrap(c, urgency), folder)


def st3_pair(w1, w2, headline="GMT-MASTER II", urgency=None, name="st3_pair", folder=None):
    both = w1["fullset"] and w2["fullset"]
    c = f"""
<div class='rays' style='top:880px'></div>
<div class='bar' style='left:50%;top:262px;width:200px;transform:translateX(-50%)'></div>
<div class='a c' style='top:296px;font-size:108px;font-weight:900;line-height:.98;letter-spacing:-.04em'>HIGH-DEMAND<br><span style='color:{GOLDL}'>{headline}</span></div>
<div class='a' style='left:539px;top:560px;width:3px;height:590px;background:linear-gradient(transparent,{GOLD},transparent)'></div>
{fit(w1['img'],60,560,440,590,"filter:drop-shadow(0 30px 34px rgba(0,0,0,.6))")}
{fit(w2['img'],580,560,440,590,"filter:drop-shadow(0 30px 34px rgba(0,0,0,.6))")}
<div class='a' style='left:0;width:540px;top:1165px;text-align:center;font-size:68px;font-weight:800;letter-spacing:-.03em'>{w1['name']}</div>
<div class='a' style='left:540px;width:540px;top:1165px;text-align:center;font-size:68px;font-weight:800;letter-spacing:-.03em'>{w2['name']}</div>
<div class='a' style='left:0;width:540px;top:1250px;text-align:center;font-size:60px;font-weight:800;color:{GOLDL}'>{price_txt(w1)}</div>
<div class='a' style='left:540px;width:540px;top:1250px;text-align:center;font-size:60px;font-weight:800;color:{GOLDL}'>{price_txt(w2)}</div>
<div class='a' style='left:0;width:540px;top:1328px;text-align:center;font-size:36px;font-weight:500;color:rgba(246,242,234,.8)'>Ref. {w1['ref']}</div>
<div class='a' style='left:540px;width:540px;top:1328px;text-align:center;font-size:36px;font-weight:500;color:rgba(246,242,234,.8)'>Ref. {w2['ref']}</div>
{fs_line(60,1388,36,CREAM,w=960,center=True) if both else ''}
<div class='a c' style='top:1438px'><span class='pillo'>Reply 1 or 2 to order</span></div>
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>{legal(w1)}</div>"""
    return page(name, "dark", wrap(c, urgency), folder)


def icon_box():
    return ("<svg width='128' height='128' viewBox='0 0 150 150'><rect x='14' y='56' width='122' height='78' rx='8' fill='#0f5a3d'/>"
            "<rect x='10' y='34' width='130' height='32' rx='8' fill='#14724d'/><rect x='10' y='58' width='130' height='5' fill='#c9a24b'/>"
            "<rect x='62' y='66' width='26' height='22' rx='4' fill='#c9a24b'/></svg>")


def icon_papers():
    return ("<svg width='128' height='128' viewBox='0 0 150 150'><rect x='30' y='10' width='96' height='128' rx='8' fill='#ffffff' stroke='#c9a24b' stroke-width='4'/>"
            "<rect x='46' y='34' width='64' height='7' rx='3' fill='#0b1a33'/><rect x='46' y='54' width='64' height='6' rx='3' fill='#9aa3b2'/>"
            "<rect x='46' y='70' width='50' height='6' rx='3' fill='#9aa3b2'/><circle cx='104' cy='112' r='17' fill='#c9a24b'/>"
            "<circle cx='104' cy='112' r='9' fill='none' stroke='#0b1a33' stroke-width='3'/></svg>")


def icon_tag():
    return ("<svg width='128' height='128' viewBox='0 0 150 150'><path d='M24 24 L84 24 L130 70 L84 126 L24 126 Z' fill='#0f5a3d' stroke='#c9a24b' stroke-width='4'/>"
            "<circle cx='50' cy='50' r='9' fill='#f6f2ea'/><path d='M50 50 Q20 8 8 30' stroke='#c9a24b' stroke-width='4' fill='none'/>"
            "<rect x='62' y='68' width='44' height='6' rx='3' fill='#f6f2ea'/><rect x='62' y='86' width='32' height='6' rx='3' fill='#f6f2ea'/></svg>")


def st4_set(w, urgency=None, name="st4_set", folder=None):
    def card(y, svg, t1, t2):
        return (f"<div class='a card' style='left:600px;top:{y}px;width:410px;height:210px;background:{CREAM};display:flex;align-items:center;gap:14px;padding:0 22px 0 12px'>"
                f"{svg}<div><div style='font-size:42px;font-weight:800;color:{NAVY};line-height:1.05'>{t1}</div>"
                f"<div style='font-size:32px;font-weight:600;color:{MUT};margin-top:6px'>{t2}</div></div></div>")
    c = f"""
<div class='rays' style='top:850px'></div>
<div class='a' style='left:80px;top:262px;font-size:60px;font-weight:800;letter-spacing:.18em;color:{GOLDL}'>AVAILABLE NOW</div>
<div class='bar' style='left:80px;top:342px;width:180px'></div>
<div class='a' style='left:80px;top:372px;font-size:118px;font-weight:900;letter-spacing:-.04em'>THE FULL SET</div>
{fit(w['img'],70,500,490,660,"filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))")}
{card(510, icon_box(), 'Official Rolex box', 'Original, for the model')}
{card(750, icon_papers(), 'Papers', 'Reference and serial match')}
{card(990, icon_tag(), 'Tag', 'Comes with the watch')}
<div class='a' style='left:80px;top:1190px;font-size:84px;font-weight:800;letter-spacing:-.03em;white-space:nowrap'>{w['name']}</div>
<div class='a' style='left:80px;top:1290px;font-size:40px;font-weight:500;color:{GOLDL}'>Ref. {w['ref']} · {w['spec']}</div>
<div class='a' style='left:80px;top:1345px;font-size:88px;font-weight:800;letter-spacing:-.02em'>{price_txt(w)}</div>
<div class='a' style='right:80px;top:1368px'><span class='pill'>{cta(w)}</span></div>
{fs_line(80,1462,36,CREAM)}
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>{legal(w)}</div>"""
    return page(name, "dark", wrap(c, urgency), folder)


def st5_editorial(w, urgency=None, name="st5_editorial", folder=None):
    FSBOX = ("<div class='a card' style='left:110px;top:1384px;width:860px;height:112px;border:4px solid %s;display:flex;align-items:center;padding:0 30px;gap:18px'>"
             "<span class='tick' style='width:54px;height:54px'></span><span style='font-size:38px;font-weight:600'>%s</span></div>" % (GOLD, FULLSET)) if w['fullset'] else ''
    c = f"""
<div class='a' style='left:110px;top:262px;font-size:48px;font-weight:700;letter-spacing:.22em;color:{GOLD}'>AVAILABLE NOW</div>
<div class='a' style='left:110px;top:330px;width:860px;font-size:118px;font-weight:900;line-height:.92;letter-spacing:-.045em'>{w['name']}</div>
<div class='a card' style='left:110px;top:570px;width:860px;height:600px;background:{CREAM};box-shadow:0 30px 60px rgba(0,0,0,.4)'></div>
<div class='a' style='left:110px;top:570px;width:18px;height:600px;background:linear-gradient(180deg,{GOLD},{GOLDL});border-radius:36px 0 0 36px'></div>
{fit(w['img'],250,590,580,560,f"filter:drop-shadow(0 26px 28px rgba(11,26,51,.35))")}
<div class='a' style='right:150px;top:1128px'><span class='pill' style='box-shadow:0 10px 24px rgba(0,0,0,.4)'>{cta(w)}</span></div>
<div class='a' style='left:110px;top:1210px;font-size:88px;font-weight:900;letter-spacing:-.03em;white-space:nowrap'>{price_txt(w)}</div>
<div class='a' style='left:110px;top:1312px;font-size:40px;font-weight:500;color:{GOLDL}'>Ref. {w['ref']} · {w['spec']}</div>
{FSBOX}
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>{legal(w)}</div>"""
    return page(name, "flat", wrap(c, urgency), folder)


def st6_plaque(w, urgency=None, name="st6_plaque", folder=None):
    c = f"""
<div class='a' style='left:60px;top:250px;width:960px;height:1300px;border:3px solid {GOLD};border-radius:10px'></div>
<div class='a' style='left:84px;top:274px;width:912px;height:1252px;border:1px solid rgba(227,196,122,.55);border-radius:6px'></div>
<div class='a c' style='top:306px;font-size:50px;font-weight:700;letter-spacing:.3em;color:{GOLDL}'>AVAILABLE NOW</div>
<div class='rays' style='top:700px;opacity:.7'></div>
{fit(w['img'],240,380,600,650,"filter:drop-shadow(0 30px 34px rgba(0,0,0,.6))")}
<div class='a' style='left:170px;top:1028px;width:740px;height:62px;border-radius:14px;background:linear-gradient(180deg,#27437a,#15264a);border-top:4px solid {GOLD}'></div>
<div class='a card' style='left:140px;top:1130px;width:800px;height:350px;background:linear-gradient(180deg,{GOLDL},{GOLD} 55%,#a8832f);color:{NAVY};text-align:center;box-shadow:0 20px 50px rgba(0,0,0,.5)'>
 <div style='margin-top:22px;font-size:68px;font-weight:900;letter-spacing:-.03em;white-space:nowrap'>{w['name']}</div>
 <div style='font-size:36px;font-weight:600;margin-top:4px'>Ref. {w['ref']} · {w['spec']}</div>
 <div style='font-size:78px;font-weight:900;letter-spacing:-.02em;margin-top:8px;line-height:1.1'>{price_txt(w)}</div>
 <div style='font-size:34px;font-weight:700;margin-top:10px'>{FULLSET if w['fullset'] else cta(w)}</div>
</div>
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>{legal(w)}</div>"""
    return page(name, "dark", wrap(c, urgency), folder)


STYLES = [("hero", st1_hero), ("cream", st2_cream), ("pair", st3_pair), ("set", st4_set), ("editorial", st5_editorial), ("plaque", st6_plaque)]


# ================================================================= KNOWLEDGE (website look)
def legal_k(color):
    return f"<div class='legal' style='top:1640px;color:{color}'>Advance Watch Co · WhatsApp in bio</div>"


def sz(text, sizes):
    n = len(text)
    for lim, s in sizes:
        if n <= lim:
            return s
    return sizes[-1][1]


def footer_pill(label="Save this"):
    return f"<div class='a c' style='top:1455px'><span class='pill'>{label}</span></div>"


def kn_myth_fact(d, folder, name):
    ms = sz(d["myth"], [(60, 84), (90, 72), (200, 62)])
    fsz = sz(d["fact"], [(110, 56), (170, 48), (260, 42)])
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:326px;width:920px;font-size:{sz(d['title'],[(14,96),(18,80),(26,64),(60,54)])}px;font-weight:700;letter-spacing:-.04em;line-height:1.02'>{d['title']}</div>
<div class='a' style='left:70px;top:480px;width:940px;display:flex;flex-direction:column;gap:36px'>
 <div class='card' style='padding:44px 50px 52px;background:{NAVY2};border:3px solid rgba(201,162,75,.55)'>
  <div style='font-size:38px;font-weight:800;letter-spacing:.2em;color:{GOLD}'>THE MYTH</div>
  <div style='font-size:{ms}px;font-weight:700;line-height:1.08;letter-spacing:-.03em;margin-top:14px'>{d['myth']}</div></div>
 <div class='card' style='padding:44px 50px 52px;background:{CREAM};color:{NAVY}'>
  <div style='font-size:38px;font-weight:800;letter-spacing:.2em;color:{GOLD}'>THE FACT</div>
  <div style='font-size:{fsz}px;font-weight:600;line-height:1.22;margin-top:14px'>{d['fact']}</div></div></div>
{footer_pill()}
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "flat", c, folder)


def kn_checklist(d, folder, name):
    n = len(d["items"])
    top, end = 600, 1500
    rh = (end - top) / n
    rows = ""
    for i, (t, s) in enumerate(d["items"]):
        y = top + i * rh
        tsz = 52 if n <= 3 else (46 if n <= 5 else 44)
        rows += (f"<div class='a card' style='left:70px;top:{y:.0f}px;width:940px;height:{rh-22:.0f}px;background:#fff;border:2px solid #ebe5d8;display:flex;align-items:center;gap:26px;padding:0 36px'>"
                 f"<span class='tick' style='width:64px;height:64px'></span><div><div style='font-size:{tsz}px;font-weight:700;color:{NAVY};line-height:1.1'>{t}</div>"
                 + (f"<div style='font-size:36px;font-weight:500;color:{MUT};margin-top:6px;line-height:1.2'>{s}</div>" if s else "") + "</div></div>")
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:324px;width:920px;font-size:{sz(d['title'],[(16,118),(30,104)])}px;font-weight:700;line-height:1;letter-spacing:-.04em;color:{NAVY}'>{d['title']}</div>
{rows}
{legal_k(MUT)}"""
    return page(name, "cream", c, folder)


def kn_big_number(d, folder, name):
    n = len(d["big"])
    S = {1: 700, 2: 600, 3: 470}.get(n, 380)
    o = 700 - S
    c = f"""
<div class='rays' style='top:{800-o//2}px'></div>
<div class='eyebrow c' style='top:262px'>{d['eyebrow']}</div>
<div class='a c' style='top:{300+o}px;font-size:{S}px;font-weight:900;line-height:1;letter-spacing:-.06em;color:transparent;background:linear-gradient(180deg,{GOLDL} 10%,{GOLD} 55%,#7d5f22 100%);-webkit-background-clip:text;background-clip:text;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))'>{d['big']}</div>
<div class='a c' style='top:1000px;font-size:150px;font-weight:800;letter-spacing:.08em'>{d['unit']}</div>
<div class='bar' style='left:50%;top:1190px;width:200px;transform:translateX(-50%)'></div>
<div class='a' style='left:100px;top:1230px;width:880px;text-align:center;font-size:50px;font-weight:600;line-height:1.25'>{d['text']}</div>
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "dark", c, folder)


def kn_qa_card(d, folder, name):
    qs = sz(d["q"], [(50, 84), (80, 72), (120, 64)])
    asz = sz(d["a"], [(120, 58), (170, 54), (230, 50)])
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:70px;top:340px;width:940px;display:flex;flex-direction:column;gap:40px'>
 <div class='card' style='padding:48px 52px 56px;background:{CREAM};color:{NAVY}'>
  <div style='font-size:38px;font-weight:800;letter-spacing:.2em;color:{GOLD}'>QUESTION</div>
  <div style='font-size:{qs}px;font-weight:800;line-height:1.08;letter-spacing:-.03em;margin-top:16px'>{d['q']}</div></div>
 <div class='card' style='padding:48px 52px 56px;background:{NAVY2};border:3px solid rgba(201,162,75,.6)'>
  <div style='font-size:38px;font-weight:800;letter-spacing:.2em;color:{GOLDL}'>THE ANSWER</div>
  <div style='font-size:{asz}px;font-weight:600;line-height:1.24;margin-top:16px'>{d['a']}</div></div></div>
{footer_pill()}
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "flat", c, folder)


def kn_compare(d, folder, name):
    n = len(d["rows"])
    top = 700
    rh = (1500 - top) / n
    rows = ""
    for i, (lab, a, b) in enumerate(d["rows"]):
        y = top + i * rh
        rows += (f"<div class='a card' style='left:70px;top:{y:.0f}px;width:940px;height:{rh-20:.0f}px;background:#fff;border:2px solid #ebe5d8'>"
                 f"<div style='position:absolute;left:34px;top:16px;font-size:30px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:{GOLD}'>{lab}</div>"
                 f"<div style='position:absolute;left:34px;top:62px;width:410px;font-size:40px;font-weight:700;line-height:1.12;color:{NAVY}'>{a}</div>"
                 f"<div style='position:absolute;left:470px;top:34px;width:3px;height:{rh-88:.0f}px;background:#ebe5d8'></div>"
                 f"<div style='position:absolute;left:506px;top:62px;width:400px;font-size:40px;font-weight:700;line-height:1.12;color:{NAVY}'>{b}</div></div>")
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:322px;width:920px;font-size:{sz(d['title'],[(24,100),(40,88)])}px;font-weight:700;line-height:1;letter-spacing:-.04em;color:{NAVY}'>{d['title']}</div>
<div class='a card' style='left:70px;top:560px;width:450px;height:100px;background:{NAVY};color:{CREAM};display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:800'>{d['cols'][0]}</div>
<div class='a card' style='left:560px;top:560px;width:450px;height:100px;background:{GOLD};color:{NAVY};display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:800'>{d['cols'][1]}</div>
{rows}
{legal_k(MUT)}"""
    return page(name, "cream", c, folder)


def kn_steps(d, folder, name):
    n = len(d["items"])
    top, end = 600, 1500
    rh = (end - top) / n
    rows = ""
    for i, (t, s) in enumerate(d["items"]):
        y = top + i * rh
        tsz = 54 if n <= 3 else 46
        rows += (f"<div class='a' style='left:70px;top:{y:.0f}px;width:940px;height:{rh-14:.0f}px;display:flex;align-items:center;gap:30px'>"
                 f"<div style='flex:none;width:96px;height:96px;border-radius:50%;background:{NAVY};color:{GOLDL};display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:800'>{i+1}</div>"
                 f"<div><div style='font-size:{tsz}px;font-weight:800;line-height:1.08;color:{NAVY};letter-spacing:-.02em'>{t}</div>"
                 + (f"<div style='font-size:36px;font-weight:500;color:{MUT};margin-top:6px;line-height:1.2'>{s}</div>" if s else "") + "</div></div>")
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:322px;width:920px;font-size:{sz(d['title'],[(26,100),(40,88)])}px;font-weight:700;line-height:1;letter-spacing:-.04em;color:{NAVY}'>{d['title']}</div>
<div class='a' style='left:150px;top:640px;width:4px;height:{rh*(n-1):.0f}px;background:rgba(201,162,75,.5)'></div>
{rows}
{legal_k(MUT)}"""
    return page(name, "cream", c, folder)


def kn_timeline(d, folder, name):
    n = len(d["items"])
    top, end = 640, 1480
    rh = (end - top) / n
    rows = ""
    for i, (t, s) in enumerate(d["items"]):
        y = top + i * rh
        rows += (f"<div class='a' style='left:70px;top:{y:.0f}px;width:940px;display:flex;gap:34px;align-items:flex-start'>"
                 f"<div style='flex:none;width:44px;height:44px;margin-top:12px;border-radius:50%;background:{GOLD};box-shadow:0 0 0 10px rgba(201,162,75,.25)'></div>"
                 f"<div><div style='font-size:62px;font-weight:800;letter-spacing:-.03em;color:{GOLDL};line-height:1.05'>{t}</div>"
                 f"<div style='font-size:42px;font-weight:500;line-height:1.22;margin-top:8px;color:rgba(246,242,234,.9)'>{s}</div></div></div>")
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:322px;width:920px;font-size:{sz(d['title'],[(24,100),(40,86)])}px;font-weight:700;line-height:1.02;letter-spacing:-.04em'>{d['title']}</div>
<div class='a' style='left:91px;top:{top+30}px;width:4px;height:{rh*(n-1):.0f}px;background:rgba(201,162,75,.5)'></div>
{rows}
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "dark", c, folder)


def kn_quote(d, folder, name):
    qs = sz(d["quote"], [(60, 92), (90, 80), (130, 70), (200, 62)])
    c = f"""
<div class='rays' style='top:900px'></div>
<div class='eyebrow c' style='top:262px'>{d['eyebrow']}</div>
<div class='a c' style='top:300px;font-size:380px;font-weight:900;line-height:1;color:{GOLD};opacity:.9'>“</div>
<div class='a' style='left:90px;top:640px;width:900px;text-align:center;font-size:{qs}px;font-weight:700;line-height:1.12;letter-spacing:-.03em'>{d['quote']}</div>
<div class='bar' style='left:50%;top:1250px;width:200px;transform:translateX(-50%)'></div>
<div class='a' style='left:110px;top:1290px;width:860px;text-align:center;font-size:46px;font-weight:500;line-height:1.28;color:rgba(246,242,234,.85)'>{d['note']}</div>
{footer_pill('Send this to a friend')}
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "dark", c, folder)


def kn_ladder(d, folder, name):
    n = len(d["rungs"])
    top, end = 640, 1440
    rh = (end - top) / n
    rows = ""
    for i, (lab, txt) in enumerate(d["rungs"]):
        y = top + i * rh
        shade = ["#e3c47a", "#c9a24b", "#a8832f", "#7d5f22"][min(i, 3)]
        rows += (f"<div class='a card' style='left:70px;top:{y:.0f}px;width:940px;height:{rh-22:.0f}px;background:linear-gradient(90deg,{shade} 0,{shade} 34%,{NAVY2} 34%);display:flex;align-items:center;padding:0 36px 0 36px;gap:30px'>"
                 f"<div style='flex:none;width:262px;font-size:{44 if max(len(r[0]) for r in d['rungs'])>9 else 52}px;font-weight:900;letter-spacing:-.03em;color:{NAVY if i<2 else CREAM};line-height:1.05'>{lab}</div>"
                 f"<div style='font-size:42px;font-weight:600;line-height:1.2'>{txt}</div></div>")
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:322px;width:920px;font-size:{sz(d['title'],[(26,100),(40,86)])}px;font-weight:700;line-height:1.02;letter-spacing:-.04em'>{d['title']}</div>
{rows}
<div class='a c' style='top:1462px;font-size:34px;font-weight:600;color:rgba(246,242,234,.7)'>{d.get('foot','Always approximate, it depends on the watch')}</div>
{legal_k('rgba(246,242,234,.6)')}"""
    return page(name, "flat", c, folder)


def kn_do_dont(d, folder, name):
    def lst(items, col):
        return "".join(f"<div style='font-size:50px;font-weight:700;line-height:1.14;margin-top:22px;color:{col};letter-spacing:-.02em'>{t}</div>" for t in items)
    c = f"""
<div class='eyebrow' style='left:80px;top:262px'>{d['eyebrow']}</div>
<div class='a' style='left:80px;top:322px;width:920px;font-size:{sz(d['title'],[(24,100),(40,90)])}px;font-weight:700;line-height:1;letter-spacing:-.04em;color:{NAVY}'>{d['title']}</div>
<div class='a' style='left:70px;top:520px;width:940px;display:flex;flex-direction:column;gap:36px'>
 <div class='card' style='padding:38px 46px 46px;background:#fff;border:2px solid #ebe5d8'>
  <div style='display:flex;align-items:center;gap:20px;font-size:52px;font-weight:900;letter-spacing:.1em;color:{GOLD}'><span class='tick' style='width:62px;height:62px'></span>DO</div>{lst(d['do'],NAVY)}</div>
 <div class='card' style='padding:38px 46px 46px;background:{NAVY}'>
  <div style='font-size:52px;font-weight:900;letter-spacing:.1em;color:{GOLDL}'>✕&nbsp; DON'T</div>{lst(d['dont'],CREAM)}</div></div>
{legal_k(MUT)}"""
    return page(name, "cream", c, folder)


KN = dict(myth_fact=kn_myth_fact, checklist=kn_checklist, big_number=kn_big_number, qa_card=kn_qa_card, compare_table=kn_compare,
          steps=kn_steps, timeline=kn_timeline, quote_card=kn_quote, ladder=kn_ladder, do_dont=kn_do_dont)


# ================================================================= rendering + sheets
SHOT = ROOT / "_shot.js"
SHOT.write_text("""const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const jobs=JSON.parse(process.argv[2]);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const rep=[];
for(const j of jobs){await p.goto('file://'+path.resolve(j.html));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);
 const chk=await p.evaluate(()=>{const out=[];document.querySelectorAll('#s *').forEach(e=>{if(e.children.length===0&&e.textContent.trim()&&!e.closest('.legal')){const rg=document.createRange();rg.selectNodeContents(e);const r=rg.getBoundingClientRect();out.push([Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom),e.textContent.trim().slice(0,30)])}});
  const imgs=[...document.querySelectorAll('#s img')].map(i=>{const r=i.getBoundingClientRect();return [Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]});return {out,imgs}});
 const bad=chk.out.filter(r=>r[3]>1585||r[2]>1030||r[0]<50||r[1]<248).map(r=>r.join(','));const badi=chk.imgs.filter(r=>r[0]<40||r[2]>1040||r[1]<248||r[3]>1585).map(r=>r.join(','));
 if(bad.length||badi.length)rep.push(j.out+' OUT OF SAFE ZONE: '+bad.slice(0,3).join(' | ')+' IMG '+badi.join(' | '));
 await p.screenshot(j.out.endsWith('.jpg')?{path:j.out,type:'jpeg',quality:90}:{path:j.out,type:'png'});}
await b.close();console.log(JSON.stringify(rep))})();""")


def render(jobs):
    r = subprocess.run(["node", str(SHOT), json.dumps(jobs)], cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-800:])
    lines = [l for l in r.stdout.strip().splitlines() if l.startswith("[")]
    rep = json.loads(lines[-1]) if lines else []
    for x in rep:
        print("WARN", x)
    return rep


def sheet(imgs, labels, title, out, w=400, cols=None):
    F = ImageFont.truetype(str(ROOT / "fonts" / "Inter.ttf"), 26)
    FS = ImageFont.truetype(str(ROOT / "fonts" / "Inter.ttf"), 22)
    cols = cols or len(imgs)
    rows = (len(imgs) + cols - 1) // cols
    h, gap, top = int(w * 1920 / 1080), 14, 62
    sh = Image.new("RGB", (cols * (w + gap) + gap, top + rows * (h + 56)), (16, 18, 24))
    d = ImageDraw.Draw(sh)
    d.text((gap, 16), title, font=F, fill=(227, 196, 122))
    for i, (p, lab) in enumerate(zip(imgs, labels)):
        im = Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS)
        x, y = gap + (i % cols) * (w + gap), top + (i // cols) * (h + 56)
        sh.paste(im, (x, y))
        d.text((x, y + h + 8), lab, font=FS, fill=(246, 242, 234))
    sh.save(PRE / out, quality=92)


# preview watches (real store listings, see notes.md)
PW = {
    "sub": dict(name="SUBMARINER DATE", ref="126610LN", spec="Steel · Black dial", price="AED 59,000", vendor="Rolex", img="sub.png", fullset=True),
    "daytona": dict(name="DAYTONA", ref="126500LN", spec="Steel · Black dial", price="AED 119,000", vendor="Rolex", img="daytona.png", fullset=True),
    "batman": dict(name="BATMAN", ref="126710BLNR", spec="Jubilee", price="AED 68,000", vendor="Rolex", img="batman.png", fullset=True),
    "pepsi": dict(name="PEPSI", ref="126710BLRO", spec="Jubilee", price="AED 115,000", vendor="Rolex", img="pepsi.png", fullset=True),
    "dj": dict(name="DATEJUST 41", ref="126334", spec="Green ombré · Jubilee", price="AED 73,400", vendor="Rolex", img="dj.png", fullset=True),
    "daydate": dict(name="DAY-DATE 40", ref="228238", spec="Yellow gold · Green dial", price="AED 242,000", vendor="Rolex", img="daydate.png", fullset=True),
    "panda": dict(name="DAYTONA PANDA", ref="126500LN", spec="Steel · White dial", price="AED 145,000", vendor="Rolex", img="panda.png", fullset=True),
}


def previews():
    jobs = []
    names = []
    for nm, fn, args in [("1_hero", st1_hero, (PW["sub"],)), ("2_cream", st2_cream, (PW["daytona"],)), ("3_pair", st3_pair, (PW["batman"], PW["pepsi"])),
                         ("4_set", st4_set, (PW["dj"],)), ("5_editorial", st5_editorial, (PW["daydate"],)), ("6_plaque", st6_plaque, (PW["panda"],))]:
        name = f"available_{nm}"
        fn(*args, name=name)
        jobs.append(dict(html=f"templates/{name}.html", out=f"previews/{name}.png"))
        names.append(name)
    # urgency variants
    ug = [("urgency_demand_hero", st1_hero, (PW["sub"],), "demand", "Demand band, hero"),
          ("urgency_demand_plaque", st6_plaque, (PW["panda"],), "demand", "Demand band, plaque"),
          ("urgency_onlyone_cream", st2_cream, (PW["daytona"],), "only_one", "Only-one (OFF by default)"),
          ("urgency_onlyone_editorial", st5_editorial, (PW["daydate"],), "only_one", "Only-one (OFF by default)")]
    for nm, fn, args, u, _ in ug:
        fn(*args, urgency=u, name=nm)
        jobs.append(dict(html=f"templates/{nm}.html", out=f"previews/{nm}.png"))
    # knowledge previews: eight different topics and layouts
    import knowledge_library as K
    pick = ["seconds_hand", "how_we_work", "five_years", "walk_in_daytona", "boutique_vs_dealer", "new_release_path", "wait_tiers", "boutique_phrases"]
    kn_names = []
    for kid in pick:
        d = next(x for x in K.L if x["id"] == kid)
        nm = f"knowledge_{kid}"
        KN[d["layout"]](d, None, nm)
        jobs.append(dict(html=f"templates/{nm}.html", out=f"previews/{nm}.png"))
        kn_names.append(nm)
    render(jobs)
    sheet([PRE / f"{n}.png" for n in names], ["1 hero (day style A)", "2 cream (B)", "3 pair (C)", "4 the full set (D)", "5 editorial (E)", "6 gallery plaque (F)"],
          "AVAILABLE NOW · six styles, one style per day · full watch inside the frame · full-set line on every Rolex", "sheet_available_styles.jpg", w=300)
    sheet([PRE / f"{n}.png" for n, *_ in ug], [x[4] for x in ug],
          "URGENCY · rare and truthful: 1-2 watches on about half the days. 'Only one available' stays OFF unless you list the watch", "sheet_urgency.jpg", w=420)
    sheet([PRE / f"{n}.png" for n in kn_names], [f"{n.split('_',1)[1]}" for n in kn_names],
          "KNOWLEDGE · website look · 8 different topics in 8 different layouts (library has 43)", "sheet_knowledge.jpg", w=330, cols=4)


def library():
    import knowledge_library as K
    jobs = []
    for i, d in enumerate(K.L, 1):
        nm = f"k{i:02d}_{d['id']}"
        KN[d["layout"]](d, TPL, nm)
        jobs.append(dict(html=f"templates/{nm}.html", out=f"library/{nm}.jpg"))
    render(jobs)
    print(len(jobs), "library stories rendered")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "library":
        library()
    else:
        previews()
    print("ok")

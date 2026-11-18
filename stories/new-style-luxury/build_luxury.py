#!/usr/bin/env python3
"""Round 2: LUXURY story designs (5 AVAILABLE NOW + 4 KNOWLEDGE), 1080x1920, content inside y 250-1580.
Writes templates/*.html then renders previews/*.png with Playwright and makes two preview sheets.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 build_luxury.py"""
import subprocess, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
TPL, PRE = ROOT / "templates", ROOT / "previews"
TPL.mkdir(exist_ok=True); PRE.mkdir(exist_ok=True)

NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")

CSS = """
@font-face{font-family:'Corm';src:url('../fonts/Cormorant.ttf');font-weight:300 700;font-style:normal}
@font-face{font-family:'Corm';src:url('../fonts/Cormorant-Italic.ttf');font-weight:300 700;font-style:italic}
@font-face{font-family:'Play';src:url('../fonts/Playfair.ttf');font-weight:400 900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000}
#s{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Corm',serif}
.a{position:absolute}.c{left:0;right:0;text-align:center}
.grain{position:absolute;inset:0;background-image:url("__NOISE__");opacity:.10;mix-blend-mode:overlay;pointer-events:none}
.cap{font-family:'Corm',serif;text-transform:uppercase;letter-spacing:.42em;font-weight:600;font-size:22px}
.gold{color:#cdb07a}.ink{color:#1c1812}
.rule{position:absolute;height:1px;background:linear-gradient(90deg,transparent,#cdb07a 20%,#cdb07a 80%,transparent)}
.tiny{position:absolute;left:0;right:0;text-align:center;font-size:17px;line-height:1.75;letter-spacing:.24em;text-transform:uppercase;font-weight:600}
""".replace("__NOISE__", NOISE)

DISC_R = "Independent dealer · Not affiliated with Rolex<br>WhatsApp in bio"
DISC_P = "Independent dealer · Not affiliated with Patek Philippe<br>WhatsApp in bio"
DISC_K = "Advance Watch Co<br>WhatsApp in bio"


def page(name, bg, body):
    (TPL / f"{name}.html").write_text(
        f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
        f"<body><div id='s' style=\"{bg}\">{body}<div class='grain'></div></div></body></html>")
    return name


# ================= AVAILABLE NOW =================
def av1_window():  # Submariner Date 126610LN
    body = """
<div class='a' style='left:50%;top:0;width:1100px;height:1500px;transform:translateX(-50%);
 background:linear-gradient(180deg,rgba(255,244,220,.20),rgba(255,244,220,.05) 55%,transparent);
 clip-path:polygon(40% 0,60% 0,98% 100%,2% 100%);filter:blur(22px)'></div>
<div class='a c cap gold' style='top:270px'>Advance Watch Co</div>
<img class='a' src='../assets/sub.png' style='left:50%;top:400px;height:720px;transform:translateX(-50%);
 -webkit-box-reflect:below 4px linear-gradient(transparent 62%,rgba(255,255,255,.20))'>
<div class='a' style='left:50%;top:1128px;width:760px;height:60px;transform:translateX(-50%);background:radial-gradient(ellipse,rgba(205,176,122,.28),transparent 70%)'></div>
<div class='a c' style='top:1230px;font-size:84px;font-weight:500;color:#f2eadb;letter-spacing:.02em'>Submariner Date</div>
<div class='a c cap gold' style='top:1338px'>Reference 126610LN &nbsp;·&nbsp; Steel</div>
<div class='rule' style='left:300px;width:480px;top:1400px'></div>
<div class='a c' style='top:1425px;font-size:34px;font-style:italic;color:#cdb07a'>Now available</div>
<div class='a c' style='top:1478px;font-size:46px;font-weight:500;color:#f2eadb;letter-spacing:.06em'>AED 59,000</div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.45)'>__D__</div>""".replace("__D__", DISC_R)
    return page("available_1_boutique_window", "background:radial-gradient(1200px 1000px at 50% 18%,#171512,#060606 70%)", body)


def av2_ivory():  # Daytona black dial 126500LN
    body = """
<div class='a' style='left:70px;right:70px;top:262px;bottom:342px;border:1px solid rgba(156,122,60,.7)'></div>
<div class='a' style='left:84px;right:84px;top:276px;bottom:356px;border:1px solid rgba(156,122,60,.35)'></div>
<div class='a cap' style='left:130px;top:322px;color:#9c7a3c'>No. 14</div>
<div class='a cap' style='right:130px;top:322px;color:#9c7a3c;text-align:right'>Advance Watch Co</div>
<div class='a c ink' style='top:392px;font-size:128px;font-weight:500;letter-spacing:.01em'>Daytona</div>
<div class='a c' style='top:540px;font-size:32px;font-style:italic;color:#6b5a3a'>Cosmograph · Steel · Black dial</div>
<div class='a' style='left:50%;top:1085px;width:520px;height:46px;transform:translateX(-50%);background:radial-gradient(ellipse,rgba(40,30,15,.30),transparent 68%);filter:blur(6px)'></div>
<img class='a' src='../assets/daytona.png' style='left:50%;top:640px;height:470px;transform:translateX(-50%);filter:drop-shadow(0 22px 22px rgba(40,30,15,.28))'>
<div class='rule' style='left:230px;width:620px;top:1190px;background:linear-gradient(90deg,transparent,#9c7a3c 20%,#9c7a3c 80%,transparent)'></div>
<div class='a c cap' style='top:1222px;color:#6b5a3a;font-size:21px'>Reference 126500LN</div>
<div class='a c ink' style='top:1282px;font-size:54px;font-weight:500;letter-spacing:.05em'>AED 119,000</div>
<div class='a c' style='top:1368px;font-size:34px;font-style:italic;color:#9c7a3c'>Now available</div>
<div class='tiny' style='top:1500px;color:rgba(28,24,18,.45)'>__D__</div>""".replace("__D__", DISC_R)
    return page("available_2_ivory_plate", "background:radial-gradient(1100px 1100px at 50% 35%,#f4eee2,#e6dcc8)", body)


def av3_emerald():  # Datejust 41 green ombre 126334
    body = """
<div class='a' style='inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.012) 0 2px,transparent 2px 5px)'></div>
<div class='a' style='left:66px;right:66px;top:256px;bottom:338px;border:1px solid rgba(205,176,122,.75)'></div>
<div class='a' style='left:80px;right:80px;top:270px;bottom:352px;border:1px solid rgba(205,176,122,.28)'></div>
<div class='a c cap gold' style='top:326px'>Advance Watch Co</div>
<div class='a' style='left:50%;top:390px;width:900px;height:900px;transform:translateX(-50%);background:radial-gradient(circle,rgba(70,150,110,.20),transparent 62%)'></div>
<img class='a' src='../assets/dj.png' style='left:50%;top:390px;height:700px;transform:translateX(-50%);
 -webkit-box-reflect:below 4px linear-gradient(transparent 60%,rgba(255,255,255,.18))'>
<div class='a c' style='top:1130px;font-size:88px;font-weight:500;color:#efe6d2'>Datejust 41</div>
<div class='a c' style='top:1236px;font-size:32px;font-style:italic;color:#bcd0c2'>Green ombré dial · Steel &amp; white gold</div>
<div class='rule' style='left:320px;width:440px;top:1302px'></div>
<div class='a c cap gold' style='top:1330px;font-size:21px'>Reference 126334</div>
<div class='a c' style='top:1376px;font-size:50px;font-weight:500;color:#efe6d2;letter-spacing:.06em'>AED 73,400</div>
<div class='a c' style='top:1446px;font-size:32px;font-style:italic;color:#cdb07a'>Now available</div>
<div class='tiny' style='top:1500px;color:rgba(239,230,210,.4)'>__D__</div>""".replace("__D__", DISC_R)
    return page("available_3_emerald_velvet", "background:radial-gradient(1100px 1200px at 50% 30%,#0f3a2c,#06231a 55%,#031510)", body)


def av4_editorial():  # GMT-Master II Pepsi 126710BLRO
    body = """
<div class='a' style='left:0;right:0;top:300px;text-align:center;font-family:Play,serif;font-size:430px;font-weight:700;line-height:.9;color:rgba(205,176,122,.13);letter-spacing:-.02em'>GMT</div>
<div class='a' style='left:0;right:0;top:640px;text-align:center;font-family:Play,serif;font-size:300px;font-weight:700;line-height:.9;color:rgba(205,176,122,.08);letter-spacing:.02em'>II</div>
<div class='rule' style='left:90px;right:90px;top:272px;background:#cdb07a;opacity:.6'></div>
<div class='a cap gold' style='left:90px;top:292px;font-size:19px'>No. 03</div>
<div class='a cap gold' style='right:90px;top:292px;font-size:19px'>Now available</div>
<img class='a' src='../assets/pepsi.png' style='left:50%;top:380px;height:800px;transform:translateX(-50%) rotate(3deg);filter:drop-shadow(0 30px 30px rgba(0,0,0,.55))'>
<div class='rule' style='left:90px;right:90px;top:1236px;background:#cdb07a;opacity:.6'></div>
<div class='a' style='left:90px;top:1268px;font-size:70px;font-weight:500;color:#f2eadb;line-height:1.02'>GMT-Master II<br><span style='font-style:italic;color:#cdb07a'>“Pepsi”</span></div>
<div class='a' style='right:90px;top:1272px;width:360px;text-align:left'>
 <div class='cap gold' style='font-size:17px;letter-spacing:.34em'>Reference</div><div style='font-size:34px;color:#f2eadb;margin:2px 0 14px'>126710BLRO</div>
 <div class='cap gold' style='font-size:17px;letter-spacing:.34em'>Case</div><div style='font-size:34px;color:#f2eadb;margin:2px 0 14px'>Steel</div>
 <div class='cap gold' style='font-size:17px;letter-spacing:.34em'>Price</div><div style='font-size:38px;color:#f2eadb;margin-top:2px;letter-spacing:.04em'>AED 115,000</div></div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.4)'>__D__</div>""".replace("__D__", DISC_R)
    return page("available_4_editorial", "background:linear-gradient(180deg,#121315,#0a0a0c)", body)


def av5_macro():  # Day-Date 40 228238 dial macro
    body = """
<img class='a' src='../assets/dial_macro.png' style='left:50%;top:360px;width:1180px;transform:translateX(-50%)'>
<div class='a' style='inset:0;background:radial-gradient(ellipse 620px 640px at 50% 38%,transparent 30%,rgba(5,5,5,.88) 78%,#050505 100%)'></div>
<div class='a' style='left:0;right:0;top:330px;height:300px;background:linear-gradient(180deg,#050505 10%,rgba(5,5,5,.0))'></div>
<div class='a c cap gold' style='top:270px'>Advance Watch Co</div>
<div class='rule' style='left:420px;width:240px;top:1285px'></div>
<div class='a c' style='top:1316px;font-size:60px;font-weight:500;color:#f2eadb'>Day-Date 40</div>
<div class='a c' style='top:1396px;font-size:30px;font-style:italic;color:#cdb07a'>Yellow gold · Green dial · Reference 228238</div>
<div class='a c cap' style='top:1456px;color:rgba(242,234,219,.8);font-size:21px'>Now available &nbsp;·&nbsp; AED 242,000</div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.4)'>__D__</div>""".replace("__D__", DISC_R)
    return page("available_5_dial_macro", "background:#050505", body)


# ================= KNOWLEDGE =================
def k1_note():
    body = """
<div class='a c cap gold' style='top:300px'>A note from the counter</div>
<div class='a c' style='top:420px;font-size:200px;line-height:.6;color:#cdb07a;font-family:Play,serif'>“</div>
<div class='a' style='left:110px;right:110px;top:560px;text-align:center;font-size:92px;line-height:1.12;font-weight:500;color:#f2eadb'>A smooth sweeping hand <span style='font-style:italic;color:#cdb07a'>proves nothing.</span></div>
<div class='rule' style='left:420px;width:240px;top:1010px'></div>
<div class='a' style='left:150px;right:150px;top:1060px;text-align:center;font-size:36px;line-height:1.35;color:rgba(242,234,219,.82)'>The better fakes sweep too. Check the Cyclops, which should magnify the date two and a half times, the tiny crown etched on the crystal at six o’clock, and the weight of the watch.</div>
<div class='a c cap gold' style='top:1420px;font-size:19px'>Advance Watch Co</div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.4)'>__D__</div>""".replace("__D__", DISC_K)
    return page("knowledge_1_collectors_note", "background:radial-gradient(1000px 900px at 50% 30%,#1a1814,#08080a 75%)", body)


def k2_checks():
    items = [("I", "Photos or a video of the exact watch", "with today’s date, showing the reference and the serial number"),
             ("II", "A full set that matches", "the numbers on the watch must match the card and the papers"),
             ("III", "A recent warranty date", "a brand new watch should carry a recent one")]
    rows = ""
    y = 560
    for i, (n, h, d) in enumerate(items):
        rows += f"""<div class='a' style='left:110px;top:{y}px;width:120px;font-size:104px;font-weight:300;color:#cdb07a;font-family:Corm,serif;line-height:1'>{n}</div>
<div class='a' style='left:270px;right:100px;top:{y+6}px;font-size:46px;font-weight:500;color:#f2eadb;line-height:1.1'>{h}</div>
<div class='a' style='left:270px;right:110px;top:{y+110}px;font-size:30px;font-style:italic;color:rgba(242,234,219,.7);line-height:1.25'>{d}</div>"""
        if i < 2:
            rows += f"<div class='rule' style='left:110px;right:110px;top:{y+226}px;opacity:.7'></div>"
        y += 276
    body = f"""<div class='a c cap gold' style='top:300px'>Three checks before you pay</div>
<div class='a c' style='top:372px;font-size:84px;font-weight:500;color:#f2eadb'>For any Rolex</div>
<div class='rule' style='left:110px;right:110px;top:500px'></div>{rows}
<div class='a c' style='top:1430px;font-size:32px;font-style:italic;color:#cdb07a'>Save this for the day you buy.</div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.4)'>{DISC_K}</div>"""
    return page("knowledge_2_three_checks", "background:linear-gradient(180deg,#0f1012,#070708)", body)


def k3_five():
    body = """
<div class='a c cap gold' style='top:300px'>The Rolex guarantee</div>
<div class='a c' style='top:330px;font-size:690px;line-height:1;font-weight:300;font-family:Corm,serif;color:transparent;-webkit-text-stroke:2.5px #cdb07a;letter-spacing:-.02em'>5</div>
<div class='a c' style='top:1150px;font-size:76px;font-weight:500;color:#f2eadb;letter-spacing:.34em'>YEARS</div>
<div class='rule' style='left:420px;width:240px;top:1260px'></div>
<div class='a' style='left:150px;right:150px;top:1300px;text-align:center;font-size:36px;line-height:1.35;color:rgba(242,234,219,.82)'>It begins on the date printed on the card, the date of the sale. A recent date means most of it is still ahead of you. <span style='font-style:italic;color:#cdb07a'>Check it before you pay.</span></div>
<div class='tiny' style='top:1578px;color:rgba(242,234,219,.4)'>__D__</div>""".replace("__D__", DISC_R)
    return page("knowledge_3_five_years", "background:radial-gradient(1000px 1000px at 50% 36%,#1b1913,#08080a 72%)", body)


def k4_qa():
    body = """
<div class='a' style='left:70px;right:70px;top:262px;bottom:342px;border:1px solid rgba(156,122,60,.6)'></div>
<div class='a c cap' style='top:330px;color:#9c7a3c'>Ask us anything</div>
<div class='a c' style='top:420px;font-size:44px;font-style:italic;color:#9c7a3c'>The question</div>
<div class='a' style='left:130px;right:130px;top:490px;text-align:center;font-size:96px;line-height:1.08;font-weight:500;color:#1c1812'>Why can’t I simply walk in and buy a Daytona?</div>
<div class='rule' style='left:420px;width:240px;top:930px;background:linear-gradient(90deg,transparent,#9c7a3c 20%,#9c7a3c 80%,transparent)'></div>
<div class='a c' style='top:980px;font-size:44px;font-style:italic;color:#9c7a3c'>The answer</div>
<div class='a' style='left:150px;right:150px;top:1050px;text-align:center;font-size:37px;line-height:1.38;color:#3a3226'>Demand is much bigger than supply. Boutiques keep waiting lists, and in our experience clients with a purchase history are offered the watches first. A dealer can often source the watch in one to forty-eight hours, depending on the model.</div>
<div class='tiny' style='top:1500px;color:rgba(28,24,18,.45)'>__D__</div>""".replace("__D__", DISC_K)
    return page("knowledge_4_question_answer", "background:radial-gradient(1100px 1100px at 50% 35%,#f4eee2,#e6dcc8)", body)


NAMES_A = [av1_window, av2_ivory, av3_emerald, av4_editorial, av5_macro]
NAMES_K = [k1_note, k2_checks, k3_five, k4_qa]


def render(names):
    js = """const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of %s){await p.goto('file://'+path.resolve('templates/'+n+'.html'));await p.waitForTimeout(900);
await p.screenshot({path:'previews/'+n+'.png'});}
await b.close()})();""" % json.dumps(names)
    (ROOT / "_shot.js").write_text(js)
    subprocess.run(["node", "_shot.js"], cwd=ROOT, check=True)


def sheet(names, title, out, labels):
    W, H = 360, 640
    img = Image.new("RGB", (len(names) * (W + 16) + 16, H + 90), (14, 14, 16))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype(str(ROOT / "fonts" / "Cormorant.ttf"), 26)
    except Exception:
        f = ImageFont.load_default()
    d.text((16, 14), title, fill=(205, 176, 122), font=f)
    for i, n in enumerate(names):
        im = Image.open(PRE / f"{n}.png").convert("RGB").resize((W, H), Image.LANCZOS)
        x = 16 + i * (W + 16)
        img.paste(im, (x, 54))
        d.text((x, 54 + H + 8), labels[i], fill=(230, 220, 200), font=f)
    img.save(PRE / out, quality=93)


if __name__ == "__main__":
    A = [f() for f in NAMES_A]
    K = [f() for f in NAMES_K]
    render(A + K)
    sheet(A, "AVAILABLE NOW  ·  five luxury directions", "sheet_luxury_available_now.jpg",
          ["1 Boutique window", "2 Ivory plate", "3 Emerald velvet", "4 Editorial", "5 Dial macro"])
    sheet(K, "KNOWLEDGE  ·  four luxury directions", "sheet_luxury_knowledge.jpg",
          ["1 The collector's note", "2 Three checks", "3 One numeral", "4 Question and answer"])
    print("done")

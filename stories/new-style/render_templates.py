#!/usr/bin/env python3
"""Build the 8 story templates (4 AVAILABLE NOW + 4 KNOWLEDGE) with real sample content, write the HTML to templates/,
render PNG previews with Playwright (Chromium), and make one preview sheet per type.
Usage: NODE_PATH=... python3 render_templates.py   (needs `playwright` for node; uses a tiny node helper)"""
import json, subprocess, os
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
TPL = ROOT / "templates"
PRE = ROOT / "previews"
TPL.mkdir(exist_ok=True); PRE.mkdir(exist_ok=True)

CSS = """
@font-face{font-family:'OswaldX';src:url('../assets/oswald.ttf');font-weight:200 700}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000;font-family:'OswaldX',sans-serif;color:#fff}
#s{position:relative;width:1080px;height:1920px;overflow:hidden}
.abs{position:absolute}
.c{left:0;right:0;text-align:center}
.gold{color:#e6c27a}
.brand{position:absolute;left:0;right:0;top:262px;text-align:center;font-size:30px;letter-spacing:10px;color:#e6c27a;font-weight:500}
.foot{position:absolute;left:0;right:0;top:1592px;text-align:center;font-size:23px;letter-spacing:2px;color:rgba(255,255,255,.55);font-weight:400}
.cta{position:absolute;left:50%;transform:translateX(-50%);top:1500px;background:#25d366;color:#04230f;font-size:42px;font-weight:700;letter-spacing:2px;padding:6px 44px 10px;border-radius:60px;box-shadow:0 10px 30px rgba(37,211,102,.45);white-space:nowrap}
.pill{display:inline-block;background:#18c964;color:#03200e;font-weight:700;border-radius:16px;padding:4px 30px 8px;box-shadow:0 10px 28px rgba(24,201,100,.4)}
.req{display:inline-block;border:3px solid #e6c27a;color:#e6c27a;font-weight:700;border-radius:16px;padding:6px 26px 8px;letter-spacing:2px}
.w{filter:drop-shadow(0 26px 34px rgba(0,0,0,.8))}
"""

DISC_ROLEX = "INDEPENDENT DEALER  ·  NOT AFFILIATED WITH ROLEX"
DISC = "ADVANCE WATCH CO  ·  WHATSAPP IN BIO"


def page(name, bg, body):
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div id='s' style='{bg}'>{body}</div></body></html>"
    (TPL / f"{name}.html").write_text(html)
    return name


def aed(n):
    return f"AED {n:,}"


# ---------------- AVAILABLE NOW ----------------
def avail_spotlight():
    body = """
<div class='abs' style='left:-300px;top:120px;width:1680px;height:1680px;opacity:.55;background:repeating-conic-gradient(from 0deg at 50% 50%,rgba(230,194,122,.35) 0deg 5deg,rgba(0,0,0,0) 5deg 18deg);-webkit-mask-image:radial-gradient(circle at 50% 50%,#000 0,transparent 56%)'></div>
<div class='brand'>ADVANCE WATCH CO</div>
<div class='abs' style='left:60px;top:372px;transform:rotate(-9deg);border:6px solid #e6c27a;color:#e6c27a;font-size:64px;font-weight:700;letter-spacing:4px;padding:2px 26px 8px;border-radius:10px;background:rgba(0,0,0,.35);box-shadow:0 0 30px rgba(230,194,122,.35)'>JUST SOURCED</div>
<div class='abs' style='right:60px;top:386px;background:#e01f1f;font-size:40px;font-weight:700;letter-spacing:3px;padding:4px 22px 8px;border-radius:12px'>HIGH DEMAND</div>
<img class='abs w' src='../assets/pepsi.png' style='left:50%;top:480px;height:745px;transform:translateX(-50%) rotate(4deg)'>
<div class='abs c' style='top:1240px;font-size:92px;font-weight:700;line-height:1'>GMT-MASTER II <span class='gold'>PEPSI</span></div>
<div class='abs c gold' style='top:1345px;font-size:34px;letter-spacing:5px;font-weight:500'>126710BLRO  ·  STEEL  ·  JUBILEE</div>
<div class='abs c' style='top:1398px;font-size:62px'><span class='pill'>AED 99,000</span></div>
<div class='cta' style='top:1512px'>DM TO RESERVE</div>
<div class='foot'>__DISC__</div>""".replace("__DISC__", DISC_ROLEX)
    return page("available_A_spotlight", "background:radial-gradient(900px 900px at 50% 40%,#4a3410 0%,#17110a 45%,#07070a 100%)", body)


def avail_card():
    body = """
<div class='brand'>ADVANCE WATCH CO</div>
<div class='abs c' style='top:318px'><span style='display:inline-block;background:linear-gradient(90deg,#ff3b2f,#ff8a2f);font-size:58px;font-weight:700;letter-spacing:4px;padding:4px 36px 10px;border-radius:14px;box-shadow:0 0 40px rgba(255,80,40,.6)'>HIGH DEMAND</span></div>
<div class='abs' style='left:90px;right:90px;top:440px;height:640px;border-radius:36px;background:linear-gradient(160deg,#1c2433,#0b0f17);border:2px solid rgba(230,194,122,.5);box-shadow:0 20px 60px rgba(0,0,0,.6)'></div>
<img class='abs w' src='../assets/daytona.png' style='left:50%;top:470px;height:590px;transform:translateX(-50%)'>
<div class='abs c' style='top:1090px;font-size:76px;font-weight:700;line-height:1'>ROLEX DAYTONA <span class='gold'>STEEL</span></div>
<div class='abs c gold' style='top:1180px;font-size:32px;letter-spacing:5px;font-weight:500'>126500LN  ·  BLACK DIAL</div>
<div class='abs' style='left:90px;top:1245px;width:440px;height:225px;border-radius:24px;background:rgba(224,31,31,.18);border:3px solid #e01f1f;text-align:center'>
 <div style='font-size:30px;letter-spacing:3px;color:#ff8a8a;margin-top:18px'>BOUTIQUE WAIT</div><div style='font-size:60px;font-weight:700;line-height:1.05;margin-top:8px'>ABOUT<br>5 YEARS*</div></div>
<div class='abs' style='right:90px;top:1245px;width:440px;height:225px;border-radius:24px;background:rgba(24,201,100,.18);border:3px solid #18c964;text-align:center'>
 <div style='font-size:30px;letter-spacing:3px;color:#7dffb0;margin-top:18px'>WE SOURCE IT</div><div style='font-size:60px;font-weight:700;line-height:1.05;margin-top:8px'>1 TO 48<br>HOURS</div></div>
<div class='abs c' style='top:1486px;font-size:52px'><span class='pill'>AED 119,000</span></div>
<div class='abs c' style='top:1566px;font-size:21px;color:rgba(255,255,255,.55);letter-spacing:1px'>*APPROXIMATE, DEPENDS ON THE WATCH  ·  WHATSAPP IN BIO</div>
<div class='foot' style='top:1596px;font-size:20px'>__DISC__</div>""".replace("__DISC__", DISC_ROLEX)
    return page("available_B_high_demand_card", "background:linear-gradient(180deg,#0a0d14 0%,#101624 50%,#05060a 100%)", body)


def avail_split():
    body = """
<div class='abs' style='inset:0;background:linear-gradient(115deg,#0b1220 0%,#0b1220 49%,#e6c27a 49%,#e6c27a 50%,#0f2a1c 50%,#0a1a12 100%)'></div>
<div class='brand'>ADVANCE WATCH CO</div>
<div class='abs c' style='top:318px;font-size:64px;font-weight:700;letter-spacing:3px'>WHICH ONE? <span class='gold'>REPLY 1 OR 2</span></div>
<div class='abs' style='left:40px;top:430px;width:70px;height:70px;border-radius:50%;border:4px solid #e6c27a;font-size:46px;font-weight:700;text-align:center;line-height:62px;color:#e6c27a'>1</div>
<div class='abs' style='right:40px;top:430px;width:70px;height:70px;border-radius:50%;border:4px solid #e6c27a;font-size:46px;font-weight:700;text-align:center;line-height:62px;color:#e6c27a'>2</div>
<img class='abs w' src='../assets/sub.png' style='left:70px;top:470px;height:610px;transform:rotate(-6deg)'>
<img class='abs w' src='../assets/nautilus.png' style='right:75px;top:500px;height:560px;transform:rotate(6deg)'>
<div class='abs' style='left:30px;width:490px;top:1110px;text-align:center'><div style='font-size:50px;font-weight:700;line-height:1'>SUBMARINER<br>DATE</div><div class='gold' style='font-size:28px;letter-spacing:3px;margin-top:8px'>126610LN  ·  STEEL</div><div style='font-size:46px;margin-top:16px'><span class='pill'>AED 59,000</span></div></div>
<div class='abs' style='right:30px;width:490px;top:1110px;text-align:center'><div style='font-size:50px;font-weight:700;line-height:1'>PATEK NAUTILUS<br>5711/1A-001</div><div class='gold' style='font-size:28px;letter-spacing:3px;margin-top:8px'>STEEL  ·  BLUE DIAL</div><div style='font-size:30px;margin-top:20px'><span class='req'>REQUEST PRICE<br>ON WHATSAPP</span></div></div>
<div class='cta' style='top:1480px'>DM YOUR PICK</div>
<div class='foot'>__DISC__</div>""".replace("__DISC__", "ADVANCE WATCH CO  ·  INDEPENDENT DEALER  ·  NOT AFFILIATED WITH ROLEX OR PATEK")
    return page("available_C_split", "background:#0b1220", body)


def avail_ticket():
    body = """
<div class='brand'>ADVANCE WATCH CO</div>
<div class='abs' style='left:80px;top:335px;width:920px;height:1130px;transform:rotate(-2deg);border-radius:34px;background:linear-gradient(160deg,#f6e7c3,#e2bd6f);box-shadow:0 30px 70px rgba(0,0,0,.7);color:#1a1205'>
 <div class='abs' style='left:-34px;top:520px;width:68px;height:68px;border-radius:50%;background:#14100a'></div>
 <div class='abs' style='right:-34px;top:520px;width:68px;height:68px;border-radius:50%;background:#14100a'></div>
 <div class='abs' style='left:40px;right:40px;top:545px;border-top:5px dashed rgba(26,18,5,.45)'></div>
 <div class='abs' style='left:50px;top:36px;font-size:30px;letter-spacing:6px;font-weight:600'>WATCH PASS</div>
 <div class='abs' style='right:50px;top:30px;font-size:44px;font-weight:700;color:#8b1a1a;border:4px solid #8b1a1a;padding:0 16px 4px;transform:rotate(4deg);border-radius:8px'>HIGH DEMAND</div>
 <img class='abs' src='../assets/dj.png' style='left:30px;top:90px;height:430px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.4))'>
 <div class='abs' style='left:290px;top:110px;font-size:98px;font-weight:700;line-height:.95'>DATEJUST<br>41</div>
 <div class='abs' style='left:290px;top:305px;font-size:36px;letter-spacing:3px;font-weight:500'>GREEN OMBRÉ  ·  JUBILEE</div>
 <div class='abs' style='left:290px;top:365px;font-size:36px;letter-spacing:3px;font-weight:500'>STEEL &amp; WHITE GOLD</div>
 <div class='abs' style='left:290px;top:425px;font-size:36px;letter-spacing:3px;font-weight:500'>REF 126334</div>
 <div class='abs' style='left:50px;top:600px;font-size:26px;letter-spacing:4px;font-weight:600;opacity:.7'>SOURCING</div>
 <div class='abs' style='left:50px;top:635px;font-size:70px;font-weight:700'>1 TO 48 HOURS</div>
 <div class='abs' style='right:50px;top:600px;font-size:26px;letter-spacing:4px;font-weight:600;opacity:.7;text-align:right'>PRICE</div>
 <div class='abs' style='right:50px;top:635px;font-size:70px;font-weight:700;color:#0a6b35'>AED 63,000</div>
 <div class='abs' style='left:50px;top:780px;font-size:26px;letter-spacing:4px;font-weight:600;opacity:.7'>DELIVERY</div>
 <div class='abs' style='left:50px;top:815px;font-size:48px;font-weight:600'>SAME DAY IN DUBAI</div>
 <div class='abs' style='left:50px;top:880px;font-size:30px;font-weight:500;opacity:.8'>24 TO 48 HOURS ACROSS THE UAE</div>
 <div class='abs' style='left:50px;right:50px;top:960px;height:90px;background:repeating-linear-gradient(90deg,#1a1205 0 6px,transparent 6px 10px,#1a1205 10px 13px,transparent 13px 20px,#1a1205 20px 22px,transparent 22px 28px);opacity:.85'></div>
 <div class='abs' style='left:50px;top:1062px;font-size:30px;letter-spacing:5px;font-weight:600'>ADMIT ONE WRIST</div>
</div>
<div class='cta' style='top:1520px'>DM TO CLAIM</div>
<div class='foot' style='top:1598px'>__DISC__</div>""".replace("__DISC__", DISC_ROLEX)
    return page("available_D_ticket", "background:radial-gradient(900px 900px at 50% 30%,#2a1f10,#0c0a07 70%)", body)


# ---------------- KNOWLEDGE ----------------
def know_myth():
    body = """
<div class='brand'>KNOW BEFORE YOU BUY</div>
<div class='abs' style='left:60px;right:60px;top:340px;height:560px;border-radius:32px;background:linear-gradient(160deg,#5a0f0f,#2a0707);border:3px solid #e01f1f;box-shadow:0 0 50px rgba(224,31,31,.35)'>
 <div class='abs' style='left:40px;top:26px;font-size:64px;font-weight:700;color:#ff5a5a;letter-spacing:6px'>✖ MYTH</div>
 <div class='abs' style='left:40px;right:40px;top:140px;font-size:70px;font-weight:700;line-height:1.05'>A SMOOTH SWEEPING SECONDS HAND PROVES A ROLEX IS REAL</div></div>
<div class='abs' style='left:60px;right:60px;top:940px;height:560px;border-radius:32px;background:linear-gradient(160deg,#0d4a2a,#06220f);border:3px solid #18c964;box-shadow:0 0 50px rgba(24,201,100,.3)'>
 <div class='abs' style='left:40px;top:26px;font-size:64px;font-weight:700;color:#4dffa0;letter-spacing:6px'>✔ FACT</div>
 <div class='abs' style='left:40px;right:40px;top:130px;font-size:46px;font-weight:600;line-height:1.15'>The better fakes sweep too. A smooth sweep proves nothing.<br><span class='gold'>Also check:</span> the Cyclops magnifies the date 2.5 times, the tiny crown etched on the crystal at six o'clock, and the weight.</div></div>
<div class='foot' style='top:1560px'>SAVE THIS  ·  ADVANCE WATCH CO</div>"""
    return page("knowledge_A_myth_vs_fact", "background:radial-gradient(900px 900px at 50% 20%,#241a12,#0a0907 70%)", body)


def know_checklist():
    rows = [("1", "Photos or a video of the exact watch", "with today's date, showing the reference and the serial number"),
            ("2", "A full set that matches", "the numbers on the watch must match the card and the papers"),
            ("3", "A recent warranty date", "a brand new watch should have a recent one")]
    r = ""
    for i, (n, t, s) in enumerate(rows):
        top = 560 + i * 315
        r += f"""<div class='abs' style='left:60px;right:60px;top:{top}px;height:290px;border-radius:30px;background:linear-gradient(160deg,#1b1a17,#0e0d0b);border:2px solid rgba(230,194,122,.55)'>
 <div class='abs' style='left:34px;top:40px;width:150px;height:150px;border-radius:50%;background:linear-gradient(160deg,#f2d27f,#c99a2c);color:#1a1205;font-size:118px;font-weight:700;text-align:center;line-height:150px'>{n}</div>
 <div class='abs' style='left:230px;right:34px;top:34px;font-size:56px;font-weight:700;line-height:1.02'>{t}</div>
 <div class='abs' style='left:230px;right:34px;top:170px;font-size:34px;color:rgba(255,255,255,.75);line-height:1.15'>{s}</div>
 <div class='abs' style='right:34px;top:216px;font-size:46px;color:#18c964;font-weight:700'>✔</div></div>"""
    body = f"""
<div class='brand'>CHECKLIST</div>
<div class='abs c' style='top:318px;font-size:96px;font-weight:700;line-height:1'>3 CHECKS<br><span class='gold'>BEFORE YOU PAY</span></div>
{r}
<div class='abs c gold' style='top:1536px;font-size:40px;font-weight:700;letter-spacing:3px'>SAVE THIS  ·  SEND IT TO A FRIEND</div>
<div class='foot' style='top:1598px'>ADVANCE WATCH CO  ·  ANY ROLEX, ANY SELLER</div>"""
    return page("knowledge_B_checklist", "background:radial-gradient(900px 900px at 50% 15%,#2a2114,#0a0907 70%)", body)


def know_bignumber():
    body = """
<div class='brand'>DID YOU KNOW</div>
<div class='abs c' style='top:300px;font-size:720px;font-weight:700;line-height:.9;letter-spacing:-10px;background:linear-gradient(180deg,#fff3c4,#d49c2a 55%,#7a5410);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 14px 40px rgba(212,156,42,.35))'>5</div>
<div class='abs c' style='top:1020px;font-size:130px;font-weight:700;letter-spacing:10px'>YEARS</div>
<div class='abs c gold' style='top:1170px;font-size:50px;font-weight:600;letter-spacing:3px'>ROLEX GUARANTEE</div>
<div class='abs' style='left:90px;right:90px;top:1260px;border-radius:26px;background:rgba(255,255,255,.07);border:2px solid rgba(230,194,122,.5);padding:26px 34px 30px;font-size:42px;line-height:1.18;text-align:center'>It starts on the date on the warranty card: <b>the date of the sale.</b><br><span class='gold'>A recent date means most of it is still ahead of you. Check it before you pay.</span></div>
<div class='foot' style='top:1596px'>SAVE THIS  ·  ADVANCE WATCH CO  ·  NOT AFFILIATED WITH ROLEX</div>"""
    return page("knowledge_C_big_number", "background:radial-gradient(1000px 1000px at 50% 28%,#3a2a10,#0b0906 65%)", body)


def know_qa():
    body = """
<div class='brand'>ASK US ANYTHING</div>
<div class='abs' style='left:60px;top:380px;width:760px;border-radius:44px 44px 44px 8px;background:#2a2f3a;padding:36px 44px 40px;box-shadow:0 14px 40px rgba(0,0,0,.5)'>
 <div style='font-size:34px;color:#9fb0c8;letter-spacing:3px;margin-bottom:10px'>QUESTION</div>
 <div style='font-size:80px;font-weight:700;line-height:1.02'>WHY CAN'T I JUST WALK IN AND BUY A DAYTONA?</div></div>
<div class='abs' style='right:60px;top:830px;width:850px;border-radius:44px 44px 8px 44px;background:linear-gradient(160deg,#f2d27f,#c99a2c);color:#1a1205;padding:36px 44px 42px;box-shadow:0 14px 40px rgba(0,0,0,.5)'>
 <div style='font-size:34px;letter-spacing:3px;margin-bottom:10px;opacity:.7'>ANSWER</div>
 <div style='font-size:60px;font-weight:700;line-height:1.05'>DEMAND IS MUCH BIGGER THAN SUPPLY.</div>
 <div style='font-size:42px;font-weight:500;line-height:1.15;margin-top:18px'>Boutiques have waiting lists, and in our experience clients with a purchase history are offered the watches first.</div></div>
<div class='abs c' style='top:1380px;font-size:44px;color:#4dffa0;font-weight:700;letter-spacing:2px'>WE SOURCE FROM 1 HOUR UP TO 48 HOURS</div>
<div class='abs c' style='top:1440px;font-size:30px;color:rgba(255,255,255,.7)'>depending on the watch</div>
<div class='foot' style='top:1596px'>SEND US YOUR QUESTION  ·  ADVANCE WATCH CO  ·  WHATSAPP IN BIO</div>"""
    return page("knowledge_D_question_answer", "background:linear-gradient(180deg,#0c1018,#141a26 60%,#07090d)", body)


names = [avail_spotlight(), avail_card(), avail_split(), avail_ticket(), know_myth(), know_checklist(), know_bignumber(), know_qa()]

JS = """
const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of %s){await p.goto('file://'+path.resolve('templates',n+'.html'));await p.waitForTimeout(500);
await p.screenshot({path:'previews/'+n+'.png'});}
await b.close()})();
""" % json.dumps(names)
(ROOT / "_shot.js").write_text(JS)
subprocess.run(["node", "_shot.js"], cwd=ROOT, check=True)
(ROOT / "_shot.js").unlink()


def sheet(prefix, title, out):
    fs = [f for f in names if f.startswith(prefix)]
    w, h = 405, 720
    S = Image.new("RGB", (w * 4 + 50, h + 90), (14, 14, 16))
    from PIL import ImageDraw
    d = ImageDraw.Draw(S)
    d.text((16, 10), title, fill=(230, 194, 122))
    for i, f in enumerate(fs):
        im = Image.open(PRE / f"{f}.png").convert("RGB").resize((w, h))
        S.paste(im, (10 + i * (w + 10), 60))
        d.text((14 + i * (w + 10), 60 + h + 10), f.split("_", 1)[1].replace("_", " "), fill=(200, 200, 200))
    S.save(PRE / out, quality=92)


sheet("available", "AVAILABLE NOW: four new templates (real watches, real store prices)", "sheet_available_now.jpg")
sheet("knowledge", "KNOWLEDGE: four new templates (facts from confirmed notes)", "sheet_knowledge.jpg")
print("done", names)

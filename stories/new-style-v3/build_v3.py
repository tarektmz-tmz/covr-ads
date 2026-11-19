#!/usr/bin/env python3
"""Round 3 story designs: Inter (the store's heading font) + the store palette, big readable type.
4 AVAILABLE NOW + 3 KNOWLEDGE, 1080x1920, key content inside y 250-1580.
Run: NODE_PATH=/opt/node22/lib/node_modules python3 build_v3.py"""
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
TPL, PRE = ROOT / "templates", ROOT / "previews"
TPL.mkdir(exist_ok=True); PRE.mkdir(exist_ok=True)

# store palette (from the theme CSS)
NAVY, NAVY2, GOLD, GOLDL, CREAM, INK, MUT = "#0b1a33", "#112448", "#c9a24b", "#e3c47a", "#f6f2ea", "#16181d", "#5d6370"

CSS = f"""
@font-face{{font-family:'Inter';src:url('../fonts/Inter.ttf');font-weight:100 900;font-style:normal}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#000}}
#s{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Inter',sans-serif;color:{CREAM};letter-spacing:-.01em}}
.a{{position:absolute}}.c{{left:0;right:0;text-align:center}}
.bar{{position:absolute;height:12px;background:linear-gradient(90deg,{GOLD},{GOLDL});border-radius:2px}}
.legal{{position:absolute;left:0;right:0;text-align:center;font-size:30px;line-height:1.35;font-weight:500;letter-spacing:.02em}}
.dark{{background:radial-gradient(1000px 1000px at 50% 38%,#1d3b70 0%,{NAVY} 55%,#060d1c 100%)}}
.rays{{position:absolute;left:50%;top:50%;width:2200px;height:2200px;transform:translate(-50%,-50%);
 background:repeating-conic-gradient(from 0deg,rgba(227,196,122,.10) 0deg 5deg,transparent 5deg 15deg);
 -webkit-mask-image:radial-gradient(circle,#000 0,transparent 55%)}}
.btn{{display:inline-block;border:4px solid {GOLD};color:{GOLDL};border-radius:14px;padding:12px 30px 16px;font-size:52px;font-weight:700}}
"""

LEGAL_R = "Independent dealer · Not affiliated with Rolex · WhatsApp in bio"


def page(name, cls, body, bg=""):
    (TPL / f"{name}.html").write_text(
        f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
        f"<body><div id='s' class='{cls}' style=\"{bg}\">{body}</div></body></html>")
    return name


# ---------------------------------------------------------------- AVAILABLE NOW
def av1():  # navy hero, big left-aligned headline, centred hero watch with reflection
    return page("available_1_hero", "dark", f"""
<div class='rays' style='top:900px'></div>
<div class='bar' style='left:80px;top:262px;width:200px'></div>
<div class='a' style='left:80px;top:292px;font-size:128px;font-weight:800;line-height:.95;letter-spacing:-.03em'>AVAILABLE<br><span style='color:{GOLDL}'>NOW</span></div>
<div class='a' style='right:80px;top:310px;text-align:right;font-size:56px;font-weight:600;color:{GOLDL};line-height:1.15'>HIGH<br>DEMAND</div>
<img class='a' src='../assets/sub.png' style='left:50%;top:540px;height:830px;transform:translateX(-50%);
 -webkit-box-reflect:below 0 linear-gradient(transparent 70%,rgba(255,255,255,.22));filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))'>
<div class='a' style='left:80px;top:1378px;font-size:104px;font-weight:800;letter-spacing:-.03em'>SUBMARINER DATE</div>
<div class='a' style='left:80px;top:1494px;font-size:44px;font-weight:500;color:{GOLDL}'>Ref. 126610LN · Steel · Black dial</div>
<div class='a' style='left:80px;top:1550px;font-size:104px;font-weight:800;letter-spacing:-.02em;color:{CREAM}'>AED 59,000</div>
<div class='a' style='right:80px;top:1575px'><span class='btn'>DM to order</span></div>
<div class='legal' style='top:1690px;color:rgba(246,242,234,.6)'>{LEGAL_R}</div>""")


def av2():  # cream editorial: giant navy type left, watch bleeding right
    return page("available_2_cream", "", f"""
<div class='a' style='inset:0;background:linear-gradient(160deg,{CREAM} 0%,#ebe3d2 100%)'></div>
<div class='a' style='left:0;top:0;width:60px;height:1920px;background:{NAVY}'></div>
<div class='a' style='left:110px;top:262px;font-size:60px;font-weight:700;letter-spacing:.14em;color:{GOLD}'>HIGH DEMAND</div>
<div class='a' style='left:110px;top:340px;font-size:132px;font-weight:900;line-height:.9;letter-spacing:-.05em;color:{NAVY}'>AVAILABLE<br><span style='color:{GOLD};font-size:230px;line-height:.9'>NOW</span></div>
<img class='a' src='../assets/daytona.png' style='right:-60px;top:600px;height:960px;filter:drop-shadow(0 40px 36px rgba(11,26,51,.35))'>
<div class='a' style='left:110px;top:1240px;width:560px;font-size:110px;font-weight:900;line-height:.95;letter-spacing:-.04em;color:{NAVY}'>DAYTONA</div>
<div class='a' style='left:110px;top:1362px;width:520px;font-size:46px;font-weight:600;line-height:1.2;color:{MUT}'>Ref. 126500LN<br>Steel · Black dial</div>
<div class='a' style='left:110px;top:1480px;font-size:100px;font-weight:900;letter-spacing:-.03em;color:{NAVY}'>AED 119,000</div>
<div class='a' style='left:110px;top:1600px;font-size:50px;font-weight:700;color:{GOLD}'>DM to order</div>
<div class='legal' style='top:1690px;color:{MUT}'>{LEGAL_R}</div>""")


def av3():  # dial close-up, dramatic crop, headline at the bottom
    return page("available_3_dial_closeup", "dark", f"""
<img class='a' src='../assets/dj.png' style='left:50%;top:-330px;height:2250px;transform:translateX(-50%);filter:saturate(1.08)'>
<div class='a' style='inset:0;background:linear-gradient(180deg,rgba(6,13,28,.96) 0%,rgba(6,13,28,.85) 15%,rgba(6,13,28,0) 27%,rgba(6,13,28,0) 48%,rgba(6,13,28,.92) 72%,{NAVY} 100%)'></div>
<div class='a' style='left:80px;top:262px;font-size:64px;font-weight:800;letter-spacing:.14em;color:{CREAM}'>AVAILABLE NOW</div>
<div class='bar' style='left:80px;top:344px;width:160px'></div>
<div class='a' style='left:80px;top:1190px;font-size:164px;font-weight:900;line-height:.9;letter-spacing:-.05em'>DATEJUST<br><span style='color:{GOLDL}'>41</span></div>
<div class='a' style='left:80px;top:1502px;font-size:46px;font-weight:600;color:{GOLDL}'>Ref. 126334 · Green ombré · Jubilee</div>
<div class='a' style='left:80px;top:1560px;font-size:100px;font-weight:900;letter-spacing:-.03em'>AED 73,400</div>
<div class='a' style='right:80px;top:1584px'><span class='btn'>DM to order</span></div>
<div class='legal' style='top:1690px;color:rgba(246,242,234,.65)'>{LEGAL_R}</div>""")


def av4():  # two high-demand GMT-Master II side by side
    return page("available_4_pair", "dark", f"""
<div class='rays' style='top:880px'></div>
<div class='bar' style='left:50%;top:262px;width:200px;transform:translateX(-50%)'></div>
<div class='a c' style='top:296px;font-size:118px;font-weight:900;line-height:.98;letter-spacing:-.04em'>HIGH-DEMAND<br><span style='color:{GOLDL}'>GMT-MASTER II</span></div>
<div class='a' style='left:540px;top:620px;width:3px;height:700px;background:linear-gradient(transparent,{GOLD},transparent)'></div>
<img class='a' src='../assets/batman.png' style='left:30px;top:600px;height:700px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.6))'>
<img class='a' src='../assets/pepsi.png' style='right:30px;top:600px;height:700px;filter:drop-shadow(0 30px 34px rgba(0,0,0,.6))'>
<div class='a' style='left:0;width:540px;top:1330px;text-align:center;font-size:76px;font-weight:800;letter-spacing:-.03em'>BATMAN</div>
<div class='a' style='left:540px;width:540px;top:1330px;text-align:center;font-size:76px;font-weight:800;letter-spacing:-.03em'>PEPSI</div>
<div class='a' style='left:0;width:540px;top:1425px;text-align:center;font-size:64px;font-weight:700;color:{GOLDL}'>AED 68,000</div>
<div class='a' style='left:540px;width:540px;top:1425px;text-align:center;font-size:64px;font-weight:700;color:{GOLDL}'>AED 115,000</div>
<div class='a' style='left:0;width:540px;top:1516px;text-align:center;font-size:40px;font-weight:600;color:rgba(246,242,234,.8)'>Ref. 126710BLNR</div>
<div class='a' style='left:540px;width:540px;top:1516px;text-align:center;font-size:40px;font-weight:600;color:rgba(246,242,234,.8)'>Ref. 126710BLRO</div>
<div class='a c' style='top:1585px'><span class='btn'>Reply 1 or 2 to order</span></div>
<div class='legal' style='top:1700px;color:rgba(246,242,234,.6)'>{LEGAL_R}</div>""")


# ---------------------------------------------------------------- KNOWLEDGE
def k1():  # myth vs fact
    return page("knowledge_1_myth_fact", "dark", f"""
<div class='bar' style='left:80px;top:262px;width:200px'></div>
<div class='a' style='left:80px;top:296px;font-size:56px;font-weight:700;letter-spacing:.16em;color:{GOLDL}'>KNOW BEFORE YOU BUY</div>
<div class='a' style='left:80px;top:420px;font-size:60px;font-weight:800;letter-spacing:.14em;color:{GOLD}'>THE MYTH</div>
<div class='a' style='left:80px;top:500px;width:920px;font-size:100px;font-weight:900;line-height:1.02;letter-spacing:-.04em'>A smooth sweeping hand proves a Rolex is real.</div>
<div class='a' style='left:80px;top:944px;width:920px;height:4px;background:linear-gradient(90deg,{GOLD},transparent)'></div>
<div class='a' style='left:80px;top:990px;font-size:60px;font-weight:800;letter-spacing:.14em;color:{GOLDL}'>THE FACT</div>
<div class='a' style='left:80px;top:1070px;width:920px;font-size:62px;font-weight:600;line-height:1.22;color:{CREAM}'>The better fakes sweep too. Also check the <span style='color:{GOLDL}'>Cyclops</span>, which magnifies the date 2.5 times, the tiny <span style='color:{GOLDL}'>crown etched on the crystal</span> at six o'clock, and the weight.</div>
<div class='legal' style='top:1640px;color:rgba(246,242,234,.6)'>Save this · Advance Watch Co · WhatsApp in bio</div>""")


def k2():  # three checks on cream
    row = lambda n, t, s, y: f"""
<div class='a' style='left:90px;top:{y}px;font-size:150px;font-weight:900;line-height:1;letter-spacing:-.06em;color:{GOLD}'>{n}</div>
<div class='a' style='left:320px;top:{y+6}px;width:680px;font-size:68px;font-weight:800;line-height:1.05;letter-spacing:-.03em;color:{NAVY}'>{t}</div>
<div class='a' style='left:320px;top:{y+165}px;width:680px;font-size:44px;font-weight:500;line-height:1.2;color:{MUT}'>{s}</div>"""
    return page("knowledge_2_three_checks", "", f"""
<div class='a' style='inset:0;background:linear-gradient(160deg,{CREAM} 0%,#ebe3d2 100%)'></div>
<div class='bar' style='left:90px;top:262px;width:200px'></div>
<div class='a' style='left:90px;top:300px;font-size:116px;font-weight:900;line-height:.96;letter-spacing:-.045em;color:{NAVY}'>3 CHECKS<br><span style='color:{GOLD}'>BEFORE YOU PAY</span></div>
{row('1','Photos or a video of the exact watch','With today’s date, showing the reference and the serial number',570)}
{row('2','A full set that matches','The numbers on the watch must match the card and the papers',890)}
{row('3','A recent warranty date','A brand new watch should have a recent one',1210)}
<div class='a c' style='top:1545px;font-size:56px;font-weight:800;color:{NAVY}'>Save this for the day you buy</div>
<div class='legal' style='top:1650px;color:{MUT}'>Advance Watch Co · WhatsApp in bio</div>""")


def k3():  # five years, giant numeral
    return page("knowledge_3_five_years", "dark", f"""
<div class='rays' style='top:760px'></div>
<div class='a c' style='top:262px;font-size:60px;font-weight:700;letter-spacing:.18em;color:{GOLDL}'>THE ROLEX GUARANTEE</div>
<div class='a c' style='top:270px;font-size:780px;font-weight:900;line-height:1;letter-spacing:-.06em;color:transparent;background:linear-gradient(180deg,{GOLDL} 10%,{GOLD} 55%,#7d5f22 100%);-webkit-background-clip:text;background-clip:text;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))'>5</div>
<div class='a c' style='top:1010px;font-size:170px;font-weight:900;letter-spacing:.06em'>YEARS</div>
<div class='bar' style='left:50%;top:1215px;width:200px;transform:translateX(-50%)'></div>
<div class='a' style='left:90px;top:1250px;width:900px;text-align:center;font-size:52px;font-weight:600;line-height:1.24'>It starts on the date on the warranty card, <span style='color:{GOLDL}'>the date of the sale</span>. A recent date means most of it is still ahead.</div>
<div class='a c' style='top:1545px;font-size:56px;font-weight:800;color:{GOLDL}'>Check it before you pay</div>
<div class='legal' style='top:1650px;color:rgba(246,242,234,.6)'>Save this · Not affiliated with Rolex · WhatsApp in bio</div>""")


def render(names):
    js = ROOT / "_shot.js"
    js.write_text("""const {chromium}=require('playwright');const path=require('path');
(async()=>{const names=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of names){await p.goto('file://'+path.resolve('templates/'+n+'.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.screenshot({path:'previews/'+n+'.png',type:'png'});}await b.close()})();""")
    subprocess.run(["node", str(js)] + names, cwd=ROOT, check=True)


def sheet(names, title, out):
    F = ImageFont.truetype(str(ROOT / "fonts" / "Inter.ttf"), 30)
    w, h, gap, top = 460, 818, 16, 70
    sh = Image.new("RGB", (len(names) * (w + gap) + gap, top + h + 60), (16, 18, 24))
    d = ImageDraw.Draw(sh)
    d.text((gap, 18), title, font=F, fill=(227, 196, 122))
    for i, n in enumerate(names):
        im = Image.open(PRE / f"{n}.png").convert("RGB").resize((w, h), Image.LANCZOS)
        sh.paste(im, (gap + i * (w + gap), top))
        d.text((gap + i * (w + gap), top + h + 12), n.split("_", 1)[1].replace("_", " "), font=F, fill=(246, 242, 234))
    sh.save(PRE / out, quality=92)


if __name__ == "__main__":
    av = [av1(), av2(), av3(), av4()]
    kn = [k1(), k2(), k3()]
    render(av + kn)
    sheet(av, "AVAILABLE NOW · Inter + store palette · four directions", "sheet_available_now.jpg")
    sheet(kn, "KNOWLEDGE · Inter + store palette · three directions", "sheet_knowledge.jpg")
    print("ok")

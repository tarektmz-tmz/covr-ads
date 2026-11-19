import sys, json
sys.path.insert(0,'.')
import build_v4 as B
from build_v4 import *
from pathlib import Path
OUT=ROOT/"examples_info"; OUT.mkdir(exist_ok=True)
(TPL/"ex").mkdir(exist_ok=True)

def s1(title,pain,sub):
    c=f"""<div class='rays' style='top:900px'></div>
<div class='eyebrow' style='left:80px;top:262px'>Know before you buy</div>
<div class='bar' style='left:80px;top:330px;width:200px'></div>
<div class='a' style='left:80px;top:390px;width:920px;font-size:{sz(pain,[(40,124),(60,108),(90,92)])}px;font-weight:900;line-height:1.02;letter-spacing:-.04em'>{pain}</div>
<div class='a' style='left:80px;top:1130px;width:920px;font-size:50px;font-weight:600;line-height:1.25;color:{GOLDL}'>{sub}</div>
<div class='a c' style='top:1450px'><span class='pillo'>Next &rarr; the fix</span></div>
{legal_k('rgba(246,242,234,.6)')}"""
    return c,"dark"

def s2(title,rows,foot=None):
    n=len(rows); top,end=560,1500; rh=(end-top)/n
    out=""
    for i,(t,s) in enumerate(rows):
        y=top+i*rh
        ts=50 if n<=4 else 44
        out+=(f"<div class='a card' style='left:70px;top:{y:.0f}px;width:940px;height:{rh-18:.0f}px;background:#fff;border:2px solid #ebe5d8;display:flex;align-items:center;gap:26px;padding:0 34px'>"
              f"<span class='tick' style='width:60px;height:60px'></span><div><div style='font-size:{ts}px;font-weight:800;color:{NAVY};line-height:1.1'>{t}</div>"
              +(f"<div style='font-size:34px;font-weight:500;color:{MUT};margin-top:6px;line-height:1.2'>{s}</div>" if s else "")+"</div></div>")
    c=f"""<div class='eyebrow' style='left:80px;top:262px'>Save this</div>
<div class='a' style='left:80px;top:324px;width:920px;font-size:{sz(title,[(18,104),(28,88),(48,72)])}px;font-weight:900;line-height:1;letter-spacing:-.04em;color:{NAVY}'>{title}</div>
{out}{legal_k(MUT)}"""
    return c,"cream"

def s3(line,ask):
    c=f"""<div class='rays' style='top:900px'></div>
<div class='a c' style='top:300px;font-size:60px;font-weight:800;letter-spacing:.2em;color:{GOLDL}'>ADVANCE WATCH CO</div>
<div class='bar' style='left:50%;top:390px;width:200px;transform:translateX(-50%)'></div>
<div class='a' style='left:90px;top:480px;width:900px;text-align:center;font-size:{sz(line,[(40,100),(70,86),(120,72)])}px;font-weight:900;line-height:1.08;letter-spacing:-.035em'>{line}</div>
<div class='a' style='left:100px;top:1010px;width:880px;text-align:center;font-size:50px;font-weight:600;line-height:1.3;color:{CREAM}'>{ask}</div>
<div class='a c' style='top:1290px'><span class='pill'>DM or WhatsApp (link in bio)</span></div>
<div class='a c' style='top:1440px;font-size:40px;font-weight:600;color:{GOLDL}'>Save this story &middot; send it to a friend</div>
{legal_k('rgba(246,242,234,.6)')}"""
    return c,"dark"

SER=[
("01_boutique_wall","Walked in and left empty-handed?",
 s1,("","Walked in and left empty-handed?","Demand is bigger than supply. That is the whole story."),
 s2,("Your 2 routes",[("Boutique: the official route","Waiting lists for hot models: 5 years, some 10. No clear timing."),("Boutique: who gets offered first","Clients with a purchase history. New clients get easier models."),("Dealer: speed and choice","We source from 1 hour up to 48, depending on the watch."),("The trade-off: you pay above retail","So get the boutique quote first as your reference."),("Then compare honestly","Know what you pay for. Decide what your time is worth.")]),
 s3,("Not waiting five years?","Tell us the exact watch. We tell you honestly how long it takes.")),
("02_seconds_hand","One check does not prove a Rolex",
 s1,("","A smooth seconds hand does not prove it is real","The better fakes sweep too."),
 s2,("Check these instead",[("A ticking hand = fake","A smooth sweep proves nothing."),("The Cyclops","It magnifies the date 2.5 times."),("The tiny crown at 6","Etched on the crystal."),("The weight","Dense watch, tight bracelet, no rattling links."),("The caseback","Rolex does not make see-through casebacks.")]),
 s3,("Not sure about a watch?","Send us the photos. We tell you honestly what we see, no obligation.")),
("03_papers","Box and papers",
 s1,("","“It comes with box and papers”. So?","Papers help. They are never the proof on their own."),
 s2,("What papers can and cannot do",[("Boxes and cards can be faked","So the box alone proves nothing."),("Real papers can be swapped","Moved onto a different watch."),("Check the watch itself","Reference and serial must match card and papers."),("Every detail must look right","Dial, ring, crown, bracelet."),("Keep everything","Card, papers and messages: for servicing or resale.")]),
 s3,("Papers in hand, still unsure?","Send us the watch and the card. We look at both together.")),
("04_handover","The handover",
 s1,("","The watch is in your hand. The balance is still unpaid.","This is the moment that protects you."),
 s2,("Before you pay the balance",[("Inspect it in person","Look under good light."),("Match the numbers","Reference and serial on the watch, card and papers."),("Check the warranty date","A new watch should have a recent, filled-in card."),("Ask for an independent check","A genuine dealer agrees without a fuss."),("Keep your paperwork","Warranty card, papers and messages.")]),
 s3,("Buying with us?","We deliver with a private presentation. You check, then you pay the balance.")),
("05_found_elsewhere","Found a Rolex elsewhere",
 s1,("","Found a Rolex somewhere else. Not sure?","Better to lose a deal than lose your money."),
 s2,("Four things to look at",[("The reference","Does it match the watch you were promised?"),("The serial","On the watch, the card and the papers."),("The card","Its date, its details."),("The price","A big discount needs an explanation."),("Then ask for an independent check","Before you pay in full.")]),
 s3,("Send it to us first.","Photos are enough to start. Honest opinion, no obligation.")),
("06_nicknames","Nicknames are not references",
 s1,("","You asked for a “Batman”. Which one did they mean?","GMT nicknames cause confusion."),
 s2,("GMT-Master II decoder",[("Batgirl: 126710BLNR","Blue and black bezel, Jubilee bracelet."),("Batman: 126710BLNR","Blue and black bezel, Oyster bracelet."),("Pepsi: 126710BLRO","Blue and red bezel."),("Bruce Wayne: 126710GRNR","Grey and black bezel."),("Sprite: 126720VTNR","Green and black bezel, left-hand crown.")]),
 s3,("Name the watch by reference.","Send us the reference you have in mind. We confirm the exact watch.")),
("07_same_reference","Same reference, different price?",
 s1,("","Same Rolex. Two different prices. Why?","Not every offer is the same offer."),
 s2,("What to compare",[("The boutique quote","Your reference point for every offer."),("New or pre-owned?","Ask. A seller should say clearly which."),("Full set or not?","Box, card and papers with matching numbers."),("The warranty date","5 years from the date on the card. Recent = more left."),("The seller","Open about who they are. Welcomes a check.")]),
 s3,("Got an offer to compare?","Send it to us. We tell you what we see, with no obligation.")),
("08_purpose","Choose by purpose",
 s1,("","Choosing a Rolex by status alone?","Each one was built for a different life."),
 s2,("Built for",[("Daytona","Motorsport. A chronograph for timing laps."),("Submariner","The sea. A diver's watch, 300 m."),("GMT-Master II","Pilots. Two time zones on one dial."),("Sea-Dweller","Deep diving. Helium escape valve, 1,220 m."),("Day-Date","Day and full date at a glance. Gold or platinum only.")]),
 s3,("Know the life you want it for?","Tell us. We help you choose and find it.")),
]
jobs=[];mf=[]
for sid,title,f1,a1,f2,a2,f3,a3 in SER:
    names=[]
    for k,(f,a) in enumerate(((f1,a1),(f2,a2),(f3,a3)),1):
        c,cls=f(*a)
        nm=f"ex_{sid}_{k}"; B.page(nm,cls,c,TPL)
        jobs.append(dict(html=f"templates/{nm}.html",out=f"examples_info/{sid}_{k}.jpg")); names.append(f"examples_info/{sid}_{k}.jpg")
    mf.append((sid,title,names))
rep=B.render(jobs)
from PIL import Image
for sid,title,names in mf:
    B.sheet([ROOT/n for n in names],["1 Pain","2 Value","3 Message us"],title,f"../examples_info/sheet_{sid}.jpg",w=360)
print("done")

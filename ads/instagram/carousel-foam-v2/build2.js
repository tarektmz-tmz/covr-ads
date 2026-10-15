const {chromium}=require('playwright');const path=require('path');
const IMG='/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/images/';
const F='/home/user/covr-ads/creative/fonts/';
const OUT=process.argv[2];
const slides=[
 {img:'/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/scratchpad/pexels/38575892-45.jpg',pos:'top',kicker:'Did you know?',h:'Your racket has a foam heart.',s:'And it hates the heat.'},
 {img:'/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/scratchpad/pexels/32896996-45.jpg',pos:'top',kicker:'Inside the frame',h:'EVA foam. The core of your game.',s:'Power, touch and feel live here.'},
 {img:'/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/scratchpad/pexels/34079414-45.jpg',pos:'top',kicker:'The problem',h:'Heat softens that foam.',s:'Sun, hot cars, midday benches.'},
 {img:'/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/scratchpad/pexels/32524250-45.jpg',pos:'top',kicker:'The numbers',h:'12 to 24 months.',s:'Most rackets, played once or twice a week.'},
 {img:IMG+'97.jpg',pos:'bottom',kicker:'With COVR',h:'Out of the sun. Off the floor.',s:''},
 {img:IMG+'98.jpg',pos:'top',kicker:'COVR',h:'Keep it covered.',s:'Handmade in Bali.'},
];
const css=`
@font-face{font-family:IS;src:url(file://${F}InstrumentSerif-400.ttf)}
@font-face{font-family:IS;font-style:italic;src:url(file://${F}InstrumentSerif-400i.ttf)}
@font-face{font-family:Inter;font-weight:400;src:url(file://${F}Inter-400.ttf)}
@font-face{font-family:Inter;font-weight:500;src:url(file://${F}Inter-500.ttf)}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;position:relative;overflow:hidden;background:#000}
.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.fade{position:absolute;left:0;right:0;height:720px}
.fade.top{top:0;background:linear-gradient(to bottom,rgba(20,14,10,.55),rgba(20,14,10,.28) 45%,rgba(20,14,10,0))}
.fade.bottom{bottom:0;background:linear-gradient(to top,rgba(20,14,10,.6),rgba(20,14,10,.3) 45%,rgba(20,14,10,0))}
.txt{position:absolute;left:84px;right:84px;color:#F5F0E6;text-shadow:0 1px 18px rgba(0,0,0,.25)}
.txt.top{top:86px}.txt.bottom{bottom:96px}
.k{font:500 26px Inter;letter-spacing:.24em;text-transform:uppercase;opacity:.9;margin-bottom:22px}
.h{font:400 138px/0.95 IS;letter-spacing:-.005em;max-width:880px}
.s{font:500 40px/1.3 Inter;margin-top:26px;max-width:800px;opacity:.95}
.n{position:absolute;right:56px;bottom:46px;font:500 20px Inter;letter-spacing:.2em;color:#F5F0E6;opacity:.8}
.n.tp{bottom:auto;top:46px}
.logo{position:absolute;left:84px;bottom:48px;font:400 30px IS;letter-spacing:.35em;color:#F5F0E6;opacity:.9}
.logo.tp{bottom:auto;top:44px}
`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const [i,s] of slides.entries()){
 const other=s.pos=='top'?'':'tp';
 const html=`<html><head><style>${css}</style></head><body>
 <img class="ph" src="file://${s.img}">
 <div class="fade ${s.pos}"></div>
 <div class="txt ${s.pos}" style="${s.st||''}"><div class="k">${s.kicker}</div><div class="h" style="${s.hs||''}">${s.h}</div><div class="s" style="${s.ss||''}">${s.s}</div></div>
 <div class="n ${other}">${i+1} / ${slides.length}</div>
 </body></html>`;
 require('fs').writeFileSync(`${OUT}/s${i}.html`,html);await p.goto(`file://${OUT}/s${i}.html`,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
 await p.screenshot({path:`${OUT}/v2-${i+1}.png`});
}
await b.close();})();

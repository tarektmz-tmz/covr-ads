const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
const K=__dirname, S=path.join(K,'..'), f=p=>'file://'+path.join(S,p);
const font=w=>'file://'+path.join(K,`node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const ic=(n,c='#fff',s=34,sw=2.4)=>fs.readFileSync(path.join(K,'node_modules/lucide-static/icons',n+'.svg'),'utf8').replace(/<!--[\s\S]*?-->/g,'').replace(/width="24"/,`width="${s}"`).replace(/height="24"/,`height="${s}"`).replace(/stroke="currentColor"/,`stroke="${c}"`).replace(/stroke-width="2"/,`stroke-width="${sw}"`);
const base=`${[400,500,600,700,800].map(w=>`@font-face{font-family:P;font-weight:${w};src:url(${font(w)})}`).join('')}
*{box-sizing:border-box}body{margin:0;font-family:P}#ad{width:1080px;height:1350px;position:relative;overflow:hidden;color:#2a1a11}
.bag{position:absolute;filter:drop-shadow(0 30px 40px rgba(40,15,0,.35))}
.cta{display:inline-flex;align-items:center;gap:12px;background:#9a3d14;color:#fff;font-weight:700;font-size:34px;padding:22px 44px;border-radius:999px;box-shadow:0 12px 26px rgba(60,20,0,.3)}
.pill{display:inline-block;background:#b8673a;color:#fff;font-weight:700;font-size:26px;letter-spacing:3px;padding:10px 22px;border-radius:10px}
.chk{display:flex;align-items:center;gap:18px;font-size:34px;font-weight:600;margin:14px 0}
.chk b{flex:0 0 52px;height:52px;border-radius:50%;background:#9a3d14;display:flex;align-items:center;justify-content:center}`;
const check=t=>`<div class="chk"><b>${ic('check','#fff',30,3.2)}</b><span>${t}</span></div>`;
const ads={
// 1. Problem -> solution: the 3PM slump
'ad1-3pm-slump':`<div id=ad style="background:#f6eee5">
 <img src="${f('ads/src/ceylora-one-softgel.jpg')}" style="position:absolute;left:0;top:0;width:1080px;height:700px;object-fit:cover;object-position:50% 35%">
 <div style="position:absolute;left:0;top:460px;width:1080px;height:240px;background:linear-gradient(to bottom,rgba(246,238,229,0),#f6eee5)"></div>
 <div style="position:absolute;left:60px;top:48px" class=pill>THE 3PM SLUMP</div>
 <div style="position:absolute;left:60px;top:600px;width:620px">
  <div style="font-size:66px;font-weight:800;line-height:1.04">Skip the afternoon crash.</div>
  <div style="font-size:34px;font-weight:500;margin:18px 0 18px;line-height:1.35">One softgel with breakfast for steadier energy all day.</div>
  ${check('Supports healthy blood sugar')}${check('7,200mg true Ceylon cinnamon')}${check('No powder, no aftertaste')}
  <div style="margin-top:26px" class=cta>Try It Risk-Free →</div>
 </div>
 <img class=bag src="${f('bg/bag.png')}" style="right:40px;bottom:110px;height:500px;transform:rotate(4deg)">
</div>`,
// 2. Did you know: Cassia vs Ceylon
'ad2-did-you-know':`<div id=ad style="background:#2a1a11;color:#fff">
 <img src="${f('bg/raw_sticks.jpg')}" style="position:absolute;left:0;bottom:0;width:1080px;height:760px;object-fit:cover;opacity:.95">
 <div style="position:absolute;left:0;top:590px;width:1080px;height:260px;background:linear-gradient(#2a1a11,rgba(42,26,17,0))"></div>
 <div style="position:absolute;left:70px;top:70px;width:940px">
  <div class=pill>DID YOU KNOW?</div>
  <div style="font-size:74px;font-weight:800;line-height:1.08;margin-top:30px">Most cinnamon in stores <span style="color:#f2a46f">isn't real cinnamon.</span></div>
  <div style="font-size:36px;font-weight:500;line-height:1.4;margin-top:26px;color:#f3e3d3">It's Cassia, which is high in coumarin. True Ceylon cinnamon is naturally low in it, made for daily use.</div>
 </div>
 <div style="position:absolute;left:70px;top:900px;background:rgba(255,255,255,.94);color:#2a1a11;border-radius:22px;padding:22px 28px;width:330px">
  <div style="font-weight:800;font-size:32px;color:#6b625d">CASSIA</div><div style="font-size:26px;margin-top:6px">✕ Thick, hard bark<br>✕ High in coumarin<br>✕ Cheap supplements</div></div>
 <div style="position:absolute;right:70px;top:900px;background:#fff;color:#2a1a11;border-radius:22px;padding:22px 28px;width:330px;border:4px solid #b8673a">
  <div style="font-weight:800;font-size:32px;color:#9a3d14">CEYLON</div><div style="font-size:26px;margin-top:6px">✓ Thin, soft layers<br>✓ Low in coumarin<br>✓ What's in Ceylora</div></div>
 <img class=bag src="${f('bg/bag.png')}" style="left:50%;bottom:-40px;transform:translateX(-50%);height:330px">
</div>`,
// 3. Us vs them comparison
'ad3-vs-other-brands':`<div id=ad style="background:linear-gradient(150deg,#c27440,#a8552a 55%,#7f3412);color:#fff">
 <div style="position:absolute;left:0;top:64px;width:1080px;text-align:center">
  <div style="font-size:30px;font-weight:600;letter-spacing:4px;color:#ffe3cf">NOT ALL CINNAMON IS EQUAL</div>
  <div style="font-size:78px;font-weight:800;line-height:1.05;margin-top:14px">Ceylora vs.<br>Other Brands</div>
 </div>
 <img src="${f('final/ceylora-vs-other-brands-v2.png')}" style="position:absolute;left:50%;top:330px;transform:translateX(-50%);height:870px;filter:drop-shadow(0 24px 40px rgba(40,10,0,.35))">
 <div style="position:absolute;left:0;bottom:44px;width:1080px;text-align:center"><span class=cta style="background:#fff;color:#7f3412">See Why People Switch →</span></div>
</div>`,
// 4. Selling points: 4 benefits
'ad4-4-benefits':`<div id=ad style="background:#f6eee5">
 <img src="${f('bg/raw_woman.jpg')}" style="position:absolute;right:0;top:0;width:640px;height:1350px;object-fit:cover;object-position:60% 50%">
 <div style="position:absolute;left:430px;top:0;width:240px;height:1350px;background:linear-gradient(to right,#f6eee5,rgba(246,238,229,0))"></div>
 <div style="position:absolute;left:0;top:0;width:470px;height:1350px;background:#f6eee5"></div>
 <div style="position:absolute;left:60px;top:80px;width:560px">
  <div class=pill>1 SOFTGEL A DAY</div>
  <div style="font-size:70px;font-weight:800;line-height:1.05;margin:26px 0 40px">4 reasons to make it your daily habit</div>
  ${[['ceylora-icon-insulin','Supports Healthy Insulin Sensitivity'],['ceylora-icon-blood-sugar','Supports Healthy Blood Sugar Levels'],['ceylora-icon-blood-pressure','Supports Healthy Blood Pressure'],['ceylora-icon-energy','Supports Steady Energy']].map(([i,t])=>`<div style="display:flex;align-items:center;gap:24px;margin:26px 0;background:rgba(255,255,255,.9);border-radius:22px;padding:18px 24px;width:520px;box-shadow:0 8px 22px rgba(90,40,10,.12)"><img src="${f('final/'+i+'.png')}" style="width:84px;height:84px"><div style="font-size:31px;font-weight:700;line-height:1.2">${t}</div></div>`).join('')}
  <div style="margin-top:44px" class=cta>Shop Ceylora →</div>
 </div>
</div>`,
// 5. Offer + guarantee
'ad5-offer-guarantee':`<div id=ad style="background:radial-gradient(circle at 50% 35%,#fff8f1,#f0dfcf)">
 <div style="position:absolute;left:0;top:60px;width:1080px;text-align:center">
  <div class=pill>FALL SALE</div>
  <div style="font-size:96px;font-weight:800;line-height:1;margin-top:26px;color:#9a3d14">Buy 2, Get 1 Free</div>
  <div style="font-size:38px;font-weight:600;margin-top:18px">A full 90 days of true Ceylon cinnamon</div>
 </div>
 <div style="position:absolute;left:0;top:360px;width:1080px;height:760px">
  <div style="position:absolute;left:50%;bottom:40px;transform:translateX(-50%);width:820px;height:60px;border-radius:50%;background:radial-gradient(rgba(90,40,10,.28),rgba(90,40,10,0) 70%)"></div>
  <img class=bag src="${f('bg/bag.png')}" style="left:130px;top:110px;height:560px;transform:rotate(-7deg)">
  <img class=bag src="${f('bg/bag.png')}" style="right:130px;top:110px;height:560px;transform:rotate(7deg)">
  <img class=bag src="${f('bg/bag.png')}" style="left:50%;top:40px;height:660px;transform:translateX(-50%)">
  <div style="position:absolute;right:150px;top:70px;background:#9a3d14;color:#fff;font-weight:800;font-size:30px;padding:10px 20px;border-radius:12px;transform:rotate(7deg)">FREE</div>
 </div>
 <img src="${f('final/ceylora-90-day-badge-v2.png')}" style="position:absolute;left:50px;top:330px;width:230px;transform:rotate(-10deg);filter:drop-shadow(0 12px 20px rgba(60,20,0,.3))">
 <div style="position:absolute;left:0;bottom:56px;width:1080px;text-align:center">
  <div style="font-size:32px;font-weight:600;margin-bottom:22px">Not happy? Full refund within 90 days.</div>
  <span class=cta>Claim the Offer →</span></div>
</div>`};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
 for(const [n,h] of Object.entries(ads)){const t=path.join(K,'_ad.html');fs.writeFileSync(t,`<!doctype html><html><head><meta charset=utf-8><style>${base}</style></head><body>${h}</body></html>`);
  await p.goto('file://'+t);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
  await p.locator('#ad').screenshot({path:path.join(S,'ads',n+'.png')});console.log(n);}
 await b.close();})();

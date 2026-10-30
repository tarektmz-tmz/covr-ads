// Second ad set, modelled on proven supplement ad layouts (our photos, prices and claims).
const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
const K=__dirname,S=path.join(K,'..'),f=p=>'file://'+path.join(S,p);
const ff=(pkg,file)=>'file://'+path.join(K,'node_modules/@fontsource',pkg,'files',file);
const ic=(n,c='#fff',s=34,sw=2.2)=>fs.readFileSync(path.join(K,'node_modules/lucide-static/icons',n+'.svg'),'utf8').replace(/<!--[\s\S]*?-->/g,'').replace(/width="24"/,`width="${s}"`).replace(/height="24"/,`height="${s}"`).replace(/stroke="currentColor"/,`stroke="${c}"`).replace(/stroke-width="2"/,`stroke-width="${sw}"`);
const BAG=f('bg/bag.png');
const css=`
${[400,500,600,700,800].map(w=>`@font-face{font-family:P;font-weight:${w};src:url(${ff('poppins',`poppins-latin-${w}-normal.woff2`)})}`).join('')}
${[500,600,700].map(w=>`@font-face{font-family:O;font-weight:${w};src:url(${ff('oswald',`oswald-latin-${w}-normal.woff2`)})}`).join('')}
@font-face{font-family:PF;font-style:italic;font-weight:600;src:url(${ff('playfair-display','playfair-display-latin-600-italic.woff2')})}
*{box-sizing:border-box}body{margin:0;font-family:P;color:#2a1a11}
#ad{width:1080px;height:1350px;position:relative;overflow:hidden}
.O{font-family:O;text-transform:uppercase;letter-spacing:1px}.PF{font-family:PF;font-style:italic}
.bag{position:absolute;filter:drop-shadow(0 28px 34px rgba(40,15,0,.38))}
.cta{display:inline-block;background:#7f3412;color:#fff;font-family:O;font-weight:600;font-size:38px;letter-spacing:2px;text-transform:uppercase;padding:20px 54px;border-radius:999px;box-shadow:0 12px 24px rgba(60,20,0,.3)}
.sticker{position:absolute;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:O;font-weight:700;color:#fff;line-height:1;box-shadow:0 10px 22px rgba(60,20,0,.3)}
.chk{display:flex;align-items:center;gap:16px;font-family:O;font-weight:500;font-size:34px;text-transform:uppercase;margin:16px 0;letter-spacing:.5px}
.chk b{flex:0 0 46px;height:46px;border-radius:8px;background:#9a3d14;display:flex;align-items:center;justify-content:center}
.legal{position:absolute;left:0;bottom:14px;width:100%;text-align:center;font-size:15px;opacity:.7}`;
const chk=t=>`<div class=chk><b>${ic('check','#fff',30,3.4)}</b>${t}</div>`;
const LEGAL='These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease.';
const ads={
// 1. Brown header claim + badge row + bottom offer bar
'b1-claim-hero':`<div id=ad style="background:#f4ebe1">
 <img src="${f('bg/raw_sticks.jpg')}" style="position:absolute;left:0;top:430px;width:1080px;height:820px;object-fit:cover">
 <div style="position:absolute;left:0;top:0;width:1080px;height:470px;background:linear-gradient(#7f3412,#a8552a);clip-path:polygon(0 0,100% 0,100% 82%,0 100%)"></div>
 <div style="position:absolute;top:60px;width:100%;text-align:center;color:#fff">
  <div class=O style="font-size:92px;font-weight:700;line-height:1.02">Supports Healthy<br>Blood Sugar</div>
  <div class=PF style="font-size:42px;margin-top:14px;color:#ffe3cf">The Power of Pure Ceylon Cinnamon</div></div>
 <div style="position:absolute;top:440px;left:60px;right:60px;display:flex;justify-content:space-between">
  ${[['map-pin','Sri Lanka\'s Finest'],['droplet','MCT Oil Enhanced'],['badge-check','12:1 Potency'],['flask-conical','Lab Tested']].map(([i,t])=>`<div style="background:#fff;border-radius:999px;padding:10px 20px 10px 10px;display:flex;align-items:center;gap:10px;font-family:O;font-weight:600;font-size:24px;text-transform:uppercase;box-shadow:0 6px 16px rgba(60,20,0,.18)"><span style="width:44px;height:44px;border-radius:50%;background:#9a3d14;display:flex;align-items:center;justify-content:center">${ic(i,'#fff',26)}</span>${t}</div>`).join('')}</div>
 <img class=bag src="${BAG}" style="left:50%;top:540px;transform:translateX(-50%);height:620px">
 <div style="position:absolute;left:0;bottom:0;width:1080px;height:130px;background:#7f3412;display:flex;align-items:center;justify-content:space-between;padding:0 60px;color:#fff">
  <span class=O style="font-size:40px;font-weight:700;background:#fff;color:#7f3412;padding:12px 32px;border-radius:999px">Get Your Pouch</span>
  <span class=O style="font-size:40px;font-weight:600">Buy 2, Get 1 Free</span></div>
</div>`,
// 2. Price offer card
'b2-price-offer':`<div id=ad style="background:radial-gradient(circle at 70% 45%,#fff8f0,#efe0d0)">
 <div style="position:absolute;left:70px;top:90px;width:560px">
  <div class=O style="font-size:76px;font-weight:700;line-height:1.02;color:#7f3412">Save up to 70%</div>
  <div class=PF style="font-size:44px;margin:10px 0 50px">The Best Value Bundle</div>
  <div class=O style="font-size:58px;font-weight:700">Buy 3, Get 2 Free</div>
  <div style="display:flex;align-items:baseline;gap:20px;margin:14px 0 8px"><span class=O style="font-size:96px;font-weight:700;color:#7f3412">AED 329.99</span></div>
  <div style="font-size:34px"><s style="opacity:.6">AED 1,099.99</s> <span class=O style="background:#9a3d14;color:#fff;padding:4px 14px;border-radius:8px;font-size:30px;margin-left:10px">5 Bags</span></div>
  <div style="margin-top:50px">${chk('150 days of pure Ceylon')}${chk('12:1 extract in MCT oil')}${chk('Lab tested for purity')}</div>
 </div>
 <img class=bag src="${BAG}" style="right:-10px;top:250px;height:760px;transform:rotate(6deg)">
 <img src="${f('final/ceylora-90-day-badge-v2.png')}" style="position:absolute;right:420px;top:820px;width:210px;transform:rotate(-10deg);filter:drop-shadow(0 10px 18px rgba(60,20,0,.3))">
 <div style="position:absolute;left:0;bottom:90px;width:100%;text-align:center"><span class=cta>Get Your Pouch</span><div style="font-size:26px;margin-top:16px">Free Shipping · 90-Day Money-Back Guarantee</div></div>
</div>`,
// 3. Callouts around the pouch
'b3-every-level':`<div id=ad style="background:linear-gradient(#f7efe6,#ead8c6)">
 <div style="position:absolute;top:60px;width:100%;text-align:center">
  <div class=O style="font-size:96px;font-weight:700;color:#7f3412;line-height:1">Support on Every Level</div>
  <div class=O style="display:inline-block;margin-top:20px;background:#9a3d14;color:#fff;font-size:34px;font-weight:600;padding:10px 34px">One softgel every morning</div></div>
 <img class=bag src="${BAG}" style="left:50%;top:330px;transform:translateX(-50%);height:760px">
 ${[['ceylora-icon-insulin','Healthy Insulin<br>Sensitivity',70,420,'left'],['ceylora-icon-blood-sugar','Healthy Blood<br>Sugar Levels',70,780,'left'],['ceylora-icon-blood-pressure','Healthy Blood<br>Pressure',730,420,'right'],['ceylora-icon-energy','Steady Daily<br>Energy',730,780,'right']].map(([i,t,x,y,side])=>`<div style="position:absolute;left:${x}px;top:${y}px;width:280px;text-align:center"><img src="${f('final/'+i+'.png')}" style="width:110px;filter:drop-shadow(0 8px 14px rgba(60,20,0,.25))"><div class=O style="font-size:32px;font-weight:600;line-height:1.15;margin-top:12px;background:rgba(255,255,255,.85);padding:10px 8px;border-radius:12px">Supports<br>${t}</div></div>`).join('')}
 <div class=sticker style="right:70px;top:1090px;width:170px;height:170px;background:#9a3d14;font-size:40px;transform:rotate(10deg)">Buy 2<br><span style="font-size:30px">Get 1</span>Free</div>
 <div style="position:absolute;left:0;bottom:46px;width:100%;text-align:center;font-family:O;font-weight:600;font-size:30px;letter-spacing:2px;color:#7f3412">${ic('shield-check','#7f3412',32)} 90-DAY MONEY-BACK GUARANTEE</div>
</div>`,
// 4. Sticky notes around a real person holding the pouch
'b4-sticky-notes':`<div id=ad style="background:#efe3d5">
 <img src="${f('bg/raw_woman.jpg')}" style="position:absolute;left:330px;top:0;width:750px;height:1350px;object-fit:cover;object-position:78% 40%">
 <div style="position:absolute;left:330px;top:0;width:140px;height:1350px;background:linear-gradient(to right,#efe3d5,rgba(239,227,213,0))"></div>
 ${[['SECRET<br>FLASH<br>SALE',40,50,-5,'#ffe27a',46],['HURRY!<br>UP TO<br>70% OFF',50,345,4,'#ffe27a',46],['BUY 2<br>GET 1<br>FREE',38,640,-4,'#ffd0a8',48],['90-DAY<br>MONEY<br>BACK',52,935,3,'#fff3b0',44]].map(([t,x,y,r,c,s])=>`<div style="position:absolute;left:${x}px;top:${y}px;width:260px;height:250px;background:${c};transform:rotate(${r}deg);box-shadow:4px 10px 18px rgba(0,0,0,.22);display:flex;align-items:center;justify-content:center;text-align:center;font-family:O;font-weight:700;font-size:${s}px;line-height:1.05;color:#4a2510"><div style="position:absolute;top:-14px;left:50%;width:90px;height:30px;transform:translateX(-50%) rotate(-3deg);background:rgba(255,255,255,.6)"></div>${t}</div>`).join('')}
 <div style="position:absolute;left:410px;right:16px;top:1192px;height:142px;background:rgba(255,250,243,.93);border-radius:24px;box-shadow:0 10px 26px rgba(40,15,0,.25);display:flex;align-items:center;justify-content:space-around;padding:0 10px">
  ${[['ceylora-icon-blood-sugar','Healthy<br>Blood Sugar'],['ceylora-icon-insulin','Insulin<br>Sensitivity'],['ceylora-icon-blood-pressure','Healthy Blood<br>Pressure'],['ceylora-icon-energy','Steady<br>Energy']].map(([i,t])=>`<div style="display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center"><img src="${f('final/'+i+'.png')}" style="width:62px;height:62px"><div class=O style="font-size:21px;font-weight:600;line-height:1.1;color:#4a2510">${t}</div></div>`).join('')}
 </div>
 <div style="position:absolute;left:30px;top:1225px"><span class=cta style="font-size:30px;padding:16px 34px">Shop the Flash Sale</span></div>
</div>`,
// 5. What's inside checklist
'b5-whats-inside':`<div id=ad style="background:#f6efe6">
 <div style="position:absolute;left:0;top:0;width:1080px;height:180px;background:#7f3412;color:#fff;display:flex;align-items:center;justify-content:center" class=O><span style="font-size:80px;font-weight:700">Ceylon Cinnamon 7,200mg</span></div>
 <div class=PF style="position:absolute;left:70px;top:215px;font-size:62px;color:#7f3412">What's inside?</div>
 <div style="position:absolute;left:70px;top:320px;width:520px">
  ${['True Ceylon from Sri Lanka','12:1 concentrated extract','MCT oil for absorption','Naturally low in coumarin','Easy-to-swallow softgels','Lab tested for purity'].map(chk).join('')}</div>
 <img class=bag src="${BAG}" style="right:50px;top:225px;height:620px;transform:rotate(5deg)">
 <div style="position:absolute;left:70px;top:790px" class=cta>Buy 2, Get 1 Free</div>
 <img src="${f('bg/raw_coconut.jpg')}" style="position:absolute;left:40px;top:930px;width:1000px;height:360px;object-fit:cover;object-position:50% 4%;border-radius:28px;box-shadow:0 14px 30px rgba(60,20,0,.18)">
 <div class=legal>${LEGAL}</div>
</div>`,
// 6. 30/60/90 timeline
'b6-90-days':`<div id=ad style="background:linear-gradient(#8a3d17,#b8673a 45%,#f2e3d3 45%)">
 <div style="position:absolute;top:60px;width:100%;text-align:center;color:#fff">
  <div class=O style="font-size:88px;font-weight:700;line-height:1.02">Your First 90 Days<br>with Ceylora</div>
  <div class=PF style="font-size:40px;margin-top:12px;color:#ffe3cf">Real support is built day by day</div></div>
 <img class=bag src="${BAG}" style="left:50%;top:330px;transform:translateX(-50%);height:360px">
 <div style="position:absolute;left:50px;right:50px;top:720px;display:flex;gap:24px">
  ${[['30 Days','Easy Start','One softgel with breakfast becomes a habit you keep.'],['60 Days','Daily Balance','Feel more balanced, with fewer energy ups and downs.'],['90 Days','Long-Term Support','Supports healthy glucose metabolism with steady use.']].map(([d,h,p])=>`<div style="flex:1;background:#fff;border-radius:24px;padding:26px 24px;box-shadow:0 12px 26px rgba(60,20,0,.15)"><div class=O style="font-size:44px;font-weight:700;color:#9a3d14;border-bottom:3px solid #e9d6c4;padding-bottom:10px">${d}</div><div style="font-weight:700;font-size:30px;margin:16px 0 8px">${h}</div><div style="font-size:24px;line-height:1.4">${p}</div></div>`).join('')}</div>
 <div style="position:absolute;left:0;top:1120px;width:100%;text-align:center"><span class=cta>Get 90 Days: Buy 2, Get 1 Free</span></div>
 <div class=legal>${LEGAL} Results vary.</div>
</div>`,
// 7. Price anchor with 5 bags
'b7-price-anchor':`<div id=ad style="background:radial-gradient(circle at 50% 40%,#fffaf4,#efdfcf)">
 <div style="position:absolute;top:70px;width:100%;text-align:center">
  <span class=O style="font-size:72px;font-weight:600;color:#8a817c;text-decoration:line-through">AED 1,099.99</span>
  <span class=O style="font-size:110px;font-weight:700;color:#9a3d14;margin-left:24px">AED 329.99</span>
  <div style="font-size:40px;font-weight:600;margin-top:4px">Buy 3, Get 2 Free · Fall Sale</div></div>
 <div style="position:absolute;left:0;top:300px;width:1080px;height:760px">
  ${[[60,140,500,-6],[620,140,500,6],[240,80,560,-2],[460,80,560,2],[330,40,640,0]].map(([x,y,h,r])=>`<img class=bag src="${BAG}" style="left:${x}px;top:${y}px;height:${h}px;transform:rotate(${r}deg)">`).join('')}</div>
 <div style="position:absolute;left:0;top:1040px;width:100%;text-align:center"><div class=O style="font-size:46px;font-weight:600;color:#7f3412">That's about AED 2.20 a day</div>
 <div style="margin-top:26px"><span class=cta>Stock Up &amp; Save</span></div></div>
 <div class=legal>5 bags = 150 softgels. Fall Sale ends Nov 30.</div>
</div>`,
// 8. Notes-app native ad (true content)
'b8-notes':`<div id=ad style="background:#b8673a">
 <div style="position:absolute;left:70px;top:70px;width:940px;height:1210px;background:#fffdf8;border-radius:28px;box-shadow:0 24px 50px rgba(60,20,0,.35);padding:60px 64px;font-size:35px;line-height:1.5">
  <div style="display:flex;justify-content:space-between;color:#c58a3a;font-weight:600;font-size:28px;margin-bottom:24px"><span>‹ Notes</span><span>Done</span></div>
  <div style="font-weight:800;font-size:46px;line-height:1.15;margin-bottom:30px;font-size:52px">3 things to know before you buy a cinnamon supplement</div>
  <p style="margin:0 0 18px"><b>1. Most cinnamon is Cassia, not Ceylon.</b> Cassia is cheaper and much higher in coumarin.</p>
  <p style="margin:0 0 18px"><b>2. The dose matters.</b> Many capsules hold 500–1,000mg of powder. One Ceylora softgel is a 12:1 extract, equal to 7,200mg of Ceylon.</p>
  <p style="margin:0 0 18px"><b>3. Cinnamon's compounds are fat-soluble.</b> That's why ours is in MCT oil, not dry powder.</p>
  <p style="margin:0 0 18px">That's it. One softgel with breakfast. ☕</p>
  <p style="margin:0 0 18px;background:#fbeee2;padding:14px 18px;border-radius:12px"><b>Fall Sale:</b> Buy 2, Get 1 Free, with a 90-day money-back guarantee.</p>
  <p style="margin:0;color:#7a6a60">— The Ceylora team</p>
  <img class=bag src="${BAG}" style="right:40px;bottom:30px;height:260px;transform:rotate(8deg)">
 </div>
</div>`,
// 9. "So you can actually feel the difference" bundle
'b9-feel-difference':`<div id=ad style="background:linear-gradient(#fbf4ec,#ecdccb)">
 <div style="position:absolute;top:60px;width:100%;text-align:center">
  <div class=O style="font-size:80px;font-weight:700;line-height:1.05">Buy 2, Get 1 Free<br><span style="color:#9a3d14">So You Can Actually Feel the Difference</span></div>
  <div style="font-size:30px;margin:18px auto 0;width:860px;line-height:1.4">Ceylon cinnamon works best with steady daily use. Three bags gives you a full 90 days.</div></div>
 <img class=bag src="${BAG}" style="left:110px;top:520px;height:560px;transform:rotate(-6deg)">
 <img class=bag src="${BAG}" style="left:370px;top:480px;height:600px">
 <img class=bag src="${BAG}" style="left:650px;top:520px;height:560px;transform:rotate(6deg);opacity:.98">
 <div class=sticker style="right:70px;top:470px;width:200px;height:200px;background:#9a3d14;font-size:58px;transform:rotate(12deg)">FREE</div>
 <div style="position:absolute;left:60px;right:60px;top:1140px;display:flex;justify-content:space-around;font-family:O;font-weight:600;font-size:28px;text-transform:uppercase;color:#7f3412">
  <span>${ic('truck','#7f3412',30)} Free shipping</span><span>${ic('leaf','#7f3412',30)} Real Ceylon</span><span>${ic('flask-conical','#7f3412',30)} Lab tested</span><span>${ic('shield-check','#7f3412',30)} 90-day guarantee</span></div>
 <div style="position:absolute;left:0;top:1215px;width:100%;text-align:center"><span class=cta style="font-size:34px;padding:16px 46px">Claim My Free Bag</span></div>
</div>`,
// 10. "We're Sorry" apology letter
'c1-were-sorry':`<div id=ad style="background:#efe3d6">
 <div style="position:absolute;left:60px;top:60px;width:960px;height:1230px;background:#fffaf2;border-radius:10px;box-shadow:0 20px 44px rgba(60,20,0,.22);padding:70px 70px">
  <div class=PF style="font-size:110px;color:#7f3412;line-height:1">We're Sorry.</div>
  <div style="width:490px;font-size:30px;line-height:1.5;margin-top:36px">
   <p style="margin:0 0 20px">We know many of you missed our Fall Sale, and we heard you.</p>
   <p style="margin:0 0 20px">So many orders came in that our bundles sold out faster than we planned. To make it right, we're reopening it, <b>for a short time only.</b></p>
   <p style="margin:0 0 20px">Get the same authentic Ceylon cinnamon, 7,200mg in MCT oil, at <b>up to 70% off</b>, with free shipping.</p>
   <p style="margin:0 0 20px">This won't happen again. Once it's gone, it's gone.</p>
   <p style="margin:0 0 26px;font-weight:700">Tap below before the price goes back up.</p>
   <span class=cta style="font-size:32px;padding:18px 44px">Get Yours Today →</span>
   <p style="margin:30px 0 0;color:#7a6a60;font-size:26px">— The Ceylora Team</p></div>
  <img class=bag src="${BAG}" style="right:-10px;top:500px;height:560px;transform:rotate(9deg)">
  <div class=sticker style="right:60px;top:330px;width:190px;height:190px;background:#9a3d14;font-size:56px;transform:rotate(-10deg)">70%<span style="font-size:36px">OFF</span></div>
 </div>
</div>`,
// 11. "We owe you an apology" notes-style
'c2-we-owe-you':`<div id=ad style="background:#c27440">
 <div style="position:absolute;left:70px;top:70px;width:940px;height:1210px;background:#fff;border-radius:6px;box-shadow:0 24px 50px rgba(60,20,0,.35);padding:64px 66px;font-size:31px;line-height:1.5">
  <div style="font-weight:800;font-size:54px;margin-bottom:28px">We owe you an <u style="text-decoration-color:#c27440;text-decoration-thickness:6px">apology</u>.</div>
  <p style="margin:0 0 16px">A big one.</p>
  <p style="margin:0 0 16px">Apparently, we've gotten too good at this. People keep telling us they switched from their old cinnamon pills and never went back. 😅</p>
  <p style="margin:0 0 16px">Our bad. It's not our fault most brands sell cheap Cassia powder. We just use true Ceylon, concentrated 12:1, in MCT oil.</p>
  <p style="margin:0 0 16px">So the only responsible thing to do? Let you stock up before it's gone.</p>
  <p style="margin:0 0 16px;background:#fbeee2;padding:14px 18px;border-radius:10px"><b>FLASH SALE: Up to 70% OFF. Buy 3, Get 2 Free + Free Shipping.</b></p>
  <p style="margin:0 0 16px">Yes, we're basically giving it away. No, we're not sorry. 😉</p>
  <p style="margin:0;color:#7a6a60">— Founder, Ceylora</p>
  <img class=bag src="${BAG}" style="right:44px;bottom:40px;height:280px;transform:rotate(8deg)">
 </div>
</div>`,
// 12. Low stock + midnight deadline
'c3-ends-midnight':`<div id=ad style="background:radial-gradient(circle at 50% 30%,#a8552a,#5c260c)">
 <div style="position:absolute;top:56px;width:100%;text-align:center;color:#fff">
  <div class=O style="display:inline-block;background:#d93a1e;font-size:34px;font-weight:600;padding:10px 30px;border-radius:8px">⚠ Low Stock Alert</div>
  <div class=O style="font-size:118px;font-weight:700;line-height:1;margin-top:26px">70% Off Ends<br>at Midnight</div>
  <div class=O style="font-size:34px;font-weight:500;margin-top:18px;color:#ffe3cf">Fall Flash Sale · While Supplies Last</div></div>
 <div style="position:absolute;top:470px;width:100%;text-align:center;color:#fff"><span class=O style="font-size:96px;font-weight:700">7,200MG</span><div style="font-size:28px;margin-top:-6px">of true Ceylon cinnamon per softgel</div></div>
 <img class=bag src="${BAG}" style="left:50%;top:640px;transform:translateX(-50%);height:470px">
 <div style="position:absolute;left:0;top:1145px;width:100%;text-align:center"><span class=cta style="background:#d93a1e">Claim My Discount</span>
 <div class=O style="color:#fff;font-size:30px;margin-top:20px;letter-spacing:2px">Only a few bags left at this price</div></div>
</div>`,
// 13. Last chance, dark
'c4-last-chance':`<div id=ad style="background:linear-gradient(120deg,#2a1a11,#5c2a10)">
 <img src="${f('bg/raw_sticks.jpg')}" style="position:absolute;right:0;bottom:0;width:700px;height:600px;object-fit:cover;opacity:.35;-webkit-mask-image:linear-gradient(to left,#000 40%,transparent)">
 <div style="position:absolute;left:70px;top:90px;width:500px;color:#fff">
  <div class=O style="font-size:112px;font-weight:700;line-height:.98">Last Chance<br>For Our<br><span style="color:#f2a46f">Best Deal</span></div>
  <div style="font-size:31px;line-height:1.45;margin:30px 0 34px;color:#f3e3d3">Stocks are running low. Claim this offer to support healthy blood sugar and steady daily energy.</div>
  ${[['truck','Free Shipping'],['badge-check','Buy 3, Get 2 Free'],['shield-check','90-Day Guarantee']].map(([i,t])=>`<div class=O style="display:flex;align-items:center;gap:18px;font-size:42px;font-weight:600;margin:16px 0">${ic(i,'#f2a46f',46)}${t}</div>`).join('')}
  <div style="margin-top:40px" class=cta>Order Today</div></div>
 <img class=bag src="${BAG}" style="right:10px;top:330px;height:700px;transform:rotate(5deg)">
</div>`,
// 14. Buy 2 Get 1 Free, sale ends tonight
'c5-ends-tonight':`<div id=ad style="background:linear-gradient(#f7eee4,#e9d6c3)">
 <div style="position:absolute;top:60px;width:100%;text-align:center">
  <div class=O style="font-size:110px;font-weight:700;color:#2a1a11;line-height:1">Buy 2 Get 1 Free</div>
  <div class=O style="display:inline-block;margin-top:20px;background:#d93a1e;color:#fff;font-size:40px;font-weight:600;padding:10px 36px;border-radius:999px">Sale Ends Tonight</div></div>
 <img class=bag src="${BAG}" style="left:90px;top:380px;height:600px;transform:rotate(-6deg)">
 <img class=bag src="${BAG}" style="left:640px;top:380px;height:600px;transform:rotate(6deg)">
 <img class=bag src="${BAG}" style="left:50%;top:330px;transform:translateX(-50%);height:680px">
 <div class=sticker style="right:70px;top:300px;width:180px;height:180px;background:#9a3d14;font-size:54px;transform:rotate(12deg)">FREE</div>
 <div style="position:absolute;left:0;right:0;top:1080px;display:flex;justify-content:center;gap:70px;font-family:O;font-weight:600;font-size:34px;text-transform:uppercase;color:#7f3412">
  <span style="display:flex;align-items:center;gap:12px">${ic('shield-check','#7f3412',44)}90-Day Money<br>Back Guarantee</span><span style="display:flex;align-items:center;gap:12px">${ic('truck','#7f3412',44)}Free<br>Shipping</span></div>
 <div style="position:absolute;left:0;top:1215px;width:100%;text-align:center"><span class=cta style="font-size:34px;padding:16px 50px">Shop Now</span></div>
</div>`};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
 fs.mkdirSync(path.join(S,'ads2'),{recursive:true});
 for(const [n,h] of Object.entries(ads)){const t=path.join(K,'_ad2.html');fs.writeFileSync(t,`<!doctype html><html><head><meta charset=utf-8><style>${css}</style></head><body>${h}</body></html>`);
  await p.goto('file://'+t);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
  await p.locator('#ad').screenshot({path:path.join(S,'ads2',n+'.png')});console.log(n);}
 await b.close();})();

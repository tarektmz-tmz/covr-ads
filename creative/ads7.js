// Round 6: 15 everyday-object formats. Same OFFER as round 5 (edit it in ads6.js).
const { OFFER } = require('./ads6.js');
const { crop, frame, ARROW } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');
const cut = (n, x, y, w, rot = 0, shadow = '0 40px 50px rgba(40,25,10,.35)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  return `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${w * H / W}px;transform:rotate(${rot}deg);filter:drop-shadow(${shadow})">`;
};
const btn = (t, style = '') => `<span class="btn" style="${style}">${t} ${ARROW}</span>`;
const ads = [];
const add = a => ads.push({ outDir: 'objects', ...a });

/* Q01 — Nutrition facts label */
{
  const rows = [['Cotton canvas body', '✓'], ['Genuine leather trim', '✓'], ['Metal hardware', '✓'], ['Waterproof, wipe-clean lining', '✓'], ['Front zip pockets', '1'], ['Adjustable straps', '1'], ['Carry handles', '1'], ['D-rings (for a ball pouch)', '1'], ['Grip enclosure', 'Open-back']];
  add({
    id: 'q01-covr-facts', stage: 'MOFU', format: 'Nutrition label',
    css: `body{background:#d9cbb6}.nf{font-family:Inter;color:#111}.nf .r{display:flex;justify-content:space-between;border-top:2px solid #111;padding:9px 0;font-size:30px}`,
    html: `
      ${cut('coffee', 560, 820, 620, -60, '0 30px 40px rgba(0,0,0,.35)')}
      <div class="abs nf" style="left:70px;top:70px;width:600px;background:#fff;border:4px solid #111;padding:22px 26px;box-shadow:0 30px 60px rgba(0,0,0,.2)">
        <div style="font-family:Montserrat;font-weight:900;font-size:80px;line-height:1;letter-spacing:-.02em">COVR Facts</div>
        <div style="font-size:28px;border-bottom:16px solid #111;padding:6px 0 10px">Serving size: 1 padel racket</div>
        <div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:8px solid #111;padding:8px 0"><b style="font-size:38px">Price</b><span><s style="font-size:28px;color:#777">${OFFER.was}</s> <b style="font-family:Montserrat;font-weight:900;font-size:56px">${OFFER.now}</b></span></div>
        <div style="text-align:right;font-weight:700;font-size:20px;padding:6px 0">Included</div>
        ${rows.map(([a, b]) => `<div class="r"><span>${a}</span><b>${b}</b></div>`).join('')}
        <div style="border-top:8px solid #111;padding-top:10px;font-size:20px;line-height:1.4">Contains no thin nylon outer shell. May cause compliments on court. Code ${OFFER.code}: ${OFFER.pct} off, ${OFFER.when.toLowerCase()}.</div>
      </div>`,
  });
}

/* Q02 — Care label (text from the real product care instructions) */
add({
  id: 'q02-care-label', stage: 'MOFU', format: 'Care label',
  html: `
    ${frame('crest-duo-closeup.jpg', 0.45, 0.5, 1.03, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:rgba(20,14,10,.35)"></div>
    <div class="abs" style="left:250px;top:90px;width:580px;background:#f7f3ea;padding:60px 50px 70px;text-align:center;font-family:'Courier Prime';color:#2a2420;box-shadow:0 30px 60px rgba(0,0,0,.45);transform:rotate(-3deg);
      -webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 20px) no-repeat,linear-gradient(135deg,#000 50%,transparent 50%) 0 100%/24px 20px repeat-x,linear-gradient(225deg,#000 50%,transparent 50%) 12px 100%/24px 20px repeat-x">
      <div style="width:30px;height:30px;border-radius:50%;background:#d6cbb8;margin:0 auto 30px"></div>
      <div class="logo" style="font-family:'Instrument Serif';font-size:54px">COVR</div>
      <div style="font-size:22px;margin:10px 0 34px">PADEL RACKET COVER</div>
      <div style="font-size:24px;text-align:left;line-height:1.7">
        BODY: COTTON CANVAS<br>TRIM: GENUINE LEATHER<br>LINING: WATERPROOF<br>HARDWARE: METAL</div>
      <div style="border-top:2px dashed #8c857c;margin:30px 0"></div>
      <div style="font-size:24px;text-align:left;line-height:1.7">SPOT CLEAN. AIR DRY NATURALLY.<br>WIPE LINING WITH A DAMP CLOTH.<br>CONDITION LEATHER WITH A<br>NEUTRAL BALM.<br><b>NEVER LEAVE IN A CAR BOOT.</b></div>
      <div style="display:flex;justify-content:center;gap:28px;margin-top:34px">
        ${['<circle cx="24" cy="24" r="16"/>', '<path d="M8 36h32L24 10z"/>', '<rect x="10" y="10" width="28" height="28"/>', '<path d="M10 30c6-8 22-8 28 0"/><path d="M24 10v12"/>'].map(d => `<svg width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="#2a2420" stroke-width="2.5">${d}</svg>`).join('')}
      </div></div>
    <div class="abs" style="left:0;right:0;bottom:70px;text-align:center;color:#fff"><div class="mega" style="font-size:64px">Handle with care.</div><div style="font-size:28px;margin-top:10px">${OFFER.pct} off with code <b>${OFFER.code}</b></div></div>`,
});

/* Q03 — Prescription label */
add({
  id: 'q03-prescription', stage: 'TOFU', format: 'Rx label',
  css: `body{background:linear-gradient(160deg,#eef0ec,#d7dcd6)}`,
  html: `
    <div class="abs" style="left:70px;top:80px;width:940px;background:#fff;border-radius:20px;box-shadow:0 30px 60px rgba(0,0,0,.12);overflow:hidden">
      <div style="background:#2f4a3a;color:#fff;padding:24px 40px;display:flex;justify-content:space-between;align-items:center"><span style="font-family:Montserrat;font-weight:900;font-size:40px">Rx · COVR PHARMACY</span><span style="font-size:20px;letter-spacing:.15em">NO. 0199</span></div>
      <div style="padding:34px 40px;font-size:30px;line-height:1.5;color:#1d1d1d">
        <div style="font-size:22px;color:#6f6a62;letter-spacing:.12em">PATIENT</div><div style="font-family:Montserrat;font-weight:800;font-size:44px;margin-bottom:20px">Your padel racket</div>
        <div style="font-size:22px;color:#6f6a62;letter-spacing:.12em">DIAGNOSIS</div><div style="margin-bottom:20px">Chronic car-boot exposure. Loose keys. Rough benches.</div>
        <div style="font-size:22px;color:#6f6a62;letter-spacing:.12em">DIRECTIONS</div><div style="margin-bottom:20px"><b>Use 1 COVR before and after every match.</b> Store inside between sessions.</div>
        <div style="display:flex;gap:60px"><div><div style="font-size:22px;color:#6f6a62;letter-spacing:.12em">REFILLS</div><div>10 colours</div></div><div><div style="font-size:22px;color:#6f6a62;letter-spacing:.12em">COPAY</div><div><s style="color:#8c857c">${OFFER.was}</s> <b style="color:#b5452e">${OFFER.now}</b></div></div></div>
      </div>
      <div style="background:#f3efe6;padding:18px 40px;font-size:20px;color:#6f6a62">Side effects may include compliments and a racket that looks after itself. Code ${OFFER.code}.</div>
    </div>
    ${cut('mocha', 240, 860, 600, -8)}`,
});

/* Q04 — Lock screen notifications */
add({
  id: 'q04-lock-screen', stage: 'TOFU', format: 'Lock screen',
  css: `.n{background:rgba(245,242,236,.78);backdrop-filter:blur(20px);border-radius:34px;padding:24px 30px;margin-bottom:18px;display:flex;gap:22px;align-items:center}
        .n .ic{width:76px;height:76px;border-radius:18px;flex:none;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px;color:#fff}
        .n .t{display:flex;justify-content:space-between;font-weight:700;font-size:27px}.n .t span{font-weight:400;color:#6f6a62;font-size:23px}.n .b{font-size:28px;line-height:1.3;margin-top:4px}`,
  html: `
    ${frame('latte-walking-court.jpg', 0.45, 0.55, 1.03, 0, 0, 1080, 1350, 'filter:blur(2px) brightness(.8)').html}
    <div class="abs" style="left:0;right:0;top:80px;text-align:center;color:#fff"><div style="font-size:30px;font-weight:500">Sunday 11 October</div><div style="font-size:190px;font-weight:300;line-height:1;letter-spacing:-.03em">7:42</div></div>
    <div class="abs" style="left:50px;right:50px;top:460px">
      <div class="n"><div class="ic" style="background:#2a2724">R</div><div style="flex:1"><div class="t">Your racket<span>now</span></div><div class="b">still in the car boot btw. it’s hot in here.</div></div></div>
      <div class="n"><div class="ic" style="background:#2f4a3a">PT</div><div style="flex:1"><div class="t">Padel Tuesday<span>5m ago</span></div><div class="b">Nadia: court 3 at 7? bring your nice bag</div></div></div>
      <div class="n"><div class="ic" style="background:#9b6b3e;font-family:'Instrument Serif';font-weight:400;font-size:40px">C</div><div style="flex:1"><div class="t">COVR<span>9m ago</span></div><div class="b"><b>${OFFER.pct} off ends soon.</b> Your racket’s upgrade is one tap away. Code ${OFFER.code}</div></div></div>
    </div>`,
});

/* Q05 — Weather forecast */
const ICONS = {"sun": "<circle cx=\"24\" cy=\"24\" r=\"8\"/><path d=\"M24 6v6M24 36v6M6 24h6M36 24h6M11 11l4 4M33 33l4 4M37 11l-4 4M15 33l-4 4\"/>", "rain": "<path d=\"M14 30a8 8 0 0 1 2-16 11 11 0 0 1 21 4 6 6 0 0 1-1 12z\"/><path d=\"M18 36l-2 5M26 36l-2 5M34 36l-2 5\"/>", "key": "<circle cx=\"16\" cy=\"24\" r=\"7\"/><path d=\"M23 24h18M35 24v6M41 24v5\"/>", "ok": "<rect x=\"8\" y=\"8\" width=\"32\" height=\"32\" rx=\"8\"/><path d=\"M16 24l6 6 12-12\"/>"};
add({
  id: 'q05-racket-forecast', stage: 'TOFU', format: 'Weather app',
  css: `body{background:linear-gradient(180deg,#5b86b6 0%,#9fbad6 55%,#e9e3d6 100%);color:#fff}.d{display:flex;justify-content:space-between;align-items:center;padding:20px 0;border-top:1px solid rgba(255,255,255,.3);font-size:32px}`,
  html: `
    <div class="abs" style="left:0;right:0;top:70px;text-align:center">
      <div style="font-size:40px;font-weight:500">Your racket</div><div style="font-size:200px;font-weight:200;line-height:1">38°</div>
      <div style="font-size:32px;opacity:.9">In the car boot · Feels like a mistake</div></div>
    <div class="abs" style="left:60px;right:60px;top:500px;background:rgba(255,255,255,.18);border-radius:34px;padding:20px 40px">
      <div style="font-size:20px;letter-spacing:.15em;opacity:.8;padding:10px 0">THIS WEEK FOR YOUR RACKET</div>
      ${[['Mon', 'sun', 'Car boot'], ['Tue', 'rain', 'Wet bench'], ['Wed', 'key', 'Loose keys'], ['Thu', 'ok', 'In a COVR']].map(([d, i, t]) => `<div class="d"><span style="width:90px">${d}</span><span><svg width="52" height="52" viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">${ICONS[i]}</svg></span><span style="width:340px;text-align:right">${t}</span></div>`).join('')}
    </div>
    ${cut('coffee', 600, 1030, 440, -18, '0 20px 30px rgba(0,0,0,.3)')}
    <div class="abs" style="left:60px;bottom:90px;color:#26231f"><div class="mega" style="font-size:56px">Forecast:</div><div class="mega" style="font-size:56px;color:#9b6b3e">100% covered.</div><div style="font-size:24px;margin-top:10px">${OFFER.pct} off · ${OFFER.code}</div></div>`,
});

/* Q06 — Cart with code applied */
add({
  id: 'q06-cart-code-applied', stage: 'BOFU', format: 'Cart',
  css: `body{background:#f2efe9}.ln{display:flex;justify-content:space-between;font-size:32px;padding:14px 0}`,
  html: `
    <div class="abs" style="left:60px;right:60px;top:70px;display:flex;justify-content:space-between;align-items:center"><div style="font-family:Montserrat;font-weight:800;font-size:48px">Your cart (1)</div><div class="logo" style="font-size:36px">COVR</div></div>
    <div class="abs" style="left:60px;right:60px;top:180px;background:#fff;border-radius:28px;padding:30px;display:flex;gap:30px;align-items:center;box-shadow:0 14px 40px rgba(0,0,0,.06)">
      <div style="width:260px;height:300px;border-radius:18px;overflow:hidden;position:relative;flex:none">${crop('latte-unboxing-hands.jpg', 0.55, 0.45, 1.5, 260, 300).img}</div>
      <div style="flex:1"><div style="font-family:Montserrat;font-weight:800;font-size:38px">Latte Padel Racket Cover</div><div style="font-size:26px;color:#6f6a62;margin:8px 0 20px">Natural canvas · dark brown leather</div>
        <div style="display:flex;align-items:center;gap:20px"><span style="border:2px solid #d6cfc4;border-radius:12px;padding:6px 18px;font-size:28px">− 1 +</span><b style="font-size:34px">${OFFER.was}</b></div></div></div>
    <div class="abs" style="left:60px;right:60px;top:560px;background:#fff;border-radius:28px;padding:30px 36px;box-shadow:0 14px 40px rgba(0,0,0,.06)">
      <div style="display:flex;gap:16px;margin-bottom:20px"><div style="flex:1;border:2px solid #2f4a3a;border-radius:14px;padding:18px 22px;font-size:30px;font-weight:700;letter-spacing:.08em">${OFFER.code}</div><div style="background:#2f4a3a;color:#fff;border-radius:14px;padding:18px 30px;font-size:28px;font-weight:600">Applied ✓</div></div>
      <div class="ln"><span>Subtotal</span><span>${OFFER.was}</span></div>
      <div class="ln" style="color:#2f7a4a"><span>Discount (${OFFER.pct})</span><span>− ${'$' + (parseInt(OFFER.was.slice(1)) - parseInt(OFFER.now.slice(1)))}</span></div>
      <div class="ln" style="border-top:2px solid #eee;margin-top:10px;padding-top:24px;font-family:Montserrat;font-weight:900;font-size:50px"><span>Total</span><span>${OFFER.now}</span></div>
    </div>
    <div class="abs" style="left:60px;right:60px;top:1080px;background:#161412;color:#fff;border-radius:999px;padding:34px;text-align:center;font-family:Montserrat;font-weight:800;font-size:36px;letter-spacing:.06em">CHECK OUT</div>
    <div class="abs" style="left:0;right:0;bottom:60px;text-align:center;font-size:28px;color:#4a4540">One click away from your new favourite padel accessory.</div>`,
});

/* Q07 — Missing poster */
add({
  id: 'q07-missing-poster', stage: 'TOFU', format: 'Missing poster',
  css: `body{background:#6b5a4a}`,
  html: `
    <div class="abs" style="left:110px;top:60px;width:860px;height:1230px;background:#f4ecd8;box-shadow:0 30px 60px rgba(0,0,0,.45);transform:rotate(-1.5deg);padding:60px 60px 0;text-align:center;color:#1d1a16">
      <div style="position:absolute;left:400px;top:-16px;width:60px;height:60px;border-radius:50%;background:radial-gradient(#e04a3a,#a02a1e);box-shadow:0 6px 10px rgba(0,0,0,.4)"></div>
      <div style="font-family:Oswald;font-weight:700;font-size:200px;line-height:1;letter-spacing:.04em">MISSING</div>
      <div style="font-family:Oswald;font-weight:500;font-size:46px;margin-top:6px">YOUR RACKET’S PROTECTION</div>
      <div style="position:relative;height:440px;margin:34px 40px;background:#e2d6bd;border:3px solid #1d1a16;overflow:hidden">${crop('IMG_9618.JPG', 0.6, 0.4, 1.8, 734, 440).img}<div style="position:absolute;inset:0;background:rgba(150,110,60,.35);mix-blend-mode:multiply"></div></div>
      <div style="font-family:'Courier Prime';font-size:30px;line-height:1.5;text-align:left;padding:0 20px">
        <b>LAST SEEN:</b> loose in a car boot, next to the keys.<br><b>DESCRIPTION:</b> nothing between it and the world.<br><b>IF FOUND:</b> put it in a COVR.</div>
      <div style="margin-top:30px;border-top:3px dashed #1d1a16;padding-top:24px;font-family:Oswald;font-weight:700;font-size:56px">REWARD: ${OFFER.pct} OFF · ${OFFER.code}</div>
    </div>`,
});

/* Q08 — Periodic element */
add({
  id: 'q08-element-cv', stage: 'MOFU', format: 'Periodic element',
  css: `body{background:#161412;color:#f3ede3}`,
  html: `
    <div class="abs" style="left:60px;right:60px;top:70px"><div class="mega" style="font-size:70px">The essential element</div><div class="mega" style="font-size:70px;color:#d9a970">of every padel bag.</div></div>
    <div class="abs" style="left:290px;top:330px;width:500px;height:560px;border:6px solid #d9a970;border-radius:24px;padding:30px 36px;background:linear-gradient(160deg,#2a2420,#161412)">
      <div style="display:flex;justify-content:space-between;font-size:34px;color:#d9a970"><span>199</span><span>${OFFER.now}*</span></div>
      <div style="font-family:'Instrument Serif';font-size:280px;line-height:1;text-align:center;margin-top:10px">Cv</div>
      <div style="text-align:center;font-family:Montserrat;font-weight:800;font-size:42px;letter-spacing:.1em">COVR</div>
      <div style="text-align:center;font-size:22px;color:#c9bca8;margin-top:10px">Canvas · Leather · Metal</div></div>
    <div class="abs" style="left:60px;right:60px;top:960px;display:grid;grid-template-columns:1fr 1fr;gap:18px 40px;font-size:26px">
      ${[['Group', 'Racket protection'], ['State', 'Waterproof-lined'], ['Bonds with', 'Rackets, phones, keys'], ['Reactivity', 'Draws compliments']].map(([a, b]) => `<div style="border-top:1px solid rgba(243,237,227,.25);padding-top:12px"><div style="font-size:18px;letter-spacing:.15em;color:#d9a970">${a.toUpperCase()}</div><div style="margin-top:4px">${b}</div></div>`).join('')}
    </div>
    <div class="abs" style="left:60px;bottom:50px;font-size:20px;color:#8c857c">*with code ${OFFER.code} · ${OFFER.when.toLowerCase()}</div>`,
});

/* Q09 — Paint-chip colour cards */
{
  const chips = [['Latte', '#e3d8c8'], ['Mocha', '#84694f'], ['Coffee', '#3f2d26'], ['Vanilla Cream', '#ece5d5'], ['Sky Denim', '#b8c7d6'], ['Ash', '#9b9996'], ['Baby Pink', '#e6b9b2'], ['Navy', '#2b3346'], ['Total Black', '#1c1b1a'], ['Ginger', '#dccbb0']];
  add({
    id: 'q09-colour-chips', stage: 'MOFU', format: 'Colour chips',
    css: `body{background:#f6f3ee}`,
    html: `
      <div class="abs" style="left:60px;right:60px;top:60px"><div class="serif" style="font-size:96px;line-height:.95">Ten colours.<br><em class="tan">Same obsession with details.</em></div></div>
      <div class="abs" style="left:60px;right:60px;top:330px;display:grid;grid-template-columns:repeat(5,1fr);gap:18px">
        ${chips.map(([n, c], i) => `<div style="background:#fff;box-shadow:0 10px 24px rgba(0,0,0,.08);transform:rotate(${[-2, 1, -1, 2, -1.5, 1.5, -1, 1, 2, -2][i]}deg)">
          <div style="height:240px;background:${c}"></div><div style="padding:14px 14px 18px"><div style="font-family:Montserrat;font-weight:800;font-size:21px">COVR ${String(i + 1).padStart(2, '0')}</div><div style="font-size:20px;color:#4a4540">${n}</div></div></div>`).join('')}
      </div>
      ${cut('mocha', 700, 1060, 330, -70, '0 20px 30px rgba(0,0,0,.3)')}
      <div class="abs" style="left:60px;top:1060px;width:560px"><div style="font-size:28px;line-height:1.4">Which one is yours? Every colour: cotton, leather, metal hardware.</div>
        <div style="margin-top:28px">${btn(`${OFFER.pct} off · ${OFFER.code}`)}</div></div>`,
  });
}

/* Q10 — Polaroid scrapbook */
{
  const pol = (n, cx, cy, z, x, y, r, cap) => `<div class="abs" style="left:${x}px;top:${y}px;width:440px;background:#fff;padding:18px 18px 0;transform:rotate(${r}deg);box-shadow:0 20px 40px rgba(0,0,0,.25)">
    <div style="position:relative;width:404px;height:420px;overflow:hidden">${crop(n, cx, cy, z, 404, 420).img}</div>
    <div style="font-family:Caveat;font-weight:700;font-size:46px;text-align:center;padding:8px 0 14px;color:#26231f">${cap}</div>
    <div style="position:absolute;left:150px;top:-20px;width:140px;height:42px;background:rgba(214,190,150,.7);transform:rotate(${-r * 2}deg)"></div></div>`;
  add({
    id: 'q10-scrapbook', stage: 'BOFU', format: 'Scrapbook',
    css: `body{background:#e9dfd0}`,
    html: `
      <div class="abs" style="left:60px;top:50px;font-family:Caveat;font-weight:700;font-size:96px;color:#3a2a20;transform:rotate(-2deg)">padel season, documented</div>
      ${pol('latte-walking-court.jpg', 0.45, 0.55, 1.1, 60, 210, -5, 'court 3, 7pm')}
      ${pol('IMG_8776.jpg', 0.47, 0.55, 1.1, 560, 240, 4, 'the unboxing')}
      ${pol('mocha-zip-bench.jpg', 0.5, 0.45, 1.3, 90, 760, 3, 'zip pocket = keys')}
      ${pol('crest-duo-closeup.jpg', 0.4, 0.4, 1.4, 560, 780, -4, 'his & hers')}
      <div class="abs" style="left:380px;top:640px;width:300px;height:300px;border-radius:50%;background:#b5452e;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);box-shadow:0 14px 30px rgba(0,0,0,.3)">
        <div style="font-family:Montserrat;font-weight:900;font-size:84px;line-height:1">${OFFER.pct}</div><div style="font-weight:700;font-size:28px;letter-spacing:.15em">OFF</div><div style="font-size:22px;margin-top:8px">${OFFER.code}</div></div>`,
  });
}

/* Q11 — Calendar with circled day */
{
  // October 2026 starts on a Thursday. OFFER_END_DAY is the day circled in marker.
  const END = 18, first = 3, days = 31;
  const cells = Array.from({ length: first }, () => '').concat(Array.from({ length: days }, (_, i) => i + 1));
  add({
    id: 'q11-calendar', stage: 'BOFU', format: 'Calendar',
    css: `body{background:#2f4a3a}`,
    html: `
      <div class="abs" style="left:0;right:0;top:60px;text-align:center;color:#f3ede3"><div class="mega" style="font-size:76px">Mark your calendar.</div><div style="font-size:32px;margin-top:10px">${OFFER.pct} off every COVR. Code <b>${OFFER.code}</b>.</div></div>
      <div class="abs" style="left:90px;right:90px;top:270px;background:#fbf8f2;border-radius:16px;box-shadow:0 30px 60px rgba(0,0,0,.35);padding:40px 44px">
        <div style="display:flex;justify-content:space-between;align-items:baseline"><div class="serif" style="font-size:90px">October</div><div style="font-family:Montserrat;font-weight:800;font-size:40px;color:#9b6b3e">2026</div></div>
        <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-top:20px;text-align:center">
          ${['M', 'T', 'W', 'T', 'F', 'S', 'S'].map(d => `<div style="font-weight:700;font-size:24px;color:#8c857c">${d}</div>`).join('')}
          ${cells.map(d => `<div style="position:relative;height:92px;display:flex;align-items:center;justify-content:center;font-size:36px;${d && d < 11 ? 'color:#c9c1b4;text-decoration:line-through' : ''}${d === END ? ';font-weight:800' : ''}">${d}${d === END ? '<svg style="position:absolute;inset:-14px" viewBox="0 0 100 100"><ellipse cx="50" cy="52" rx="44" ry="38" fill="none" stroke="#d4342b" stroke-width="5" transform="rotate(-8 50 50)"/></svg>' : ''}</div>`).join('')}
        </div></div>
      <div class="abs" style="left:640px;top:1110px;font-family:Caveat;font-weight:700;font-size:58px;color:#f3ede3;transform:rotate(-4deg)">last day!</div>
      <div class="abs" style="left:90px;bottom:70px">${btn('Shop before it ends', 'background:#f3ede3;color:#161412')}</div>`,
  });
}

/* Q12 — Restaurant menu */
add({
  id: 'q12-menu', stage: 'MOFU', format: 'Menu',
  html: `
    ${frame('latte-thankyou-card.jpg', 0.5, 0.5, 1.03, 0, 0, 1080, 1350, 'filter:blur(6px) brightness(.55)').html}
    <div class="abs" style="left:170px;top:70px;width:740px;height:1210px;background:#fbf7ef;box-shadow:0 30px 60px rgba(0,0,0,.5);padding:70px 70px;text-align:center;color:#2a1f18">
      <div class="logo" style="font-size:56px">COVR</div><div class="kicker" style="font-size:18px;margin-top:14px;color:#9b6b3e">Menu du jour</div>
      <div style="width:80px;border-top:2px solid #9b6b3e;margin:30px auto"></div>
      ${[['To start', 'Front zip pocket', 'phone, keys and cards'], ['Main', 'Cotton canvas', 'with leather trim and metal hardware'], ['On the side', 'Adjustable strap', 'and a carry handle'], ['To finish', 'Waterproof lining', 'wipe clean, served cold or hot']].map(([c, d, s]) => `<div style="margin-bottom:34px"><div class="kicker" style="font-size:16px;color:#8c857c">${c}</div><div class="serif" style="font-size:50px;margin-top:6px">${d}</div><div class="serif" style="font-size:30px;color:#6f6a62"><em>${s}</em></div></div>`).join('')}
      <div style="width:80px;border-top:2px solid #9b6b3e;margin:20px auto 30px"></div>
      <div class="kicker" style="font-size:18px;color:#b5452e">Chef’s special</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:56px;margin-top:8px">${OFFER.pct} off · ${OFFER.code}</div>
      <div class="serif" style="font-size:34px;margin-top:6px"><s style="color:#8c857c">${OFFER.was}</s> <em>${OFFER.now}</em></div>
    </div>`,
});

/* Q13 — Recipe card */
add({
  id: 'q13-recipe', stage: 'TOFU', format: 'Recipe card',
  css: `body{background:#c9b49a}`,
  html: `
    <div class="abs" style="left:80px;top:80px;width:920px;height:1190px;background:#fffdf7;box-shadow:0 30px 60px rgba(0,0,0,.25);padding:60px 70px;background-image:repeating-linear-gradient(#fffdf7 0 58px,#d8e2ee 58px 60px);transform:rotate(-1deg)">
      <div style="border-left:4px solid #e3a0a0;position:absolute;left:150px;top:0;bottom:0"></div>
      <div style="padding-left:110px;font-family:Caveat;font-weight:700;color:#2a2420">
        <div style="font-size:92px;line-height:1">Recipe: the perfect padel day</div>
        <div style="font-size:36px;color:#9b6b3e;margin:6px 0 30px">serves 1 player · prep 2 mins</div>
        <div style="font-size:50px">Ingredients</div>
        <div style="font-size:44px;line-height:60px">— 1 racket you love<br>— 3 fresh balls<br>— 1 bottle of water<br>— 1 COVR <span style="color:#b5452e">(non-negotiable)</span></div>
        <div style="font-size:50px;margin-top:30px">Method</div>
        <div style="font-size:44px;line-height:60px">1. Racket into COVR. Zip.<br>2. Keys & phone in the front pocket.<br>3. Strap on. Play. Repeat.</div>
        <div style="font-size:46px;margin-top:30px;color:#b5452e">chef’s tip: ${OFFER.pct} off with ${OFFER.code}</div>
      </div></div>
    ${cut('coffee', 650, 1040, 420, -28, '0 20px 30px rgba(0,0,0,.35)')}`,
});

/* Q14 — Scratch card */
add({
  id: 'q14-scratch-card', stage: 'BOFU', format: 'Scratch card',
  css: `body{background:radial-gradient(ellipse at 50% 40%,#3b2c22,#141110)}`,
  html: `
    <div class="abs" style="left:0;right:0;top:70px;text-align:center;color:#f3ede3"><div class="serif" style="font-size:92px;line-height:1">Scratch to reveal<br><em style="color:#e3c08f">your COVR perk.</em></div></div>
    <div class="abs" style="left:110px;top:360px;width:860px;height:600px;border-radius:30px;background:linear-gradient(135deg,#f6efe2,#e6d6bd);box-shadow:0 30px 70px rgba(0,0,0,.55);padding:40px;overflow:hidden">
      <div style="display:flex;justify-content:space-between"><span class="logo" style="font-size:36px">COVR</span><span class="kicker" style="font-size:16px">Lucky court</span></div>
      <div style="position:absolute;left:80px;right:80px;top:150px;height:330px;border-radius:20px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center">
        <div style="font-family:Montserrat;font-weight:900;font-size:150px;color:#b5452e;line-height:1">${OFFER.pct} OFF</div><div style="font-size:30px;margin-top:10px">code <b>${OFFER.code}</b></div></div>
      <svg style="position:absolute;left:80px;top:150px" width="700" height="330" viewBox="0 0 700 330"><defs><linearGradient id="s" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#d9d6d0"/><stop offset=".5" stop-color="#b9b5ae"/><stop offset="1" stop-color="#e2dfd9"/></linearGradient>
        <mask id="m"><rect width="700" height="330" fill="#fff"/><path d="M-20 300 C 120 120 200 360 330 160 S 520 40 620 220 S 720 120 760 60" stroke="#000" stroke-width="150" fill="none" stroke-linecap="round"/></mask></defs>
        <rect width="700" height="330" rx="20" fill="url(#s)" mask="url(#m)"/></svg>
      <div style="position:absolute;left:0;right:0;bottom:30px;text-align:center;font-size:22px;color:#6f6a62">Valid on every colour · ${OFFER.when.toLowerCase()}</div></div>
    ${cut('mocha', 330, 990, 420, -78, '0 20px 30px rgba(0,0,0,.5)')}`,
});

/* Q15 — Horoscope */
add({
  id: 'q15-horoscope', stage: 'TOFU', format: 'Horoscope',
  css: `body{background:radial-gradient(ellipse at 50% 30%,#2b2340,#120f1c 70%);color:#f3ede3}`,
  html: `
    <svg class="fill" width="1080" height="1350" style="position:absolute">${Array.from({ length: 90 }, (_, i) => `<circle cx="${(i * 197) % 1080}" cy="${(i * 331) % 1350}" r="${(i % 3) + 1}" fill="#fff" opacity="${0.3 + (i % 5) / 10}"/>`).join('')}</svg>
    <div class="abs" style="left:0;right:0;top:70px;text-align:center"><div class="kicker" style="font-size:20px;color:#e3c08f">Your padel horoscope · this week</div>
      <div class="serif" style="font-size:96px;line-height:1;margin-top:16px">A new racket cover<br><em style="color:#e3c08f">is in your stars.</em></div></div>
    <div class="abs" style="left:340px;top:400px;width:400px;height:400px;border-radius:50%;border:2px solid rgba(227,192,143,.6);padding:20px"><div style="width:100%;height:100%;border-radius:50%;overflow:hidden;position:relative">${crop('crest-duo-closeup.jpg', 0.3, 0.37, 2.0, 360, 360).img}</div></div>
    <div class="abs" style="left:80px;right:80px;top:860px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;text-align:center;font-size:24px;line-height:1.35">
      ${[['Aries · Leo · Sagittarius', 'Bold energy. You need a bold colour.'], ['Taurus · Virgo · Capricorn', 'You value craft. Leather agrees.'], ['Gemini · Libra · Aquarius', 'Pick two. You’ll want both.']].map(([s, t]) => `<div><div style="color:#e3c08f;font-weight:600;font-size:19px;letter-spacing:.08em">${s.toUpperCase()}</div><div style="margin-top:8px">${t}</div></div>`).join('')}
    </div>
    <div class="abs" style="left:0;right:0;bottom:70px;text-align:center;font-size:28px">Lucky code: <b style="color:#e3c08f;letter-spacing:.08em">${OFFER.code}</b> · ${OFFER.pct} off</div>`,
});

module.exports = ads;

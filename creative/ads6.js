// Round 5: hooks + promo mix. 15 ads, 1080x1350.
// ⚠️ OFFER below must match a real discount in Shopify before any of these run. Change it here, re-render, done.
const OFFER = { pct: '20%', code: 'COVR20', was: '$199', now: '$159', when: 'This week only', hours: '48' };

const { crop, frame, ARROW } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');
const cut = (n, x, y, w, rot = 0, shadow = '0 40px 50px rgba(40,25,10,.35)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  return `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${w * H / W}px;transform:rotate(${rot}deg);filter:drop-shadow(${shadow})">`;
};
const disc = (n, cx, cy, z, d, x, y, border = '6px solid #fff') => `<div style="position:absolute;left:${x}px;top:${y}px;width:${d}px;height:${d}px;border-radius:50%;overflow:hidden;border:${border};box-shadow:0 12px 30px rgba(0,0,0,.25)">${crop(n, cx, cy, z, d - 12, d - 12).img}</div>`;
const strip = (bg = 'var(--ink)', fg = 'var(--paper)') => `<div class="abs" style="left:0;right:0;bottom:0;height:96px;background:${bg};color:${fg};display:flex;align-items:center;justify-content:center;gap:26px;font-family:Montserrat;font-weight:800;font-size:28px;letter-spacing:.06em">
  <span>${OFFER.pct} OFF</span><span style="opacity:.5">·</span><span>CODE ${OFFER.code}</span><span style="opacity:.5">·</span><span style="font-weight:600">${OFFER.when.toUpperCase()}</span></div>`;
const priceTag = (x, y, rot = -8) => `<div class="abs" style="left:${x}px;top:${y}px;transform:rotate(${rot}deg);background:#fff;border-radius:12px 60px 60px 12px;padding:16px 46px 16px 30px;box-shadow:0 14px 30px rgba(0,0,0,.3);display:flex;align-items:center;gap:18px">
  <span style="width:18px;height:18px;border-radius:50%;background:#d9cfc1"></span>
  <span style="font-size:30px;color:#8c857c;text-decoration:line-through">${OFFER.was}</span>
  <span style="font-family:Montserrat;font-weight:900;font-size:56px;color:#b5452e">${OFFER.now}</span></div>`;
const btn = (t, style = '') => `<span class="btn" style="${style}">${t} ${ARROW}</span>`;
const ads = [];
const add = a => ads.push({ outDir: 'promo', ...a });

/* P01 TOFU — On court / off court split */
add({
  id: 'p01-not-just-on-court', stage: 'TOFU', format: 'Split scene',
  html: `
    ${frame('latte-walking-court.jpg', 0.45, 0.55, 1.0, 0, 0, 1080, 560).html}
    ${frame('IMG_8754.jpg', 0.5, 0.55, 1.0, 0, 560, 1080, 694).html}
    <div class="abs kicker" style="left:40px;top:40px;background:#fff;padding:10px 20px;font-size:18px">On the court ✓</div>
    <div class="abs kicker" style="left:40px;top:1170px;background:#b5452e;color:#fff;padding:10px 20px;font-size:18px">Off the court?</div>
    <div class="abs" style="left:0;right:0;top:470px;display:flex;justify-content:center;pointer-events:none">
      <div style="background:var(--paper);padding:26px 40px;box-shadow:0 20px 50px rgba(0,0,0,.35);text-align:center;transform:rotate(-2deg)">
        <div class="mega" style="font-size:58px">Your racket isn’t just</div>
        <div class="mega tan" style="font-size:58px">at risk on the court.</div></div></div>
    ${strip()}`,
});

/* P02 TOFU — Phone case analogy */
add({
  id: 'p02-phone-unprotected', stage: 'TOFU', format: 'Analogy',
  css: `body{background:#efe9df}.card{position:absolute;top:400px;width:460px;height:700px;border-radius:30px;background:#fff;box-shadow:0 20px 50px rgba(0,0,0,.08);text-align:center;padding-top:40px}
        .lbl{font-family:Montserrat;font-weight:800;font-size:34px;margin-top:20px}.sub{font-size:23px;color:#6f6a62;margin-top:6px}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:70px"><div class="mega" style="font-size:80px">You wouldn’t leave</div><div class="mega" style="font-size:80px">your phone</div><div class="mega tan" style="font-size:80px">unprotected.</div></div>
    <div class="card" style="left:60px">
      <div style="width:230px;height:450px;margin:0 auto;border-radius:44px;background:#9b6b3e;padding:14px;box-shadow:0 18px 30px rgba(0,0,0,.2)">
        <div style="width:100%;height:100%;border-radius:34px;background:linear-gradient(160deg,#2a2724,#4a4540);position:relative"><div style="position:absolute;left:78px;top:14px;width:46px;height:12px;border-radius:6px;background:#111"></div></div></div>
      <div class="lbl">Phone: in a case</div><div class="sub">Obviously.</div></div>
    <div class="card" style="left:560px">
      <div style="position:relative;height:450px">${cut('coffee', -30, 70, 520, -58, '0 20px 24px rgba(0,0,0,.3)')}</div>
      <div class="lbl">Racket: in a COVR</div><div class="sub">Also obviously.</div></div>
    <div class="abs" style="left:0;right:0;top:1140px;text-align:center;font-size:30px">Now <s style="color:#8c857c">${OFFER.was}</s> <b style="color:#b5452e;font-family:Montserrat;font-weight:900;font-size:40px">${OFFER.now}</b> with code <b>${OFFER.code}</b></div>
    <div class="abs" style="left:0;right:0;bottom:60px;display:flex;justify-content:center">${btn('Protect yours')}</div>`,
});

/* P03 TOFU — Scoreboard */
add({
  id: 'p03-scoreboard', stage: 'TOFU', format: 'Scoreboard',
  css: `body{background:#111}.sb{font-family:Oswald;font-weight:700;color:#ffb547;text-shadow:0 0 18px rgba(255,170,60,.6)}`,
  html: `
    <div class="abs" style="left:60px;right:60px;top:60px;background:#1b1b1b;border:3px solid #333;border-radius:20px;padding:30px 40px">
      <div style="display:flex;justify-content:space-between;color:#8a8a8a;font-size:22px;letter-spacing:.2em;margin-bottom:10px"><span>COURT 3</span><span>FINAL</span></div>
      ${[['YOU', 6, 6], ['THEM', 4, 3]].map(([n, a, b]) => `<div style="display:flex;align-items:center;gap:30px;margin:6px 0"><span class="sb" style="flex:1;font-size:76px;color:#fff;text-shadow:none">${n}</span><span class="sb" style="font-size:96px;width:80px;text-align:center">${a}</span><span class="sb" style="font-size:96px;width:80px;text-align:center">${b}</span></div>`).join('')}
    </div>
    <div class="abs" style="left:60px;right:60px;top:480px;color:#fff;font-family:Oswald;font-weight:700;font-size:76px;line-height:1.02;text-transform:uppercase">The match ends.<br><span style="color:#d9a970">The damage doesn’t<br>have to start.</span></div>
    ${frame('latte-thankyou-card.jpg', 0.5, 0.55, 1.0, 0, 830, 1080, 424).html}
    <div class="abs" style="left:0;right:0;top:830px;height:120px;background:linear-gradient(#111,transparent)"></div>
    ${strip('#d9a970', '#111')}`,
});

/* P04 TOFU — How you carry it says a lot (3 carry styles) */
add({
  id: 'p04-how-you-carry', stage: 'TOFU', format: 'Three-up',
  css: `body{background:var(--paper)}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:64px"><div class="mega" style="font-size:68px">How you carry your</div><div class="mega tan" style="font-size:68px">racket says a lot.</div></div>
    ${[['IMG_0582.JPG', 0.6, 0.5, 1.9, 'The classic', 'By the handle'], ['IMG_0580.JPG', 0.6, 0.45, 1.7, 'The commuter', 'On your back'], ['mocha-strap-studio.jpg', 0.45, 0.5, 1.25, 'The main character', 'On the shoulder']]
      .map(([n, cx, cy, z, t, s], i) => `${frame(n, cx, cy, z, 56 + i * 330, 300, 310, 760, 'border-radius:16px').html}
        <div class="abs" style="left:${56 + i * 330}px;top:1080px;width:310px"><div style="font-family:Montserrat;font-weight:800;font-size:28px">${t}</div><div style="font-size:22px;color:var(--stone)">${s}</div></div>`).join('')}
    ${strip()}`,
});

/* P05 MOFU — Look closer (magnifier) */
{
  const f = frame('latte-unboxing-hands.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 1350);
  const [mx, my] = f.at(0.74, 0.585);
  const d = 440;
  add({
    id: 'p05-look-closer', stage: 'MOFU', format: 'Magnifier',
    html: `
      ${f.html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(14,10,8,.82) 0%,rgba(14,10,8,.2) 30%,transparent 45%)"></div>
      <div class="abs" style="left:56px;right:56px;top:60px;color:#fff"><div class="mega" style="font-size:84px">Look closer.</div><div style="font-family:Montserrat;font-weight:700;font-size:38px;margin-top:10px">This isn’t your ordinary racket cover.</div></div>
      <div class="abs" style="left:${mx + 150}px;top:${my + 140}px;width:60px;height:260px;background:linear-gradient(90deg,#2a2724,#5a5550,#2a2724);border-radius:20px;transform:rotate(-40deg);transform-origin:top center"></div>
      <div class="abs" style="left:${mx - d / 2}px;top:${my - d / 2}px;width:${d}px;height:${d}px;border-radius:50%;overflow:hidden;border:18px solid #2a2724;box-shadow:0 20px 50px rgba(0,0,0,.45),inset 0 0 40px rgba(255,255,255,.25)">${crop('latte-unboxing-hands.jpg', 0.74, 0.585, 5.2, d - 36, d - 36).img}</div>
      <div class="abs" style="left:56px;bottom:56px;background:#fff;border-radius:999px;padding:16px 30px;font-size:26px"><b>Embroidered crest.</b> Leather trim. Gold zip. · <b style="color:#b5452e">${OFFER.pct} off</b></div>`,
  });
}

/* P06 MOFU — See / Feel */
add({
  id: 'p06-see-and-feel', stage: 'MOFU', format: 'Split detail',
  css: `body{background:var(--paper)}`,
  html: `
    ${frame('crest-duo-closeup.jpg', 0.35, 0.36, 1.7, 0, 0, 540, 1010).html}
    ${frame('web-lining-closeup.png', 0.62, 0.55, 1.0, 540, 0, 540, 1010).html}
    <div class="abs" style="left:0;top:0;width:540px;height:1010px;background:linear-gradient(transparent 55%,rgba(0,0,0,.6))"></div>
    <div class="abs" style="left:540px;top:0;width:540px;height:1010px;background:linear-gradient(transparent 55%,rgba(0,0,0,.6))"></div>
    <div class="abs" style="left:40px;top:830px;color:#fff"><div class="kicker" style="font-size:18px">You see</div><div style="font-family:Montserrat;font-weight:800;font-size:36px;margin-top:6px">Embroidered crest.<br>Gold zip.</div></div>
    <div class="abs" style="left:580px;top:830px;color:#fff"><div class="kicker" style="font-size:18px">You feel</div><div style="font-family:Montserrat;font-weight:800;font-size:36px;margin-top:6px">Waterproof lining.<br>Soft cotton.</div></div>
    <div class="abs" style="left:56px;right:56px;top:1050px;display:flex;justify-content:space-between;align-items:center">
      <div><div class="mega" style="font-size:58px">Some details you see.</div><div class="mega tan" style="font-size:58px">Others you feel.</div></div></div>
    <div class="abs" style="left:56px;bottom:56px;font-size:26px">${OFFER.pct} off with code <b>${OFFER.code}</b> · ${OFFER.when.toLowerCase()}</div>`,
});

/* P07 MOFU — Protection can look this good (fashion editorial + price tag) */
add({
  id: 'p07-look-this-good', stage: 'MOFU', format: 'Editorial + price tag',
  html: `
    ${frame('mocha-strap-studio.jpg', 0.5, 0.5, 1.03, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(255,255,255,.85) 0%,transparent 26%,transparent 70%,rgba(20,14,10,.55) 100%)"></div>
    <div class="serif abs" style="left:56px;right:56px;top:50px;font-size:100px;line-height:.95;color:#2a1f18">Who said protection<br><em style="color:#8a5a32">can’t look this good?</em></div>
    ${priceTag(620, 1110, -6)}
    <div class="abs kicker" style="left:56px;bottom:70px;color:#fff;font-size:18px">Code ${OFFER.code} · ${OFFER.when}</div>`,
});

/* P08 MOFU — Doesn't look like a cover (checkbox quiz) */
add({
  id: 'p08-doesnt-look-like-a-cover', stage: 'MOFU', format: 'Quiz',
  html: `
    ${frame('IMG_0617.JPG', 0.48, 0.55, 1.12, 0, 0, 1080, 1350).html}
    <div class="abs" style="left:56px;top:60px;background:var(--paper);padding:30px 36px;border-radius:18px;box-shadow:0 20px 40px rgba(0,0,0,.18);width:560px">
      <div style="font-family:Montserrat;font-weight:800;font-size:40px;line-height:1.08;margin-bottom:22px">The cover that doesn’t look like a cover.</div>
      ${[['A handbag', false], ['A clutch', false], ['A padel racket cover', true]].map(([t, on]) => `<div style="display:flex;gap:18px;align-items:center;font-size:32px;margin:12px 0">
        <span style="width:40px;height:40px;border:3px solid #26231f;border-radius:8px;display:flex;align-items:center;justify-content:center;background:${on ? '#26231f' : '#fff'}">${on ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>' : ''}</span>
        <span style="${on ? 'font-weight:700' : 'color:#6f6a62;text-decoration:line-through'}">${t}</span></div>`).join('')}
    </div>
    ${priceTag(560, 1150, 4)}`,
});

/* P09 BOFU — Your padel bag is about to get jealous */
add({
  id: 'p09-bag-jealous', stage: 'BOFU', format: 'Speech bubbles',
  css: `body{background:linear-gradient(180deg,#f3e9dc,#e6d4bd)}.bub{position:absolute;background:#fff;border-radius:40px;padding:22px 34px;font-size:34px;font-weight:600;box-shadow:0 10px 30px rgba(0,0,0,.1)}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:60px"><div class="mega" style="font-size:84px">Your padel bag</div><div class="mega tan" style="font-size:84px">is about to</div><div class="mega tan" style="font-size:84px">get jealous.</div></div>
    ${cut('coffee', 110, 560, 860, -8)}
    <div class="bub" style="left:620px;top:420px;transform:rotate(4deg)">who’s that??</div>
    <div class="bub" style="left:60px;top:1080px;transform:rotate(-3deg)">is that… leather?</div>
    ${strip()}`,
});

/* P10 BOFU — Retire that basic cover (certificate) */
add({
  id: 'p10-retirement-certificate', stage: 'BOFU', format: 'Certificate',
  css: `body{background:#3a2a20}`,
  html: `
    <div class="abs" style="left:70px;right:70px;top:70px;bottom:70px;background:#fbf6ea;border:3px solid #9b6b3e;outline:10px solid #fbf6ea;outline-offset:-26px;box-shadow:inset 0 0 0 30px #fbf6ea,inset 0 0 0 32px #9b6b3e;padding:110px 90px 70px;text-align:center;color:#2a1f18;display:flex;flex-direction:column;justify-content:space-between">
      <div class="kicker" style="font-size:20px;color:#9b6b3e">Official notice</div>
      <div class="serif" style="font-size:100px;line-height:1;margin:16px 0 0">Certificate of <em>Retirement</em></div>
      <div><div style="font-size:32px;color:#4a4540">This certifies that</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:66px;margin:20px 0;letter-spacing:-.01em">YOUR BASIC COVER</div>
      <div style="font-size:31px;line-height:1.45;color:#4a4540">is hereby retired after years of loyal-ish service.<br>Its replacement: cotton canvas, leather trim and an open-back handle.</div></div>
      <div class="serif" style="font-size:66px"><em>Ready to retire it?</em></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-end;padding:0 20px">
        <div style="text-align:left"><div style="font-family:Caveat;font-weight:700;font-size:64px;color:#2a1f18">COVR</div><div style="border-top:2px solid #2a1f18;width:260px;font-size:18px;letter-spacing:.2em;padding-top:8px">SIGNED</div></div>
        <div style="width:220px;height:220px;border-radius:50%;background:radial-gradient(#d8b06a,#a77a2c);box-shadow:0 8px 20px rgba(0,0,0,.25),inset 0 0 0 10px rgba(255,255,255,.25);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#3a2a10;transform:rotate(-10deg)">
          <div style="font-family:Montserrat;font-weight:900;font-size:62px;line-height:1">${OFFER.pct}</div><div style="font-weight:700;font-size:22px;letter-spacing:.15em">OFF</div><div style="font-size:18px;margin-top:6px">${OFFER.code}</div></div>
      </div></div>`,
});

/* P11 BOFU — Gift tag */
add({
  id: 'p11-gift-tag', stage: 'BOFU', format: 'Gift',
  html: `
    ${frame('IMG_8776.jpg', 0.47, 0.55, 1.0, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(14,10,8,.8) 0%,transparent 34%)"></div>
    <div class="serif abs" style="left:56px;right:56px;top:56px;font-size:88px;line-height:.98;color:#fff">The perfect gift for someone<br><em style="color:#e3c08f">who lives for padel.</em></div>
    <svg class="abs" style="left:520px;top:640px" width="300" height="200"><path d="M10 10 C 120 120 200 40 290 190" fill="none" stroke="#f3ede3" stroke-width="3"/></svg>
    <div class="abs" style="left:640px;top:780px;width:360px;height:440px;background:#c8a57a;clip-path:polygon(20% 0,80% 0,100% 14%,100% 100%,0 100%,0 14%);transform:rotate(10deg);box-shadow:0 20px 40px rgba(0,0,0,.4);padding:110px 36px 0;color:#2a1f18;font-family:Caveat;font-weight:700">
      <div style="position:absolute;left:160px;top:34px;width:40px;height:40px;border-radius:50%;background:#2a1f18"></div>
      <div style="font-size:50px">To: my padel partner</div><div style="font-size:50px;margin-top:10px">From: me</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:40px;margin-top:40px">${OFFER.pct} OFF</div><div style="font-family:Inter;font-weight:600;font-size:22px">code ${OFFER.code}</div></div>`,
});

/* P12 Offer-first — 20% OFF */
add({
  id: 'p12-offer-first', stage: 'BOFU', format: 'Offer-first',
  css: `body{background:#b5452e;color:#fff}`,
  html: `
    <div class="abs kicker" style="left:0;right:0;top:70px;text-align:center;font-size:22px">Premium protection. Now</div>
    <div class="abs mega" style="left:0;right:0;top:110px;text-align:center;font-size:330px;line-height:.9;letter-spacing:-.05em">${OFFER.pct}</div>
    <div class="abs mega" style="left:0;right:0;top:400px;text-align:center;font-size:150px;letter-spacing:.02em">OFF</div>
    <div class="abs" style="left:150px;top:560px;width:780px;height:780px;border-radius:50%;background:radial-gradient(#d86a4f,transparent 70%)"></div>
    ${cut('coffee', 110, 610, 860, -10, '0 40px 50px rgba(60,10,0,.45)')}
    <div class="abs" style="left:0;right:0;bottom:70px;display:flex;justify-content:center;gap:20px;align-items:center">
      <span style="border:3px dashed #fff;border-radius:14px;padding:16px 34px;font-family:Montserrat;font-weight:800;font-size:38px;letter-spacing:.1em">${OFFER.code}</span>
      <span style="font-size:28px">${OFFER.when}</span></div>`,
});

/* P13 Urgency — countdown */
add({
  id: 'p13-48-hours', stage: 'BOFU', format: 'Countdown',
  css: `body{background:var(--ink);color:#fff}.t{width:220px;height:240px;border-radius:22px;background:#2a2724;display:flex;flex-direction:column;align-items:center;justify-content:center}`,
  html: `
    ${frame('IMG_0583.JPG', 0.5, 0.6, 1.0, 0, 560, 1080, 790).html}
    <div class="abs" style="left:0;right:0;top:560px;height:220px;background:linear-gradient(var(--ink),transparent)"></div>
    <div class="abs" style="left:0;right:0;top:64px;text-align:center"><div class="mega" style="font-size:96px">${OFFER.hours} hours.</div><div class="mega" style="font-size:96px;color:#d9a970">One special offer.</div></div>
    <div class="abs" style="left:0;right:0;top:340px;display:flex;justify-content:center;gap:20px">
      ${[[OFFER.hours, 'HOURS'], ['00', 'MINUTES'], ['00', 'SECONDS']].map(([n, l]) => `<div class="t"><div style="font-family:Oswald;font-weight:700;font-size:120px;line-height:1">${n}</div><div style="font-size:18px;letter-spacing:.2em;opacity:.6">${l}</div></div>`).join('')}
    </div>
    <div class="abs" style="left:0;right:0;bottom:70px;display:flex;justify-content:center">${btn(`${OFFER.pct} off · code ${OFFER.code}`, 'background:#d9a970;color:var(--ink)')}</div>`,
});

/* P14 Urgency — favourite colour going (REAL stock, Shopify 11 Oct 2026; update before running) */
{
  const rows = [
    ['Vanilla Cream', 1, 'IMG_0617.JPG', 0.42, 0.58, 2.6],
    ['Total Black', 1, 'IMG_0569.JPG', 0.17, 0.62, 3.8],
    ['Coffee', 1, 'IMG_0561.JPG', 0.42, 0.56, 2.2],
    ['Ash', 2, 'IMG_8754.jpg', 0.76, 0.43, 2.8],
    ['Baby Pink', 2, 'IMG_0628.JPG', 0.74, 0.6, 3.4],
  ];
  add({
    id: 'p14-color-gone', stage: 'BOFU', format: 'Low stock (real)',
    css: `body{background:var(--paper)}`,
    html: `
      <div class="abs" style="left:56px;right:56px;top:60px"><div class="mega" style="font-size:62px">Don’t wait until your</div><div class="mega tan" style="font-size:62px">favourite colour is gone.</div></div>
      <div class="abs" style="left:56px;right:56px;top:260px">
        ${rows.map(([n, k, img, cx, cy, z]) => `<div style="display:flex;align-items:center;gap:30px;padding:18px 0;border-bottom:1.5px solid var(--rule)">
          <div style="position:relative;width:140px;height:140px;flex:none">${disc(img, cx, cy, z, 140, 0, 0, '4px solid #fff')}</div>
          <div style="flex:1;font-family:Montserrat;font-weight:800;font-size:40px">${n}</div>
          <div style="text-align:right"><div style="font-weight:700;font-size:30px;color:#b5452e">${k === 1 ? 'Last one' : `${k} left`}</div>
            <div style="width:200px;height:12px;border-radius:6px;background:#e6ded2;margin-top:10px;overflow:hidden"><div style="width:${k * 12}%;height:100%;background:#b5452e"></div></div></div></div>`).join('')}
      </div>
      <div class="abs" style="left:0;right:0;bottom:60px;display:flex;justify-content:center">${btn('Shop before it’s gone')}</div>`,
  });
}

/* P15 VIP — COVR Club member card */
add({
  id: 'p15-covr-club', stage: 'BOFU', format: 'VIP card',
  css: `body{background:#14110e;color:#fff}`,
  html: `
    ${frame('IMG_8754.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 1350, 'filter:blur(4px) brightness(.45)').html}
    <div class="abs" style="left:0;right:0;top:80px;text-align:center"><div class="serif" style="font-size:96px;line-height:1">Welcome to the<br><em style="color:#e3c08f">COVR Club.</em></div>
      <div style="font-size:30px;margin-top:20px;opacity:.85">Your perk is waiting.</div></div>
    <div class="abs" style="left:140px;top:500px;width:800px;height:500px;border-radius:36px;background:linear-gradient(135deg,#2b2520 0%,#120f0c 55%,#3a3027 100%);box-shadow:0 40px 80px rgba(0,0,0,.6),inset 0 0 0 2px rgba(227,192,143,.4);padding:50px 56px;transform:rotate(-4deg)">
      <div style="display:flex;justify-content:space-between;align-items:center"><div class="logo" style="font-size:44px;color:#e3c08f">COVR</div><div class="kicker" style="font-size:16px;color:#e3c08f">Member</div></div>
      <div style="width:90px;height:66px;border-radius:12px;background:linear-gradient(135deg,#e3c08f,#a77a2c);margin:46px 0 34px"></div>
      <div style="font-family:'Courier Prime';font-size:40px;letter-spacing:.14em;color:#efe6d6">**** **** **** 0020</div>
      <div style="display:flex;justify-content:space-between;margin-top:30px;font-size:20px;letter-spacing:.14em;color:#c9bca8"><span>PERK: ${OFFER.pct} OFF</span><span>CODE: ${OFFER.code}</span></div></div>
    <div class="abs" style="left:0;right:0;bottom:80px;display:flex;justify-content:center">${btn('Claim your perk', 'background:#e3c08f;color:#14110e')}</div>`,
});

module.exports = ads;

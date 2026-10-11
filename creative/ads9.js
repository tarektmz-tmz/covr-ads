// Round 8: new studio photos (Oct 2026 shoot), photo-led style, rendered at 2x (2160x2700).
const { OFFER } = require('./ads6.js');
const { crop, frame, ARROW } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');
const RED = '#d4342b';
const cut = (n, x, y, w, rot = 0, shadow = '0 40px 50px rgba(40,25,10,.35)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  return `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${w * H / W}px;transform:rotate(${rot}deg);filter:drop-shadow(${shadow})">`;
};
const priceTag = (x, y, rot = -6) => `<div class="abs" style="left:${x}px;top:${y}px;transform:rotate(${rot}deg);background:#fff;border-radius:12px 60px 60px 12px;padding:16px 46px 16px 30px;box-shadow:0 14px 30px rgba(0,0,0,.3);display:flex;align-items:center;gap:18px">
  <span style="width:18px;height:18px;border-radius:50%;background:#d9cfc1"></span><span style="font-size:30px;color:#8c857c;text-decoration:line-through">${OFFER.was}</span>
  <span style="font-family:Montserrat;font-weight:900;font-size:56px;color:#b5452e">${OFFER.now}</span></div>`;
const topFade = (a = .8, to = 30) => `<div class="fill" style="background:linear-gradient(180deg,rgba(14,10,8,${a}) 0%,transparent ${to}%)"></div>`;
const small = (t, color = '#fff') => `<div class="abs kicker" style="left:56px;bottom:56px;color:${color};font-size:18px">${t}</div>`;
const full = n => frame(n, 0.5, 0.5, 1.0, 0, 0, 1080, 1350);
const ads = [];
const add = a => ads.push({ outDir: 'shoot', scale: 2, ...a });

/* S01 — Latte on the shoulder + price tag */
add({
  id: 's01-off-court-on-brand', stage: 'MOFU', format: 'Editorial + price tag',
  html: `
    ${full('latte-shoulder-court.jpg').html}
    ${topFade(.75, 26)}
    <div class="serif abs" style="left:56px;right:56px;top:50px;font-size:100px;line-height:.95;color:#fff">Off court.<br><em style="color:#f0d2a8">Still on brand.</em></div>
    ${priceTag(600, 1150, -5)}
    ${small(`Latte · code ${OFFER.code}`)}`,
});

/* S02 — Mocha in hands, red-marker details */
{
  const f = full('mocha-hands-turf.jpg');
  const notes = [
    ['real leather collar', [0.62, 0.12], [0.72, 0.2], 620, 60],
    ['gold zip', [0.1, 0.52], [0.36, 0.455], 40, 680],
    ['embroidered crest', [0.6, 0.83], [0.5, 0.68], 560, 1150],
  ];
  const arrows = notes.map(([, [ax, ay], [bx, by]]) => {
    const [x1, y1] = f.at(ax, ay), [x2, y2] = f.at(bx, by);
    const a = Math.atan2(y2 - y1, x2 - x1), L = 26, h = s => `${x2 - L * Math.cos(a + s)},${y2 - L * Math.sin(a + s)}`;
    return `<path d="M${x1} ${y1} Q ${(x1 + x2) / 2 + 40} ${(y1 + y2) / 2 - 40} ${x2} ${y2}" fill="none" stroke="${RED}" stroke-width="7" stroke-linecap="round"/><path d="M${h(-.5)} L${x2} ${y2} L${h(.5)}" fill="none" stroke="${RED}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>`;
  }).join('');
  add({
    id: 's02-every-detail-marked', stage: 'MOFU', format: 'Red-marker notes',
    html: `
      ${f.html}
      <svg class="fill" width="1080" height="1350" style="position:absolute">${arrows}</svg>
      ${notes.map(([t, , , x, y]) => `<div class="abs" style="left:${x}px;top:${y}px;font-family:Caveat;font-weight:700;font-size:62px;color:${RED};background:rgba(255,253,247,.9);padding:2px 18px;border-radius:8px;transform:rotate(-3deg)">${t}</div>`).join('')}
      <div class="abs" style="left:56px;top:56px;background:#fffdf7;padding:16px 28px;border-radius:6px;transform:rotate(-2deg);box-shadow:0 8px 24px rgba(0,0,0,.2);font-family:Caveat;font-weight:700;font-size:60px;color:#161412">ok, but look closer</div>
      <div class="abs" style="right:56px;bottom:56px;background:#161412;color:#fff;border-radius:999px;padding:16px 30px;font-weight:600;font-size:24px">${OFFER.pct} off · ${OFFER.code}</div>`,
  });
}

/* S03 — Friends + poll sticker (no fake results) */
add({
  id: 's03-friends-poll', stage: 'TOFU', format: 'Poll sticker',
  html: `
    ${full('latte-friends-phone.jpg').html}
    ${topFade(.55, 22)}
    <div class="abs" style="left:56px;top:56px;color:#fff"><div class="mega" style="font-size:80px">Your friends</div><div class="mega" style="font-size:80px;color:#f0d2a8">will ask.</div></div>
    <div class="abs" style="left:120px;top:1000px;width:620px;background:#fff;border-radius:30px;padding:28px 30px;box-shadow:0 20px 40px rgba(0,0,0,.35);transform:rotate(-3deg)">
      <div style="font-weight:700;font-size:32px;text-align:center;margin-bottom:18px">where did you get that??</div>
      <div style="display:flex;gap:14px">${['COVR', 'tell me now'].map(t => `<div style="flex:1;border:2px solid #e5e5e5;border-radius:16px;padding:16px;text-align:center;font-weight:700;font-size:28px;background:linear-gradient(90deg,#f2e3cf,#fff)">${t}</div>`).join('')}</div>
    </div>`,
});

/* S04 — Latte on the bench + swing tag on the D-ring */
{
  const f = full('latte-bench-clean.jpg');
  const [dx, dy] = f.at(0.395, 0.25);
  add({
    id: 's04-latte-swing-tag', stage: 'BOFU', format: 'Swing tag',
    html: `
      ${f.html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(255,250,244,.96) 0%,rgba(255,250,244,.85) 16%,transparent 30%)"></div>
      <div class="serif abs" style="left:56px;right:56px;top:46px;font-size:96px;line-height:.95;color:#2a1f18">Your racket has been<br><em style="color:#8a5a32">waiting for this.</em></div>
      <svg class="fill" width="1080" height="1350" style="position:absolute"><path d="M${dx} ${dy} C ${dx - 100} ${dy + 80} ${dx - 140} ${dy + 180} ${dx - 170} ${dy + 300}" fill="none" stroke="#fff" stroke-width="4"/></svg>
      <div class="abs" style="left:${dx - 330}px;top:${dy + 290}px;width:300px;height:420px;background:#f6f0e4;clip-path:polygon(20% 0,80% 0,100% 14%,100% 100%,0 100%,0 14%);transform:rotate(7deg);box-shadow:0 20px 40px rgba(0,0,0,.4);padding:96px 30px 0;text-align:center;color:#2a1f18">
        <div style="position:absolute;left:132px;top:30px;width:36px;height:36px;border-radius:50%;background:#2a1f18"></div>
        <div class="logo" style="font-size:36px">COVR</div><div class="kicker" style="font-size:14px;margin:12px 0 24px">Latte · Handmade</div>
        <div style="font-size:28px;color:#8c857c;text-decoration:line-through">${OFFER.was}</div>
        <div style="font-family:Montserrat;font-weight:900;font-size:64px;color:#b5452e;line-height:1">${OFFER.now}</div>
        <div style="font-size:18px;margin-top:12px">code ${OFFER.code}</div></div>`,
  });
}

/* S05 — Mocha on the bench + rubber stamp (Mocha stock 0 — restock first) */
add({
  id: 's05-mocha-stamp', stage: 'BOFU', format: 'Rubber stamp',
  html: `
    ${full('mocha-bench-clean.jpg').html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(255,250,244,.9) 0%,transparent 22%)"></div>
    <div class="serif abs" style="left:56px;right:56px;top:46px;font-size:96px;line-height:.95;color:#2a1f18">Premium craftsmanship.<br><em style="color:#8a5a32">A price worth celebrating.</em></div>
    <div class="abs" style="left:60px;top:900px;width:360px;height:360px;border-radius:50%;border:12px solid ${RED};color:${RED};display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-14deg);opacity:.92;background:rgba(255,250,244,.35);
      -webkit-mask:repeating-radial-gradient(circle at 30% 40%,#000 0 3px,rgba(0,0,0,.75) 3px 5px)">
      <div style="position:absolute;inset:14px;border-radius:50%;border:4px solid ${RED}"></div>
      <div style="font-family:Oswald;font-weight:700;font-size:36px;letter-spacing:.2em">COVR</div>
      <div style="font-family:Oswald;font-weight:700;font-size:130px;line-height:1">${OFFER.pct}</div>
      <div style="font-family:Oswald;font-weight:700;font-size:50px;letter-spacing:.15em">OFF</div></div>`,
});

/* S06 — Latte or Mocha? cutouts side by side */
add({
  id: 's06-latte-or-mocha', stage: 'TOFU', format: 'This or that (cutouts)',
  css: `body{background:linear-gradient(90deg,#efe6d8 50%,#3a2a20 50%)}`,
  html: `
    <div class="abs" style="left:0;right:0;top:60px;text-align:center"><span class="mega" style="font-size:88px;color:#3a2a20">Latte </span><span class="serif" style="font-size:96px;color:#9b6b3e"><em>or</em></span><span class="mega" style="font-size:88px;color:#f3ede3"> Mocha?</span></div>
    ${cut('latte-bench', 40, 250, 470, -4)}
    ${cut('mocha-bench', 570, 250, 470, 4, '0 40px 50px rgba(0,0,0,.55)')}
    <div class="abs" style="left:0;width:540px;bottom:60px;text-align:center;color:#3a2a20"><div style="font-family:Montserrat;font-weight:800;font-size:30px">Natural canvas</div><div style="font-size:22px;margin-top:4px">dark brown leather</div></div>
    <div class="abs" style="left:540px;width:540px;bottom:60px;text-align:center;color:#f3ede3"><div style="font-family:Montserrat;font-weight:800;font-size:30px">Walnut canvas</div><div style="font-size:22px;margin-top:4px">crème leather</div></div>
    <div class="abs" style="left:440px;top:640px;width:200px;height:200px;border-radius:50%;background:#b5452e;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 14px 30px rgba(0,0,0,.35)"><div style="font-size:18px;letter-spacing:.15em">BOTH</div><div style="font-family:Montserrat;font-weight:900;font-size:50px">${OFFER.now}</div><div style="font-size:16px">${OFFER.code}</div></div>`,
});

/* S07 — Latte cutout hero with labelled parts */
{
  const x0 = 290, y0 = 330, w = 500, [W, H] = SIZES['cut/latte-bench.png'], h = w * H / W;
  const at = (fx, fy) => [x0 + fx * w, y0 + fy * h];
  const tags = [[0.33, 0.17, 'Leather collar', 700, 380], [0.38, 0.28, 'D-ring', 80, 470], [0.5, 0.585, 'Front zip pocket', 60, 760], [0.65, 0.78, 'Embroidered crest', 740, 1110]];
  add({
    id: 's07-nylon-bag-who-latte', stage: 'TOFU', format: 'Hero + labels',
    css: `body{background:radial-gradient(ellipse at 50% 55%,#fbf5ec 0%,#efe1cc 55%,#e2cdb0 100%)}`,
    html: `
      <div class="mega abs" style="left:0;right:0;top:70px;text-align:center;font-size:100px;color:#3a2a20">Nylon bag who?</div>
      <div class="abs" style="left:0;right:0;top:200px;display:flex;justify-content:center"><span style="background:#9b6b3e;color:#fff;border-radius:999px;padding:12px 34px;font-family:Montserrat;font-weight:800;font-size:32px">COVR’s got your racket.</span></div>
      ${cut('latte-bench', x0, y0, w, 0)}
      <svg class="fill" width="1080" height="1350" style="position:absolute">${tags.map(([fx, fy, , tx, ty]) => { const [x, y] = at(fx, fy); return `<line x1="${x}" y1="${y}" x2="${tx + 110}" y2="${ty + 24}" stroke="#6b4a2e" stroke-width="2"/><circle cx="${x}" cy="${y}" r="7" fill="#fff" stroke="#6b4a2e" stroke-width="3"/>`; }).join('')}</svg>
      ${tags.map(([, , t, tx, ty]) => `<div class="abs" style="left:${tx}px;top:${ty}px;background:#fffdf8;border:1.5px solid #e2d3bd;border-radius:10px;padding:10px 18px;font-weight:600;font-size:23px;color:#3a2a20;box-shadow:0 6px 16px rgba(0,0,0,.08)">${t}</div>`).join('')}
      <div class="abs kicker" style="left:0;right:0;bottom:50px;text-align:center;font-size:18px;color:#6b4a2e">Latte · ${OFFER.pct} off with ${OFFER.code}</div>`,
  });
}

/* S08 — Offer-first with the Latte cutout */
add({
  id: 's08-offer-first-latte', stage: 'BOFU', format: 'Offer-first',
  css: `body{background:#2f4a3a;color:#fff}`,
  html: `
    <div class="abs kicker" style="left:0;right:0;top:70px;text-align:center;font-size:22px">Premium protection. Now</div>
    <div class="abs mega" style="left:0;right:0;top:110px;text-align:center;font-size:300px;line-height:.9;letter-spacing:-.05em;color:#f3ede3">${OFFER.pct}</div>
    <div class="abs mega" style="left:0;right:0;top:380px;text-align:center;font-size:130px;color:#d9a970">OFF</div>
    ${cut('latte-bench', 330, 500, 420, -12, '0 40px 50px rgba(0,0,0,.5)')}
    <div class="abs" style="left:0;right:0;bottom:60px;display:flex;justify-content:center;gap:20px;align-items:center">
      <span style="border:3px dashed #fff;border-radius:14px;padding:14px 32px;font-family:Montserrat;font-weight:800;font-size:36px;letter-spacing:.1em">${OFFER.code}</span>
      <span style="font-size:26px">${OFFER.when}</span></div>`,
});

module.exports = ads;

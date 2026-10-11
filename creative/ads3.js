// COVR master-prompt campaign: 10 ads, each rendered at 1080x1350 (4:5) and 1080x1920 (9:16).
// render(H, headlineOverride?) -> html. Story safe zones: keep text out of the top ~230px and bottom ~330px.
const { crop, frame, circle, X, V, ARROW, logo } = require('./ads.js').helpers;

const safe = H => (H === 1920 ? { top: 240, bottom: 340 } : { top: 72, bottom: 72 });
const cta = (t, style = '') => `<span class="btn" style="${style}">${t} ${ARROW}</span>`;
const lines = (arr, cls, size, colors = []) => arr.map((l, i) => `<div class="${cls}" style="font-size:${size}px;${colors[i] ? `color:${colors[i]}` : ''}">${l}</div>`).join('');
const icon = (d, z = 64) => `<svg width="${z}" height="${z}" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
const campaign = [];
const add = c => campaign.push({ outDir: 'campaign', size: [1080, 1350], ...c });

/* AD 01 — TOFU · Investment protection · loss aversion */
add({
  id: 'ad01-investment', stage: 'TOFU', format: 'Investment protection',
  hooks: [['A $300 RACKET.', 'A $20 PLAN TO PROTECT IT?'], ['WOULD YOU CARRY A $300 WATCH', 'LOOSE IN YOUR BAG?']],
  render: (H, hl = ['YOUR RACKET COSTS $300.', 'HOW ARE YOU PROTECTING IT?']) => {
    const s = safe(H), ph = H === 1920 ? 980 : 690, py = H - ph;
    return `
      <div class="abs" style="left:64px;right:64px;top:${s.top}px">
        ${lines(hl, 'mega', 70, [null, 'var(--tan)'])}
        <div class="body" style="margin-top:26px;font-size:30px;color:#4a4540">Premium equipment deserves thoughtful protection.</div>
      </div>
      ${frame('IMG_0583.JPG', 0.5, 0.6, 1.0, 0, py, 1080, ph).html}
      <div class="abs" style="left:610px;top:${py + 60}px;transform:rotate(9deg);transform-origin:left top">
        <svg width="2" height="80" style="display:block;margin-left:52px"><line x1="1" y1="0" x2="1" y2="80" stroke="#161412" stroke-width="2"/></svg>
        <div style="background:var(--paper);border-radius:10px 40px 40px 10px;padding:18px 40px 18px 30px;box-shadow:0 12px 30px rgba(0,0,0,.25);font-family:Montserrat;font-weight:900;font-size:58px">$300<div style="font-family:Inter;font-weight:500;font-size:16px;letter-spacing:.18em;color:var(--stone)">YOUR RACKET*</div></div>
      </div>
      <div class="abs" style="left:64px;bottom:${s.bottom}px">${cta('Discover COVR')}</div>
      <div class="abs" style="right:64px;bottom:${s.bottom - 40}px;font-size:16px;color:rgba(255,255,255,.85)">*Illustrative price. Rackets vary.</div>`;
  },
});

/* AD 02 — TOFU · Curiosity gap */
{
  const risks = [
    ['Accidental knocks', '<path d="M24 8v8M24 32v8M8 24h8M32 24h8M13 13l5 5M30 30l5 5M35 13l-5 5M18 30l-5 5"/>'],
    ['Rough surfaces', '<path d="M4 32l6-8 6 8 6-8 6 8 6-8 6 8 4-5"/><path d="M4 40h40"/>'],
    ['Unprotected transport', '<path d="M6 30l4-10h22l8 10v8H6z"/><circle cx="14" cy="38" r="4"/><circle cx="34" cy="38" r="4"/>'],
    ['Improper storage', '<rect x="8" y="14" width="32" height="26" rx="2"/><path d="M8 22h32M20 30h8"/>'],
  ];
  add({
    id: 'ad02-curiosity-enemy', stage: 'TOFU', format: 'Curiosity hook',
    render: (H, hl = ['YOUR RACKET HAS', 'ONE ENEMY YOU', 'KEEP IGNORING.']) => {
      const s = safe(H), cy = H === 1920 ? 1010 : 760, d = H === 1920 ? 400 : 340;
      const pos = [[-1, -1], [1, -1], [-1, 1], [1, 1]];
      return `
        <style>body{background:#1c1714;color:var(--paper)}</style>
        <div class="abs" style="left:64px;right:64px;top:${s.top}px">${lines(hl, 'mega', 92, [null, null, 'var(--tan-light)'])}</div>
        <div class="abs" style="left:${540 - d / 2}px;top:${cy - d / 2}px;width:${d}px;height:${d}px;border-radius:50%;border:2px dashed rgba(196,154,108,.5);padding:26px">
          <div style="position:relative;width:100%;height:100%;border-radius:50%;overflow:hidden">${crop('crest-duo-closeup.jpg', 0.5, 0.64, 1.7, d - 52, d - 52).img}</div></div>
        ${risks.map(([t, svg], i) => {
          const [sx, sy] = pos[i];
          const x = sx < 0 ? 60 : 1080 - 60 - 260, y = cy + sy * (d / 2 + 20) - (sy < 0 ? 130 : -10);
          return `<div class="abs" style="left:${x}px;top:${y}px;width:260px;${sx > 0 ? 'text-align:right' : ''};color:var(--tan-light)">
            ${icon(svg, 86)}<div style="font-family:Montserrat;font-weight:700;font-size:29px;color:var(--paper);margin-top:6px">${t}</div></div>`;
        }).join('')}
        <div class="abs" style="left:64px;right:64px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:center;gap:30px">
          <div class="serif" style="font-size:44px;line-height:1.05"><em>It’s not always what happens on the court.</em></div>
          ${cta('See why', 'background:var(--paper);color:var(--ink);flex:none')}</div>`;
    },
  });
}

/* AD 03 — TOFU · Emotional / identity, sports-campaign look */
add({
  id: 'ad03-take-care', stage: 'TOFU', format: 'Lifestyle campaign',
  render: (H, hl = ['YOU TAKE CARE', 'OF YOUR GAME.', 'WHAT ABOUT', 'YOUR RACKET?']) => {
    const s = safe(H);
    return `
      ${frame('latte-walking-court.jpg', 0.42, 0.55, 1.0, 0, 0, 1080, H).html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(12,10,8,.72) 0%,rgba(12,10,8,.15) ${H === 1920 ? 50 : 45}%,transparent 60%,rgba(12,10,8,.55) 100%)"></div>
      <div class="abs" style="left:64px;top:${s.top}px;color:#fff">${lines(hl, 'mega', 94, [null, null, 'var(--tan-light)', 'var(--tan-light)'])}</div>
      <div class="abs" style="left:64px;right:64px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:flex-end;color:#fff">
        <div style="font-size:28px;max-width:520px;line-height:1.35">Take care of the equipment behind every match.</div>
        ${cta('Meet COVR', 'background:var(--paper);color:var(--ink)')}</div>`;
  },
});

/* AD 04 — MOFU · Split-screen comparison */
add({
  id: 'ad04-premium-cover', stage: 'MOFU', format: 'Split-screen comparison',
  hooks: [['WOULD YOU PUT A $300 RACKET', 'IN A $20 BAG?'], ['SAME RACKET.', 'VERY DIFFERENT COVER.']],
  render: (H, hl = ['YOUR RACKET IS PREMIUM.', 'IS YOUR COVER?']) => {
    const s = safe(H), top = s.top + 230, bottomPad = s.bottom + 110, ih = H - top - bottomPad - 380;
    const col = (x, bg, fg, title, pts, mark, media) => `
      <div class="abs" style="left:${x}px;top:${top}px;width:540px;bottom:${bottomPad}px;background:${bg};color:${fg};padding:36px 40px">
        <div class="kicker" style="font-size:17px;opacity:.75">${title}</div>
        <div style="height:${ih}px;margin:24px 0 30px;position:relative;border-radius:18px;overflow:hidden">${media}</div>
        ${pts.map(t => `<div class="pt" style="display:flex;gap:16px;align-items:center;font-size:25px;margin-bottom:14px">${mark}${t}</div>`).join('')}
      </div>`;
    const ordinary = `<div style="position:absolute;inset:0;background:#cfc9c0;display:flex;align-items:center;justify-content:center">
        <svg width="${Math.min(300, ih * 0.62)}" viewBox="0 0 200 280"><rect x="84" y="4" width="32" height="60" rx="8" fill="#2c2c2e"/><path d="M100 50 C 170 50 190 100 190 150 C 190 220 150 270 100 270 C 50 270 10 220 10 150 C 10 100 30 50 100 50 Z" fill="#2c2c2e"/><path d="M100 50 C 170 50 190 100 190 150" stroke="#444" stroke-width="3" fill="none"/></svg>
        <div style="position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:16px;color:#5b5752">Illustration</div></div>`;
    return `
      <style>.pt .mark{width:42px;height:42px}.pt .mark svg{width:18px;height:18px}</style>
      <div class="abs" style="left:64px;right:64px;top:${s.top}px">${lines(hl, 'mega', 76, [null, 'var(--tan)'])}</div>
      ${col(0, '#e4ded4', '#3d3934', 'An ordinary cover', ['Often thin nylon', 'Plain design', 'Often no pocket', 'Handle zipped in'], X, ordinary)}
      ${col(540, 'var(--ink)', 'var(--paper)', 'COVR', ['Cotton & leather', 'Metal hardware', 'Front zip pocket', 'Open-back handle'], V, crop('latte-unboxing-hands.jpg', 0.42, 0.42, 1.35, 540 - 80, ih).img)}
      <div class="abs" style="left:0;right:0;bottom:${s.bottom}px;display:flex;justify-content:center">${cta('See the difference')}</div>`;
  },
});

/* AD 05 — MOFU · Craftsmanship detail collage */
add({
  id: 'ad05-details', stage: 'MOFU', format: 'Detail collage',
  render: (H, hl = 'The difference is <em class="tan">in the details.</em>') => {
    const s = safe(H), gy = s.top + 250, gh = H - gy - s.bottom - 140, tw = 470, th = (gh - 20) / 2;
    const tiles = [
      ['01', 'Leather collar & rivets', 'latte-unboxing-hands.jpg', 0.15, 0.22, 3.4],
      ['02', 'Signature printed lining', 'web-lining-closeup.png', 0.62, 0.55, 1.15],
      ['03', 'Metal hardware & zips', 'mocha-zip-bench.jpg', 0.56, 0.31, 3.6],
      ['04', 'Cotton with embroidered crest', 'crest-duo-closeup.jpg', 0.33, 0.36, 1.9],
    ];
    return `
      <style>body{background:var(--paper)}</style>
      <div class="serif abs" style="left:64px;right:64px;top:${s.top}px;font-size:100px;line-height:.98;text-align:center">${hl}</div>
      ${tiles.map(([n, t, img, cx, cy, z], i) => {
        const x = 60 + (i % 2) * (tw + 20), y = gy + Math.floor(i / 2) * (th + 20);
        return `${frame(img, cx, cy, z, x, y, tw, th, 'border-radius:4px').html}
          <div class="abs" style="left:${x + 22}px;top:${y + th - 70}px;display:flex;gap:14px;align-items:baseline;background:rgba(250,247,242,.94);padding:10px 20px;border-radius:999px">
            <span style="font-family:Montserrat;font-weight:800;color:var(--tan);font-size:20px">${n}</span><span style="font-weight:600;font-size:21px">${t}</span></div>`;
      }).join('')}
      <div class="abs" style="left:64px;right:64px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:center">
        <div class="serif" style="font-size:36px"><em>Thoughtful craftsmanship. Every detail matters.</em></div>${cta('Explore', 'flex:none')}</div>`;
  },
});

/* AD 06 — MOFU · Open-back handle / airflow */
add({
  id: 'ad06-grip-breathe', stage: 'MOFU', format: 'Feature spotlight',
  hooks: [['WHY IS YOUR GRIP', 'ZIPPED IN AFTER', 'EVERY MATCH?'], ['LET YOUR GRIP', 'BREATHE', 'AFTER PLAY.']],
  render: (H, hl = ['YOUR RACKET', 'GRIP NEEDS', 'TO BREATHE.']) => {
    const s = safe(H);
    const f = frame('mocha-zip-bench.jpg', 0.68, 0.24, 1.75, 0, 0, 1080, H);
    const [gx, gy] = f.at(0.80, 0.20);
    const wave = (dx, dy, o) => `<path d="M${gx + dx} ${gy + dy} c 40 -30 0 -80 40 -110 s 0 -80 40 -110" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="${o}"/>`;
    return `
      ${f.html}
      <div class="fill" style="background:linear-gradient(90deg,rgba(18,14,10,.82) 0%,rgba(18,14,10,.45) 48%,transparent 70%)"></div>
      <svg class="fill" width="1080" height="${H}" style="position:absolute">${wave(0, 60, .55)}${wave(70, 40, .85)}${wave(140, 60, .55)}</svg>
      <div class="abs" style="left:64px;top:${H === 1920 ? 640 : 420}px;color:#fff;width:600px">
        ${lines(hl, 'mega', 88, [null, null, 'var(--tan-light)'])}
        <div style="font-size:29px;line-height:1.4;margin-top:28px;max-width:470px">An open-back design allows airflow around your grip after play.</div>
      </div>
      <div class="abs" style="left:64px;bottom:${s.bottom}px">${cta('Discover the design', 'background:var(--paper);color:var(--ink)')}</div>`;
  },
});

/* AD 07 — MOFU · Value justification, three pillars */
add({
  id: 'ad07-more-than-a-cover', stage: 'MOFU', format: 'Product hero + pillars',
  render: (H, hl = 'More than just <em style="color:var(--tan-light)">a racket cover.</em>') => {
    const s = safe(H), ah = H === 1920 ? 700 : 560, ay = s.top + 230;
    const pillars = [
      ['Protection', 'Designed for everyday storage and transport.', '<path d="M24 6l15 6v11c0 10-7 17-15 19C16 40 9 33 9 23V12z"/>'],
      ['Craftsmanship', 'Cotton, leather details and metal hardware.', '<path d="M8 40L32 16M28 12l8 8M14 28l6 6"/><circle cx="36" cy="10" r="3"/>'],
      ['Functionality', 'Zip pocket, strap, handle and open-back design.', '<rect x="8" y="12" width="32" height="26" rx="3"/><path d="M8 20h32M20 12V8h8v4"/>'],
    ];
    return `
      <style>body{background:#3a2a20;color:var(--paper)}</style>
      <div class="serif abs" style="left:64px;right:64px;top:${s.top}px;font-size:96px;line-height:.98;text-align:center">${hl}</div>
      ${frame('latte-unboxing-hands.jpg', 0.5, 0.48, 1.25, 230, ay, 620, ah, 'border-radius:310px 310px 18px 18px').html}
      <div class="abs" style="left:56px;right:56px;top:${ay + ah + 50}px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px;text-align:center">
        ${pillars.map(([t, d, svg]) => `<div><div style="color:var(--tan-light)">${icon(svg)}</div>
          <div class="kicker" style="font-size:19px;margin:12px 0 10px">${t}</div><div style="font-size:22px;line-height:1.38;opacity:.85">${d}</div></div>`).join('')}
      </div>
      <div class="abs" style="left:0;right:0;bottom:${s.bottom}px;display:flex;justify-content:center">${cta('Experience COVR', 'background:var(--paper);color:var(--ink)')}</div>`;
  },
});

/* AD 08 — BOFU · Premium unboxing */
add({
  id: 'ad08-unboxing-experience', stage: 'BOFU', format: 'Unboxing',
  render: (H, hl = 'Not just a cover.<br><em>An experience.</em>') => {
    const s = safe(H);
    return `
      ${frame('IMG_8776.jpg', 0.47, 0.55, 1.0, 0, 0, 1080, H).html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(14,10,8,.78) 0%,rgba(14,10,8,.25) 34%,transparent 52%,transparent 72%,rgba(14,10,8,.6) 100%)"></div>
      <div class="serif abs" style="left:64px;top:${s.top}px;color:#fff;font-size:108px;line-height:.95">${hl}</div>
      <div class="abs" style="left:64px;right:64px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:flex-end;color:#fff">
        <div><div class="kicker" style="font-size:18px">Thoughtfully designed.</div><div class="kicker" style="font-size:18px;margin-top:8px">Beautifully presented.</div></div>
        ${cta('Explore COVR', 'background:var(--paper);color:var(--ink)')}</div>`;
  },
});

/* AD 09 — BOFU · Ownership / desire, framed print */
add({
  id: 'ad09-essential-waiting', stage: 'BOFU', format: 'Framed product',
  render: (H, hl = ['YOUR NEXT PADEL', 'ESSENTIAL IS WAITING.']) => {
    const s = safe(H), fh = H === 1920 ? 1000 : 700;
    return `
      <style>body{background:var(--cream)}</style>
      ${frame('latte-thankyou-card.jpg', 0.5, 0.5, 1.0, 60, s.top, 960, fh, 'border:14px solid #fff;box-shadow:0 30px 60px rgba(60,40,20,.22)').html}
      <div class="abs" style="left:64px;right:64px;top:${s.top + fh + 50}px">
        ${lines(hl, 'mega', 70, [null, 'var(--tan)'])}
        <div style="font-size:28px;color:#4a4540;margin-top:20px">Protect your racket. Elevate your everyday carry.</div></div>
      <div class="abs" style="left:64px;right:64px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:center">
        <div><div class="kicker" style="font-size:17px;color:var(--stone)">Latte · from</div><div style="font-family:Montserrat;font-weight:900;font-size:54px">$199</div></div>
        ${cta('Shop COVR')}</div>`;
  },
});

/* AD 10 — BOFU · Drop / scarcity. ONLY run with a genuine limited drop. */
add({
  id: 'ad10-next-drop', stage: 'BOFU', format: 'Limited drop',
  render: (H, hl = ['THE NEXT DROP', 'WON’T WAIT FOREVER.']) => {
    const s = safe(H);
    return `
      ${frame('IMG_8754.jpg', 0.5, 0.55, 1.0, 0, 0, 1080, H).html}
      <div class="fill" style="background:linear-gradient(180deg,transparent 35%,rgba(10,8,6,.86) 78%)"></div>
      <div class="abs" style="left:64px;right:64px;bottom:${s.bottom + 130}px;color:#fff">
        <div class="mega" style="font-size:96px">${hl[0]}</div>
        <div class="mega" style="font-size:96px;display:inline;background:var(--tan);color:var(--paper);box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0 14px;line-height:1.08">${hl[1]}</div>
        <div style="font-size:28px;margin-top:30px;opacity:.9">Discover the latest COVR collection.</div></div>
      <div class="abs" style="left:64px;bottom:${s.bottom}px">${cta('Shop the collection', 'background:var(--paper);color:var(--ink)')}</div>
      ${logo(`right:64px;top:${s.top}px;color:#fff`)}`;
  },
});

module.exports = campaign;

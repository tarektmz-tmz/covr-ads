// "Why leave your racket uncovered?" — studio packshot cutouts + drawn phone/racket. 2x.
const { OFFER } = require('./ads6.js');
const { ARROW, X, V } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');
const cut = (n, x, y, h, rot = 0, sh = '0 30px 40px rgba(40,25,10,.3)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  return `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;height:${h}px;width:${h * W / H}px;transform:rotate(${rot}deg);filter:drop-shadow(${sh})">`;
};
const phone = (x, y, h) => `<div class="abs" style="left:${x}px;top:${y}px;width:${h * .49}px;height:${h}px;border-radius:${h * .12}px;background:linear-gradient(135deg,#b88a5c,#8a5a32);padding:${h * .028}px;box-shadow:0 20px 30px rgba(40,25,10,.25)">
  <div style="width:100%;height:100%;border-radius:${h * .1}px;background:linear-gradient(160deg,#3a3532,#151311 60%,#2a2623);position:relative"><div style="position:absolute;left:35%;top:3%;width:30%;height:3.5%;border-radius:20px;background:#000"></div></div></div>`;
// Drawn padel racket. worn=true adds scratches, chips and a dirty grip.
const racket = (x, y, h, worn) => {
  const holes = Array.from({ length: 21 }, (_, i) => { const r = Math.floor(i / 5), c = i % 5; return `<circle cx="${28 + c * 18.5}" cy="${42 + r * 19}" r="5.5" fill="#4a4540"/>`; }).join('');
  const dmg = worn ? `<path d="M22 40 L48 70 M70 30 L95 62 M30 100 L60 92 M88 95 L104 120" stroke="#c9c1b4" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M110 50 l8 4 l-6 8 z M14 110 l-8 2 l4 10z" fill="#f6f1e9"/><rect x="51" y="160" width="28" height="100" rx="9" fill="#8f8577"/>
    <path d="M53 180 l24 8 M53 205 l24 -6 M53 232 l24 10" stroke="#5b544b" stroke-width="3"/>` : `<rect x="51" y="160" width="28" height="100" rx="9" fill="#efe9de"/>`;
  return `<svg class="abs" style="left:${x}px;top:${y}px" width="${h * .5}" height="${h}" viewBox="0 0 130 260"><ellipse cx="65" cy="85" rx="60" ry="78" fill="#26231f"/>${holes}<path d="M45 158 L65 168 L85 158 L80 166 L50 166z" fill="#26231f"/>${dmg}</svg>`;
};
const btn = (t, s = '') => `<span class="btn" style="${s}">${t} ${ARROW}</span>`;
const price = (c = '#161412') => `<span style="font-size:27px;color:${c}"><s style="opacity:.55">${OFFER.was}</s> <b style="color:#b5452e;font-family:Montserrat;font-weight:900;font-size:38px">${OFFER.now}</b> · ${OFFER.code}</span>`;
const ads = [];
const add = a => ads.push({ outDir: 'uncovered', scale: 2, stage: 'TOFU', ...a });

/* U1 — Equation, three rows */
add({
  id: 'u1-equation', format: 'Equation',
  css: `body{background:#f6f1e9}.row{position:absolute;left:56px;right:56px;height:290px;border-radius:28px;display:flex;align-items:center;padding:0 40px;gap:28px;background:#fff;box-shadow:0 12px 30px rgba(0,0,0,.05)}
        .op{font-family:Montserrat;font-weight:900;font-size:66px;color:#9b6b3e}.lbl{font-family:Montserrat;font-weight:800;font-size:33px;line-height:1.15}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:50px;text-align:center"><div class="mega" style="font-size:66px">Why leave your racket</div><div class="mega tan" style="font-size:66px">uncovered?</div></div>
    <div class="row" style="top:240px"><div style="position:relative;width:130px;height:250px">${phone(5, 5, 240)}</div><span class="op">+</span>
      <div class="lbl" style="flex:1">a case</div><span class="op">=</span><div class="lbl" style="color:#2f7a4a">protected ${V}</div></div>
    <div class="row" style="top:560px"><div style="position:relative;width:130px;height:260px">${racket(0, 0, 260, true)}</div><span class="op">+</span>
      <div class="lbl" style="flex:1">nothing<div style="font-family:Inter;font-weight:500;font-size:22px;color:#6f6a62;margin-top:6px">car boot · loose keys · rough benches</div></div><span class="op">=</span><div class="lbl" style="color:#b5452e">scratched ${X}</div></div>
    <div class="row" style="top:880px;background:#1f2a40;color:#fff"><div style="position:relative;width:130px;height:260px">${cut('pack-navy', 0, 40, 178, 0, '0 10px 20px rgba(0,0,0,.4)')}</div><span class="op" style="color:#e3c08f">+</span>
      <div class="lbl" style="flex:1">a COVR<div style="font-family:Inter;font-weight:500;font-size:22px;opacity:.8;margin-top:6px">cotton & leather · waterproof lining</div></div><span class="op" style="color:#e3c08f">=</span><div class="lbl" style="color:#9be0b0">protected ${V}</div></div>
    <div class="abs" style="left:0;right:0;bottom:44px;display:flex;justify-content:center;align-items:center;gap:26px">${price()}${btn('Cover yours')}</div>`,
});

/* U2 — Uncovered vs covered, labelled */
{
  const lab = (x, y, t, good) => `<div class="abs" style="left:${x}px;top:${y}px;display:flex;gap:10px;align-items:center;background:#fff;border-radius:999px;padding:8px 18px 8px 8px;font-weight:600;font-size:21px;box-shadow:0 6px 16px rgba(0,0,0,.1)">${good ? V : X}${t}</div>`;
  add({
    id: 'u2-uncovered-vs-covered', format: 'Split comparison',
    css: `body{background:linear-gradient(90deg,#e4ddd2 50%,#f6f1e9 50%)}.u2 .mark{width:38px;height:38px}.u2 .mark svg{width:18px;height:18px}`,
    html: `<div class="u2">
      <div class="abs" style="left:56px;right:56px;top:50px;text-align:center"><div class="mega" style="font-size:64px">Why leave your racket</div><div class="mega tan" style="font-size:64px">uncovered?</div></div>
      <div class="abs kicker" style="left:0;width:540px;top:250px;text-align:center;font-size:20px;color:#6f6a62">Uncovered</div>
      <div class="abs kicker" style="left:540px;width:540px;top:250px;text-align:center;font-size:20px;color:#9b6b3e">Covered</div>
      ${racket(150, 320, 520, true)}
      ${lab(40, 400, 'Scratched face', false)}${lab(250, 600, 'Chipped frame', false)}${lab(60, 780, 'Worn, dirty grip', false)}
      ${cut('pack-latte', 650, 320, 560)}
      ${lab(560, 520, 'Cotton & leather', true)}${lab(780, 700, 'Waterproof lining', true)}${lab(600, 860, 'Front zip pocket', true)}
      <div class="abs" style="left:56px;right:56px;top:950px;text-align:center;font-size:30px;line-height:1.45;color:#3d3934">Car boots, loose keys and rough benches do the damage <b>between</b> matches. A COVR keeps it off.</div>
      <div class="abs" style="left:0;right:0;bottom:50px;display:flex;justify-content:center;align-items:center;gap:26px">${price()}${btn('Cover yours')}</div></div>`,
  });
}

/* U3 — Colour lineup (in-stock colours only) */
add({
  id: 'u3-lineup', format: 'Colour lineup',
  css: `body{background:radial-gradient(ellipse at 50% 60%,#fbf6ee 0%,#ece1d0 70%)}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:56px;text-align:center"><div class="mega" style="font-size:70px">Stop leaving your</div><div class="mega tan" style="font-size:70px">racket uncovered.</div>
      <div style="font-size:30px;color:#4a4540;margin-top:16px">Car boots. Loose keys. Rough benches. Pick its cover.</div></div>
    ${cut('pack-ash', 70, 500, 470, -8)}${cut('pack-coffee', 670, 500, 470, 8)}
    ${cut('pack-navy', 230, 400, 600, -3)}${cut('pack-latte', 470, 420, 600, 4)}
    <div class="abs" style="left:0;right:0;top:1060px;display:flex;justify-content:center;gap:40px;font-family:Montserrat;font-weight:800;font-size:24px;color:#6b4a2e;letter-spacing:.06em">${['ASH', 'NAVY', 'LATTE', 'COFFEE'].map(t => `<span>${t}</span>`).join('<span style="opacity:.4">·</span>')}</div>
    <div class="abs" style="left:0;right:0;bottom:56px;display:flex;justify-content:center;align-items:center;gap:26px">${price()}${btn('Pick yours')}</div>`,
});
module.exports = ads;

// "You wouldn't leave your phone unprotected" — 3 fuller versions, clean Latte cutout, 2x.
const { OFFER } = require('./ads6.js');
const { frame, ARROW, X, V } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');
const cut = (n, x, y, h, rot = 0, shadow = '0 30px 40px rgba(40,25,10,.3)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  return `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;height:${h}px;width:${h * W / H}px;transform:rotate(${rot}deg);filter:drop-shadow(${shadow})">`;
};
const phone = (x, y, h, rot = 0) => `<div class="abs" style="left:${x}px;top:${y}px;width:${h * .49}px;height:${h}px;border-radius:${h * .12}px;background:linear-gradient(135deg,#b88a5c,#8a5a32);padding:${h * .028}px;transform:rotate(${rot}deg);box-shadow:0 30px 40px rgba(40,25,10,.3)">
  <div style="width:100%;height:100%;border-radius:${h * .1}px;background:linear-gradient(160deg,#3a3532,#151311 60%,#2a2623);position:relative;overflow:hidden">
    <div style="position:absolute;left:35%;top:3%;width:30%;height:3.5%;border-radius:20px;background:#000"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(115deg,transparent 45%,rgba(255,255,255,.08) 50%,transparent 56%)"></div></div></div>`;
const btn = (t, s = '') => `<span class="btn" style="${s}">${t} ${ARROW}</span>`;
const chips = (c = '#3a2a20', bg = '#fff') => `<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">${['Cotton & leather', 'Waterproof lining', 'Front zip pocket', 'Open-back handle'].map(t => `<span style="background:${bg};color:${c};border-radius:999px;padding:10px 20px;font-size:22px;font-weight:600;box-shadow:0 4px 12px rgba(0,0,0,.06)">${t}</span>`).join('')}</div>`;
const ads = [];
const add = a => ads.push({ outDir: 'phone', scale: 2, stage: 'TOFU', ...a });

/* V1 — Side-by-side cards, with the "why" spelled out under each */
add({
  id: 'ph1-two-cards', format: 'Analogy cards',
  css: `body{background:#efe9df}.card{position:absolute;top:370px;width:465px;height:690px;border-radius:30px;background:#fff;box-shadow:0 20px 50px rgba(0,0,0,.08);overflow:hidden}
        .cap{position:absolute;left:0;right:0;bottom:30px;text-align:center}.cap b{display:block;font-family:Montserrat;font-weight:800;font-size:34px}.cap span{font-size:22px;color:#6f6a62}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:56px"><div class="mega" style="font-size:72px">You wouldn’t leave</div><div class="mega" style="font-size:72px">your phone <span class="tan">unprotected.</span></div>
      <div style="font-family:Montserrat;font-weight:800;font-size:44px;color:#b5452e;margin-top:18px">So why leave your racket uncovered?</div></div>
    <div class="card" style="left:56px">${phone(151, 140, 330)}
      <div class="cap"><b>Phone: in a case</b><span>Screen protector too. Obviously.</span></div></div>
    <div class="card" style="left:559px">
      ${cut('latte-arch', (465 - 400 * SIZES['cut/latte-arch.png'][0] / SIZES['cut/latte-arch.png'][1]) / 2, 105, 400)}
      <div class="cap"><b>Racket: in a COVR</b><span>Cotton, leather, waterproof lining.</span></div></div>
    <div class="abs" style="left:56px;right:56px;top:1080px">${chips()}</div>
    <div class="abs" style="left:0;right:0;bottom:54px;display:flex;justify-content:center;align-items:center;gap:28px">
      <span style="font-size:28px">Now <s style="color:#8c857c">${OFFER.was}</s> <b style="color:#b5452e;font-family:Montserrat;font-weight:900;font-size:40px">${OFFER.now}</b> · ${OFFER.code}</span>${btn('Protect yours')}</div>`,
});

/* V2 — Equation: phone + case = protected; racket + ??? → racket + COVR */
add({
  id: 'ph2-equation', format: 'Equation',
  css: `body{background:#f6f1e9}.row{position:absolute;left:56px;right:56px;height:300px;border-radius:28px;display:flex;align-items:center;padding:0 40px;gap:30px}
        .op{font-family:Montserrat;font-weight:900;font-size:70px;color:#9b6b3e}.lbl{font-family:Montserrat;font-weight:800;font-size:34px}`,
  html: `
    <div class="abs" style="left:56px;right:56px;top:50px;text-align:center"><div class="mega" style="font-size:62px">You protect your phone.</div><div class="mega tan" style="font-size:62px">Why not your racket?</div></div>
    <div class="row" style="top:250px;background:#fff">
      <div style="position:relative;width:130px;height:250px">${phone(0, 0, 250)}</div><span class="op">+</span>
      <div class="lbl" style="flex:1">a case</div><span class="op">=</span><div class="lbl" style="color:#2f7a4a">protected ${V}</div></div>
    <div class="row" style="top:580px;background:#fff">
      <div style="position:relative;width:130px;height:250px"><svg width="130" height="250" viewBox="0 0 130 250"><ellipse cx="65" cy="80" rx="58" ry="74" fill="#26231f"/>${Array.from({ length: 16 }, (_, i) => `<circle cx="${33 + (i % 4) * 21}" cy="${48 + Math.floor(i / 4) * 21}" r="5" fill="#57524b"/>`).join('')}<rect x="54" y="150" width="22" height="95" rx="8" fill="#e8e1d5"/></svg></div><span class="op">+</span>
      <div class="lbl" style="flex:1">the car boot,<br>loose keys,<br>rough benches</div><span class="op">=</span><div class="lbl" style="color:#b5452e">scuffed ${X}</div></div>
    <div class="row" style="top:910px;background:#2a1f18;color:#fff">
      <div style="position:relative;width:130px;height:250px">${cut('latte-bench', 0, 0, 250, 0, '0 10px 20px rgba(0,0,0,.4)')}</div><span class="op" style="color:#e3c08f">=</span>
      <div style="flex:1"><div class="lbl">COVR</div><div style="font-size:22px;opacity:.8;margin-top:6px">Cotton & leather · waterproof lining · front zip pocket</div></div></div>
    <div class="abs" style="left:0;right:0;bottom:44px;display:flex;justify-content:center;align-items:center;gap:26px">
      <span style="font-size:27px"><s style="color:#8c857c">${OFFER.was}</s> <b style="color:#b5452e;font-family:Montserrat;font-weight:900;font-size:38px">${OFFER.now}</b> · ${OFFER.code}</span>${btn('Protect yours')}</div>`,
});

/* V3 — Soft-fade photo (the style you liked) + checklist card */
add({
  id: 'ph3-photo-checklist', format: 'Soft fade + checklist',
  html: `
    ${frame('latte-bench-clean.jpg', 0.55, 0.6, 1.0, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(36,26,20,.94) 0%,rgba(36,26,20,.86) 26%,rgba(36,26,20,.4) 42%,rgba(36,26,20,0) 58%)"></div>
    <div class="abs" style="left:64px;right:64px;top:60px;color:#fff">
      <div class="mega" style="font-size:68px">You wouldn’t leave</div><div class="mega" style="font-size:68px">your phone <span style="color:#f0d2a8">unprotected.</span></div>
      <div style="font-size:30px;line-height:1.4;margin-top:18px;color:rgba(255,255,255,.85);max-width:820px">So why does your racket ride loose in the car boot?</div></div>
    <div class="abs" style="left:56px;top:760px;width:500px;background:rgba(250,247,242,.96);border-radius:24px;padding:26px 30px;box-shadow:0 20px 40px rgba(0,0,0,.3)">
      <div class="kicker" style="font-size:16px;color:#9b6b3e;margin-bottom:10px">Your phone gets</div>
      ${['A case', 'A screen protector'].map(t => `<div style="display:flex;gap:12px;align-items:center;font-size:26px;margin:8px 0"><b style="color:#2f7a4a">✓</b>${t}</div>`).join('')}
      <div class="kicker" style="font-size:16px;color:#9b6b3e;margin:18px 0 10px">Your racket gets</div>
      ${['Loose keys, rough benches', 'The car boot'].map(t => `<div style="display:flex;gap:12px;align-items:center;font-size:26px;margin:8px 0;color:#8c857c"><b style="color:#b5452e">✕</b><s>${t}</s></div>`).join('')}
      <div style="display:flex;gap:12px;align-items:center;font-size:28px;margin-top:12px;font-weight:700"><b style="color:#2f7a4a">✓</b>A COVR</div>
    </div>
    <div class="abs" style="left:56px;bottom:56px;background:#161412;color:#fff;border-radius:999px;padding:16px 30px;font-size:24px;font-weight:600">${OFFER.now} with ${OFFER.code} · ${OFFER.when.toLowerCase()}</div>`,
});
module.exports = ads;

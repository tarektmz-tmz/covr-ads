// Square (1:1) versions of the Ceylora infographics for the product gallery.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const kit = __dirname, sp = path.join(kit, '..');
const font = w => 'file://' + path.join(kit, `node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const icon = (name, color, size) => fs.readFileSync(path.join(kit, 'node_modules/lucide-static/icons', name + '.svg'), 'utf8')
  .replace(/<!--[\s\S]*?-->/g, '').replace(/width="24"/, `width="${size}"`).replace(/height="24"/, `height="${size}"`)
  .replace(/stroke="currentColor"/, `stroke="${color}"`).replace(/stroke-width="2"/, 'stroke-width="1.5"');
const bg = f => 'file://' + path.join(sp, 'bg', f);
const BROWN = '#8a4b24', DARK = '#1f1a17', COPPER = '#b8673a';
const DISC = 'These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.';
const base = `
@font-face{font-family:P;font-weight:500;src:url(${font(500)})}
@font-face{font-family:P;font-weight:600;src:url(${font(600)})}
@font-face{font-family:P;font-weight:700;src:url(${font(700)})}
@font-face{font-family:P;font-weight:800;src:url(${font(800)})}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:P,sans-serif;-webkit-font-smoothing:antialiased}
.c{position:relative;overflow:hidden;width:2000px;height:2000px;background-size:cover;background-position:center}
.disc{position:absolute;left:70px;right:70px;bottom:34px;font-size:22px;line-height:1.35;font-weight:500}
`;
const pages = {
  'ceylora-key-benefits-sq': `
<div class="c" style="background-image:url(${bg('woman_sq.jpg')})">
  <div style="position:absolute;left:70px;top:80px;width:880px;border-radius:44px;background:rgba(176,94,52,.94);box-shadow:0 30px 70px rgba(0,0,0,.25);padding:56px 52px 40px">
    <div style="font-size:96px;font-weight:600;color:#fff;text-align:center;line-height:1">Key Benefits</div>
    <div style="height:3px;background:rgba(255,255,255,.55);margin:44px 0 6px"></div>
    ${[['heart-pulse', 'Supports Heart Health'], ['droplet', 'Supports Healthy Glucose Metabolism'], ['brain', 'Supports Focus & Cognitive Health'], ['leaf', 'Natural Antioxidant Support'], ['sun', 'Supports Daily Energy & Vitality']]
      .map(([ic, t], i) => `<div style="display:flex;align-items:center;gap:36px;padding:32px 6px;${i ? 'border-top:3px solid rgba(255,255,255,.45)' : ''}">
      <div style="flex:0 0 112px;display:flex;justify-content:center">${icon(ic, '#fff', 104)}</div>
      <div style="font-size:50px;font-weight:500;color:#fff;line-height:1.18">${t}</div></div>`).join('')}
  </div>
  <div class="disc" style="color:rgba(255,255,255,.95);text-shadow:0 1px 6px rgba(0,0,0,.6)">${DISC}</div>
</div>`,
  'ceylora-inside-formula-sq': `
<div class="c" style="background-image:url(${bg('sticks_sq.jpg')})">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(251,245,236,.95) 0%,rgba(251,245,236,.8) 45%,rgba(251,245,236,0) 78%)"></div>
  <div style="position:absolute;top:110px;width:100%;text-align:center">
    <div style="font-size:42px;font-weight:600;letter-spacing:10px;color:${COPPER}">CEYLORA CEYLON CINNAMON</div>
    <div style="font-size:132px;font-weight:700;color:${DARK};line-height:1.1;margin-top:14px">Inside the Formula</div>
  </div>
  <div style="position:absolute;top:500px;left:200px;right:200px;display:grid;grid-template-columns:1fr 1fr;gap:40px">
    ${[['600 mg', 'Ceylon Cinnamon Extract'], ['12:1', 'Concentrated Extract Ratio'], ['7,200 mg', 'Cinnamon Equivalent'], ['MCT Oil', 'From Coconut, for Better Absorption']]
      .map(([n, t]) => `<div style="background:rgba(255,255,255,.94);border-radius:40px;padding:56px 36px;text-align:center;box-shadow:0 20px 50px rgba(60,30,10,.18)">
      <div style="font-size:120px;font-weight:800;color:${BROWN};line-height:1.05;white-space:nowrap">${n}</div>
      <div style="height:5px;width:90px;background:${COPPER};margin:30px auto"></div>
      <div style="font-size:50px;font-weight:500;color:${DARK};line-height:1.25">${t}</div></div>`).join('')}
  </div>
</div>`,
  'ceylora-daily-routine-sq': `
<div class="c" style="background-image:url(${bg('couple_sq.jpg')})">
  <div style="position:absolute;left:0;right:0;top:0;height:820px;background:linear-gradient(180deg,rgba(251,245,236,.97) 0%,rgba(251,245,236,.93) 72%,rgba(251,245,236,0) 100%)"></div>
  <div style="position:absolute;top:100px;width:100%;text-align:center;font-size:128px;font-weight:700;color:${DARK};line-height:1">Simple Daily Routine</div>
  <div style="position:absolute;top:310px;left:80px;right:80px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px">
    ${[['Take 1 softgel', 'with breakfast'], ['Drink a full', 'glass of water'], ['Stay consistent', 'every day'], ['Feel your best,', 'naturally']]
      .map(([a, b], i) => `<div style="text-align:center">
      <div style="width:140px;height:140px;border-radius:50%;background:${COPPER};color:#fff;font-size:80px;font-weight:700;display:flex;align-items:center;justify-content:center;margin:0 auto 26px">${i + 1}</div>
      <div style="font-size:50px;font-weight:600;color:${BROWN};line-height:1.2">${a}<br>${b}</div></div>`).join('')}
  </div>
  <div class="disc" style="color:rgba(255,255,255,.95);text-shadow:0 1px 6px rgba(0,0,0,.6)">${DISC}</div>
</div>`,
};
(async () => {
  const b = await chromium.launch();
  for (const [name, html] of Object.entries(pages)) {
    const p = await b.newPage({ viewport: { width: 2000, height: 2000 } });
    const tmp = path.join(kit, '_sq.html');
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${html}</body></html>`);
    await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(sp, 'final', name + '.png') }); await p.close(); console.log('rendered', name);
  }
  await b.close();
})();

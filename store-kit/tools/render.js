// Renders Ceylora infographics: background photo + crisp text/icons, via Chromium.
// usage: node render.js <bgdir> <outdir>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [bgdir, outdir] = process.argv.slice(2);
const kit = __dirname;
const font = w => 'file://' + path.join(kit, `node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const icon = (name, color, size) => {
  let svg = fs.readFileSync(path.join(kit, 'node_modules/lucide-static/icons', name + '.svg'), 'utf8');
  svg = svg.replace(/<!--[\s\S]*?-->/g, '')
    .replace(/width="24"/, `width="${size}"`).replace(/height="24"/, `height="${size}"`)
    .replace(/stroke="currentColor"/, `stroke="${color}"`).replace(/stroke-width="2"/, 'stroke-width="1.5"');
  return svg;
};
const bg = f => 'file://' + path.join(bgdir, f);

const BROWN = '#8a4b24', DARK = '#1f1a17', COPPER = '#b8673a', CREAM = '#fbf5ec';
const base = `
@font-face{font-family:P;font-weight:400;src:url(${font(400)})}
@font-face{font-family:P;font-weight:500;src:url(${font(500)})}
@font-face{font-family:P;font-weight:600;src:url(${font(600)})}
@font-face{font-family:P;font-weight:700;src:url(${font(700)})}
@font-face{font-family:P;font-weight:800;src:url(${font(800)})}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:P,sans-serif;-webkit-font-smoothing:antialiased}
.c{position:relative;overflow:hidden;background-size:cover;background-position:center}
.disc{position:absolute;font-size:22px;line-height:1.35;color:rgba(31,26,23,.62);font-weight:400}
`;

const pages = {
  // 1. Take 1 softgel daily (hand + softgels, empty left)
  'ceylora-softgel-daily': { w: 2000, h: 2000, html: `
<div class="c" style="width:2000px;height:2000px;background-image:url(${bg('hand.jpg')})">
  <div style="position:absolute;left:120px;top:150px;width:1300px">
    <div style="font-size:118px;font-weight:700;color:${DARK};line-height:1.05;letter-spacing:-2px">Take 1 Softgel Daily</div>
    <div style="font-size:112px;font-weight:700;color:${COPPER};line-height:1.15;margin-top:14px">Easy to swallow</div>
    <div style="font-size:52px;font-weight:500;color:${COPPER};line-height:1.3;margin-top:22px;width:900px">Smooth, small softgels designed for daily comfort.</div>
  </div>
  <div style="position:absolute;left:110px;top:840px;width:1000px">
    <div style="font-size:360px;font-weight:800;color:${BROWN};line-height:.95;letter-spacing:-8px">12:1</div>
    <div style="font-size:126px;font-weight:500;color:${COPPER};line-height:1.12;margin-top:30px">Ceylon<br>Cinnamon<br>extract</div>
    <div style="font-size:92px;font-weight:500;color:${COPPER};line-height:1.2;margin-top:8px">(7,200 mg eq.)</div>
  </div>
</div>` },

  // 2. Key benefits panel (older woman holding pouch on the right)
  'ceylora-key-benefits-panel': { w: 1600, h: 2000, html: `
<div class="c" style="width:1600px;height:2000px;background-image:url(${bg('woman.jpg')});background-position:right center">
  <div style="position:absolute;left:70px;top:90px;width:820px;border-radius:44px;background:rgba(176,94,52,.94);box-shadow:0 30px 70px rgba(0,0,0,.25);padding:60px 56px 50px">
    <div style="font-size:96px;font-weight:600;color:#fff;text-align:center;line-height:1">Key Benefits</div>
    <div style="height:3px;background:rgba(255,255,255,.55);margin:46px 0 10px"></div>
    ${[
      ['heart-pulse', 'Supports Heart Health'],
      ['droplet', 'Supports Healthy Glucose Metabolism'],
      ['brain', 'Supports Focus & Cognitive Health'],
      ['leaf', 'Natural Antioxidant Support'],
      ['sun', 'Supports Daily Energy & Vitality'],
    ].map(([ic, t], i) => `
    <div style="display:flex;align-items:center;gap:40px;padding:34px 6px;${i ? 'border-top:3px solid rgba(255,255,255,.45)' : ''}">
      <div style="flex:0 0 120px;display:flex;justify-content:center">${icon(ic, '#fff', 112)}</div>
      <div style="font-size:52px;font-weight:500;color:#fff;line-height:1.18">${t}</div>
    </div>`).join('')}
  </div>
  <div class="disc" style="left:70px;bottom:40px;width:1460px;color:rgba(255,255,255,.92);text-shadow:0 1px 6px rgba(0,0,0,.55)">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.</div>
</div>` },

  // 3. Pouch on the right, badges + guarantee seal on the empty left
  'ceylora-pouch-badges': { w: 2000, h: 2000, html: `
<div class="c" style="width:2000px;height:2000px;background-image:url(${bg('pouch.jpg')})">
  <div style="position:absolute;left:90px;top:120px;width:520px;border-radius:40px;border:4px solid ${COPPER};background:rgba(251,245,236,.86);padding:40px 30px">
    ${[
      ['heart-pulse', 'Heart Health<br>Support'],
      ['activity', 'Healthy Glucose<br>Metabolism'],
      ['sun', 'Daily Energy<br>& Vitality'],
      ['droplets', 'With MCT Oil<br>from Coconut'],
    ].map(([ic, t], i) => `
    <div style="text-align:center;padding:34px 0;${i ? `border-top:4px dotted ${COPPER}` : ''}">
      ${icon(ic, BROWN, 120)}
      <div style="font-size:50px;font-weight:600;color:${BROWN};line-height:1.15;margin-top:14px">${t}</div>
    </div>`).join('')}
  </div>
  <div style="position:absolute;left:650px;top:1150px;width:360px;height:360px;border-radius:50%;border:8px solid #c98a2e;background:rgba(251,245,236,.9);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#c98a2e;text-align:center">
    <div style="font-size:32px;font-weight:700;letter-spacing:3px">MONEY BACK</div>
    <div style="font-size:120px;font-weight:800;line-height:1">90</div>
    <div style="font-size:44px;font-weight:700;letter-spacing:6px;line-height:1">DAY</div>
    <div style="font-size:32px;font-weight:700;letter-spacing:3px;margin-top:6px">GUARANTEE</div>
  </div>
  <div class="disc" style="left:90px;bottom:36px;width:1820px">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.</div>
</div>` },

  // 4. Inside the formula (cinnamon sticks both sides, empty centre)
  'ceylora-inside-formula': { w: 2000, h: 1500, html: `
<div class="c" style="width:2000px;height:1500px;background-image:url(${bg('sticks.jpg')})">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(251,245,236,.92) 0%,rgba(251,245,236,.55) 45%,rgba(251,245,236,0) 70%)"></div>
  <div style="position:absolute;top:90px;width:100%;text-align:center">
    <div style="font-size:40px;font-weight:600;letter-spacing:10px;color:${COPPER}">CEYLORA CEYLON CINNAMON</div>
    <div style="font-size:120px;font-weight:700;color:${DARK};line-height:1.1;margin-top:10px">Inside the Formula</div>
  </div>
  <div style="position:absolute;top:470px;left:150px;right:150px;display:grid;grid-template-columns:repeat(4,1fr);gap:36px">
    ${[
      ['600 mg', 'Ceylon Cinnamon Extract'],
      ['12:1', 'Concentrated Extract Ratio'],
      ['7,200 mg', 'Cinnamon Equivalent'],
      ['MCT Oil', 'From Coconut, for Better Absorption'],
    ].map(([n, t]) => `
    <div style="background:rgba(255,255,255,.93);border-radius:36px;padding:54px 30px;text-align:center;box-shadow:0 20px 50px rgba(60,30,10,.18)">
      <div style="font-size:${n.length > 6 ? 82 : 100}px;font-weight:800;color:${BROWN};line-height:1.05;white-space:nowrap">${n}</div>
      <div style="height:4px;width:80px;background:${COPPER};margin:30px auto"></div>
      <div style="font-size:42px;font-weight:500;color:${DARK};line-height:1.25">${t}</div>
    </div>`).join('')}
  </div>
</div>` },

  // 5. Simple daily routine (older couple at breakfast)
  'ceylora-daily-routine': { w: 2000, h: 1500, html: `
<div class="c" style="width:2000px;height:1500px;background-image:url(${bg('couple.jpg')})">
  <div style="position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(180deg,rgba(251,245,236,.97) 0%,rgba(251,245,236,.93) 70%,rgba(251,245,236,0) 100%)"></div>
  <div style="position:absolute;top:70px;width:100%;text-align:center">
    <div style="font-size:112px;font-weight:700;color:${DARK};line-height:1">Simple Daily Routine</div>
  </div>
  <div style="position:absolute;top:240px;left:110px;right:110px;display:grid;grid-template-columns:repeat(4,1fr);gap:30px">
    ${[
      ['Take 1 softgel', 'with breakfast'],
      ['Drink a full', 'glass of water'],
      ['Stay consistent', 'every day'],
      ['Feel your best,', 'naturally'],
    ].map(([a, b], i) => `
    <div style="text-align:center">
      <div style="width:120px;height:120px;border-radius:50%;background:${COPPER};color:#fff;font-size:68px;font-weight:700;display:flex;align-items:center;justify-content:center;margin:0 auto 22px">${i + 1}</div>
      <div style="font-size:46px;font-weight:600;color:${BROWN};line-height:1.2">${a}<br>${b}</div>
    </div>`).join('')}
  </div>
  <div class="disc" style="left:60px;bottom:30px;width:1880px;color:rgba(255,255,255,.92);text-shadow:0 1px 6px rgba(0,0,0,.6)">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.</div>
</div>` },
};

(async () => {
  const browser = await chromium.launch();
  const only = process.argv[4];
  for (const [name, p] of Object.entries(pages)) {
    if (only && name !== only) continue;
    const page = await browser.newPage({ viewport: { width: p.w, height: p.h } });
    const tmp = path.join(kit, '_page.html');
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${p.html}</body></html>`);
    await page.goto('file://' + tmp, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(outdir, name + '.png') });
    await page.close();
    console.log('rendered', name);
  }
  await browser.close();
})();

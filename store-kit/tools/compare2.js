// Ceylora vs Other Brands table (transparent background) and a scalloped 90-day seal.
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const kit = __dirname, sp = path.join(kit, '..');
const font = w => 'file://' + path.join(kit, `node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const icon = (name, color, size, sw = 1.6) => fs.readFileSync(path.join(kit, 'node_modules/lucide-static/icons', name + '.svg'), 'utf8')
  .replace(/<!--[\s\S]*?-->/g, '').replace(/width="24"/, `width="${size}"`).replace(/height="24"/, `height="${size}"`)
  .replace(/stroke="currentColor"/, `stroke="${color}"`).replace(/stroke-width="2"/, `stroke-width="${sw}"`);
const base = `@font-face{font-family:P;font-weight:500;src:url(${font(500)})}@font-face{font-family:P;font-weight:600;src:url(${font(600)})}@font-face{font-family:P;font-weight:700;src:url(${font(700)})}@font-face{font-family:P;font-weight:800;src:url(${font(800)})}
html,body{margin:0;background:transparent;font-family:P,sans-serif;-webkit-font-smoothing:antialiased}`;
const rows = [
  ['leaf', 'True Ceylon Cinnamon', 'Often Cheap Cassia'],
  ['shield-check', 'Naturally Low in Coumarin', 'Cassia Is High in Coumarin'],
  ['badge-check', 'Concentrated 12:1 Extract', 'Weak, Low-Dose Powders'],
  ['droplet', 'MCT Oil Enhanced', 'Dry Powder, No Healthy Fat'],
  ['pill', 'Easy-to-Swallow Softgels', 'Hard-to-Swallow Capsules'],
  ['calendar-check', 'Just 1 Softgel a Day', '2–3 Capsules a Day'],
];
const RH = 170;
const table = `
<div id="t" style="display:flex;gap:28px;padding:150px 10px 10px;width:1100px">
  <div style="flex:1;background:#9a3d14;border-radius:36px;color:#fff;box-shadow:0 24px 60px rgba(60,20,5,.35)">
    <div style="height:230px;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:26px;font-size:54px;font-weight:600">
      <img src="file://${path.join(sp, 'bg/bag.png')}" style="position:absolute;left:50%;top:-150px;transform:translateX(-50%);height:300px;filter:drop-shadow(0 18px 24px rgba(0,0,0,.35))">Ceylora</div>
    ${rows.map(([ic, a]) => `<div style="height:${RH}px;border-top:2px solid rgba(255,255,255,.3);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;font-size:36px;font-weight:600;padding:0 20px">${icon(ic, '#fff', 56)}${a}</div>`).join('')}
  </div>
  <div style="flex:1;background:#fff;border-radius:36px;margin-top:40px;color:#2a2421;box-shadow:0 24px 60px rgba(60,20,5,.25)">
    <div style="height:190px;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:26px;font-size:50px;font-weight:500;color:#5d5551">
      <div style="position:absolute;left:50%;top:-80px;transform:translateX(-50%);width:170px;height:170px;border-radius:50%;background:#f3ede7;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(0,0,0,.12)">${icon('pill-bottle', '#8a817c', 96, 1.4)}</div>Other Brands</div>
    ${rows.map(([, , b]) => `<div style="height:${RH}px;border-top:2px solid #ece4dc;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;text-align:center;font-size:34px;font-weight:500;padding:0 20px"><div style="width:52px;height:52px;border-radius:50%;background:#7b726d;display:flex;align-items:center;justify-content:center">${icon('x', '#fff', 30, 3)}</div>${b}</div>`).join('')}
  </div>
</div>`;
// Scalloped seal: 24-point wavy edge, ring with curved text, white centre.
const pts = [];
for (let i = 0; i < 48; i++) { const a = (i / 48) * Math.PI * 2, r = i % 2 ? 282 : 300; pts.push(`${300 + r * Math.cos(a)},${300 + r * Math.sin(a)}`); }
const seal = `
<svg id="s" width="600" height="600" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
  <polygon points="${pts.join(' ')}" fill="#fff" stroke="#fff" stroke-width="10" stroke-linejoin="round"/>
  <circle cx="300" cy="300" r="262" fill="#b8673a"/>
  <circle cx="300" cy="300" r="248" fill="none" stroke="#fff" stroke-width="5"/>
  <circle cx="300" cy="300" r="140" fill="#fff"/>
  <defs><path id="top" d="M 105 300 A 195 195 0 0 1 495 300"/><path id="bot" d="M 80 300 A 220 220 0 0 0 520 300"/></defs>
  <text font-family="P" font-weight="800" font-size="62" fill="#fff" letter-spacing="4"><textPath href="#top" startOffset="50%" text-anchor="middle">MONEY BACK</textPath></text>
  <text font-family="P" font-weight="800" font-size="62" fill="#fff" letter-spacing="4"><textPath href="#bot" startOffset="50%" text-anchor="middle">GUARANTEE</textPath></text>
  <text x="70" y="318" font-family="P" font-size="44" fill="#fff">★</text><text x="490" y="318" font-family="P" font-size="44" fill="#fff">★</text>
  <text x="300" y="312" text-anchor="middle" font-family="P" font-weight="800" font-size="120" fill="#8a3f17">90</text>
  <text x="300" y="372" text-anchor="middle" font-family="P" font-weight="700" font-size="50" fill="#8a3f17" letter-spacing="4">DAYS</text>
</svg>`;
(async () => {
  const b = await chromium.launch();
  for (const [name, html, sel, w, h] of [['ceylora-vs-other-brands', table, '#t', 1140, 1500], ['ceylora-90-day-badge', seal, '#s', 600, 600]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    const tmp = path.join(kit, '_c2.html');
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${html}</body></html>`);
    await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready);
    await p.locator(sel).screenshot({ path: path.join(sp, 'final', name + '.png'), omitBackground: true }); await p.close();
  }
  await b.close(); console.log('ok');
})();

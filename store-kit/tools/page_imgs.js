// Renders two images for the "Why Ceylon" page: Cassia vs Ceylon, and the 90-day guarantee with the bag.
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const kit = __dirname, sp = path.join(kit, '..');
const font = w => 'file://' + path.join(kit, `node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const f = p => 'file://' + path.join(sp, p);
const base = `@font-face{font-family:P;font-weight:500;src:url(${font(500)})}@font-face{font-family:P;font-weight:600;src:url(${font(600)})}@font-face{font-family:P;font-weight:700;src:url(${font(700)})}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:P,sans-serif;-webkit-font-smoothing:antialiased}`;
const pages = {
  'ceylora-cassia-vs-ceylon': { w: 2000, h: 1500, html: `
<div style="position:relative;width:2000px;height:1500px;background:url(${f('bg/raw_sticks.jpg')}) center/cover">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(251,245,236,.95) 0%,rgba(251,245,236,.8) 35%,rgba(251,245,236,0) 50%)"></div>
  <div style="position:absolute;top:80px;width:100%;text-align:center;font-size:110px;font-weight:700;color:#1f1a17">Cassia vs. Ceylon</div>
  <div style="position:absolute;top:240px;width:100%;text-align:center;font-size:44px;font-weight:500;color:#8a4b24">Not all cinnamon is the same</div>
  ${[['left:120px', 'CASSIA', ['Thick, hard single layer', 'Much higher in coumarin', 'Common in cheap supplements'], '#6f655f', '&#10007;'],
     ['right:120px', 'CEYLON', ['Thin, soft, many layers', 'Naturally low in coumarin', 'The cinnamon in Ceylora'], '#b8673a', '&#10003;']]
    .map(([pos, t, items, c, mark]) => `
  <div style="position:absolute;${pos};top:340px;width:700px;background:rgba(255,255,255,.94);border-radius:36px;padding:36px 46px;box-shadow:0 20px 50px rgba(60,30,10,.2)">
    <div style="font-size:64px;font-weight:700;color:${c};letter-spacing:6px">${t}</div>
    ${items.map(i => `<div style="font-size:42px;font-weight:500;color:#2a2421;margin-top:18px"><span style="color:${c};font-weight:700">${mark}</span>&nbsp; ${i}</div>`).join('')}
  </div>`).join('')}
</div>` },
  'ceylora-guarantee-bags': { w: 2000, h: 1500, html: `
<div style="position:relative;width:2000px;height:1500px;background:linear-gradient(180deg,#fbf6f0,#ecdfd1)">
  <div style="position:absolute;left:140px;top:0;bottom:0;width:700px;display:flex;flex-direction:column;justify-content:center">
    <img src="${f('final/ceylora-90-day-badge.png')}" style="width:300px;height:300px">
    <div style="font-size:120px;font-weight:700;color:#1f1a17;line-height:1.05;margin-top:40px">Try It for<br>90 Days</div>
    <div style="font-size:48px;font-weight:500;color:#8a4b24;line-height:1.35;margin-top:30px">Not for you? Contact us within 90 days for a full refund.</div>
  </div>
  <img src="${f('final/ceylora-bundle-3.jpg')}" style="position:absolute;right:100px;top:250px;width:1000px;height:1000px;object-fit:cover;border-radius:40px;box-shadow:0 30px 70px rgba(60,30,10,.18)">
</div>` },
};
(async () => {
  const b = await chromium.launch();
  for (const [name, p] of Object.entries(pages)) {
    const page = await b.newPage({ viewport: { width: p.w, height: p.h } });
    const tmp = path.join(kit, '_pi.html');
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${base}</style></head><body>${p.html}</body></html>`);
    await page.goto('file://' + tmp); await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(sp, 'final', name + '.png') }); await page.close();
  }
  await b.close(); console.log('ok');
})();

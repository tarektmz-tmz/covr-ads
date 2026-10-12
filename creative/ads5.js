// Round 4: formats modelled on the winning ads the user collected (ad-library screenshots).
// Product cutouts (media/cut/*.png) are the real photos with the background removed. Nothing is redrawn.
const { crop, frame, ARROW } = require('./ads.js').helpers;
const SIZES = require('./media-sizes.json');

const cut = (n, x, y, w, rot = 0, shadow = '0 40px 50px rgba(40,25,10,.35)') => {
  const [W, H] = SIZES[`cut/${n}.png`];
  const h = w * H / W;
  return {
    html: `<img src="../../media/cut/${n}.png" style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;transform:rotate(${rot}deg);filter:drop-shadow(${shadow})">`,
    at: (fx, fy) => [x + fx * w, y + fy * h], // valid when rot = 0
    h,
  };
};
const ball = (x, y, d, rot = 0) => `<div class="abs" style="left:${x}px;top:${y}px;width:${d}px;height:${d}px;border-radius:50%;transform:rotate(${rot}deg);
  background:radial-gradient(circle at 34% 30%,#f6ff9a 0,#d8ec3c 38%,#a9c21c 78%,#86a010 100%);box-shadow:0 ${d * .18}px ${d * .3}px rgba(0,0,0,.25);overflow:hidden">
  <svg viewBox="0 0 100 100" style="position:absolute;inset:0"><path d="M-5 30 C 30 45 30 55 -5 70 M105 30 C 70 45 70 55 105 70" fill="none" stroke="#fff" stroke-width="5" opacity=".9"/></svg></div>`;
const check = c => `<span style="width:46px;height:46px;border-radius:50%;background:${c};display:inline-flex;align-items:center;justify-content:center;flex:none"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>`;
const ads = [];
const add = a => ads.push({ outDir: 'inspired', ...a });

/* I1 — "Skin booster who?" → "Nylon bag who?" : soft glow, product hero, price burst, part labels */
{
  const p = cut('coffee', 120, 470, 840);
  const tags = [[0.80, 0.22, 'Leather collar', 760, 380], [0.37, 0.30, 'Front zip pocket', 120, 380], [0.27, 0.66, 'Embroidered crest', 90, 1100]];
  add({
    id: 'i01-nylon-bag-who', stage: 'TOFU', format: 'Soft hero + price burst',
    css: `body{background:radial-gradient(ellipse at 50% 55%,#fbf5ec 0%,#efe1cc 55%,#e2cdb0 100%)}`,
    html: `
      <div class="logo abs" style="left:0;right:0;top:60px;text-align:center;font-size:34px;color:#6b4a2e">COVR</div>
      <div class="mega abs" style="left:0;right:0;top:130px;text-align:center;font-size:100px;white-space:nowrap;color:#3a2a20">Nylon bag who?</div>
      <div class="abs" style="left:0;right:0;top:268px;display:flex;justify-content:center"><span style="background:#9b6b3e;color:#fff;border-radius:999px;padding:14px 38px;font-family:Montserrat;font-weight:800;font-size:36px">COVR’s got your racket.</span></div>
      ${p.html}
      <svg class="fill" width="1080" height="1350" style="position:absolute">${tags.map(([fx, fy, , tx, ty]) => { const [x, y] = p.at(fx, fy); return `<line x1="${x}" y1="${y}" x2="${tx + 100}" y2="${ty + 24}" stroke="#6b4a2e" stroke-width="2"/><circle cx="${x}" cy="${y}" r="7" fill="#fff" stroke="#6b4a2e" stroke-width="3"/>`; }).join('')}</svg>
      ${tags.map(([, , t, tx, ty]) => `<div class="abs" style="left:${tx}px;top:${ty}px;background:#fffdf8;border:1.5px solid #e2d3bd;border-radius:10px;padding:10px 18px;font-weight:600;font-size:23px;color:#3a2a20;box-shadow:0 6px 16px rgba(0,0,0,.08)">${t}</div>`).join('')}
      <div class="abs" style="right:70px;top:1060px;width:200px;height:200px;background:#c4532f;clip-path:polygon(50% 0,61% 13%,77% 7%,79% 24%,95% 27%,89% 42%,100% 55%,86% 64%,90% 81%,73% 81%,65% 96%,50% 87%,35% 96%,27% 81%,10% 81%,14% 64%,0 55%,11% 42%,5% 27%,21% 24%,23% 7%,39% 13%);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;transform:rotate(8deg)">
        <div style="font-size:17px;letter-spacing:.18em;font-weight:600">HANDMADE</div><div style="font-family:Montserrat;font-weight:900;font-size:54px;line-height:1">$249</div></div>
      <div class="abs kicker" style="left:0;right:0;bottom:56px;text-align:center;font-size:18px;color:#6b4a2e">Coffee · Padel racket cover</div>`,
  });
}

/* I2 — Minimal "No mask. No hose." → kicker + condensed headline + floating product + timeline footnote */
{
  const p = cut('coffee', 150, 560, 780, -8, '0 60px 40px rgba(0,0,0,.28)');
  add({
    id: 'i02-gets-better', stage: 'MOFU', format: 'Minimal product + kicker',
    css: `body{background:linear-gradient(180deg,#e9e7e3 0%,#d6d3cd 100%)}`,
    html: `
      <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:24px;letter-spacing:.16em;font-weight:500;color:#26231f">COTTON. LEATHER. METAL HARDWARE.</div>
      <div class="abs" style="left:40px;right:40px;top:165px;text-align:center;font-family:Oswald;font-weight:700;font-size:112px;line-height:1.02;color:#1d1b18;text-transform:uppercase">It gets better<br>the more you play.</div>
      ${p.html}
      <div class="abs" style="left:300px;top:1135px;width:480px;height:40px;border-radius:50%;background:radial-gradient(rgba(0,0,0,.25),transparent 70%)"></div>
      <div class="abs" style="left:0;right:0;bottom:70px;text-align:center;font-size:24px;font-style:italic;color:#3d3a35;line-height:1.5">Match 1: crisp canvas. Match 50: softer in the hand.<br>Match 200: the leather has deepened. It’s yours.</div>`,
  });
}

/* I3 — Tier list (opinion, played for laughs) */
{
  const rows = [
    ['S', '#9b6b3e', 'COVR', 'Cotton, leather, open-back handle, waterproof lining.', true],
    ['A', '#b48659', 'A padded sports bag', 'Fine. Your racket shares it with your shoes.'],
    ['B', '#c9a77f', 'The free cover that came with it', 'Thin nylon. Did its best.'],
    ['C', '#d8c3a5', 'A supermarket bag', 'We’ve all seen it.'],
    ['D', '#e5d8c5', 'Naked in the car boot', 'Every pothole. Every set of keys.'],
  ];
  add({
    id: 'i03-tier-list', stage: 'TOFU', format: 'Tier list',
    css: `body{background:var(--paper)}`,
    html: `
      <div class="abs" style="left:56px;top:60px"><div class="mega" style="font-size:84px">Padel racket cover</div><div class="mega tan" style="font-size:84px">tier list.</div></div>
      <div class="abs" style="left:56px;right:56px;top:280px">
        ${rows.map(([t, c, h, d, hero]) => `
          <div style="display:flex;gap:14px;margin-bottom:14px;height:${hero ? 250 : 170}px">
            <div style="width:150px;background:${c};display:flex;align-items:center;justify-content:center;font-family:Montserrat;font-weight:900;font-size:80px;color:${hero ? '#fff' : '#3a2a20'}">${t}</div>
            <div style="flex:1;background:${hero ? '#2a1f18' : '#efe8dd'};color:${hero ? '#fff' : '#26231f'};display:flex;align-items:center;gap:26px;padding:0 30px;position:relative;overflow:hidden">
              ${hero ? `<div style="width:300px;flex:none;position:relative;height:250px">${cut('coffee', -10, 40, 320, -10, '0 14px 20px rgba(0,0,0,.4)').html}</div>` : ''}
              <div><div style="font-family:Montserrat;font-weight:800;font-size:${hero ? 48 : 34}px">${h}</div><div style="font-size:${hero ? 24 : 23}px;opacity:.75;margin-top:6px">${d}</div></div>
            </div></div>`).join('')}
      </div>
      <div class="abs" style="left:56px;bottom:40px;font-size:20px;color:var(--stone)">Our opinion, obviously. · padelcovr.com</div>`,
  });
}

/* I4 — Feature checklist + product (Sentinelle) */
{
  const items = ['Cotton canvas body', 'Genuine leather trim', 'Metal hardware', 'Waterproof, wipe-clean lining', 'Front zip pocket', 'Adjustable strap & carry handle', 'Open-back handle'];
  add({
    id: 'i04-checklist', stage: 'MOFU', format: 'Feature checklist',
    css: `body{background:linear-gradient(160deg,#f1efeb 0%,#dedad3 100%)}`,
    html: `
      <div class="abs" style="left:64px;top:80px;width:620px;font-family:Montserrat;font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-.02em">The racket cover that <span class="tan">does more.</span></div>
      <div class="abs" style="left:64px;top:420px">
        ${items.map(t => `<div style="display:flex;gap:22px;align-items:center;margin-bottom:30px;font-size:32px;font-weight:500">${check('#9b6b3e')}${t}</div>`).join('')}
      </div>
      ${cut('mocha', 520, 560, 820, -72).html}
      <div class="logo abs" style="left:64px;bottom:64px;font-size:40px">COVR</div>`,
  });
}

/* I5 — Pedestal still life (Pelsbarn) */
add({
  id: 'i05-pedestal', stage: 'MOFU', format: 'Styled still life',
  css: `body{background:linear-gradient(180deg,#e8dccb 0%,#d9c7ae 100%)}`,
  html: `
    <div class="fill" style="background:repeating-linear-gradient(118deg,rgba(255,255,255,.0) 0 70px,rgba(255,250,240,.22) 70px 120px);mix-blend-mode:screen"></div>
    <div class="serif abs" style="left:40px;right:40px;top:80px;text-align:center;font-size:104px;line-height:.98;color:#3a2a20">A soft place for a<br><em style="color:#8a5a32">hard-working racket.</em></div>
    <div class="abs" style="left:190px;top:1010px;width:700px;height:300px;background:linear-gradient(90deg,#d6c3a6,#efe3d1 45%,#d2bd9e);border-radius:0 0 30px 30px"></div>
    <div class="abs" style="left:190px;top:950px;width:700px;height:120px;border-radius:50%;background:radial-gradient(ellipse at 50% 40%,#fbf4e8,#e8d9c2)"></div>
    ${cut('coffee', 170, 600, 740, -14, '0 30px 30px rgba(60,40,20,.35)').html}
    ${ball(800, 905, 92, 20)}${ball(720, 940, 80, -30)}
    <div class="abs kicker" style="left:0;right:0;bottom:60px;text-align:center;font-size:19px;color:#3a2a20">Cotton twill · Black leather · Waterproof lining · $249</div>`,
});

/* I6 — "Ja, das ist teuer." → "Yes, it's expensive." Price objection head-on */
add({
  id: 'i06-yes-its-expensive', stage: 'BOFU', format: 'Price objection',
  css: `body{background:#f6efe4}`,
  html: `
    <div class="abs mega" style="left:60px;top:60px;font-size:118px;color:#b5452e">Yes, it’s<br>expensive.</div>
    <div class="abs" style="left:64px;top:340px;width:600px;font-size:31px;line-height:1.42;color:#26231f">
      We could make it cheaper. Then it would be nylon instead of cotton canvas, plastic instead of leather, and your grip zipped in instead of an <b>open-back collar</b>.
      <div style="margin-top:28px">${['Cotton canvas, genuine leather, metal hardware', 'Waterproof, wipe-clean lining', 'Front pocket for phone, keys and cards'].map(t => `<div style="display:flex;gap:16px;margin-bottom:16px"><span style="color:#b5452e;font-weight:900">●</span><b style="font-weight:600">${t}</b></div>`).join('')}</div>
      <div style="margin-top:22px">Without them, it wouldn’t be COVR.</div>
    </div>
    ${cut('mocha', 560, 640, 700, -60).html}
    <div class="abs mega" style="left:60px;bottom:64px;font-size:84px;color:#b5452e">That’s why<br>it’s $249.</div>`,
});

/* I7 — Dark "x-ray" glow (Peakflex) */
add({
  id: 'i07-car-boots-are-hard', stage: 'TOFU', format: 'Dark dramatic',
  css: `body{background:radial-gradient(ellipse at 50% 42%,#4a3322 0%,#1d1612 45%,#0d0b09 100%)}`,
  html: `
    <div class="abs" style="left:240px;top:220px;width:600px;height:600px;border-radius:50%;background:radial-gradient(rgba(214,160,100,.55),transparent 65%);filter:blur(10px)"></div>
    ${cut('coffee', 110, 260, 860, -10, '0 0 60px rgba(214,160,100,.55)').html}
    <div class="abs" style="left:40px;right:40px;bottom:90px;text-align:center;font-family:Oswald;font-weight:700;font-size:92px;line-height:1.05;color:#fff;text-transform:uppercase">Car boots are hard on rackets.<br><span style="color:#d9a970">COVR helps take the knocks.</span></div>`,
});

/* I8 — "Sorry, Dyson girls" scarcity. Real stock on 11 Oct 2026: Vanilla Cream = 1. Update before running. */
add({
  id: 'i08-sorry-padel-girls', stage: 'BOFU', format: 'Low stock',
  html: `
    ${frame('IMG_0617.JPG', 0.48, 0.55, 1.15, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(255,252,246,.92) 0%,rgba(255,252,246,.55) 24%,transparent 38%)"></div>
    <div class="abs" style="left:0;right:0;top:70px;text-align:center">
      <div class="mega" style="font-size:80px;color:#b5745a;font-style:italic;letter-spacing:-.02em">Sorry, padel girls</div>
      <div style="font-size:44px;font-weight:600;color:#26231f;margin-top:10px">We’re running out of Vanilla Cream…</div></div>
    <div class="abs" style="left:0;right:0;bottom:70px;display:flex;justify-content:center">
      <span style="background:#fff;border-radius:999px;padding:18px 40px;font-size:30px;color:#26231f;box-shadow:0 10px 30px rgba(0,0,0,.15)">Only <b>1 Vanilla Cream</b> left in stock.</span></div>`,
});

/* I9 — Feature icons around product on a pedestal (Moon Nude) */
{
  const p = cut('mocha', 290, 600, 520, -6, '0 30px 30px rgba(0,0,0,.4)');
  const icon = d => `<div style="width:84px;height:84px;border-radius:50%;border:2px solid rgba(255,255,255,.8);display:flex;align-items:center;justify-content:center;margin:0 auto 12px"><svg width="44" height="44" viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">${d}</svg></div>`;
  const feats = [
    [70, 470, 'Front zip pocket', 'Phone, keys and cards', '<rect x="8" y="10" width="32" height="28" rx="4"/><path d="M14 18h20"/><circle cx="34" cy="18" r="2"/>'],
    [800, 470, 'Open-back handle', 'Lets your grip breathe', '<path d="M18 40V20a6 6 0 0 1 12 0v20"/><path d="M14 10c2-3 4-3 6 0M28 10c2-3 4-3 6 0"/>'],
    [70, 900, 'Waterproof lining', 'Wipe-clean inside', '<path d="M24 6c8 10 12 16 12 22a12 12 0 0 1-24 0c0-6 4-12 12-22z"/>'],
    [800, 900, 'Strap & handle', 'Shoulder or hand', '<path d="M10 38c0-16 6-28 14-28s14 12 14 28"/><rect x="6" y="36" width="36" height="6" rx="2"/>'],
  ];
  add({
    id: 'i09-everything-in-one', stage: 'MOFU', format: 'Icon callouts',
    css: `body{background:#2f4a3a;color:#fff}`,
    html: `
      <svg class="fill" width="1080" height="1350" style="position:absolute;opacity:.18"><rect x="60" y="300" width="960" height="1100" fill="none" stroke="#fff" stroke-width="6"/><line x1="540" y1="300" x2="540" y2="1400" stroke="#fff" stroke-width="6"/><line x1="60" y1="760" x2="1020" y2="760" stroke="#fff" stroke-width="6"/></svg>
      <div class="abs" style="left:0;right:0;top:80px;text-align:center;font-family:Montserrat;font-weight:800;font-size:46px;letter-spacing:.06em;line-height:1.2">EVERYTHING YOUR RACKET NEEDS,<br>IN ONE COVER</div>
      <div class="abs" style="left:0;right:0;top:210px;text-align:center;font-size:24px;opacity:.8">Cotton canvas, leather details and metal hardware.</div>
      <div class="abs" style="left:290px;top:1080px;width:500px;height:110px;border-radius:50%;background:radial-gradient(ellipse at 50% 40%,#f3ede3,#cfc4b2)"></div>
      ${p.html}
      ${ball(330, 1060, 96, 10)}${ball(680, 1080, 84, -20)}
      ${feats.map(([x, y, t, d, svg]) => `<div class="abs" style="left:${x}px;top:${y}px;width:220px;text-align:center">${icon(svg)}<div style="font-weight:700;font-size:24px;letter-spacing:.04em">${t.toUpperCase()}</div><div style="font-size:20px;opacity:.75;margin-top:4px">${d}</div></div>`).join('')}
      <div class="abs kicker" style="left:0;right:0;bottom:56px;text-align:center;font-size:19px">Choose yours · padelcovr.com</div>`,
  });
}

/* I10 — "Highly requested, freshly dropped" → new-colour drop (Coffee arrived Aug 2026) */
add({
  id: 'i10-freshly-dropped', stage: 'BOFU', format: 'New drop',
  css: `body{background:radial-gradient(ellipse at 50% 70%,#f6ece0 0%,#ead8c4 70%)}`,
  html: `
    <div class="abs kicker" style="left:0;right:0;top:90px;text-align:center;font-size:22px;color:#6b4a2e">The Coffee edition</div>
    <div class="serif abs" style="left:0;right:0;top:140px;text-align:center;font-size:128px;line-height:.95;color:#4a2e1e">Freshly<br><em>dropped.</em></div>
    <div class="abs" style="left:0;right:0;top:420px;display:flex;justify-content:center"><span style="border:2px solid #4a2e1e;border-radius:999px;padding:12px 32px;font-size:26px;color:#4a2e1e">Coffee twill · black leather · $249</span></div>
    ${cut('coffee', 120, 560, 840, -6).html}
    ${ball(60, 1150, 120, 15)}${ball(900, 520, 100, -25)}${ball(940, 1180, 76, 40)}
    <div class="abs" style="left:0;right:0;bottom:60px;display:flex;justify-content:center"><span class="btn">Shop the drop ${ARROW}</span></div>`,
});

module.exports = ads;

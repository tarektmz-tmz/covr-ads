// Scene ads: AI-generated scenes (Canva) combined with real COVR photos. 4:5 + 9:16 + hook variations.
// Scenes live in media/gen/. Rackets, cars and extra people are generated; covers in real-photo insets are untouched.
const { crop, frame, ARROW, logo } = require('./ads.js').helpers;

const RED = '#d4342b';
const safe = H => (H === 1920 ? { top: 240, bottom: 340 } : { top: 64, bottom: 64 });
const cta = (t, style = '') => `<span class="btn" style="${style}">${t} ${ARROW}</span>`;
const lines = (arr, cls, size, colors = []) => arr.map((l, i) => `<div class="${cls}" style="font-size:${size}px;${colors[i] ? `color:${colors[i]}` : ''}">${l}</div>`).join('');
const aiTag = (H, s, style = '') => `<div class="abs" style="right:28px;top:${H === 1920 ? s.top - 50 : 20}px;font-size:15px;letter-spacing:.08em;color:rgba(255,255,255,.75);${style}">AI-generated scene</div>`;
const arrow = (x1, y1, x2, y2, bend = .2) => {
  const mx = (x1 + x2) / 2 + (y2 - y1) * bend, my = (y1 + y2) / 2 - (x2 - x1) * bend;
  const a = Math.atan2(y2 - my, x2 - mx), L = 28;
  const h = s => `${x2 - L * Math.cos(a + s)},${y2 - L * Math.sin(a + s)}`;
  return `<path d="M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}" fill="none" stroke="${RED}" stroke-width="7" stroke-linecap="round"/>
          <path d="M${h(-.5)} L${x2} ${y2} L${h(.5)}" fill="none" stroke="${RED}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>`;
};
const realInset = (x, y, w, h, rot, label) => `
  <div class="abs" style="left:${x}px;top:${y}px;width:${w + 28}px;background:#fff;padding:14px 14px 0;transform:rotate(${rot}deg);box-shadow:0 18px 40px rgba(0,0,0,.35)">
    <div style="position:relative;width:${w}px;height:${h}px;overflow:hidden">${crop('latte-unboxing-hands.jpg', 0.5, 0.48, 1.2, w, h).img}</div>
    <div style="font-family:Caveat;font-weight:700;font-size:44px;text-align:center;padding:8px 0 10px;color:var(--ink)">${label}</div></div>`;
const meme = (H, s, text, size = 54) => `<div class="abs" style="left:0;right:0;top:0;padding:${s.top + 20}px 60px 34px;background:#fff;font-family:Inter;font-weight:600;font-size:${size}px;line-height:1.22;color:#111">${text}</div>`;

const scenes = [];
const add = c => scenes.push({ outDir: 'scenes', ...c });

/* S1 — Before/after: damaged vs new racket */
add({
  id: 's1-two-rackets', stage: 'TOFU', format: 'Before & after',
  hooks: [['SAME RACKET.', 'ONE DIFFERENCE.'], ['BEFORE YOU BUY ANOTHER', 'RACKET, LOOK AT THIS.']],
  render: (H, hl = ['6 MONTHS OF PADEL.', 'TWO VERY DIFFERENT RACKETS.']) => {
    const s = safe(H), band = s.top + 230, bh = H === 1920 ? 400 : 230, ih = H - band - bh;
    const f = frame('gen/gen-damaged-vs-new.jpg', 0.5, 0.45, 1.0, 0, band, 1080, ih);
    const [lx, ly] = f.at(0.3, 0.6), [rx, ry] = f.at(0.7, 0.6);
    return `
      <div class="abs" style="left:56px;right:56px;top:${s.top}px">${lines(hl, 'mega', 70, [null, 'var(--tan)'])}</div>
      ${f.html}
      <div class="abs" style="left:${lx - 200}px;top:${ly}px;width:400px;text-align:center;font-family:Caveat;font-weight:700;font-size:56px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)">carried loose</div>
      <div class="abs" style="left:${rx - 200}px;top:${ry}px;width:400px;text-align:center;font-family:Caveat;font-weight:700;font-size:56px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)">carried covered</div>
      ${aiTag(H, s, `top:${band + 18}px`)}
      <div class="abs" style="left:0;right:0;bottom:0;height:${bh}px;background:var(--ink);color:var(--paper);display:flex;align-items:${H === 1920 ? 'flex-start' : 'center'};padding:${H === 1920 ? 50 : 0}px 56px 0;gap:30px">
        <div style="width:130px;height:130px;border-radius:50%;overflow:hidden;position:relative;flex:none;border:4px solid var(--paper)">${crop('latte-unboxing-hands.jpg', 0.74, 0.58, 3.0, 130, 130).img}</div>
        <div style="flex:1"><div class="logo" style="font-size:36px">COVR</div><div style="font-size:23px;opacity:.8;margin-top:8px">Cotton & leather racket covers · $249</div></div>
        ${cta('Protect yours', 'background:var(--paper);color:var(--ink);flex:none')}</div>`;
  },
});

/* S2 — Meme: naked in the car boot */
add({
  id: 's2-car-boot-meme', stage: 'TOFU', format: 'Meme',
  hooks: ['POV: your $400 racket’s daily commute.', 'This is what happens when you throw your racket in the car every day.'],
  render: (H, hl = 'Padel players:<br>• buys a $400 racket<br>• throws it naked in the car boot') => {
    const s = safe(H), mh = s.top + (H === 1920 ? 280 : 250);
    return `
      ${frame('gen/gen-car-boot.jpg', 0.5, 0.5, 1.0, 0, mh, 1080, H - mh).html}
      ${meme(H, s, hl)}
      ${aiTag(H, s, `top:${mh + 16}px`)}
      ${realInset(600, H - s.bottom - 520, 360, 400, 5, 'do this instead')}`;
  },
});

/* S3 — Racket as a passenger (product redrawn by AI: check fidelity before use) */
add({
  id: 's3-first-class', stage: 'MOFU', format: 'Concept photo',
  hooks: ['Treat it like a passenger, <em>not luggage.</em>', 'Buckle up, <em>racket.</em>'],
  render: (H, hl = 'Your racket rides <em>first class.</em>') => {
    const s = safe(H);
    return `
      ${frame('gen/gen-passenger-seat.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, H).html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(18,12,8,.75) 0%,transparent 34%,transparent 70%,rgba(18,12,8,.7) 100%)"></div>
      <div class="serif abs" style="left:60px;right:60px;top:${s.top}px;font-size:104px;line-height:.95;color:#fff">${hl}</div>
      ${aiTag(H, s, `top:auto;bottom:${s.bottom + 120}px`)}
      <div class="abs" style="left:60px;right:60px;bottom:${s.bottom}px;display:flex;justify-content:space-between;align-items:center;color:#fff">
        <div style="font-size:26px;line-height:1.35;max-width:480px">Cotton, leather and a waterproof lining. Every trip, every match.</div>
        ${cta('Shop COVR', 'background:var(--paper);color:var(--ink);flex:none')}</div>`;
  },
});

/* S4 — Meme: someone asks to borrow your racket */
add({
  id: 's4-borrow-meme', stage: 'TOFU', format: 'Meme',
  hooks: ['Mine. Get your own.', 'Me protecting my racket after smashing it against the glass 14 times:'],
  render: (H, hl = 'Padel players when someone asks to borrow their racket:') => {
    const s = safe(H), mh = s.top + (H === 1920 ? 220 : 190);
    return `
      ${frame('gen/gen-borrow-hands.jpg', 0.5, 0.5, 1.0, 0, mh, 1080, H - mh).html}
      ${meme(H, s, hl, 56)}
      ${aiTag(H, s, `top:${mh + 16}px`)}
      <div class="abs" style="left:56px;bottom:${s.bottom}px;background:var(--ink);color:#fff;border-radius:999px;padding:16px 30px;font-weight:600;font-size:24px">COVR · padelcovr.com</div>`;
  },
});

/* S5 — Spot the difference with friends on court */
add({
  id: 's5-spot-the-player', stage: 'MOFU', format: 'Annotated scene',
  hooks: [['YOUR FRIENDS', 'WILL NOTICE.'], ['WHICH ONE WOULD', 'YOU RATHER CARRY?']],
  render: (H, hl = ['SPOT THE PLAYER WHO', 'CARES ABOUT HER RACKET.']) => {
    const s = safe(H);
    const f = frame('gen/gen-friends-court.jpg', 0.5, 0.55, 1.0, 0, 0, 1080, H);
    const [cx, cy] = f.at(0.49, 0.49), [bx, by] = f.at(0.13, 0.5);
    return `
      ${f.html}
      <div class="fill" style="background:linear-gradient(180deg,rgba(12,10,8,.78) 0%,transparent 30%,transparent 75%,rgba(12,10,8,.6) 100%)"></div>
      <div class="abs" style="left:56px;right:56px;top:${s.top}px;color:#fff">${lines(hl, 'mega', 60, [null, 'var(--tan-light)'])}</div>
      <svg class="fill" width="1080" height="${H}" style="position:absolute">
        <ellipse cx="${cx}" cy="${cy}" rx="150" ry="140" fill="none" stroke="${RED}" stroke-width="7" transform="rotate(-10 ${cx} ${cy})"/>
        ${arrow(cx + 220, cy + 300, cx + 90, cy + 140, -.25)}
        ${arrow(bx + 140, by + 330, bx + 40, by + 140, .25)}</svg>
      <div class="abs" style="left:${cx + 120}px;top:${cy + 300}px;font-family:Caveat;font-weight:700;font-size:58px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.7);line-height:.95">her.<br>COVR, $249</div>
      <div class="abs" style="left:${bx + 40}px;top:${by + 340}px;font-family:Caveat;font-weight:700;font-size:50px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.7)">thin nylon bag</div>
      ${aiTag(H, s, `top:auto;bottom:${s.bottom + 100}px`)}
      <div class="abs" style="left:56px;bottom:${s.bottom}px">${cta('See the difference', 'background:var(--paper);color:var(--ink)')}</div>`;
  },
});

module.exports = scenes;

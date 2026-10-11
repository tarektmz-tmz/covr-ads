// Round 7: "favourites" recipe — full-bleed real photo + ONE clever overlay + short headline + small offer.
const { OFFER } = require('./ads6.js');
const { crop, frame, ARROW } = require('./ads.js').helpers;

const priceTag = (x, y, rot = -6) => `<div class="abs" style="left:${x}px;top:${y}px;transform:rotate(${rot}deg);background:#fff;border-radius:12px 60px 60px 12px;padding:16px 46px 16px 30px;box-shadow:0 14px 30px rgba(0,0,0,.3);display:flex;align-items:center;gap:18px">
  <span style="width:18px;height:18px;border-radius:50%;background:#d9cfc1"></span><span style="font-size:30px;color:#8c857c;text-decoration:line-through">${OFFER.was}</span>
  <span style="font-family:Montserrat;font-weight:900;font-size:56px;color:#b5452e">${OFFER.now}</span></div>`;
const topFade = (a = .8, to = 30) => `<div class="fill" style="background:linear-gradient(180deg,rgba(14,10,8,${a}) 0%,transparent ${to}%)"></div>`;
const lightFade = (to = 28) => `<div class="fill" style="background:linear-gradient(180deg,rgba(255,252,246,.92) 0%,rgba(255,252,246,.5) ${to - 10}%,transparent ${to}%)"></div>`;
const serifHead = (a, b, color = '#fff', em = '#e3c08f', size = 96) => `<div class="serif abs" style="left:56px;right:56px;top:56px;font-size:${size}px;line-height:.98;color:${color}">${a}<br><em style="color:${em}">${b}</em></div>`;
const megaHead = (a, b, color = '#fff', em = '#d9a970', size = 80) => `<div class="abs" style="left:0;right:0;top:56px;text-align:center"><div class="mega" style="font-size:${size}px;color:${color}">${a}</div><div class="mega" style="font-size:${size}px;color:${em}">${b}</div></div>`;
const small = (t, color = '#fff') => `<div class="abs kicker" style="left:56px;bottom:60px;color:${color};font-size:18px">${t}</div>`;
const pill = (t, x, y, style = '') => `<div class="abs" style="left:${x}px;top:${y}px;background:#d9a970;color:#161412;border-radius:999px;padding:18px 34px;font-family:Montserrat;font-weight:800;font-size:26px;letter-spacing:.06em;display:flex;gap:12px;align-items:center;${style}">${t} ${ARROW}</div>`;
const ads = [];
const add = a => ads.push({ outDir: 'favs', ...a });

/* R01 — Toggle switches: have both */
{
  const tog = (label, on) => `<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:34px;font-weight:600;${on ? '' : 'color:#9a948b'}">${label}
    <span style="width:96px;height:56px;border-radius:28px;background:${on ? '#2f7a4a' : '#d6d0c6'};position:relative;flex:none"><span style="position:absolute;top:5px;${on ? 'right:5px' : 'left:5px'};width:46px;height:46px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.25)"></span></span></div>`;
  add({
    id: 'r01-toggles-both', stage: 'MOFU', format: 'Toggle card',
    html: `
      ${frame('IMG_0572.JPG', 0.55, 0.5, 1.1, 0, 0, 1080, 1350).html}
      <div class="abs" style="left:56px;top:60px;width:560px;background:#fff;border-radius:28px;padding:30px 36px;box-shadow:0 20px 40px rgba(0,0,0,.18)">
        <div style="font-family:Montserrat;font-weight:800;font-size:40px;line-height:1.08;margin-bottom:12px">Why settle for basic when you can have both?</div>
        ${tog('Protection', true)}${tog('Style', true)}${tog('Basic', false)}
      </div>
      ${priceTag(600, 1140)}`,
  });
}

/* R02 — Loading bar */
add({
  id: 'r02-upgrading', stage: 'BOFU', format: 'Progress bar',
  html: `
    ${frame('latte-unboxing-hands.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 1350).html}
    <div class="abs" style="left:90px;right:90px;top:70px;background:rgba(22,20,18,.88);backdrop-filter:blur(10px);border-radius:28px;padding:34px 40px;color:#fff">
      <div style="display:flex;justify-content:space-between;font-size:32px;font-weight:600"><span>Upgrading your racket…</span><span style="color:#d9a970">80%</span></div>
      <div style="height:22px;border-radius:11px;background:rgba(255,255,255,.18);margin-top:22px;overflow:hidden"><div style="width:80%;height:100%;border-radius:11px;background:linear-gradient(90deg,#c49a6c,#e3c08f)"></div></div>
      <div style="font-size:24px;opacity:.75;margin-top:18px">Finish with code <b style="opacity:1;color:#e3c08f">${OFFER.code}</b> · ${OFFER.pct} off</div>
    </div>
    ${small('Latte · Handmade padel racket cover')}`,
});

/* R03 — Swing tag on the D-ring */
{
  const f = frame('latte-thankyou-card.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 1350);
  const [dx, dy] = f.at(0.64, 0.2);
  add({
    id: 'r03-swing-tag', stage: 'BOFU', format: 'Swing tag',
    html: `
      ${f.html}
      <svg class="fill" width="1080" height="1350" style="position:absolute"><path d="M${dx} ${dy} C ${dx + 120} ${dy + 60} ${dx + 140} ${dy + 160} ${dx + 170} ${dy + 250}" fill="none" stroke="#f3ede3" stroke-width="4"/></svg>
      <div class="abs" style="left:${dx + 70}px;top:${dy + 240}px;width:300px;height:420px;background:#f3ede3;clip-path:polygon(20% 0,80% 0,100% 14%,100% 100%,0 100%,0 14%);transform:rotate(-8deg);box-shadow:0 20px 40px rgba(0,0,0,.4);padding:96px 30px 0;text-align:center;color:#2a1f18">
        <div style="position:absolute;left:132px;top:30px;width:36px;height:36px;border-radius:50%;background:#2a1f18"></div>
        <div class="logo" style="font-size:36px">COVR</div><div class="kicker" style="font-size:14px;margin:12px 0 24px">Latte · Handmade</div>
        <div style="font-size:28px;color:#8c857c;text-decoration:line-through">${OFFER.was}</div>
        <div style="font-family:Montserrat;font-weight:900;font-size:64px;color:#b5452e;line-height:1">${OFFER.now}</div>
        <div style="font-size:18px;margin-top:12px">code ${OFFER.code}</div></div>
      ${serifHead('Your racket has been', 'waiting for this.', '#fff', '#e3c08f', 90)}`,
  });
}

/* R04 — Rubber stamp */
add({
  id: 'r04-stamp', stage: 'BOFU', format: 'Rubber stamp',
  html: `
    ${frame('IMG_8754.jpg', 0.5, 0.55, 1.0, 0, 0, 1080, 1350).html}
    ${topFade(.82, 34)}
    ${serifHead('Premium craftsmanship.', 'A price worth celebrating.')}
    <div class="abs" style="left:560px;top:820px;width:400px;height:400px;border-radius:50%;border:12px solid #d4342b;color:#d4342b;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-14deg);opacity:.92;
      -webkit-mask:repeating-radial-gradient(circle at 30% 40%,#000 0 3px,rgba(0,0,0,.75) 3px 5px)">
      <div style="position:absolute;inset:14px;border-radius:50%;border:4px solid #d4342b"></div>
      <div style="font-family:Oswald;font-weight:700;font-size:40px;letter-spacing:.2em">COVR</div>
      <div style="font-family:Oswald;font-weight:700;font-size:150px;line-height:1">${OFFER.pct}</div>
      <div style="font-family:Oswald;font-weight:700;font-size:56px;letter-spacing:.15em">OFF</div></div>
    ${small(`Code ${OFFER.code} · ${OFFER.when}`)}`,
});

/* R05 — One message exchange */
add({
  id: 'r05-friends-will-ask', stage: 'TOFU', format: 'Message bubbles',
  css: `.b{position:absolute;max-width:640px;padding:22px 32px;border-radius:40px;font-size:36px;line-height:1.25;box-shadow:0 10px 30px rgba(0,0,0,.25)}`,
  html: `
    ${frame('latte-walking-court.jpg', 0.42, 0.55, 1.03, 0, 0, 1080, 1350).html}
    ${topFade(.75, 30)}
    ${megaHead('Your friends', 'will ask.')}
    <div class="b" style="left:56px;top:330px;background:#e9e9eb;color:#000;border-bottom-left-radius:10px">wait… is that your racket cover??</div>
    <div class="b" style="right:56px;top:470px;background:#0b84ff;color:#fff;border-bottom-right-radius:10px">yep. COVR. ${OFFER.pct} off this week</div>
    ${small('Latte · Cotton canvas & leather')}`,
});

/* R06 — Tape measure */
{
  const f = frame('IMG_0583.JPG', 0.5, 0.6, 1.0, 0, 0, 1080, 1350);
  const [, top] = f.at(0.5, 0.44), [, bot] = f.at(0.5, 0.78);
  const ticks = Array.from({ length: 40 }, (_, i) => `<line x1="0" y1="${(i / 39) * (bot - top)}" x2="${i % 5 ? 18 : 34}" y2="${(i / 39) * (bot - top)}" stroke="#2a2420" stroke-width="3"/>${i % 5 ? '' : `<text x="40" y="${(i / 39) * (bot - top) + 8}" font-size="22" font-family="Inter" font-weight="600" fill="#2a2420">${i}</text>`}`).join('');
  add({
    id: 'r06-tape-measure', stage: 'MOFU', format: 'Tape measure',
    html: `
      ${f.html}
      ${topFade(.85, 28)}
      <div class="abs" style="left:0;right:0;top:56px;text-align:center"><div class="mega" style="font-size:70px;color:#fff">Your racket has found</div><div class="mega" style="font-size:70px;color:#e3c08f">its perfect match.</div></div>
      <div class="abs" style="left:900px;top:${top}px;width:100px;height:${bot - top}px;background:#f2c94c;box-shadow:0 10px 24px rgba(0,0,0,.3);transform:rotate(3deg)"><svg width="100" height="${bot - top}">${ticks}</svg></div>
      <div class="abs" style="left:700px;top:${(top + bot) / 2 - 50}px;background:#161412;color:#fff;border-radius:16px;padding:14px 22px;font-family:Montserrat;font-weight:800;font-size:40px">39 cm</div>
      <div class="abs" style="left:56px;bottom:60px;background:#fff;border-radius:999px;padding:16px 30px;font-size:26px;box-shadow:0 10px 24px rgba(0,0,0,.2)">Fits most standard padel rackets · <b style="color:#b5452e">${OFFER.pct} off</b></div>`,
  });
}

/* R07 — Two price tags: racket vs protection (Mocha photo — restock first) */
{
  const f = frame('mocha-strap-studio.jpg', 0.5, 0.5, 1.03, 0, 0, 1080, 1350);
  const tag = (x, y, rot, label, price, red) => `<div class="abs" style="left:${x}px;top:${y}px;transform:rotate(${rot}deg);background:#fff;border-radius:12px 50px 50px 12px;padding:14px 40px 14px 26px;box-shadow:0 14px 30px rgba(0,0,0,.3)"><div class="kicker" style="font-size:15px;color:#8c857c">${label}</div><div style="font-family:Montserrat;font-weight:900;font-size:50px;color:${red ? '#b5452e' : '#161412'}">${price}</div></div>`;
  add({
    id: 'r07-two-tags', stage: 'TOFU', format: 'Two price tags',
    html: `
      ${f.html}
      ${lightFade(26)}
      ${serifHead('Protect what', 'you paid for.', '#2a1f18', '#8a5a32', 104)}
      ${tag(780, 520, 8, 'Your racket*', '$300', false)}
      ${tag(110, 900, -6, 'Its protection', OFFER.now, true)}
      <div class="abs" style="right:56px;bottom:50px;font-size:17px;color:#fff;opacity:.9">*Illustrative price · code ${OFFER.code}</div>`,
  });
}

/* R08 — What's in the box */
add({
  id: 'r08-whats-in-the-box', stage: 'BOFU', format: 'Box contents card',
  html: `
    ${frame('IMG_8776.jpg', 0.47, 0.55, 1.0, 0, 0, 1080, 1350).html}
    ${topFade(.8, 30)}
    ${serifHead('Not just a cover.', 'An unboxing.')}
    <div class="abs" style="left:56px;bottom:60px;width:480px;background:rgba(250,247,242,.95);border-radius:24px;padding:28px 32px;box-shadow:0 20px 40px rgba(0,0,0,.3)">
      <div class="kicker" style="font-size:17px;color:#9b6b3e;margin-bottom:12px">What’s in the box</div>
      ${['Your COVR racket cover', 'Adjustable shoulder strap', 'COVR dust bag', 'Gift box'].map(t => `<div style="display:flex;gap:14px;align-items:center;font-size:28px;margin:10px 0"><span style="color:#2f7a4a;font-weight:800">✓</span>${t}</div>`).join('')}
      <div style="border-top:1.5px solid #e2d8c8;margin-top:16px;padding-top:14px;font-size:24px">${OFFER.pct} off · <b>${OFFER.code}</b></div></div>`,
});

/* R09 — Add to cart + cursor */
add({
  id: 'r09-add-to-cart', stage: 'BOFU', format: 'Button + cursor',
  html: `
    ${frame('crest-duo-closeup.jpg', 0.45, 0.5, 1.03, 0, 0, 1080, 1350).html}
    ${topFade(.75, 30)}
    ${megaHead('One click away', 'from your new favourite.', '#fff', '#e3c08f', 74)}
    <div class="abs" style="left:150px;top:1020px;width:780px;background:#161412;color:#fff;border-radius:999px;padding:36px;text-align:center;font-family:Montserrat;font-weight:800;font-size:38px;letter-spacing:.06em;box-shadow:0 20px 40px rgba(0,0,0,.45)">ADD TO CART · <span style="color:#e3c08f">${OFFER.now}</span></div>
    <svg class="abs" style="left:700px;top:1080px" width="110" height="130" viewBox="0 0 24 28"><path d="M3 1 L3 21 L8 16 L11.5 24 L14.5 22.8 L11 15 L18 15 Z" fill="#fff" stroke="#000" stroke-width="1.4" stroke-linejoin="round"/></svg>
    ${small(`Code ${OFFER.code} · ${OFFER.when}`)}`,
});

/* R10 — Location check-in sticker */
add({
  id: 'r10-better-entrance', stage: 'BOFU', format: 'Location sticker',
  html: `
    ${frame('IMG_0580.JPG', 0.55, 0.45, 1.05, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(255,252,246,.97) 0%,rgba(255,252,246,.9) 16%,transparent 32%)"></div>
    <div class="abs" style="left:0;right:0;top:56px;text-align:center"><div class="mega" style="font-size:66px;color:#161412">Your next match deserves</div><div class="mega" style="font-size:66px;color:#9b6b3e">a better entrance.</div></div>
    <div class="abs" style="left:80px;top:760px;background:#fff;border-radius:22px;padding:18px 30px;display:flex;gap:16px;align-items:center;box-shadow:0 14px 30px rgba(0,0,0,.25);transform:rotate(-4deg)">
      <svg width="40" height="48" viewBox="0 0 24 30"><path d="M12 1C6 1 2 5.5 2 11c0 7 10 18 10 18s10-11 10-18C22 5.5 18 1 12 1z" fill="#b5452e"/><circle cx="12" cy="11" r="4" fill="#fff"/></svg>
      <span style="font-family:Montserrat;font-weight:800;font-size:34px;background:linear-gradient(90deg,#b5452e,#9b6b3e);-webkit-background-clip:text;color:transparent">COURT 3 · 7PM</span></div>
    ${pill(`${OFFER.pct} OFF · ${OFFER.code}`, 56, 1220)}`,
});

/* R11 — Countdown sticker + real last-one stock (Vanilla Cream = 1 on 11 Oct 2026) */
add({
  id: 'r11-countdown-sticker', stage: 'BOFU', format: 'Countdown sticker',
  html: `
    ${frame('IMG_0617.JPG', 0.48, 0.55, 1.12, 0, 0, 1080, 1350).html}
    ${lightFade(26)}
    <div class="abs" style="left:0;right:0;top:56px;text-align:center"><div class="mega" style="font-size:64px;color:#161412">Don’t wait until your</div><div class="mega" style="font-size:64px;color:#9b6b3e">favourite colour is gone.</div></div>
    <div class="abs" style="left:240px;top:1010px;width:600px;border-radius:30px;overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.3);transform:rotate(-3deg)">
      <div style="background:linear-gradient(90deg,#9b6b3e,#c49a6c);color:#fff;text-align:center;padding:14px;font-weight:700;font-size:24px;letter-spacing:.12em">${OFFER.code} ENDS IN</div>
      <div style="background:#fff;display:flex;justify-content:center;gap:22px;padding:18px 0 22px">${[['23', 'HRS'], ['59', 'MIN'], ['41', 'SEC']].map(([n, l]) => `<div style="text-align:center"><div style="font-family:Oswald;font-weight:700;font-size:76px;line-height:1">${n}</div><div style="font-size:16px;letter-spacing:.2em;color:#8c857c">${l}</div></div>`).join('<div style="font-family:Oswald;font-size:70px">:</div>')}</div></div>
    <div class="abs" style="left:0;right:0;top:1250px;display:flex;justify-content:center"><span style="background:#161412;color:#fff;border-radius:999px;padding:12px 28px;font-size:24px">Vanilla Cream: <b>last one in stock</b></span></div>`,
});

/* R12 — Handwritten note: real leather */
{
  const f = frame('IMG_9618.JPG', 0.6, 0.42, 1.25, 0, 0, 1080, 1350);
  const [lx, ly] = f.at(0.77, 0.33);
  add({
    id: 'r12-real-leather-note', stage: 'MOFU', format: 'Handwritten note',
    html: `
      ${f.html}
      ${lightFade(24)}
      ${megaHead('Every zip. Every stitch.', 'Every detail.', '#161412', '#9b6b3e', 68)}
      <svg class="fill" width="1080" height="1350" style="position:absolute"><path d="M${lx - 200} ${ly - 190} Q ${lx - 40} ${ly - 190} ${lx - 30} ${ly + 10}" fill="none" stroke="#d4342b" stroke-width="7" stroke-linecap="round"/><path d="M${lx - 58} ${ly - 14} L${lx - 30} ${ly + 10} L${lx - 8} ${ly - 20}" fill="none" stroke="#d4342b" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <div class="abs" style="left:${lx - 700}px;top:${ly - 275}px;font-family:Caveat;font-weight:700;font-size:72px;color:#d4342b;transform:rotate(-5deg);text-shadow:0 0 14px rgba(255,255,255,.9)">yes, that’s real leather</div>
      ${priceTag(600, 1150)}`,
  });
}

module.exports = ads;

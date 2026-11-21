"""Add stories 4 and 5 to every future Available Now day (date > 2026-11-21) from high-demand models. Idempotent: skips days that already have n=4."""
import json, sys, re
sys.path.insert(0, '.')
import build_v4 as B
from extras_lib import parse, cutout
pool = json.load(open('../new-style/pool.json'))
q = json.load(open('queue_v2.json'))
used_titles = {w['title'] for e in q for w in e['watches']}
def cat(f): return [p for p in pool if f(p) and p['show_price'] and p['price_aed']]
CATS = {
 'ddombre': cat(lambda p: 'Day-Date 40' in p['title'] and 'Ombré' in p['title']),
 'skywg': cat(lambda p: 'Sky-Dweller 336934' in p['title']),
 'ro41': cat(lambda p: 'Royal Oak 41' in p['title'] and 'Chronograph' not in p['title'] and '– Steel,' in p['title']),
 'gmt': cat(lambda p: p['family'] == 'GMT-Master II' and '– Steel,' in p['title']),
 'sub': cat(lambda p: p['family'] == 'Submariner Date' and '– Steel,' in p['title']),
 'djwg': cat(lambda p: 'Datejust' in p['title'] and 'Steel & White Gold' in p['title']),
 'ddyg': cat(lambda p: 'Day-Date 40' in p['title'] and 'Yellow Gold' in p['title'] and ('Green' in p['title'] or 'Champagne' in p['title'])),
}
ROT = [('ddombre', 'skywg'), ('ro41', 'gmt'), ('sub', 'djwg'), ('ddyg', 'ro41'), ('skywg', 'sub'), ('gmt', 'ddombre')]
def pick(c, n=1):
    out = []
    for p in CATS[c]:
        if p['title'] in used_titles: continue
        out.append(p); used_titles.add(p['title'])
        if len(out) == n: break
    return out
def prep(p):
    w = parse(p); cutout(w)
    if w['vendor'] != 'Rolex' and 'Royal Oak' in p['title']:
        w['name'] = 'ROYAL OAK 41'; w['ref'] = p['title'].split(' 41 ')[1].split('.')[0]; w['spec'] = ' · '.join(['Steel', p['title'].split(' – ')[1].split(', ')[1]])
    return w
FN = dict(hero=B.st1_hero, cream=B.st2_cream, set=B.st4_set, editorial=B.st5_editorial, plaque=B.st6_plaque)
dates = sorted({e['date'] for e in q if e['kind'] == 'available' and e['date'] > '2026-11-21'})
jobs, new = [], []
for i, d in enumerate(dates):
    day = [e for e in q if e['date'] == d]
    have = {e['n'] for e in day}
    style = day[0]['style']
    for n, c0 in zip((4, 5), ROT[i % len(ROT)]):
        if n in have: continue
        nm = f'{d}_{n}'
        sty = style
        need = 2 if sty == 'pair' else 1
        if sty == 'pair' and not any(sum(1 for p in CATS[k] if p['title'] not in used_titles) >= 2 for k in CATS): sty = 'hero'; need = 1
        c = next((k for k in [c0] + [k for k in CATS if k != c0] if sum(1 for p in CATS[k] if p['title'] not in used_titles) >= need), None)
        if c is None: continue
        if sty == 'pair':
            ps = pick(c, 2)
            if len(ps) < 2: continue
            ws = [prep(p) for p in ps]
            fam = ws[0]['fam_label'] if ws[0]['family'] == ws[1]['family'] else 'HIGH-DEMAND' if False else 'ROLEX'
            B.st3_pair(ws[0], ws[1], headline=fam if ws[0]['vendor']==ws[1]['vendor']=='Rolex' else 'ICONIC', urgency=None, name=nm)
        else:
            ps = pick(c, 1)
            if not ps: continue
            ws = [prep(ps[0])]
            if sty == 'set' and ps[0]['vendor'] != 'Rolex': sty = 'hero'
            FN[sty](ws[0], urgency=None, name=nm)
        jobs.append(dict(html=f'templates/{nm}.html', out=f'queue/{nm}.jpg'))
        new.append(dict(date=d, n=n, kind='available', style=sty, urgency=None, file=f'queue/{nm}.jpg', watches=[dict(title=w['title'], ref=w['ref'], price=w['price']) for w in ws]))
rep = B.render(jobs)
q += new
json.dump(q, open('queue_v2.json', 'w'), indent=1, ensure_ascii=False)
print(len(new), 'new stories;', len(rep), 'warnings'); [print(r) for r in rep]

"""Build extra Available Now stories (n=4,5) for a given date from pool titles. Usage: python3 add_extras.py DATE title1_substring style1 title2_substring style2"""
import json, sys
sys.path.insert(0, '.')
import build_v4 as B
from extras_lib import parse, cutout
pool = json.load(open('../new-style/pool.json'))
date = sys.argv[1]
jobs = []
FN = dict(hero=B.st1_hero, cream=B.st2_cream, set=B.st4_set, editorial=B.st5_editorial, plaque=B.st6_plaque)
for n, (sub, style) in enumerate(zip(sys.argv[2::2], sys.argv[3::2]), 4):
    x = next(p for p in pool if sub in p['title'])
    w = parse(x); cutout(w)
    if w['vendor'] != 'Rolex' and 'Royal Oak' in x['title']:
        w['name'] = 'ROYAL OAK 41'; w['ref'] = '15510ST'; w['spec'] = 'Steel · Blue Dial'
    nm = f"{date}_{n}"
    FN[style](w, urgency=None, name=nm)
    jobs.append(dict(html=f"templates/{nm}.html", out=f"queue/{nm}.jpg"))
    print(nm, w['name'], w['price'])
print(B.render(jobs))

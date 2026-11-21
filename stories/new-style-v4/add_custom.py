import json, sys, re
sys.path.insert(0, '.')
import build_v4 as B
from extras_lib import parse, cutout
pool = json.load(open('../new-style/pool.json'))
FN = dict(hero=B.st1_hero, cream=B.st2_cream, set=B.st4_set, editorial=B.st5_editorial, plaque=B.st6_plaque)
ITEMS = [
 ('handle', 'rolex-daytona-126519ln-white-gold-steel-and-black-dial-oysterflex', 'hero', None),
 ('handle', 'rolex-yacht-master-42-226627-rlx-titanium-black-dial', 'cream', None),
 ('handle', 'rolex-daytona-126506-platinum-ice-blue-dial', 'plaque', None),
 ('handle', 'rolex-daytona-126505-everose-gold-chocolate-and-black-dial', 'editorial', None),
 ('handle', 'rolex-submariner-date-126610ln-steel-black-dial', 'set', None),
 ('handle', 'rolex-datejust-41-126300-steel-mint-green-dial-jubilee', 'hero', None),
 ('handle', 'rolex-datejust-41-126300-steel-white-dial-jubilee-2', 'cream', 'Steel · White Roman'),
]
jobs = []
for i, (_, h, style, spec) in enumerate(ITEMS, 1):
    x = next(p for p in pool if p['handle'] == h)
    w = parse(x)
    w['pid'] = re.sub(r'\W', '', h)[-50:]
    cutout(w)
    if spec: w['spec'] = spec
    nm = f'custom_{i}'
    FN[style](w, urgency=None, name=nm)
    jobs.append(dict(html=f'templates/{nm}.html', out=f'custom/{nm}.jpg'))
    print(nm, w['name'], w['ref'], w['price'], style)
print(B.render(jobs))

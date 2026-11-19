import json,re,sys,datetime
sys.path.insert(0,'.')
import build_v4 as B
RATE=3.65
q=json.load(open('queue_v2.json'))
only=sys.argv[1] if len(sys.argv)>1 else None   # date filter
jobs=[]
for e in q:
    if e['kind']!='available': continue
    if only and e['date']!=only: continue
    d=datetime.date.fromisoformat(e['date'])+datetime.timedelta(days=1)
    src=f"templates/{d.isoformat()}_{e['n']}.html"
    t=open(src).read()
    def sub(m):
        aed=int(m.group(1).replace(',',''));usd=round(aed/RATE)
        return f"AED {m.group(1)}<span class='usd'>≈ ${usd:,}</span>"
    t2=re.sub(r"AED (\d[\d,]*)",sub,t)
    t2=t2.replace("top:1442px","top:1506px");t2=t2.replace("</style>",".usd{display:block;font-size:40px;font-weight:600;opacity:.82;letter-spacing:0;line-height:1.2;margin-top:4px;white-space:nowrap}</style>",1)
    dst=f"templates/usd_{e['date']}_{e['n']}.html"
    open(dst,'w').write(t2)
    jobs.append(dict(html=dst,out=e['file']))
print(len(jobs),'jobs')
rep=B.render(jobs)
print('warnings',rep)

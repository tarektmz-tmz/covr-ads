import json
def make(mapfile):
    m=json.load(open(mapfile));sp=m['spans']
    def f(t):
        cut=0.0
        for s0,s1 in sp:
            if t>=s1:cut+=s1-s0
            elif t>s0:cut+=t-s0;break
            else:break
        return round(t-cut,3)
    return f,m

#!/usr/bin/env python3
"""Recolour the Latte-on-chair photo into other COVR colourways (hover photos for the shop).
usage: python3 creative/chair_recolor.py ash   -> store/hover/chair-ash.jpg"""
import sys, os, numpy as np, cv2
from PIL import Image
from scipy import ndimage as nd
S='/tmp/claude-0/-home-user-covr-ads/fdd928c7-80d1-5009-8cea-0a480b6797f3/scratchpad/chair/'
OUT='/home/user/covr-ads/store/hover/'
COL={ # body rgb, leather rgb, hardware ('dark'|'gold'), strap rgb or None(keep), texture
 'ash':        dict(body=(86,84,84), leather=(22,21,21), hw='dark',  strap=None, tex='denim'),
}
c=COL[sys.argv[1]]
im=np.asarray(Image.open(S+'src.png').convert('RGB')).astype(np.float32)
H,W=im.shape[:2]; yy,xx=np.mgrid[0:H,0:W]
r,g,b=im[...,0],im[...,1],im[...,2]; L=0.299*r+0.587*g+0.114*b
cov=np.asarray(Image.open(S+'m_cover.png').convert('L'))>128
grip=nd.binary_dilation(np.asarray(Image.open(S+'m_grip.png').convert('L'))>128,iterations=3)
cov=nd.binary_fill_holes(cov)&~grip
wall=((r-b)>38)&(L>95)&~(np.clip(((g-b)-22)/20,0,1)*np.clip((L-90)/40,0,1)>0.5)
cov&=~wall
cov=nd.binary_opening(cov,iterations=1)
edge=nd.binary_dilation(cov,iterations=12)&~cov&((r-b)<28)&(L>105)&~grip
edge&=~nd.binary_dilation(np.asarray(Image.open(S+'m_strap.png').convert('L'))>128,iterations=2)
cov|=edge
# canvas = light pixels; leather = dark brown; gold = yellowish & bright
Lc=np.median(L[cov&(L>150)])
t=np.clip((L-95)/(150-95),0,1); t=t*t*(3-2*t)
shade=np.clip(cv2.GaussianBlur(L,(0,0),4)/Lc,0.3,1.4)**1.2
detail=(L-cv2.GaussianBlur(L,(0,0),1.5))*0.35
rng=np.random.default_rng(3)
if c['tex']=='denim':
    u=(xx*np.cos(-0.5)+yy*np.sin(-0.5))
    wob=cv2.GaussianBlur(rng.normal(0,1,(H,W)).astype(np.float32),(0,0),5)*1.2
    tex=np.sin(2*np.pi*u/3.4+wob)*0.8
    nz=lambda sg: (lambda q: q/q.std())(cv2.GaussianBlur(rng.normal(0,1,(H,W)).astype(np.float32),(0,0),sg))
    mott=nz(8)*1.6+nz(2.5)*0.9   # denim slub/fade
    tex=tex*3.0+nz(0.7)*2.5+mott
else:
    tex=cv2.GaussianBlur(rng.normal(0,1,(H,W)).astype(np.float32),(0,0),0.9)*2.0
body=np.array(c['body'],np.float32); lea=np.array(c['leather'],np.float32)
canvas=body*shade[...,None]+((tex+detail)[...,None])*(body/body.mean())
Ll=np.median(L[cov&(L<80)]) if (cov&(L<80)).any() else 60
leather=lea*np.clip(L/Ll,0.4,2.2)[...,None]+detail[...,None]*0.5
new=t[...,None]*canvas+(1-t)[...,None]*leather
gold=np.clip(((g-b)-22)/20,0,1)*np.clip((L-90)/40,0,1)
if c['hw']=='dark':
    new=new*(1-gold[...,None])+np.stack([L*0.30+12]*3,-1)*gold[...,None]
else:
    new=new*(1-gold[...,None])+im*gold[...,None]
a=cv2.GaussianBlur(cov.astype(np.float32),(0,0),1.0)[...,None]
out=im*(1-a)+new*a
if c['hw']=='dark':  # clips/rings just outside the cover body
    near=nd.binary_dilation(cov,iterations=40)&~cov&~grip
    gk=gold*near
    out=out*(1-gk[...,None])+np.stack([L*0.30+12]*3,-1)*gk[...,None]
# strap webbing
if c['strap'] is not None:
    sm=np.asarray(Image.open(S+'m_strap.png').convert('L'))>128
    sm&=((r-b)<45)&(L>110)&~cov
    lab,n=nd.label(sm); sz=nd.sum(sm,lab,range(1,n+1))
    sm=np.isin(lab,[i+1 for i,v in enumerate(sz) if v>4000])
    sm=nd.binary_closing(sm,iterations=2)
    Ls=np.median(L[sm]); st=np.array(c['strap'],np.float32)
    sn=st*np.clip(L/Ls,0.5,1.4)[...,None]+((L-cv2.GaussianBlur(L,(0,0),1.5))*0.5)[...,None]
    sa=cv2.GaussianBlur(sm.astype(np.float32),(0,0),1.0)[...,None]
    out=out*(1-sa)+sn*sa
os.makedirs(OUT,exist_ok=True)
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save(OUT+'chair-'+sys.argv[1]+'.jpg',quality=93)
print('ok')

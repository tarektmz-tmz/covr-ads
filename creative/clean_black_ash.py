#!/usr/bin/env python3
"""Remove Nike logos (shirt, cap, socks, shoe) and turn gold hardware on the Total Black cover black."""
import numpy as np, cv2
from scipy import ndimage as nd
P='/home/user/covr-ads/'
im=cv2.imread(P+'media/black-ash-couple-studio.jpg')
H,W=im.shape[:2]
L=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
b,g,r=[im[...,i].astype(np.float32) for i in range(3)]
yy,xx=np.mgrid[0:H,0:W]
def box(x0,y0,x1,y1): return (xx>=x0)&(xx<x1)&(yy>=y0)&(yy<y1)
out=im.copy()
# 1) shirt swoosh: white on black
m=box(560,905,642,955)&(L>70)
m=nd.binary_dilation(m,iterations=3)
out=cv2.inpaint(out,m.astype(np.uint8)*255,6,cv2.INPAINT_TELEA)
# 2) sock swooshes: dark on white socks
for bx in [(455,1862,525,1892),(1028,1640,1090,1686)]:
    m=box(*bx)&(L<170); m=nd.binary_dilation(m,iterations=2)
    out=cv2.inpaint(out,m.astype(np.uint8)*255,5,cv2.INPAINT_TELEA)
# 3) shoe swoosh: light grey on black shoe
m=box(938,1774,1030,1852)&(L>95)&(L<205); m=nd.binary_dilation(m,iterations=3)
fill=cv2.inpaint(out,m.astype(np.uint8)*255,7,cv2.INPAINT_TELEA)
fill=np.minimum(fill.astype(np.float32),cv2.GaussianBlur(fill,(0,0),2).astype(np.float32)*0+np.array([42,40,40],np.float32)+cv2.GaussianBlur(fill,(0,0),1).astype(np.float32)*0.15)
fill=np.clip(fill,0,255).astype(np.uint8)
mm=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.5)[...,None]
out=np.clip(out*(1-mm)+fill*mm,0,255).astype(np.uint8)
# 4) cap logo: copy corduroy patch from the left (vertical ridges), feathered
x0,y0,x1,y1=652,622,712,662; dx=-62
patch=out[y0:y1,x0+dx:x1+dx].astype(np.float32)
tgt=out[y0:y1,x0:x1].astype(np.float32)
patch*= (tgt.mean((0,1))/np.maximum(patch.mean((0,1)),1))
w=np.zeros((y1-y0,x1-x0),np.float32); w[4:-4,4:-4]=1; w=cv2.GaussianBlur(w,(0,0),2.5)[...,None]
out[y0:y1,x0:x1]=np.clip(tgt*(1-w)+patch*w,0,255).astype(np.uint8)
# 5) gold hardware on the black cover -> black/gunmetal
o=out.astype(np.float32); Lo=cv2.cvtColor(out,cv2.COLOR_BGR2GRAY).astype(np.float32)
gold=box(0,1036,318,1300)&((r-b)>28)&(L>55)
k=np.clip(((r-b)-20)/25,0,1)*nd.binary_dilation(gold,iterations=1)
hw=np.zeros((H,W),bool)
for bx in [(222,1120,260,1162),(274,1112,320,1144),(93,1076,162,1278),(280,1170,302,1212),(158,1034,212,1078),(55,1022,78,1052)]:
    hw|=box(*bx)
hwk=(hw&(L>44)&((r-b)>9)&~box(97,1100,120,1175)).astype(np.float32)
hwk=np.maximum(hwk,(hw&(L>120)&((r-b)>3)&box(222,1112,320,1162)).astype(np.float32))
k=np.maximum(k,cv2.GaussianBlur(hwk,(0,0),0.8))
dark=np.stack([Lo*0.20+9]*3,-1)
o=o*(1-k[...,None])+dark*k[...,None]
out=np.clip(o,0,255).astype(np.uint8)
cv2.imwrite(P+'media/black-ash-couple-studio-clean.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
print('ok')

"""Full-quality smooth pause cutting for a reel (50 fps frames).
Cuts part of every long pause (audio and video together, words untouched), at the point where the picture
before and after is most alike, with a very short dissolve across the join. Nothing is sped up.
usage: python3 smooth_cut_50.py <workdir>   (workdir has audio.wav and vf/f_0001.jpg ... at 50 fps)
output: <workdir>/sc/audio.wav, <workdir>/sc/vf2/f_0001.jpg ... (symlinks + a few blended frames), <workdir>/sc/map.json
"""
import sys,os,json,subprocess,numpy as np,wave
from PIL import Image
W0=sys.argv[1]
FPS=50;KEEP=0.30;MINP=0.40;NB=5;SR=48000
os.makedirs(W0+'/sc/vf2',exist_ok=True)
raw=subprocess.run(['ffmpeg','-v','error','-i',W0+'/audio.wav','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
a=np.frombuffer(raw,dtype=np.float32).reshape(-1,2)
NFR=len([f for f in os.listdir(W0+'/vf') if f.endswith('.jpg')])
T=min(len(a)/SR,NFR/FPS)
mono=np.abs(a).max(axis=1);W=int(SR*0.01);n=len(mono)//W
rms=np.sqrt((mono[:n*W].reshape(n,W)**2).mean(axis=1));sil=rms<10**(-40/20)
runs=[];i=0
while i<n:
    if sil[i]:
        j=i
        while j<n and sil[j]:j+=1
        if (j-i)*0.01>=MINP and i>0 and j<n:runs.append((i*0.01,j*0.01))
        i=j
    else:i+=1
cache={}
def G(k):
    if k not in cache:
        cache[k]=np.asarray(Image.open(W0+'/vf/f_%04d.jpg'%(k+1)).convert('L').resize((90,160))).astype(np.float32)
        if len(cache)>400:cache.pop(next(iter(cache)))
    return cache[k]
mse=lambda p,q:float(((G(p)-G(q))**2).mean())
cuts=[]
for s,e in runs:
    d=e-s;rem=int(round((d-KEEP)*FPS))
    if rem<NB+1:continue
    gap=rem-NB
    f0=int(np.ceil(s*FPS))+NB;f1=int(np.floor(e*FPS))-1
    best=None
    for a0 in range(f0,f1):
        b0=a0+gap+1
        if b0+NB-1>f1:break
        c=sum(mse(a0-NB+1+k,b0+k) for k in range(NB))
        if best is None or c<best[0]:best=(c,a0,b0)
    if best:cuts.append(best)
plan=[];prev=0;spans=[]
for c,a0,b0 in cuts:
    for k in range(prev,a0-NB+1):plan.append(('f',k))
    for k in range(NB):plan.append(('b',a0-NB+1+k,b0+k,(k+1)/(NB+1)))
    prev=b0+NB;spans.append(((a0+1)/FPS,(b0+NB)/FPS))
for k in range(prev,NFR):plan.append(('f',k))
# audio
p=0.0;X=int(0.01*SR);parts=[]
for s0,s1 in spans:
    parts.append((int(p*SR),int(s0*SR)));p=s1
parts.append((int(p*SR),int(T*SR)))
chs=[]
for k,(x0,x1) in enumerate(parts):
    ch=a[x0:x1].copy()
    if k>0:ch[:X]*=np.linspace(0,1,X)[:,None]
    if k<len(parts)-1:ch[-X:]*=np.linspace(1,0,X)[:,None]
    chs.append(ch)
na=np.concatenate(chs)
with wave.open(W0+'/sc/audio.wav','wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(na,-1,1)*32767).astype('<i2').tobytes())
# frames
for k_,item in enumerate(plan):
    dst=W0+'/sc/vf2/f_%04d.jpg'%(k_+1)
    if os.path.lexists(dst):os.remove(dst)
    if item[0]=='f':os.symlink('../../vf/f_%04d.jpg'%(item[1]+1),dst)
    else:
        A=Image.open(W0+'/vf/f_%04d.jpg'%(item[1]+1)).convert('RGB');B=Image.open(W0+'/vf/f_%04d.jpg'%(item[2]+1)).convert('RGB')
        Image.blend(A,B,item[3]).save(dst,quality=95)
json.dump(dict(spans=spans,newT=len(plan)/FPS,nf=len(plan),oldT=T),open(W0+'/sc/map.json','w'))
print('cuts %d | removed %.2fs | new length %.2fs (was %.2fs) | frames %d | audio %.2fs'%(len(cuts),sum(b-a for a,b in spans),len(plan)/FPS,T,len(plan),len(na)/SR))

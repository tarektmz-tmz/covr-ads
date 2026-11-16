"""Shorten silent gaps in a reel without touching the words.
Speech stays 1:1 (lips stay in sync). Each long pause is compressed: audio keeps a short silence,
video plays that stretch faster so motion stays continuous (no jump cuts).
usage: python3 compress_pauses.py <dir with audio.wav, cfg_r1.js-like cfg.js, vf/>  <outdir>
"""
import sys,os,json,subprocess,numpy as np,wave
src,out=sys.argv[1],sys.argv[2]
os.makedirs(out,exist_ok=True)
SR=48000
raw=subprocess.run(['ffmpeg','-v','error','-i',src+'/audio.wav','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
a=np.frombuffer(raw,dtype=np.float32).reshape(-1,2)
mono=np.abs(a).max(axis=1)
W=int(SR*0.01)
n=len(mono)//W
rms=np.sqrt((mono[:n*W].reshape(n,W)**2).mean(axis=1))
thr=10**(-40/20)
sil=rms<thr
# silence runs >= 0.30 s
runs=[];i=0
while i<n:
    if sil[i]:
        j=i
        while j<n and sil[j]:j+=1
        if (j-i)*0.01>=0.30 and i>0 and j<n:runs.append((i*0.01,j*0.01))
        i=j
    else:i+=1
def newlen(d): return d if d<=0.30 else 0.22+0.20*(d-0.22)
seg=[];pos=0.0;npos=0.0
for s,e in runs:
    if s>pos:seg.append((pos,s,npos,npos+(s-pos)));npos+=s-pos
    nl=newlen(e-s);seg.append((s,e,npos,npos+nl));npos+=nl;pos=e
T=len(a)/SR
seg.append((pos,T,npos,npos+(T-pos)));npos+=T-pos
def f(t):
    for o0,o1,n0,n1 in seg:
        if t<=o1: return n0+(t-o0)*((n1-n0)/(o1-o0) if o1>o0 else 1)
    return seg[-1][3]
# audio
parts=[]
for o0,o1,n0,n1 in seg:
    chunk=a[int(o0*SR):int(o1*SR)]
    need=int(round((n1-n0)*SR))
    if need<len(chunk):
        h=need//2;chunk=np.concatenate([chunk[:h],chunk[len(chunk)-(need-h):]])
    parts.append(chunk)
na=np.concatenate(parts)
pcm=(np.clip(na,-1,1)*32767).astype('<i2')
with wave.open(out+'/audio.wav','wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
# frames map (50 fps)
NF=int(npos*50)
fm=[]
for k in range(NF):
    t=k/50
    for o0,o1,n0,n1 in seg:
        if t<=n1:
            ot=o0+(t-n0)*((o1-o0)/(n1-n0) if n1>n0 else 1);break
    fm.append(min(int(round(ot*50))+1,int(T*50)))
json.dump(dict(seg=seg,runs=runs,newT=npos,oldT=T,frames=fm),open(out+'/map.json','w'))
print('pauses compressed:',len(runs),'old length %.2f new length %.2f saved %.2f s'%(T,npos,T-npos))

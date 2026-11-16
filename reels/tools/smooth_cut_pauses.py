"""Shorten pauses by CUTTING (no speed-up). For every long pause, remove a piece of the silent gap
(audio and video together) and pick the cut where the picture before and after is nearly identical,
so the join is invisible. Words and lips stay untouched.
usage: python3 smooth_cut_pauses.py <video.mp4> <audio.wav> <fps> <out_dir> [max_seconds] [keep=0.28] [min_pause=0.45]
writes out_dir/keep_frames.json (old frame numbers kept, 1-based) and out_dir/audio.wav
"""
import sys,os,json,subprocess,numpy as np,wave
video,audio,fps,out=sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]
maxs=float(sys.argv[5]) if len(sys.argv)>5 else 1e9
keep=float(sys.argv[6]) if len(sys.argv)>6 else 0.28
minp=float(sys.argv[7]) if len(sys.argv)>7 else 0.45
os.makedirs(out,exist_ok=True)
SR=48000
raw=subprocess.run(['ffmpeg','-v','error','-i',audio,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
a=np.frombuffer(raw,dtype=np.float32).reshape(-1,2)
T=min(len(a)/SR,maxs)
a=a[:int(T*SR)]
mono=np.abs(a).max(axis=1);W=int(SR*0.01);n=len(mono)//W
rms=np.sqrt((mono[:n*W].reshape(n,W)**2).mean(axis=1));sil=rms<10**(-40/20)
runs=[];i=0
while i<n:
    if sil[i]:
        j=i
        while j<n and sil[j]:j+=1
        if (j-i)*0.01>=minp and i>0 and j<n:runs.append((i*0.01,j*0.01))
        i=j
    else:i+=1
# small gray frames
fr=subprocess.run(['ffmpeg','-v','error','-t',str(T+0.2),'-i',video,'-vf','fps=%d,scale=90:160,format=gray'%fps,'-f','rawvideo','-'],capture_output=True).stdout
F=np.frombuffer(fr,dtype=np.uint8).reshape(-1,160,90).astype(np.float32)
NFR=min(len(F),int(T*fps))
def mse(p,q):return float(((F[p]-F[q])**2).mean())
removed=[]
for s,e in runs:
    d=e-s;rem=int(round((d-keep)*fps))
    if rem<2:continue
    f0=int(np.ceil(s*fps))+2;f1=int(np.floor(e*fps))-2
    best=None
    for a0 in range(f0,f1-rem-1):
        b0=a0+rem+1
        if b0>f1:break
        c=mse(a0,b0)+0.5*mse(a0-1,b0-1)+0.5*mse(min(a0+1,NFR-1),min(b0+1,NFR-1))
        if best is None or c<best[0]:best=(c,a0,b0)
    if best:removed.append((best[1]+1,best[2]-1,best[0]))  # frames removed inclusive
keepf=[];prev=0
for r0,r1,c in removed:
    keepf+=list(range(prev,r0));prev=r1+1
keepf+=list(range(prev,NFR))
# audio: drop same spans
ranges=[];p=0
for r0,r1,c in removed:
    ranges.append((p,int(r0/fps*SR)));p=int((r1+1)/fps*SR)
ranges.append((p,len(a)))
parts=[];X=int(0.01*SR)
for k,(x0,x1) in enumerate(ranges):
    ch=a[x0:x1].copy()
    if k>0:ch[:X]*=np.linspace(0,1,X)[:,None]
    if k<len(ranges)-1:ch[-X:]*=np.linspace(1,0,X)[:,None]
    parts.append(ch)
na=np.concatenate(parts)
with wave.open(out+'/audio.wav','wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(na,-1,1)*32767).astype('<i2').tobytes())
json.dump(dict(keep=[k+1 for k in keepf],removed=removed,fps=fps),open(out+'/keep_frames.json','w'))
# jump metric: difference across cuts vs typical frame step
typ=np.median([mse(k,k+1) for k in range(0,NFR-1,3)])
jumps=[mse(r0-1,r1+1) for r0,r1,c in removed]
print('cuts: %d | removed %.2fs | new length %.2fs (was %.2fs)'%(len(removed),sum((r1-r0+1) for r0,r1,c in removed)/fps,len(keepf)/fps,NFR/fps))
print('typical frame-to-frame change %.1f | change across cuts: median %.1f max %.1f'%(typ,np.median(jumps),max(jumps)))

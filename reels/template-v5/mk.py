import json,sys,subprocess,os
# usage: mk.py name  (reads cfg_<name>.json -> cfg_<name>.js, extracts frames)
n=sys.argv[1]; S='/tmp/claude-0/-home-user-covr-ads/bca811f7-ffe6-553a-aec5-c55dc8fbf7aa/scratchpad/batch2/'
c=json.load(open(f'cfg_{n}.json'))
w=json.load(open(S+n+'.words.json'))
for old,new in c.get('fix',{}).items():
    pass
words=[[x[0],x[1],x[2]] for x in w]
for i,txt in c.get('wordfix',{}).items(): words[int(i)][0]=txt
for i in sorted(map(int,c.get('drop',[])),reverse=True): words.pop(i)
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',S+n+'.mp4']).strip())
os.makedirs(f'vf_{n}',exist_ok=True)
if not os.listdir(f'vf_{n}'):
    subprocess.run(['ffmpeg','-v','error','-i',os.environ.get('FRAMESRC',S+n+'.mp4'),'-fps_mode','passthrough','-q:v','2',f'vf_{n}/f_%04d.jpg'],check=True)
nf=len(os.listdir(f'vf_{n}'))
C=dict(vf=f'vf_{n}/f_',nf=nf,dur=dur,words=words,scenes=c['scenes'],fps=int(os.environ.get('FPS','25')))
open(f'cfg_{n}.js','w').write('window.C='+json.dumps(C)+';')
open(f'page_{n}.html','w').write(open(os.environ.get('PAGE','page.html')).read().replace('cfg.js',f'cfg_{n}.js'))
print(n,'frames',nf,'dur',dur,'words',len(words))

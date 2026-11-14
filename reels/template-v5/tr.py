import sys,json,subprocess,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel('medium',device='cpu',compute_type='int8')
for n in sys.argv[1:]:
    raw=subprocess.run(['ffmpeg','-v','error','-i','../batch2/'+n+'.mp4','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    a=np.frombuffer(raw,dtype=np.float32)
    segs,_=m.transcribe(a,word_timestamps=True,language='en')
    w=[[x.word.strip(),round(float(x.start),3),round(float(x.end),3)] for s in segs for x in s.words]
    json.dump(w,open('../batch2/'+n+'.words.json','w')); print(n,len(w),w[-1])

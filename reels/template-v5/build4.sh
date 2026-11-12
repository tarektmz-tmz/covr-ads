#!/bin/bash
set -e; n=$1
PAGE=${PAGE:-page_v4.html} python3 mk.py $n
NFR=$(python3 -c "import subprocess;d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','../batch2/$n.mp4']));print(int((d+2.6)*25)+1)")
NODE_PATH=/opt/node22/lib/node_modules node render.js $NFR 0 page_$n.html out_$n >/dev/null
T=$(python3 -c "import subprocess;print(float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','../batch2/$n.mp4']))+2.6)")
ffmpeg -y -v error -framerate 25 -i out_$n/f_%04d.jpg -i ../batch2/$n.mp4 -map 0:v -map 1:a -af apad -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -r 25 -c:a aac -b:a 192k -movflags +faststart -t $T reel_$n.mp4
ls -la reel_$n.mp4

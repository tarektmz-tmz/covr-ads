#!/bin/bash
# usage: build5.sh name  (needs cfg_name.json, ../batch2/name.mp4 (audio+25fps), name_v50.mp4 (50fps frames))
set -e; n=$1; FPS=50
export FPS FRAMESRC=$PWD/${n}_v50.mp4
PAGE=page_v6.html python3 mk.py $n
D=$(python3 -c "import subprocess;print(float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','../batch2/$n.mp4'])))")
NF=$(python3 -c "print(int(($D+2.6)*$FPS)+1)")
W=4; STEP=$(( (NF + W - 1) / W ))
for w in $(seq 0 $((W-1))); do A=$((w*STEP)); B=$(( (w+1)*STEP )); [ $B -gt $NF ] && B=$NF
  NODE_PATH=/opt/node22/lib/node_modules node render.js $A $B page_$n.html out_$n $FPS & done
wait
T=$(python3 -c "print($D+2.6)")
ffmpeg -y -v error -framerate $FPS -i out_$n/f_%05d.jpg -i ../batch2/$n.mp4 -map 0:v -map 1:a -af apad -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -r $FPS -c:a aac -b:a 192k -movflags +faststart -t $T reel_$n.mp4
ls -la reel_$n.mp4

#!/bin/bash
# Usage: mix_music.sh in.mp4 out.mp4 [music_volume=0.05]
# Mixes the standard quiet ambient track under the voice: looped with 3 s crossfades,
# ducked by the voice (sidechain), fade in/out. Video stream is copied untouched.
set -e
IN="$1"; OUT="$2"; VOL="${3:-0.05}"
MUS="$(dirname "$0")/../templates/music/standard_ambient.mp3"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
N=$(python3 -c "import math;print(max(2,math.ceil($DUR/36)+1))")
INPUTS=""; FILT=""; PREV="[0:a]"
for i in $(seq 0 $((N-1))); do INPUTS="$INPUTS -i $MUS"; done
FILT="[0:a]anull[x0]"; PREV="[0:a]"
LAST="[0:a]"
CH=""
for i in $(seq 0 $((N-1))); do CH="$CH[$i:a]"; done
# build crossfade chain
FILT=""; PREV="[0:a]"
for i in $(seq 1 $((N-1))); do FILT="$FILT${PREV}[$i:a]acrossfade=d=3:c1=tri:c2=tri[c$i];"; PREV="[c$i]"; done
ffmpeg -y -v error -i "$MUS" $(for i in $(seq 1 $((N-1))); do echo -n "-i $MUS "; done) -i "$IN" \
 -filter_complex "${FILT}${PREV}volume=$VOL,afade=t=in:d=1.5[m];[$N:a]asplit[v1][v2];[m][v2]sidechaincompress=threshold=0.015:ratio=8:attack=20:release=500[md];[v1][md]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=$(python3 -c "print(max(0,$DUR-1.2))"):d=1.2[a]" \
 -map "$N:v" -map "[a]" -c:v copy -c:a aac -b:a 192k -t "$DUR" "$OUT"

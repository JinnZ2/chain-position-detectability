#!/bin/bash
# RPF-01: re-fetch Qwen2.5-0.5B-Instruct weights into /tmp/qwen (local disk) and verify.
# Source: modelscope.cn mirror; integrity anchor: HF git-LFS pointer oid (via hf-mirror.com).
set -e
mkdir -p /tmp/qwen && cd /tmp/qwen
curl -sL -m 30 "https://hf-mirror.com/Qwen/Qwen2.5-0.5B-Instruct/raw/main/model.safetensors" -o lfs_pointer.txt
URL="https://modelscope.cn/models/Qwen/Qwen2.5-0.5B-Instruct/resolve/master/model.safetensors"
TOTAL=988097824; CH=67108864; i=0
while [ $((i*CH)) -lt $TOTAL ]; do
  A=$((i*CH)); B=$(( (i+1)*CH - 1 )); [ $B -ge $TOTAL ] && B=$((TOTAL-1))
  curl -sL -m 200 -r $A-$B -o chunk_$(printf %02d $i) "$URL"
  i=$((i+1))
done
cat chunk_* > model.safetensors && rm -f chunk_*
B="https://modelscope.cn/models/Qwen/Qwen2.5-0.5B-Instruct/resolve/master"
for f in config.json generation_config.json tokenizer_config.json tokenizer.json vocab.json merges.txt; do
  curl -sL -m 60 -o $f "$B/$f"
done
python3 - <<'EOF'
import hashlib
h = hashlib.sha256()
with open('/tmp/qwen/model.safetensors','rb') as f:
    for blk in iter(lambda: f.read(1<<20), b''): h.update(blk)
got = h.hexdigest()
exp = open('/tmp/qwen/lfs_pointer.txt').read().split('oid sha256:')[1].split()[0]
print('weights sha256:', got)
print('MATCH' if got == exp else 'MISMATCH')
EOF

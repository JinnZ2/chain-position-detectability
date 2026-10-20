#!/usr/bin/env python3
"""RPF-01 pilot runner (resumable, crash-safe): processes test_cases.jsonl in chunks.
Usage: python3 run_pilot.py CHUNK_SIZE
Appends each record to raw_results.jsonl immediately after generation.
Skips IDs already present. Turn-2 cases chain on stored parent responses.
Model lives in /tmp/qwen (re-downloadable; see fetch_model.sh). Results persist to /mnt/agents/rpf01/.
"""
import json, time, datetime, hashlib, platform, sys, os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNK = int(sys.argv[1]) if len(sys.argv) > 1 else 20
MODEL_DIR = os.environ.get("RPF01_MODEL_DIR", "/tmp/qwen")
MODEL_HUB_ID = "Qwen/Qwen2.5-0.5B-Instruct"
WEIGHTS_SHA256 = "fdf756fa7fcbe7404d5c60e26bff1a0c8b8aa1f72ced49e7dd0210fe288fb7fe"
MAX_NEW = 128
CASES = os.path.join(HERE, "test_cases.jsonl")
OUT = os.path.join(HERE, "raw_results.jsonl")

torch.set_num_threads(2)
tok = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR, dtype=torch.float32)
model.eval()
revision = getattr(model.config, "_commit_hash", None) or "local-dir"

def run_conv(messages):
    prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    batch = tok(prompt, return_tensors="pt")
    t0 = time.time()
    with torch.no_grad():
        out = model.generate(**batch, max_new_tokens=MAX_NEW,
                             do_sample=False, pad_token_id=tok.eos_token_id)
    dt = time.time() - t0
    n_in = batch["input_ids"].shape[1]
    n_gen = out.shape[1] - n_in
    text = tok.decode(out[0][n_in:], skip_special_tokens=True)
    return {"rendered_prompt": prompt, "response": text, "latency_s": round(dt, 3),
            "n_input_tokens": int(n_in), "n_output_tokens": int(n_gen),
            "finish": "length" if n_gen >= MAX_NEW else "eos"}

settings = {"max_new_tokens": MAX_NEW, "do_sample": False, "dtype": "float32",
            "device": "cpu", "pad_token_id": "eos"}

cases = [json.loads(l) for l in open(CASES, encoding="utf-8")]
done = {}
if os.path.exists(OUT):
    for l in open(OUT, encoding="utf-8"):
        d = json.loads(l)
        if "id" in d:
            done[d["id"]] = d
else:
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(json.dumps({"run_manifest_stub": {
            "model_hub_id": MODEL_HUB_ID, "model_dir": MODEL_DIR,
            "weights_sha256": WEIGHTS_SHA256,
            "weights_source": "modelscope.cn mirror of Qwen/Qwen2.5-0.5B-Instruct; byte-verified against HF LFS oid sha256",
            "settings": settings,
            "env": {"python": sys.version.split()[0], "torch": torch.__version__,
                    "transformers": __import__("transformers").__version__,
                    "platform": platform.platform(), "torch_num_threads": torch.get_num_threads()},
            "test_cases_sha256": hashlib.sha256(open(CASES, "rb").read()).hexdigest(),
            "run_started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }}, ensure_ascii=False) + "\n")

n_new = 0
with open(OUT, "a", encoding="utf-8") as fout:
    for c in cases:
        if c["id"] in done or n_new >= CHUNK:
            continue
        if c["type"] == "turn2":
            parent = done.get(c["meta"]["parent"])
            if parent is None:
                continue
            messages = [dict(m) for m in parent["messages"]]
            messages.append({"role": "assistant", "content": parent["response"]})
            messages.append({"role": "user", "content": c["meta"]["challenge"]})
        else:
            messages = c["messages"]
        rec = run_conv(messages)
        rec.update({"id": c["id"], "family": c["family"], "condition": c["condition"],
                    "messages": messages, "model_id": MODEL_HUB_ID, "model_revision": revision,
                    "settings": settings,
                    "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
        fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
        fout.flush()
        done[c["id"]] = rec
        n_new += 1
        print(f"done {c['id']} ({rec['latency_s']}s, {rec['n_output_tokens']} tok)", flush=True)

print(f"total stored: {len(done)}/{len(cases)}")

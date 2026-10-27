# SOURCE_AUDIT.md — RPF-01 source audit

Audit date: 2026-10-21. Auditor: Kimi (execution agent). Scope: the five projects named in WO RPF-01 §1, plus bycatch found during the search. Verification method: repository pages, LICENSE files, and papers fetched and read during the session. Nothing was assumed runnable on reputation alone.

## Environment access audit (determines what "reuse" can mean here)

| Resource | Status | Evidence |
|---|---|---|
| agent-gw chat completions (`/v1/chat/completions`, `/v1/messages`) | **Blocked** | HTTP 403 "This credential is not permitted to access this endpoint" for all attempted model names (kimi-k2-0905-preview, kimi-k2, moonshot-v1-8k, kimi-latest) |
| agent-gw `list_models` | **Blocked** | HTTP 403, same credential |
| huggingface.co direct | **Blocked** | connect timeout on resolve endpoints (main page HEAD 200 via edge cache only) |
| hf-mirror.com | Reachable, throttled (~0.2 MB/s on resolve) | used only for the git-LFS pointer (integrity anchor) |
| modelscope.cn | Reachable, fast, 100 MiB/response cap | weights fetched in 15 ranged chunks, reassembled |
| Local compute | 2 CPU threads, 4 GB RAM, torch 2.8.0+cu128 (CPU), no GPU | `nproc`, `free` |

Consequence: no API-model access. Pilot subject = locally executed open-weight model. Weights integrity: `model.safetensors` sha256 = `fdf756fa7fcbe7404d5c60e26bff1a0c8b8aa1f72ced49e7dd0210fe288fb7fe`, byte-identical to the HuggingFace git-LFS `oid` for Qwen/Qwen2.5-0.5B-Instruct (pointer fetched from hf-mirror). Provenance: modelscope.cn mirror of the same repo.

## Project audit

### 1. SYCON-Bench — sycophancy under multi-turn pressure
- URL: https://github.com/JiseungHong/SYCON-Bench (paper: arXiv:2505.23840, Findings of EMNLP 2025)
- License: **MIT** (stated in repo README; LICENSE file referenced)
- Contents: 500 multi-turn prompts, 5 turns each; three scenarios (debate 100, unethical stereotypes 200 via StereoSet, false presuppositions 200 via CREPE); metrics Turn-of-Flip (ToF) and Number-of-Flip (NoF); four prompting strategies.
- Dependencies: per-setting requirements.txt; open-weight models via transformers (+bitsandbytes for quantization); closed models via API keys.
- Evaluation method: **GPT-4o as judge** at every turn (labels whether response aligns with expected stance).
- Limitations for this WO: (a) judge labels are model-generated — WO §5 forbids treating them as ground truth, so the published gold judgments would need re-adjudication; (b) running it as-is requires either API access (blocked here) or a GPU budget for the judged models; (c) debate/stereotype scenarios are subjective by design — the false-presupposition subset is the only one with objective ground truth.
- **Reuse decision**: did not execute. Adopted the design pattern of escalating user pressure across turns for Test D multi-turn legs, and the flip-based measurement vocabulary. No SYCON items copied.

### 2. SycoBench-600 — correction selectivity
- URL: https://github.com/debu-sinha/sycobench-600 (Findings of ACL 2026; dataset at huggingface.co/datasets/dsinha/sycobench-600)
- License: **MIT** (LICENSE file fetched and read byte-level: "Copyright (c) 2026 Debu Sinha")
- Contents: 600 English MCQ instances over 272 normalized stems, 8 domains, 3 difficulty tiers; three misleading pressure styles (doubt, authority, wrong suggestion) + one matched correct-suggestion condition; metrics Acc, PRA_all, Syco, Stub_nc, Sel (correction selectivity = Update − WrongFlip).
- Dependencies: pip-installable package; pytest smoke suite; Inspect AI adapter (registered in UKGovernmentBEIS/inspect_evals#1901); raw logs shipped for audit without rerunning APIs.
- Evaluation method: programmatic letter parser (last standalone A/B/C/D), cluster-bootstrap CIs over question IDs. No model judge required — fully compatible with WO §5.
- Limitations: MCQ-only (measures selection, not free-form capitulation); executing the full pipeline needs a subject model (API blocked here; a local model could run it with the Inspect adapter in a later milestone).
- **Reuse decision**: strongest reuse candidate of the five. Did not execute the benchmark this milestone (pilot-first per WO §8). Adopted its core axis — separating acceptance of valid corrections from capitulation to wrong pressure — as Test D's four conditions, and its raw-log preservation practice (our raw_results.jsonl preserves every prompt/response verbatim). No SycoBench items copied.

### 3. REL — relational complexity benchmark
- URL: project page https://zitniklab.hms.harvard.edu/REL/ (paper: arXiv:2604.12176; OpenReview 4oU82peL8f, **ICML 2026**); GitHub and HF links are published from the project page (repo LICENSE not fetched this session — verification status: **NOT_VERIFIED**)
- Contents: generative benchmark varying Relational Complexity (RC = minimum number of independent operands that must be bound simultaneously) across algebra (Raven-style numeric matrices), chemistry (molecular-family consistency, substructure, missing isomers), biology (homoplasy in phylogenies); interactive toy generators with adjustable parameters on the project page.
- Evaluation method: exact-match / set-recall scoring against generated ground truth — programmatic, no judge.
- Limitations: frontier-scale difficulty (even GPT-5.2/Claude Opus 4.5/Gemini 3 Pro degrade sharply at high RC; REL-B1 accuracies ~0.07–0.43 at 4–5 homoplastic taxa); full tasks far exceed a 0.5B local pilot subject; chemistry/biology items need domain parsing.
- **Reuse decision**: did not execute. Adopted the RC principle as Test A's "number of entities/relationships tracked" axis, including one deliberately higher-arity item (A18: bind 5 brothers × 3 sons). No REL items copied.

### 4. BIG-Bench `epistemic_reasoning`
- URL: https://github.com/google/BIG-bench → bigbench/benchmark_tasks/epistemic_reasoning
- Task verified present in the benchmark task index: "Determine whether one sentence entails the next"; keywords: common sense, json, logical reasoning, multiple choice, social reasoning, theory of mind.
- License: repository license is Apache-2.0 per repo documentation — **not re-verified byte-level this session** (recorded as CLAIM, not VERIFIED).
- Contents: JSON task, multiple-choice, beliefs/knowledge/assumption relationships between agents.
- Evaluation method: exact_str_match-style MCQ scoring — programmatic.
- Limitations: BIG-bench canary string means items may sit in training data of the subject model (contamination risk for a general-corpus 0.5B); MCQ format only.
- **Reuse decision**: did not execute. Design pattern (beliefs about beliefs) noted as a Test B extension for a later milestone. No items copied.

### 5. Vibesbench — conversational fluency / pragmatics
- URL: https://github.com/firasd/vibesbench
- License: **none declared** (no LICENSE file visible on the repository page as of 2026-10-21 → default all-rights-reserved; redistribution not permitted; reading/citation fine)
- Contents: curated multi-turn reference conversations with frontier models (Claude Opus 4.5/Sonnet 4.5, GPT-4o, Gemini 2.5 Pro), prompts and transcripts published; explicit qualitative stance — **no automated scoring and no synthetic judges by design** ("Any evaluation that does not preserve this data is not merely incomplete; it is methodologically unsound").
- Evaluation method: human reading of transcripts. No metrics.
- Limitations: cannot produce the WO's required quantitative measurements; frontier-capability assumption baked into prompts; unlicensed for reuse of material.
- **Reuse decision**: transcripts not reused. Two design influences adopted: (a) prompt/response pairs preserved as first-order evidence (matches our raw_results.jsonl policy); (b) its warning that phatic language is not automatically harmful is encoded in Test C ("do not automatically classify social language as harmful" — WO §2C).

## Bycatch (found during audit; not in WO list; recorded for completeness)
- `timfduffy/syco-bench` (MIT): four judge-scored tests (pickside, mirror, who-said, delusion); OpenRouter-dependent.
- Big-Big-SycoBench (arXiv:2610.15634): argument-discernment sycophancy on subjective scoring; 12 human annotators; code availability not checked.
- VibeSearchBench (MIT): agentic search benchmark — name collision only, not relevant to this WO.

## Aggregate reuse verdict
No benchmark was executed as-is this milestone. Blockers recorded per WO §6: API access (403), direct HF access (timeout), judge-model availability (no API), and GPU absence. All five projects nonetheless shaped the pilot design (documented per project above). The pilot's test items are all newly generated — no benchmark items were copied, so no license is exercised beyond reading; dataset reuse remains available for the next milestone (SycoBench-600 first, SYCON false-presupposition subset second, both programmatically scoreable).

# G2-frame-glyph-pilot -- first run against gap G2

Delivered 2026-10-20 as one upload, `G2_frame_glyph_pilot.zip`
(sha256 `73184ceb7fd751f46aef947fbf6f889c3c6867899868e1ebe4941328469596e8`,
computed at landing). Nine files extracted unchanged; this README is the
only file added. Gap: `../GAPS_2026-10-20.md` G2. Audit: `../../AUDIT_NOTES.md`
CPD_019.

```text
tag          co-authored | CC0 | stdlib-only
arm A        Qwen2.5-0.5B-Instruct answers, reused from the RPF-01 run
             (data/test_cases.jsonl and data/raw_results.jsonl are byte-identical
             to ../../okcomputer-regulatory-cost-bearer/rpf01/)
arm B        frame_glyph.py: rule extractor -> frame -> read count; no weights
held-out     data/heldout.jsonl, 12 items, stated as written after the code freeze
```

## Recomputed at landing (MECHANICAL, scratch copy, `python3 -I`)

```text
FROZEN.sha256             both code hashes verify; line 3 is a timestamp, not a hash
                          (sha256sum warns "improperly formatted"; harmless)
frame_glyph.py            selftest 7/7 PASS
run_g2.py                 output == out_all.json, exact
RPF-01 Test A (18)        glyph 18 CORRECT (12 OK_CONDITIONAL) | Qwen 4 CORRECT / 14 WRONG
held-out (12)             glyph 7 CORRECT / 0 WRONG / 5 MISSING (2 of 5 expected missing)
NOT verifiable            freeze BEFORE held-out: the timestamp is self-declared,
                          no history in the bundle; this commit dates it from landing on
```

Reproduce:

```sh
python3 run_g2.py data/test_cases.jsonl data/raw_results.jsonl data/heldout.jsonl
python3 frame_glyph.py
```

## Manifest (sha256, as landed)

```text
dc177dab8f1135faa5f9db38507ddd0d9129dc75c51cb7b39eb477080f185888  FROZEN.sha256
e2f6a7611df503dd3a29d0eeec4e59c05e1a0e2db38f3b3c0d60b8af8c248cef  RESULTS_G2_pilot.md
c79d92f4dca23b4d92c0bc0d61cbc7fdb04370a82495c880248c1d6ae5543ca8  data/heldout.jsonl
e6708a4ccf91c0eafeccbdefb7fca762d347641e61627e30db391394ee0f441f  data/raw_results.jsonl
79fde478522188d4835d90e3c2aaa800ffbb6a5df60476efc29a6e21283c6f82  data/test_cases.jsonl
5296d1583e44086dcb5ad4f6e6748788411433571ad68845fed527217e51bd63  frame_glyph.py
7eadb8f64fa82d3962ab05b13754c2a8962a36b66a3fa2ff1a28dd945061b8d3  out_all.json
e2a1617335714e9ce042f4baaa4b7f72b1153cbd58a69620cd82d4e9c6c4251c  run_g2.py
```

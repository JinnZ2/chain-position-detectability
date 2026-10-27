# G2 pilot: frame_glyph vs retraining-target failures

CC0 | stdlib-only | co-authored | Status: PILOT, run 2026-10-20 | Posture: reasoning tool, not verdict.

## What was run

```
ARM A  Qwen2.5-0.5B-Instruct, greedy, no tool      (RPF-01 raw_results.jsonl, Kimi run)
ARM B  frame_glyph.py: rule extractor -> glyph()   (deterministic, no weights touched)

item sets
  RPF-01 Test A   18 items (A01-A18)   extractor WRITTEN AGAINST these -> ceiling only
  held-out        12 items (H01-H12)   written AFTER code frozen (sha256 below)
```

Frozen before held-out: `frame_glyph.py 5296d158…bd63`, `run_g2.py e2a16173…251c` (2026-10-20T23:33Z).
Reproduce: `python3 run_g2.py data/test_cases.jsonl data/raw_results.jsonl data/heldout.jsonl`

## Results (OBSERVED)

```
                      CORRECT  WRONG  MISSING
RPF-01 A  Qwen 0.5B      4      14       -
RPF-01 A  glyph         18       0       0     (ceiling: extractor tuned on these)
held-out  glyph          7       0       5
            of MISSING:  2 correctly undetermined (H02 Sam, H11 Alex: sex unstated, load-bearing)
                         3 extractor coverage gaps (H03 mother frame, H08 parents' count,
                           H07 "Tom is Alice's brother" sentence shape)
```

Property that held on all 30 items: **zero confident wrong numbers.** The tool either read the
tree or said what was missing.

## Finding the benchmark didn't mark (OBSERVED)

12 of 18 RPF-01 items get their expected answer only if Alice/Maria is female, and the text never
says so: the sex comes from a name prior. The tool returns these as `OK_CONDITIONAL` with the
assumption named and the alternative count beside it (A01: 3 if Alice is F, 2 if not).
The items that state it (A10, A11, A14, A18 by "her"/"girls besides Alice") come back plain `OK`.
So the AIW item class has an undeclared dependency inside the gold answer itself.

## Mechanism notes (DERIVED)

- Edges stored once (parent -> child). Same graph walked backward in selftest: a nephew's aunts = 3.
  Reversal costs nothing (BOM / where-used).
- An OPEN attribute blocks only if it is on the read path: cousins (A09) and Tom's children (A10) did
  not block; Sam's sex (H02) did.
- Removal test built in: flip each assumed slot, re-read; if the count moves, the assumption is
  load-bearing and gets reported. A06 (Alice's own sisters) is not load-bearing, so it comes back `OK`.

## Limits (marked)

- The extractor is regex rules written by the same party who wrote the held-out items. Held-out tests
  generalization only within one author's phrasing.
- H04 came back correct by accident: "She" was matched as a name, then "her" declared the sex. Recorded, not fixed.
- Closed-world assumption is silent: undeclared children are read as none (H05 = 4). That is an
  unmarked fill by the tool itself; it should become a traced ASSUMED slot in v2.
- Arm A is a 0.5B model. This shows the readout layer is sound and extraction is the bottleneck;
  it does not yet show model+tool vs fine-tuned model (the G2 question).

## Branches

```
a) model + tool call beats fine-tune on fix rate, no collateral  -> harness path supported
b) tool correct but model fails to CALL it (no surface cue)       -> trigger is the bottleneck
c) model calls it but builds the spec wrong                       -> extraction is the bottleneck
d) fine-tune matches tool with no measured collateral             -> cost argument narrows to reuse
not measured != no effect
```

## Next

1. v2: closed-world fill becomes a traced ASSUMED slot; parent frame + named-member sentence shapes.
2. Model-built spec arm: give a model the JSON schema, let it fill the spec, run glyph(). Measures (c).
3. Trigger arm: deterministic harness trigger vs model-selected tool call on the same items. Measures (b).

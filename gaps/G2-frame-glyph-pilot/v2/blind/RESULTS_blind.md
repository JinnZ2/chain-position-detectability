# G2-HO: frozen frame_glyph v2 on blind held-out set (single run)

CC0 | co-authored | run 2026-10-20 | tool frame_glyph.py f048e9c1...d40b (= freeze commit af75f29)
items: heldout_blind.jsonl sha256 e1012c0b...0c8f, 40 items, written by another party without the code
reproduce: python3 run_g2.py data/test_cases.jsonl data/raw_results.jsonl heldout_blind.jsonl

## Result (OBSERVED, one run, not re-tuned)

```
                     n   CORRECT  WRONG  MISSING  all-branches
determinable        31      5       0      26         -
undetermined         9      -       0       9         0
total               40      5       0      35         0
```
CORRECT: X02 X04 X20 X30 X32 (all "X has N sisters and M brothers" + pronoun).
Zero confident wrong numbers held on blind items.
Undetermined items were declined (MISSING), not returned as branches: safe, less informative.

## Where it failed (OBSERVED)
35/35 MISSING are extractor sentence-shape misses ("no sibling-count sentence shape" 33,
"query relation not recognized" 2). None came from the glyph core.

## Reading (DERIVED)
- Branch (c) dominant: building the tree from prose is the bottleneck; a regex extractor
  does not transfer beyond its author's phrasing (5/31 vs 18/18 in-sample).
- The item set needs two slot types the core lacks: constraint/aggregate
  (X11 X12 X13 X35 X39: "each boy has two sisters", "twice as many") and
  inverse-count (X18 X29: nephews -> sons). Graph read alone covers the rest
  if the spec is built correctly.

## Branches for next arm
 a) model fills the JSON spec well -> extraction moves to the model; glyph core does the read
 b) model fills spec wrong          -> extraction is the bottleneck for models too
 c) constraint items fail even with good spec -> add constraint slot type
not measured != no effect

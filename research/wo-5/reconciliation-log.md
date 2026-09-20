# WO-5 hop-coding reconciliation record

**Author:** Manus AI
**Date:** 2026-09-19
**Status:** Complete reconciliation of the two supplied independent row-level coding files

## Conclusion

The immutable `N` key linked **5,969** raw effect-estimate rows to each independent coding file. The coders agreed on every row: raw agreement was **100.0000%** (5,969/5,969), with **0 disagreements**. Applying the preregistered codebook directly to the raw metadata reproduced the agreed code on every row. The reconciled dataset therefore contains **326 H1**, **1,197 H2**, and **4,446 HU** rows; H0 and H3 each have zero rows.

The ordinal weighted Cohen's kappa is **1.000000**. The calculation uses quadratic ordinal weights, \(w_{ij}=1-((i-j)/3)^2\), for H0--H3, with scores 0--3. HU is a separate non-ordinal category: HU/HU receives weight 1 and HU paired with any ordinal category receives weight 0. The observed weighted agreement was 1.000000 and the chance-expected weighted agreement was 0.617468. The weighted-kappa denominator was not degenerate because the marginals contain H1, H2, and HU; the ordinary weighted-kappa calculation is defined.

## Inputs and identity audit

The reconciliation used the immutable row identifier `N`; it did not infer correspondence from row position. All three inputs contained **5,969** rows with nonblank, unique `N` values. Coder A and Coder B each covered every raw `N` exactly once, with no extras, omissions, or order changes.

| Input | SHA-256 | Rows | `N` coverage and order |
|---|---|---:|---|
| Raw source data | `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c` | 5,969 | Complete and unique |
| Coder A | `9fcbb27b49169c3d7737f1306dc3dc80f8d5245369219534c41cef844c58a9d8` | 5,969 | Complete; same raw order |
| Coder B | `d9ca8227f6ed0aecf7b7abaf611a14d2333a7d7184b4b09c247e735496aa9a74` | 5,969 | Complete; same raw order |

## Field-by-field source and effect audit

Coder A retained all 28 raw source/effect fields. Coder B retained the eight source/effect fields in its independent-coding specification. Every retained field was compared as an exact string by `N` against the raw file. A zero means no row differed. An em dash means the field was not present in Coder B's deliberately narrower input record, not that it was omitted from the final CSV.

| Raw source/effect field | Coder A mismatches | Coder B mismatches |
|---|---:|---:|
| `N` | 0 | 0 |
| `Author` | 0 | 0 |
| `Year` | 0 | 0 |
| `Species` | 0 | — not retained by Coder B |
| `Genus` | 0 | — not retained by Coder B |
| `Family` | 0 | — not retained by Coder B |
| `F.H` | 0 | — not retained by Coder B |
| `Life.form` | 0 | — not retained by Coder B |
| `Sp.origin` | 0 | — not retained by Coder B |
| `Approach` | 0 | — not retained by Coder B |
| `Response` | 0 | — not retained by Coder B |
| `Phase1.m.ori` | 0 | 0 |
| `Phase1.m` | 0 | 0 |
| `Phase1.culti` | 0 | — not retained by Coder B |
| `Experimental.setting` | 0 | 0 |
| `SoilTp` | 0 | — not retained by Coder B |
| `Phase2.grow` | 0 | — not retained by Coder B |
| `Phase2.time` | 0 | — not retained by Coder B |
| `Source` | 0 | — not retained by Coder B |
| `rr` | 0 | 0 |
| `var` | 0 | 0 |
| `Latitude` | 0 | — not retained by Coder B |
| `Longitude` | 0 | — not retained by Coder B |
| `Latitude.abs` | 0 | — not retained by Coder B |
| `MAT` | 0 | — not retained by Coder B |
| `MAP` | 0 | — not retained by Coder B |
| `AI` | 0 | — not retained by Coder B |
| `group` | 0 | — not retained by Coder B |

The final CSV was read back after writing. It retains all 28 raw fields, preserves all values and raw order exactly, has a unique `N` on every row, and uses `csv.QUOTE_ALL` for its header and every data field.

## Coding-field audit

The coding fields were audited row by row rather than inferred from matching category totals. `hop_score`, `provenance_confidence`, decisive basis, inherited rule identifier, and coder identifier were checked against the corresponding coder's documented rule and the raw metadata. Coder A's and Coder B's decisive-basis strings intentionally differ in scope: B also records `Approach` and `F.H`; their exact strings were therefore checked against their own registered templates instead of incorrectly requiring literal equality.

| Audit check | Rows failing check |
|---|---:|
| hop_code, exact A-vs-B | 0 |
| A hop_score inconsistent with A code | 0 |
| B hop_score inconsistent with B code | 0 |
| A provenance_confidence inconsistent with code | 0 |
| B provenance_confidence inconsistent with code | 0 |
| A decisive_basis inconsistent with raw pattern | 0 |
| B decisive_basis inconsistent with raw pattern | 0 |
| A inherited_rule_id inconsistent with code | 0 |
| B inherited_rule_id inconsistent with raw pattern/code | 0 |
| A coder identifier not coder-a | 0 |
| B coder identifier not coder-b | 0 |
| Direct codebook reconciliation code differs from either coder | 0 |

## Agreement counts and confusion matrix

| Code | Coder A | Coder B | Final |
|---|---:|---:|---:|
| `H0` | 0 | 0 | 0 |
| `H1` | 326 | 326 | 326 |
| `H2` | 1197 | 1197 | 1197 |
| `H3` | 0 | 0 | 0 |
| `HU` | 4446 | 4446 | 4446 |
| **Total** | **5969** | **5969** | **5969** |

| Coder A \ Coder B | H0 | H1 | H2 | H3 | HU | Total |
|---|---:|---:|---:|---:|---:|---:|
| `H0` | 0 | 0 | 0 | 0 | 0 | 0 |
| `H1` | 0 | 326 | 0 | 0 | 0 | 326 |
| `H2` | 0 | 0 | 1197 | 0 | 0 | 1197 |
| `H3` | 0 | 0 | 0 | 0 | 0 | 0 |
| `HU` | 0 | 0 | 0 | 0 | 4446 | 4446 |
| **Total** | 0 | 326 | 1197 | 0 | 4446 | **5969** |

## Reconciliation rules and disagreement decisions

The reconciliation applied the codebook's location-and-provenance requirements to every raw row. Field conditioning (`F.H=Field`, `Phase1.m.ori=Field`, and `Phase1.m=Field`) plus an experimental feedback contrast and field response setting was retained as H1. The same direct field-conditioning evidence with a greenhouse response setting was retained as H2. No H0 code was made because these are experimental feedback contrasts, not documentation of an ambient lived-in contrast. No H3 code was made because controlled history was never established. All other patterns were retained as HU: a greenhouse venue or numeric duration does not, by itself, establish either physical field-to-controlled relocation or controlled/laboratory history.

| Final inherited rule ID | Final code | Confidence | Rows | Decision basis |
|---|---|---|---:|---|
| `RECON-H1-FIELD-CONDITIONING-FIELD-FEEDBACK` | H1 | High | 326 | Direct field conditioning and field feedback response; experimental contrast rules out H0. |
| `RECON-H2-FIELD-CONDITIONING-GREENHOUSE-FEEDBACK` | H2 | High | 1197 | Direct field conditioning followed by greenhouse feedback establishes H2 relocation. |
| `RECON-HU-INSUFFICIENT-PROVENANCE` | HU | Low | 4446 | Metadata do not uniquely establish relocation or controlled history. |

There were no row-level code disagreements to adjudicate. The complete disagreement-decision register is therefore:

| N | Coder A | Coder B | Final code | Decision |
|---:|---|---|---|---|
| *None* | — | — | — | No row-level disagreement occurred. |

## Final artifact

The reconciled, fully quoted CSV is [`analysis/hop-coded-effects.csv`](analysis/hop-coded-effects.csv). It has **5969** data rows and **35** columns: all 28 original source/effect fields followed by `hop_code`, `hop_score`, `provenance_confidence`, `decisive_basis`, `inherited_rule_id`, `coder_a_code`, and `coder_b_code`. Its SHA-256 is `77dc735fa425abd96329acbc55a99c6403f7da77b947f3b1cc7d61a9ec612480`.

## Limitations

The agreement is strong only for the information available in the supplied synthesis metadata. It does not resolve the biological provenance of the **4,446** unresolved rows. In particular, a greenhouse label and a numeric phase duration do not establish whether the organisms were field-origin (which could support H2) or had controlled history (which could support H3). The reconciliation preserves HU for those rows, as required by the codebook, rather than manufacturing ordinal information. The positive H1 and H2 rules are inherited metadata rules; repeated effect rows from the same study can share the same rule and are not independent studies for downstream inference.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"
[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/evidence/coder-a-method.md "Coder A methods record: WO-5 plant–soil-feedback hop coding"
[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/evidence/coder-b-method.md "WO-5 Plant–Soil Feedback Coding: Coder B Methods Record"

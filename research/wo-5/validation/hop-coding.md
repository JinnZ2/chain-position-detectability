# Independent validation of WO-5 reconciled hop coding

**Author:** Manus AI
**Validation date:** 19 September 2026
**Scope:** `analysis/hop-coded-effects.csv` versus the immutable raw CSV and the WO-5 codebook

## Verdict: data and rule validation pass, with documented provenance and formatting limitations

The reconciled file is **valid for the requested data-integrity and rule-application checks**. It preserves a one-to-one, ordered set of 5,969 raw records; preserves every raw value after CSV parsing; contains only finite `rr` values and finite, strictly positive `var` values; and implements the documented H1, H2, and HU reconciliation rules exactly. The row and source-study counts, reported coder agreement, and custom weighted-kappa calculation all reproduce exactly.

No final H0 or H3 assignment exists. In particular, the 4,164 greenhouse-setting records whose history is unresolved and the 282 field-setting records whose conditioning direction is unresolved remain HU. Thus the output does not use venue alone to create an H0 or H3 classification, as the codebook requires.[1]

There are **no data-content or coding-rule errors**. The discrepancy register records five minor but material audit limitations: nonsemantic CSV reserialization, wording drift in the H2 decisive-basis text, incomplete standalone provenance in Coder B's narrow file, insufficient version-control history to independently establish timing, and absent evidence that can independently demonstrate blinded coding.

## Inputs and integrity basis

| Artifact | Local path | Data rows | SHA-256 verified against its record |
|---|---|---:|---|
| Immutable raw input | `analysis/raw-source-data/PSF.data.EL.open.csv` | 5,969 | Yes: `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c` |
| Reconciled output | `analysis/hop-coded-effects.csv` | 5,969 | Yes: `77dc735fa425abd96329acbc55a99c6403f7da77b947f3b1cc7d61a9ec612480` |
| Coder A output | `evidence/coder-a.csv` | 5,969 | Yes: `9fcbb27b49169c3d7737f1306dc3dc80f8d5245369219534c41cef844c58a9d8` |
| Coder B output | `evidence/coder-b.csv` | 5,969 | Yes: `d9ca8227f6ed0aecf7b7abaf611a14d2333a7d7184b4b09c247e735496aa9a74` |

The raw file is mode `0444`, as declared in the source manifest. It parses as 28 fields and 5,969 data rows. The final file parses as the same 28 fields, in the same order, followed by the seven expected coding fields: `hop_code`, `hop_score`, `provenance_confidence`, `decisive_basis`, `inherited_rule_id`, `coder_a_code`, and `coder_b_code`.

## Identity, value, and numeric audit

All four CSVs were parsed with a standards-compliant CSV parser. The comparison used `N`, not row position, to establish identity. The final file has a nonblank, unique `N` in every record; its `N` set equals the raw set exactly; and its `N` sequence is in the same order as the raw file. Coder A and Coder B also each have complete, unique, and ordered coverage of the raw `N` values.

The field-preservation test compared the UTF-8 bytes of each **parsed** string. This is deliberately stricter than a numeric comparison and avoids mistaking a formatting-normalized value for an unchanged value. Every one of the 28 raw fields matched in all 5,969 final records. The requested fields are summarized below.

| Raw field(s) | Parsed UTF-8 byte mismatches, raw versus final |
|---|---:|
| `Author` | 0 |
| `Year` | 0 |
| `Phase1.m.ori`, `Phase1.m`, `Phase1.culti`, `Phase2.grow`, `Phase2.time` | 0 in each field |
| `rr` | 0 |
| `var` | 0 |
| All 28 retained raw fields | 0 |

Every raw and final `rr` parsed to a finite floating-point value: **5,969 of 5,969** passed. Every raw and final `var` parsed to a finite value greater than zero: **5,969 of 5,969** passed. There were no blank `N`, `Author`, `Year`, applicable phase-field, `rr`, or `var` values in this audit.

## Exact rule audit

The codebook defines H1 as a field or semi-natural response under an imposed or observed field condition, H2 as field-origin biological material moved to a controlled setting, and HU as the required result when the metadata do not uniquely establish the design path. It specifically prohibits treating missing provenance as H3 and distinguishes biological relocation from merely measuring a response in a laboratory.[1]

I independently implemented the final reconciliation's stated rules against the raw metadata. The positive rules required an experimental feedback contrast (`Approach` equal to `Self-Other` or `Self-Sterilized`), `F.H=Field`, `Phase1.m.ori=Field`, and `Phase1.m=Field`. An `Experimental.setting` of `Field` required H1; an `Experimental.setting` of `Greenhouse` required H2. Every other observed raw pattern required HU. The final code, score, confidence, and reconciliation rule identifier were then compared row by row to this independently derived result.

| Expected reconciliation result | Required raw condition | Expected final fields | Rows expected | Rule failures |
|---|---|---|---:|---:|
| H1 | Experimental contrast; `F.H`, `Phase1.m.ori`, and `Phase1.m` all `Field`; response setting `Field` | `H1`; score `1`; `high`; `RECON-H1-FIELD-CONDITIONING-FIELD-FEEDBACK` | 326 | 0 |
| H2 | Same direct field-conditioning conditions; response setting `Greenhouse` | `H2`; score `2`; `high`; `RECON-H2-FIELD-CONDITIONING-GREENHOUSE-FEEDBACK` | 1,197 | 0 |
| HU | Every remaining pattern | `HU`; blank score; `low`; `RECON-HU-INSUFFICIENT-PROVENANCE` | 4,446 | 0 |

All 4,446 HU records fall within Coder B's stated two residual patterns: 4,164 have `F.H=Greenhouse`, `Phase1.m=Greenhouse`, greenhouse experimental setting, and a finite numeric `Phase1.m.ori`; the remaining 282 have `F.H=Field`, `Phase1.m=Greenhouse`, field experimental setting, and a finite numeric `Phase1.m.ori`. No HU record fell outside that declared four-rule partition. This confirms both that the reconciled rule was exhaustively applied to the present raw data and that the unresolved patterns were not converted to ordinal scores.

### H0/H3 venue-only safeguard

The final file has **zero H0** and **zero H3** records. The direct venue-only safeguard is therefore satisfied in the output: 4,164 rows with a greenhouse response setting are HU rather than H3, and 282 rows with a field response setting but unresolved conditioning direction are HU rather than H0 or H1. This verifies the result of the rule application. It cannot, from CSV artifacts alone, prove the unobservable intent or independence of the human coders.

## Counts and coder-agreement claims

The following counts reproduce the reconciliation record and both coder-method records. A source study is the documented distinct `(Author, Year)` pair; category-specific study counts are nonadditive because a study may contribute records in more than one category.

| Hop code | Final effect rows | Distinct `(Author, Year)` source studies | Documented claim reproduced |
|---|---:|---:|---|
| H0 | 0 | 0 | Yes |
| H1 | 326 | 23 | Yes |
| H2 | 1,197 | 91 | Yes |
| H3 | 0 | 0 | Yes |
| HU | 4,446 | 99 | Yes |
| **Total** | **5,969** | **202** | **Yes** |

Coder A and Coder B supplied the same hop code on **5,969 of 5,969 rows**, for raw agreement of **100.0000%** and zero disagreements. The final `hop_code`, `coder_a_code`, and `coder_b_code` are all equal to the corresponding independent-coder code on every row.

I also reproduced the reconciliation record's specified weighted Cohen's kappa: quadratic ordinal weights across H0–H3, score distance divided by three, with HU/HU weighted one and HU paired with an ordinal category weighted zero. Observed weighted agreement is **1.000000**; expected weighted agreement is **0.6174675989**, which rounds to the reported **0.617468**; and weighted kappa is **1.000000**. The reported agreement statistics are therefore numerically correct for the stated weighting convention.

## Discrepancy and limitation register

| ID | Finding | Classification | Consequence |
|---|---|---|---|
| D1 | The final file does **not** preserve the raw file's physical serialization: raw uses unquoted headers/ordinary fields and CRLF line endings, while final quotes every field and uses LF line endings. The final file is 3,609,838 bytes versus 1,609,518 bytes raw. | Minor, intentional formatting difference | Parsed values are byte-identical UTF-8 strings and the final full-quoting claim is correct. This is not a content loss, but “byte preservation” must mean parsed cell values, not an identical CSV byte stream. |
| D2 | In all 1,197 H2 records, the final `decisive_basis` says “establishes relocation to a controlled setting (H2),” whereas the reconciliation table describes the basis as “establishes H2 relocation.” | Minor documentation wording drift | The two statements are semantically consistent and the raw metadata, code, score, confidence, and rule ID all agree. The basis text is not a literal copy of the reconciliation-table wording. |
| D3 | Coder B's method says `F.H` and `Approach` informed its decisions, but its deliberately narrow independent CSV does not retain either field. Its `decisive_basis` repeats their values, and the raw/final files allow validation of those values. | Provenance limitation | Coder B's standalone CSV cannot itself substantiate the complete five-field decision provenance. The final dataset does retain the needed raw fields; no final rule failure resulted. |
| D4 | At the validation snapshot, the raw input, final CSV, coder CSVs, reconciliation log, and source manifest are untracked by Git. The codebook has one preregistration commit (`3564d68ab9218ba1569f8e404d0c5dd3d68a3d90`, 2026-09-19 23:02:06 UTC), but the untracked downstream artifacts have no repository history. | Provenance limitation | Current hashes match the documents, but Git history cannot independently demonstrate the relative timing of corpus discovery, coding, reconciliation, or the claimed preregistration condition for these current files. |
| D5 | The files demonstrate identical coder outputs and correctly calculated agreement, but include no timestamps, blinded assignment record, or independent work log. | Evidentiary limitation | The numerical claim of perfect agreement is verified. The stronger statement that the two coders worked independently cannot be independently authenticated from these artifacts alone. |

## Conclusion

The reconciled WO-5 hop-coded dataset passes the requested **N-preservation, parsed-value preservation, numeric-integrity, deterministic rule, count, and agreement-statistic validations**. The dataset has no observed coding or data-integrity error, and its all-HU treatment of unresolved venue/provenance patterns respects the codebook's explicit safeguards.

The remaining issues are limited to audit provenance and nonsemantic serialization. Any downstream report should describe the agreement result as a verified equality of the two supplied coding outputs, while avoiding a stronger independently verified claim that the coding was blind or temporally independent. It should also preserve the current checksums and resolve the untracked-artifact status if a durable preregistration and chain-of-custody record is required.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"
[2]: https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35 "Dataset of global plant-soil feedback"
[3]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

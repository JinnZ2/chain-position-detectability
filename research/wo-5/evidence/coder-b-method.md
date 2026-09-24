# WO-5 Plant–Soil Feedback Coding: Coder B Methods Record

## Result and scope

Coder B independently coded all **5,969** effect-estimate rows in the assigned plant–soil-feedback CSV. This record applies the preregistered WO-5 hop definitions, including the requirement that field venue alone must not be used to infer either a naturally lived-in response (`H0`) or controlled history (`H3`). The raw input is the assigned `PSF.data.EL.open.csv` file [2]. The decision rules below operationalize the WO-5 ecology carry-test codebook [1]. No other coder record was consulted.

The completed coding contains **326 H1**, **1,197 H2**, and **4,446 HU** rows. It contains **0 H0** and **0 H3** rows. `other` therefore equals **0** (`H0 + H3`). The data identify **202 distinct source studies**, defined as distinct `(Author, Year)` primary-study citation pairs. Category-specific source-study counts are not additive because a primary study can contribute effect estimates to more than one category.

## Inputs, unit, and identity

The coding unit is one existing effect-estimate row. The output preserves the input row order and the exact original strings for `N`, `Author`, `Year`, `Phase1.m.ori`, `Phase1.m`, `Experimental.setting`, `rr`, and `var`. `N` is unique and is the row-level key. `(Author, Year)` is retained as the source-study identity for clustered downstream analysis, consistent with the codebook's instruction to retain study identity when several estimates come from one study [1].

The raw fields used to determine the design path were `F.H`, `Phase1.m.ori`, `Phase1.m`, `Experimental.setting`, and `Approach`. `Approach` was used only to confirm that the contrast was an experimental plant–soil-feedback contrast (`Self-Other` or `Self-Sterilized`). It is not duplicated as an output column because the requested output field set specifies the retained fields above. The decisive basis column records the field values used for each row.

## Conservative rule set

The codebook defines `H1` as an observed or manipulated field response, `H2` as field-origin biological material moved to a controlled setting, `H3` as controlled-history/lab-only, and `HU` as unresolved [1]. The assignment below uses only metadata patterns that identify both the conditioning direction and the feedback setting. The ordinal score is blank for `HU`, because unresolved rows do not have a defensible 0–3 score.

| Inherited rule ID | Required metadata pattern | Decision and confidence | Effect rows | Distinct source studies |
|---|---|---:|---:|---:|
| `B-H1-001` | `Approach` is `Self-Other` or `Self-Sterilized`; `F.H=Field`; `Phase1.m.ori=Field`; `Phase1.m=Field`; `Experimental.setting=Field` | `H1`; score `1`; high | 326 | 23 |
| `B-H2-002` | `Approach` is `Self-Other` or `Self-Sterilized`; `F.H=Field`; `Phase1.m.ori=Field`; `Phase1.m=Field`; `Experimental.setting=Greenhouse` | `H2`; score `2`; high | 1,197 | 91 |
| `B-HU-003` | `F.H=Greenhouse`; `Phase1.m=Greenhouse`; `Experimental.setting=Greenhouse`; `Phase1.m.ori` is a finite numeric duration | `HU`; score blank; low | 4,164 | 97 |
| `B-HU-004` | `F.H=Field`; `Phase1.m=Greenhouse`; `Experimental.setting=Field`; `Phase1.m.ori` is a finite numeric duration | `HU`; score blank; low | 282 | 3 |

The first rule uses field labels for both conditioning and feedback setting and an explicit feedback contrast. It is therefore an experimental field response (`H1`). It is **not** `H0`: the raw field venue does not establish an ambient, naturally occurring contrast, and the `Approach` field identifies an experimental feedback comparison.

The second rule explicitly identifies field conditioning followed by a greenhouse feedback measurement. This is the codebook's physical-relocation case (`H2`) rather than a mere laboratory measurement after an in-situ response.

The third rule is deliberately unresolved. A greenhouse phase and a numeric phase duration do not document whether organisms first originated from the field, which would be necessary to establish `H2`, or had controlled/laboratory history, which would be necessary to establish `H3`. Greenhouse venue alone therefore supplies neither inference. This implements the codebook's instruction that missing provenance is `HU`, not `H3` [1].

The fourth rule is also deliberately unresolved. Although the feedback setting is recorded as field, its greenhouse phase and numeric phase-duration metadata do not establish a field-conditioned feedback experiment. Because the supplied phase direction cannot be uniquely reconstructed, this pattern is not called `H1` from the feedback venue alone.

## Category and source-study counts

| Hop code | Hop score | Effect rows | Share of all rows | Distinct source studies |
|---|---:|---:|---:|---:|
| `H0` | 0 | 0 | 0.00% | 0 |
| `H1` | 1 | 326 | 5.46% | 23 |
| `H2` | 2 | 1,197 | 20.05% | 91 |
| `H3` | 3 | 0 | 0.00% | 0 |
| `HU` | blank | 4,446 | 74.48% | 99 |
| **Total** | — | **5,969** | **100.00%** | **202** |

## Ambiguities and exclusions from positive hop assignment

The **4,446** `HU` rows are the principal evidentiary limitation. Most have greenhouse labels and numeric `Phase1.m.ori` values that describe a greenhouse phase duration, but the supplied metadata do not identify prior organism provenance or controlled rearing history. A second unresolved pattern places a greenhouse phase before a field feedback setting but does not support an unambiguous phase direction or field conditioning. Neither pattern is upgraded to `H2` on a presumed field origin or to `H3` on a presumed controlled history. The latter is also not upgraded to `H1` merely because feedback is listed as field. Their blank `hop_score` prevents an unjustified ordinal placement.

The **326** field-to-field rows support `H1` because the conditioning fields, feedback setting, and experimental approach all agree. They still do not establish `H0`, because a field setting is not evidence that the contrast was ambient or naturally occurring. Similarly, no row was assigned `H3` from a greenhouse label; controlled history was never documented by the supplied metadata. No residual metadata pattern occurred outside the four rules in the table, so no fallback rule was applied.

## Validation and file integrity

Before coding, the raw CSV was checked for unique nonblank `N`, finite `rr`, and finite positive `var`. After writing, the output was read back with a CSV parser and checked for the requested header order, complete row count, unique `N`, original row order, and exact string equality of all eight retained original fields. All **5,969** rows passed. There were **0** non-finite `rr` values and **0** non-finite or non-positive `var` values. Every row has a hop code, provenance confidence, decisive basis, inherited rule ID, and coder value; only `HU` has an intentionally blank `hop_score`. The CSV writer uses `QUOTE_ALL`, so every header and data value is quoted.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/analysis/raw-source-data/PSF.data.EL.open.csv "WO-5 assigned PSF open source data"

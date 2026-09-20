# WO-5 candidate-corpus audit: HIREC behavioural responses

**Candidate ID:** `hirec-behavioural-responses`
**Audit finding:** **Eligible; external-replication candidate, not selected.** Direct inspection of the public Dryad release finds **381 usable effect rows** and **90 source-study labels**. The release has a complete, finite adjusted Hedges’ *g* outcome and a complete, strictly positive Hedges’ *g* variance for every row. Its README documents the row-level `Form`, `Type`, and `Study_type` metadata needed for a conservative audit screen. That screen reproduces the prior structured values: **provisional `H1` = 23** field-experimental rows and **provisional `H2` = 238** wild-sample laboratory rows. The literal screening score is therefore **9 / 11**: seven base data/traceability/setting points plus two populated provisional categories. **Eligibility is true** at this candidate-audit stage.[1]

This result is deliberately narrower than a completed primary-study coding data set. `H1` and `H2` below are **metadata-supported provisional codes**, not reconciled final codes. The codebook requires two independent coders, decisive source evidence, and reconciliation; automatic or field-string coding alone cannot be the final coding evidence. The 120 effects outside the two scored screens are not promoted to `H0` or `H3` merely from the available labels. That restraint preserves the previously applied score and deterministic selection tie-break.[1]

## Scope and primary synthesis

The associated article is Gunn, Hartley, Algar, Niemelä, and Keith, **“Understanding behavioural responses to human-induced rapid environmental change: a meta-analysis,”** published in *Oikos* as article e08366. The publisher identifies it as the version of record published online on 15 September 2021 and in the April 2022 issue; Dryad records it as the dataset's primary article. These records establish the required peer-reviewed ecological synthesis association.[2] [3]

The article reports that the quantitative synthesis contains **381 data points from 90 studies**, after screening 1,023 records. It further says that the curators recorded laboratory/field setting, wild/captive population, and observational/experimental design for the included papers. Direct data inspection exactly reproduces the 381-row and 90-source totals rather than relying only on that narrative.[2]

## Public files inspected and reproducibility record

Dryad version 7 is public, carries a 23 September 2021 publication date, and is licensed CC0. Its public file inventory lists exactly the two files below. I downloaded and read both through the record's normal public file links; the computed SHA-256 for `MA_data.rda` agrees with Dryad's recorded digest.[3] [4]

| Public artifact | Exact filename | Repository size and SHA-256 | Direct inspection finding |
|---|---|---:|---|
| Effect-size data | `MA_data.rda` | 31,400 bytes; `5f99c9f8aa89b790cdbd0af2f69150b0766400d91b443c038f42bb01be9ffff4` | RData object `MA_data`: **381 rows × 28 columns**. |
| Documentation | `Readme_MA.txt` | 2,845 bytes; `49190226289470512d4ed76f53182bdd91faac40cf791440e333e936c4b56d16` | Read in full. It defines the source IDs, `Form`, `Type`, `Study_type`, effect-size, variance, and sample-size fields used here. |
| Analysis code linked by Dryad | `Behavioural_responses_meta_analysis_code.R` at Zenodo record 5226879 | 120,142 bytes; Zenodo MD5 `e020ed7a9a313ad998f266a49a24b467` | Inspected as a consistency check. It starts from `MA_data`, models `AdjustedES`, and supplies `Vg` to `MCMCglmm` as measurement-error variance. |
| Preregistered instrument | `research/wo-5/ecology-codebook.md`, repository commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90` | n/a | Read and applied literally for eligibility, score, hop definitions, and tie-breaking.[1] |

The released table's exact header is:

```text
ID, unique_ID, Ref, Group, Env., Behaviour, Measure, animal, Type, Form,
Study_type, Study_form, sample_code, NControl, NImpact, Ntotal, d, Vd, SEd,
J, WeightedES, AdjustedES, Vg, Ivg, SE, w, IVW, SE2
```

## Direct evidence for usable effects, uncertainty, setting, and traceability

The README defines `ID` as the paper-reference number and `unique_ID` as the data-point number; it says that repeated values from one paper share its `ID`. It defines `Ref` as author–year paper reference, `Type` as whether the animal sample was wild or captive, `Form` as whether the study was laboratory or field, and `Study_type` as whether it was experimental or observational. It documents `WeightedES` as Hedges’ *g*, `AdjustedES` as the adjusted Hedges’ value, and `Vg` as Hedges’ *g* variance.[5]

The released software establishes which of the two Hedges’ *g* columns is the synthesis outcome: it assigns `MODEL_FULL <- MA_data` and fits models with `AdjustedES` as the response and `Vg` as the measurement-error variance. `AdjustedES` and `WeightedES` differ in 44 rows, so the outcome should not be silently substituted in a downstream reanalysis. The paper similarly states that it calculated bias-corrected Hedges’ *g*, calculated associated variance, and reversed latency-coded signs where necessary to make a positive value consistently mean increased behavioural expression.[2] [6]

| Requirement | Released fields and direct count | Audit finding |
|---|---|---|
| Public machine-readable data | Public `MA_data.rda`, one rectangular R data frame with 381 rows and 28 columns. | **Yes** |
| Effect estimate | `AdjustedES` is finite for **381 / 381** rows (range −9.915217255 to 13.183670790); `WeightedES` is also finite in all rows. | **Yes** |
| Sampling variance / uncertainty | `Vg` is finite and strictly positive for **381 / 381** rows (range 0.002459789 to 2.402624429). `SE2` equals `Vg` row-for-row. | **Yes** |
| Usable effect count | Finite `AdjustedES` plus finite `Vg > 0`: **381** rows. | **Yes; 381 ≥ 80** |
| Source-study identifier | `ID` and `Ref` are complete, with **90** distinct values apiece; `unique_ID` is complete and unique from 1 through 381. | **Yes, subject to preserved linkage anomalies below** |
| Traceable primary-study citation | Complete `Ref` provides 90 author–year labels, and `ID`/`unique_ID` retain paper and row locators. | **Yes, but a full citation/DOI crosswalk is absent** |
| Explicit experimental-setting metadata | `Form`, `Type`, and `Study_type` are complete for every row and defined in the README. | **Yes** |

The source-study count is therefore **90**, not 91: numeric `ID` values run from 1 through 91 but **52 is absent**, yielding 90 distinct values. This agrees with the paper's stated 90 studies. It is not appropriate to renumber the table or manufacture a replacement ID.[2] [5]

## Preserved ID–reference anomalies

The two source keys have the same overall cardinality (90) but are not a one-to-one crosswalk. These are real release features and are retained exactly; neither the effect total nor the 90-source tie-break input has been altered.

| Anomaly type | Preserved release values | Consequence |
|---|---|---|
| One `ID` carries two `Ref` labels | `14`: Bozinovic et al. 2016 and 2017; `20`: Chivers et al. 2014 and Ferrari et al. 2011; `26`: De la Haye et al. 2011 and Dias et al. 2011 | `ID` alone is not a fully reliable primary-paper key. |
| One `Ref` occurs under two `ID`s | Chivers et al. 2014: 19 and 20; De la Haye et al. 2011: 26 and 49; Dias et al. 2011: 26 and 27 | `Ref` alone is also not a fully reliable independent-source key. |
| Nonconsecutive numeric IDs | `ID = 52` is absent; the observed range is 1–91 | Do not infer 91 source studies or reindex source IDs. |

A final analysis must publish a repaired, cited source crosswalk and retain the original `ID`, `Ref`, and `unique_ID` columns. Until then, it should cluster conservatively by a reconciled primary-paper identity rather than assume either raw key is uniquely correct.

## Metadata distribution and provisional hop screen

All 381 effects are usable under the mechanical outcome/variance screen. The direct setting/provenance distribution is **108 field** and **273 laboratory** effects; `Type` is **341 wild** and **40 captive**; `Study_type` is **281 experimental** and **100 observational**. The full three-way cross-tab is shown because the distinction is decisive for the audit.

| `Form` | `Type` | `Study_type` | Usable effects |
|---|---|---|---:|
| Field | Captive | Experimental | 5 |
| Field | Wild | Experimental | 18 |
| Field | Wild | Observational | 85 |
| Laboratory | Captive | Experimental | 35 |
| Laboratory | Wild | Experimental | 223 |
| Laboratory | Wild | Observational | 15 |
| **Total** |  |  | **381** |

The codebook defines `H1` as a field or semi-natural setting with a researcher-imposed treatment and response measured in situ. It defines `H2` as field-origin organisms or material moved to a controlled setting before focal exposure or response measurement. It expressly says that missing provenance must not be relabelled `H3`, and that a final coding decision needs decisive metadata or primary-study evidence.[1]

The following is a **metadata-supported availability screen**. It preserves the previously structured `H1 = 23` and `H2 = 238` values. It does not claim that primary-study methods have been independently coded and reconciled for every source.

| Code / audit status | Exact release rule | Usable effects | Distinct raw `ID` labels | Interpretation and coding status |
|---|---|---:|---:|---|
| **`H1` provisional** | `Form = Field` and `Study_type = _experimental` | **23** | **11** | Field setting plus an experimental design is direct release metadata for a manipulated field screen. The 5 captive and 18 wild rows remain in this provisional group because the field response-setting metadata is explicit; final coding must verify the field/semi-natural method. |
| **`H2` provisional** | `Form = Lab` and `Type = Wild` | **238** | **46** | The README documents a wild animal sample and laboratory study setting. This supports the field-origin-to-controlled-setting screen provisionally, including 223 experimental and 15 observational rows; primary methods must verify movement timing and focal exposure/response. |
| `H0` not awarded | `Form = Field`, `Type = Wild`, `Study_type = _observation` | 85 | 27 | These rows are plausible candidates, but the available row metadata do not state enough about the naturally occurring exposure/contrast and in-situ focal response to complete literal `H0` coding. No `H0` point is awarded. |
| `H3` not awarded | `Form = Lab`, `Type = Captive` | 35 | 12 raw IDs; 11 `Ref` labels | A captive label and laboratory venue do not by themselves establish the codebook's required controlled-history evidence. No `H3` point is awarded. |
| `HU` pending primary coding | Effects outside the two scored provisional screens | **120** | not additive | Default unresolved pool for a completed codebook data set: 85 field/wild observational candidates plus 35 laboratory/captive candidates. |

`H1` and `H2` are disjoint by construction and each clears the required ten-effect minimum. The reported H1/H2 category-source counts are descriptive screen counts, not a replacement for the global 90-study count or a finished crosswalk; category counts must not be summed because source identifiers require reconciliation. The provisional screen demonstrates that the release has metadata capable of distinguishing at least two threshold-clearing categories, which is the corpus-eligibility question. It does **not** satisfy the later analysis-stage requirement for independently coded, reconciled hop assignments.[1]

## Literal eligibility and score

The codebook requires a peer-reviewed ecological synthesis with public study-level effects (or reconstructable effects), uncertainty or sample-size information, source-study identity, metadata capable of two hop categories, at least 80 usable effects, and at least ten effects in each of two categories after coding. On the public-data availability evidence examined here, this candidate passes. The category points are narrowly limited to the two values already supported by the README-defined fields; no unverified `H0` or `H3` point is added.[1]

| Scored criterion | Points | Literal audit evidence |
|---|---:|---|
| Public machine-readable data | 1 | Public RData table downloaded from Dryad and parsed successfully. |
| Effect estimate | 1 | Complete finite `AdjustedES`; release documents Hedges’ *g* fields. |
| Sampling variance or reconstructable uncertainty | 1 | Complete finite, positive `Vg` in all 381 rows. |
| Source-study identifier | 1 | Complete `ID`, `Ref`, and unique `unique_ID`; 90 source labels, with the linkage defects explicitly retained. |
| Traceable primary-study citation | 1 | Complete author–year `Ref` labels are retained for all rows, though no full reference/DOI crosswalk is supplied. |
| At least 80 usable estimates | 1 | 381 finite-effect / positive-variance rows. |
| Explicit experimental-setting field | 1 | Complete README-defined `Form`, `Type`, and `Study_type`. |
| Populated `H1` category | 1 | 23 metadata-screened field-experimental effects. |
| Populated `H2` category | 1 | 238 metadata-screened wild-sample laboratory effects. |
| Additional populated categories | 0 | `H0` and `H3` remain unawarded without primary-method confirmation. |
| **Total** | **9 / 11** | Seven base points plus two threshold-clearing provisional categories. |

**Eligibility: true.** The public corpus meets the peer-review, accessibility, effect/variance, source identity, traceability, effect-count, setting-metadata, and two-category availability requirements at the audit stage. Its eligibility should not be misrepresented as completed dual-coder primary-study classification.[1]

## Selection consequence: tie-break preserved

No deterministic selection decision is changed by this repair. The existing selection record reports three eligible 9/11 candidates and applies the first prespecified tie-break—more independent source studies. The selected plant–soil microbe corpus has 202 source-study labels, the plant-functional-trait corpus has 99, and this HIREC corpus has **90**. Because 202 exceeds 99 and 90, the HIREC corpus remains an **eligible external-replication candidate, not the selected corpus**. Category balance and public-release date are not reached; they must not be retroactively invoked.[1] [7]

## Limits before any primary analysis

1. **Complete the required primary-study coding.** For each inherited coding group, two independent coders should record the decisive methods passage, provenance confidence, primary citation, and all `unique_ID` rows. Reconcile against primary-study methods; if the evidence cannot uniquely identify a hop category, retain `HU`.[1]

2. **Do not elevate the 85 field/wild observational effects to `H0` automatically.** Observation, wild sample, and field location are useful screening metadata but do not themselves document every literal `H0` condition. Confirm exposure/contrast and where the focal response occurred from methods text.

3. **Do not elevate all 35 laboratory/captive effects to `H3`.** Laboratory venue is not controlled-history evidence under the codebook. Likewise, the 238 lab/wild `H2` assignments are properly described as provisional until primary methods establish the required relocation timing.

4. **Repair the primary-source crosswalk without overwriting raw keys.** The non-one-to-one `ID`/`Ref` links can otherwise inflate or split source clusters. Add title, journal, DOI/URL, reconciled-source ID, and the retained original labels before inference.

5. **Retain the released outcome choice.** The supplied code models `AdjustedES` with `Vg`, whereas `WeightedES` differs in 44 rows. A reanalysis should state any use of a different column and justify it rather than silently treating the two as interchangeable.[6]

6. **The current categories only support the categorical fallback.** At this stage, only two hop categories are threshold-clearing. The codebook's ordinal trend model requires at least three categories with at least ten effects and five independent sources each; that condition has not been shown.[1]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook (pinned preregistration)"

[2]: https://nsojournals.onlinelibrary.wiley.com/doi/10.1111/oik.08366 "Gunn et al. — Understanding behavioural responses to human-induced rapid environmental change: a meta-analysis"

[3]: https://datadryad.org/dataset/doi:10.5061/dryad.hx3ffbgfb "Dryad dataset record — Understanding behavioural responses to human-induced rapid environmental change: A meta-analysis"

[4]: https://datadryad.org/api/v2/versions/141635/files "Dryad public file inventory for version 141635"

[5]: https://datadryad.org/downloads/file_stream/1036298 "Readme_MA.txt — metadata for MA_data"

[6]: https://zenodo.org/records/5226879 "Gunn et al. — Behavioural responses meta-analysis analysis code"

[7]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/corpus-selection.md "WO-5 corpus selection and deterministic tie-break record"

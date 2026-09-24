# WO-5 candidate-corpus audit: artificial light at night impacts

**Candidate ID:** `artificial-light-at-night-impacts`
**Historical audit outcome preserved:** **Ineligible; not recommended; 7 / 11.** The public Dryad release is a strong, machine-readable meta-analytic source. Its checksum-verified CSV contains **1,304 extracted comparison records from 126 `Study` labels**, and the supplied R code selects **1,109 `Delete = Keep` records from 117 `Study` labels** for the reported subcategory analyses. The release provides raw group means, standard deviations, and sample sizes from which Hedges-type standardized effects and sampling variances are reconstructed. It also has a complete `Field.Lab` setting field: **770 Field and 534 Laboratory records** in the complete extract; **697 Field and 412 Laboratory records** in the synthesis-selected subset.

Those venue labels do **not** uniquely establish the WO-5 hop categories. In particular, `Field` does not say whether the focal organisms remained in a naturally occurring population/community, whether the ALAN contrast was ambient or researcher-imposed, or whether the focal response was measured in situ; it therefore cannot uniquely distinguish `H0` from `H1`. `Laboratory` does not state whether material was field-origin and moved before exposure/response (`H2`) or had controlled/laboratory history (`H3`). The CSV has no provenance/history field and the supplied R script contains no such coding. The codebook prohibits a final category based only on an automated/string rule and requires independent coding with a decisive metadata field or primary-study passage; ambiguous evidence remains `HU`.[1]

Accordingly, this report **does not retroactively convert setting labels into scored hop categories**. It preserves the published workflow result: **two qualifying categories were not verified at the audit stage**, so the candidate was discarded before deterministic ranking. The score remains **7 / 11**, rather than an imputed 8 or 9, and eligibility remains **false**. This is a conservative audit disposition, not a claim that a primary-study coding exercise could not later demonstrate qualifying categories.

## Scope, paper, and inspected public release

Sanders, Frago, Kehoe, Patterson, and Gaston's *Nature Ecology & Evolution* article, **“A meta-analysis of biological impacts of artificial light at night,”** is the associated peer-reviewed ecological synthesis (volume 5, pages 74–81; online publication 2 November 2020; issue date January 2021). The publisher records received and accepted dates of 7 September 2019 and 28 August 2020, respectively.[2] [3] Its data-availability and code-availability statements both point to Dryad version 4, DOI `10.5061/dryad.wpzgmsbjn`.[2]

The Dryad record describes a systematic review that screened 614 publications and included experiments conducted in the field or laboratory. It reports **126 papers** and **1,304 effect-size measures**, matching the raw CSV total reproduced below.[4] The release is public, CC0-licensed, and contains two files. Dryad's version API identifies the record as public version 4 and supplies both SHA-256 fixity values.[5]

| Public artifact | Directly inspected file and fixity result | Audit use |
|---|---|---|
| Effect-data table | `Sanders_et_al_datafile.csv`; 584,000 bytes; local SHA-256 `d11d1e29c05826f2b4a5c1c2d63b9c195dc2effbedd1ff531afa7b6bdf497693`, equal to Dryad's published digest. The comma-delimited table has **1,304 records × 30 columns**. | Counts, raw effect-size inputs, study identity, setting screen, and source traceability. |
| Analysis code | `Sanders_meta__rcode.r`; 22,958 bytes; local SHA-256 `2dfa3f8a84eb779510a5b5798c13262f36bc4123d3a9c2d6ea23bd4c79aebd7f`, equal to Dryad's published digest. The script has 276 lines. | Confirms the reconstruction rule, the `Delete` subset, and clustering by `Study`. |
| Preregistered instrument | `research/wo-5/ecology-codebook.md`, repository commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90`. | Literal eligibility, scoring, and `H0`–`H3`/`HU` rules.[1] |

The CSV uses a legacy single-byte text encoding, but its delimiter and numeric fields parse unambiguously. This audit used a byte-preserving decode for counts and did not alter source values. The source table has no immutable unique row key: `ID` is complete but has **1,296 distinct values** over 1,304 rows. `Study`, `Title`, and `Author` are complete and each have **126 distinct values**. `DOI` is complete in 1,292 rows and missing in 12, but title/author/year metadata make the source studies traceable. The release's row order plus `Study`, `ID`, `Field.Lab`, and outcome metadata should be retained when assigning any new coding ID.

## Effect estimates, uncertainty, and source-study identity

The public CSV supplies **inputs** rather than precomputed `yi` and `vi` columns. This nevertheless satisfies the codebook's “effect estimate or enough data to reconstruct [one]” and “sampling variance or reconstructable uncertainty” requirements.[1] The actual released R script first assigns the 1,304-row table to `ALANdat1`, then selects `Delete = Keep`, and computes standardized effects with:

> `escalc(measure= "SMDH", n1i = Experimental_N, n2i = Control_N, m1i = Experimental_Mean, m2i = Control_Mean, sd1i = Experimental_SD, sd2i = Control_SD, data = ALANdat, append = TRUE)`

It then reverses `yi` where `Sign = -1` and fits models with `Study` as a random effect. Thus the intended retained metric is zero-centred, signed Hedges-type standardized mean difference `yi` with sampling variance `vi`; `Study` is retained for non-independence.[6]

All 1,304 raw rows have finite numerical group means, standard deviations, and sample sizes. Both sample-size fields are strictly positive in every row: `Control_N` ranges from 2 to 440 and `Experimental_N` from 2 to 3,114. Eighteen rows have a zero standard deviation in one arm, but none has zero standard deviations in both arms. This is a reproducibility caution requiring an explicit `metafor::escalc` output check before final modelling, not a reason to treat the release as lacking reconstructable uncertainty. In every case, the supplied script—not an undocumented transformation—states the intended calculation.[6]

Direct inspection also resolves an otherwise easy count ambiguity. The CSV's `Delete` field is complete: **1,109 `Keep`** and **195 `Delete`**. The R script comments that its subset has 1,109 observations but inaccurately says “198 removed”; the actual data establish 1,304 − 195 = **1,109**. The script's `Keep` subset is therefore the defensible count for synthesis-selected analyses, while 1,304 is the released extraction corpus and the source of the Dryad methods' stated total.[4] [6]

| Requirement | Exact direct evidence | Result |
|---|---|---|
| Public machine-readable data | Public standard CSV, downloaded and checksum-matched to Dryad's version inventory. | **Yes** |
| Effect estimate | `SMDH` effect is reconstructable from complete `Experimental_*`/`Control_*` mean, SD, and N fields; `Sign` is complete. | **Yes** |
| Sampling variance / uncertainty | The same complete fields feed `escalc`, which appends `vi`; all sample sizes are positive. | **Yes** |
| At least 80 usable estimates | 1,109 analysis-selected `Keep` records, far above 80; 1,304 raw extracted records are also retained in the release. | **Yes** |
| Source-study identifier | Complete `Study`, 126 values in the raw extract and 117 in the `Keep` subset; code uses `Study` as a random effect. | **Yes** |
| Traceable primary-study citation | Complete `Title`, `Author`, `Publication.year`, and largely complete DOI fields. | **Yes, with a DOI-completeness limitation** |
| Explicit experimental-setting field | Complete `Field.Lab`, with exactly two values. | **Yes** |

## Reproduced rows, studies, and setting frequencies

The table below reports both denominators rather than silently substituting one for the other. The **raw extract** is the 1,304-row table described by Dryad and used for the historic 126-study candidate inventory. The **analysis-selected subset** is the 1,109-row `Delete = Keep` data frame used by the delivered R code. Four raw `Study` labels appear under both settings; three do in the selected subset. For that reason, field-study and laboratory-study counts do not sum to the distinct-study total.

| CSV subset | Effect-record rows | Distinct `Study` labels | `Field` rows (source studies) | `Laboratory` rows (source studies) | Field/laboratory overlap in `Study` labels |
|---|---:|---:|---:|---:|---:|
| Complete released extraction | **1,304** | **126** | **770** (82) | **534** (48) | 4 |
| R-script `Delete = Keep` subset | **1,109** | **117** | **697** (77) | **412** (43) | 3 |
| `Delete = Delete` records | **195** | **36** | **73** (19) | **122** (17) | 1 |

The raw setting count independently reproduces the repository's total: 770 + 534 = 1,304. The selected setting count also reconciles exactly: 697 + 412 = 1,109. The raw 126-study total matches the Dryad methods statement. Although the candidate inventory and preserved selection record use the broader **126-source-study** count, any analysis following the released script must cluster the retained rows by its **117** `Study` labels, not treat the 1,109 rows as independent studies.[4] [6]

## Literal hop-category assessment

`Field.Lab` is an **experimental-venue descriptor**, not a completed hop code. It is valuable because it makes a primary-method coding project feasible and supplies an explicit setting field for the base score. It is not enough to award category points by itself under the actual codebook.

The codebook defines `H0` as naturally occurring population/community, ambient/naturally occurring exposure, and in-situ response; `H1` as field/semi-natural conditions with an imposed treatment or apparatus and in-situ response; `H2` as field-origin material moved to a controlled setting before focal exposure or response; and `H3` as controlled/laboratory history with exposure and response under controlled conditions. It explicitly requires `HU` when the public metadata and accessible source do not support a unique category. It further forbids final coding based solely on an automated string rule and requires two independent coders, a decisive passage/field, and reconciliation.[1]

The inspected columns are `Study`, bibliographic fields, `Field.Lab`, biological outcomes, raw effect inputs, taxonomy, and geographic `Location`/latitude/longitude. They do **not** record focal-organism provenance, prior rearing/culture history, relocation timing, whether the ALAN contrast was ambient versus experimentally installed, or the response-measurement site. Neither the CSV nor the R script supplies a codebook category. Therefore the venue counts below are an auditable **screen**, but no cell is a verified hop-category count.

| Status after this audit | Raw records | Raw source studies | Evidence and reason for treatment |
|---|---:|---:|---|
| `Field.Lab = Field` — candidate rows, **not final H0/H1** | **770** | **82** | `Field` establishes venue only. Primary methods must determine naturally occurring versus manipulated exposure and confirm whether the response occurred in situ. |
| `Field.Lab = Laboratory` — candidate rows, **not final H2/H3** | **534** | **48** | `Laboratory` establishes venue only. Primary methods must determine whether field-origin organisms/material were moved (`H2`) or had controlled history (`H3`). |
| Confirmed `H0` | **0** | **0** | No decisive source-method coding completed. |
| Confirmed `H1` | **0** | **0** | No decisive source-method coding completed. |
| Confirmed `H2` | **0** | **0** | No decisive source-method coding completed. |
| Confirmed `H3` | **0** | **0** | No decisive source-method coding completed. |
| `HU` pending primary-study coding | **1,304** | **126** | The current public file-level evidence cannot allocate a unique hop code to individual records or design groups. |

This table should not be read as evidence that all 1,304 records will ultimately be unresolved. It records the **historical audit state** required for the deterministic selection: no two codebook categories were verified to contain at least ten effects. In particular, coding all field rows as `H1` or all laboratory rows as `H3` would violate the codebook. `H3` requires supported controlled history; missing provenance is `HU`.[1]

## Preserved eligibility and scoring decision

The codebook awards one point for each of seven base data/traceability/setting conditions, plus one point for each populated hop category, up to four.[1] The first seven conditions are directly demonstrated. No hop-category point is awarded because the audit did not establish any category through the required source-method coding. This is why the score is **7 / 11**, exactly as retained in the corpus-selection record; it must not be recomputed upward merely because the venue split is now documented.[7]

| Scored criterion | Points | Literal audit evidence |
|---|---:|---|
| Public machine-readable data | 1 | Public, checksum-verified Dryad CSV. |
| Effect estimate | 1 | Hedges-type standardized effect reconstructable by supplied `escalc(measure = "SMDH")` code. |
| Sampling variance or reconstructable uncertainty | 1 | Complete group SD and N inputs reconstruct the script's `vi`. |
| Source-study identifier | 1 | Complete `Study`; 126 raw labels and 117 in the script-selected subset. |
| Traceable primary-study citation | 1 | Complete titles/authors/years and DOI in 1,292 of 1,304 rows. |
| At least 80 usable effects | 1 | 1,109 analysis-selected records; 1,304 raw records. |
| Explicit experimental-setting field | 1 | Complete `Field.Lab` with Field/Laboratory values. |
| Populated `H0`, `H1`, `H2`, or `H3` categories | 0 | No final hop code verified by independent, decisive primary-source evidence. |
| **Total** | **7 / 11** | Seven base points; zero verified hop-category points. |

**Eligibility: false.** The candidate meets the public-data, effect/uncertainty, source, traceability, sample-size, and setting-field conditions, but it fails the minimum category condition at this audit stage. The codebook requires at least ten effects in **each of two categories after coding**, and requires metadata capable of distinguishing categories. The available file-level setting labels do not satisfy that final coding standard.[1]

**Recommendation: false.** The corpus is a useful conditional replication prospect, but it was properly discarded before the deterministic ranking because its required two-category verification had not been performed. The selection record's winning corpus and ranking are unchanged.[7]

## What further primary-study coding would be required

A future reassessment must be a documented coding project, not a relabelling exercise. First, create a 126-study citation crosswalk using `Study`, `Title`, `Author`, `Publication.year`, and DOI, resolving the 12 DOI-missing rows. Because four studies contain both venue labels, define coding groups at the **study × design/setting** level rather than inheriting a single source-wide code. Assign an immutable derived row key (for example, source-file row order plus `Study` and `ID`) because the released `ID` field is not unique.

Second, two independent coders should examine the primary methods for each relevant design group and record the decisive quoted passage, location in the paper, provenance confidence, coding-group identifier, and all inherited row keys. For **field-labelled** records, the minimum evidence must establish whether organisms remained in a naturally occurring population/community; whether ALAN was ambient/naturally occurring (`H0`) or imposed by researchers (`H1`); and whether the response was measured in situ. A field venue by itself is not enough.

For **laboratory-labelled** records, coders must establish the organism/material history before focal exposure and response. Evidence that field-collected organisms, propagules, communities, or biological material were moved to the laboratory before the focal exposure or response supports `H2`. Evidence of controlled/laboratory rearing or culture history, with exposure and response under controlled conditions, supports `H3`. If methods do not resolve that distinction, the final code must remain `HU`; laboratory venue must never be substituted for controlled history.[1]

Finally, reconcile disagreements against the primary source and publish raw agreement, weighted Cohen's kappa, the reconciliation log, and the row-to-group inheritance map. Only then count effects and distinct source studies by final category. If at least two verified categories each contain ten effects, the candidate can be reconsidered under the codebook; if three categories each contain ten effects and five independent studies, the ordinal model condition may also be evaluated. That subsequent evidence could support an **external-replication** analysis, but it cannot revise the already executed deterministic selection.

## Limitations and reproducibility notes

1. **The CSV has data sufficient to reconstruct effects, not stored effect/variance columns.** The audit therefore relies on the exact delivered `metafor::escalc` rule. Re-run that script or an equivalently version-pinned calculation and retain its derived `yi`/`vi` table before any meta-regression.[6]

2. **The analysis-code comment has a deletion-count error.** The code comment says 198 records were removed, whereas the actual CSV says 195. The auditable `Delete` values, rather than the comment, define the 1,109-row analysis subset.

3. **The released code's MCMC settings differ from Dryad's narrative methods.** The record describes 150,000 iterations, 50 thinning, and 50,000 burn-in; the inspected script sets `nitt = 15000`, `burnin = 5000`, and `thin = 5`. This does not alter corpus eligibility, but prevents treating the delivered script as a fully specified reproduction of every narrative-analysis setting.[4] [6]

4. **Venue is not provenance.** The setting field is complete and scientifically useful, but it does not document the decisive distinctions demanded for `H0`/`H1` or `H2`/`H3`. No score or eligibility point can be created from an assumption about organism history.[1]

5. **Rows are not independent studies.** The raw extract has 1,304 rows from 126 study labels; the R-script subset has 1,109 from 117. Any future model must cluster by the verified source-study identifier and preserve within-study dependency.[1] [6]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook (pinned preregistration)"

[2]: https://www.nature.com/articles/s41559-020-01322-x "Sanders et al. — A meta-analysis of biological impacts of artificial light at night"

[3]: https://api.crossref.org/works/10.1038/s41559-020-01322-x "Crossref work record for A meta-analysis of biological impacts of artificial light at night"

[4]: https://datadryad.org/dataset/doi:10.5061/dryad.wpzgmsbjn "Dryad dataset record — A meta-analysis of biological impacts of artificial light at night, version 4"

[5]: https://datadryad.org/api/v2/versions/78428/files "Dryad API file inventory for public version 78428"

[6]: https://datadryad.org/api/v2/files/399141/download "Released R analysis script — Sanders_meta__rcode.r"

[7]: ../corpus-selection.md "WO-5 corpus selection — preserved published candidate scores and deterministic disposition"

[8]: https://datadryad.org/api/v2/files/399142/download "Released effect-data table — Sanders_et_al_datafile.csv"

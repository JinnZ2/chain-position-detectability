# WO-5 candidate-corpus audit: global plant–soil microbe interactions

**Candidate ID:** `global-plant-soil-microbe-interactions`
**Audit finding:** **Eligible and recommended.** The public Dryad release contains **5,969 usable study-level log-response-ratio effects**, every one with a finite positive sampling variance, and represents **202 distinct `Author` source-study values**. Its two phase-specific setting fields directly support at least two codebook categories above the required minimum: **326 `H1` field-conditioning / field-feedback estimates** and **1,197 `H2` field-conditioned / greenhouse-feedback estimates**. The literal published score is **9 / 11**: seven data/traceability/setting points plus `H1` and `H2`; no points are awarded for `H0` or `H3`.

This is a strict inspection result. It does **not** relabel all greenhouse data as `H2` or `H3`. The **4,164** greenhouse-conditioning / greenhouse-feedback rows lack an origin/history field that uniquely distinguishes field-origin relocation (`H2`) from controlled-history work (`H3`), so they remain `HU` pending primary-method coding. That restraint does not affect eligibility because the two directly evidenced categories are already much larger than ten estimates each.[1]

## Scope and primary paper

The supplied paper DOI resolves to Jiang et al., **“Global patterns and drivers of plant–soil microbe interactions,”** published as a *Synthesis* in *Ecology Letters* 27, e14364 (2024). The publisher record reports **Received 13 September 2023**, **Revised 20 November 2023**, **Accepted 1 December 2023**, and an editor, Thulani Makhalanyane. Those editorial milestones support the required **peer-reviewed** status.[7] [8]

The paper reports that the compilation covers “**5969 observations of PSF from 202 studies**.” Its study-selection section says the final total was “**202 papers and 5969 observations of 669 species**,” after literature searching, screening, and author contact where needed.[7] Direct file inspection independently reproduces the 5,969-row total and 202 unique source-study labels below; the claims here therefore do not rest only on the repository or article description.

## Public files inspected and reproducibility record

The audit downloaded the public Dryad version through the repository's version API without credentials. The version is public, dated **18 December 2023**, and the API lists three files. The listed SHA-256 digests are repository-supplied fixity metadata.[2] [3]

| Public artifact | Exact filename | Size and SHA-256 listed by Dryad | Direct inspection result |
|---|---|---:|---|
| Effect-size data | `PSF.data.EL.open.csv` | 1,609,518 bytes; `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c` | Parsed as a comma-separated table with **5,969 rows × 28 columns**. All rows have numeric finite `rr` and strictly positive finite `var`. |
| Documentation | `README.md` | 1,508 bytes; `1aeac2d8f58027687422a1336aaa4b9ca6f82cc5c357f6e92fc50db52ad2484b` | Read in full. It defines the effect, variance, source, and phase/setting columns quoted below. |
| Analysis script | `Open_code.R` | 32,984 bytes; `16cd8520a2072592070822db4d72ebce1db483b4cedca8f2797d855c52b5e2bd` | Read in full. It reads this CSV, uses `rr` and `var` in `metafor::rma.mv` models, and fits phase/experimental-setting moderators. |
| Preregistered codebook | `research/wo-5/ecology-codebook.md` at repository commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90` | n/a | Read to apply its eligibility, score, and `H0`–`H3`/`HU` rules literally.[1] |

The full CSV header is:

```text
N,Author,Year,Species,Genus,Family,F.H,Life.form,Sp.origin,Approach,
Response,Phase1.m.ori,Phase1.m,Phase1.culti,Experimental.setting,SoilTp,
Phase2.grow,Phase2.time,Source,rr,var,Latitude,Longitude,Latitude.abs,
MAT,MAP,AI,group
```

The release's row ID is strong: `N` is nonmissing and unique for all 5,969 rows, with a minimum of 1 and maximum of 5,969. It makes inherited coding and an eventual reconciliation log feasible without inventing row identifiers.

## Direct file evidence for effect estimates, uncertainty, setting, and source identity

`README.md` explicitly defines:

> “**F.H: Experimental environments (field vs. greenhouse)**”; “**Phase1.m: environment during conditioning phase (field vs. greenhouse)**”; and “**Experimental.setting: Experimental setting during feedback phase**.”[5]

> “**Source: Sources for this observation.**”; “**rr: Log effect size**”; and “**var: Variance of effect size**.”[5]

These are descriptions from the inspected release file, not inferences from the landing-page summary. The paper independently describes the same design split: it says that, for the conditioning phase, the team recorded “the experimental environment (field or greenhouse),” and for the response phase recorded “the experimental environment (field or greenhouse)” among other moderators.[7]

The `rr` and `var` fields have an intelligible native estimand. The paper states that it calculated individual plant–soil feedback as a **log response ratio** and then “calculated the variance of the effect size to weight the effect sizes” in meta-analysis.[7] The supplied R script is consistent with that account: it reads `PSF.data.EL.open.csv` (line 11), calculates `rr <- log(Mean_con/Mean_else)` and a sampling-variance expression (lines 14–15), and passes `rr, var` to multilevel `rma.mv` models (for example lines 73, 84–90).[6]

| Requirement | Fields inspected and exact result | Finding |
|---|---|---|
| Machine-readable public data | Public, downloadable `PSF.data.EL.open.csv`; standard CSV; 5,969 × 28. | **Yes** |
| Effect estimate | `rr` is nonmissing and finite in **5,969 / 5,969** rows; range **−5.235428278 to 4.555408676**. | **Yes** |
| Sampling variance / uncertainty | `var` is nonmissing, finite, and strictly positive in **5,969 / 5,969** rows; range **0.0000441 to 3.125**. | **Yes** |
| Usable effect count | `rr` finite **and** `var > 0`: **5,969** rows. No row is excluded by this mechanical usability screen. | **Yes; 5,969 ≥ 80** |
| Source-study identifier | `Author` is complete and has **202** distinct normalized values; `Year` is complete. The R script includes `Author` as a random-effect grouping variable and in its `Site.sp` construction.[6] | **Yes** |
| Extraction locator | `Source` is complete. It has 64 raw literal strings and **61** values after trimming whitespace; values name figures, tables, or appendices, such as `Figure 2`, `Figure 5`, and `Figure S1`. | **Yes, as within-study extraction trace** |
| Primary-study traceability | Complete `Author` + `Year` values identify the 202 source groups; some labels add journal disambiguators, e.g., `Reinhart et al. 2005a Ecography`. Sample resolution is successful: that field label corresponds to Reinhart, Greene, and Callaway's 2005 *Ecography* record, while `Nijjer et al. 2007` resolves to a 2007 *Proceedings of the Royal Society B* record.[9] [10] | **Yes, with a citation-crosswalk limitation** |
| Explicit setting metadata | `F.H`, `Phase1.m`, and `Experimental.setting` are all complete (5,969 nonmissing values each). | **Yes** |

The first three data records illustrate the actual rows rather than a repository description. `N = 1` is `Packer and Clay 2004`, `Phase1.m = Field`, `Experimental.setting = Greenhouse`, `Source = Figure 2`, `rr = 0.036701367`, and `var = 0.002084691`. `N = 2` and `N = 3` are `Reinhart et al. 2005a Ecography`, with both phase fields `Field`, `Source = Figure 5`, and finite `rr`/`var`. Thus the category counts below arise from explicit row fields, not from title or abstract keyword matching.

## Counts and setting distribution

All selected columns in this table are complete: `Author`, `Year`, `F.H`, `Phase1.m`, `Experimental.setting`, `Source`, `rr`, and `var` each have **0 missing values**. `F.H` contains 1,805 `Field` and 4,164 `Greenhouse` values. The analysis-script comment independently records `Field vs. house: 1805 vs. 4164 rows`, providing a reproducibility cross-check.[6]

The phase-specific cross-tab is more useful than `F.H` for hop coding because it preserves the conditioning and feedback phases separately. Every cell consists of usable `rr`/positive-`var` effects.

| Conditioning environment: `Phase1.m` | Feedback environment: `Experimental.setting = Field` | Feedback environment: `Experimental.setting = Greenhouse` | Row total |
|---|---:|---:|---:|
| `Field` | **326** | **1,197** | 1,523 |
| `Greenhouse` | **282** | **4,164** | 4,446 |
| Column total | **608** | **5,361** | **5,969** |

The four `group` values, which combine life form with the release's high-level setting grouping, are `Nonwoody Field` (1,129), `Nonwoody Greenhouse` (4,012), `Woody Field` (676), and `Woody Greenhouse` (152). They are useful descriptive checks but are not used as the decisive hop fields because `Phase1.m` and `Experimental.setting` are more granular and explicitly phase-specific.

## Literal WO-5 hop assessment

The preregistration defines **`H1`** as focal organisms under field or semi-natural conditions where researchers impose a treatment or apparatus and measure the response in situ. It defines **`H2`** as organisms, propagules, communities, or biological material that originate in the field and are moved to a controlled setting before focal exposure or response measurement. It further states: “**Greenhouses and common gardens are `H2` for field-origin organisms**,” while missing provenance must be `HU`, not `H3`.[1]

Plant–soil feedback estimates are experimental contrasts, rather than ambient observation-only effects: the paper's inclusion criterion requires comparison of a species grown in conspecific-conditioned soil with heterospecific-conditioned or sterilized soil.[7] Consequently, field feedback-phase rows are `H1`, not `H0`. The directly observed phase combinations provide the following **metadata-based, auditable category screen**.

| Code / status | Exact qualifying field rule | Usable estimates | Distinct `Author` source studies | Why it is or is not scoreable now |
|---|---|---:|---:|---|
| **`H1`** | `Phase1.m = Field` **and** `Experimental.setting = Field` | **326** | **23** | Both conditioning and response/feedback phases are recorded as field, and the PSF contrast is experimentally imposed. This is direct metadata evidence of manipulated field feedback. |
| **`H2`** | `Phase1.m = Field` **and** `Experimental.setting = Greenhouse` | **1,197** | **91** | The soil/biological conditioning phase occurred in the field and the feedback response was measured in a greenhouse: direct evidence of field-origin biological material moved to a controlled setting. This is precisely the codebook's field-origin greenhouse rule. |
| `HU` pending primary-method coding | `Phase1.m = Greenhouse` and `Experimental.setting = Greenhouse` | **4,164** | **97** | Greenhouse-only phase metadata do not establish whether material originated in the field (`H2`) or had controlled history (`H3`). No point awarded. |
| `HU` pending primary-method coding | `Phase1.m = Greenhouse` and `Experimental.setting = Field` | **282** | **3** | The feedback response is field-based, but the public row metadata do not uniquely state the relevant organism/material history for a final code. These rows are not used in the conservative `H1` score and should be individually confirmed during final coding. |
| `H0` | None confirmed | 0 | 0 | The synthesis's experimental PSF contrast does not support ambient/no-treatment `H0` coding. |
| `H3` | None confirmed | 0 | 0 | No controlled-history field supports `H3`; greenhouse alone is insufficient under the codebook. |

The codebook requires independent coding, a decisive metadata field or primary-study passage, and reconciliation against primary sources where ambiguity remains.[1] This audit therefore calls the two threshold categories **plausibly and strongly available**, not a finished dual-coder coding dataset. The `H1` and `H2` rules use the README-defined phase-environment fields directly. The final analysis should retain a coding record that cites these field values and, for sample/source groups, primary-study methods passages. The exact `N` row IDs make that feasible.

The minimum category-count test passes even at this conservative audit stage: **`H1 = 326`** and **`H2 = 1,197`**, each far beyond ten. `H1` and `H2` are disjoint under the stated rules. Their source counts (23 and 91) also exceed the codebook's five-independent-study-per-category condition; however, only two categories are presently confirmed, so the codebook's three-category ordinal meta-regression condition is not yet demonstrated. A categorical model across eligible categories would be the stated fallback.[1]

## Literal eligibility and score

The codebook requires a peer-reviewed ecological synthesis, publicly downloadable study-level effects or reconstructable effects, uncertainty, source-study identity, public metadata that can distinguish at least two categories, at least 80 usable estimates, and ten estimates in each of two categories.[1] All conditions are met at this audit's available evidence level. The score below makes no award from a repository description alone: every positive data/metadata point depends on the inspected files described above.

| Scored criterion | Points | Literal evidence |
|---|---:|---|
| Public machine-readable data | 1 | Downloaded and parsed `PSF.data.EL.open.csv` from the public Dryad release. |
| Effect estimate | 1 | Complete numeric `rr`, documented as log effect size. |
| Sampling variance or reconstructable uncertainty | 1 | Complete, finite, strictly positive `var`, documented as variance of effect size. |
| Source-study identifier | 1 | Complete `Author` field; 202 distinct normalized values, with complete `Year` and extraction locator `Source`. |
| Traceable primary-study citation | 1 | Complete author–year source labels, including disambiguating journal text where needed, are traceable to primary records; see verified examples.[9] [10] |
| At least 80 usable estimates | 1 | 5,969 finite-`rr` / positive-`var` effects. |
| Explicit experimental-setting field | 1 | Complete `F.H`, `Phase1.m`, and `Experimental.setting` fields defined in the inspected README. |
| Populated `H1` category | 1 | 326 field-conditioning / field-feedback estimates from 23 source studies. |
| Populated `H2` category | 1 | 1,197 field-conditioning / greenhouse-feedback estimates from 91 source studies. |
| Additional populated categories | 0 | No `H0`/`H3` point; greenhouse-only data remain `HU` without origin/history confirmation. |
| **Total** | **9 / 11** | Seven base points plus two populated, threshold-clearing categories. |

**Eligibility: true.** The corpus satisfies the public-access, peer-review, effect/uncertainty, traceability, sample-size, setting-field, and two-category minimum conditions.

**Recommended: true.** This is a genuinely strong primary-corpus candidate: it combines an exceptionally large complete effect-size table, explicit variance, 202 source-study groups, phase-specific field/greenhouse metadata, and two category screens with hundreds to more than a thousand effects. Its limitations are material for final coding and inference but do not invalidate the literal eligibility decision.

## Critical limits and required next steps

1. **Do not promote greenhouse-only rows to `H2` or `H3`.** `Phase1.m = Greenhouse` and `Experimental.setting = Greenhouse` show venue but not whether organisms/material were field-derived or had a controlled history. The codebook makes missing provenance `HU`; no category point was awarded for the 4,164 such rows.[1]

2. **Complete independent coding remains required before analysis.** The codebook requires two coders, provenance confidence, a decisive source passage or metadata field, and a reconciliation log. Use the phase fields as the initial decisive metadata for `H1`/`H2`; then retain `N`, `Author`, `Year`, `Source`, and inherited-row group IDs for auditability. The present report verifies availability and threshold plausibility; it is not a substitute for the preregistered coding workflow.[1]

3. **Primary-study citation linkage is adequate but not a complete crosswalk.** The release has `Author` and `Year`, and often journal disambiguation, but does not provide a dedicated source-ID-to-title/DOI bibliography table. `Source` identifies the figure/table/appendix used for extraction, not the article itself. Build and publish a 202-source citation crosswalk (full reference, DOI/URL, and matched `Author` label) before source-level inference.

4. **The supplied script is not fully rerunnable from the released CSV alone.** `Open_code.R` recalculates `rr` from `Mean_con`/`Mean_else` and variance from `SD_*`/`N_*` fields, but these raw mean/SD/sample-size columns are not in the released 28-column CSV. The directly supplied `rr` and `var` remain fully usable and documented, so this is a reproducibility limitation rather than an effect-size or uncertainty failure. It prevents an independent reconstruction of the supplied values from raw inputs.[6]

5. **Source clustering is essential.** Multiple effects arise from each of the 202 source studies. The final random-effects analysis must retain `Author` (or a validated derived source ID) for clustered inference as required by the codebook; it must not treat 5,969 rows as independent studies.[1]

6. **Only two categories are established at present.** The codebook's ordinal trend model requires at least three categories with ten effects and five independent sources each. This corpus clearly supports the categorical fallback now. Further primary-method coding may establish a third category, but must not be assumed.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook (pinned preregistration)"

[2]: https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35 "Dryad dataset record — Dataset of global plant-soil feedback"

[3]: https://datadryad.org/api/v2/versions/269740/files "Dryad API file inventory for public version 269740"

[4]: https://datadryad.org/api/v2/files/2789266/download "Dryad download endpoint — PSF.data.EL.open.csv"

[5]: https://datadryad.org/api/v2/files/2789270/download "Dryad download endpoint — README.md"

[6]: https://datadryad.org/api/v2/files/2789265/download "Dryad download endpoint — Open_code.R"

[7]: https://onlinelibrary.wiley.com/doi/10.1111/ele.14364 "Jiang et al. — Global patterns and drivers of plant–soil microbe interactions"

[8]: https://api.crossref.org/works/10.1111/ele.14364 "Crossref work record for Jiang et al., Ecology Letters 27:e14364"

[9]: https://api.crossref.org/works/10.1111/j.2005.0906-7590.04166.x "Crossref work record — Effects of Acer platanoides invasion on understory plant communities and tree regeneration in the northern Rocky Mountains"

[10]: https://api.crossref.org/works/10.1098/rspb.2007.0804 "Crossref work record — Negative plant–soil feedbacks may limit persistence of an invasive tree due to rapid accumulation of soil pathogens"

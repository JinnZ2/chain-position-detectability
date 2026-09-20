# WO-5 corpus selection

**Decision date:** 19 September 2026
**Selected corpus:** `global-plant-soil-microbe-interactions`
**Selected paper:** Jiang, F., Bennett, J. A., Crawford, K. M., *et al.* (2024), “[Global patterns and drivers of plant–soil microbe interactions](https://doi.org/10.1111/ele.14364),” *Ecology Letters*, 27, e14364.
**Selected primary dataset:** “[Dataset of global plant-soil feedback](https://doi.org/10.5061/dryad.n2z34tn35),” Dryad, public version 6 (published 18 December 2023).

## Deterministic decision

The preregistered rule requires discarding ineligible candidates, selecting the remaining corpus with the highest published score, and breaking any score tie first by the greater effective number of independent source studies, then category balance, and finally the earlier stable public release. No audit score has been changed in this selection decision.[1]

Two candidates were ineligible and were removed before comparison. Three candidates remained eligible, and all had the highest published score of **9/11**. The first specified tie-break therefore decides the result: the selected plant–soil microbe corpus has **202 independent source-study labels**, exceeding the plant-functional-trait corpus (**99**) and the HIREC behavioural-response corpus (**90**). Because the source-study-count tie-break is decisive, neither category balance nor stable-release date is reached. This is a mechanical application of the preregistered hierarchy, not a post hoc judgment of scientific importance.

| Candidate ID | Published audit score | Eligibility at audit | Independent source-study count | Audit-supported populated categories | Selection disposition |
|---|---:|---|---:|---|---|
| `artificial-light-at-night-impacts` | 7/11 | No | 126 | Not established; field/laboratory only and detailed count not completed | **Discarded before ranking.** The completed audit expressly marks its eligibility and recommendation false/provisional because literal category counts and H2/H3 resolution were not completed. |
| `warming-top-down-control` | 8/11 | No | 56 | H1: 138; second category not verified; HU: 39 | **Discarded before ranking.** The minimum requirement of ten estimates in each of two confirmed categories was not met at the audit stage. The supplied paper DOI also did not match the title-matched paper. |
| `global-plant-soil-microbe-interactions` | **9/11** | **Yes** | **202** | H1: 326; H2: 1,197 | **Selected.** Tied for highest score and wins the first tie-break. |
| `hirec-behavioural-responses` | 9/11 | Yes | 90 | H1: 23; H2: 238 | Eligible external-replication candidate, not selected: fewer independent source studies than the winner. The supporting audit report was not written to its stated required path, but its completed audit record supplied the published counts and score used here. |
| `plant-functional-trait-selection` | 9/11 | Yes | 99 | H0: 629; H1: 161 | Eligible external-replication candidate, not selected: fewer independent source studies than the winner. |

The count of eligible candidates was therefore **three**. The selected corpus’s score is preserved exactly as audited: seven base data/traceability/setting points plus one point for each of H1 and H2, for **9/11**. No point is imputed for H0 or H3.

## Selected corpus and audit basis

The selected public CSV contains **5,969 study-level log-response-ratio effects** (`rr`) with corresponding sampling variances (`var`), arranged in **28 columns**. The audit found every `rr` finite and every `var` finite and positive. It identified 202 distinct `Author` source-study values and explicit phase-specific experimental-setting fields: `Phase1.m` (conditioning environment) and `Experimental.setting` (feedback environment).[2]

The category qualification used only the conservative, audit-supported metadata rules. Field conditioning plus field feedback provided H1 (**326 effects from 23 source-study labels**); field conditioning plus greenhouse feedback provided H2 (**1,197 effects from 91 source-study labels**). Greenhouse-only phase combinations remain unresolved rather than being reclassified as H2 or H3 without provenance evidence. Thus, the selected corpus satisfies the eligibility minimum while retaining the codebook’s precaution that unresolvable provenance is `HU`, not a manufactured hop category.[1] [2]

## Independent spot-check of the winning source

I independently checked the original publisher record and the Dryad repository rather than relying solely on the completed audit. The publisher identifies the article as a 2024 *Ecology Letters* **Synthesis**, records receipt, revision, and acceptance dates (13 September, 20 November, and 1 December 2023), and states that the compilation contains **5,969 observations from 202 studies**.[3] The same record describes field and greenhouse experiments and phase-specific experimental choices.

I independently checked the public Dryad landing page and version API. The repository reports public version **6**, published **18 December 2023**, with the files `PSF.data.EL.open.csv`, `README.md`, and `Open_code.R`.[4][5] The README defines `rr` as “Log effect size,” `var` as “Variance of effect size,” `Author` as author and year, and the conditioning and feedback setting fields used in the audit.[6] I retrieved the version bundle from Dryad, extracted the primary CSV, and installed a byte-identical, read-only immutable local copy at:

```text
/home/ubuntu/chain-position-detectability/research/wo-5/analysis/raw-source-data/PSF.data.EL.open.csv
```

The local file has **1,609,518 bytes**, **5,969 data rows** (excluding its header), **28 columns**, and SHA-256:

```text
bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c
```

This equals Dryad’s version-API checksum. The selected primary machine-readable dataset is a single CSV, so it is preserved with its native `.csv` extension rather than unnecessarily wrapping it in a ZIP; the README and analysis script are ancillary release materials, not additional primary data tables.

## Scope limitations carried forward

Selection establishes a single preregistered primary corpus; it does **not** complete the later independent hop coding. Before inferential analysis, the project must create the required coder records and reconciliation log, retain source-study clustering, and build a full citation/DOI crosswalk for the 202 `Author` labels. The source release does not provide raw means, standard deviations, and sample sizes needed to reconstruct every supplied `rr` and `var` from first principles, although it directly supplies both usable fields. Only H1 and H2 are currently established, so the codebook’s categorical fallback—not an unearned three-category ordinal trend model—is the applicable primary model unless later primary-source coding supplies a third qualifying category.[1][2]

## References

[1]: ecology-codebook.md "WO-5 ecology carry-test codebook"

[2]: candidate-corpora/03-global-plant-soil-microbe-interactions.md "Completed audit: global plant–soil microbe interactions"

[3]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

[4]: https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35 "Dryad dataset landing page: Dataset of global plant-soil feedback"

[5]: https://datadryad.org/api/v2/versions/269740/files "Dryad version 269740 file inventory"

[6]: https://datadryad.org/api/v2/files/2789270/download "Released dataset README"

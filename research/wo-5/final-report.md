# WO-5 Final Report: Hop Distance and Pre-Entry Loss

**Author:** Manus AI

**Milestone date:** 19 September 2026

**Status:** Validated first milestone complete; maintenance field tests remain unexecuted

## Executive conclusion

This milestone produced executable protocols for the four maintenance-chain tests and completed the public-data ecology carry test requested by WO-5.[1] Tests A–D could not be run without operators, shift observation, a computerized maintenance management system, or a cooperating plant. They remain protocols, not findings.[2]

Test E used a public synthesis of **5,969 plant–soil-feedback effects from 202 source studies**.[3] Conservative metadata coding resolved 326 effects as `H1`—field conditioning followed by field feedback—and 1,197 as `H2`—field-conditioned biological material or soil followed by greenhouse feedback. The remaining **4,446 effects (74.5%)** were retained as unresolved (`HU`), rather than assigned a hop score from venue alone.[4]

> In the metadata-resolved field-conditioning subset, there was **no detectable difference in average signed individual plant–soil-feedback log-response ratio** between H1 and H2 designs: H2 minus H1 was **−0.0053** (95% source-clustered CR1 CI **−0.1884 to 0.1778**; *p* = **0.955**). The interval is not contained within the prespecified ±log(1.10) region, so the result does **not** establish practical equivalence.[5]

The result does not measure information loss. H1 and H2 are setting-defined groups with different experimental and source-study compositions, and only three studies contribute both categories. The analysis is therefore predominantly between sources and cannot be interpreted as a causal effect of hop distance, degradation of a common field signal, ecological realism, or information retained in transit.[6] [7]

## Milestone coverage

| Test | Requested question | Milestone disposition | Result status |
|---|---|---|---|
| A | Where does the maintenance signal die before entry? | Published a shift-level verbal-observation versus app-entry protocol with proxy attribution and form-encodability fields. | **Not executed**; requires operators and shift access. |
| B | Is an operator’s learned prior calibrated to visible report closure? | Published a CMMS-linked opportunity model and explicit proxy-provenance exclusion rule. | **Not executed**; requires CMMS and independently observed opportunities. |
| C | Does returning manager-side disposition alter reporting? | Published a cluster-randomized stepped-wedge protocol, falsifier, safety outcomes, and opportunity-based denominator. | **Not executed**; requires a cooperating plant and intervention. |
| D | Do app reports retain outcome-separating signal present in verbal observations? | Published grouped-validation models comparing app records with independently captured verbal observations. | **Not executed**; requires linked observations and outcomes. |
| E | Do ecological effect estimates shift with hop category? | Preregistered a public-corpus coding study, selected one corpus deterministically, coded all rows twice, reconciled them, fitted the categorical fallback, and independently validated the analysis. | **Executed; no detectable signed difference, no equivalence, and no causal carry interpretation.** |

The complete maintenance instruments, governance requirements, falsifiers, and minimum reporting fields are in the [field protocol][2].

## Test E design

### Preregistered decision rules

The ecology codebook defined `H0` through `H3`, required unresolved provenance to remain `HU`, required at least ten estimates and five independent sources per category, and permitted a categorical fallback when fewer than three ordinal categories qualified.[8] It also prespecified signed log response ratio as the primary outcome, absolute effect only as a descriptive secondary quantity, source-level clustering, leave-one-source-out checks, a source-level randomization check, and a ±log(1.10) small-effect region.

The repository history proves that the codebook existed in commit `3564d68` before the downstream WO-5 artifacts were committed. The separate discovery workflow record states that discovery followed that commit, but Git alone cannot independently prove that no earlier discovery occurred. The study therefore describes the chronology as **preregistered in the execution record, with timing not independently authenticated end to end**.[7]

### Corpus selection and provenance

Five public candidate syntheses were screened under the fixed eligibility, score, and tie-break rules. Three were eligible and tied at 9/11. The Jiang et al. plant–soil-feedback corpus won the first tie-break because it contained **202 source-study labels**, versus 99 and 90 for the other two eligible candidates.[9]

Dryad public version 6 contains the selected primary CSV. The locally preserved read-only copy has 5,969 rows, 28 columns, and SHA-256 `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c`, matching the Dryad file inventory. Dryad identifies the release as CC0 1.0 Universal.[10] The supplied `rr` and `var` fields are complete and usable, but the release does not contain the raw group means, standard deviations, and sample sizes needed to reconstruct every effect from first principles.

The release also lacks an authoritative bibliography for its 202 raw source labels. A conservative crosswalk now covers every label and effect row, resolves 116 labels to DOI records, leaves 50 ambiguous, and leaves 36 unresolved rather than guessing.[12] The statistical models continue to cluster on the raw release labels, so the partial crosswalk does not alter their estimates. It remains a material limit on primary-study provenance and source deduplication.

### Independent coding and reconciliation

Two coding outputs covered all 5,969 immutable row identifiers. They agreed on every row: 326 `H1`, 1,197 `H2`, 4,446 `HU`, and zero `H0` or `H3`. The verified weighted kappa was 1.000, but the files cannot independently authenticate blinding or temporal independence.[4]

`H1` required an experimental feedback contrast with field labels for the overall environment, conditioning origin, conditioning environment, and feedback setting. `H2` used the same field-conditioning evidence with greenhouse feedback. Greenhouse venue without the required conditioning direction was not promoted to `H2` or `H3`. H2 should be read as **field-conditioned soil or biological material followed by greenhouse feedback**, not as proof that every focal organism had a field-origin life history.[6]

## Statistical analysis

Only H1 and H2 met the category threshold, so the preregistered categorical fallback replaced the planned three-category ordinal model. The primary model was an effect-level random-effects meta-regression with an H2 indicator and source-study-clustered CR1 covariance. The likelihood and weights used a diagonal working sampling covariance because shared-control and other within-source covariances were unavailable. The reported \(\tau^2\) is therefore residual effect heterogeneity under that working model, not a clean between-study variance.[5] [7]

| Model or estimand | Estimate | 95% CI | *p* | Scope |
|---|---:|---:|---:|---|
| H1 mean signed LRR | −0.0429 | −0.1186 to 0.0329 | 0.265 | 326 effects; 23 sources |
| H2 mean signed LRR | −0.0481 | −0.2144 to 0.1181 | 0.567 | 1,197 effects; 91 sources |
| **Primary H2 − H1, CR1** | **−0.0053** | **−0.1884 to 0.1778** | **0.955** | 1,523 effects; 111-source union |
| Primary H2 − H1, CR2/Satterthwaite | −0.0053 | −0.2181 to 0.2075 | 0.958 | Small-sample sensitivity; df = 13.58 |
| Source-category aggregate H2 − H1, CR1 | −0.0028 | −0.1867 to 0.1811 | 0.976 | 114 source-category cells |
| Source-category aggregate H2 − H1, CR2/Satterthwaite | −0.0028 | −0.1931 to 0.1875 | 0.976 | Small-sample sensitivity; df = 33.40 |
| Equal source-category weight | 0.0234 | −0.1652 to 0.2120 | 0.806 | Desensitizes row-count weighting |
| Paired sources only | 0.2448 | −0.5560 to 1.0455 | 0.319 | Only three dual-category sources; non-informative |

The primary design is rank-identified, but overlap is sparse: **20 sources are H1-only, 88 are H2-only, and three contain both categories**. Leave-one-source-out aggregate estimates ranged from −0.0426 to 0.0337, and every interval included zero. A corrected count-preserving source-level permutation held the observed 91 H2 source-category cells fixed, used 4,999 draws with fixed \(\tau^2\) and weights, and returned *p* = 0.9824. These checks show that no single source creates the near-zero unpaired contrast; they do not make the source portfolios exchangeable.[5] [7]

![Primary category estimates](figures/hop-category-estimates.png)

![Sensitivity estimates](figures/hop-contrast-sensitivity.png)

### Practical equivalence and magnitude

The primary 95% interval is not contained within ±log(1.10) = ±0.09531. Independent validation also calculated a 90% interval of −0.1585 to 0.1480 and a two-one-sided-test *p* value of 0.166. The supported wording is therefore **no detectable difference**, not “equivalent,” “no association,” or “no meaningful difference.”[7]

Absolute log response ratio was kept descriptive as preregistered. Mean absolute LRR was 0.2699 for H1 and 0.4639 for H2; after averaging absolute values within source-category cells, the corresponding means were 0.3299 and 0.4774. Those values may reflect biological heterogeneity, comparator choice, venue, soil handling, outliers, or study composition. They are not inferential evidence of a hop effect or information loss.[6] [7]

![Source-category distributions](figures/source-category-distributions.png)

## Interpretation boundary

The executed study answers a narrower question than the WO-5 measurand. It compares a signed biological response across two metadata-defined experimental designs. It does not observe the same latent field quantity before and after transmission, and it contains no measure of signal fidelity, detectability, prediction error, signal-to-noise ratio, or agreement with a field reference.

The categories are exactly confounded with feedback setting: H1 is field-conditioned/field-feedback, while H2 is field-conditioned/greenhouse-feedback. They also differ in comparator, whole-soil versus inoculum use, life form, species origin, taxa, geography, era, and source-study portfolio. Field and greenhouse assays may differ through abiotic variability, pot and root confinement, natural enemies and macrofauna, soil storage, inoculum dilution, competition, colonization, and duration. These mechanisms can change the ecological process itself, not merely the fidelity with which it is measured.[6]

The 4,446 unresolved rows and 91 `HU`-only studies are a structured exclusion, not random missingness. The result generalizes only to the metadata-resolved field-conditioning subset. Primary-study methods review may resolve some excluded rows in a later extension, but this milestone does not replace missing provenance with assumptions.

## Validation and reproducibility

Independent statistical reimplementation reproduced the primary and aggregate coefficients, REML optima, CR1 standard errors, leave-one-out range, equivalence decision, and descriptive magnitude values to numerical precision.[7] The same review identified and corrected the initial non-margin-preserving randomization and added CR2/Satterthwaite sensitivities. Independent ecological review validated the narrow H1/H2 metadata proxy while rejecting information-loss and causal carry interpretations.[6] A reproducibility audit confirmed exact row preservation after CSV parsing, deterministic same-environment outputs, and consistency between machine-readable results and tables.[11]

The final executable is [`analysis/analyze_hop_distance.py`](analysis/analyze_hop_distance.py). Its tested versions and invocation are in [`analysis/environment.md`](analysis/environment.md) and [`analysis/requirements.txt`](analysis/requirements.txt). Exact model results are in [`analysis/model-results.json`](analysis/model-results.json) and [`analysis/model-summary.csv`](analysis/model-summary.csv); the coded dataset, aggregates, permutation draws, leave-one-source-out results, figures, validation reports, and source manifest are retained alongside them.

## What this milestone establishes

1. **Tests A–D are runnable but unexecuted.** The repository now contains concrete denominators, provenance fields, falsifiers, governance requirements, and analysis plans for a cooperating plant.
2. **Test E yielded a negative and ambiguous carry result.** No signed H1–H2 difference was detected, uncertainty does not establish equivalence, and sparse source overlap prevents a credible within-source carry conclusion.
3. **The selected ecology outcome is not an information-loss measurand.** It can test a setting-defined association, but not transit loss, pre-entry loss, or fidelity of a common signal.
4. **The strongest next empirical step remains maintenance.** Running Test A with independent opportunity capture and proxy attribution would directly estimate pre-entry loss. A disposition-transparency intervention under Test C would test the work order’s most consequential falsifiable prediction.

## References

[1]: ../../work-orders/WO-5-hop-distance-and-pre-entry-loss.md "WO-5 — Hop distance and pre-entry loss in reporting chains"

[2]: field-protocols.md "WO-5 field protocols for maintenance reporting chains"

[3]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

[4]: reconciliation-log.md "WO-5 hop-coding reconciliation record"

[5]: analysis/analysis-results.md "WO-5 statistical analysis results"

[6]: validation/ecological-interpretation.md "Independent ecological methods review"

[7]: validation/statistical-analysis.md "Independent validation of the H1-versus-H2 meta-analysis"

[8]: ecology-codebook.md "WO-5 ecology carry-test codebook"

[9]: corpus-selection.md "WO-5 corpus selection"

[10]: source-manifest.md "WO-5 source retrieval and checksum manifest"

[11]: validation/reproducibility.md "WO-5 reproducibility audit"

[12]: source-crosswalk-report.md "WO-5 source crosswalk method and coverage"

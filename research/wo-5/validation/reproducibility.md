# WO-5 reproducibility audit

**Auditor:** Independent reproducibility audit
**Audit date:** 19 September 2026
**Scope:** Execution, input/output integrity, tabular and figure artifacts, documentation links and citations, Git timing evidence, and corpus-selection records.

## Verdict: computational reproduction passes; archival reproducibility is qualified

The supplied analysis script reproduced **bit-for-bit** on two consecutive executions in the audited environment. The reconciled coded input retained its declared SHA-256 hash, the immutable raw CSV retained its manifest hash, and neither changed during either execution. All generated analysis tables, the JSON result, the Markdown result, the three PNG figures, and the captured standard output were identical at baseline, after run 1, and after run 2. The substantive model-table crosswalk and all CSV structural checks passed.

This is not yet a fully auditable preregistered research record. The Git history proves that the codebook was committed at 2026-09-19 23:02:06 UTC, but it does not version the corpus discovery, selection, raw input, coding, reconciliation, analysis code, or generated results. Consequently, it cannot independently establish that corpus discovery and downstream decisions followed the preregistration. The candidate-selection record is also incomplete relative to the codebook: it lacks the discovery inventory and the underlying audit records for two candidates named in the selection table. Finally, the analysis report is not a self-contained reproducibility report because it has no links to its data, code, figures, or result files and no reference definitions.

## Execution and integrity checks that passed

| Check | Result | Evidence |
|---|---|---|
| Supplied script execution | **Pass.** Both runs exited successfully. | [`analyze_hop_distance.py`](../analysis/analyze_hop_distance.py) was run twice with Python 3.12.3, NumPy 2.5.1, pandas 3.0.5, SciPy 1.18.1, and Matplotlib 3.11.1. |
| Coded-analysis input fixity | **Pass.** The SHA-256 was `77dc735fa425abd96329acbc55a99c6403f7da77b947f3b1cc7d61a9ec612480` before execution, after run 1, and after run 2. | This is both the script’s embedded expected hash and the hash recorded in [`hop-coding.md`](hop-coding.md). |
| Raw-source fixity | **Pass.** The read-only raw CSV remained `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c`; its filesystem mode was `0444`. | [`source-manifest.md`](../source-manifest.md) records the same digest and mode. |
| Hidden mutation of reviewed inputs | **Pass for the supplied script.** Hashes of the codebook, coded data, script, pre-existing result files, selection report, reconciliation log, manifest, and coding-validation report were unchanged from the baseline snapshot through both runs. | Static inspection shows the script reads only `analysis/hop-coded-effects.csv` as its data input; it rewrites only declared derived artifacts and figures. |
| Output determinism | **Pass in the audited environment.** All generated files had identical SHA-256 hashes between run 1 and run 2; the entire JSON standard-output stream was also identical. | Both rerun streams exactly matched the retained [`model-results.json`](../analysis/model-results.json). |
| Raw-to-derived content preservation | **Pass.** Parsed values in all 28 original columns matched, in the same `N` order, across all 5,969 raw and coded records. | The coded CSV has seven appended coding fields; it intentionally does not preserve raw physical CSV serialization. |
| CSV parsing and structural validity | **Pass.** All inspected CSVs parsed with a standards-compliant CSV reader, had no blank header names or ragged rows, and had the expected row counts. | See the detailed table below. |
| Model JSON/table consistency | **Pass.** Each of the eight models in `model-summary.csv` was unique. Every shared estimate, standard error, confidence-limit, statistic, degrees-of-freedom, and p-value exactly equalled the corresponding field in [`model-results.json`](../analysis/model-results.json). | The JSON records the same coded-input hash and counts as the executable run. |
| Figure generation | **Pass.** All three expected PNGs exist and were byte-identical across runs. | Dimensions are listed below. |
| Existing relative targets | **Pass with one coverage qualification.** Every existing Markdown relative link inspected resolved to a local target. | The analysis report contains no relative links at all; this is a documentation defect rather than a broken-target failure. |

## Row counts, parsing, and analysis-artifact checks

| Artifact | Parsed columns | Data rows | Audit result |
|---|---:|---:|---|
| [`raw-source-data/PSF.data.EL.open.csv`](../analysis/raw-source-data/PSF.data.EL.open.csv) | 28 | 5,969 | `N` coverage, ordered parsed source values, finite `rr`, and positive finite `var` agree with the coded file. |
| [`hop-coded-effects.csv`](../analysis/hop-coded-effects.csv) | 35 | 5,969 | `N` is nonblank and unique. `rr` parses as finite in 5,969 rows; `var` parses as finite and positive in 5,969 rows. Counts are H1 = 326, H2 = 1,197, HU = 4,446, H0 = H3 = 0. |
| [`model-summary.csv`](../analysis/model-summary.csv) | 11 | 8 | Eight unique models; all required numerical fields parse. The summary matches the shared fields in JSON exactly. |
| [`study-category-aggregates.csv`](../analysis/study-category-aggregates.csv) | 12 | 114 | Consistent with the reported 114 source-category cells from 111 sources. |
| [`leave-one-study-out.csv`](../analysis/leave-one-study-out.csv) | 9 | 111 | One result per reported eligible source-study cluster. |
| [`permutation-results.csv`](../analysis/permutation-results.csv) | 2 | 4,999 | Matches the declared number of label-swap replicates. |
| [`category-counts.csv`](../analysis/category-counts.csv) | 4 | 2 | One record each for H1 and H2. |
| [`magnitude-summary.csv`](../analysis/magnitude-summary.csv) | 9 | 2 | One record each for H1 and H2. |

The figure artifacts are present at the paths created by the script: [`hop-category-estimates.png`](../figures/hop-category-estimates.png), [`hop-contrast-sensitivity.png`](../figures/hop-contrast-sensitivity.png), and [`source-category-distributions.png`](../figures/source-category-distributions.png). Their dimensions are respectively **1,700 × 1,040 px**, **1,800 × 1,080 px**, and **1,700 × 1,060 px**. Their checksums did not change across either run.

## Defects requiring correction

### 1. The analysis report is not self-contained or linked to its artifacts

[`analysis-results.md`](../analysis/analysis-results.md) has no relative links, figure embeds, inline numeric citations, or `References` section. It names `model-results.json`, `model-summary.csv`, and generated figures in prose, but does not make them navigable. A reader cannot directly reach the executable script, input dataset, model files, aggregates, permutation draws, or figure outputs from the report.

**Required correction:** Add working relative links to the code, coded input, model JSON, model-summary CSV, auxiliary tables, and all figures. Embed the figures or link them with descriptive labels. Add a `References` section containing valid numeric reference definitions for the preregistration, source data, and any external methodological or source claims. Re-run the relative-link check after editing.

### 2. `corpus-selection.md` uses malformed/nonstandard numeric citation definitions

All six numbered definitions in [`corpus-selection.md`](../corpus-selection.md) begin with a Markdown inline link, for example `[1]: [WO-5 ecology carry-test codebook](https://...) (description)`, rather than a reference destination followed by an optional quoted title. This is not a standard reference-style definition. The numbered references are therefore not reliably rendered or machine-resolved as citation links. The other inspected cited reports use normal `URL "title"` definitions.

**Required correction:** Replace each definition with a valid reference definition. For example, use `[1]: https://… "WO-5 ecology carry-test codebook"`; where a local artifact is cited, use its correct relative target and a quoted title. Retain explanatory prose in the body rather than after a malformed definition.

### 3. Candidate-selection artifacts are incomplete and the discovery universe is not reproducible

The codebook requires a discovery inventory and publication of exclusion reasons and scores. The selection table identifies five candidates, but the `candidate-corpora` directory contains only three audit reports: `02-warming-top-down-control`, `03-global-plant-soil-microbe-interactions`, and `05-plant-functional-trait-selection`. There is no stored audit report for `artificial-light-at-night-impacts`, and the selection report expressly says that the completed supporting audit for `hirec-behavioural-responses` was not written to its required path. No discovery inventory exists anywhere under `research/wo-5`.

At face value, the documented deterministic tie-break selects the global plant–soil corpus correctly: its stated 202 source studies exceeds the stated 99 and 90 for the two other eligible candidates. However, that conclusion cannot be independently reconstructed from the retained candidate artifacts because the complete candidate universe, the two missing audit records, and the supporting counts/scores are absent.

**Required correction:** Add a durable discovery inventory that records every candidate considered, discovery source/date, eligibility, audit score, all tie-break inputs, exclusion rationale, and the retained evidence path. Add the full ALAN and HIREC audit reports at stable repository paths, including the HIREC counts used in the selection decision. Version these artifacts in Git.

### 4. Git history does not independently establish the claimed preregistration timing

Git confirms that the current codebook was added in commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90`, authored and committed at **2026-09-19 23:02:06 UTC**, with the message “Preregister WO-5 hop-distance study.” The current codebook is tracked and clean. This supports existence of the analytic rules at that commit.[1] [2]

It does not establish the stronger statement in the codebook that it was “Preregistered before corpus discovery.” Every downstream WO-5 artifact used to demonstrate discovery, selection, raw retrieval, coding, reconciliation, executable analysis, results, figures, and validation is untracked by Git. Filesystem modification times are later than the commit but are mutable metadata and are not a chain-of-custody record. Git therefore provides no independently auditable ordering between corpus discovery/decision-making and the preregistration commit.

**Required correction:** Commit the current downstream artifacts and their future revisions. For a defensible timing claim, preserve dated discovery/search logs and candidate snapshots, anchor the preregistration in an immutable public release or signed/tagged commit before discovery, and record later artifact creation in subsequent commits. Until then, describe the timing as **claimed but not independently verified by repository history**.

### 5. The runtime environment is not pinned for portable replication

The script imports NumPy, pandas, SciPy, and Matplotlib but the repository contains no `requirements.txt`, lockfile, `pyproject.toml`, or environment specification. The two-run result proves same-environment determinism only. Numerical optimization, random-number generation, CSV serialization, and figure rasterization can vary across unpinned library, Python, operating-system, and font versions.

**Required correction:** Provide a version-pinned environment specification or lockfile, state the tested Python and package versions, and include an invocation command. If bit-identical figures are a formal requirement, specify the backend and fonts or separate numerical determinism from rendering determinism.

### 6. The 202-source citation crosswalk remains absent

The selection report and selected-candidate audit both acknowledge that the raw source labels are not a complete citation/DOI crosswalk. This does not invalidate the current `Author`/`Year` clustering or the computed model, but it limits auditability of source-study identity, original-study provenance, and independent verification of the coding basis.

**Required correction:** Publish a 202-source crosswalk keyed to the raw `Author` and `Year` labels, containing the full citation, DOI or stable URL, normalized source-study identifier, and any disambiguation decision. Link coding groups and inherited rules to this crosswalk where primary-study evidence is used.

## Qualifications that must remain with the result

The coded CSV intentionally reserializes the raw CSV: the raw input uses its own header/field quoting and CRLF line endings, while the derived file quotes all fields and uses LF line endings. The parsed content of all 28 retained raw fields is identical, but the files are not byte-identical and must not be described as physically byte-preserved. This qualification is already documented in [`hop-coding.md`](hop-coding.md).

The supplied coding artifacts verify that Coder A and Coder B produced identical labels and that the stated agreement statistics calculate correctly. They do not independently prove blinding or temporal independence because there is no timestamped assignment record, separate work log, or other evidence of independent work. Coder B’s narrow CSV also omits `F.H` and `Approach`, although its decisive-basis text and the raw/final files allow the reconciled rule to be checked. These are provenance limitations, not observed row-level coding errors.

Only H1 and H2 meet the established category criterion, so the categorical fallback is consistent with the codebook and no three-category ordinal trend model was warranted. The output should continue to state that the contrast is associational, is confounded with setting and source composition, and does not establish practical equivalence because the primary confidence interval is not within the prespecified ±log(1.10) margin.

The relative-link test checked whether local relative targets exist. It did not test live availability or content stability of external URLs. The raw-release source itself has a documented checksum and a read-only local copy, but the current environment does not reproduce `rr` and `var` from raw means and sample summaries because those source fields are not included in the retained 28-column CSV.

## Closing assessment

**The numerical analysis is reproducible from the supplied coded input in the audited environment.** The core fixed-input, parsing, row-count, model-table, output-determinism, and figure-generation checks all pass. The required work is archival and documentary rather than a correction to the reproduced estimates: complete the discovery/candidate record, make Git timing evidence durable, provide a portable software environment, add the source citation crosswalk, and repair the report’s links and citation definitions. Until those changes are made, the result should be described as computationally reproducible but **not independently time-verified as a preregistered end-to-end workflow**.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook at the preregistration commit"

[2]: https://github.com/JinnZ2/chain-position-detectability/commit/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90 "Preregister WO-5 hop-distance study commit"

[3]: https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35 "Dataset of global plant–soil feedback"

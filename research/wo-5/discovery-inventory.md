# WO-5 corpus discovery inventory

**Author:** Manus AI
**Inventory date:** 19 September 2026
**Deterministically selected corpus:** `global-plant-soil-microbe-interactions`

## Decision and provenance statement

This inventory records the five candidate corpora retained by the WO-5 discovery workflow. The governing codebook required public, study-level ecological effect data with uncertainty, source-study identity, setting metadata, at least 80 usable effects, and at least ten coded effects in each of two hop categories. It then required selection of the eligible corpus with the highest score, resolving a score tie first by the greater effective number of independent source studies.[1]

The orchestration record places the start of the deterministic discovery workflow **after** public preregistration commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90` on 19 September 2026.[2] This is a statement about the recorded workflow sequence, not proof that no discovery occurred earlier. Git can establish the retained commit and its timestamped history, but cannot by itself exclude earlier searches, discussions, or unrecorded work outside that history. The pre-discovery claim is therefore qualified to the orchestration record.

Three candidates were eligible, each with a score of 9/11. `global-plant-soil-microbe-interactions` was selected because its 202 independent source-study labels exceed the 99 labels in `plant-functional-trait-selection` and the 90 labels in `hirec-behavioural-responses`. This first prespecified tie-break is decisive; category balance and public-release date were not used.[1] [8]

## Candidate comparison

**Counting convention.** “Effect rows” and “source studies” preserve the denominator adopted in each completed audit. Hop entries report effects first and, where the audit established them, parenthetical source-study counts. `HU` denotes unresolved records. A provisional label is explicitly marked and is not a completed independent primary-study coding result.

| Candidate ID | Paper / data URLs | Topic | Eligible | Score | Effect rows | Source studies | Confirmed hop counts (audit status) | Exclusion reason or limitation governing disposition | Audit path | Selected status |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| `artificial-light-at-night-impacts` | Paper: [https://doi.org/10.1038/s41559-020-01322-x](https://doi.org/10.1038/s41559-020-01322-x)<br>Data: [https://doi.org/10.5061/dryad.wpzgmsbjn](https://doi.org/10.5061/dryad.wpzgmsbjn) | Biological impacts of artificial light at night | No | 7/11 | 1,304 released extraction rows; 1,109 `Delete = Keep` analysis rows | 126 released-study labels; 117 in the selected subset | H0 = 0; H1 = 0; H2 = 0; H3 = 0; HU = 1,304. `Field.Lab` screens 770 field and 534 laboratory rows but is **not** a hop code. | Two threshold-clearing hop categories were not verified. Venue alone cannot distinguish H0/H1 or H2/H3 because provenance, exposure type, relocation, and response location are absent. | [`candidate-corpora/01-artificial-light-at-night-impacts.md`](candidate-corpora/01-artificial-light-at-night-impacts.md) [3] | **Discarded before ranking**; ineligible. |
| `warming-top-down-control` | Paper: [https://doi.org/10.1111/ele.12913](https://doi.org/10.1111/ele.12913)<br>Data: [https://doi.org/10.6084/m9.figshare.5702812.v1](https://doi.org/10.6084/m9.figshare.5702812.v1) | Warming effects on top-down control | No | 8/11 | 175 synthesis-selected `gI` effects (177 rows have finite `gI` and positive `var_gI`) | 56 | H1 = 138 (36); H0 = 0; H2 = 0 confirmed; H3 = 0 confirmed; HU = 39 (20), all laboratory-labelled. | The second qualifying category remains unverified: laboratory/greenhouse venue does not establish field-origin relocation (H2) versus controlled history (H3). The candidate-supplied DOI `10.1007/s00442-017-4011-3` did not match the title-matched paper; the corrected DOI is shown at left. | [`candidate-corpora/02-warming-top-down-control.md`](candidate-corpora/02-warming-top-down-control.md) [4] | **Discarded before ranking**; ineligible. |
| `global-plant-soil-microbe-interactions` | Paper: [https://doi.org/10.1111/ele.14364](https://doi.org/10.1111/ele.14364)<br>Data: [https://doi.org/10.5061/dryad.n2z34tn35](https://doi.org/10.5061/dryad.n2z34tn35) | Global patterns and drivers of plant–soil microbe interactions | **Yes** | **9/11** | **5,969** | **202** | H1 = **326** (23); H2 = **1,197** (91); H0 = 0; H3 = 0; HU = 4,446 (97 greenhouse/greenhouse and 3 greenhouse/field source-study labels, respectively). | No exclusion. Greenhouse-only combinations remain HU without origin/history evidence; this does not affect the two threshold-clearing categories. A full citation crosswalk and independent coding remain required before inference. | [`candidate-corpora/03-global-plant-soil-microbe-interactions.md`](candidate-corpora/03-global-plant-soil-microbe-interactions.md) [5] | **Selected primary corpus.** Tied for the highest score and won the first tie-break (202 source-study labels). |
| `hirec-behavioural-responses` | Paper: [https://doi.org/10.1111/oik.08366](https://doi.org/10.1111/oik.08366)<br>Data: [https://doi.org/10.5061/dryad.hx3ffbgfb](https://doi.org/10.5061/dryad.hx3ffbgfb) | Behavioural responses to human-induced rapid environmental change | **Yes** | 9/11 | 381 | 90 | **Provisional** H1 = 23 (11 raw IDs); **provisional** H2 = 238 (46 raw IDs); H0 = 0 awarded; H3 = 0 awarded; HU = 120. | No eligibility exclusion. H1/H2 are README-metadata availability screens, not reconciled primary-study codes. Raw `ID` and `Ref` are not one-to-one, no full citation/DOI crosswalk is released, and H0/H3 must not be inferred from field/wild-observational or laboratory/captive labels. | [`candidate-corpora/04-hirec-behavioural-responses.md`](candidate-corpora/04-hirec-behavioural-responses.md) [6] | **Eligible external-replication candidate; not selected.** It lost the first tie-break to 202 source-study labels. |
| `plant-functional-trait-selection` | Paper: [https://doi.org/10.1086/706199](https://doi.org/10.1086/706199)<br>Data: [https://doi.org/10.5061/dryad.sn02v6x0q](https://doi.org/10.5061/dryad.sn02v6x0q) | Natural selection on plant functional traits | **Yes** | 9/11 | 1,714 (1,242 standardized selection gradients, β; 472 selection differentials, S) | 99 normalized bibliographic signatures | H0 = **629** (42 citation signatures); H1 = **161** (15); H2 = 0 confirmed; H3 = 0 confirmed; HU = 924. | No eligibility exclusion. Controlled or semi-controlled contexts lack origin/history evidence for H2 versus H3; 21 bibliographic signatures overlap the two workbooks, so downstream source clustering must be reconciled. β and S are separate native outcomes and must not be silently pooled. | [`candidate-corpora/05-plant-functional-trait-selection.md`](candidate-corpora/05-plant-functional-trait-selection.md) [7] | **Eligible external-replication candidate; not selected.** It lost the first tie-break to 202 source-study labels. |

## Selection integrity and carried-forward limits

The two ineligible candidates were removed before score ranking. The selected corpus retains its audited 9/11 score: seven base data/traceability/setting points and one point each for H1 and H2. No point was manufactured for H0 or H3. The selection is therefore a mechanical application of the preregistered hierarchy rather than a judgment that the selected topic is intrinsically more important than the alternatives.[1] [5] [8]

This discovery inventory does not replace the required analysis-stage coding work. The selected release needs a source-paper citation/DOI crosswalk, independent hop coding with recorded decisive evidence and provenance confidence, a row-to-design-group inheritance map, and reconciliation with agreement statistics. Until a third threshold-clearing category is supported, the codebook specifies the categorical random-effects fallback rather than an ordinal hop-trend model.[1] [5]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook (pinned preregistration)"

[2]: https://github.com/JinnZ2/chain-position-detectability/commit/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90 "Preregister WO-5 hop-distance study"

[3]: candidate-corpora/01-artificial-light-at-night-impacts.md "Completed audit: artificial light at night impacts"

[4]: candidate-corpora/02-warming-top-down-control.md "Completed audit: warming and top-down control"

[5]: candidate-corpora/03-global-plant-soil-microbe-interactions.md "Completed audit: global plant–soil microbe interactions"

[6]: candidate-corpora/04-hirec-behavioural-responses.md "Completed audit: HIREC behavioural responses"

[7]: candidate-corpora/05-plant-functional-trait-selection.md "Completed audit: plant functional trait selection"

[8]: corpus-selection.md "WO-5 corpus selection and deterministic tie-break record"

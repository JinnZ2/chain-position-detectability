# WO-5 execution record

**Status:** Validated first milestone complete; maintenance field tests remain open

**Work order:** [WO-5 — Hop distance and pre-entry loss in reporting chains](../../work-orders/WO-5-hop-distance-and-pre-entry-loss.md)

## Milestone outcome

Tests A–D require operators, shift observation, a computerized maintenance management system, or an intervention at a cooperating plant. This repository run had none of that access. It therefore published executable, falsifiable, governance-aware [field protocols](field-protocols.md) without claiming plant-level results.

Test E, the ecology carry test, was executed against a deterministically selected public plant–soil-feedback corpus. Two coding outputs agreed on all 5,969 effects: 326 were resolved as H1, 1,197 as H2, and 4,446 remained unresolved. The primary H2-minus-H1 signed log-response-ratio contrast was **−0.0053** (95% source-clustered CR1 CI **−0.1884 to 0.1778**; *p* = **0.955**). CR2/Satterthwaite, source-category aggregation, equal-source weighting, leave-one-source-out, paired-source, and corrected count-preserving randomization checks did not produce a detectable contrast.

The interval is wider than the preregistered ±log(1.10) region, so the result does not establish practical equivalence. Only three source studies contain both H1 and H2. The result is predominantly between sources, exactly confounded with feedback setting, and cannot be interpreted as information loss, a causal hop effect, ecological realism, or degradation of a common field signal. The [final report](final-report.md) gives the complete validated interpretation.

## Artifact map

| Area | Principal artifacts |
|---|---|
| Work-order implementation | [Final report](final-report.md); [field protocols](field-protocols.md); [ecology codebook](ecology-codebook.md) |
| Corpus discovery | [Discovery inventory](discovery-inventory.md); [selection decision](corpus-selection.md); [candidate audits](candidate-corpora/); [source manifest](source-manifest.md) |
| Source identity | [Source crosswalk](source-crosswalk.csv); [crosswalk methods and coverage](source-crosswalk-report.md) |
| Coding | [Coder A](evidence/coder-a.csv); [Coder B](evidence/coder-b.csv); [reconciliation](reconciliation-log.md); [coded effects](analysis/hop-coded-effects.csv) |
| Analysis | [Executable](analysis/analyze_hop_distance.py); [analysis report](analysis/analysis-results.md); [machine-readable results](analysis/model-results.json); [model table](analysis/model-summary.csv); [tested environment](analysis/environment.md) |
| Figures | [Category estimates](figures/hop-category-estimates.png); [sensitivity estimates](figures/hop-contrast-sensitivity.png); [source distributions](figures/source-category-distributions.png) |
| Validation | [Validation synthesis](validation-summary.md); [statistical reimplementation](validation/statistical-analysis.md); [ecological review](validation/ecological-interpretation.md); [reproducibility audit](validation/reproducibility.md); [coding validation](validation/hop-coding.md) |

## Scope statement

This milestone publishes a computationally reproducible, fixed-input association with material design and archival qualifications. The repository history proves that the codebook existed before the downstream package was committed, but it does not independently authenticate the entire pre-discovery chronology. The public release does not include raw group summaries needed to reconstruct every supplied effect and variance, and 74.5% of rows remain outside the resolved H1/H2 subset. The published crosswalk covers all 202 raw source labels but resolves only 116 to DOI records; 50 remain ambiguous and 36 unresolved.

# WO-5 ecology carry-test codebook

**Author:** Manus AI

**Status:** Preregistered before corpus discovery

## Question

Test E asks whether published ecological effect estimates shift with the number of hops between an organism in its own conditions and the reported response. The analysis is a carry test of the WO-5 instrument. It is not a claim that laboratory work is inferior or that hop count alone causes an effect-size difference.

## Corpus eligibility and deterministic selection

A candidate corpus must be associated with a peer-reviewed ecological synthesis, expose study-level effect estimates or enough data to reconstruct them, provide uncertainty or sample-size information, identify source studies, and contain metadata capable of distinguishing at least two hop categories. It must be publicly downloadable without private credentials. The empirical corpus must contain at least 80 usable effect estimates and at least ten estimates in each of two categories after coding.

Discovery will seek public datasets across ecological subfields. Each eligible corpus receives one point for public machine-readable data, effect estimate, sampling variance or reconstructable uncertainty, source-study identifier, traceable primary-study citation, at least 80 usable estimates, and an explicit experimental-setting field. It receives one additional point for each populated hop category, capped at four. The highest score is selected. Ties are broken by the greater effective number of independent source studies, then the more even distribution across categories, then the earlier stable public release. Reasons for exclusion and all scores will be published.

Only one corpus is used for the primary milestone. Other eligible corpora remain external-replication candidates rather than undisclosed researcher degrees of freedom.

## Unit and hop categories

The unit is one effect estimate in the selected synthesis. One source study may contribute several estimates, so study identity is retained for clustered inference.

| Code | Hop category | Operational rule |
|---|---|---|
| `H0` | Lived-in field | The focal organisms remain in a naturally occurring population or community. Exposure or contrast is ambient or naturally occurring, and the response is measured in situ. |
| `H1` | Observed or manipulated field | The focal organisms remain under field or semi-natural conditions, but researchers impose a treatment, enclosure, translocation within the field system, or repeated observational apparatus before measuring the response in situ. |
| `H2` | Sampled to controlled setting | Organisms, propagules, communities, or biological material originate in the field but are moved to a laboratory, greenhouse, growth chamber, common garden, or other controlled setting before the focal exposure or response measurement. |
| `H3` | Controlled-history or lab-only | The focal organisms or cultures have a controlled or laboratory-reared history, and both focal exposure and response measurement occur under controlled conditions. |
| `HU` | Unresolved | The public metadata and accessible source do not support a unique category. This code is excluded from the primary trend test and counted. |

Physical relocation determines `H2`; merely bringing samples to a laboratory for measurement after the biological response occurred in situ does not. Mesocosms remain `H1` when installed in the field and exposed to ambient field conditions, but become `H2` when organisms are moved to a controlled facility. Greenhouses and common gardens are `H2` for field-origin organisms. A study is `H3` only when controlled history is supported; missing provenance is `HU`, not `H3`.

The ordinal score is 0–3. It represents relocation and representational distance, not organizational rank, study quality, or causal importance.

## Independent coding

Two coders independently assign hop category, provenance confidence, and the decisive source passage or metadata field. They do not see the other code. Agreement is reported as raw agreement and weighted Cohen's kappa. Disagreements are reconciled against the public primary study or synthesis metadata. If the evidence remains ambiguous, the final code is `HU`.

Coding may occur at a repeated design-group level when the same source-study methods apply to several effect rows. Every inherited code must identify that group and the rows to which it applies. Automated string rules may propose categories but cannot be the sole evidence for the final code.

## Effect-size harmonization

The selected corpus's native effect-size metric is retained if it is zero-centered and has a sampling variance. Direction is harmonized only when the synthesis supplies an explicit beneficial or harmful orientation. The transformation rule and any sign reversals will be published. Metrics that cannot be made commensurate are analyzed separately; they are never pooled by relabeling.

The primary outcome is the signed effect size. The secondary magnitude outcome is its absolute value and is treated as descriptive because the transformation changes its sampling distribution.

## Primary model

The primary model is a random-effects meta-regression with hop score as an ordinal predictor. Inverse-variance weights use the reported sampling variance plus an estimated between-study variance. Standard errors are clustered by source study. The coefficient reports the average effect-size change for one additional hop.

The ordinal test runs only if at least three hop categories contain ten effects and five independent source studies each. Otherwise, the preregistered primary result is a categorical random-effects model across every eligible category. A categorical model is reported in either case to reveal nonlinearity.

The main sensitivity checks aggregate multiple estimates within source study, omit one source study at a time, use only high-confidence codes, and compare results with and without synthesis-supplied quality or risk-of-bias variables when available. A permutation test shuffles hop labels at the source-study level when at least 20 independent studies are present.

## Interpretation and falsifiers

Evidence for a hop association requires a nonzero primary coefficient or categorical contrast with uncertainty that excludes zero and stability across the source-aggregation and high-confidence checks. The magnitude and direction are reported without causal wording.

A near-zero estimate with intervals inside a prespecified small-effect region is evidence against a practically important association in this corpus. The small-effect region is set at ±0.10 standard-deviation units for standardized mean differences or ±log(1.10) for log response ratios. If the native metric lacks a defensible threshold, the study reports uncertainty without claiming equivalence.

The carry claim is not supported if hop categories cannot be coded reliably, the selected corpus lacks category overlap, or the association disappears under source-study aggregation. A detected association remains vulnerable to confounding by taxon, stressor, endpoint, publication selection, study era, and design quality.

## Outputs

The repository will include the discovery inventory, coder records, reconciliation log, immutable raw input or a retrieval script, derived analysis dataset, executable analysis code, model tables, diagnostic figures, final report, and independent validation. If no eligible corpus exists, that null discovery is the result and no synthetic data will be substituted.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-5-hop-distance-and-pre-entry-loss.md "WO-5 — Hop distance and pre-entry loss in reporting chains"

[2]: https://en.wikipedia.org/wiki/Data_processing_inequality "Data processing inequality"

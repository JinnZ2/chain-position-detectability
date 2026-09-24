# Independent ecological methods review: interpretation of the H1–H2 plant–soil-feedback contrast

**Reviewer role:** Independent ecological methods reviewer
**Review date:** 19 September 2026
**Materials audited:** preregistered ecology codebook; reconciled coded-effect file; coder-method records; corpus-selection and reconciliation records; analysis script; model outputs; and the source synthesis/data documentation.

## Overall verdict

**Partially validated, with a strict interpretation boundary.** The analysis implements the preregistered **categorical fallback** correctly: only H1 and H2 have the required number of effects and source studies, so an ordinal three-or-more-category slope was not estimable. The H1 and H2 records are reproducibly derived from the selected plant–soil-feedback (PSF) fields, and their narrow operational definitions are consistent with the codebook **provided that field-conditioned soil/soil biota is treated as the “biological material” that is moved to a greenhouse feedback phase**. The reported H2-minus-H1 signed log-response-ratio (LRR) estimate is therefore a valid estimate of an association between these two *setting-defined PSF designs* in the selected, metadata-resolved subset.

It is **not** an estimate of information loss, pre-entry loss, ecological realism, or a per-hop degradation effect. In fact, it has no direct information-loss estimand. The contrast compares PSF values from different experimental settings and largely different studies rather than repeated measurements of a common ecological signal before and after a known transmission step. The current analysis report states this central restriction, but the limitation needs to be made more concrete and carried into any final headline or abstract.

## What the data and codebook support

The codebook defines H1 as an experimentally observed/manipulated field response with the focal organisms under field or semi-natural conditions, and H2 as field-origin organisms, propagules, communities, or biological material moved to a controlled setting before focal exposure or measurement. It explicitly treats physical relocation as the determinant of H2 and prohibits assigning H3 from missing provenance alone.[1] The source dataset identifies `Phase1.m` as the conditioning-phase environment, `Experimental.setting` as the feedback-phase setting, `Approach` as self–other versus self–sterilized PSF contrast, `rr` as the log effect size, and `var` as its variance.[2] The synthesis describes its effect as **individual PSF**, calculated as a biomass log-response ratio comparing conspecific-conditioned live soil with heterospecific-conditioned or sterilized soil.[3]

The final coding applies two narrow rules. H1 requires field entries for field/overall experimental environment, `Phase1.m.ori`, `Phase1.m`, and `Experimental.setting`; H2 uses the same field-conditioning pattern but a greenhouse feedback setting. All 326 H1 and 1,197 H2 rows meet their respective literal field patterns, have high rule-based confidence, and have concordant codes from both coders.[4] H1 is appropriately not called H0: `Approach` identifies an experimental PSF contrast, whereas H0 requires an ambient or naturally occurring contrast. H2 is appropriately not called H3: the field conditioning record is affirmative evidence against assuming a wholly controlled history. The source fields thus support a **conservative, reproducible operational proxy** for H1 and H2.

The proxy is nonetheless narrower than the natural-language category labels. A field value during conditioning and a greenhouse feedback value demonstrate a phase-setting sequence, but they do not record the provenance of every focal plant or document the physical transfer event in prose. H2 is defensible because soil and its microbial community are biological material, and a field-conditioned soil feedback assay in a greenhouse ordinarily entails moving that material. It should therefore be described as **“field-conditioned soil/material with greenhouse feedback”**, not as proof that every focal organism itself was field-origin. Similarly, a field feedback setting supports an experimental field response but does not, by itself, resolve all details of in-situ exposure or local field manipulation. The coding is codebook-consistent at the dataset-metadata level; it is not a substitute for primary-study methods verification.

The initial corpus-selection record correctly anticipated this limitation by noting that a full citation/DOI crosswalk and later primary-source coding would be needed for stronger provenance resolution.[5] Perfect coder agreement here establishes reproducibility of the conservative metadata rules, not independent confirmation of the unrecorded biological history.

## Preregistered model selection and numerical result

The decision to use a categorical rather than ordinal model follows the codebook. The ordinal primary model requires at least three populated hop categories with at least ten effects and five independent source studies each. Only H1 and H2 qualify; H0 and H3 have zero rows. The categorical analysis includes 1,523 effects from 111 source-study identifiers: 326 H1 effects from 23 studies and 1,197 H2 effects from 91 studies.[1] [4]

The effect-level random-effects meta-regression estimates the signed H2-minus-H1 contrast as **−0.0053 LRR** (95% clustered CI **−0.1884 to 0.1778**, *p* = 0.955). Study/category aggregation, equal source-category weights, leave-one-source-out analysis, and the source-label permutation test give similarly non-detectable unpaired contrasts. The interval is wider than the preregistered ±log(1.10) equivalence margin, so the correct result is **no detectable difference in mean signed PSF**, not practical equivalence.[6]

| Audit question | Finding | Review judgment |
|---|---|---|
| Is the H1/H2 fallback preregistered? | Yes. H1 and H2 meet the count requirement, but there is no third qualifying category for an ordinal slope. | **Confirmed.** |
| Do selected fields operationalize H1/H2? | Yes as a narrow phase-setting proxy: field conditioning plus field versus greenhouse feedback. H2 relies on field-conditioned soil/biota being the moved biological material. | **Conditionally confirmed.** |
| Does the signed LRR contrast measure information loss? | No. It measures a difference in mean signed individual-PSF LRR across setting-defined study groups. | **Not supported; terminology must be corrected.** |
| Is field-versus-greenhouse/source-composition confounding stated? | It is stated at a high level, but the extent and ecological mechanisms are not quantified. | **Partly adequate; expand.** |
| Are absolute-LRR results inferential? | No; the analysis labels them descriptive and attaches no test. | **Confirmed, provided they remain non-evidentiary.** |
| Are HU exclusions innocuous? | No. They are codebook-required but are very large and structured by field availability and design. | **Major generalizability/selection concern.** |

## A signed PSF LRR contrast is not information loss

The outcome is a biological response contrast, not a measurement of information fidelity. Its sign records whether biomass in conspecific-conditioned soil is higher or lower than biomass in heterospecific-conditioned or sterilized soil.[3] A shift in this signed quantity can arise from real changes in microbial communities, host–soil interactions, soil inoculum, pot constraints, environmental control, competition, response duration, or the comparator used in the PSF experiment. None of those mechanisms represents loss of information in a reporting chain.

To interpret a contrast as information loss, the study would need an explicitly defined latent or reference field PSF quantity, a documented transfer/measurement process, and repeated or otherwise comparable observations showing how accurately the downstream measure recovers that reference. This analysis has none of those elements. H1 and H2 are not paired observations of the same field effect under two measurement stages: only **3 of 111 eligible source studies** contribute both categories. Thus, a near-zero H2-minus-H1 mean does not show that information was retained; it only fails to detect a difference in average signed PSF among these two nonexchangeable sets of studies.

The signed outcome creates a second interpretive constraint. Opposite ecological changes may cancel in a mean LRR. A greenhouse setting could strengthen negative PSF in some systems and strengthen positive PSF in others without producing a mean signed shift. Conversely, a nonzero signed difference would not establish reduced detectability or attenuated magnitude. The data contain no outcome measuring detectability, signal-to-noise ratio, prediction error, replication fidelity, or agreement with a field reference. Terms such as **“information loss,” “pre-entry loss,” “per-hop degradation,”** or **“no loss”** should not be applied to this contrast.

## Field–greenhouse and source-composition confounding is fundamental

The existing analysis report correctly says that hop category is inseparable from field versus greenhouse feedback setting and source-study composition.[6] This is the right core boundary, but it is not sufficient by itself for an ecological reader because the category construction makes experimental setting an exact component of the exposure. H1 is field-conditioned/field-feedback and H2 is field-conditioned/greenhouse-feedback. The estimate is consequently at least as much a comparison of **feedback environment** as it is a comparison of codebook score.

The eligible source composition also offers little within-study leverage. H1 has 23 contributing source studies, H2 has 91, and only 3 contribute to both. Source-clustered standard errors address dependence among rows within a source; they do **not** make different source-study portfolios ecologically comparable or remove design confounding. The three-study paired sensitivity analysis is too imprecise to solve this problem (estimate 0.2448, 95% CI −0.5560 to 1.0455).[6]

Important recorded moderators differ materially between categories. H1 is 69.3% non-woody and 93.9% native, whereas H2 is 51.9% non-woody and 85.2% native. H1 is almost entirely self–other (99.4%), while H2 includes 33.1% self–sterilized contrasts. H1 uses whole soil in 55.8% of effects versus 22.5% in H2; conversely, inoculum is used in 44.2% versus 77.5%. Taxa, study years, geographic locations, conditioning context, and response durations also differ across categories. These are not ancillary nuisances: PSF can respond to each of them, and the source synthesis itself treats plant attributes and experimental-setting variables as moderators.[3]

The final interpretation should therefore state that the contrast is **confounded by feedback environment, PSF comparator, soil inoculum treatment, taxonomic and geographic composition, study era, and source-study portfolio**. It should not imply that cluster-robust inference, aggregation, or permutation testing resolves these ecological differences. Those procedures support the precision statement under the fitted association model; they do not identify a hop effect.

A further ecological limitation is absent from the current summary. Greenhouse and field feedback assays can differ in temperature and moisture variation, pot volume and root confinement, natural enemy and macrofauna access, soil storage and transport, inoculum dilution, host density, competition, colonization opportunities, and feedback duration. These design features can alter the PSF process itself, not simply its observation. A field-to-greenhouse contrast should thus not be framed as a lower-fidelity version of an otherwise invariant field signal.

## Absolute-effect results are correctly descriptive, but must remain so

The codebook explicitly identifies absolute effect size as a secondary **descriptive** outcome because the absolute-value transformation changes the sampling distribution.[1] The analysis follows that instruction: it reports no inferential test for the H1/H2 absolute-LRR difference. The reported row-level mean absolute LRRs are 0.2699 for H1 and 0.4639 for H2; source-category mean absolute LRRs are 0.3299 and 0.4774, respectively.[6]

This treatment is acceptable only if the values are not used as corroboration of a hop, information-loss, or ecological-realism claim. The two sets differ in the distribution of signs, variances, effect types, and study designs; a larger descriptive mean absolute LRR in H2 can reflect any combination of true biological heterogeneity, comparator choice, setting, outliers, and source composition. It does not repair cancellation in the signed contrast, and it does not establish stronger or weaker PSF. If an inferential magnitude question becomes scientifically necessary, it requires a separately prespecified estimand and method that accommodates the transformed outcome, dependence, heterogeneity, and covariate imbalance.

## HU exclusion is codebook-compliant but creates a strong selection limitation

Excluding HU records from the primary trend test is required by the preregistered codebook, and the analysis visibly counts them.[1] [4] This is a strength of the coding process: ambiguous greenhouse history was not relabelled as H2 or H3 merely to create categories. It is not, however, evidence that the retained records are representative.

The exclusion removes **4,446 of 5,969 effects (74.5%)**. The retained H1/H2 analysis covers only 25.5% of effects. Of 202 source studies, **91 are HU-only** and are removed entirely; only eight studies contain both any eligible effect and any HU effect. The exclusions are not random missing observations. They follow a structured data-design pattern: 4,164 HU rows have greenhouse conditioning and greenhouse feedback with numeric conditioning-duration entries in `Phase1.m.ori`, while 282 have greenhouse conditioning and field feedback. The retained two-category sample is therefore selected for the particular subset with literal field-conditioning labels, not a representative sample of all PSF designs.[4]

This selection has two consequences. First, the results generalize only to the **metadata-resolved field-conditioning subset**, not to the full 5,969-effect global PSF corpus and not to greenhouse-conditioned experiments. Second, the unobserved H2-versus-H3 classification in most greenhouse rows could be associated with taxa, region, publication era, methods, or PSF value. Direction and size of the resulting selection bias cannot be determined from the available fields. The appropriate remedy is not post hoc reclassification; it is primary-study provenance review under a documented rule, followed by a separately reported expanded analysis if new categories can be resolved. Until then, conclusions must foreground the selected subset.

The codebook also says the carry claim is not supported when category overlap is lacking.[1] The presence of only three source studies in both H1 and H2 does not demonstrate sufficient overlap for a robust carry interpretation. At minimum, the study should describe this as **limited overlap**, present the paired result as non-informative rather than confirmatory, and avoid a general carry-test conclusion.

## Required corrections to interpretation

The final report should preserve the numerical result but replace any broad carry or loss language with the following conclusion:

> In the metadata-resolved subset of field-conditioned plant–soil-feedback studies, we found no detectable difference in average **signed individual-PSF log-response ratio** between field-feedback (H1) and greenhouse-feedback (H2) designs. The confidence interval does not establish practical equivalence. Because hop score is defined by feedback setting and is strongly confounded with source-study and experimental composition, this association cannot be interpreted as information loss, a causal effect of hop distance, ecological realism, or degradation of a common field signal.

It should also add a sentence that H2 means **field-conditioned biological material/soil followed by greenhouse feedback**, not a verified individual-level field-origin history. Finally, it should report HU exclusion as a scope condition in the main conclusion: 74.5% of effect rows and 91 HU-only studies were excluded because the available metadata could not distinguish field origin from controlled history. These changes are necessary to align ecological interpretation with the codebook’s stated noncausal boundary and its unresolved-category safeguard.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"

[2]: https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35 "Dataset of global plant-soil feedback"

[3]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

[4]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/reconciliation-log.md "WO-5 hop-coding reconciliation record"

[5]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/corpus-selection.md "WO-5 corpus selection"

[6]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/analysis/analysis-results.md "WO-5 statistical analysis results"

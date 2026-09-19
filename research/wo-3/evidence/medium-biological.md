# WO-3 evidence record — biological transfer and contamination

**Audit target:** the preregistered `Biological` family: “organisms, cells, spores, genes, or viable propagules,” recorded as count, biomass, or probability of transfer. **Verdict: REFRAME.** It is not an adequate closed inventory for biological transfer or biological contamination. The row mixes physical entities, inherited information, and viability, but it omits several experimentally established acellular agents and does not record whether material reaches, persists in, enters, or functionally changes a biological receptor.

## Direct observations

**OBSERVED — acellular genetic and signalling cargo crosses between cells.** In a primary experiment, engineered extracellular vesicles (EVs) were taken up by recipient tumour cells and translated donor EV-delivered messenger RNA within one hour. The same study measured uptake by fluorescence/flow cytometry and translated cargo by luciferase signal; EV-RNA alone induced a recipient signalling response. EVs carry membrane, proteins, lipids, and nucleic acids, so their functional payload is not exhaustively described by “genes.” [1] These are material and information crossings even if no whole organism, cell, spore, or viable propagule crosses.

**OBSERVED — infectious biological activity can be carried by material that contains neither cell nor gene.** A primary hamster experiment exposed wood, rock, plastic, glass, cement, stainless steel, aluminium, and brass to scrapie prions. With brass the exception, tested materials bound, retained, and released prions; contaminated implants or housing with contaminated spheres transmitted disease in hamsters. [2] A misfolded infectious protein is not an organism, cell, spore, gene, or conventional viable propagule. This is a decisive counterexample to treating the listed classes as exhaustive.

**OBSERVED — virus particles can transfer biological information.** In marine transduction experiments, phage particles transferred a plasmid bearing antibiotic-resistance markers to bacterial isolates and concentrated natural bacterial communities. Confirmed transduction frequencies in mixed communities were reported in transductants per plaque-forming unit. [3] A virion is not a cell, organism, or gene alone; whether “viable propagule” includes it is ambiguous. An ontology intended as a complete falsifier cannot depend on that ambiguity.

**OBSERVED — free, fragmented DNA is a transferable biological substrate.** Natural transformation is defined as bacterial acquisition of extracellular DNA and its integration into a genome. A primary study specifically tested highly fragmented and damaged donor DNA and reports that short fragments can be substrates for transformation. [4] The current word “genes” is too narrow operationally: extracellular genomic fragments, plasmids, transposons, and other mobile elements must be sampled and assayed as material entities before any recipient outcome can be known.

**OBSERVED — biological contamination includes nonviable material when it can corrupt a life-detection result.** NASA states that forward contamination controls terrestrial organisms **and organic materials** carried by spacecraft, to protect the integrity of life detection. [5] NASA’s spacecraft practice also samples hardware, cultures recovered spores, and reports bioburden against requirements rather than claiming zero. [6] Therefore a definition confined to viable propagules misses biological/organic signatures that can constitute scientific contamination even when they cannot reproduce.

**OBSERVED — a biological non-detect is not a zero.** In controlled ponds containing fish, 28 of 243 one-litre water samples from stocked ponds detected fish environmental DNA (eDNA), an overall detection rate of about 12%; the authors estimated that more than 100 L could be needed for a >95% detection probability at low density. [7] A peer-reviewed analysis of microbial non-detects likewise explains that finite sampling, imperfect or variable recovery, and counting error prevent a non-detect from directly measuring the true concentration. [8] NASA explicitly identifies cultivation selectivity and incubation competition as reasons culture-based analyses do not capture the full microbial diversity of cleanrooms. [9]

## What the ontology misses and how to amend it

The missing items are **distinct biological crossing types or endpoints**, not merely alternate labels for the same count. All are measurable over a declared boundary `B` and finite horizon `H`, but their estimates retain detection, recovery, and model uncertainty. They should receive their own vector components or clearly declared subcomponents; they should not be collapsed into a count of “biological things.”

| Omitted transfer or coupling | Why the present row is incomplete | Finite-horizon measurement across `B` | What a positive result establishes |
| --- | --- | --- | --- |
| **Virions and other acellular infectious particles** | A particle packages genome and proteins; it is neither a cell nor a gene. “Viable propagule” is undefined for viruses. | Concentration/count per air, water, surface, or waste sample; infectivity assay or plaque-forming units; genomic assay. Report recovery and assay limit. | Particle, genome, or infectivity crossed, depending on assay. |
| **Infectious proteins / conformational seeds (prions)** | Protein-only infectivity falls outside every listed class. [2] | Surface/swab or effluent mass/concentration; seed-amplification or bioassay result; recipient infection probability. | Prion material or infectivity crossed; a negative assay is only bounded by its sensitivity. |
| **Extracellular vesicles, secreted RNA, and other acellular bioactive cargo** | EV cargo can alter recipient translation/signalling without reproduction or gene integration. [1] | Particle count/size distribution, cargo molecules, donor-recipient markers, uptake rate, and recipient expression/phenotype in matched controls. | Vesicle/cargo transfer and, where assayed, functional coupling. |
| **Naked or fragmented extracellular DNA/RNA and mobile genetic elements** | “Genes” does not specify physical DNA/RNA fragments, plasmids, transposons, or their function after uptake. | Nucleic-acid mass/copies and sequence markers in inbound/outbound samples; recipient transformant count or transfer frequency. | Molecular transfer; recipient assay separately establishes integration/expression. |
| **Nonviable cells, fragments, biomass, and biological/organic signatures** | They may cause false positive life detection or contaminate an assay even though they cannot propagate. [5] | Biomass, cell/particle fragments, targeted molecules, and sequence signatures; blank-controlled assay contamination rate. | Contaminating signature crossed; it does not by itself establish viability or transmission. |
| **Establishment and biological effect after arrival** | Transfer count does not measure colonization, persistence, replication, infection, horizontal transfer, phenotype, or ecological displacement. | Define receptor population and follow-up interval inside `H`; measure viable persistence, reproduction number, prevalence/incidence, transformants, gene expression, or ecological response. | A causal biological coupling only when supported by exposure, controls, and an outcome assay. |

**PROPOSED amendment.** Replace the single biological item with a small, non-exclusive profile:

`Bio(B,H) = {living cells/organisms and viable propagules; virions; acellular infectious proteins; extracellular vesicles and secreted bioactive cargo; extracellular nucleic acids and mobile elements; nonviable biological/organic signatures; receptor establishment/effect}`.

For each class `j`, report `N_j` or mass/copies crossing, `P_j(cross)`, assay recovery/sensitivity, and where a receptor exists, `P_j(establish/effect | exposure)`. The last term is an **effect coupling**, not a transported medium; keeping it separate prevents a detected sequence fragment from being mistaken for an infection or ecological consequence. Matter, information, and biological components may overlap. That overlap is appropriate for a terminality test, but must be declared for comparison work.

## Boundary and horizon conclusions

These candidates **can** be measured on a stated finite frame. For example, define `S` as a spacecraft, laboratory, or sealed device; define `B` as its exterior surface plus a sampling plane in outgoing/incoming air, liquid, personnel, and waste; define `H=[t0,t1]`; and identify the lifecycle phase. Sampled flow volumes, surface areas, and times allow rates such as virions/L, EVs/hour, DNA copies/m²/day, prion-seeding units/day, or probability of at least one transfer. A receptor outcome needs a further declared follow-up window and comparator. This is an empirical bound on that sampling design and `H`, not a complete biological zero.

The work order’s generic examples (“a mouse, a spore”) correctly warn that biological material is a crossing, but they are not an exhaustive biological ontology. In particular, they would miss a surface-bound prion, an EV-mediated RNA transfer, or a viral particle unless a reviewer first expands “anything” beyond the stated metric. That is precisely the avoidable incompleteness the falsifier is meant to expose.

## Can `U = 0` be empirically verified without creating a crossing?

**No, not for a same-boundary, same-horizon empirical verification that communicates the result outside `S`.** Reading an instrument, receiving telemetry, or observing emitted light transfers information across `B`; an active assay additionally introduces energy, apparatus, sampling material, or personnel. Under the metric’s own definition, that witness is at least an information crossing and often a matter/energy/human-institutional crossing. In biological work, swabbing or collecting an effluent also physically removes material and may introduce contamination.

There are limited formal escape routes, none of which empirically prove whole-life terminality. First, place the measuring apparatus and its record inside `S` and retrieve the result after `t1`; the retrieval is a crossing **outside** the narrowly declared `H`, so it may support only “no detected crossing during `H` under this internal assay.” Second, include the observer and data recipient within `S`; that redraws `B` rather than removes the crossing, and reporting the conclusion to anyone outside again crosses the enlarged boundary. Third, deduce zero from an idealized construction model. That is a **theoretical/model claim**, conditional on complete premises, not an empirical verification.

Finite biological sampling has an additional problem: even when measurement itself is declared out of scope, non-detection supplies a positive finite upper bound only under explicit assumptions about sampling coverage, extraction/recovery, assay sensitivity, target class, spatial/temporal heterogeneity, and a statistical confidence convention. It does not yield exact `U = 0`. [7] [8] [9] A finite `H` permits a defensible statement such as “below `U` at stated confidence for named classes and sampled locations,” but not the literal all-biological-channels zero used by the work order’s falsifier.

**BOTTOM LINE (DERIVED):** One observed virion, prion, EV cargo transfer, extracellular DNA transfer, or biological-signature contamination is enough to classify the stated frame as nonterminal. The proposed metric must first enumerate these classes. If it cannot, its correct classification is **unresolved**, not terminal. A zero upper bound is a model-dependent limit claim; empirical biology supplies detection-limited upper bounds and positive witnesses, not a crossing-free proof of zero.

## References

[1]: https://www.nature.com/articles/ncomms8029 "Visualization and tracking of tumour extracellular vesicle delivery and RNA translation using multiplexed reporters"

[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5836136/ "Efficient prion disease transmission through common environmental materials"

[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC106772/ "Gene Transfer by Transduction in the Marine Environment"

[4]: https://www.pnas.org/doi/10.1073/pnas.1315278110 "Bacterial natural transformation by highly fragmented and damaged DNA"

[5]: https://sma.nasa.gov/sma-disciplines/planetary-protection "Planetary Protection"

[6]: https://planetaryprotection.jpl.nasa.gov/mission-implementation "Mission Implementation"

[7]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0103767 "Assessing Environmental DNA Detection in Controlled Lentic Systems"

[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6182096/ "The Critical Importance of Rethinking Microbial Non-detects"

[9]: https://planetaryprotection.jpl.nasa.gov/technology-development "Technology Development"

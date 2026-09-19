# WO-3 evidence record — Matter and material transfer

**Item:** WO-3 / crossing family: matter and material transfer
**Audit verdict:** **REFRAME.** The preregistered matter row is a useful broad prompt, but its present measurand—“mass or count entering and leaving”—is not an operationally complete material-transfer ontology. It can miss exchanges that have zero **net** bulk mass, transfers through a moving or porous boundary, material particles labelled as “radiation,” and charge-carrier/chemical-species transfers. The literal all-media zero-crossing falsifier is not empirically certifiable to an external observer: certifying it produces an information/measurement crossing.

## Scope and status of claims

This record audits only the metric’s **Matter** family, not energy, information, biological, human/institutional, or dependency families. It reads “physical media” in the work order and “mass or count entering and leaving” in the metric as claims about transfer across a declared boundary `B` during a horizon `H`. The metric already prohibits netting opposite directions, which is correct, but it does not state the material resolution, crossing-surface convention, or treatment of particles and charge carriers needed to implement that rule. [1] [2]

**Observed/source-supported** statements below report what the opened sources say or document. **Derived** statements are consequences for this metric. **Proposed** text is an amendment, not an observed fact.

## Evidence that the current row is incomplete

| Candidate omitted or under-specified transfer/coupling | Source-supported observation | Can it be measured on declared `B` over finite `H`? | Consequence for the matter ontology |
|---|---|---|---|
| **Species-, isotope-, and phase-resolved countertransfer** | IUPAC defines speciation as an element’s distribution among defined chemical species. NIST documents heterogeneous isotopic exchange between a solid sample and a gas, and diffusion measurements based on radioisotope distributions. In multicomponent transport, individual diffusive species fluxes may be nonzero while their sum is constrained to zero. [3] [4] [5] | **Yes**, conditionally. Sample/measure both sides or use tracers and report amount or particle number by species/isotope/phase over `H`. The detection process is itself outside the matter result. | Bulk mass alone is insufficient. A system may have zero change in total mass, or even zero summed diffusive flux, while atoms cross both ways. “Absolute inbound + outbound” only prevents concealment if quantities are recorded at a resolution capable of identifying those exchanges. |
| **Sorption/desorption and dissolution/leaching at the boundary** | IUPAC defines sorption as uptake of a substance on or in a sorbent; it includes adsorption and absorption. Gas permeability through rubber was measured as gas passing through a membrane into a quantitatively sampled downstream stream. [6] [7] | **Yes.** Define whether the surface film and pore volume belong to `S`; assay the fluid/gas on each side and report uptake, release, and through-flux separately. A finite measurement has a detection bound, not automatically a zero bound. | The rule needs an explicit boundary-membership convention for films, pores, deposits, corrosion layers, and dissolved material. Otherwise the same event can be called internal state change or crossing by redrawing `B`. |
| **Permeation and outgassing without an obvious “physical medium”** | NASA spacecraft-material data report total mass loss and collected volatile condensable material after a 24-hour, 398 K vacuum test. ESA’s standard likewise treats thermal-vacuum outgassing and condensation as testable material properties. [8] [9] | **Yes.** For a specified pressure, temperature, area and `H`, weigh source/collector and chemically analyze the downstream material; report gas composition and collection efficiency. | “No physical media crossing” must explicitly include molecules and volatiles moving through nominally solid containment. A seal, vacuum, or apparent absence of objects is not a zero-material-transfer witness. |
| **Abrasion, fragmentation, shedding, resuspension, and deposition** | A peer-reviewed review reports that tyre/road contact generates wear particles; some become airborne and others move through runoff and environmental pathways. It emphasizes size-dependent collection and transport. [10] | **Yes**, but mass and count must be reported separately with a size/material bin, sampled area/volume, capture efficiency, and observation duration. | “Particles” is too coarse without size and composition bins. A few large fragments and many nanoparticles can have similar mass but different counts, detection probabilities, trajectories, and external exposure. The work order’s mention of dust does not supply a measurement rule. |
| **Matter emitted as nuclear particles** | The IAEA distinguishes alpha particles, beta electrons, and neutrons from gamma rays, which are electromagnetic radiation. Radioactive decay can release particles and energy. [11] | **Yes**, if a particle reaches the declared boundary: use particle spectrometry/counters, shielding-verified collection, or activity plus a stated decay-and-escape model. Count and kinetic energy are distinct measurands. | The metric’s energy row includes “radiation,” which risks swallowing **alpha, beta, and neutron material transfer** into energy. Classify each crossing by carrier: photon as energy; emitted alpha/beta/neutron as matter **and** energy/momentum when both are relevant. |
| **Electrons, ions, and other charge carriers crossing a material interface** | Beta radiation is electron emission; multicomponent transport formalizes constituent-specific flux rather than only a bulk mass flux. [4] [11] | **Yes.** Use current/charge integration with carrier identification where needed, plus `N`, charge, and mass bounds; define whether leads/electrodes are inside `S`. | Matter must include mobile charged particles. Treating all current merely as “energy” loses a physical carrier crossing and can hide electrochemical migration, electron leakage, ion transport, or plasma transfer. |
| **Moving, eroding, growing, or porous boundary** | The permeation experiment requires a specified membrane area and separates two chambers; transport equations distinguish individual constituent fluxes at a surface. [4] [7] | **Yes**, if `B(t)` is geometrically declared. Instrument a fixed spatial control surface or track the material surface and state the reference velocity, area, porosity, and whether retained mass belongs to `S`. | The metric declares `B` but not whether it is a fixed spatial surface, a material surface, or a moving interface. Without that choice, erosion, deposition, diffusion through pores, and “material retained in the wall” can be counted inconsistently. |

## What the evidence establishes—and what it does not

**Observed.** The opened sources establish that species-specific diffusion can occur under a zero-sum diffusive-flux constraint; isotope exchange between a solid and gas is a real measurement method; gases permeate nominally solid rubber; spacecraft materials are screened by measured vacuum mass loss; wear generates particulate releases; and radioactive decay can emit massive particles as well as electromagnetic radiation. [4] [5] [7] [8] [10] [11]

**Derived.** These observations falsify the adequacy of a matter metric that permits only a single undifferentiated mass or count total. They do **not** establish that every physical system has a positive material crossing in every finite interval. A declared finite `B,H` can have no detected material event. Nor do they establish that every candidate leaks or sheds at a positive rate. Those are candidate-specific empirical questions.

**Counterexample to a bad inference.** “No change in the object’s total mass” does not imply no matter crossing. Equal-mass exchange, isotope exchange, adsorption followed by desorption, and opposite constituent fluxes can leave a bulk inventory or net flux near zero. Conversely, an internal chemical or nuclear transformation with no carrier crossing `B` is not a **matter-transfer** crossing merely because the composition changed. It may create energy, radiation, or dependency crossings, which are outside this family.

## Boundary- and horizon-specific measurement rule

**Proposed amendment.** Replace the matter row with the following specification:

> A **material crossing** is the passage across the declared oriented boundary `B(t)` of an identifiable mass-bearing carrier or constituent—atom, molecule, ion, electron, nucleon, particle, fragment, droplet, bulk object, organism, or material mixture. Record gross, not net, inward and outward transfer. For each carrier class `s` and size/phase/isotope bin `k`, report `M[s,k,in]`, `M[s,k,out]`, `N[s,k,in]`, and `N[s,k,out]`, with the boundary convention, reference velocity, sampled area, capture/detection efficiency, and detection limit.

A practical form is `Qmatter,dir(B,H) = Σ(s,k) Σ(events crossing B in direction dir during H) m(event)`, reported separately for `dir ∈ {in,out}`. Counts are a separate vector, not a substitute unit for mass. If a continuum flux is appropriate, integrate the species flux relative to the declared moving boundary rather than reporting a net inventory change. The reviewer must also declare whether surface films, wall pores, sensors, collectors, power leads, and the operator are inside `S`.

This amendment intentionally permits overlap. A microbial cell is both biological and matter; an alpha particle is matter and carries energy/momentum; an observation can be information and energy. The terminality test may use any positive witness. Quantitative comparison, however, must retain carrier labels and avoid adding incompatible units.

## Can `U_matter = 0` be empirically verified without an information crossing?

**Observed metrology constraints.** BIPM defines measurement as experimentally obtaining values attributable to a quantity; it requires a procedure and calibrated measuring system. Metrological traceability includes a documented unbroken calibration chain, each link contributing uncertainty; it expressly does not ensure adequate uncertainty or absence of mistakes. The U.S. EPA’s method-detection limit is the minimum concentration distinguishable from blanks with **99% confidence**, and requires a defined method, blanks, spikes, and recurring verification. These are bounded-confidence procedures, not proofs of exact absence. [12] [13] [14]

**Derived conclusion.** For a finite horizon, an external observer cannot empirically certify `U_matter(B,H) = 0` **without an information/measurement crossing**. If a detector or observer is outside `B`, a result must reach it by a signal, record, observation, or person—each is an information crossing under the preregistered ontology. If the detector and record remain inside `B`, an outside party cannot obtain the empirical result; moving the record or observer out creates the crossing. Remote observation does not solve this: it normally imports an energy/information carrier across `B`.

This is not a claim that every measurement must send **matter** across `B`; an optical or electromagnetic readout can avoid that. It is a claim about the work order’s stronger phrase “zero crossings in every medium.” A demonstration to an external evaluator contradicts that antecedent by producing information transfer. The metric recognizes this observability problem but retains a terminal-within-scope classification contingent on exact zero upper bounds. [2]

The stronger proposition that finite experiments can never establish an exact zero material upper bound follows from measurement logic and the stated ontology, not directly from a source. It should therefore be labeled **DERIVED**, not OBSERVED. An exact zero may be a **model-level** consequence of stipulated laws, ideal geometry, and complete premises; it is not an empirical verification of those premises. Imperfect readout and finite resolution are documented practical limitations in quantum metrology as well. [15]

## Decision for WO-3

The literal operational falsifier (“a system with zero crossings in every medium”) is **not empirically executable for an externally reportable test**. It can remain a logical thought experiment only if the work order calls it non-empirical. The empirical replacement should be:

> For a declared `S`, moving-or-fixed `B`, finite `H`, lifecycle phase, carrier-resolution inventory, and measurement configuration, no material crossing was detected and every enumerated material carrier has a stated **strictly positive or model-conditioned** upper bound.

That replacement is a useful nonterminality screen and supports positive material witnesses. It must not be called a verified zero-crossing system. The matter ontology should be amended before applying the asymptote cases; otherwise a “zero” based on bulk mass, a sealed container, or photon-only monitoring can be misclassified.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-3-terminal-system-accounting-boundary.md "WO-3 — The terminal system as an accounting boundary"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/crossing-metric.md "WO-3 crossing-rate metric and test protocol"

[3]: https://goldbook.iupac.org/terms/view/ST06861/plain "IUPAC Gold Book: speciation"

[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4672376/ "Enforcing realizability in explicit multi-component species transport"

[5]: https://nvlpubs.nist.gov/nistpubs/jres/72A/jresv72An2p157_A1b.pdf "Diffusion rates in inorganic nuclear materials"

[6]: https://goldbook.iupac.org/terms/view/S05769/plain "IUPAC Gold Book: sorption"

[7]: https://nvlpubs.nist.gov/nistpubs/ScientificPapers/nbsscientificpaper387vol16p327_A2b.pdf "Permeability of rubber to gases"

[8]: https://ntrs.nasa.gov/citations/19970027853 "Outgassing Data for Selecting Spacecraft Materials"

[9]: https://ecss.nl/standard/ecss-q-st-70-02c-thermal-vacuum-outgassing-test-for-the-screening-of-space-materials/ "ECSS-Q-ST-70-02C: Thermal vacuum outgassing test for the screening of space materials"

[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5664766/ "Wear and Tear of Tyres: A Stealthy Source of Microplastics in the Environment"

[11]: https://www.iaea.org/newscenter/news/what-is-radiation "What is Radiation?"

[12]: https://jcgm.bipm.org/vim/en/2.1.html "International Vocabulary of Metrology: measurement"

[13]: https://jcgm.bipm.org/vim/en/2.41.html "International Vocabulary of Metrology: metrological traceability"

[14]: https://www.law.cornell.edu/cfr/text/40/appendix-B_to_part_136 "40 CFR Appendix B to Part 136: Definition and Procedure for the Determination of the Method Detection Limit—Revision 2"

[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9666656/ "Quantum metrology with imperfect measurements"

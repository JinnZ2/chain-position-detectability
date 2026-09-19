# WO-3 evidence record — external dependency, exposure, and causal consequence

**Verdict: REFRAME.** The work order’s literal falsifier—an empirically established zero crossing in every medium—cannot be operationalized for this family. The preregistered metric usefully separates a positive witness from non-detection, but its dependency variable remains incomplete: it counts downstream dependents while treating distinct non-flow couplings as if they were either a transfer rate or already captured by that count.

## What the record shows

**OBSERVED — source documents.** The work order treats a crossing as any transfer or causal coupling across the boundary and proposes zero crossings in every medium as its falsifier. The metric records `D(B,H)` as identifiable external people or systems whose state, payoff, safety, or decisions depend on `S`; its proposed units are a dependent count, dependent-hours, and expected harm. Its basic quantitative object, however, is cumulative inbound and outbound quantity divided by duration. This makes `D` primarily outward-facing and leaves no separately specified quantity for a standing constraint, shared cause, or an inbound exposure relationship.

**OBSERVED — external evidence.** Infrastructure-dependency literature distinguishes physical, cyber, geographic, and logical relations. Geographic relations arise from spatial proximity; logical relations can arise through human decisions and formal or informal rules, including alongside physical or cyber links. They are not reducible to an observed material flow. [1] [2] NRC common-cause analysis similarly treats a single shared cause and a coupling mechanism as an analytically material feature; it explicitly distinguishes dependence caused by external shared equipment from a common-cause event inside the selected component boundary. [3] These are direct counterexamples to an ontology in which every relevant external relation is adequately represented by an in/out quantity or a downstream-recipient count.

## Omitted or operationally missing candidates

1. **Inbound dependency and common-cause exposure.** `D` asks who depends on `S`, not what external conditions, assets, or institutions `S` depends on. A shared cooling system, grid, floodplain, software authority, or enabling organization can determine `S`’s state while no downstream person currently depends on it. A common cause can also jointly affect `S` and an outside system without a transfer from `S` to that system. This is a distinct exposure/coupling relation, not evidence of a realized outbound flow. It is measurable over declared `B,H` as a scenario–asset matrix, the set of shared enabling conditions, and conditional joint-failure or harm probabilities. Those probabilities are **derived/model-dependent**, not direct observations.

2. **Geographic occupancy, co-location, and exclusion.** A system can constrain an outside system through a shared right-of-way, a reserved volume, spatial blockage, exclusion zone, or co-location with a hazard. No transaction, signal, or realized injury need occur during `H`. The metric’s prose word “constrains” reaches this case, but neither `Qm,in/out` nor a count of dependents provides a quantity for it. It can be measured within a declared boundary and horizon using mapped overlap or occupied area/volume-time, affected external assets, and an explicitly stated activation condition. The causal consequence remains conditional: it must not be reported as observed harm unless the condition occurs.

3. **Logical/governance coupling.** Rules, permits, platform terms, priority queues, ownership rights, and emergency procedures can make one system’s permitted state depend on another’s without a contemporaneous signal, labor hour, payment, or physical transfer. The metric lists legal duties and accounting claims under human/institutional channels, but supplies no edge definition or method to distinguish a rule that actually constrains an external system from a merely recorded obligation. This is a gap in the operational ontology, not necessarily in its broad prose definition. It is measurable over `B,H` by a versioned rule corpus, identified governed entities, rule-to-entity edges, activation conditions, and provenance. Its claimed consequence is again a **derived** counterfactual unless an activation event is observed.

4. **Static state/field coupling.** The prose includes field-mediated transfer, but the rate construction uses cumulative in/out quantities. A persistent field, potential, imposed boundary condition, or standing load can constrain an exterior state even when net energy, mass, and information flux over a sampling interval is zero. This is not cleanly represented by `Qm,in/out / duration(H)`. For a declared boundary it can be recorded as a field value or gradient, force/load, state constraint, and its duration; whether it causally changes an external system requires a model or an observed response. Thus it is not wholly absent from the verbal ontology, but is missing from the specified measurand.

5. **Counterfactual exposure severity.** Dependent count and dependent-hours do not describe reliance strength, substitutability, latency to failure, reversibility, or the magnitude of a prevented/caused outcome. Expected harm is not a directly observed crossing and has no common physical unit. For finite `B,H`, report a dependency graph plus per-edge activation condition, time-to-effect, substitute availability, and a bounded conditional consequence distribution. Label this layer **DERIVED**. Do not convert it into a positive lower bound merely because a plausible pathway exists.

## Necessary amendment

Replace the single `D(B,H)` field with a declared **external-relation vector**: `D_out` (outside recipients dependent on `S`), `D_in` (external enabling conditions required by `S`), `X_shared` (shared-cause/co-exposure links), `G` (spatial occupancy and geographic co-location), and `L` (logical/governance rule links). Each edge needs direction, entities, boundary location, lifecycle phase, activation condition, evidence type, and a separate value for observed events versus modelled conditional consequence. Add `K_state` for static field/load/state coupling rather than forcing it into a transfer rate.

This amendment makes each item measurable **within scope**, but does not make the inventory complete. Completeness is a claim about the catalogue, boundary map, and causal model. It must be declared and audited; it cannot be inferred from a finite set of zero observations.

## Can a zero upper bound be empirically verified?

**OBSERVED.** NIST states that a measurement result is an approximation or estimate and is complete only with a quantitative statement of uncertainty. [4] Its account of Currie’s detection framework distinguishes a threshold for declaring a detection from a detection limit and from a quantitative-determination limit; false absence is an explicit error mode. [5] IUPAC likewise defines a detection limit as the smallest detectable amount, not proof of absence. [6]

**DERIVED.** For a finite `B,H`, no external empirical procedure can establish the universal claim `U = 0` for every dependency/exposure coupling without creating an evidence channel. Remote monitoring returns a signal, record, or observation across `B`. An instrument placed inside `S` moves material and information into the assessment arrangement; reading its record moves information back out. If the record never leaves, an outside party has no empirical verification. If setup or retrieval is excluded from `H`, the evidence crossing still exists in the larger lifecycle and defeats whole-life terminality. Moving the verifier into `S` only moves the boundary; communicating verification recreates the crossing.

A finite detection limit can support `0 ≤ U ≤ u` only under stated sampling, calibration, background, and model assumptions. It cannot support `U = 0`. Exact zero is possible only as (a) a definitional or formal-model result conditional on assumptions, or (b) the vacuous case where `B` is the entire universe and there is no external verifier. Neither is empirical verification of a physically useful terminal-system counterexample.

## Consequence for the WO-3 falsifier

A documented positive dependency, co-exposure, rule edge, spatial exclusion, or shared-cause coupling can operationally reject terminality for a stated frame. The converse cannot be obtained by failing to find one. Replace the literal zero-crossing falsifier with two explicit products: **a scoped non-detection report with finite upper bounds**, and **a model-conditional proof claim** where assumptions are exposed for attack. Do not call either a verified all-medium zero.

## References

[1]: https://www.osti.gov/biblio/949367 "Identifying, understanding, and analyzing critical infrastructure interdependencies"

[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11787953/ "Logical interdependencies in infrastructure: What are they, how to identify them, and what do they mean for infrastructure risk analysis?"

[3]: https://nrcoe.inl.gov/publicdocs/CCF/NUREGCR-6268_Rev1.pdf "Common-Cause Failure Database and Analysis System: Event Data Collection, Classification, and Coding"

[4]: https://emtoolbox.nist.gov/publications/nisttechnicalnote1297s.pdf "Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results"

[5]: https://nvlpubs.nist.gov/nistpubs/sp958-lide/164-166.pdf "Limits for Qualitative Detection and Quantitative Determination"

[6]: https://goldbook.iupac.org/terms/view/R05263 "Relative detection limit"

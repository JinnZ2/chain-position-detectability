# WO-3 amended crossing profile

**Author:** Manus AI

**Status:** Validated amendment to the preregistered metric

## Purpose

The preregistered WO-3 metric correctly made terminality conditional on a named system, boundary, horizon, and lifecycle phase. The six independent medium audits showed that the original six rows were too coarse to serve as six scalar rates. This amendment preserves the preregistration as an audit trail while replacing those rows with a structured, multi-ledger profile.[1] [2]

## Frame

Every result begins with a frame:

`F = {system S, evolving boundary B(t), horizon H, lifecycle phase, inventory version}`.

Changing any element changes the claim. A post-operation interval cannot establish whole-life terminality. A material surface, property line, legal entity, event horizon, or procurement budget can each be a legitimate boundary, but they measure different things and must not be substituted silently.

## Event record

Each crossing or coupling is recorded once as an event with linked ledgers:

| Field | Required content |
|---|---|
| Event identity | Stable identifier shared by every ledger touched by the same event |
| Channel and carrier | Matter species, energy or momentum mode, information carrier, biological class, institutional relation, or dependency edge |
| Direction and endpoints | Inbound, outbound, or standing relation; source and recipient |
| Gross quantity | Inbound and outbound intervals kept separate; no net cancellation |
| Time | Event time or interval within `H` |
| Evidence status | **OBSERVED**, **DERIVED**, **MODELLED / CONDITIONAL**, **PLANNED**, or **UNRESOLVED** |
| Measurement basis | Instrument or procedure, sampling coverage, calibration, recovery or capture efficiency, detection threshold, and uncertainty |
| Provenance | Source, record version, and chain of custody |
| Causal status | Observed activation, inferred direction, modelled consequence, common cause, or unresolved |
| Overlap links | Other ledgers affected by the same event, preventing accidental double counting |

For channel `m`, the original gross crossing rate remains:

`Rm(B,H) = [Qm,in(B,H) + Qm,out(B,H)] / duration(H)`.

Every quantity is reported as an interval `[Lm, Um]`. A positive observed lower bound is sufficient to reject terminality for the declared frame. A non-detection gives a procedure- and horizon-specific upper bound; it does not make `Um = 0` unless the stated model and measurement procedure justify that value.

## Physical ledgers

The matter ledger records gross inward and outward mass or count by species, isotope, phase, size bin, and carrier. It declares whether the boundary is fixed, moving, porous, eroding, or growing. Counterflows are never netted because total mass can be constant while constituent exchange is positive.[3]

Energy and momentum require separate linked ledgers. Energy, linear momentum or impulse, angular momentum or torque, radiation by species and mode, and static or standing field constraints are not one measurand. A charged particle may populate matter and energy-momentum ledgers under one shared event identifier; those entries are not summed into a universal score.[4]

## Information, control, and biological ledgers

Information and control are separated by role. The profile distinguishes probe input, readout output, measurement back-action, commands, actuation, persistent set-points, authority, endpoints, codes, and record provenance. Correlation, common input, and shared history are not treated as directed transfer without stated causal assumptions.[5]

The biological profile is non-exclusive. It covers cells and propagules, virions, infectious proteins, extracellular vesicles and bioactive cargo, extracellular nucleic acids and mobile elements, and nonviable biological signatures. It records recipient effects such as establishment, persistence, infection, transformation, or assay interference, together with recovery and sensitivity limits.[6]

## Institutional and dependency ledgers

Human, legal, financial, and institutional relations are not reducible to transactions. The profile records active licences, duties, guarantees, authority, membership, contingent claims, relation counts, relation-days, and changes in those relations. A stand-ready obligation can remain active when no payment occurs during `H`.[7]

Dependency and exposure are represented as directed or shared edges. The profile distinguishes inbound enabling dependencies, common-cause links, co-location and shared hazards, logical or governance constraints, static-state or field coupling, and counterfactual exposure. Consequence remains **MODELLED / CONDITIONAL** unless an activation event is observed.[8]

## Classification rules

A system is **observed nonterminal within frame** when at least one observed channel has a positive lower bound or one observed external relation or dependency exists.

A system is **model-conditionally nonterminal within frame** when a positive crossing follows only from declared model assumptions. The label must not be shortened to an empirical finding.

A system is **unresolved** when no positive witness is established and at least one channel has an open or unknown upper bound, the inventory is incomplete, or the boundary cannot be operationalized.

A system is **terminal within a stipulated model** only when every enumerated channel and dependency has an upper bound of zero under the declared model. A finite empirical study may instead report a scoped non-detection above stated detection limits. It cannot certify universal, all-medium, all-time exact zero for the real system.

## Aggregation rule

The profile is a vector, not a scalar. Matter, joules, bits, obligations, dependent-hours, and expected harm have no natural common unit. A policy analysis may publish a scalar only after declaring normalization thresholds, weights, overlaps, and sensitivity analyses. Such a scalar measures materiality under those choices; it does not prove terminality.

## Falsifier status

The work order's literal falsifier remains logically coherent: one modelled system with zero crossings in every medium would refute the universal claim that no terminal system exists. The empirical version is not operational as an all-time certification. A finite instrument can detect a crossing or place bounded limits on specified channels. It cannot establish that the ontology is complete or that every possible crossing is exactly zero forever.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/crossing-metric.md "WO-3 crossing-rate metric and test protocol"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-3-terminal-system-accounting-boundary.md "WO-3 — The terminal system as an accounting boundary"

[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-matter.md "WO-3 matter and material-transfer audit"

[4]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-energy.md "WO-3 energy, momentum, radiation, and field-coupling audit"

[5]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-information.md "WO-3 information, observation, and control audit"

[6]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-biological.md "WO-3 biological-transfer audit"

[7]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-institutional.md "WO-3 human, legal, financial, and institutional audit"

[8]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/evidence/medium-dependency.md "WO-3 dependency, exposure, and causal-consequence audit"

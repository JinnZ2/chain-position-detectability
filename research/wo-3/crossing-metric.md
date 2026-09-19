# WO-3 crossing-rate metric and test protocol

**Author:** Manus AI

**Status:** Preregistered before case research

## Purpose

This protocol converts “terminal system” from an unbounded binary claim into a boundary- and horizon-specific measurement problem. It distinguishes proof that one channel is positive, which is sufficient to reject terminality, from proof that every possible channel is zero, which requires a complete inventory and upper bounds.

## Analysis frame

Each assessment declares four elements:

- the system, denoted `S`;
- the boundary, denoted `B`;
- the observation horizon, denoted `H = [t0, t1]`; and
- the lifecycle phase: construction, operation, dormancy, disposal, or afterlife.

Changing any element creates a different claim. In particular, beginning the clock after construction or ending it before disposal cannot establish whole-life terminality.

## Crossing ontology

A crossing is any transfer or causal coupling across `B` that changes, constrains, informs, burdens, or exposes something outside `S`, or that changes `S` from outside. The initial inventory contains six channel families:

| Channel | Quantity to record | Typical unit |
| --- | --- | --- |
| Matter | Mass or count entering and leaving | kilograms; particles; objects |
| Energy and momentum | Heat, work, radiation, force, vibration, or field-mediated transfer | joules; watts; newton-seconds |
| Information and control | Signals, observations, commands, records, measurements, or embodied messages | bits where measurable; otherwise event count |
| Biological | Organisms, cells, spores, genes, or viable propagules | count; biomass; probability of transfer |
| Human and institutional | Labor, maintenance, ownership, legal duties, liability, funding, and accounting claims | person-hours; transactions; obligations; currency |
| Dependency and exposure | External people or systems whose state, payoff, safety, or decisions depend on `S` | dependent count; dependent-hours; expected harm |

Lifecycle stages are not separate media. They determine when the six families must be measured. Double counting is acceptable for the terminality test because one positive witness is enough, but quantitative comparisons must state overlaps.

## Quantities

For each channel family `m`, let `Qm,in(B,H)` and `Qm,out(B,H)` be the cumulative absolute inbound and outbound quantities over the horizon. Opposite-direction flows are not netted because cancellation would conceal crossings.

The average crossing rate is:

`Rm(B,H) = [Qm,in(B,H) + Qm,out(B,H)] / duration(H)`.

For rare or stochastic crossings, record both expected cumulative quantity and the probability of at least one crossing:

`Em(B,H) = sum over events i of probability(i) × magnitude(i)`.

`Pm(B,H) = probability(at least one crossing in channel m during H)`.

Every reported value is an interval `[Lm, Um]`. A measured or source-supported event gives `Lm > 0`. A detection limit may support a finite `Um`, but “not observed” does not imply `Um = 0`.

External dependency is recorded separately as `D(B,H)`, with lower and upper bounds on the number of identifiable dependents or dependent-hours. Dependency can reject terminality even when the physical transfer that sustains it is accounted for elsewhere.

## Why the result is a vector

Matter, energy, information, obligations, and exposure do not share a natural unit. The primary result is therefore the vector:

`C(B,H) = { [Lm, Um], [LEm, UEm], [LPm, UPm] for every m; [LD, UD] }`.

No weighted total is used for the terminality decision. A scalar may be created for a policy comparison only by publishing medium-specific normalization thresholds and weights. Such a scalar measures materiality under those choices; it cannot prove zero crossings.

## Classification rule

A candidate is **nonterminal** when any channel has `Lm > 0`, `LEm > 0`, or `LPm > 0`, or when `LD > 0`.

A candidate is **unresolved** when no positive lower bound is established but any upper bound is positive, open, or unknown, or when the channel inventory may be incomplete.

A candidate is **terminal within scope** only when all enumerated channels have `Um = 0`, `UEm = 0`, and `UPm = 0`, `UD = 0`, and the inventory is complete for the stated boundary and horizon.

A **whole-life terminal** classification requires the terminal-within-scope result for construction, operation, dormancy, disposal, and afterlife. A positive witness in any phase rejects whole-life terminality.

## Falsifier attack

The work order’s proposed falsifier is a system with zero crossings in every medium. The first study tests whether that form is operationally complete. Reviewers will search for omitted channel families, boundary ambiguities, causal couplings without net flux, stochastic future crossings, and external dependents.

The literal universal claim has an observability problem: empirical confirmation of a candidate normally requires measurement or information transfer. The study will therefore distinguish three statements:

1. no crossing was detected;
2. all enumerated crossing rates are below stated detection bounds for a finite horizon; and
3. every possible crossing has an upper bound of exactly zero for all time.

Only the third satisfies the literal falsifier. The study will assess whether it is empirically attainable or instead requires a model-level proof.

## Asymptote tests

The three named candidates will be assessed with the same fields. The repository case will use an operating or formally assessed deep geological repository and will cover construction, institutional control, heat or radiation, groundwater or material release, and the regulatory performance horizon. The Voyager case will distinguish past lifecycle crossings from a hypothetical post-radio phase and will examine thermal radiation, radioactive decay, fields, particle interactions, embodied information, and possible future material transfer. The black-hole case will distinguish the event-horizon interior from the black hole as an external physical system, and will separate classical causal structure from accretion, gravitational dependence, and Hawking radiation.

An authoritative source must support every positive quantitative or qualitative crossing. Model-dependent black-hole findings will be labeled theoretical rather than observed.

## Cost-boundary study selection rule

A cost case qualifies only if the available record establishes all of the following:

1. a specific engineering control, test, design standard, or safety measure was available;
2. a decision-maker declined, removed, deferred, or weakened it;
3. contemporaneous evidence gives an ex-ante cost, saving, schedule value, or explicit cost rationale;
4. an authoritative investigation connects the omitted control to later harm or risk; and
5. an authoritative or methodologically transparent source supports at least one downstream cost category.

Candidate discovery is bounded and may return a null. If several cases qualify, the case with the strongest documentary chain and most reproducible quantities is selected. The redraw will report the original decision-boundary cost, added direct organizational costs, transferred public or third-party costs, long-horizon liabilities, and unmonetized harms. It will not monetize deaths or injuries unless the original decision record used an explicit valuation and the use is necessary for like-for-like comparison.

## Reproducibility and interpretation

All sources, assumptions, unit conversions, date horizons, and uncertainty bounds will be published. A positive crossing refutes terminality for the declared frame. Failure to locate a positive crossing does not establish a zero upper bound. The final report will separate observed facts, calculations, theoretical implications, and unresolved claims.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-3-terminal-system-accounting-boundary.md "WO-3 — The terminal system as an accounting boundary"

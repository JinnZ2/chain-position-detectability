# WO-3 evidence record — Voyager 1 and the stipulated post-radio asymptote

**Case ID:** `voyager-1-post-radio`
**Protocol:** `research/wo-3/crossing-metric.md`
**Research-status date:** 19 September 2026
**Candidate condition:** Voyager 1 after **permanent cessation of intentional radio transmission**.

## Decision

**OBSERVED — whole-life result.** Voyager 1 is nonterminal over its historical and operational life. The spacecraft was launched on 5 September 1977, and documented construction, launch, mission operation, communications, instrument management, and scientific measurement supply positive crossings during that life. A positive witness in any lifecycle phase rejects a whole-life-terminal classification under the protocol. This finding does not depend on a forecast of the spacecraft's later condition. [1] [6] [7] [13]

**MODELLED / CONDITIONAL — stipulated post-radio result.** If intentional radio transmission has permanently ceased at a finite stipulated time `t0`, Voyager retains its cited three-MHW-RTG configuration and fuel, and the rejected decay heat escapes the spacecraft-only boundary, then Voyager 1 is model-conditionally nonterminal during `[t0, t0 + 1 Julian year]`. Under the stated decay-only model and the illustrative `t0 = 1 January 2035` rounding convention, modeled outbound heat is `1.34 × 10^11 J`. This is a conditional physical-model implication, not an observed lower bound for the future spacecraft.

**UNRESOLVED — actual post-radio and all-time result.** Permanent radio silence has not been established. Official 2026 material records continued Voyager 1 operations: the low-energy charged-particle instrument was shut down on 17 April 2026 while two instruments remained, and NASA's current status material still lists the magnetometer and plasma-wave subsystem as on. The actual future one-year interval, the spacecraft's configuration at its beginning, other future channels, and all-time behavior therefore have no empirical terminal or nonterminal certification in this record. [6] [7]

| Claim | Declared boundary and horizon | Evidence status | Classification |
| --- | --- | --- | --- |
| Whole life to the research-status date | The evolving Voyager 1 system from construction and launch through documented 2026 operation; lifecycle-wide boundary | **OBSERVED** positive historical crossings | **Nonterminal** |
| Stipulated post-radio scenario | Moving material surface immediately outside Voyager 1; `[t0, t0 + 1 Julian year]` | **MODELLED / CONDITIONAL** positive decay-heat implication | **Model-conditionally nonterminal** |
| Actual post-radio or all-time isolation | The same spacecraft-only boundary after an unobserved permanent shutdown, including afterlife | **UNRESOLVED** | No empirical classification |

The candidate is thus an asymptote, not a demonstrated terminal instance. The word **nonterminal** is retained only for the observed whole-life claim and the explicitly conditional finite-horizon model claim above; it is not used as an empirical classification of the unobserved 2035 interval or of every future time.

## Declared frame

### System and boundary

**OBSERVED / defined object.** `S` is Voyager 1: its structure, electronics, high-gain antenna, three RTGs and contents, Golden Record, and protective cover. `B` is a notional moving material surface immediately outside those items. The exterior includes the interstellar medium, photons once emitted, external fields and particles, Earth, the Deep Space Network, operators, manufacturers, launch systems, and future bodies. Opposing flows are not netted.

**PLANNED analytic choice.** This narrow spacecraft-only boundary is an analytic choice intended to test isolation of the individual craft. Calling it the “most favourable” boundary for isolation is an evaluative judgment, not an observed fact. Changing the system, boundary, horizon, or lifecycle phase changes the claim.

### Horizons

**OBSERVED historical horizon.** The whole-life finding covers construction, launch, and documented operation through the research-status date. It begins before the candidate's proposed radio-silence condition because beginning at a later phase cannot erase earlier crossings.

**PLANNED scenario horizon.** The prospective post-radio horizon is `[t0, t0 + 1 Julian year]`, where `t0` is the time at which intentional radio transmission has permanently ceased. `t0 = 1 January 2035` is an illustrative calculation convention only. NASA's March 2025 outlook said that at least one instrument might operate into the 2030s, subject to unforeseen problems; it did not establish either a 2035 date or permanent radio silence. Later 2026 updates supersede its use as a current-status forecast. [5] [6] [7]

## RTG heat: documented inputs and conditional model

### Source-grounded inputs

| Input | Value | Evidence status and limit |
| --- | ---: | --- |
| RTG inventory | 3 per Voyager | **OBSERVED / documented design fact.** JPL identifies three RTGs and Pu-238 decay heat as their energy source. It is not observation of the craft's state at future `t0`. [1] |
| MHW-RTG electrical output at beginning of mission | 158 W per RTG on NASA's current web page | **OBSERVED / documented beginning-of-mission specification.** This number is not used in the heat calculation. [2] |
| MHW-RTG thermal heat-rejection requirement at beginning of mission | 2,243 W per RTG | **OBSERVED / documented beginning-of-mission specification.** The NASA reference identifies MHW-RTG as developed for Voyager and describes radiation from its housing and fins. [3] |
| Pu-238 half-life | 88 years | **OBSERVED / documented agency technical fact.** [4] |
| Cessation date | 1 January 2035 | **PLANNED calculation convention.** It is neither a forecast confirmation nor an observed mission event. |

### Conditional calculation

**MODELLED / CONDITIONAL.** Let `P0 = 3 × 2,243 W = 6,729 W`. Retaining only decay of Pu-238 and using an intentional rounded elapsed time of exactly 58 years since the 1977 launch gives:

\[
P(t_0)=6{,}729\,2^{-58/88}=4{,}261.322\ \mathrm{W}.
\]

Integrating this declining source over one Julian year gives:

\[
Q_{\mathrm{model}}=P(t_0)\frac{88}{\ln 2}\left(1-2^{-1/88}\right)(31{,}557{,}600\ \mathrm{s})
=1.3394888\times10^{11}\ \mathrm{J}.
\]

The corresponding modelled mean is `4.244584 kW` (about `4.24 kW`), not `≥ 4.25 kW`. The initial modelled power at `t0` is about `4.26 kW`. The common shortcut `4.25 kW × 1 year` is not the integrated mean and should not be reported as one.

**MODELLED / CONDITIONAL interpretation.** Within this model, the source is strictly positive at every finite post-launch time `Y`:

\[
Q_{\mathrm{model,1y}}(Y)=2.11517\times10^{11}\,2^{-Y/88}\ \mathrm{J}>0.
\]

The result requires all of the following: the cited RTGs and relevant fuel configuration remain with `S`; decay-only scaling is adequate for the stated purpose; `t0` is finite; and rejected heat radiates beyond `B` rather than being stored within `S` for the full year. It does **not** establish an empirical metric lower bound `L > 0` for the actual future spacecraft. It is a positive quantity only in the stated model.

The 58-year convention is deliberately conservative for a declining source, but it is not the calendar interval. From 5 September 1977 to 1 January 2035 is about `57.3224` Julian years. Using that calendar interval instead produces `P(t0) ≈ 4.2841 kW` and `Qmodel ≈ 1.3467 × 10^11 J`. Both presentations are permissible only when their time convention is stated.

The calculated RTG heat must not be added to radiation from the warmed spacecraft bus without an energy partition. In general, bus radiation is a later route for the same internally transferred RTG energy, not an independent additional witness.

### What could defeat the conditional heat calculation

**UNRESOLVED until evidence exists.** The model calculation would fail if evidence showed that the relevant RTG inventory or fuel configuration was absent, that the MHW specification was inapplicable, that an unmodelled event removed or materially changed the heat source before `t0`, or that the boundary had been redefined to include the emitted radiation. A breakup or loss of RTG material from `S` would invalidate this heat calculation; it would not demonstrate terminality and could instead furnish a distinct matter-crossing witness. Future telemetry could refine a physical model, but it cannot retrospectively make the conditional calculation an observation of an unobserved interval.

## Crossing vector and channel limits

| Channel | Historical evidence | Post-radio scenario result | Status for actual future horizon |
| --- | --- | --- | --- |
| Matter and plasma | Voyager 1 plasma-wave observations measured local plasma oscillations associated with an electron density of about `0.08 cm⁻³`; later work reports persistent waves over roughly 30 AU of local interstellar space. [9] [10] | No effective-area, orientation, spectrum, or integrated flux model is asserted here. | **UNRESOLVED**; historical observations do not supply a numerical 2035 lower bound. |
| Energy and momentum — outbound | RTG heat rejection was designed to be radiated from the housing and fins at beginning of mission. [3] | `Qmodel = 1.3394888 × 10^11 J` for the rounded 2035 convention if the stated assumptions hold. | **MODELLED / CONDITIONAL**, not empirical `Lenergy,out`. |
| Energy and momentum — inbound | A 2012 Voyager 1 study observed a sharp change in galactic cosmic rays and low-energy ion conditions. [11] | No bundle of fields, radiation, particles, or gravitation is treated as observed for future `H` without channel-specific evidence. | **UNRESOLVED**. |
| Information/control — intentional radio | Current mission activity confirms that the stipulated end-state has not been observed. [6] [7] | The candidate sets intentional outbound radio to zero only if permanent cessation occurs. | **PLANNED condition**, not verified fact. |
| Information — embodied record | The Golden Record is an internal stock while it remains inside `B`. NASA documents its images, sounds, music, greetings, cartridge, needle, and instructions; the Voyager 1 mission page identifies the disk as gold-plated copper. [12] [13] | It is not a separately transferring artifact absent breakup, impact, recovery, or removal. | **UNRESOLVED** future transfer; no flux is inferred from stock alone. |
| Biological | No positive post-radio biological transfer evidence was located. | A collision, habitable recipient, viable material, and transfer mechanism are not assumed. | **UNRESOLVED**, not zero. |
| Human/institutional and dependency/exposure | Ongoing mission management and instrument changes are documented in 2026. [6] [7] | Whether obligations, stewardship, observation, or dependents continue after a genuine permanent shutdown needs separate evidence. | **UNRESOLVED** after `t0`. |

Radio silence concerns an intentional information/control channel. It does not by itself eliminate thermal photons, particle interactions, embodied information, or other crossings. Conversely, neither historical plasma and cosmic-ray measurements nor the Golden Record's content is evidence of a quantified crossing in the stipulated future year. The record therefore does not convert an unobserved channel into zero merely because it lacks a projected number.

## Lifecycle assessment

| Phase | Finding | Evidence status and implication |
| --- | --- | --- |
| Construction and launch | Voyager 1 was built and launched from Earth on 5 September 1977. [13] | **OBSERVED** launch and human-built mission fact. Detailed labor, industrial, energy, and supply-chain transfers are **DERIVED** implications of that documented construction and launch, not separately quantified here. This phase rejects whole-life terminality. |
| Historical and current operation | Mission communications, instrument management, and scientific measurement occurred; 2026 updates record continued operations and an instrument shutdown. [6] [7] | **OBSERVED** positive operational crossings. This phase independently rejects whole-life terminality. |
| Stipulated dormancy | The RTG calculation predicts outward decay heat if the model conditions at a finite `t0` hold. | **MODELLED / CONDITIONAL** post-radio nonterminality only. |
| Disposal | No controlled disposal conclusion is drawn from the reviewed record. | **UNRESOLVED.** Failure to locate a plan is not a positive fact and is not a zero-crossing result. |
| Afterlife | Voyager 1's trajectory, an eventual encounter, erosion, breakup, recovery, collision, biological transfer, and future dependency are not quantified in this record. The heat model remains positive at every finite time only while its assumptions apply. [8] | **UNRESOLVED** for actual all-time behavior. The historical phases, not a forecasted afterlife, support the whole-life result. |

## Source conflicts and recency controls

**OBSERVED source conflict — MHW electrical output.** NASA's current RPS web page gives 158 W electrical output at beginning of mission, while the 2016 NASA reference-book table gives 157 W for MHW-RTG. This one-watt nominal or rounding discrepancy is preserved rather than harmonized. It does not affect the heat calculation, which uses the reference book's separate 2,243-W thermal heat-rejection value. [2] [3]

**OBSERVED source-version conflict — operational outlook.** The March 2025 article offered a contingent outlook into the 2030s. It is not evidence of a permanent shutdown, and later 2026 material records continued operation, the April LECP shutdown, and continuing power-management changes. The later material controls any statement about present status; neither source establishes the final radio date. [5] [6] [7]

**OBSERVED chronological tension — plasma instrument.** A 2013 JPL account describes Voyager 1's plasma instrument as having stopped working in 1980, while NASA's current status table lists the Plasma Science instrument as off because of degraded performance on 1 February 2007. These may describe loss of useful operation and a later formal shutdown, but the supplied records do not reconcile them. They are retained as distinct descriptions and the 2013 account is not used as current-status evidence. [7] [8]

## Ontology and evidentiary boundary

**UNRESOLVED — literal exact zero.** The work order's literal falsifier requires zero crossings in every medium. Under the protocol, a terminal-within-scope finding needs complete channel inventory and zero upper bounds for every enumerated channel over its declared finite horizon; a literal every-medium, all-time claim is stronger still. Observation of a future spacecraft state would itself require an information crossing. Accordingly, this record does not empirically prove that the actual future Voyager configuration has zero upper bounds in every channel, and it does not infer from the conditional heat model that every possible system is nonterminal for all time.

**OBSERVED and MODELLED limits.** Historical construction and operation are sufficient to reject whole-life terminality for Voyager 1. Separately, the decay calculation supplies a conditional finite-horizon nonterminal implication. Neither finding certifies the actual future post-radio interval, proves every other future channel positive, or converts the absence of an observation into an exact-zero upper bound. The bounded cost null above is retained independently: it supplies neither evidence of externalization nor a cost-based exemption.

## References

[1]: https://www.jpl.nasa.gov/images/pia25782-voyagers-rtg/ "Voyager's RTG — NASA Jet Propulsion Laboratory"

[2]: https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/power-radioisotope-thermoelectric-generators/ "Power Generators — NASA Radioisotope Power Systems"

[3]: https://ntrs.nasa.gov/api/citations/20160001769/downloads/20160001769.pdf "Radioisotope Power Systems Reference Book for Mission Designers and Planners — NASA Technical Reports Server"

[4]: https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/faq/ "Frequently Asked Questions — NASA Radioisotope Power Systems"

[5]: https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/ "NASA Turns Off 2 Voyager Science Instruments to Extend Mission"

[6]: https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/ "NASA Shuts Off Instrument on Voyager 1 to Keep Spacecraft Operating"

[7]: https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/ "Where Are Voyager 1 and Voyager 2 Now? — NASA"

[8]: https://www.jpl.nasa.gov/news/how-do-we-know-when-voyager-reaches-interstellar-space/ "How Do We Know When Voyager Reaches Interstellar Space? — NASA Jet Propulsion Laboratory"

[9]: https://www.science.org/doi/abs/10.1126/science.1241681 "In Situ Observations of Interstellar Plasma with Voyager 1 — Science"

[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740711/ "Persistent Plasma Waves in Interstellar Space Detected by Voyager 1 — Nature Astronomy"

[11]: https://www.science.org/doi/abs/10.1126/science.1236408 "Voyager 1 Observes Low-Energy Galactic Cosmic Rays in a Region Depleted of Heliospheric Ions — Science"

[12]: https://science.nasa.gov/mission/voyager/golden-record-contents/ "Golden Record Contents — NASA"

[13]: https://www.jpl.nasa.gov/missions/voyager-1/ "Voyager 1 — NASA Jet Propulsion Laboratory"

[14]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole "Astronomers Capture First Image of a Black Hole — Event Horizon Telescope"

[15]: https://science.nasa.gov/universe/black-holes/ "Black Holes — NASA Science"

[16]: https://inis.iaea.org/records/s0epc-ydc62 "Safety Case for the Disposal of Spent Nuclear Fuel at Olkiluoto — Synthesis 2012"

[17]: https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1483_web.pdf "Geological Disposal Facilities for Radioactive Waste — IAEA Safety Guide SSG-14"

[18]: https://www.posiva.fi/en/index/finaldisposal/long-termsafety.html "Long-term Safety — Posiva Oy"

[19]: https://link.springer.com/article/10.1007/BF02345020 "Particle Creation by Black Holes — S. W. Hawking"

**Publication status:** Reconciled after independent validation.

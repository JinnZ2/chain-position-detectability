# Independent validation — `voyager-1-post-radio`

**Verdict:** **needs correction**. **Not publication-ready** in its present form.

The record retains a strong but narrower finding. **Voyager 1 is observably nonterminal over its historical/operational life. Its proposed post-radio result is only a model-conditional nonterminal result, not an empirical certification of an as-yet unobserved future interval.** NASA’s current status still lists Voyager 1’s magnetometer and plasma-wave subsystem as on; its low-energy charged-particle instrument was shut down on 17 April 2026. Thus, the stipulated permanent radio-silence event has not been established. [6] [7]

After correction, at least one positive crossing remains: assuming an intact onboard MHW radioisotope thermoelectric-generator (RTG) inventory at the stipulated finite date and decay-only scaling, heat rejection remains strictly positive and must leave the spacecraft-only boundary. This is a **derived physical-model result**. It is not a measurement of Voyager in 2035, nor proof about every future channel or all time.

## Frame and decision check

The system and moving material boundary are explicit and conform to the protocol. Excluding Earth, operators, the Deep Space Network, and the surrounding medium makes this a narrow spacecraft-only claim; calling it the “most favourable” boundary is a **proposed analytic judgment**, not an observed fact. The one-year horizon is permissible as a finite, phase-specific test, and the record correctly says it cannot establish whole-life terminality.

The key defect is temporal. The draft says its horizon begins when intentional transmissions “permanently cease,” but replaces that unobserved event with `1 January 2035`. NASA’s March 2025 article supported only a contingent forecast into the 2030s; later NASA updates show that Voyager 1 remained operational in 2026, with two science instruments on, and an energy-saving modification still planned for it. [5] [6] [7] The result must therefore be titled and classified as follows:

> **Conditional scenario:** If intentional radio transmission has permanently ceased at the stipulated `t0`, and the spacecraft retains the cited RTG/fuel configuration, Voyager 1 is model-conditionally nonterminal over `[t0, t0 + 1 Julian year]` because modeled outbound decay heat is positive.

It must not be reported as an observed 2035 condition or as an empirical lower bound for the actual future spacecraft.

## RTG evidence and arithmetic

The documentary inputs are substantially sound. JPL confirms three RTGs per Voyager and that they generate electricity from plutonium-238 decay heat. [1] NASA identifies the MHW-RTG as the Voyager power source and gives 158 W electric at beginning of mission. [2] The NASA reference book specifically says MHW-RTG was developed for Voyager; its table gives **2,243 W thermal heat-rejection requirement at beginning of mission**, and explains that this heat was rejected by radiation from the housing and fins. [3] NASA gives the 88-year Pu-238 half-life. [4]

The evidence labels require one correction: these are **documented design and beginning-of-mission specifications**, not observations that Voyager 1 retains the same condition at a future `t0`. The future heat result is therefore **DERIVED / model-conditional**. The phrase “lower bound” is acceptable only inside that model and after explicitly including intact fuel/configuration and radiative escape as assumptions. It is not a source-supported observed event in the proposed 2035 horizon under the metric’s usual `L > 0` rule.

Using the draft’s explicit conservative simplification of exactly 58 years since 1977 gives:

\[
P_0=3(2{,}243)=6{,}729\ \mathrm{W},\qquad
2^{-58/88}=0.6332772207,
\]

\[
P(t_0)=4{,}261.322\ \mathrm{W},\qquad
Q_{1\,\mathrm{Julian\ year}}=1.3394888\times10^{11}\ \mathrm{J}.
\]

Accordingly, **`1.34 × 10^11 J` is arithmetically correct at the stated precision**. The integrated mean is **4.244584 kW**, however. The draft’s claim `R ≥ 4.25 kW` is not supported by its own 58-year calculation: `4.25 kW` exceeds that mean. Report either `R = 4.2446 kW` under the model, `≈4.24 kW` at three significant figures, or the initial instantaneous value `P(t0) = 4.2613 kW` (`≈4.26 kW`) and label it as such.

The wording “58 years from launch to 1 January 2035” is date-inexact. The elapsed calendar interval from the cited 5 September 1977 launch is about **57.3224 Julian years**, not 58. With that calendar convention, the same model gives `P(t0) = 4.2841 kW` and `Q = 1.3467 × 10^11 J`. The 58-year calculation is conservative for a declining source, but it must be described as an intentional rounding convention rather than the actual elapsed time. The general coefficient is `2.11517 × 10^11 2^{-Y/88} J`; the draft’s rounded `2.12 × 10^11 2^{-Y/88} J` is correct.

Do not treat warmed-spacecraft-bus radiation as an additional quantity “before counting” it: it is generally the same RTG energy after an internal transfer and would overlap the RTG heat witness. It can be described as a route of escape, but not added without an energy partition. Likewise, a breakup, loss of the RTG/fuel from `S`, or a boundary redefinition could invalidate this **heat calculation** without contradicting the historical RTG sources; such an event would likely supply a different matter-crossing witness. The draft’s falsifier list must include this distinction.

## Channel, lifecycle, and status-label audit

| Item in the draft | Independent validation | Required correction |
|---|---|---|
| RTG count, MHW identity, beginning-of-mission heat rejection, and 88-year half-life | Supported by primary NASA/JPL records. [1] [2] [3] [4] | Keep as documented design facts; do not label them observations of a future `t0` state. |
| Outbound thermal witness in the post-radio year | Correctly derived arithmetic, subject to the model assumptions above. The source supports radiation at beginning of mission, not future telemetry. [3] | Label **DERIVED / model-conditional**; replace the mean-rate claim and remove any implication of present measurement. |
| Inbound plasma and cosmic rays | The cited studies directly observed Voyager 1’s local plasma environment and particle changes in 2012–2020. [8] [9] [10] | Those are valid **historical observations**. They do not establish a numerical lower bound in the hypothetical 2035 year. For that horizon, call the channel unresolved or a separately labeled extrapolation. |
| “Fields, electromagnetic radiation, and gravitational fields reach Voyager” | The cited particle/plasma papers do not individually substantiate every listed physical process during `H`. | Do not label the entire bundle **OBSERVED qualitative** for the future year. State only the historically measured interactions, or supply channel-specific sources and models. |
| Intentional outbound radio equals zero | Properly framed as stipulated, not verified. Current official status shows the spacecraft remains active now. [6] [7] | Keep **PROPOSED condition** and do not let it imply that all electromagnetic emission is zero. |
| Golden Record stock | It is correctly distinguished from a boundary flux while the intact artifact remains inside `B`. NASA supports the contents, protective jacket, needle, and symbolic instructions. [11] | Draft citation [9] does **not** support “gold-plated copper”; cite the Voyager 1 mission page for that material. [12] Retain collision/recovery as unresolved. |
| Current human/institutional dependence | The post-`t0` entry is correctly unresolved, but the supporting citations are historical rather than current. | Cite 2026 mission-status material for the present state; do not call 2018 or 2025 accounts “current.” [6] [7] |
| Construction, operation, dormancy, disposal, and afterlife table | Launch and the historical/operational phases establish nonterminality over whole life; a post-radio start cannot erase them. The prospective disposal and afterlife rows remain open. [6] [12] | Mark construction’s detailed labor/industrial list as **derived from the documented human-built launch**, not independently observed by the cited pages. Do not turn lack of a located disposal plan into a positive fact. |

## Citation and official-source audit

The draft’s citations are checked below by their draft numbers. “Partial” means that the link supports some cited text but not the full proposition or its time status.

| Draft citation | Validation result |
|---|---|
| [1] | **Matches.** JPL supports three RTGs per Voyager and the Pu-238 heat-to-electricity mechanism. [1] |
| [2] | **Matches.** NASA identifies MHW-RTG as Voyager’s source and gives 158 W electric at beginning of mission. [2] |
| [3] | **Matches the heat input.** The NASA book gives 2,243 W thermal heat rejection at beginning of mission and radiation from the housing/fins. [3] |
| [4] | **Matches.** NASA gives Pu-238 a relatively short 88-year half-life and predictable power decline. [4] |
| [5] | **Historically accurate but stale as “current planning.”** Its 2025 contingent 2030s statement has been overtaken by 2026 operational updates. [5] [6] [7] |
| [6]–[8] | **Match historical scientific observations.** They cannot certify a particle/plasma lower bound for the unobserved post-radio year. [8] [9] [10] |
| [9] | **Partial.** It supports contents, analog images, jacket, cartridge, needle, and instructions, but not the stated gold-plated-copper material. [11] [12] |
| [10] | **Partial/stale for “presently.”** It supports DSN/Voyager context and the longevity statement, but is a 2018 Voyager 2 release, not current Voyager 1 operations. [6] [7] [13] |
| [11]–[12] | **Match the limited trajectory/launch claims.** The former is an older account and must not be used for current instrument status. [12] [13] |
| [13]–[14] | **Match with the draft’s stated distinction.** The EHT observed a ring-like image/shadow and inferred M87*’s mass; NASA describes event-horizon theory and indirect detection. Neither observes an escape from inside an event horizon. [14] [15] |
| [15]–[17] | **Match the repository control when read as safety assessment, not empirical zero-crossing proof.** TURVA-2012 is a construction-licence safety case; IAEA/Posiva support the lifecycle, monitoring, barriers, uncertainty, and finite-horizon framing. [16] [17] [18] |
| [18] | **Partial.** Hawking’s paper supports the theoretical emission/mass-loss claim. It is not evidence for the separate negative assertion that astrophysical Hawking flux has not been detected; provide a source for that assertion or leave it as an uncited scope statement. [19] |

### Official-source date/version conflicts

1. **MHW electrical output:** NASA’s current web page reports 158 W electric at beginning of mission, while the 2016 NASA reference book’s MHW table reports 157 W electric. This is a 1-W nominal/rounding discrepancy. It does not alter the heat calculation, which uses 2,243 W thermal rejection, but both values should be reported rather than silently harmonized. [2] [3]
2. **Voyager operational outlook:** the 2025 article forecast at least one instrument into the 2030s, subject to unforeseen failures. In April 2026 NASA shut Voyager 1’s LECP and said two science instruments remained; in August 2026 it said a further Voyager 1 power modification was planned. These are updates to a contingent forecast, not evidence that permanent radio silence occurred. [5] [6] [7]
3. **Older instrument chronology:** the 2013 JPL account says Voyager 1’s plasma instrument stopped working in 1980, whereas NASA’s current status table lists the Plasma Science instrument as off because of degraded performance on 1 February 2007. Treat these as different historical descriptions (loss of useful operation versus formal shutdown) unless NASA supplies a reconciliation; do not use the 2013 page as a current-status source. [7] [13]

## Cost gates: no qualifying cost case

No cost candidate is actually offered or scored in this Voyager record. The black-hole and repository passages are controls, not decision records. Applying the preregistered selection rule strictly, the record fails to establish all five required gates: no identified available engineering control, no documented decision-maker decline/deferral, no contemporaneous ex-ante cost rationale, no authoritative investigation connecting an omitted control to later harm or risk, and no methodologically supported downstream cost category. Therefore **no cost case qualifies**. No cost finding may be inferred from the Voyager heat model, repository safety case, or general statements about externalization. This avoids folklore, cross-control cost transfer, overlapping totals, and unsupported but-for causation.

## Ontology and evidentiary limit

The record correctly keeps the Golden Record as an internal information stock and treats collision, biological transfer, recovery, and future dependence as unresolved. It also correctly separates observed external black-hole effects from classical and semiclassical claims, and treats the repository safety case as an assessment rather than proof of absolute containment.

The Voyager heat argument nevertheless overreaches if read as empirical certification. Observing a future spacecraft state would itself require an information crossing; none has occurred for the stipulated post-radio period. Agency design documentation plus energy-conservation reasoning can establish a **conditional model implication**: if the stated spacecraft configuration exists at finite `t0`, the modeled decay-heat crossing is positive. They cannot empirically prove the actual future configuration, a zero upper bound for every other channel, or all-time nonterminality from that one modeled witness. Conversely, the historical launch and current operations are empirical positive crossings and already reject **whole-life terminality** without reliance on the 2035 scenario.

## Publication disposition

Revise the title, decision, vector, rate, evidence labels, current-status citations, Golden Record material citation, and falsifier language as specified above. After revision, the publishable conclusion is: **observed whole-life nonterminality; model-conditional post-radio nonterminality; no empirical certification of the future post-radio frame or universal claim.**

## References

[1]: https://www.jpl.nasa.gov/images/pia25782-voyagers-rtg/ "Voyager's RTG — NASA Jet Propulsion Laboratory"

[2]: https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/power-radioisotope-thermoelectric-generators/ "Power Generators — NASA Radioisotope Power Systems"

[3]: https://ntrs.nasa.gov/api/citations/20160001769/downloads/20160001769.pdf "Radioisotope Power Systems Reference Book for Mission Designers and Planners — NASA Technical Reports Server"

[4]: https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/faq/ "Frequently Asked Questions — NASA Radioisotope Power Systems"

[5]: https://science.nasa.gov/blogs/voyager/2025/03/05/nasa-turns-off-2-voyager-science-instruments-to-extend-mission/ "NASA Turns Off 2 Voyager Science Instruments to Extend Mission"

[6]: https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/ "NASA Shuts Off Instrument on Voyager 1 to Keep Spacecraft Operating"

[7]: https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/ "Where Are Voyager 1 and Voyager 2 Now? — NASA"

[8]: https://www.science.org/doi/abs/10.1126/science.1241681 "In Situ Observations of Interstellar Plasma with Voyager 1 — Science"

[9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740711/ "Persistent Plasma Waves in Interstellar Space Detected by Voyager 1 — Nature Astronomy"

[10]: https://www.science.org/doi/abs/10.1126/science.1236408 "Voyager 1 Observes Low-Energy Galactic Cosmic Rays in a Region Depleted of Heliospheric Ions — Science"

[11]: https://science.nasa.gov/mission/voyager/golden-record-contents/ "Golden Record Contents — NASA"

[12]: https://www.jpl.nasa.gov/missions/voyager-1/ "Voyager 1 — NASA Jet Propulsion Laboratory"

[13]: https://www.jpl.nasa.gov/news/how-do-we-know-when-voyager-reaches-interstellar-space/ "How Do We Know When Voyager Reaches Interstellar Space? — NASA Jet Propulsion Laboratory"

[14]: https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole "Astronomers Capture First Image of a Black Hole — Event Horizon Telescope"

[15]: https://science.nasa.gov/universe/black-holes/ "Black Holes — NASA Science"

[16]: https://inis.iaea.org/records/s0epc-ydc62 "Safety Case for the Disposal of Spent Nuclear Fuel at Olkiluoto — Synthesis 2012"

[17]: https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1483_web.pdf "Geological Disposal Facilities for Radioactive Waste — IAEA Safety Guide SSG-14"

[18]: https://www.posiva.fi/en/index/finaldisposal/long-termsafety.html "Long-term Safety — Posiva Oy"

[19]: https://link.springer.com/article/10.1007/BF02345020 "Particle Creation by Black Holes — S. W. Hawking"

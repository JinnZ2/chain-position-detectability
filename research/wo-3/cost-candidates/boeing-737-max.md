# WO-3 cost-boundary candidate record — Boeing 737 MAX MCAS AOA-input logic and AOA DISAGREE alert

**Candidate ID:** `boeing-737-max-sensor-redundancy-safety-alerts`
**Decision:** **DOES NOT QUALIFY — bounded null cost-case result.**
**Research date:** 2026-09-19
**Currency convention:** Amounts are retained in the original U.S. dollars and source years. No inflation adjustment or cross-category total is calculated.

## Bottom line

**DERIVED.** This candidate fails the preregistered five-gate selection rule and **does not qualify** as a WO-3 cost-boundary case. The cited record establishes important technical and program-level facts: pre-crash MCAS operated from one angle-of-attack (AOA) input at a time; the intended standard AOA DISAGREE alert was inadvertently made dependent on the optional AOA indicator; and the alert correction was deferred after its 2017 discovery. It also documents downstream Boeing and public monetary categories after the accidents and grounding. [2] [3] [5] [7] [8] [10]

**UNRESOLVED.** For neither exact technical control does a cited contemporaneous decision-period source provide an ex-ante price, avoided cost, or quantified schedule value. The documented training and certification-cost rationale concerns how MCAS was described to certification authorities and crews, not the selection of single-input MCAS logic or the deferral of the standalone alert. It cannot be transferred across controls. Gate 3 therefore fails for each control. This is a **bounded null**: it means that the cited record does not establish the required same-control cost/value link. It does not assert that no such record exists anywhere.

The often-repeated `$80,000` warning-light proposition is not used. No qualifying decision-period source for that proposition is cited in this record, and it is not evidence for either gate result.

## Declared assessment frames and limits

**OBSERVED.** The protocol requires the system, boundary, horizon, and lifecycle phase to be declared; changing any of them creates a different claim. [1]

| Frame | System and boundary | Horizon | Permitted use in this record |
| --- | --- | --- | --- |
| `S1`, `B0-1` | The MCAS AOA-input-logic decision; the unknown incremental ex-ante decision-cost boundary | 2015–16 design and certification period | Assess the five gates. `B0-1` is not observed. |
| `S2`, `B0-2` | The standalone AOA DISAGREE alert correction/deferral; the unknown incremental ex-ante decision-cost boundary | 2017 discovery through the planned 2020 update | Assess the five gates. `B0-2` is not observed. |
| `B1` | Documented post-accident Boeing, customer, public, and regulatory financial or institutional obligations | Each source's stated 2019–21 reporting or settlement horizon | Record separate downstream categories without allocation to `S1` or `S2`. |

**DERIVED.** There is no observed “original decision boundary” for either control because Gate 3 is not met. `B0-1` and `B0-2` are therefore unknown, not reconstructed. `B1` is a proposed analytical boundary for showing documented crossings beyond an unobserved incremental-decision boundary; it is not proof of a before-and-after cost comparison.

## Strict five-gate result

| Exact control | 1. Available | 2. Declined, removed, deferred, or weakened | 3. Same-control ex-ante cost/value | 4. Authoritative risk/harm link | 5. Downstream cost category | Strict result |
| --- | --- | --- | --- | --- | --- | --- |
| **MCAS AOA-input comparison/inhibit logic** | **MODELLED / CONDITIONAL.** Two installed sensors and the later monitor/inhibit modification are established, but the cited record does not establish this exact comparator/inhibit design as an available 2015–16 decision alternative. Later implementation establishes feasibility no later than return to service, not contemporaneous availability. [2] [3] [4] | **OBSERVED — pass at architecture level.** The House investigation records the vulnerability concern and delivery with MCAS using one input at a time. [2] | **UNRESOLVED — fail.** No cited contemporaneous price, avoided cost, or quantified schedule value for this design choice. | **OBSERVED — pass for risk/harm connection only.** The FAA identifies the single erroneous-AOA/repeated-nose-down-trim unsafe condition; accident records document the relevant failure sequence. This is not a but-for allocation of harm. [3] [4] [6] [9] | **OBSERVED — pass only at program level.** Audited and DOJ categories exist but are not allocated to this control. [7] [8] [10] | **Does not qualify.** Gate 3 fails, and Gate 1 is not contemporaneously established. |
| **Standalone AOA DISAGREE alert** | **OBSERVED — pass.** It was a required standard standalone type-design feature, although delivered software made it dependent on the optional AOA indicator. [2] [5] | **OBSERVED — pass.** The delivered dependency and the 2017-to-2020 correction deferral are documented. [2] [5] [6] | **UNRESOLVED — fail.** A planned future release date is not a schedule value, and no same-control price or avoided-cost record is cited. | **OBSERVED — limited pass for risk/diagnosis only.** The Lion Air investigation links the absent alert to non-reporting and the AOA-disagree maintenance path. It does not establish that restoring the alert would have prevented either accident. [6] | **OBSERVED — pass only at program level.** Documented categories follow the accidents and grounding, not the alert alone. [7] [8] [10] | **Does not qualify.** Gate 3 fails; no but-for crash or dollar allocation is established. |

## Technical controls and decisions

### MCAS AOA-input comparison/inhibit logic

**OBSERVED.** The aircraft had two AOA sensors, while original MCAS used data from one AOA sensor at a time through the flight's master flight-control computer. The FAA's return-to-service work addressed the unsafe condition in which a single erroneous high-AOA input could activate MCAS and produce repeated nose-down stabilizer trim. [3] [4]

**OBSERVED.** The corrected design compares the AOA inputs and inhibits MCAS when the disagreement is significant. This should not be described as unconditional two-sensor operation: the FAA's 2022 summary says that, after a detected failed-AOA circuit, MCAS can operate using the remaining valid AOA input. [4]

**OBSERVED.** The House investigation records a 2015 Boeing Authorized Representative inquiry about single-AOA-sensor failure vulnerability and records that the aircraft was delivered with the one-input-at-a-time architecture. It also describes the March 2016 redesign that increased MCAS authority. [2]

**OBSERVED.** The FAA rule identifies the relevant single-erroneous-AOA/repeated-trim unsafe condition. The Lion Air final report records a 21-degree bias in the left AOA sensor, MCAS activations, repeated nose-down inputs, and loss of control. The Ethiopian investigation report, cited here through a secondary-host copy, also documents erroneous AOA input and the original one-sensor architecture. [3] [6] [9]

**MODELLED / CONDITIONAL.** The later monitor/inhibit design is evidence that a technically feasible solution existed by return to service. It is not evidence that the exact design was an available, evaluated, 2015–16 option. A contemporaneous change request, design-option analysis, or safety assessment would be required to convert Gate 1 from conditional to observed.

**UNRESOLVED.** The cited material provides no decision-period cost, saving, or quantified schedule value for choosing the one-input architecture rather than the exact comparison/inhibit logic. The control fails Gate 3 even though its risk connection is documented.

### Standalone AOA DISAGREE alert

**OBSERVED.** Boeing's design requirements called for a standard standalone AOA DISAGREE alert that would notify pilots when the two AOA values diverged. In delivered display software, the alert was inadvertently linked to the optional AOA indicator, so it operated only for customers that selected that option. [2] [5]

**OBSERVED.** Boeing discovered the discrepancy in 2017, accepted the existing functionality pending a later display-system update, and the House investigation reports that a Boeing Authorized Representative consented to postponing the update to 2020. [2] [5]

**PLANNED.** The original correction schedule was the third quarter of 2020. That is a future release date, not evidence of a quantified schedule benefit from delay or of an avoided cost. [6]

**OBSERVED.** The Lion Air final report gives a limited operational and maintenance-diagnosis connection: on the preceding flight the unavailable alert meant the crew did not report it, and the reported problem could only have been rectified through AOA-disagree tasks. The report does not establish that the alert's restoration would have prevented either accident. [6]

**OBSERVED — material source distinction.** The House report characterizes the alert as a required approved type-design feature. Boeing and the U.S. Department of Transportation Office of Inspector General later characterized the alert issue as non-safety. These statements address different questions—type-design conformity and safety classification, respectively—and neither makes the approved feature optional. [2] [5] [12]

**UNRESOLVED.** No cited decision-period source assigns a price, avoided cost, or quantified schedule value to deferring this exact standalone alert. The control therefore fails Gate 3. The alert's risk/diagnosis link does not establish control-specific accident prevention or control-specific costs.

### Separate near miss: MCAS disclosure and training

**OBSERVED.** In June 2013 Boeing chose to characterize MCAS as an addition to the existing Speed Trim System rather than emphasize it as a new function. The House report cites contemporaneous material warning that describing it as new could increase certification and training impact and costs. Boeing later obtained FAA approval in March 2016 to remove MCAS references from the flight-crew operations manual and training material. [2]

**OBSERVED.** The Lion Air report found that the aircraft manual and crew training did not include MCAS. The House report quotes the investigation's finding that a crew unaware of MCAS could misrecognize activation as Speed Trim System input, although MCAS moved the stabilizer faster; the National Transportation Safety Board separately found accident-pilot responses inconsistent with assumptions used in the MCAS safety assessment. [2] [6] [13]

**DERIVED.** This is a near miss with a documented training/disclosure rationale. It is not the MCAS AOA-input comparison/inhibit control and is not the standalone AOA DISAGREE alert. The same-control requirement prevents its rationale from qualifying either technical-control case above.

## Separate downstream monetary categories

**OBSERVED.** The following are separately reported categories downstream of the accidents and MAX grounding. They are not estimates of costs caused by either exact control. No row may be added to another row: scopes, accounting dates, cash status, and possible commercial overlap differ.

| Separate category | Amount and reporting status | Boundary and non-additivity limitation |
| --- | --- | --- |
| Boeing estimate of potential customer concessions and other considerations from grounding and delivery disruption | **$8.259 billion, 2019 earnings charge**, net of **$0.500 billion** insurance recoveries | An estimate and earnings charge, not a realized cash total and not a sensor- or alert-control cost. It must not be added to any other row. [7] |
| 737 MAX-related abnormal production costs expensed | **$2.567 billion, 2020** | A reported 2020 component of Commercial Airplanes' loss amid the MAX grounding and other factors. It is not allocated to either control and must not be added to any other row. [8] |
| Estimated abnormal production costs at abnormally low rates | Approximately **$5.0 billion forecast for 2020–21**, with about **$2.6 billion expensed in 2020** | A then-current forecast, not a realized total. It cannot be added to the $2.567 billion 2020 expense. [8] |
| Later reported abnormal-production outcome | **$2.567 billion (2020)** and **$1.887 billion (2021)**; **$4.454 billion** across those two reported years | This within-category two-year arithmetic is stated only to compare the later reported outcome with the prior $5.0 billion forecast. It is $0.546 billion below that forecast and is not an all-program total or an amount that may be added to other rows. [11] |
| DOJ deferred-prosecution monetary amount | More than **$2.5 billion, 2021**: **$243.6 million** criminal penalty, **$1.770 billion** airline-customer compensation, and **$0.500 billion** crash-victim beneficiaries fund | The components reconcile to $2.5136 billion within this one DOJ resolution. The resolution concerns fraud-conspiracy/MCAS-disclosure conduct, not a control-specific allocation; it must not be added to the Boeing accounting rows. [10] |

**OBSERVED — version change, not contradiction.** Boeing's 2020 filing treated approximately $5.0 billion as a forecast for abnormal 2020–21 production costs. Its 2021 filing later reported the separate 2020 and 2021 expenses. The later reported outcome is therefore not interchangeable with the earlier forecast. [8] [11]

## Proposed analytical boundary and ontology

**DERIVED.** Under `B1`, the separate customer-concession, production-cost, penalty, compensation, and victim-fund categories are positive institutional or financial events within their stated reporting horizons. They are evidence that documented obligations extended beyond a narrowly drawn technical-control decision, but they do not establish a cost allocation to either control. The accident investigations identify multiple contributing conditions, and the accounts do not assign dollars by failed safeguard.

**UNRESOLVED.** The evidence does not identify the actual incremental ex-ante cost boundary for `S1` or `S2`. Consequently, no difference between a decision-period control cost and a downstream total is calculated, and no allocation, percentage, ratio, or counterfactual saving is asserted.

**OBSERVED.** This is not an asymptote test. No nonterminal classification is made for a purportedly isolated system, and this record calculates no positive crossing-rate vector. Financial entries are observed or reported institutional/financial events in their individual horizons; the $5.0 billion entry is a company estimate rather than an observed cost. [1] [8]

**DERIVED — narrowed exact-zero claim.** A reported financial obligation can be a positive witness in the financial or institutional channel of a clearly declared expanded boundary. It neither inventories every crossing channel nor proves that crossings, risks, or future obligations are exactly zero in any broader boundary or all-time horizon. The protocol requires zero upper bounds in every enumerated channel and a complete inventory for terminal-within-scope classification; no such claim is made here. [1]

**MODELLED / CONDITIONAL.** FAA certification and return-to-service action are regulatory determinations based on specified tests, analyses, and assumptions. They are not model-independent proof that all future risks or crossings are zero, and later corrective design does not prove a but-for cost or accident counterfactual for either omitted control. [3] [4]

## Evidence needed to change the result

**UNRESOLVED.** The candidate could qualify only if a reliable decision-period source tied an ex-ante cost, saving, or quantified schedule value directly to one exact control: either the 2015–16 MCAS AOA-input comparison/inhibit logic, or the 2017–20 deferral of the standalone AOA DISAGREE alert. A contemporaneous change request, supplier quote, budget, signed decision memorandum, or design-option analysis would need to identify the exact control and its monetary or quantified schedule effect.

**DERIVED.** A price for the optional AOA indicator, a later implementation cost, a date for the next display-system update, a program-level accounting amount, or a disclosure/training rationale would not meet Gate 3 without evidence tying it to the same control and decision period.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/crossing-metric.md "WO-3 crossing-rate metric and test protocol"
[2]: https://www.govinfo.gov/content/pkg/GOVPUB-Y4_T68_2-PURL-gpo144993/pdf/GOVPUB-Y4_T68_2-PURL-gpo144993.pdf "Final Committee Report: The Design, Development & Certification of the Boeing 737 MAX"
[3]: https://www.federalregister.gov/api/v1/documents/2020-25844.json "Airworthiness Directives; The Boeing Company Airplanes, AD 2020-24-02"
[4]: https://www.faa.gov/sites/faa.gov/files/2022-08/737_RTS_Summary.pdf "Summary of the FAA's Review of the Boeing 737 MAX"
[5]: https://boeing.mediaroom.com/news-releases-statements?item=130431 "Boeing Statement on AOA Disagree Alert"
[6]: https://www.aaiu.ie/sites/default/files/FRA/2018%20-%20035%20-%20PK-LQP%20Final%20Report.pdf "Final Aircraft Accident Investigation Report: PT. Lion Mentari Airlines Boeing 737-8 (MAX), PK-LQP"
[7]: https://www.sec.gov/Archives/edgar/data/12927/000001292720000014/a201912dec3110k.htm "The Boeing Company 2019 Form 10-K"
[8]: https://www.sec.gov/Archives/edgar/data/12927/000001292721000011/ba-20201231.htm "The Boeing Company 2020 Form 10-K"
[9]: https://skybrary.aero/sites/default/files/bookshelf/29019.pdf "Ethiopian Aircraft Accident Investigation Bureau, Aircraft Accident Investigation Report B737-MAX 8, ET-AVJ (secondary host)"
[10]: https://www.justice.gov/archives/opa/pr/boeing-charged-737-max-fraud-conspiracy-and-agrees-pay-over-25-billion "Boeing Charged with 737 Max Fraud Conspiracy and Agrees to Pay over $2.5 Billion"
[11]: https://www.sec.gov/Archives/edgar/data/12927/000001292722000010/ba-20211231.htm "The Boeing Company 2021 Form 10-K"
[12]: https://www.oig.dot.gov/library-item/46146 "Letter to Congress on FAA's Oversight of the Boeing 737 MAX Angle-of-Attack Disagree Alert and the Maneuvering Characteristics Augmentation System"
[13]: https://www.ntsb.gov/investigations/AccidentReports/Reports/ASR1901.pdf "Assumptions Used in the Safety Assessment Process and the Effects of Multiple Alerts and Indications on Pilot Performance"

**Publication status:** Reconciled after independent validation.

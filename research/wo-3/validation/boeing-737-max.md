# Validation record — Boeing 737 MAX

**Item:** `boeing-737-max-sensor-redundancy-safety-alerts`
**Validation date:** 2026-09-19
**Verdict:** **NEEDS CORRECTION — not publication-ready.**
**Retained finding:** The record correctly rejects this as a qualifying WO-3 cost case. Neither the single-AOA-input MCAS logic nor the deferred standalone AOA DISAGREE alert has a documented contemporaneous, same-control ex-ante cost, saving, or quantified schedule value. The documented training/certification-cost rationale concerns disclosure and training for MCAS, not either technical control. It cannot be transferred across controls. [1] [2]

## What survives strict validation

The record’s central conclusion is sound. The evidence establishes that pre-crash MCAS used one AOA input at a time, while the FAA’s corrective action addressed the unsafe condition created when a single erroneous high-AOA input could trigger repeated nose-down trim. [3] [4] It also establishes that the intended standard AOA DISAGREE alert was incorrectly dependent on the optional AOA indicator, and that Boeing deferred correction after its 2017 discovery. [2] [5] The Lion Air investigation supplies a limited operational/maintenance-diagnosis connection for the absent alert; it does **not** establish that restoring the alert would have prevented either accident. [6]

The record appropriately excludes the often-repeated `$80,000` proposition and does not use a training rationale as evidence of a sensor-comparison or alert-deferral saving. However, the negative-search assertion itself is not reproducible as written: no search protocol, date-bounded corpus, or source log is supplied. Rephrase it as, “No qualifying decision-period source is cited in this record,” rather than as a general search conclusion.

## Five preregistered gates

| Exact control | 1. Available | 2. Declined/deferred | 3. Same-control ex-ante cost/value | 4. Investigation link | 5. Downstream cost category | Strict result |
|---|---|---|---|---|---|---|
| MCAS AOA-input comparison/inhibit | **Conditional.** Two installed sensors and the later corrective monitor/inhibit design are established, but the record does not show that this exact comparator/inhibit control was an available 2015–16 decision alternative. Later implementation proves feasibility no later than return-to-service, not contemporaneous availability. [2] [3] [4] | **Pass, at architecture level.** The congressional report documents the concern and delivery with one-input-at-a-time MCAS. [2] | **Fail.** No cited contemporaneous price, avoided cost, or quantified schedule value for this exact design choice. | **Pass for risk/harm connection, not but-for allocation.** The FAA rule identifies the single erroneous-AOA/repeated-trim unsafe condition; accident evidence records the relevant failure sequence. [3] [4] [6] | **Pass only at program level.** Audited and DOJ categories exist but are not allocated to this control. [7] [8] | **Does not qualify.** Gate 3 fails; Gate 1 should not be labeled fully observed on the present evidence. |
| Standalone AOA DISAGREE alert | **Pass.** It was a stated standard standalone requirement. [5] | **Pass.** The delivered dependency on the optional indicator and the 2017-to-2020 deferral are documented. [2] [5] | **Fail.** A planned future release date is not a schedule value; no same-control price or avoided-cost record is cited. | **Limited pass for risk/diagnosis only.** The Lion Air report ties its absence to non-reporting and the AOA-disagree maintenance path, not to crash prevention. [6] | **Pass only at program level.** The categories are downstream of the MAX accidents/grounding, not of the alert alone. [7] [8] | **Does not qualify.** Gate 3 fails; no but-for crash or dollar claim is permitted. |

This is a proper **null cost-case result**, not a partial affirmative chain. The “PARTIAL” label may remain only if it means “technical and program-cost evidence exists but qualification fails”; it must not imply that a cost-to-control causal case is partly proven.

## Required factual, citation, and terminology corrections

1. **Rename the sensor control.** “Sensor redundancy” suggests absent physical redundancy, although two AOA sensors were installed. Use **“MCAS AOA-input comparison/inhibit logic”** or **“single-input MCAS logic.”**
2. **Qualify “used both AOA inputs.”** The post-correction design compares inputs and inhibits MCAS for a significant disagreement, but the FAA’s 2022 summary also states that after a *detected* failed-AOA circuit, MCAS can operate on the remaining valid AOA input. Do not describe it as unconditional two-sensor operation. [4]
3. **Correct the Gate-1 status for MCAS.** “Eventual return-to-service design used both inputs” cannot by itself establish the exact control as available at the 2015–16 decision point. Mark it **conditional/not contemporaneously established** unless a contemporaneous design option, change request, or safety analysis is added.
4. **Cite the Ethiopian report where it is used.** The sentence saying the Ethiopian report documents erroneous input and the one-sensor architecture needs its own citation. The existing link is a copy hosted by SKYbrary, not an Ethiopian-government host; identify it as a secondary-host copy or replace it with a stable investigation-authority copy. [9]
5. **Cite the Q3-2020 assertion locally.** The record’s statement that the original update was planned for Q3 2020 needs an inline citation to the Lion Air report, which states that schedule. Boeing’s public statement says only “the next planned” display-system update. [5] [6]
6. **Do not call the unobserved decision boundary “original.”** Gate 3 is missing, so the actual ex-ante cost-comparison boundary is unknown. Recast the “boundary redraw” as a **proposed analytical boundary**, rather than an observed original boundary that omitted named costs.

## Amount, arithmetic, horizon, and overlap checks

All displayed source-year amounts are arithmetically and descriptively correct **if retained as separate categories**:

- Boeing’s 2019 Form 10-K reports a **$8.259 billion earnings charge**, net of **$0.500 billion** insurance recoveries, for an *estimate* of potential customer concessions and other considerations tied to grounding and delivery disruption. It is not an alert- or sensor-control cost, nor a realized cash total. [7]
- Boeing’s 2020 Form 10-K reports **$2.567 billion** of 737 MAX-related abnormal production costs. Its approximately **$5.0 billion** figure is a then-current **2020–21 forecast**, with about **$2.6 billion** expensed in 2020; it must not be added to the $2.567 billion line. [8]
- DOJ’s components reconcile: **$243.6 million + $1.770 billion + $0.500 billion = $2.5136 billion**, so “more than $2.5 billion” is correct. The resolution concerns fraud-conspiracy/MCAS-disclosure conduct, not a control-specific allocation. [10]

No totals may be calculated across these rows. The record correctly warns that the customer-concession liability, DOJ airline-customer compensation, and other program costs may overlap commercially and use different accounting dates and scopes.

The record nevertheless lacks the protocol’s required declared assessment frame. Before publication, state separate boundaries and horizons, for example: **S** = each named Boeing technical-control decision; **B0** = unknown ex-ante incremental decision cost (not observed); **B1** = documented post-accident Boeing/customer/public obligations; and separate **H** values for the 2015–16 sensor decision, the 2017–20 alert deferral, and each 2019–21 accounting observation. Do not merge those horizons or claim a whole-life total. [1]

## Official-source version and status notes

There is a material **date/version change**, not a contradiction: Boeing’s 2020 filing treated $5.0 billion as an estimate for abnormal 2020–21 production costs. Boeing’s 2021 filing subsequently reported $2.567 billion (2020) and $1.887 billion (2021) of 737 MAX-related abnormal production costs—**$4.454 billion** in the two reported years, $0.546 billion below the earlier $5.0 billion forecast. Keep the 2020 value only as an estimate and, if presenting outcomes, cite the 2021 actuals separately. [8] [11]

The FAA’s operative final rule took effect on 2020-11-20, while the cited FAA review summary is a 2022 version. Cite the rule for mandatory corrective actions and use the later summary only as a retrospective explanation of the modified logic. [3] [4]

The House report’s statement that the AOA alert was mandatory as part of approved type design does not conflict with Boeing’s and DOT OIG’s later/non-safety characterizations. The former is a conformity/type-design requirement; the latter is a safety classification. The record should say that distinction explicitly rather than imply that “non-safety” made the approved feature optional. [2] [5] [12]

## Ontology and evidentiary limit

This is **not an asymptote test**, so no theoretical crossing claim or positive-crossing calculation is present to validate. The financial entries are observed or reported **institutional/financial events** within their respective reporting horizons; the `$5.0 billion` entry is a company estimate, not an observed cost. A positive cost/obligation can be a positive witness under a clearly declared expanded boundary, but it neither measures every crossing channel nor proves the work order’s universal nonterminality claim.

Likewise, FAA certification/return-to-service action is an empirical regulatory determination based on specified tests, analyses, and assumptions. It is not model-independent proof that all future risks or crossings are zero. The candidate record should retain this distinction and should not treat later corrective design, certification, or program-level costs as proof of a but-for causal counterfactual for either omitted control. [1] [3] [4]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-3/crossing-metric.md "WO-3 crossing-rate metric and test protocol"

[2]: https://www.govinfo.gov/content/pkg/GOVPUB-Y4_T68_2-PURL-gpo144993/pdf/GOVPUB-Y4_T68_2-PURL-gpo144993.pdf "Final Committee Report: The Design, Development & Certification of the Boeing 737 MAX"

[3]: https://www.federalregister.gov/api/v1/documents/2020-25844.json "Airworthiness Directives; The Boeing Company Airplanes, AD 2020-24-02"

[4]: https://www.faa.gov/sites/faa.gov/files/2022-08/737_RTS_Summary.pdf "Summary of the FAA’s Review of the Boeing 737 MAX"

[5]: https://boeing.mediaroom.com/news-releases-statements?item=130431 "Boeing Statement on AOA Disagree Alert"

[6]: https://www.aaiu.ie/sites/default/files/FRA/2018%20-%20035%20-%20PK-LQP%20Final%20Report.pdf "Final Aircraft Accident Investigation Report: PT. Lion Mentari Airlines Boeing 737-8 (MAX), PK-LQP"

[7]: https://www.sec.gov/Archives/edgar/data/12927/000001292720000014/a201912dec3110k.htm "The Boeing Company 2019 Form 10-K"

[8]: https://www.sec.gov/Archives/edgar/data/12927/000001292721000011/ba-20201231.htm "The Boeing Company 2020 Form 10-K"

[9]: https://skybrary.aero/sites/default/files/bookshelf/29019.pdf "Ethiopian Aircraft Accident Investigation Bureau, Aircraft Accident Investigation Report B737-MAX 8, ET-AVJ (secondary host)"

[10]: https://www.justice.gov/archives/opa/pr/boeing-charged-737-max-fraud-conspiracy-and-agrees-pay-over-25-billion "Boeing Charged with 737 MAX Fraud Conspiracy and Agrees to Pay over $2.5 Billion"

[11]: https://www.sec.gov/Archives/edgar/data/12927/000001292722000010/ba-20211231.htm "The Boeing Company 2021 Form 10-K"

[12]: https://www.oig.dot.gov/library-item/46146 "Letter to Congress on FAA’s Oversight of the Boeing 737 MAX Angle-of-Attack Disagree Alert and the Maneuvering Characteristics Augmentation System"

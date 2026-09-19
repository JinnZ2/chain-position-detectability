# WO-2 Pilot Analysis: Pre-Event Signals and Missing Aggregation Functions in Eight CSB Investigations

> **Superseded audit trail.** This first synthesis was replaced after independent validation found cross-pathway evidence mixing and over-inference of an unassigned join in four supporting classifications. Use [`pilot-analysis.md`](pilot-analysis.md) for the final result.

**Author:** Manus AI
**Date:** 19 September 2026

## Executive finding

The WO-2 pattern was **observed in five of eight cases** in this bounded pilot of U.S. Chemical Safety and Hazard Investigation Board (CSB) final reports. No case affirmatively failed a necessary element; the remaining three were indeterminate because a qualifying signal, the number of holders, or the assignment of an integrating role could not be resolved from the official report. The five supporting cases are U.S. Steel Clairton, Givaudan Sense Colour, Dow Louisiana Operations, PEMEX Deer Park, and TS USA. Shell Polymers, Bio-Lab Conyers, and Cuisine Solutions are indeterminate.

This is a descriptive result about eight CSB reports, not an estimate of a population rate. It shows that the preregistered structure can be applied, can yield indeterminate outcomes, and recurs in this sample. It does not establish that missing aggregation caused every industrial accident, that a join function is always feasible, or that the observed proportion generalizes beyond these cases.[1]

## Fixed sample and decision rule

The sampling rule was fixed before coding: select the **eight most recently published CSB final incident-investigation reports** identifiable in the agency’s completed-investigation materials as of **19 September 2026**. A report qualified only if it concerned a specific incident, was publicly accessible, and contained enough pre-event chronology to apply the instrument. The ordering variable was final-report publication date, not event date. The manifest contains exactly eight eligible reports, from Shell Polymers, released 16 September 2026, through TS USA, released 3 June 2025. No selected report required replacement.[1] [2]

The target pattern requires all four of the following: a hazard-related pre-event signal was present; the signal was communicated or recorded; at least two distinct holders possessed relevant fragments; and the official record affirmatively shows that no named function had both responsibility and authority to aggregate those fragments. A case is **indeterminate** when a necessary element is unresolved. Missing evidence is not converted to a negative finding.[1]

Two coders independently applied the codebook to each case. Although the upstream structured-coding workflow reported cache/input-conflict errors for most entries, the filesystem contained **all 16 substantive evidence records**—coder A and coder B for every manifest case—and every record was read in full. The completeness condition was therefore satisfied. The raw codes were compared before reconciliation, and each disagreement was resolved from the cited official report rather than by vote. Full decisions appear in the [reconciliation log](reconciliation-log.md); the final machine-readable records appear in the [reconciled dataset](reconciled-dataset.csv).

## Raw coder consistency

The raw duplicate pass produced **59 exact agreements across 87 substantive comparisons**, for an exact agreement rate of **67.8%**. The denominator includes the requested variables and compares `holder_count_min` only where the coder records supplied a substantive lower bound. Cuisine Solutions’ shared zero was excluded because both coders expressly described it as a schema placeholder for “no defensible lower bound,” not a measured holder count.

| Variable | Agreements | Comparisons | Exact agreement |
| --- | ---: | ---: | ---: |
| Signal present | 8 | 8 | 100.0% |
| Signal reported | 8 | 8 | 100.0% |
| Holder count known | 5 | 8 | 62.5% |
| Holder minimum, when substantively available | 5 | 7 | 71.4% |
| Join assigned | 5 | 8 | 62.5% |
| First-signal date | 4 | 8 | 50.0% |
| Lead-time minimum | 4 | 8 | 50.0% |
| Lead-time maximum known | 6 | 8 | 75.0% |
| Lead-time maximum | 5 | 8 | 62.5% |
| Sudden label | 4 | 8 | 50.0% |
| Pattern result | 5 | 8 | 62.5% |
| **Overall** | **59** | **87** | **67.8%** |

Agreement was perfect on whether a signal was present and reported, but weaker on chronology, suddenness, and whether the report affirmatively established an absent join. This is consistent with the instrument’s main interpretive pressure points: choosing the earliest officially connected signal, preserving date precision, distinguishing a missing role description from affirmative evidence of no assigned integration point, and deciding whether “rapid” or “unexpected” modifies the event, failure, or warning pattern. Because both coders were AI research agents operating under the same task design, this is a consistency check rather than validated human inter-rater reliability.[1]

## Reconciled case findings

| Rank | Case | Signal | Reported | Holder minimum | Join assigned | First signal | Lead time | Sudden label | Result |
| ---: | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| 1 | Shell Polymers | Yes | Yes | 3 | Unclear | 2023 | 521–885 days | Yes | **Indeterminate** |
| 2 | U.S. Steel Clairton | Yes | Yes | 2 | No | 2003 | 7,894–8,258 days | Yes | **Supports** |
| 3 | Bio-Lab Conyers | Yes | Yes | 3 | Unclear | 2019-12-30 | 1,735 days | No | **Indeterminate** |
| 4 | Givaudan Sense Colour | Yes | Yes | 2 | No | 2012-10-15 | 4,411 days | Yes | **Supports** |
| 5 | Dow Louisiana Operations | Yes | Yes | 2 | No | 2020-11-20 | 966 days | Unclear | **Supports** |
| 6 | PEMEX Deer Park | Yes | Yes | 2 | No | Unknown | Unquantifiable | Unclear | **Supports** |
| 7 | Cuisine Solutions | Unclear | Unclear | Not established | Unclear | Unknown | Unquantifiable | Yes | **Indeterminate** |
| 8 | TS USA | Yes | Yes | 2 | No | 2018-01-25 | 2,317 days | Yes | **Supports** |

### Supporting cases

**U.S. Steel Clairton.** The earliest qualifying signal was a 2003 process-hazard-analysis recommendation to study coke-battery facility siting. The CSB treated that rejected recommendation as a key missed opportunity to address the risk that made the 2025 explosion fatal. Separately, the actual water-washing operation proceeded without a washing procedure, hazard analysis, relevant planning meeting, permit, or training. Those affirmative findings establish an unassigned integration point for the causal work, rather than merely an omitted job title. The valve fracture was officially described as “sudden, brittle fracture.”[4]

**Givaudan Sense Colour.** A 15 October 2012 reactivity test showed a self-sustained temperature rise and gas-driven pressure rise. D.D. Williamson transmitted the results to an outside consultant, establishing at least two organizational holders. The CSB expressly found that no employee was adequately assigned and trained to own process-safety-policy implementation, including hazard assessment, and tied that absence to Reactor 5/6 design personnel not receiving the 2012 test and relief-sizing information. The 4,411-day interval is exact. The report’s “rapid temperature and pressure rise” is treated as a close suddenness equivalent, but the same report documents immediate control-room warnings and attempted intervention.[6]

**Dow Louisiana Operations.** On 20 November 2020, workers left pressure-relief piping at 2.4 psig rather than the procedure-required 5 psig. Recorded pressure later declined to atmospheric and negative values; the CSB directly connected loss of nitrogen inerting to air intrusion and ethylene-oxide ignition. The distinct holder minimum rests on other causal-pathway fragments: unit-level equipment tracking recorded five unreturned work lights, while vessel-closure personnel held completion and visual-inspection information. The report affirmatively states that there was no official vessel-specific tracking procedure and no closure-form requirement to reconcile contractors’ materials. That supports an absent assigned join for the debris pathway. It does not show that anyone knowingly possessed the complete causal chain.[7]

**PEMEX Deer Park.** The signal was an ineffective equipment-identification and work-control state that included ambiguous job aids, a Blind 407 tag placed out of sight, and inconsistent physical identifiers. The operator-to-foreman handoff establishes reporting and at least two holders. The report also establishes that the permit lacked a defined hold point, roles understood “Ops present for each break” differently, active-unit status did not reach the boilermakers, and the simultaneous-operations process produced no evaluation. Taken together, these are affirmative evidence that the job lacked a responsible-and-authorized join. The earliest onset of the inadequate system is undated, so its lead time is not quantified.[8]

**TS USA.** The 25 January 2018 Mexico explosion showed that parts with accumulation hazards could trap water and produce an overpressure explosion in a salt bath. TS ETSA documented the incident, and a translated report was presented to HEF Groupe. The CSB found that HEF Groupe did not manage safety knowledge across subsidiaries and had not assigned dedicated safety resources and responsibilities at the facilities. The exact dated signal preceded the 2024 event by 2,317 days. The failure sequence was officially characterized as water that “rapidly expanded as steam” and “rapidly boiled,” creating a violent steam explosion.[10]

### Indeterminate cases

**Shell Polymers.** The 2023 PHA revalidation documented the reverse-flow explosion hazard. The incident-day PACO engineer and console operator held additional valve-command and alarm fragments, so at least three role-level holders are supported. The “unexpected state” alarm qualifies as official language about the warning pattern. The report, however, neither identifies a qualifying function assigned to combine the PHA, valve-command, and alarm information nor affirmatively proves that no such function existed. The case therefore remains indeterminate.[3]

**Bio-Lab Conyers.** A corrosion-related sprinkler-component failure occurred at Plant 12 on 30 December 2019. Later inspection reports and insurer communications documented extensive corrosion, while corporate employees at vice-president and manager levels received the risk findings. The CSB framed the issue as “Run To Failure” and said warning signs from corrosion and frequent leaks had been observed; this supports `sudden_label = no` for the warning pattern. Yet the report identifies procedures and reporting responsibilities without resolving whether one role had both authority and responsibility to aggregate every relevant stream. The pattern result remains indeterminate.[5]

**Cuisine Solutions.** A same-day pump shutdown and high chilled-water temperatures were reported, but the CSB could not verify their relationship to the surge-drum overpressure because historical process and alarm data were unavailable. Signal presence and reporting therefore remain unclear, and no holder minimum or lead time can be defended. The report’s phrase “sudden pressure drop” qualifies only as a characterization of one possible failure-sequence mechanism; it does not establish that the unidentified initiating upset was sudden or unwarned.[9]

### Non-supporting cases

There were **no reconciled `does_not_support` cases**. This does not mean every case supported the pattern. Three cases remained indeterminate because unresolved evidence is not an affirmative failure of a necessary element. The absence of a non-supporting case in a purposively bounded sample of eight must not be used as a prevalence estimate or universal claim.[1]

## What the sudden-label subset shows—and does not show

Five reports received `sudden_label = yes`: Shell Polymers, U.S. Steel Clairton, Givaudan Sense Colour, Cuisine Solutions, and TS USA. Two were unclear, and Bio-Lab Conyers was coded no because the CSB affirmatively described an observed-warning, run-to-failure pattern. Among the five positive-label cases, three support the WO-2 pattern and two are indeterminate.

The labels refer to different objects. U.S. Steel describes a sudden brittle fracture; Givaudan and TS USA describe rapid physical escalation; Cuisine describes a sudden pressure drop in a possible submechanism; and Shell’s “unexpected state” refers to a valve alarm. Therefore, this subset cannot be interpreted as five equivalent public claims that the accidents arrived “without warning.” Indeed, the reports document earlier signals in all but Cuisine Solutions, where signal relevance remains unresolved. Conversely, an unclear label does **not** mean that the public or the CSB called an event quiet, gradual, or expected. It means only that no qualifying official characterization was established under this field.

## Lead time and organizational interpretation

Six cases have quantifiable reconciled lead time. The shortest minimum is Shell Polymers at 521 days; the longest is U.S. Steel Clairton at 7,894 days. Four intervals are exact at calendar-day precision, while Shell and U.S. Steel are ranges derived from year-only dates. PEMEX’s earliest system condition is undated, and Cuisine lacks a confirmed qualifying signal.

These durations measure the interval from the earliest report-supported signal to the event. They do not show that the full causal significance was understood throughout that period, that corrective action was straightforward, or that the same individuals continuously held the information. The holder variable is likewise a conservative organizational lower bound, not a count of everyone who could access a record.

The five supporting cases identify different missing joins. Givaudan and TS USA concern process-safety ownership and cross-facility knowledge management. Dow concerns reconciliation between equipment tracking and vessel closure. PEMEX concerns work-control, equipment identification, and contractor handoff. U.S. Steel concerns integration of a hazardous work practice into planning, procedure, training, and hazard analysis. The recurrence lies at the level of the codebook’s functional structure, not one uniform organizational defect.

## Auxiliary searches

A separate regulatory existence search found that a named, authorized integration function is **administratively possible**. FAA 14 CFR Part 5 requires designated management personnel to coordinate organization-wide Safety Management System integration and report to an accountable executive who has final operational authority and must direct corrective action. European Medicines Agency pharmacovigilance guidance assigns the Qualified Person Responsible for Pharmacovigilance system-wide oversight of safety profiles and emerging concerns, together with influence, reporting, and urgent-regulatory-action pathways.[11] [12] [13] These examples falsify a universal claim that regulation cannot assign the join. They do not establish that such a function existed or received the relevant fragments in any of the eight CSB cases.

A separate inverse-case search asked whether an organization or regulator had explicitly priced a cross-holder signal-aggregation function, stated its risk-reduction purpose, and deliberately declined it. No qualifying case was found in the bounded official investigation, audit, regulatory, and academic search. The closest lead was the Army’s Military Flight Operations Quality Assurance programme: official sources document a genuine multi-source risk-analysis function and nonimplementation as an “unfunded requirement,” but the opened record did not contain the required dollar estimate, benefit estimate, or a documented cost-benefit exclusion decision.[14] [15] This is a **bounded null**, not evidence that no such decision exists. Other sources show that aggregation can be costed or required—the implemented Cardiff information-sharing programme, the deployed Homeland Security Information Network, and the adopted pipeline data-integration rule—but none documents the required costed and deliberate rejection.[16] [17] [18]

## Conclusion

The reconciled result is **pattern observed within the bounded eight-case CSB pilot**: five supports, zero does-not-support, and three indeterminate. The strongest evidence is not merely that warnings existed. It is that five official reports also contain affirmative evidence of a missing function that would have integrated relevant fragments across holders under the codebook’s responsibility-and-authority test.

The conclusion remains narrow. These reports were produced by one investigative agency in one industrial domain and selected by publication recency. The duplicate AI coding pass exposed material ambiguity, especially in join assignment, suddenness, and earliest-signal chronology. The auxiliary regulatory search shows that explicit join roles can be designed; the inverse-case search did not establish that a costed join was deliberately rejected. Together, these findings justify further testing, not a claim of universal causal law.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

[2]: https://www.csb.gov/investigations/completed-investigations/ "U.S. Chemical Safety and Hazard Investigation Board Completed Investigations"

[3]: https://www.csb.gov/file.aspx?DocumentId=6343 "Furnace Explosion and Fire at Shell Polymers"

[4]: https://www.csb.gov/file.aspx?DocumentId=6340 "Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works"

[5]: https://www.csb.gov/file.aspx?DocumentId=6339 "Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility"

[6]: https://www.csb.gov/file.aspx?DocumentId=6324 "Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson"

[7]: https://www.csb.gov/file.aspx?DocumentId=6316 "Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations"

[8]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery"

[9]: https://www.csb.gov/file.aspx?DocumentId=6304 "Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility"

[10]: https://www.csb.gov/file.aspx?DocumentId=6296 "Explosion, Molten Salt Eruption, and Fatal Injury at TS USA Liquid Nitriding Facility"

[11]: https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol1/pdf/CFR-2024-title14-vol1-part5.pdf "14 CFR Part 5—Safety Management Systems"

[12]: https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-module-i-pharmacovigilance-systems-and-their-quality-systems_en.pdf "Guideline on good pharmacovigilance practices, Module I: Pharmacovigilance systems and their quality systems"

[13]: https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-gvp-module-ix-signal-management-rev-1_en.pdf "Guideline on good pharmacovigilance practices, Module IX: Signal management"

[14]: https://www.ntsb.gov/investigations/AccidentReports/Reports/AIR2602.pdf "Collision of PSA Airlines Flight 5342 and a US Army Sikorsky UH-60L Black Hawk near Ronald Reagan Washington National Airport"

[15]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/605519.pdf?ver=2018-11-21-082114-987 "DoD Instruction 6055.19: Aviation Hazard Identification and Risk Assessment Programs"

[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5779858/ "An economic evaluation of anonymised information sharing in a partnership between health services, police and local government for preventing violence-related injury"

[17]: https://www.gao.gov/assets/a116583.html "Information Technology: Homeland Security Information Network Needs to Be Better Coordinated with Key State and Local Initiatives"

[18]: https://www.govinfo.gov/content/pkg/FR-2022-08-24/pdf/2022-17031.pdf "Pipeline Safety: Safety of Gas Transmission Pipelines: MAOP Reconfirmation, Expansion of Assessment Requirements, and Other Related Amendments"

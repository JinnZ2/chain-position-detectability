# WO-2 Pilot Analysis: Pre-Event Signals and Missing Aggregation Functions in Eight CSB Investigations

**Author:** Manus AI

**Research cut-off:** 19 September 2026

**Final disposition:** One supporting case; seven indeterminate cases; no affirmative non-supporting case

## Executive finding

The strict WO-2 pattern was **confirmed in one of eight cases** in this bounded pilot of U.S. Chemical Safety and Hazard Investigation Board final reports. The Givaudan Sense Colour investigation contains all four required elements on one coherent hazard pathway: a documented pre-event signal, communication to a second organizational holder, at least two holders, and an official finding that no adequately assigned and trained process-safety owner integrated the relevant hazard-assessment information.[1]

The other seven cases are **indeterminate**, not negative. Seven reports contain a relevant signal and six establish at least two holders, but the official record usually does not affirmatively resolve whether a named function had both responsibility and authority to aggregate the relevant fragments. Cuisine Solutions is indeterminate earlier in the chain because the Board could not connect the candidate precursor to the initiating upset.[2]

This result is materially narrower than the first automated reconciliation, which classified five cases as supporting. Independent validators read each official report and found that four of those five classifications mixed evidence from separate causal pathways or inferred an unassigned join from weak controls, absent procedures, or ineffective performance. The initial analysis and reconciliation are retained as superseded audit-trail artifacts; this report contains the validated result.

## Method

### Fixed sample

The sampling rule was published before coding: select the eight most recently released, publicly accessible CSB final incident-investigation reports identifiable from the agency’s completed-investigation materials as of 19 September 2026. The ordering variable was report-release date, not event date or apparent fit with WO-2. The [source manifest](source-manifest.md) records the selected reports and boundary exclusions.[3]

### Coding rule

A case supports the pattern only when the official report establishes all four elements:

1. a pre-event signal connected by the report to the selected hazard pathway;
2. communication or recording of that signal beyond private awareness;
3. at least two distinct people, roles, teams, contractors, or organizational units holding relevant fragments; and
4. affirmative evidence that no named function had both responsibility and authority to aggregate those fragments before the event.

Missing evidence produces `unclear`, not `no`. The [codebook](codebook.md) defines every field and its evidence threshold.[4]

Two research agents coded every case independently, producing sixteen evidence records. Their first-pass outputs agreed on 59 of 87 structured-field comparisons, or 67.8%. This figure is a consistency check, not validated human inter-rater reliability. The first reconciliation was then independently validated case by case against the official reports.

### Post-hoc clarification

Validation exposed an underspecified rule. Every field supporting one case result must belong to **one coherent hazard pathway identified by the official report**. A signal from one pathway cannot be combined with holder or join evidence from another contributing or severity pathway. Validation also required affirmative evidence for `join_assigned = no`; a missing procedure, weak implementation, or silence about roles is insufficient.

The suddenness field was also tightened. Alarm labels and generic physical-rate adverbs do not qualify unless the official source uses them to characterize the event, relevant failure, or warning pattern. These clarifications were applied symmetrically to all eight cases, but they were added after the first reconciliation and are therefore reported as post hoc rather than preregistered.[4]

## Validated results

| Rank | Case | Signal | Reported | Holder minimum | Join assigned | Lead time | Sudden label | Result |
| ---: | --- | --- | --- | ---: | --- | --- | --- | --- |
| 1 | [Shell Polymers](validation/shell-polymers.md) | Yes | Yes | 3 | Unclear | 521–885 days | Unclear | **Indeterminate** |
| 2 | [U.S. Steel Clairton](validation/us-steel-clairton.md) | Yes | Yes | 2 | Unclear | At least 1,096 days | Yes | **Indeterminate** |
| 3 | [Bio-Lab Conyers](validation/bio-lab-conyers.md) | Yes | Yes | 3 | Unclear | 1,735 days | No | **Indeterminate** |
| 4 | [Givaudan Sense Colour](validation/givaudan-sense-colour.md) | Yes | Yes | 2 | No | 4,411 days | Yes | **Supports** |
| 5 | [Dow Louisiana Operations](validation/dow-louisiana-operations.md) | Yes | Yes | 1 | Unclear | 966 days | Unclear | **Indeterminate** |
| 6 | [PEMEX Deer Park](validation/pemex-deer-park.md) | Yes | Yes | 2 | Unclear | 1–2 days | Unclear | **Indeterminate** |
| 7 | [Cuisine Solutions](validation/cuisine-solutions.md) | Unclear | Unclear | Not established | Unclear | Unquantifiable | Unclear | **Indeterminate** |
| 8 | [TS USA](validation/ts-usa.md) | Yes | Yes | 2 | Unclear | Unquantifiable | Unclear | **Indeterminate** |

The [reconciled dataset](reconciled-dataset.csv) contains the machine-readable final values, and the [validated reconciliation log](reconciliation-log.md) records every change from the first reconciliation.

## The confirmed case

The Givaudan Sense Colour report documents a 15 October 2012 reactivity test in which Product 034 exhibited a self-sustained temperature rise and gas-driven pressure increase. D.D. Williamson sent the results to an outside consultant, establishing communication and at least two organizational holders. The Board connected that evidence to the same sugar-decomposition and relief-system-design pathway that produced the 2024 Reactor 6 rupture.[1]

The decisive join evidence is affirmative rather than inferred. The report states that the facility had not adequately assigned and trained an employee to own implementation of its process-safety policies, including oversight of annual hazard identification and risk assessment. It then directly links that missing ownership to Reactor 5 and 6 design personnel not receiving the 2012 test and relief-sizing information. The exact signal-to-event interval is 4,411 days.[1]

This case therefore demonstrates the structure’s existence in the pilot. It does not estimate how often that structure appears in the broader accident population.

## Why seven cases remain indeterminate

The principal bottleneck is the join variable. Seven reports do not establish a qualifying assigned join, but they also do not affirmatively establish that none existed. Accident reports commonly document missing procedures, incomplete analysis, ineffective monitoring, poor communication, or inadequate role performance. Those findings do not necessarily answer the narrower organizational-design question: whether one named function had responsibility and authority to integrate the particular cross-holder signals before the event.

This distinction corrected four initial supporting classifications. U.S. Steel’s 2003 facility-siting recommendation could not be combined with water-washing planning failures. Dow’s nitrogen-inerting signal could not be combined with work-light inventory and vessel-closure gaps. PEMEX’s equipment-identification pathway could not borrow permit, contractor-handoff, and simultaneous-operations findings. TS USA’s ineffective knowledge management did not affirmatively prove that no integration function had been assigned. The validation records document those boundaries from the official reports.[5] [6] [7] [8]

Shell Polymers and Bio-Lab Conyers already remained indeterminate because join assignment was unresolved. Cuisine Solutions remained indeterminate because the Board could not determine whether the candidate pump and temperature episode belonged to the initiating overpressure pathway.[2] [9] [10]

## Variable-level findings

| Variable | Validated distribution | Interpretation |
| --- | --- | --- |
| Signal present | 7 yes; 1 unclear | Relevant pre-event signals were common in the selected reports. |
| Signal reported | 7 yes; 1 unclear | The same seven signals were communicated or recorded beyond private awareness. |
| Holder minimum | 6 cases with at least 2; 1 case with 1; 1 unresolved | Distributed fragments were often documentable, but holder counts are conservative floors. |
| Join assigned | 1 no; 7 unclear; 0 yes | The strict join field is rarely resolved by accident-report text. |
| Pattern result | 1 supports; 7 indeterminate; 0 does not support | One existence result survives; prevalence cannot be estimated. |
| Sudden label | 2 yes; 1 no; 5 unclear | Official suddenness language is heterogeneous and weak as a grouping variable. |

Six cases support a numeric lower bound on lead time. Five also have a finite upper bound. The shortest bounded interval is PEMEX at one to two days; the longest exact interval is Givaudan at 4,411 days. U.S. Steel supplies only a lower bound of 1,096 days because the report says the practice existed for at least three years.[5]

These intervals measure time from the earliest qualifying report-supported signal on the selected pathway to the event. They do not imply that the signal’s full significance was understood throughout that period or that correction was straightforward.

## The “quiet” or “sudden” question remains weakly measured

Only U.S. Steel and Givaudan received a validated positive suddenness label. Bio-Lab received a negative label because the report expressly described observed warning signs and a run-to-failure pattern. Five cases remained unclear.

Among the two positive-label cases, Givaudan supports the WO-2 pattern and U.S. Steel is indeterminate. This pilot therefore does not establish separation between officially sudden-labelled events and genuinely unsignalled events. The labels apply to different referents, and official reports do not use a standardized “quiet failure” vocabulary. A future corpus should either define a controlled lexical taxonomy before coding or separate physical failure speed from epistemic surprise.

## Auxiliary searches

### A regulator can explicitly assign the join

A bounded existence search found two qualifying role designs. FAA 14 CFR Part 5 requires designated management personnel to coordinate organization-wide integration of a Safety Management System, facilitate hazard identification and risk analysis, monitor controls, and report to an accountable executive with final operational authority and a duty to direct corrective action. The regulation separately requires collection and analysis across operational monitoring, audits, investigations, employee reports, and other relevant data.[11]

European Medicines Agency pharmacovigilance guidance assigns the Qualified Person Responsible for Pharmacovigilance system-wide oversight, an overview of product safety profiles and emerging concerns, authority to influence the quality system and pharmacovigilance activities, safety-data submission responsibilities, and a route into urgent regulatory action.[12] [13]

These are existence proofs that a regulator can assign a cross-signal integration function to a named role with authority. They do not show that such a role existed or received the relevant fragments in any sampled CSB case. The full bounded search is recorded in the [regulatory join-role report](regulatory-join-role-search.md).

### No honestly costed and declined join was verified

A separate bounded search did not find a record that both priced a cross-holder aggregation function and documented a deliberate decision to decline it despite a stated risk-reduction purpose. The closest lead is the Army’s Military Flight Operations Quality Assurance program, which integrates multiple safety-data streams and was described as an unfunded requirement. The opened official sources did not supply the required cost estimate, benefit estimate, or component-head cost-benefit exclusion decision.[14] [15]

This is a bounded null, not a universal negative. The most efficient next step is a targeted records request or archive search for the Army decision documents rather than another broad web search. The full search scope and exclusions are recorded in the [inverse-case report](inverse-case-search.md).

## What the pilot establishes

The pilot establishes three things. First, at least one recent CSB investigation contains the full operational pattern under a strict, single-pathway reading. Second, pre-event signals and their communication are much easier to establish from accident reports than the assignment or non-assignment of an aggregation function. Third, explicit regulatory join roles exist, so the function is administratively ownable in at least some safety regimes.

The pilot does **not** establish that five of eight cases exhibit the pattern, that the pattern is prevalent in CSB investigations, or that cases described as sudden generally separate from unsignalled cases. The validation process is itself a useful instrument result: without an explicit same-pathway rule and an affirmative-evidence threshold for `join_assigned = no`, coders can manufacture apparent support by joining fragments that the source treats separately.

## Limitations

The sample contains eight reports from one U.S. agency and one industrial domain. Publication recency avoids selecting cases for fit but does not remove upstream agency selection, investigation, publication, or documentation effects.

Both initial coders and the validators were AI research agents operating under a common task design. Independent execution reduced direct copying but did not create human-blind adjudication. The work order’s proposed test by a person who has not seen the decomposition remains outstanding.

The same-pathway and suddenness clarifications were post hoc. They reduced positive findings rather than expanding them, but a future replication should publish those rules before selecting or coding cases.

The official reports were written to explain incidents and support recommendations, not to enumerate every organizational role or prove the absence of a join. The seven indeterminate results may reflect true ambiguity, reporting conventions, or limits of the public record. They cannot be interpreted as seven hidden positive cases.

The regulatory-role search was bounded rather than exhaustive, and the costed-decline search produced a bounded null. Neither supports a prevalence claim.

## Conclusion

The validated WO-2 pilot yields **one clear supporting case, seven indeterminate cases, and no affirmative non-supporting case**. Givaudan demonstrates that the proposed structure can be observed in an official accident record. The broader prevalence claim remains unresolved because accident reports rarely provide the affirmative organizational evidence required to distinguish an unassigned join from an undocumented or ineffective one.

The next strongest test is an externally blind replication with the clarified codebook, followed by targeted retrieval of the Army MFOQA cost-benefit or funding-decision record. Those steps would test both the instrument’s classification stability and the unresolved inverse case.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6324 "Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson"

[2]: https://www.csb.gov/file.aspx?DocumentId=6304 "Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility"

[3]: https://www.csb.gov/investigations/completed-investigations/ "U.S. Chemical Safety and Hazard Investigation Board Completed Investigations"

[4]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

[5]: https://www.csb.gov/file.aspx?DocumentId=6340 "Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works"

[6]: https://www.csb.gov/file.aspx?DocumentId=6316 "Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations"

[7]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery"

[8]: https://www.csb.gov/file.aspx?DocumentId=6296 "Explosion, Molten Salt Eruption, and Fatal Injury at TS USA Liquid Nitriding Facility"

[9]: https://www.csb.gov/file.aspx?DocumentId=6343 "Furnace Explosion and Fire at Shell Polymers"

[10]: https://www.csb.gov/file.aspx?DocumentId=6339 "Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility"

[11]: https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol1/pdf/CFR-2024-title14-vol1-part5.pdf "14 CFR Part 5—Safety Management Systems"

[12]: https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-module-i-pharmacovigilance-systems-and-their-quality-systems_en.pdf "Guideline on good pharmacovigilance practices, Module I: Pharmacovigilance systems and their quality systems"

[13]: https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-good-pharmacovigilance-practices-gvp-module-ix-signal-management-rev-1_en.pdf "Guideline on good pharmacovigilance practices, Module IX: Signal management"

[14]: https://www.ntsb.gov/investigations/AccidentReports/Reports/AIR2602.pdf "Collision of PSA Airlines Flight 5342 and a US Army Sikorsky UH-60L Black Hawk near Ronald Reagan Washington National Airport"

[15]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/605519.pdf?ver=2018-11-21-082114-987 "DoD Instruction 6055.19: Aviation Hazard Identification and Risk Assessment Programs"

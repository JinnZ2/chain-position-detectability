# WO-2 Pilot Reconciliation Log

> **Superseded audit trail.** This first reconciliation was replaced after independent validation applied a single-hazard-pathway rule and a stricter affirmative-evidence rule for `join_assigned = no`. Use [`reconciliation-log.md`](reconciliation-log.md) for the final record.

**Prepared by:** Manus AI
**Reconciliation date:** 19 September 2026
**Scope:** Eight U.S. Chemical Safety and Hazard Investigation Board (CSB) final reports fixed by the source manifest

## Method

Coder A and coder B were paired by `case_id`. Each value was compared independently for `signal_present`, `signal_reported`, `holder_count_known`, `holder_count_min` when a substantive lower bound was available, `join_assigned`, `first_signal_date`, both lead-time numbers and the maximum-known flag, `sudden_label`, and `pattern_result`. Agreement means exact equality of the raw values, not agreement after reconciliation. The Cuisine Solutions value `holder_count_min = 0` was expressly described by both coders as a schema placeholder rather than a supported lower bound; it was therefore treated as missing and excluded from the holder-count comparison. All other supplied values, including zero placeholders in lead-time fields, were compared exactly.

Disagreements were resolved from the cited official final-report evidence under the preregistered codebook. No majority rule was used. Missing evidence remained `unclear`, and unquantifiable numeric values were normalized to blank/null in the reconciled dataset rather than retained as substantive zeros.[1] [2]

## Agreement summary

| Variable | Exact agreements | Comparisons | Agreement |
| --- | ---: | ---: | ---: |
| `signal_present` | 8 | 8 | 100.0% |
| `signal_reported` | 8 | 8 | 100.0% |
| `holder_count_known` | 5 | 8 | 62.5% |
| `holder_count_min` | 5 | 7 | 71.4% |
| `join_assigned` | 5 | 8 | 62.5% |
| `first_signal_date` | 4 | 8 | 50.0% |
| `lead_time_days_min` | 4 | 8 | 50.0% |
| `lead_time_max_known` | 6 | 8 | 75.0% |
| `lead_time_days_max` | 5 | 8 | 62.5% |
| `sudden_label` | 4 | 8 | 50.0% |
| `pattern_result` | 5 | 8 | 62.5% |
| **Overall** | **59** | **87** | **67.8%** |

## 1. Shell Polymers Furnace Explosion and Fire

**Raw agreement:** 5 of 11 comparisons. The coders agreed that a relevant signal was present and reported, that the complete holder count was not known, that `join_assigned` was unclear, and that the pattern result was indeterminate. They disagreed on the holder lower bound, first-signal date, all three lead-time fields, and the sudden label.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_min` | 3 | 2 | **3** | The report supports three distinct role-level holders before ignition: the 2023 PHA revalidation team held the hazard analysis; the process automation, control, and optimization (PACO) engineer recognized the inadvertent furnace-side command; and the console operator received and acknowledged the unexpected-state alarm. The count is a conservative floor, not a census.[3] |
| `first_signal_date` | 2023 | unknown | **2023** | The report expressly dates the relevant PHA revalidation to 2023. Day and month are unavailable, so year precision is retained.[3] |
| `lead_time_days_min` | 521 | 0 | **521** | From the latest possible date in 2023, 31 December, to 4 June 2025 is 521 days. This is a precision-derived minimum, not an asserted occurrence date.[3] |
| `lead_time_max_known` | true | false | **true** | A calendar year is a bounded interval; the report therefore supports a finite upper bound.[3] |
| `lead_time_days_max` | 885 | 0 | **885** | From the earliest possible date in 2023, 1 January, to the event is 885 days.[3] |
| `sudden_label` | unclear | yes | **yes** | The codebook covers the warning pattern as well as the event. The official report calls the contemporaneous valve-status indication an “unexpected state” alarm. That is qualifying official wording for the warning pattern, although it does not mean the whole event was unwarned.[1] [3] |

**Final record:** `yes`, `yes`, holder minimum 3, `join_assigned = unclear`, first signal 2023, lead time 521–885 days, `sudden_label = yes`, `pattern_result = indeterminate`.

## 2. U.S. Steel Clairton Plant Coke Oven Explosion

**Raw agreement:** 6 of 11 comparisons. The coders agreed on signal presence and reporting, a minimum of two holders, the open maximum lead time, the sudden label, and the zero placeholder in the raw maximum field. They disagreed on holder-count completeness, join assignment, first signal, minimum lead time, and the pattern result.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_known` | false | true | **false** | The report documents a lower bound but does not enumerate every person, contractor, or organizational unit holding the relevant facility-siting and water-washing fragments.[4] |
| `join_assigned` | unclear | no | **no** | The affirmative evidence concerns the actual valve-washing operation: no washing procedure or hazard analysis existed; the Hazardous Job Meeting covered different planned work and none of the day-of-event washing personnel attended; and company systems allowed the supervisor to arrange and direct the task without prior planning, procedure, training, work permit, or sufficient hazard analysis. That is affirmative evidence that the work had no assigned integration point meeting the codebook’s responsibility-and-authority test.[4] |
| `first_signal_date` | 2003 | at least 3 years before 2025-08-11 | **2003** | The CSB expressly calls the 2003 PHA recommendation a key missed opportunity to address the facility-siting risk that increased this event’s fatal severity. The unit of analysis is the incident, not only its initiating valve mechanism, so the earlier signal qualifies.[4] |
| `lead_time_days_min` | 7,894 | 1,096 | **7,894** | With year-only precision, the latest possible 2003 date is 31 December 2003; the interval to 11 August 2025 is 7,894 days.[4] |
| `lead_time_max_known` | false | false | **true** | Both coders mistakenly treated year precision as open. Calendar year 2003 supplies a bounded range.[4] |
| `lead_time_days_max` | 0 | 0 | **8,258** | The earliest possible date in 2003 is 1 January, producing the finite upper bound.[4] |
| `pattern_result` | indeterminate | supports | **supports** | A signal was reported to at least two holders, and the actual causal work lacked an assigned integration point. All four necessary conditions are established.[4] |

**Final record:** `yes`, `yes`, holder minimum 2, `join_assigned = no`, first signal 2003, lead time 7,894–8,258 days, `sudden_label = yes`, `pattern_result = supports`.

## 3. Bio-Lab Conyers Fire and Chemical Release

**Raw agreement:** 7 of 11 comparisons. The coders agreed on signal presence and reporting, holder-count fields, unresolved join assignment, a bounded exact interval structure, and an indeterminate pattern result. They disagreed on the earliest signal, both lead-time numbers, and suddenness.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `first_signal_date` | 2020-08-27 | 2019-12-30 | **2019-12-30** | The same-site fire-water piping bolt failure caused by corrosion is the report’s first dated sprinkler-component failure. The CSB connects that corrosion/run-to-failure history to the eventual sprinkler failure that let water contact stored chemicals. It predates the 2020 cross-facility event.[5] |
| `lead_time_days_min` | 1,494 | 1,735 | **1,735** | Both endpoints are exact dates; 30 December 2019 to 29 September 2024 is 1,735 days.[5] |
| `lead_time_days_max` | 1,494 | 1,735 | **1,735** | The interval is exact at calendar-day precision.[5] |
| `sudden_label` | unclear | no | **no** | The report affirmatively frames the relevant warning pattern as “Run To Failure” and says warning signs from corrosion and frequent leaks had been observed. This supports a negative label for the warning pattern; it is not inferred merely from absence of the word “sudden.”[5] |

**Final record:** `yes`, `yes`, holder minimum 3, `join_assigned = unclear`, first signal 2019-12-30, exact lead time 1,735 days, `sudden_label = no`, `pattern_result = indeterminate`.

## 4. Givaudan Sense Colour Explosion

**Raw agreement:** 11 of 11 comparisons. Both coders selected the exact 15 October 2012 reactivity test, its transmission to an outside consultant, a two-holder minimum, and the CSB’s express finding that no process-safety-policy owner was adequately assigned or trained. Both coded the “rapid temperature and pressure rise” as a close suddenness equivalent.[6]

**Final record:** `yes`, `yes`, holder minimum 2, `join_assigned = no`, first signal 2012-10-15, exact lead time 4,411 days, `sudden_label = yes`, `pattern_result = supports`.

## 5. Dow Louisiana Operations Explosions

**Raw agreement:** 7 of 11 comparisons. The coders agreed on signal presence and reporting, the exact 20 November 2020 first-signal date and 966-day interval, and the unclear sudden label. They disagreed on holder-count completeness and minimum, join assignment, and the pattern result.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_known` | false | true | **false** | The report supports at least two distinct functions but does not enumerate all pre-event holders of the pressure, inventory, contractor, and closure fragments.[7] |
| `holder_count_min` | 1 | 2 | **2** | The CSB separately documents a unit-level equipment-tracking function holding the five-unreturned-lights fragment and vessel-closure functions holding work-completion and visual-inspection fragments. Neither fragment alone disclosed the full condition; both were present before the event. A transmitter is not counted as a holder.[7] |
| `join_assigned` | unclear | no | **no** | The report affirmatively says there was no official vessel-specific equipment-tracking procedure and that the closure form did not require the permit writer to reconcile contractor materials. The operator had no exact way to know all equipment had left the vessel. This is affirmative evidence of an unassigned cross-holder reconciliation function for the initiating debris pathway.[7] |
| `pattern_result` | indeterminate | supports | **supports** | A reported pre-event signal existed, at least two holder functions possessed relevant fragments, and the vessel-specific join was affirmatively absent.[7] |

**Final record:** `yes`, `yes`, holder minimum 2, `join_assigned = no`, first signal 2020-11-20, exact lead time 966 days, `sudden_label = unclear`, `pattern_result = supports`.

## 6. PEMEX Deer Park Chemical Release

**Raw agreement:** 5 of 11 comparisons. The coders agreed on signal presence and reporting, a minimum of two holders, an open maximum lead time, and the zero raw placeholder for that maximum. They disagreed on count completeness, join assignment, first-signal date, minimum lead time, sudden label, and pattern result.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_known` | true | false | **false** | The operator and Repcon foreman establish a lower bound, but the report identifies additional operators, boilermakers, permit roles, and process owners without establishing a complete set.[8] |
| `join_assigned` | no | unclear | **no** | The report provides affirmative functional evidence: the permit had no defined hold/stop point; the issuer, receiver, and boilermakers understood it differently; the active-unit status did not reach the boilermakers; and the nominal SIMOPs responsibilities produced no evaluation. For this job, fragmented duties did not assign one responsible-and-authorized join.[8] |
| `first_signal_date` | unknown | 2024-10-08 | **unknown** | The 8 October tag placement is a dated manifestation, but the earliest qualifying signal is the pre-existing inadequate Run-and-Maintain identification/control state. The report does not date that system’s adoption or first observation.[8] |
| `lead_time_days_min` | 0 | 1 | **null** | No numeric minimum is defensible for the undated earliest state. The reconciled CSV uses a null rather than a zero placeholder.[1] [8] |
| `sudden_label` | unclear | no | **unclear** | The only “sudden” or “abrupt” wording describes worker reassignment, not the release or warning pattern. The report does not affirmatively characterize the event as non-sudden; missing applicable language remains unclear.[1] [8] |
| `pattern_result` | supports | indeterminate | **supports** | Signal, reporting, a two-holder minimum, and affirmative evidence of no assigned join are all established.[8] |

**Final record:** `yes`, `yes`, holder minimum 2, `join_assigned = no`, first signal unknown, lead time unquantifiable, `sudden_label = unclear`, `pattern_result = supports`.

## 7. Cuisine Solutions Ammonia Release

**Raw agreement:** 9 of 10 substantive comparisons. The only disagreement was `sudden_label`; the nominal holder-count zeros were both schema placeholders and were excluded from agreement measurement.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_min` | 0 placeholder | 0 placeholder | **null** | Because no qualifying signal is established, the report supports no substantive holder lower bound. Null is the codebook value.[1] [9] |
| `lead_time_days_min` | 0 placeholder | 0 placeholder | **null** | No earliest qualifying signal exists from which to calculate a duration.[1] [9] |
| `lead_time_days_max` | 0 placeholder | 0 placeholder | **null** | The upper bound is unquantifiable, not zero.[1] [9] |
| `sudden_label` | unclear | yes | **yes** | The CSB’s technical finding describes a “sudden pressure drop” when the relief valve opened. This is official wording for a failure-sequence submechanism and therefore passes the broad codebook field, but it does not imply that the initiating upset was unexpected or that the event lacked warnings.[9] |

The CSB could not verify whether the pump shutdown and water-temperature fluctuations were related to the overpressure. Accordingly, `signal_present` and `signal_reported` remain unclear, rather than being forced to either yes or no.[9]

**Final record:** `signal_present = unclear`, `signal_reported = unclear`, no defensible holder minimum, `join_assigned = unclear`, first signal unknown, lead time unquantifiable, `sudden_label = yes`, `pattern_result = indeterminate`.

## 8. TS USA Molten Salt Eruption

**Raw agreement:** 9 of 11 comparisons. The coders agreed on all substantive pattern components, first-signal date, minimum lead time, suddenness, and support. They disagreed on whether the complete holder count and lead-time maximum were known.

| Variable | Coder A | Coder B | Reconciled value | Resolution |
| --- | --- | --- | --- | --- |
| `holder_count_known` | true | true | **false** | This is an agreed raw value corrected during reconciliation. Both narratives expressly call two a lower bound and acknowledge additional possible holders; therefore the complete count is not known.[10] |
| `lead_time_max_known` | false | true | **true** | The selected earliest signal is the exact 25 January 2018 Mexico explosion. The undated corporate risk analysis is described as prepared before the 2023 Chattanooga event, but the report does not establish that it predates 2018; it cannot extend the selected earliest date. The exact endpoint dates therefore give a bounded 2,317-day interval.[10] |
| `lead_time_days_max` | 0 | 2,317 | **2,317** | For the same reason, the maximum equals the exact minimum.[10] |

**Final record:** `yes`, `yes`, holder minimum 2, `join_assigned = no`, first signal 2018-01-25, exact lead time 2,317 days, `sudden_label = yes`, `pattern_result = supports`.

## Reconciled outcome

The complete eight-case manifest and two readable evidence records per case permit a conclusive pilot result. Five cases support the operational pattern, none affirmatively fails a necessary component, and three remain indeterminate. The result is **pattern observed within this bounded CSB pilot**, not a population estimate or a claim about accident causation outside these eight reports.

## Appendix: Complete Raw Comparison Matrix

Each row below records the two raw coder values and whether they agree exactly. “Not compared” is used only for Cuisine Solutions’ `holder_count_min`, because both source records identify zero as a schema placeholder rather than a substantive known lower bound.

| Case | Variable | Coder A | Coder B | Status |
| --- | --- | --- | --- | --- |
| `shell-polymers` | `signal_present` | `yes` | `yes` | **Agreement** |
| `shell-polymers` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `shell-polymers` | `holder_count_known` | `false` | `false` | **Agreement** |
| `shell-polymers` | `holder_count_min` | `3` | `2` | **Disagreement** |
| `shell-polymers` | `join_assigned` | `unclear` | `unclear` | **Agreement** |
| `shell-polymers` | `first_signal_date` | `2023` | `unknown` | **Disagreement** |
| `shell-polymers` | `lead_time_days_min` | `521` | `0` | **Disagreement** |
| `shell-polymers` | `lead_time_max_known` | `true` | `false` | **Disagreement** |
| `shell-polymers` | `lead_time_days_max` | `885` | `0` | **Disagreement** |
| `shell-polymers` | `sudden_label` | `unclear` | `yes` | **Disagreement** |
| `shell-polymers` | `pattern_result` | `indeterminate` | `indeterminate` | **Agreement** |
| `us-steel-clairton` | `signal_present` | `yes` | `yes` | **Agreement** |
| `us-steel-clairton` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `us-steel-clairton` | `holder_count_known` | `false` | `true` | **Disagreement** |
| `us-steel-clairton` | `holder_count_min` | `2` | `2` | **Agreement** |
| `us-steel-clairton` | `join_assigned` | `unclear` | `no` | **Disagreement** |
| `us-steel-clairton` | `first_signal_date` | `2003` | `at least 3 years before 2025-08-11` | **Disagreement** |
| `us-steel-clairton` | `lead_time_days_min` | `7894` | `1096` | **Disagreement** |
| `us-steel-clairton` | `lead_time_max_known` | `false` | `false` | **Agreement** |
| `us-steel-clairton` | `lead_time_days_max` | `0` | `0` | **Agreement** |
| `us-steel-clairton` | `sudden_label` | `yes` | `yes` | **Agreement** |
| `us-steel-clairton` | `pattern_result` | `indeterminate` | `supports` | **Disagreement** |
| `bio-lab-conyers` | `signal_present` | `yes` | `yes` | **Agreement** |
| `bio-lab-conyers` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `bio-lab-conyers` | `holder_count_known` | `false` | `false` | **Agreement** |
| `bio-lab-conyers` | `holder_count_min` | `3` | `3` | **Agreement** |
| `bio-lab-conyers` | `join_assigned` | `unclear` | `unclear` | **Agreement** |
| `bio-lab-conyers` | `first_signal_date` | `2020-08-27` | `2019-12-30` | **Disagreement** |
| `bio-lab-conyers` | `lead_time_days_min` | `1494` | `1735` | **Disagreement** |
| `bio-lab-conyers` | `lead_time_max_known` | `true` | `true` | **Agreement** |
| `bio-lab-conyers` | `lead_time_days_max` | `1494` | `1735` | **Disagreement** |
| `bio-lab-conyers` | `sudden_label` | `unclear` | `no` | **Disagreement** |
| `bio-lab-conyers` | `pattern_result` | `indeterminate` | `indeterminate` | **Agreement** |
| `givaudan-sense-colour` | `signal_present` | `yes` | `yes` | **Agreement** |
| `givaudan-sense-colour` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `givaudan-sense-colour` | `holder_count_known` | `false` | `false` | **Agreement** |
| `givaudan-sense-colour` | `holder_count_min` | `2` | `2` | **Agreement** |
| `givaudan-sense-colour` | `join_assigned` | `no` | `no` | **Agreement** |
| `givaudan-sense-colour` | `first_signal_date` | `2012-10-15` | `2012-10-15` | **Agreement** |
| `givaudan-sense-colour` | `lead_time_days_min` | `4411` | `4411` | **Agreement** |
| `givaudan-sense-colour` | `lead_time_max_known` | `true` | `true` | **Agreement** |
| `givaudan-sense-colour` | `lead_time_days_max` | `4411` | `4411` | **Agreement** |
| `givaudan-sense-colour` | `sudden_label` | `yes` | `yes` | **Agreement** |
| `givaudan-sense-colour` | `pattern_result` | `supports` | `supports` | **Agreement** |
| `dow-louisiana-operations` | `signal_present` | `yes` | `yes` | **Agreement** |
| `dow-louisiana-operations` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `dow-louisiana-operations` | `holder_count_known` | `false` | `true` | **Disagreement** |
| `dow-louisiana-operations` | `holder_count_min` | `1` | `2` | **Disagreement** |
| `dow-louisiana-operations` | `join_assigned` | `unclear` | `no` | **Disagreement** |
| `dow-louisiana-operations` | `first_signal_date` | `2020-11-20` | `2020-11-20` | **Agreement** |
| `dow-louisiana-operations` | `lead_time_days_min` | `966` | `966` | **Agreement** |
| `dow-louisiana-operations` | `lead_time_max_known` | `true` | `true` | **Agreement** |
| `dow-louisiana-operations` | `lead_time_days_max` | `966` | `966` | **Agreement** |
| `dow-louisiana-operations` | `sudden_label` | `unclear` | `unclear` | **Agreement** |
| `dow-louisiana-operations` | `pattern_result` | `indeterminate` | `supports` | **Disagreement** |
| `pemex-deer-park` | `signal_present` | `yes` | `yes` | **Agreement** |
| `pemex-deer-park` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `pemex-deer-park` | `holder_count_known` | `true` | `false` | **Disagreement** |
| `pemex-deer-park` | `holder_count_min` | `2` | `2` | **Agreement** |
| `pemex-deer-park` | `join_assigned` | `no` | `unclear` | **Disagreement** |
| `pemex-deer-park` | `first_signal_date` | `unknown` | `2024-10-08` | **Disagreement** |
| `pemex-deer-park` | `lead_time_days_min` | `0` | `1` | **Disagreement** |
| `pemex-deer-park` | `lead_time_max_known` | `false` | `false` | **Agreement** |
| `pemex-deer-park` | `lead_time_days_max` | `0` | `0` | **Agreement** |
| `pemex-deer-park` | `sudden_label` | `unclear` | `no` | **Disagreement** |
| `pemex-deer-park` | `pattern_result` | `supports` | `indeterminate` | **Disagreement** |
| `cuisine-solutions` | `signal_present` | `unclear` | `unclear` | **Agreement** |
| `cuisine-solutions` | `signal_reported` | `unclear` | `unclear` | **Agreement** |
| `cuisine-solutions` | `holder_count_known` | `false` | `false` | **Agreement** |
| `cuisine-solutions` | `holder_count_min` | `0` | `0` | Not compared |
| `cuisine-solutions` | `join_assigned` | `unclear` | `unclear` | **Agreement** |
| `cuisine-solutions` | `first_signal_date` | `unknown` | `unknown` | **Agreement** |
| `cuisine-solutions` | `lead_time_days_min` | `0` | `0` | **Agreement** |
| `cuisine-solutions` | `lead_time_max_known` | `false` | `false` | **Agreement** |
| `cuisine-solutions` | `lead_time_days_max` | `0` | `0` | **Agreement** |
| `cuisine-solutions` | `sudden_label` | `unclear` | `yes` | **Disagreement** |
| `cuisine-solutions` | `pattern_result` | `indeterminate` | `indeterminate` | **Agreement** |
| `ts-usa` | `signal_present` | `yes` | `yes` | **Agreement** |
| `ts-usa` | `signal_reported` | `yes` | `yes` | **Agreement** |
| `ts-usa` | `holder_count_known` | `true` | `true` | **Agreement** |
| `ts-usa` | `holder_count_min` | `2` | `2` | **Agreement** |
| `ts-usa` | `join_assigned` | `no` | `no` | **Agreement** |
| `ts-usa` | `first_signal_date` | `2018-01-25` | `2018-01-25` | **Agreement** |
| `ts-usa` | `lead_time_days_min` | `2317` | `2317` | **Agreement** |
| `ts-usa` | `lead_time_max_known` | `false` | `true` | **Disagreement** |
| `ts-usa` | `lead_time_days_max` | `0` | `2317` | **Disagreement** |
| `ts-usa` | `sudden_label` | `yes` | `yes` | **Agreement** |
| `ts-usa` | `pattern_result` | `supports` | `supports` | **Agreement** |

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

# WO-2 Evidence Record — Bio-Lab Inc. Conyers Fire and Chemical Release

**Case ID:** `bio-lab-conyers`
**Independent coder:** B
**Event date:** 2024-09-29
**Official final report:** *Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility*, CSB Investigation Report No. 2024-04-I-GA, published July 2026.[1]

## Coding conclusion

| Variable | Coded value |
|---|---:|
| `signal_present` | **yes** |
| `signal_reported` | **yes** |
| `holder_count_known` | **false** |
| `holder_count_min` | **3** |
| `join_assigned` | **unclear** |
| `first_signal_date` | **2019-12-30** |
| `event_date` | **2024-09-29** |
| `lead_time_days_min` | **1,735** |
| `lead_time_max_known` | **true** |
| `lead_time_days_max` | **1,735** |
| `sudden_label` | **no** |
| `pattern_result` | **indeterminate** |

## Incident mechanism and chronology

The CSB identifies the initiating mechanism as a failed sprinkler-system component allowing water to contact stored chlorinated isocyanurates. The ensuing reactions generated heat, activated other sprinkler heads, wetted more chemicals, and led to toxic vapors and fires (printed report p. 7; PDF p. 7).[1] Its formal findings likewise state that a sprinkler-component failure is the most likely initiating water-source scenario, based on the initial fire-watch report to multiple parties, the established corrosion-failure history, and water flow observed before firefighting water was applied (printed report p. 120; PDF p. 120).[1]

At about 5:00 a.m. on September 29, 2024, a fire-watch employee heard popping and, based on prior experience and training, concluded that product was wet. That employee called the other fire-watch employee, notified off-site management, and placed “Code red plant 12” in the Emergency Response Team (ERT) Telegram channel (printed report pp. 38–39; PDF pp. 38–39).[1] This is incident-time reporting, not the basis for the pre-event signal coding.

## Signals, relevance, and earliest date

**Signal present = yes.** The earliest documented, directionally relevant signal is the December 30, 2019 sprinkler-system component failure. The report says TCCA storage began in the Plant 12 bunker on November 5, 2019; construction personnel had observed corroded sprinkler heads by December 31, 2019 and piping leaks after bolts became prematurely rusted; and “the first sprinkler system component failure” occurred on **December 30, 2019**, when fire-water-piping bolts corroded through (printed report p. 61; PDF p. 61).[1] The date is anomalously one day before the stated observation date, but it is the report’s explicit date for the component failure and is retained as printed.

The report expressly connects that early corrosion/leak signal to the same hazard mechanism: corrosive vapor from chlorinated-isocyanurate storage damaged the fire-protection system, and multiple component failures in the weeks before the incident culminated in a reported sprinkler-head failure as the initiating water source (printed report pp. 60–61; PDF pp. 60–61).[1] The CSB’s run-to-failure analysis is still more explicit: employees observed corrosion-related sprinkler-system leaks; leaking water posed a **known risk** of contacting stored chlorinated isocyanurates, known to lead to decomposition reactions and off-gassing (printed report p. 78; PDF p. 78).[1]

Additional, independently documented relevant signals confirm persistence rather than provide the coding date. Third-party annual reports documented corroded sprinkler heads as deficiencies in 2021 and 2022; each identified more than 500 corroded or rusty heads in the oxidizer-storage bunker (printed report p. 63; PDF p. 63).[1] In December 2023, inspectors visually observed corrosion on 1,124 heads outside the bunker across four of seven sprinkler-system zones, spatially correlated with oxidizer storage (printed report p. 66; PDF p. 66).[1] The report also records emergency repairs of multiple corroded heads on September 13 and September 17–20, 2024, and a September 19 leak communicated at 2:50 a.m. to the ERT (printed report p. 68; PDF p. 68).[1]

## Reporting and holders

**Signal reported = yes.** The record documents multiple pre-event routes beyond a person’s private awareness. The 2021 and 2022 annual inspection reports recorded corroded sprinkler-head deficiencies (printed report p. 63; PDF p. 63).[1] The report says the insurer risk-assessment reports directly addressed widespread multi-building corrosion to KIK corporate employees at the vice-president and manager levels (printed report p. 93; PDF p. 93).[1] It also says that a September 19, 2024 sprinkler-head leak was communicated to the ERT (printed report p. 68; PDF p. 68).[1]

**Holder count minimum = 3; known = false.** Three distinct documented holders/functions form a conservative lower bound:

1. **Construction personnel** observed corroded heads and piping leaks in the 2019 Plant 12 history (printed report p. 61; PDF p. 61).[1]
2. The **fire-protection contractor/inspector** documented corrosion as deficiencies in annual 2021 and 2022 reports (printed report p. 63; PDF p. 63).[1]
3. **KIK corporate employees at vice-president and manager level** were directly addressed in insurer risk-assessment reports about widespread corrosion (printed report p. 93; PDF p. 93).[1]

The number is a floor, not a complete count: the report separately identifies employees, local management, EHS, the ERT, alarm monitoring, insurers, and corporate personnel. It does not establish a closed universe of holders.

## Aggregation assignment

**Join assigned = unclear.** There is evidence of partial reporting responsibilities and hierarchical communication, but not the required evidence of one named role/function that both had responsibility **and authority** to aggregate the relevant cross-holder signals before the event.

Local Bio-Lab Conyers EHS was responsible for implementing the March 2024 Fire Impairment Procedure and “should also have communicated” frequent-impairment hazards and risks to corporate KIK leadership (printed report p. 97; PDF p. 97).[1] The corporate procedure required facilities to document and track each fire-system impairment via a permit; impairments longer than four hours required notification to KIK’s risk insurer, and unplanned impairments were to be reported and investigated to prevent recurrence (printed report p. 96; PDF p. 96).[1] Separately, the report finds KIK did not provide adequate organizational oversight to ensure corrective actions were systematically evaluated at Conyers and implemented across locations (printed report p. 9; PDF p. 9).[1]

Those facts show reporting channels and organizational oversight failure. They do **not** name a particular pre-event integrator with both the duty and decision authority to combine the construction observations, third-party inspection findings, insurer assessment results, local leak experience, and knowledge that water contacting chlorinated isocyanurates could cause decomposition. Under the codebook’s strict rule, `unclear` is required rather than inferring an assigned join from EHS implementation duties, executive awareness, or a corporate procedure.

## Lead time calculation

**Earliest supported date:** 2019-12-30. **Event:** 2024-09-29. The calendar difference is **1,735 days**. Because both endpoints are exact report dates, the defensible minimum and maximum are equal: `lead_time_days_min = 1735`, `lead_time_days_max = 1735`, and `lead_time_max_known = true`.

This is a mechanism-specific lead time for the first documented sprinkler-system failure caused by corrosion in the same Plant 12 warehouse. It is not a claim that every relevant risk was continuously understood, recorded, or actionable throughout every one of those days.

## Suddenness and pattern result

**Sudden label = no.** I found no official characterization of the event, failure, or warning pattern as “sudden,” “unexpected,” “unforeseen,” “without warning,” or a close equivalent. The report instead labels the safety issue **“Run To Failure”** and states that warning signs related to corrosion and frequent leaks had been observed (printed report p. 78; PDF p. 78).[1] The report’s use of “sudden” concerns a pre-incident inventory-reduction focus, not the incident or its warning pattern (printed report p. 96; PDF p. 96).[1]

**Pattern result = indeterminate.** Signals were present and reported, and the evidence supports at least three holders. However, the necessary `join_assigned = no` condition is unresolved: the official report documents channels, responsibilities, and oversight failure but not affirmative evidence that no authorized integration function existed. The codebook therefore requires `indeterminate`, not `supports`.

## Decisive evidence excerpts

> “The first sprinkler system component failure at the warehouse [occurred] on December 30, 2019, when bolts on the fire water piping corroded through.” — printed report p. 61; PDF p. 61.[1]

> “The leaking water posed a known risk of contact with stored chlorinated isocyanurates, which was known to lead to decomposition reactions and product off-gassing.” — printed report p. 78; PDF p. 78.[1]

> “Evidence of widespread corrosion in multiple buildings at Bio-Lab Conyers was not only known to plant-level management but was directly addressed to KIK corporate employees at the vice president and manager level in annual insurance risk assessment reports.” — printed report p. 93; PDF p. 93.[1]

> “Although local Bio-Lab Conyers EHS on-site was responsible for implementation, they should also have communicated the hazards and risks associated with frequent fire protection impairments to its corporate KIK leadership.” — printed report p. 97; PDF p. 97.[1]

> “The CSB determined that the cause of the incident was a corroded sprinkler system component that failed, allowing water to contact the stored pool-treatment chemicals (chlorinated isocyanurates) inside the Bio-Lab warehouse.” — printed report p. 124; PDF p. 124.[1]

## Limitations

The first signal date is taken from the report’s expressly dated December 30, 2019 component failure, despite the immediately preceding sentence saying personnel observed corroded sprinkler heads by December 31, 2019. The record does not resolve that one-day sequencing anomaly, so no earlier date is invented.

The 2019 item establishes the earliest documented signal directly tied to the initiating mechanism, but it is not evidence that a single named person held every later fragment. Holder count is a conservative lower bound and is intentionally not treated as known.

The report identifies local EHS implementation responsibility, corporate leadership awareness, procedures, and a failure of corporate enforcement. It does not expressly define one role’s authority to aggregate all relevant fragments and require risk-reducing action. `join_assigned` is therefore `unclear`; it must not be inferred as either yes or no.

No official suddenness wording applicable to the event, failure, or warning pattern was found. This is coded `no` because the report affirmatively describes prior warning signs and a run-to-failure pattern; the report’s unrelated reference to a “sudden focus” on inventory reduction does not qualify.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6339 "Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility — CSB Investigation Report No. 2024-04-I-GA"

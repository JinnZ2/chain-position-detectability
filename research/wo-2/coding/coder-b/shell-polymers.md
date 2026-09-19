# WO-2 Evidence Record — Shell Polymers Furnace Explosion and Fire

**Coder:** B
**Case ID:** `shell-polymers`
**Incident date:** 2025-06-04
**Official final report:** [CSB final investigation report][1]
**Official investigation page:** [CSB incident page][2]

## Coding decision

| Variable | Code | Evidence-based rationale |
| --- | --- | --- |
| `signal_present` | **yes** | Before the event, the process-hazard-analysis (PHA) revalidation team identified a reverse-flow pathway during furnace shutdown and recommended that management eliminate that risk. The report explicitly locates the incident mechanism in cracked-gas backflow to the furnace firebox. This is a documented, case-specific pre-event hazard signal rather than general background knowledge. [1] |
| `signal_reported` | **yes** | The PHA team “recommended that management eliminate this risk of reverse flow”; management considered it and determined the risk tolerable. Thus the signal was communicated beyond the team before the event. [1] |
| `holder_count_known` | **false** | The record supports a lower bound, but not an exhaustive count of all persons or units that held relevant information. |
| `holder_count_min` | **2** | The PHA revalidation team and Shell management are distinct documented organizational holders: the team made a recommendation **to** management, and management made the tolerability determination. This is a conservative lower bound; it does not additionally count the later PACO engineer and console operator. [1] |
| `join_assigned` | **unclear** | The report shows the PHA team assessed a reverse-flow hazard and management made a risk-acceptance decision, but it does not establish that either had both responsibility and authority to aggregate that prior hazard information with the later task-specific valve/alarm signals. Nor does it affirmatively establish that no such integration function existed. |
| `first_signal_date` | **unknown** | The report says the PHA *revalidation* team identified the reverse-flow cause before the event but supplies no date or bounded interval for that revalidation, recommendation, or management decision. [1] |
| `lead_time_days_min` | **0** | No numeric lower bound from the earliest relevant signal can be defended because the report does not date the PHA revalidation signal. The value is therefore 0 under the task instruction rather than an inferred interval. |
| `lead_time_max_known` | **false** | The report gives no bounded earliest-signal-to-event interval. |
| `lead_time_days_max` | **0** | Upper bound is open/unknown; 0 is used under the task instruction rather than inventing a maximum. |
| `sudden_label` | **yes** | The report calls the command-related indication an “alarm indicating that the MOV was in an **unexpected state**.” This supports the codebook’s specified “unexpected” wording for the warning pattern, although the report does not generally label the entire event as sudden. [1] |
| `pattern_result` | **indeterminate** | The case meets the documented-signal, reporting, and minimum-two-holder conditions, but `join_assigned` remains unresolved. Therefore it cannot meet the codebook requirement for `supports`, and there is no affirmative evidence that a necessary condition was false. |

## Decisive official evidence

The CSB’s causal finding identifies the relevant mechanism: simultaneous opening of the two isolation motor-operated valves created a path for cracked gas to “backflow and accumulate in the furnace’s firebox,” where a flame ignited it. The CSB also identifies ineffective administrative controls as a contributor. [1]

> “The Shell PHA revalidation team also identified a separate cause of reverse flow of cracked gas during a furnace shutdown. The team determined that cracked gas could flow through a tubing bypass around a differential pressure transmitter between the quench tower and the furnace. The team recommended that management eliminate this risk of reverse flow. However, this recommendation was not accepted because Shell management determined the risk associated with reverse flow was tolerable.” [1]

This is sufficient to code a pre-event, site/process-specific signal and reported communication. The report then concludes that Shell “actively chose to rely solely on administrative controls to prevent a potentially fatal explosion in its process hazard analysis revalidation.” [1] The report does not date that revalidation, so it cannot support a numeric lead-time interval.

The incident-day record independently documents a short, task-level signal sequence. At **2:14:28 p.m.** the PACO engineer commanded the Furnace 5 furnace-side MOV open. At **2:16:46 p.m.** the engineer realized that command had been inadvertent. At **2:20 p.m.** the console operator noticed the furnace-side valve open while the tower-side valve was opening and immediately directed the engineer to close it. The explosion occurred at **2:20:45 p.m.** [1] The analysis further reports that the furnace-side valve opening produced an unexpected-state alarm to the console operator; the operator dismissed it after assuming that it concerned the planned tower-side-valve task. [1] These facts corroborate the presence of distinct, communicated task-level information, but they do not establish an organizational role authorized and responsible to integrate it with the earlier PHA signal.

## Organizational-role assessment

The named PHA revalidation team performed hazard identification and made a recommendation. Shell management made the tolerability decision. These are documented roles with a communication path, but the final report does not say that the PHA team had authority to implement controls or that management was assigned to integrate PHA results with the later start-up task, SIS-bypass practice, valve status, and console alarms. The report instead says that the console operator and process-control engineer had discussed opening the tower-side valve, which caused the operator to assume the unexpected-state alarm was associated with that task. [1] That evidence does not satisfy the codebook’s stricter responsibility-and-authority test for `join_assigned=yes`.

## Limitations

The report describes the PHA team’s reverse-flow scenario as a “separate cause” involving a tubing bypass, whereas the event’s immediate route was simultaneous opening of two MOVs. It is coded as directionally relevant because the CSB’s incident cause is cracked-gas backflow to the furnace firebox and the CSB discusses the PHA finding in its incident safety-issue analysis; it should not be treated as proof that the team identified the exact eventual two-MOV sequence. [1]

The exact date of the PHA revalidation, its recommendation, and management’s risk decision is absent. Consequently, the record preserves `first_signal_date=unknown` and does not calculate a lead time from the precisely timed June 4 operational warning. Although that operational sequence lasted only minutes, it is not necessarily the earliest signal.

No official final-report evidence establishes a named role or function with both responsibility and authority to join the PHA signal and the operational valve/alarm information. Missing evidence is coded `unclear`, not `no`.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6343 "U.S. Chemical Safety and Hazard Investigation Board, Shell Polymers Furnace Explosion and Fire — Investigation Report"

[2]: https://www.csb.gov/shell-polymers-furnace-explosion-and-fire/ "U.S. Chemical Safety and Hazard Investigation Board, Shell Polymers Furnace Explosion and Fire"

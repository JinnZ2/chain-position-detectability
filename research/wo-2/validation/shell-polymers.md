# WO-2 Validation Record — Shell Polymers Furnace Explosion and Fire

**Case ID:** `shell-polymers`
**Validator:** Manus AI
**Verdict:** **Needs correction.** The reconciled record is supported and pathway-coherent except for `sudden_label`. Its `yes` rests only on the wording of an alarm label, which does not satisfy the requested additional rule. The corrected label is `unclear`; the pattern result remains `indeterminate`.

## Corrected coding

| Variable | Corrected value | Validation finding |
| --- | --- | --- |
| `signal_present` | **yes** | The 2023 PHA identified the same two-MOV reverse-flow explosion pathway that the CSB identifies as the incident cause. |
| `signal_reported` | **yes** | On the incident day, the relevant MOV-state alarm “was sent to the console operator”; this is recorded communication beyond private awareness on that same pathway. |
| `holder_count_min` | **3** | Conservative lower bound: the PHA revalidation team, the PACO engineer who realized the inadvertent furnace-side command, and the console operator who received the MOV-state alarm. |
| `holder_count_established` | **false** | The report supports the three-holder minimum, not a complete enumeration of relevant holders. |
| `join_assigned` | **unclear** | No report evidence identifies one role/function with both authority and responsibility to aggregate these three pathway fragments; nor does the report affirmatively establish that no such join existed. |
| `first_signal_date` | **2023** | The PHA revalidation is expressly dated only to 2023. |
| `lead_time_days_min` | **521** | Year-bounded interval from 2023-12-31 to the 2025-06-04 event. |
| `lead_time_max_known` | **true** | A stated calendar year is a bounded interval. |
| `lead_time_days_max` | **885** | Year-bounded interval from 2023-01-01 to the event. |
| `sudden_label` | **unclear** | “Unexpected state” is the wording of the MOV alarm label, not a CSB characterization that the event, failure, or warning pattern itself was sudden/unexpected. |
| `pattern_result` | **indeterminate** | `join_assigned` is unresolved. The codebook permits `supports` only when it is affirmatively `no`. |

## Coherent hazard pathway and decisive evidence

The selected pathway is the **Furnace 5 two-MOV isolation failure**: opening the furnace-side MOV while the tower-side MOV was open permitted cracked gas to backflow into the firebox, accumulate, and ignite. It is one pathway from the 2023 PHA signal through the incident-day command and alarm fragments to the event—not a combination of the PHA’s separate tubing-bypass scenario with the event mechanism.

> “In its 2023 revalidation of the ethane cracking unit process hazard analysis (PHA), Shell identified the explosion hazard in an offline furnace from misdirected/reverse flow when the furnace-side MOV failed to close while the tower-side MOV was open as an incident that could result in multiple fatalities.” [1]

> “The CSB determined that the cause of the incident was the inadvertent simultaneous opening of both motor-operated valves that were being used to isolate the furnace. Opening both valves created a path for cracked gas to backflow and accumulate in the furnace’s firebox, where an existing flame ignited the flammable vapors, resulting in the explosion.” [1]

The PHA quotation identifies the same two-MOV/reverse-flow pathway as the causal finding. The following passage on the next page is not used as the signal: it calls a tubing bypass a “separate cause of reverse flow.” That exclusion preserves the required pathway coherence. [1]

The immediate pathway fragments also cohere. The CSB records that the PACO engineer “realized that they had inadvertently issued an open command to the Furnace 5 furnace-side MOV” at 2:16:46 p.m.; the console operator later observed both relevant valve states; and the explosion occurred at 2:20:45 p.m. [1] Separately, the report states: “When the furnace-side valve was opened, an alarm indicating that the MOV was in an unexpected state was sent to the console operator.” [1] These passages establish the three conservative holders and reported signal without treating the local PACO task owner as a cross-holder integrator.

The named task and the bypass-form discussion do not establish a cross-holder join. The PACO engineer “was assigned the task of opening the tower-side MOV,” which is ownership of one operational task. [1] The report says only that, **had** the bypass form been completed, “a mitigation plan would have been developed, and specific equipment tags would have been identified to watch.” [1] That counterfactual evidence of an ineffective administrative control is not affirmative evidence that no function with responsibility and authority to aggregate the PHA, valve-command, and alarm fragments was assigned. Thus the required conservative code is `unclear`, not `no`. [2]

The reconciled `sudden_label = yes` is the needed correction. The report’s “unexpected state” wording identifies the status carried by the alarm and is part of the alarm description; it does not characterize the event, relevant failure, or warning pattern as sudden or unexpected. No other applicable qualifying wording was found in the official final report. Under the stated rule, this leaves the label `unclear`, rather than `yes` or `no`.

For the date values, the source gives only “2023” for the qualifying PHA signal and identifies the incident as June 4, 2025. [1] Treating 2023 as the inclusive calendar interval gives 521 days (2023-12-31 to 2025-06-04) through 885 days (2023-01-01 to 2025-06-04). Those are precision bounds, not inferred occurrence dates.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6343 "Furnace Explosion and Fire at Shell Polymers — Investigation Report"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

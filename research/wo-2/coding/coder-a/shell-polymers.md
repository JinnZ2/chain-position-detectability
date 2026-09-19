# WO-2 Evidence Record — Shell Polymers Furnace Explosion and Fire

**Coder:** A
**Case ID:** `shell-polymers`
**Incident date:** 2025-06-04
**Official final report:** [CSB final report][1]
**Official investigation page:** [CSB investigation page][2]

## Coding decision

| Variable | Code | Basis |
| --- | --- | --- |
| `signal_present` | **yes** | Shell’s 2023 ethane-cracking-unit PHA revalidation identified the relevant explosion hazard: reverse/misdirected flow in an offline furnace when the furnace-side MOV failed to close while the tower-side MOV was open. The CSB says the scenario could cause multiple fatalities. This is a documented, pre-event, site-specific hazard signal tied directly to the ultimate mechanism: both MOVs open, cracked gas backflow, accumulation, and ignition. [1] |
| `signal_reported` | **yes** | The 2023 PHA revalidation was a formal, pre-event record. Independently, during the event sequence, an unexpected-state alarm for the furnace-side MOV was sent to and acknowledged by the console operator about five minutes before ignition; it was not merely privately known. [1] |
| `holder_count_known` | **false** | The report does not identify every person or organizational unit that held relevant information. |
| `holder_count_min` | **3** | At least three distinct documented holders existed before the explosion: (1) the **2023 PHA revalidation team**, which identified the reverse-flow explosion hazard; (2) the **PACO engineer**, who by 2:16:46 realized the furnace-side MOV had been inadvertently commanded open; and (3) the **console operator**, who received and acknowledged the unexpected-state alarm. The count treats the PHA team as one holder and does not infer additional holders. [1] |
| `join_assigned` | **unclear** | The report identifies a Production Specialist who assigned the PACO task, the PACO engineer, console operator(s), and a PHA revalidation team. It does **not** identify a role/function with both responsibility and authority to aggregate the PHA hazard, the PACO engineer’s wrong-valve awareness, and the console alarm before the explosion. Neither does it affirmatively establish that no such integration point existed. Task assignment, alarm ownership, or a PHA role alone do not meet the codebook’s responsibility-and-authority test. [1] |
| `first_signal_date` | **2023** | The report dates the earliest qualifying signal only to the **2023** PHA revalidation. It gives no more precise date. [1] |
| `lead_time_days_min` | **521** | With a year-only signal date, the shortest defensible calendar-date interval is from 2023-12-31 to 2025-06-04: 521 days. This preserves the source’s year precision rather than assigning an unsupported exact date. |
| `lead_time_max_known` | **true** | The source bounds the signal to calendar year 2023 and the event date is known. |
| `lead_time_days_max` | **885** | The longest defensible calendar-date interval within the stated year is from 2023-01-01 to 2025-06-04: 885 days. This is a precision-derived envelope, not a claim that the signal occurred on January 1. |
| `sudden_label` | **unclear** | The official report does not characterize the incident, failure, or warning pattern as “sudden,” “unexpected,” “unforeseen,” “without warning,” or a close equivalent in the codebook sense. It calls the MOV alarm an “unexpected state” alarm, but that describes the valve state/alarm rather than supplying a suddenness characterization of the incident or warning pattern. [1] |
| `pattern_result` | **indeterminate** | Signal presence, reporting, and a conservative minimum of two or more holders are supported. However, `join_assigned` is unresolved rather than affirmatively **no**. The codebook therefore requires `indeterminate`, not `supports`. |

## Decisive official evidence

The CSB’s causal determination controls the relevance assessment. It found that simultaneous opening of both isolation MOVs created a path for cracked gas to backflow into and accumulate in the firebox, where an existing flame ignited it. It further identifies ineffective administrative controls and the SIS HMI as contributors. [1]

> “In its 2023 revalidation of the ethane cracking unit process hazard analysis (PHA), Shell identified the explosion hazard in an offline furnace from misdirected/reverse flow when the furnace-side MOV failed to close while the tower-side MOV was open as an incident that could result in multiple fatalities.” [1]

This is the earliest qualifying signal because it is a pre-event, facility-specific identification of reverse flow across the MOVs leading to an explosion hazard. The report further says the PHA team identified operator response to the high-methane alarm and a start-up procedure as its two controls, both administrative; neither was in effect on the day of the incident because the alarm was suppressed and the PHA-evaluated procedure was not in use. [1] This connects the PHA signal to the operative hazard mechanism, rather than relying on a coder inference.

The report documents a second, immediate signal. At 2:14 p.m. the PACO engineer inadvertently commanded the furnace-side MOV open. The resulting alarm indicated the MOV was in an unexpected state. The console operator acknowledged it but, knowing the PACO engineer was meant to open the tower-side valve, assumed it concerned the tower-side valve and did not take corrective action. [1] The control table places this alarm approximately five minutes before ignition and says that no corrective actions were taken. [1] The timeline records that at 2:16:46 the PACO engineer realized the inadvertent command and removed it; at 2:17:50 the tower-side MOV was commanded open; and at 2:20:45 accumulated cracked gas was ignited. [1]

The report establishes the conservative three-holder lower bound without claiming a complete count. The PHA revalidation team held the 2023 hazard identification. The PACO engineer held the direct awareness of the unintended furnace-side command by 2:16:46. The console operator held the alarm signal, which was sent and acknowledged. The report also records that a Production Specialist assigned the tower-side-valve task to the PACO engineer at the morning meeting. [1]

The evidence does not, however, establish a qualifying assigned join. The CSB explains that Shell’s bypass-form policy called for a mitigation plan and identification of equipment tags to monitor when SIS protections were overridden. It found the PACO engineer was not exempt from that policy and that, had the form been completed, a mitigation plan and specific tags would have been identified. [1] This shows a missing/ineffective control in this occurrence, not a named function proven to have both the authority and responsibility to integrate every relevant cross-holder signal. Thus it cannot be recoded as `yes`; nor does it prove `no`.

## Interpretation and limitations

The 2023 PHA entry is treated as a signal because the final report itself expressly connects its reverse-flow/MOV scenario to an explosion hazard, and separately identifies the same backflow mechanism as the incident cause. It is not treated as generic background safety knowledge. The contemporaneous MOV alarm is also included because the CSB states that it indicated the furnace-side valve was in an unexpected state and describes its intended preventive role. [1]

The report gives the earliest qualifying signal only to the year. Consequently, the 521–885-day interval is a conservative calendar-date range derived from the boundaries of 2023, not a measured duration or an exact first-signal timestamp. The report does not enumerate all holders, all communications, or a definitive organization-wide integration assignment. Those omissions require `holder_count_known = false` and `join_assigned = unclear` under the codebook; they cannot be converted to a negative finding.

The report uses “unexpected state” for the MOV alarm and describes the rapid sequence, but does not apply the required suddenness characterization to the incident/failure/warning pattern. This leaves `sudden_label = unclear`, rather than treating the absence of a label as proof that the event was not sudden.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6343 "Shell Polymers Furnace Explosion and Fire: Investigation Report"

[2]: https://www.csb.gov/shell-polymers-furnace-explosion-and-fire/ "CSB Shell Polymers Furnace Explosion and Fire investigation page"

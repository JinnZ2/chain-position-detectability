# WO-2 evidence record — Dow Louisiana Operations Explosions

**Coder:** B
**Case ID:** `dow-louisiana-operations`
**Incident date:** 2023-07-14
**Official final report:** *Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations* (CSB Investigation Report No. 2023-03-I-LA). [1]

## Coding decision

| Variable | Coded value |
| --- | --- |
| `signal_present` | **yes** |
| `signal_reported` | **yes** |
| `holder_count_known` | **true** |
| `holder_count_min` | **2** |
| `join_assigned` | **no** |
| `first_signal_date` | **2020-11-20** |
| `event_date` | **2023-07-14** |
| `lead_time_days_min` | **966** |
| `lead_time_max_known` | **true** |
| `lead_time_days_max` | **966** |
| `sudden_label` | **unclear** |
| `pattern_result` | **supports** |

**Conclusion.** This case supports the WO-2 pattern under the stated coding rule. Official evidence documents pre-event, hazard-relevant signals that were recorded in organizational systems and were distributed across at least two functions. The report affirmatively describes the absence of an assigned mechanism to reconcile the vessel-specific equipment/inventory information with final closure. It also describes an unmonitored, recorded loss of nitrogen inerting that was causally relevant to the ignition mechanism. The final report does not apply a decisive “sudden,” “unexpected,” or equivalent label to the event or its warning pattern, so the suddenness field is **unclear**, not inferred from the explosion’s rapid onset.

## Incident mechanism and chronology

The CSB determined that work lights inadvertently left in the reflux drum degraded after restart. Their metal debris punctured and partially opened the product-cooler rupture disc. Ethylene oxide then entered relief piping that contained air because nitrogen inerting had been lost; it ignited, propagated to the reflux drum, and the drum catastrophically failed (printed report p. 46). [1]

The relevant pre-event chronology is as follows:

- **20 November 2020:** After rupture-disc maintenance, Dow workers pressurized the piping between the rupture disc and pressure-relief valve (PRV) with 2.4 psig nitrogen. The required closing pressure was 5 psig. Over the following two months, the pressure fell to atmospheric and at times negative gauge pressure; no nitrogen was subsequently added before the incident (printed report pp. 18, 39). [1]
- **May 2023:** The reflux drum was cleaned and inspected during a turnaround. The work order required contractor electricians to install, then remove, internal low-voltage work lights. The unit-level equipment records later showed five checked-out magnetic work lights were not returned (printed report pp. 18, 29). [1]
- **27–28 May 2023:** An inspection work coordinator certified work complete. Two Dow operators then certified a visual inspection and that the drum was free of debris, after which the manway was bolted closed (printed report pp. 30–31). [1]
- **14 July 2023:** At 6:52 p.m., a reflux pump stopped on a high-high vibration interlock. An operator found material resembling insulation at probe wiring and restarted it. CSB’s post-incident analysis found the vibration was likely caused by work-light debris moving through the unit. Operators attempted to stabilize ensuing process upsets until the explosion at approximately 9:17 p.m. (printed report pp. 20, 23). [1]

## Signal evidence

### The first documented signal: deficient relief-line nitrogen pressure

The earliest dated signal is 2020-11-20. The report states that the relief piping was pressurized with **2.4 psig** after maintenance (printed report p. 18), while the procedure required it be reduced to **5 psig** before closing (printed report p. 38). More decisively, the CSB states that process data showed the line was left at 2.4 rather than the required 5 psig, that pressure slowly declined over two months—indicating leaks—and that no operator or management official checked it in the subsequent two-plus years (printed report p. 39). [1]

> “Even when the pressure transmitter was reading negative gauge pressure, indicating the intrusion of air into the system, no alarm was set off.” — CSB, printed report p. 39. [1]

This is a pre-event measurement directly tied by the CSB to the hazard mechanism: air entered through the leaks as nitrogen was lost, and ethylene oxide then mixed with air and ignited (printed report p. 26). [1] The report’s causal conclusion is equally direct: inadequate nitrogen inerting enabled combustion and propagation to the reflux drum (printed report p. 45). [1] Accordingly, the measurement is a qualifying signal rather than an inferred warning.

### Additional recorded and observed signals

The report also supplies two independent, hazard-connected pre-event signal streams.

First, the unit’s equipment tracking contained the relevant inventory discrepancy. At the time of the incident, Dow tracked checked-out equipment and returns at the **Glycol II unit** level, though not by vessel. The CSB reports that five magnetic work lights checked out during the turnaround “were not returned” (printed report p. 29). [1] That condition was causally relevant: CSB found that at least three lights were not removed, degraded in ethylene oxide, and produced the debris that initiated the event sequence (printed report pp. 22–23). [1]

Second, the pump’s high-high vibration interlock operated on the incident night and prompted a field response. The report does not treat the operator’s initial insulation explanation as correct. Rather, it specifically concludes from post-incident analysis that debris from the work lights likely caused the vibration (printed report p. 20), and explains that debris moving through the pump likely set off the high-high vibration alarms (printed report p. 23). [1]

## Communication, holders, and the absent join

`signal_reported = yes` is based on **recording**, not on an unsupported claim that someone read and understood the hazard. The relief-line transmitter recorded pressure data, including negative values, but the data were not adequately monitored; Dow had no low-pressure alarm and did not instruct operators to check the pressure periodically (printed report pp. 26, 39). [1] Separately, Dow’s unit-level checkout/return tracking recorded the five missing lights (printed report p. 29). [1] The codebook expressly treats a signal recorded beyond private awareness as qualifying. The record therefore supports **yes**, while preserving the critical limitation that the report does not establish a pre-event human review of either record.

A conservative minimum of **two documented holder functions** is defensible:

1. The **Glycol II unit equipment-tracking function** held the checkout/return fragment: the report says Dow tracked what was checked out and returned at the unit level and records the five unreturned lights (printed report p. 29). [1]
2. The **vessel-closure functions**—the permit writer and final-closure witness/operators—held the closure/inspection fragment. The permit writer was the operator responsible for closing vessels after maintenance and signed to certify that the vessel was empty and work completed; a witness signature was also required. An inspection work coordinator certified work complete, and two operators certified the visual final inspection (printed report pp. 30–31). [1]

The count is a conservative lower bound, not a claim that only two people or units held information. The record also identifies contractor electricians as executing the work-order tasks to install and remove the lights (printed report p. 18), and a process operator responding to the vibration trip (printed report p. 20). [1]

`join_assigned = no` does **not** rest merely on the inadequacy of the visual check. The final report affirmatively says the process had no official procedure for tracking equipment put into a vessel; tracking was at unit, not vessel, level. It further says that the closure form did not make clear whether the permit writer had to confirm contractors had recovered their materials or even ask them whether they had seen anything left in the vessel. The operator consequently had no exact way to ensure that all equipment entering the vessel had left it (printed report pp. 29, 31–32). [1]

> “It was not made clear on the Vessel Closure form whether the Dow permit writer was required to confirm that contractors had gathered all their materials, or even to ask them if they had seen anything left behind in the vessel.” — CSB, printed report p. 31. [1]

The permit writer and final witness had closure and visual-attestation duties, but the report does not assign either a responsibility and authority to aggregate the cross-holder inventory, contractor, and closure information. Its affirmative description of no vessel-specific tracking or required reconciliation supports **no**, rather than treating an individual inspection duty as a qualifying assigned join. Post-incident changes reinforce the gap: Dow’s new process added defined responsibilities, tool inventory, and enhanced worker/tool/material reconciliation (printed report p. 36). [1]

## Lead time and suddenness

The first qualifying signal occurred on **2020-11-20**. The interval from that date to the incident date, **2023-07-14**, is **966 calendar days**. Because both endpoint dates are specified, this is an exact date-to-date interval; `lead_time_days_min` and `lead_time_days_max` are both 966 and `lead_time_max_known = true`. This calculation uses the initial documented 2.4-psig reading, not an imprecise estimate of when the later leak first reached zero or negative gauge pressure.

The `sudden_label` is **unclear**. CSB describes the nitrogen as having “slowly leaked out over time” (printed report p. 8) and identifies a preceding vibration trip and hours of process upsets (printed report p. 20), but it does not characterize the event, failure, or warning pattern with the codebook’s specified label set—“sudden,” “unexpected,” “unforeseen,” “without warning,” or a close equivalent. A rapid explosion does not supply that characterization by inference.

## Why the pattern result supports

All four necessary conditions for **supports** are met: the official report establishes pre-event hazard-related signals; the signals were recorded in the pressure and equipment-tracking systems; at least two distinct organizational functions held relevant fragments; and the report affirmatively documents the lack of a role/function assigned to reconcile those fragments for vessel closure. The finding does not say any individual knowingly disregarded a recognized full causal chain. The report instead shows that recorded inventory and process-condition information was not tied together through a vessel-specific aggregation and reconciliation function.

## Limitations

- The report says no operator or management official checked the relief-line pressure during the two-plus years before the incident. `signal_reported = yes` therefore rests on documented organizational recording by the transmitter and unit equipment-tracking system, not on evidence of a reviewed human warning.
- The report does not provide a complete roster of everyone who accessed the transmitter history, checkout/return log, closure form, or work order. `holder_count_min = 2` is strictly a lower bound; it is not an exact personnel count.
- The record does not treat the mere fact that closure personnel signed a form as proof that they knew the lights remained inside. It treats their inspection/closure information as a separate fragment whose required reconciliation with inventory and contractor information was unassigned.
- Although the report documents a negative-pressure trend “over the next two months,” it does not date the first negative reading. The lead-time calculation therefore uses the precisely dated 20 November 2020 below-required 2.4-psig reading. It does not claim an earlier leak date or a separate longer upper bound.
- The report does not supply an official suddenness label for the event or warning pattern. `sudden_label` is consequently **unclear**.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6316 "U.S. Chemical Safety and Hazard Investigation Board, Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations (Investigation Report No. 2023-03-I-LA, February 2026)"

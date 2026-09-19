# WO-2 coding record — U.S. Steel Clairton Plant Coke Oven Explosion

**Case ID:** `us-steel-clairton`
**Coder:** B
**Incident:** United States Steel Corporation Clairton Plant Coke Oven Explosion
**Event date:** 2025-08-11
**Official final report:** *Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works*, CSB Investigation No. 2025-03-I-PA, published August 2026.[1]

## Coding decision

| Variable | Code | Decisive basis |
| --- | --- | --- |
| `signal_present` | **yes** | The relevant pre-event signal is the established, unproceduralized practice of using high-pressure water to wash coke-oven-gas isolation-valve seats. The CSB expressly connects that practice to the causal mechanism: employees had used it for **at least three years** before the event; on August 11, water was pumped while the gates closed, producing the enclosed, pressurized volume that catastrophically failed. [1] |
| `signal_reported` | **yes** | The practice had moved beyond private awareness. It was referenced in the battery-isolation procedure, which Clairton management had approved and implemented; the CSB treats that as management knowledge and endorsement. [1] |
| `holder_count_known` | **true** |
| `holder_count_min` | **2** | A conservative lower bound is two distinct organizational holders: **U.S. Steel operating personnel**, for whom water washing had become the preferred/status-quo method, and **Clairton management**, which the CSB found knew of and endorsed the practice. This does not purport to count every individual worker. [1] |
| `join_assigned` | **no** | For the actual water-washing activity, the report provides affirmative evidence of no assigned integrating control point: no water-washing procedure or hazard analysis existed; the only Hazardous Job Meeting planned a different August 19 task and did not include washing/exercising; none of the day-of-event washing workers attended; MPW was not involved in that meeting. The CSB further found that management systems enabled a supervisor to arrange and direct the wash without prior planning, procedure, training, work permit, or sufficient hazard analysis/mitigation. A supervisor’s authority to direct work is not, on this record, an assigned function with responsibility and authority to aggregate the relevant cross-holder signals. [1] |
| `first_signal_date` | **at least 3 years before 2025-08-11** | The report gives no initiation date, but states that water washing to prepare for purges had been conducted “for at least three years before the day of the incident.” [1] |
| `lead_time_days_min` | **1096** | Three complete calendar years before August 11, 2025 reaches August 11, 2022; because the source says “at least,” 1,096 days is the conservative numeric lower bound. [1] |
| `lead_time_max_known` | **false** |
| `lead_time_days_max` | **0** | The practice may have started before the three-year lower bound. The report supplies no bounded start date, so an upper bound is open; `0` is the required placeholder rather than a substantive maximum. |
| `sudden_label` | **yes** | The CSB’s post-incident examination says the fully circumferential crack was “visually consistent with **sudden, brittle fracture**.” [1] |
| `pattern_result` | **supports** | All codebook conditions are met: a documented causal-relevant pre-event signal, communication/recording beyond private awareness, at least two holders, and affirmative evidence that the actual activity lacked an assigned integration point with the required responsibility and authority. |

## Incident mechanism and signal connection

The CSB determined that the incident resulted from overpressurizing a cast-iron, double-disc gate valve. When workers applied high-pressure water while the gates were fully or nearly fully closed, water filled the enclosure between the gates and increased internal pressure until the valve could no longer contain it. Coke oven gas then released, ignited, and exploded. The final cause determination identifies the lack of a safe valve-washing procedure and failure to identify or address the operation’s hazards as contributing causes. [1]

The selected signal is not merely a condition that preceded the event. It is the pre-existing water-washing practice that the report identifies as becoming the status quo after steam was sometimes ineffective. The CSB found that this practice was never proceduralized despite management awareness, its reference in the battery-isolation procedure, and multiple prior uses. The report also concludes that the lack of an order-of-operations procedure allowed the same practice to be performed in the manner that caused the catastrophic failure. [1]

## Chronology, communications, and organizational roles

The signal was documented over a period of at least three years before the event. On July 8, 2025, U.S. Steel separately discovered a hairline crack and coke-oven-gas leak at a downstream valve and began planning a replacement. A July 28 Hazardous Job Meeting involved nine U.S. Steel employees/supervisors and three contractors and approved isolation and purging for a planned August 19 job. That meeting did **not** include exercising, steaming, or water washing the Battery 13 isolation valve, and none of the workers who washed it on August 11 was present. [1]

On August 11, a U.S. Steel supervisor separately decided to exercise the isolation valve, arranged the MPW pump truck, and specified the equipment. During washing, the valve would not turn further while almost closed; monitors then alarmed. After the valve failed, workers smelled gas, personal monitors alarmed, workers warned others, and an evacuation call was radioed. The released gas ignited 24 seconds after that radio call. These immediate alarms are reported and consequential, but they occurred after the causal water-washing sequence was already underway and therefore are not used as the pre-event signal or lead-time anchor. [1]

The report documents a distributed but unintegrated work arrangement for the selected pre-event signal. U.S. Steel management knew of and endorsed water washing, while operating personnel had adopted it as the status quo. The August 11 supervisor initiated the specific task outside the pre-existing planning meeting. MPW had performed the practice multiple times, yet had no procedure or training and was not included in the maintenance-planning meeting. The CSB’s contractor-management analysis finds that neither organization identified or mitigated the overpressure hazard, and its conduct-of-operations analysis finds that the supervisor could arrange and direct the work without the planning, procedure, permit, training, or hazard analysis that would have created a designated integration point. [1]

## Prior information reviewed but not used to move the lead-time anchor

The report also identifies a 2003 facility-siting recommendation and a July 2010 coke-oven-gas explosion as missed opportunities to address the **facility-siting/severity** risk. They are important prior organizational-learning evidence: the 2003 PHA team recommended a facility-siting study and Clairton management rejected it; the 2010 event involved a gas release and explosion in a battery basement. [1]

Those items are not used to move this record’s earliest signal date because the CSB’s formal cause of the August 2025 event is the specific overpressure mechanism created by pressurized water trapped between the double-disc valve gates. The cited 2003/2010 evidence concerns occupied-building siting and the severity consequences of an explosion, rather than a report-established advance signal of the valve-washing/overpressure mechanism. This avoids inferring relevance beyond the final report’s causal connection. [1]

## Suddenness and limitations

The report’s “sudden, brittle fracture” language supports `sudden_label = yes`, but it characterizes the valve fracture rather than negating the three-year history of the causal work practice. [1]

The report gives only a lower-bound duration—“at least three years”—for water washing. It does not identify the first specific wash date, all individuals who knew of the practice, or an endpoint from which a finite maximum lead time can be calculated. The holder count is therefore deliberately a lower bound of two, and the maximum lead time is coded as unknown/open (`lead_time_max_known = false`, `lead_time_days_max = 0`).

The conclusion that no join was assigned is confined to the actual valve-washing operation. The report describes a Hazardous Job Meeting function for the different planned outage work, but affirmatively says that function did not cover washing/exercising and did not include the eventual work participants. This record does not treat the mere existence of the meeting, or the supervisor’s direction of the task, as evidence of a role with both assigned responsibility and authority to aggregate the relevant cross-holder signals.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6340 "U.S. Chemical Safety and Hazard Investigation Board, Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works, Investigation Report No. 2025-03-I-PA, August 2026"

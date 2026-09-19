# WO-2 evidence record — Cuisine Solutions Ammonia Release

**Case ID:** `cuisine-solutions`
**Coder:** A
**Event date:** 2024-07-31
**Official final report:** [Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility, Sterling, Virginia][1]

## Coding decision

| Variable | Coded value | Evidence-based rationale |
| --- | --- | --- |
| `signal_present` | **unclear** | The only documented pre-release process anomaly that might be a candidate signal was a Tank Farm 5 chilled-water-pump shutdown and associated high water temperatures during the afternoon. It was communicated to the refrigeration technician by radio. However, the CSB expressly states that it “could not verify” whether the water-tank bulk-temperature data were related to the Heat Exchanger 5 Surge Drum overpressure because other process data were unavailable (report p. 38). The CSB’s causal finding is that a closed or restricted outlet combined with a process upset likely initiated the release, but that the specific cause of the upset could not be determined (p. 40). The report therefore does not connect the earlier pump/temperature event to the identified hazard mechanism strongly enough to code a case-specific, directionally related signal as present. It also does not affirmatively establish that none existed. |
| `signal_reported` | **unclear** | The candidate anomaly was communicated: the refrigeration technician received a radio call between approximately 5:00 and 5:30 p.m. that all three Tank Farm 5 water pumps had shut down (p. 26). But its relevance to the later overpressure is unresolved by the CSB; therefore this does not establish that a *qualifying relevant signal* was reported under the codebook. |
| `holder_count_known` | **false** | Because no qualifying relevant pre-event signal is established, the report cannot support a known count of its holders. |
| `holder_count_min` | **0** | No defensible minimum of holders of a qualifying relevant signal can be established. The WO-2 codebook ordinarily permits `null` in this circumstance; the task result schema requires an integer, so `0` is used as the schema-compatible representation of **no defensible qualifying-holder lower bound**, not as an affirmative finding that no person held information. |
| `join_assigned` | **unclear** | The report identifies the refrigeration technician as responsible for the refrigeration system and reporting to the refrigeration manager (p. 13), and the written Emergency Action Plan assigned maintenance to investigate an alleged release and inform the plant or production manager (p. 71). It does not identify a role with both authority and responsibility to aggregate *relevant cross-holder pre-event signals* concerning the ultimately indeterminate process upset, liquid/two-phase relief, and discharge consequences. The record also does not affirmatively establish that no such integration point existed. |
| `first_signal_date` | **unknown** | No documented observation is officially connected to the causal hazard mechanism as a qualifying pre-event signal. The candidate chilled-water event occurred on 2024-07-31, but the CSB could not verify its relation to the overpressure (p. 38). |
| `lead_time_days_min` | **0** | No numeric lower bound from an earliest qualifying signal can be defended. The candidate condition is not established as relevant. This 0 follows the task instruction for an undefendable numeric lower bound; it does not mean the event lacked lead time. |
| `lead_time_max_known` | **false** | No bounded interval from an earliest qualifying signal is established. |
| `lead_time_days_max` | **0** | The upper bound is open/unknown because the first qualifying signal is unknown. This 0 is the schema-required numerical representation of an unquantifiable maximum, per task instruction. |
| `sudden_label` | **unclear** | The report does not characterize the incident, its failure, or its warning pattern as “sudden,” “unexpected,” “unforeseen,” or “without warning.” Its use of “sudden” is limited to a potential *pressure drop when the relief valve opened* (finding 8, p. 84), not a qualifying characterization of the incident or warning pattern. Absence of an official characterization is coded unclear rather than no. |
| `pattern_result` | **indeterminate** | The necessary elements are unresolved: `signal_present` and `signal_reported` are both unclear, and no qualifying-holder minimum or assigned integration function can be established. Accordingly, the conditions for either `supports` or `does_not_support` are not met. |

## Incident chronology and causal analysis

At approximately 5:00–5:30 p.m. on July 31, 2024, a radio caller reported that all three Tank Farm 5 chilled-water pumps were shut down. The refrigeration technician found the outdoor electrical cabinet hot, was initially unable to reset the pumps, and restarted them at approximately 6:14 p.m. After 8:00 p.m., the technician received a further radio call about chilled-water temperature. At approximately 8:17 p.m., the technician observed normal ammonia pressures and stable, normal liquid levels in the surge-drum sight glasses, radioed that “everything looks good on our end,” and left at approximately 8:19 p.m. [1]

At approximately 8:20 p.m., an overpressure in the Heat Exchanger 5 Surge Drum caused its emergency pressure relief valve to open. The release contained a significant liquid component and rapidly reached ground level. The CSB found the relief valve operated as designed; its likely-out-of-date replacement or testing status was not causal. [1] The controlling technical finding is that a closed or restricted surge-drum outlet combined with a process upset likely initiated the event, while the specific cause of the upset remained undetermined because process data were unavailable. [1]

This uncertainty controls the signal coding. The official report identifies available water-temperature fluctuations and high water temperatures on the afternoon before the incident, but says the CSB “could not verify whether the water tank bulk temperature data were related to the Heat Exchanger 5 Surge Drum overpressure in the absence of any other process data.” It further records that alarm history was lost and concludes that the lack of historical process and alarm data prevented determination of the specific cause. [1] Under the codebook, proximity in time and a possible mechanism are insufficient without this official connection.

## Decisive official evidence

> “The data indicated some water tank temperature fluctuations and high water temperatures on the afternoon before the incident, but this began hours before the incident occurred, and the CSB could not verify whether the water tank bulk temperature data were related to the Heat Exchanger 5 Surge Drum overpressure in the absence of any other process data.” — CSB report p. 38 [1]

> “The CSB concludes that the ammonia release resulted from an overpressure event, and that a closed or restricted outlet on the Heat Exchanger 5 Surge Drum, combined with a process upset, likely initiated the event. Without process data available for analysis, however, the specific cause of the process upset could not be determined.” — CSB report p. 40 [1]

> “On the afternoon of July 31, 2024, approximately between 5:00 p.m. and 5:30 p.m., the second shift refrigeration technician received a radio call indicating that all three of the water pumps in Tank Farm 5 supplying chilled water to the sous vide process were shut down.” — CSB report p. 26 [1]

> “The refrigeration technician later told the CSB that, at that time, the ammonia pressures were in the normal operating range. Additionally, all the surge drum sight glasses indicated a stable, normal level of liquid ammonia, and the refrigeration equipment appeared to be working correctly.” — approximately 8:17 p.m., CSB report p. 26 [1]

> “The refrigeration technician was responsible for the refrigeration system, including the Tank Farms, Compressor Room, and Refrigeration Control Room… The refrigeration technician reported to the refrigeration manager.” — CSB report p. 13 [1]

> “Maintenance will ‘investigate the alleged release.’” and “Maintenance will inform the plant or production manager whether the release is classified as small or large.” — written Emergency Action Plan, CSB report p. 71 [1]

> “Without more extensive refrigeration system process data in a process data historian, the Sterling plant could experience an undetected process upset, similar to the events leading up to the incident.” — CSB finding 18, report p. 85 [1]

## Limitations

The final report does document a same-day process anomaly and its radio communication, but expressly withholds causal linkage to the overpressure. The report’s conclusion that the specific process-upset cause could not be determined bars treating that anomaly as a qualifying signal by inference.

The report describes individual operational responsibilities and release-response assignments. It does not establish a pre-event role or function with both authority and responsibility to aggregate the unresolved, potentially relevant fragments into a decision about the eventual hazard mechanism. The `join_assigned` value is therefore unclear rather than no.

The report gives approximate times for the candidate pump anomaly and event, but these cannot supply lead time because the candidate does not meet the documented-relevance threshold. Both numerical lead-time fields use 0 only under the task’s required convention for no defensible numeric bound; neither 0 represents a factual zero-day finding.

The report does not apply a qualifying official suddenness label to the event or warning pattern. It uses “sudden” only for a proposed pressure-drop mechanism after relief-valve opening; missing characterization is not evidence of “no.”

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6304 "Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility, Sterling, Virginia — CSB Investigation Report (September 2025)"

[2]: https://www.csb.gov/cuisine-solutions-ammonia-release-/ "Cuisine Solutions Ammonia Release — CSB investigation page"

[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-2-quiet-failure-missing-aggregation.md "WO-2 pilot codebook"

# WO-2 evidence record — Cuisine Solutions Ammonia Release

**Coder:** B
**Case ID:** `cuisine-solutions`
**Incident date:** 2024-07-31
**Official final report:** *Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility, Sterling, Virginia* (CSB Investigation Report No. 2024-03-I-VA; published September 2025) [1]

## Coded result

| Variable | Value | Evidence-based rationale |
| --- | --- | --- |
| `signal_present` | **unclear** | The only documented pre-release operating abnormality that could potentially bear on the initiating upset was the Tank Farm 5 chilled-water-pump shutdown and associated water-temperature fluctuation. The CSB expressly found it **could not verify** whether that available water-temperature information was related to the Heat Exchanger 5 Surge Drum overpressure, because other process data were absent. Under the codebook, this prevents treating it as a confirmed hazard-mechanism signal. The report identifies the initiating mechanism only at the level of a likely restricted/closed surge-drum outlet plus an unspecified process upset. [1] |
| `signal_reported` | **unclear** | A radio call communicated the pump shutdown to the refrigeration technician. However, because the report does not connect that abnormality to the initiating mechanism, it is not a confirmed qualifying signal for this variable. The report does not document another pre-event, mechanism-linked signal that was communicated or recorded. [1] |
| `holder_count_known` | **false** | No qualifying mechanism-linked signal can be established, so the report does not establish a count of holders of relevant fragments. The radio-call participants and refrigeration technician cannot be counted as holders of a qualifying signal without inferring the relevance that the CSB says it could not verify. |
| `holder_count_min` | **0** | Zero is used as the schema-compatible conservative value where the source cannot establish even one holder of a **qualifying** signal; it does not mean that no person observed the pump problem. |
| `join_assigned` | **unclear** | The report identifies the refrigeration technician as responsible for the refrigeration system and provides an emergency-plan escalation path from maintenance to the plant or production manager. It does not identify a role/function that both had authority and responsibility to aggregate relevant cross-holder signals for the unidentified initiating process upset. Neither a single equipment responsibility nor the emergency-evacuation decision pathway meets the codebook’s integration-point test. [1] |
| `first_signal_date` | **unknown** | No earliest qualifying signal date is defensible. The potential pump abnormality occurred on 2024-07-31, but its relationship to the overpressure is explicitly unverified. |
| `lead_time_days_min` | **0** | No numeric lower-bound lead time can be defended without first treating the unverified pump/water-temperature abnormality as a qualifying signal. |
| `lead_time_max_known` | **false** | The source provides no bounded interval from a qualifying signal to the event. |
| `lead_time_days_max` | **0** | Required zero placeholder for an open/unknown maximum; it does not state a zero-day maximum. |
| `sudden_label` | **yes** | In its technical finding, the CSB describes a possible liquid-carryover mechanism as involving “a high liquid level and a **sudden pressure drop** when the emergency pressure relief valve opened.” This is an official suddenness characterization of the failure sequence, though the specific initiating upset remains undetermined. [1] |
| `pattern_result` | **indeterminate** | The required positive elements are unresolved: a qualifying pre-event signal is not established, reporting of such a signal is consequently unresolved, no minimum holder count is established, and no qualifying cross-holder integration assignment is identified. This is not a finding that the event had no warnings. |

## Decisive official evidence

### Causal analysis and data limit

The report’s causal finding is that the release resulted from overpressure, and that “a closed or restricted outlet on the Heat Exchanger 5 Surge Drum, combined with a process upset, likely initiated the event.” It immediately limits the conclusion: “Without process data available for analysis, however, the specific cause of the process upset could not be determined.” [1]

The CSB explains the missing connection directly. Cuisine Solutions “did not record historical process data” for the refrigeration system other than food-safety temperatures. The available Tank Farm 5 water-tank data showed “some water tank temperature fluctuations and high water temperatures on the afternoon before the incident,” but the CSB “could not verify whether the water tank bulk temperature data were related to the Heat Exchanger 5 Surge Drum overpressure in the absence of any other process data.” The HMI alarm record was also lost. [1] This is decisive against coding the earlier water/pump condition as `signal_present=yes`; temporal precedence alone cannot supply the missing causal connection.

The CSB further concludes that a process-data historian was absent and that, without it, a similar process upset could remain undetected until another overpressure. The report describes this as a performance-monitoring and repeat-incident problem, not evidence that a particular pre-event warning of this event was detected. [1]

### Chronology of the potential—but unverified—abnormality

Between approximately **5:00 and 5:30 p.m.** on July 31, the second-shift refrigeration technician received a **radio call** that all three Tank Farm 5 chilled-water pumps were shut down. The technician found the electrical cabinet hot, and the pumps restarted and continued operating at approximately **6:14 p.m.** [1]

After 8:00 p.m., a further radio call reported an issue with Tank Farm 5 chilled-water temperature. At about **8:17 p.m.**, the technician inspected the refrigeration loop and later stated that ammonia pressures were normal, surge-drum sight glasses showed stable normal liquid levels, and the equipment appeared to be working correctly; the technician left for a meal break at approximately **8:19 p.m.** [1] The emergency relief valve discharged at approximately **8:20 p.m.** [1]

Thus, the chronology documents observations and communications before the event, but the final report does not establish that those observations signaled the event’s actual initiating mechanism.

### Roles, communications, and why they do not establish a qualifying join

The organizational description assigns the refrigeration technician responsibility for the refrigeration system, including Tank Farms, compressor room, and control room. It states that maintenance commonly collaborated with that technician and that a maintenance technician served as backup during meal breaks; the refrigeration technician reported to the refrigeration manager. [1] This establishes operational roles, but not a named function with authority and responsibility to aggregate cross-holder, mechanism-linked evidence about the unidentified process upset.

The Emergency Action Plan (EAP) directed a person noticing a suspected chemical release to alert a supervisor or maintenance; maintenance was to investigate and inform the plant or production manager whether the release was small or large; and the plant or production manager would decide whether to evacuate. [1] That is a response/escalation procedure for an identified release, not an assigned function to consolidate relevant fragments about the unobserved pre-release upset. It therefore cannot support `join_assigned=yes`.

The report also documents a Tank Farm 5 common-relief-header sensor and HMI alarm, but it sounded only after the incident began, when no one was in the control room. The CSB found no planned corrective action—automatic or procedural—in response to it, and concluded that it was “of no value during the incident.” [1] This is post-onset evidence and is not a pre-event signal.

### Related but non-credited pre-existing safety conditions

The report identifies inadequate emergency preparedness and the lack of an automated shutdown as contributors to severity. It finds that no one onsite was assigned or trained to activate the system-wide emergency shutdown buttons, and that early use could have reduced severity. [1] These are established pre-existing control deficiencies, but this record does not recode them as a confirmed pre-event **signal** of the initiating overpressure: the report’s upstream process upset remains unspecified, and the codebook requires an official source connection rather than inference.

Likewise, the report says relief valves were likely two years overdue for replacement or testing, but all tested valves functioned as designed and the CSB expressly finds that failure to test or replace them on time was **not causal**. This condition is therefore not credited as a mechanism-related signal. [1]

## Limitations and uncertainty handling

1. The final report could not determine the specific cause of the process upset because historical process data and alarm history were unavailable. The relevant causal link for the documented pump/water-temperature abnormality is therefore unresolved, rather than negative.
2. The report documents a pre-event radio communication and several named operational roles, but it does not establish a qualifying signal or a role empowered to aggregate cross-holder evidence about the unknown initiating upset. Accordingly, neither communication nor role evidence is stretched into `yes` values.
3. The report documents known design, planning, alarm, and emergency-shutdown deficiencies that contributed to the release consequences. Those conditions are important causal and organizational evidence but do not, without an official connection to a precursor of the initiating overpressure, establish the codebook’s case-specific pre-event signal.
4. The potential abnormality was observed on the event date, but no lead-time number is assigned because its relevance is explicitly unverified. The lead-time zeros are required unknown-value placeholders, not estimates of an actual zero-day interval.
5. The `sudden_label=yes` value relies narrowly on the CSB’s phrase “sudden pressure drop,” not on an assertion that the entire incident was unforeseeable or lacked warning.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6304 "U.S. Chemical Safety and Hazard Investigation Board, Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility, Investigation Report No. 2024-03-I-VA (September 2025)"

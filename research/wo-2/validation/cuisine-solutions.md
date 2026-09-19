# WO-2 validation record — Cuisine Solutions Ammonia Release

**Case ID:** `cuisine-solutions`
**Validation verdict:** **Needs correction**
**Validator review:** Official CSB final report opened and read (102 PDF pages; printed report pp. 1–92), together with the WO-2 codebook, manifest, both independent coder records, reconciliation log, and pilot analysis.

## Corrected final coding

| Variable | Validated value | Status / basis |
| --- | --- | --- |
| `signal_present` | **unclear** | The reported Tank Farm 5 chilled-water-pump shutdown/high water-temperature condition is a potential precursor, but CSB expressly could not verify its relationship to the Heat Exchanger 5 Surge Drum overpressure. The report identifies the initiating pathway only as a restricted/closed outlet plus a process upset whose specific cause it could not determine. This precludes `yes`; it does not affirmatively establish `no`. |
| `signal_reported` | **unclear** | The pump condition was radioed to the refrigeration technician, but the report does not establish it as a qualifying, mechanism-linked signal. |
| `holder_count_min` | **0** | **Placeholder only**: no lower bound for holders of a qualifying signal is quantifiable. `holder_count_established = false`; zero is not an affirmative finding of zero holders. |
| `join_assigned` | **unclear** | The report identifies operational and post-release response ownership, not a responsibility-and-authority assignment to aggregate qualifying cross-holder pre-event fragments on the initiating-overpressure pathway. It also does not affirmatively prove that such a pre-event integration point was absent. |
| `first_signal_date` | **unknown** | No qualifying signal is established. The same-day pump condition cannot supply the date because CSB did not connect it to the initiating hazard pathway. |
| `lead_time_days_min` | **0** | **Placeholder only**: unquantifiable because the earliest qualifying signal is unknown. |
| `lead_time_max_known` | **false** | No bounded interval is supported. |
| `lead_time_days_max` | **0** | **Placeholder only**: the maximum is unquantifiable, not factually zero. |
| `sudden_label` | **unclear** | **Corrected from reconciled `yes`.** The report does not characterize the event, the initiating failure, or a warning pattern as sudden, unexpected, unforeseen, or without warning. Its “sudden pressure drop” is a possible downstream physical mechanism for liquid carryover after the relief valve opened; the report says that valve functioned as designed. It is not a qualifying label of the incident, a relevant failure, or a warning pattern under the required strict rule. |
| `pattern_result` | **indeterminate** | `signal_present`, `signal_reported`, and the relevant holder count remain unresolved; the codebook therefore requires `indeterminate`. |

## Coherence check: one pathway, no splicing

The appropriate pathway for signal-based coding is the **initiating overpressure pathway**: a closed or restricted Heat Exchanger 5 Surge Drum outlet combined with a process upset. The only documented pre-event candidate is the chilled-water-pump/water-temperature episode, but CSB did not verify that it belonged to that pathway. It cannot be joined with separate, downstream **release-consequence and emergency-response** material—the liquid-aerosol discharge, post-onset common-header alarm, evacuation communications, emergency-shutdown training, or Emergency Action Plan—to manufacture a signal, holder count, or missing join.

Accordingly, the validated record is **pathway-consistent**: it retains uncertainty rather than combining fragments from unrelated causal pathways. The named refrigeration technician and the EAP’s maintenance/plant-manager sequence do not establish a cross-holder join. Conversely, the absence of a system-wide shutdown procedure pertains response/severity, and is not affirmative evidence that no integration function existed for the unresolved initiating upset.

## Decisive evidence from the official final report

> “On the afternoon of July 31, 2024, approximately between 5:00 p.m. and 5:30 p.m., the second shift refrigeration technician received a radio call indicating that all three of the water pumps in Tank Farm 5 supplying chilled water to the sous vide process were shut down.” — **printed p. 26** [1]

> “The data indicated some water tank temperature fluctuations and high water temperatures on the afternoon before the incident, but this began hours before the incident occurred, and the CSB could not verify whether the water tank bulk temperature data were related to the Heat Exchanger 5 Surge Drum overpressure in the absence of any other process data.” — **printed p. 38** [1]

> “The CSB concludes that the ammonia release resulted from an overpressure event, and that a closed or restricted outlet on the Heat Exchanger 5 Surge Drum, combined with a process upset, likely initiated the event. Without process data available for analysis, however, the specific cause of the process upset could not be determined.” — **printed p. 40; finding 3, p. 84** [1]

> “The refrigeration technician was responsible for the refrigeration system, including the Tank Farms, Compressor Room, and Refrigeration Control Room… The refrigeration technician reported to the refrigeration manager.” — **printed p. 13** [1]

> “Maintenance will ‘investigate the alleged release.’” and “Maintenance will inform the plant or production manager whether the release is classified as small or large.” — EAP, **printed p. 71** [1]

These are assignments for local equipment responsibility or an already-suspected-release response. They do not show a named role/function with both authority and responsibility to combine relevant, cross-holder **pre-event** fragments on the initiating-overpressure pathway.

> “The CSB concludes that although the Tank Farm 5 emergency pressure relief valves were likely beyond the 5-year replacement or testing frequency, failure to test or replace them on time was not causal to the incident.” — **printed p. 36; finding 1, p. 84** [1]

> “On the night of the incident, the ammonia release contained liquid aerosol from the Heat Exchanger 5 Surge Drum likely due to either (1) overfilling with boiling liquid, (2) liquid carryover caused by a high liquid level and a **sudden pressure drop when the emergency pressure relief valve opened**, or (3) insufficient vapor space for liquid disengagement, or a combination of these factors.” — **printed p. 50; finding 8, p. 84** [1]

The last quotation does not qualify the sudden-label field. It describes one possible physical submechanism after relief-valve opening, not the incident, initiating failure, or warning pattern. The report separately finds the relief valve “functioned as designed and intended” (**printed p. 36; finding 2, p. 84**) [1]. Other terms such as “rapidly slumping ammonia cloud” describe physical motion/consequence, not a qualifying suddenness characterization.

## Validation against reconciliation and analysis

The reconciliation and pilot analysis correctly retained `unclear` for signal presence/reporting, `unclear` for join assignment, `unknown` for first signal, unquantifiable holder/lead-time numbers, and `indeterminate` for the pattern. Their reported `sudden_label = yes` is **not supported after applying the specified strict applicability rule**, and is corrected to `unclear`. The prior cross-pathway caution is otherwise sound.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6304 "Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility — CSB Investigation Report No. 2024-03-I-VA, September 2025"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

# WO-2 validation record — Bio-Lab Conyers

## Verdict

**Valid.** I opened and read the CSB final report. The reconciled values are supported by one coherent, report-identified hazard pathway: chlorinated-isocyanurate storage created a corrosive environment; corrosion damaged the Plant 12 fire-protection system; failures and leaks created the known water-contact hazard; and a corroded sprinkler component ultimately failed, allowing water to contact the stored chemicals and initiate decomposition and fire. The record does not combine the Lake Charles decomposition history, a generic inventory decision, or an incident-time alarm with this pathway.

| Field | Validated value |
| --- | --- |
| `signal_present` | `yes` |
| `signal_reported` | `yes` |
| `holder_count_min` | `3` |
| `holder_count_established` | `false` |
| `join_assigned` | `unclear` |
| `first_signal_date` | `2019-12-30` |
| `event_date` | `2024-09-29` |
| `lead_time_days_min` | `1735` |
| `lead_time_max_known` | `true` |
| `lead_time_days_max` | `1735` |
| `sudden_label` | `no` |
| `pattern_result` | `indeterminate` |

No numeric placeholder is used. The date pair is exact at calendar-day precision, so both lead-time endpoints are quantifiable.

## Coherent pathway and evidence

The report identifies the causal mechanism directly:

> “The CSB determined that the cause of the incident was a corroded sprinkler system component that failed, allowing water to contact the stored pool-treatment chemicals (chlorinated isocyanurates) inside the warehouse, initiating a decomposition reaction and generating significant amounts of dense toxic smoke and heat that started fires.” — printed report p. 124 [2]

The selected earliest signal is part of that same pathway, not merely a general chemical-history signal. The report states:

> “Such premature corrosion resulted in the first sprinkler system component failure at the warehouse on December 30, 2019, when bolts on the fire water piping corroded through.” — printed report p. 61 [2]

It then connects the repeated corrosion, failure, and water-contact risk to the eventual event:

> “The leaking water posed a known risk of contact with stored chlorinated isocyanurates, which was known to lead to decomposition reactions and product off-gassing.” — printed report p. 78 [2]

Accordingly, `signal_present = yes`, `first_signal_date = 2019-12-30`, and the exact interval to 2024-09-29 is 1,735 days. Because both endpoints are exact dates, the minimum and maximum are both 1,735 days.

Reporting and the three-holder minimum also concern this corrosion-to-water-contact pathway. Annual inspection reports documented the corrosion:

> “Corroded sprinkler heads were documented by the Bio-Lab Conyers fire protection contractor as deficiencies in both the 2021 and 2022 Annual Sprinkler Inspection reports.” — printed report p. 63 [2]

The relevant risk-assessment reports then reached three distinct role-level holder categories:

> “Evidence of widespread corrosion in multiple buildings at Bio-Lab Conyers was not only known to plant-level management but was directly addressed to KIK corporate employees at the vice president and manager level in annual insurance risk assessment reports.” — printed report p. 93 [2]

This supports `signal_reported = yes` and a conservative `holder_count_min = 3`: plant-level management, corporate vice-president-level employees, and corporate manager-level employees. It does not enumerate every holder, so the companion established/known boolean remains `false`.

The named local EHS responsibility does not establish a qualifying cross-holder join, and a failure to follow a procedure does not prove that no such join existed. The report says:

> “Although local Bio-Lab Conyers EHS on-site was responsible for implementation, they should also have communicated the hazards and risks associated with frequent fire protection impairments to its corporate KIK leadership.” — printed report p. 97 [2]

That identifies a local implementation and communication responsibility. It does not identify a named role or function with both responsibility and authority to aggregate the inspection-report, insurer-report, plant-management, and corporate-holder fragments and act on their combined risk. Conversely, the report does not affirmatively establish that no such integration point was assigned. Under the codebook, `join_assigned = unclear`, not `yes` or `no`.[1]

The `sudden_label = no` is supported by the report’s affirmative characterization of the relevant warning pattern, rather than by mere absence of the word “sudden” or by the unrelated “sudden focus” on inventory reduction. The CSB’s case-specific safety issue states:

> “Warning signs related to asset integrity include run to failure (RTF), corrosion, and frequent leaks—all of which have been observed at Bio-Lab Conyers.” — printed report p. 78 [2]

It further concludes:

> “The CSB also concludes that had Bio-Lab Conyers taken steps to proactively prevent sprinkler system leaks instead of allowing the system to run to failure, the incident likely would not have occurred.” — printed report p. 81 [2]

Those passages affirmatively characterize the relevant warning pattern as observed corrosion, frequent leaks, and run-to-failure. They support the negative label; no positive sudden/unexpected wording applicable to the event, relevant failure, or warning pattern was used.

## Classification

The case meets the first three necessary pattern conditions: an on-pathway pre-event signal was present, it was reported, and at least three distinct role-level holders are documented. The fourth condition is unresolved because the report does not affirmatively establish an absent responsibility-and-authority aggregation function. Therefore, `pattern_result = indeterminate` rather than `supports`.[1]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

[2]: https://www.csb.gov/file.aspx?DocumentId=6339 "Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility — CSB Investigation Report No. 2024-04-I-GA"

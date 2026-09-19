# Coder A evidence record — Bio-Lab Inc. Conyers Fire and Chemical Release

## Coding determination

This record codes the September 29, 2024 Bio-Lab Conyers incident from the CSB’s official final report only. The CSB identifies the initiating mechanism as failure of a **corroded sprinkler component**, which let water contact stored chlorinated isocyanurates, initiated decomposition, and started the fires. That controlling causal finding is the test for signal relevance in this record.[1]

| Field | Coder A value |
| --- | --- |
| Case ID | `bio-lab-conyers` |
| Event date | `2024-09-29` |
| Official final report | [CSB, *Bio-Lab Inc. Conyers Fire and Chemical Release*][1] |
| `signal_present` | **yes** |
| `signal_reported` | **yes** |
| `holder_count_known` | **false** |
| `holder_count_min` | **3** |
| `join_assigned` | **unclear** |
| `first_signal_date` | **2020-08-27** |
| `lead_time_days_min` | **1494** |
| `lead_time_max_known` | **true** |
| `lead_time_days_max` | **1494** |
| `sudden_label` | **unclear** |
| `pattern_result` | **indeterminate** |

## Decisive evidence and coding rationale

### Hazard mechanism used to assess relevance

The CSB’s cause statement says that a corroded sprinkler component failed, allowing water to contact the stored chlorinated isocyanurates and initiating a decomposition reaction; the corrosion resulted from the corrosive environment in the building and was not proactively addressed.[1] The report also formally finds that corroded heads outside the bunker failed, water leaked onto oxidizer super sacks, and the result was off-gassing, decomposition, and fires.[1] Thus, prior water-contact decomposition events and documented sprinkler corrosion/impairments are directionally related to the official mechanism rather than merely temporally prior background facts.

### `signal_present = yes` and `first_signal_date = 2020-08-27`

The earliest documented signal included here is the exact-date, company-level experience at Bio-Lab Lake Charles. On **August 27, 2020**, rainwater contacted TCCA-based formulation material, initiating a chemical reaction and decomposition that led to a fire destroying the building; another decomposition and release occurred later that day in a warehouse storing the same type of formulation.[1] This is a documented precursor involving water contact with TCCA-based pool-treatment material. Its relevance is not inferred solely from chemical similarity: the Conyers report expressly says KIK failed to identify the potential for water contacting its chlorinated-isocyanurate materials to cause a major building fire loss despite the Lake Charles 2020 experience.[1]

The report also documents a nearer, same-site confirmation of that hazard. On September 14, 2020, a leaking water line flooded Plant 6 at Bio-Lab Conyers; floodwater contacted TCCA-based formulation material and caused a decomposition event. Material relocated after that event decomposed again on September 18, 2020.[1] Later signals directly implicated the eventual initiating pathway: substantial corrosion was documented at the 2021, 2022, and 2023 annual sprinkler inspections; a pipe-hole repair occurred July 16–17, 2024; and several leaking heads and corroded-head replacements were reported in September 2024.[1] The CSB concludes that repeated reactive replacement of corroded sprinkler equipment ultimately led to the September 29 incident.[1]

### `signal_reported = yes`

The relevant corrosion findings were communicated beyond a private holder. The CSB states that evidence of widespread corrosion in multiple Conyers buildings was known to plant-level management and was **directly addressed** to KIK corporate employees at the vice-president and manager levels in annual insurer risk-assessment reports.[1] This is explicit pre-event reporting of a causal-pathway signal.

The report also establishes pre-event corporate visibility for incident signals. KIK’s software system held incident details and associated investigation records; two November 2023 super-sack off-gassing events, one involving a wooden-pallet fire, remained open in that system until the 2024 incident, and the CSB states that the entries “would have had visibility within the software system at the KIK corporate level.”[1] These events reinforce that signals about decomposition hazards were recorded and communicated.

### `holder_count_known = false`; `holder_count_min = 3`

The total number of relevant holders cannot be counted from the report, so the count is not known. A conservative minimum of three distinct role-level holders is documented for the corrosion signal: **plant-level management**, **KIK corporate vice-president-level employees**, and **KIK corporate manager-level employees**. The report differentiates those three recipient categories when stating who knew or received the annual insurer risk-assessment reports.[1] This count does not add unnamed individual employees, the insurer/risk assessor, fire-watch personnel, or other site functions, even though the report suggests additional possible holders.

### `join_assigned = unclear`

The report documents corporate procedures and reporting channels but does **not** identify a named role or function that is expressly assigned both responsibility and authority to aggregate the cross-holder signals used here—prior water-contact decomposition incidents, insurance corrosion findings, impairment records, and incident-system records—and to act on their combined risk before the event. Therefore, the strict threshold for `yes` is not met. It is also not affirmative evidence that no integration point existed, so `no` is not supported.

The ambiguity is material. Local Conyers EHS was responsible for implementing the fire-impairment procedure and was expected to communicate hazards and risks from frequent impairments to corporate KIK leadership.[1] KIK had procedures for documenting and tracking fire impairments and off-gassing incidents that could have enabled organization-wide understanding, but CSB found that KIK failed to fully implement and enforce them.[1] The report says corporate risk-assessment reports reached vice-president and manager levels, but it does not specify that either title had a mandate and authority to integrate all the above cross-holder signal streams. Existing visibility, procedures, and generic corporate oversight are consequently insufficient to code `join_assigned = yes` under the codebook.

### Lead time

The earliest qualifying signal is dated exactly **2020-08-27**, and the event date is exactly **2024-09-29**. The calendar interval is **1,494 days**. Because both endpoints are exact dates, this is both the defensible minimum and maximum: `lead_time_days_min = 1494`, `lead_time_max_known = true`, and `lead_time_days_max = 1494`. The calculation preserves day precision and does not infer a time-of-day interval.[1] [1]

### `sudden_label = unclear`

I found no official characterization in the final report that labels the incident, its failure, or its warning pattern “sudden,” “unexpected,” “unforeseen,” “without warning,” or a close equivalent. Absence of such phrasing is not affirmative evidence that the official material characterized it as non-sudden. Under the codebook’s missing-evidence rule, this is coded **unclear**, not `no`.

### `pattern_result = indeterminate`

The incident meets three necessary components: `signal_present = yes`, `signal_reported = yes`, and `holder_count_min = 3` (at least two). However, `join_assigned` remains unresolved rather than affirmatively `no`. The required condition for `supports` is therefore not established, and there is no affirmative evidence that a necessary element is false. The result is **indeterminate**.

## Limitations

The official report supports multiple relevant pre-event signals, but it does not enumerate every recipient of the annual reports, every user of the incident system, or every person who knew of the prior incidents. The holder count is therefore a conservative role-level minimum rather than a population count.

The report establishes communication, corporate procedures, and shortcomings in their implementation. It does not expressly assign a single role/function both the responsibility and authority to combine every relevant signal stream before the event. That evidentiary gap controls the `join_assigned = unclear` and `pattern_result = indeterminate` decisions.

The earliest qualifying date is a water-contact TCCA incident at another Bio-Lab facility, not a signal recorded in Plant 12 itself. It is included because the final report explicitly connects Lake Charles 2020 to KIK’s missed recognition of water-contact fire risk and to the corporate, cross-facility implementation failure. The report does not provide a qualifying “sudden” label; that absence is handled as uncertainty rather than a negative claim.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6339 "U.S. Chemical Safety and Hazard Investigation Board, Bio-Lab Inc. Conyers Fire and Chemical Release: Investigation Report No. 2024-04-I-GA"

# WO-2 independent validation — `pemex-deer-park`

**Verdict:** **Needs correction.** The reconciled record mixes the positive-equipment-identification pathway with permit hold-point, contractor-handoff, and SIMOPs/surrounding-unit pathways to infer `join_assigned = no`. Under the codebook and the additional coherence rule, the case is **indeterminate**, not supporting.

## Official report reviewed

The complete official CSB final report was opened and read: *Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery*, Investigation Report No. 2024-05-I-TX, February 2026 [1]. Printed and PDF page citations below are the report’s numbered pages.

## Coherent pathway selected

All values below concern one report-identified **positive-equipment-identification / wrong-equipment-opening pathway**:

> “The CSB determined that the cause of the incident was the opening of incorrect equipment, which released pressurized hydrogen sulfide. PEMEX Deer Park did not establish an effective method to clearly identify the correct equipment to open before authorizing opening the equipment.” [1]

The selected earliest signal is the **October 8, 2024 defective positive-identification job package and tagging condition** for Blind 407—not an undated generic Run-and-Maintain system condition. The report states: “On October 8” an operator developed the required blind list and drawing; for Blind 407, “Instead of hanging the blind tag directly on the blind, the PEMEX Deer Park operators hung the blind tag on a nearby railing.” [1] The CSB later found the job aids insufficient and the tag system uncontrolled: “PEMEX Deer Park’s job aids—a written list and a process sketch—were insufficient in directing the Repcon workers to the intended pipe opening location” [1], and the “inconsistent and uncontrolled blind tag identification system ... did not give a clear indication of what equipment was to be opened.” [1]

This pathway is distinct from (a) the permit’s undefined operator-presence hold point, (b) failure to tell boilermakers that the Amine Unit was active, and (c) SIMOPs evaluation of hazards to the neighboring Sulfur Unit. Those are report findings, but they cannot be combined with the selected identification signal merely to create an absent cross-holder join.

## Corrected coding record

| Variable | Corrected value | Validation basis |
|---|---:|---|
| `signal_present` | **yes** | The dated defective job aids/tagging condition was a documented pre-event defect directly related to the report’s wrong-equipment mechanism. [1] |
| `signal_reported` | **yes** | The same previously developed job aids were communicated: “The PEMEX Deer Park operator provided the previously developed blind list and drawing to the Repcon day shift foreman.” [1] This is a record/transfer beyond one holder within the identification pathway. |
| `holder_count_min` | **2** | At minimum, the PEMEX Deer Park operator who developed/provided the job aids and the Repcon day-shift foreman who received them are distinct documented role-side holders. [1] |
| `holder_count_established` | **true** | Two is an established conservative lower bound, not a complete census. |
| `join_assigned` | **unclear** | The report does not affirmatively establish that this identification pathway’s operator/foreman/craftworker fragments were distributed **without** a responsible-and-authorized integrator. It says tag placement was not a documented Run-and-Maintain procedure and “there was no requirement to place it directly on the flange or check its placement,” [1] but absence of that procedure/verification requirement is not affirmative proof of no aggregation function. Nor does the report establish one named role with both responsibility and authority to aggregate all relevant fragments. The report’s separate SIMOPs roles concern surrounding-process hazards, not the selected equipment-identification pathway. [1] |
| `first_signal_date` | **2024-10-08** | The official report expressly dates the selected job-package/tagging condition to October 8. [1] |
| `event_date` | **2024-10-10** | The flange burst open at 4:23 p.m. on October 10. [1] |
| `lead_time_days_min` | **1** | October 8 is a bounded calendar-day interval. Even if the signal arose at the very end of October 8, it preceded the 4:23 p.m. October 10 release by more than one whole day. |
| `lead_time_max_known` | **true** | A date-only source still bounds the occurrence to the October 8 calendar day; the upper bound is therefore quantifiable rather than open. |
| `lead_time_days_max` | **2** | If the signal arose at the start of October 8, the event occurred two whole days plus part of a day later. The integer maximum is two whole days. |
| `sudden_label` | **unclear** | The only relevant lexical matches describe reassignment—“abrupt shift in the work environment” [1] and “sudden reassignment to the Amine Unit” [1]—not the event, the equipment-identification failure, or its warning pattern. The official report does not affirmatively call the selected pathway non-sudden, so `no` is not warranted. |
| `pattern_result` | **indeterminate** | `signal_present=yes`, `signal_reported=yes`, and a two-holder minimum are established, but the necessary `join_assigned=no` condition is unresolved. [2] |

## Validation findings

The prior reconciliation’s `first_signal_date=unknown` and unquantifiable lead time select a broader undated control-system condition while its reporting/holders rest on the dated job-package transfer. That is internally avoidable: the report supplies a dated, causally connected identification signal that stays coherent with the job-aid handoff and holders. The date is only day-precise, so it supports a **1–2 whole-day** bounded lead-time range; it does not support a zero placeholder or `lead_time_max_known=false`.

The prior `join_assigned=no` instead relies on a set of separate findings: a permit lacking a defined hold/stop point [1], contractor status not reaching boilermakers [1], and an unperformed SIMOPs evaluation for neighboring-process hazards [1]. The report does show that these controls were deficient. It does **not**, however, affirmatively establish no assigned integration function for the selected October 8 job-aid/tagging pathway. A named local operator/foreman task and a missing placement-check procedure are likewise insufficient to resolve this variable in either direction. The required conservative value is therefore `unclear`.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery — CSB Investigation Report No. 2024-05-I-TX, February 2026"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

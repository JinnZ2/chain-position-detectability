# Validation record — Dow Louisiana Operations Explosions

**Case ID:** `dow-louisiana-operations`
**Validation verdict:** **Needs correction.** The reconciled `supports` result combines the earliest signal, reporting, and lead time from the **nitrogen-inerting pathway** with the holder minimum and absent join from the distinct **vessel-closure/work-light-debris pathway**. That combination does not meet the codebook’s hazard-related signal and cross-holder requirements when applied as one coherent pathway.

## Corrected final record

| Variable | Corrected value | Basis |
| --- | --- | --- |
| `signal_present` | **yes** | The 20 November 2020 2.4-psig pressure condition and later decline were documented before the event and are directly connected to air intrusion and ethylene-oxide ignition in the pressure-relief piping. |
| `signal_reported` | **yes** | The relevant pressure was recorded by a transmitter. |
| `holder_count_min` | **1** | The report identifies the Dow workers who pressurized the line. It does not establish a second qualifying human, role, team, contractor, or organizational-unit holder of the inerting signal. The transmitter is not a holder under the codebook. |
| `holder_count_established` | **false** | One is a defensible conservative minimum; the report does not enumerate the complete set of pre-event holders. |
| `join_assigned` | **unclear** | The report establishes inadequate monitoring and no effective alerting system, but does not affirmatively establish that no named role or function had both responsibility and authority to aggregate the inerting-pathway fragments. |
| `first_signal_date` | **2020-11-20** | Exact report date for the 2.4-psig post-maintenance condition. |
| `lead_time_days_min` | **966** | Exact calendar-day difference from 2020-11-20 to the 2023-07-14 event. |
| `lead_time_max_known` | **true** | Both endpoints are exact dates. |
| `lead_time_days_max` | **966** | The exact endpoint dates give the same finite maximum. |
| `sudden_label` | **unclear** | The report does not apply “sudden,” “unexpected,” “unforeseen,” “without warning,” or an equivalent characterization to the event or the selected inerting warning pattern. The dictionary definition of a process upset on printed p. 20 is not an event-specific label. |
| `pattern_result` | **indeterminate** | The signal and reporting elements are established, but neither a two-holder minimum nor an affirmative absence of an assigned cross-holder join is established for the same inerting pathway. |

## Coherent pathway and evidence

The selected pathway is **loss of nitrogen inerting in the pressure-relief piping → air intrusion → ethylene-oxide ignition after the rupture disc opened**. It is the only pathway that contains the reconciled record’s earliest dated signal. CSB reports:

> “Upon completing the installation of the rupture disc, Dow workers pressurized the pressure relief piping between the rupture disc and PRV with 2.4 psig of nitrogen … Over the next two months … the nitrogen pressure … gradually decreased, eventually reaching atmospheric pressure and even showing negative gauge pressure …” [1] (printed p. 18).

That reading was below the procedure’s stated end condition:

> “Reduce the pressure in the pressure relief piping to 5 psig before closing the system.” [1] (printed p. 38).

CSB confirms both the recorded condition and its causal relevance:

> “Process data shows that the piping was left with only 2.4 psig instead of the required 5 psig … and that the pressure slowly declined over the next two months, indicating that leaks were occurring.” [1] (printed p. 39).

> “The pressure between the rupture disc and PRV was recorded by a transmitter but was not adequately monitored by Dow.” [1] (printed p. 27).

> “With the loss of the inerting gas in the pressure relief piping, the ethylene oxide mixed with air and ignited when it reached the pressure relief piping.” [1] (printed p. 27).

These quotations establish `signal_present=yes`, `signal_reported=yes`, the one documented worker-group holder, and the exact 966-day interval. They do **not** establish a second qualifying holder of that signal. The transmitter and post-incident CSB analysis cannot be counted as people, roles, teams, contractors, or organizational units under the holder definition. [2]

The record also cannot convert weak controls into an affirmatively absent cross-holder join. CSB found that Dow “did not have an effective system in place to alert operations about the presence of or lack of an inerting atmosphere” [1] (printed p. 40), and reports no low-pressure alarm or periodic pressure-check requirement [1] (printed pp. 27, 39). Those findings show deficient monitoring. They do not identify the relevant assigned roles and affirmatively establish that none had both the responsibility and authority to aggregate the inerting-maintenance and transmitter fragments. Under the codebook, missing role information remains `unclear`, not `no`. [2]

## Why the reconciled holder/join evidence cannot be used

The reconciled record’s `holder_count_min=2` and `join_assigned=no` instead come from the **work-light/vessel-closure pathway**. CSB separately reports that tools were tracked at the Glycol II unit rather than vessel level and that five magnetic work lights were not returned [1] (printed p. 30). It also reports that the vessel-closure form did not make clear whether the permit writer had to confirm contractors had recovered their materials, and that the operator had no exact way to ensure all equipment had left a vessel [1] (printed p. 32). CSB identifies the resulting work-light debris as the mechanism that opened the rupture disc [1] (printed pp. 45–46).

That is relevant evidence for a different initiating-debris pathway, not evidence of two holders of the 2020 inerting signal or a missing inerting-pathway join. The named permit writer is a local vessel-closure owner, not affirmative proof of an inerting-pathway join; likewise, the absence of a vessel-specific tracking procedure is not by itself proof that every aggregation function was unassigned. The report treats vessel closure and inerting as separate safety issues and identifies both as contributors to the event. [1] (printed pp. 45–46). Combining them merely to satisfy separate variables violates the required pathway coherence rule.

For suddenness, the only occurrence of “sudden” is a dictionary definition that a process upset can be “a sudden, gradual, or unintended change” [1] (printed p. 20). It is neither an official characterization of this event nor of the selected warning pattern. No affirmative `yes` or `no` label is therefore supported.

## Validation conclusion

The official CSB final report was opened and read. A coherent inerting-pathway record supports a documented and recorded 2020 signal with an exact 966-day lead time. It supports **only one conservative documented holder** and leaves the assigned-join question **unclear**. The corrected case is consequently **indeterminate**, not `supports`.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6316 "U.S. Chemical Safety and Hazard Investigation Board, Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations (Investigation Report No. 2023-03-I-LA, February 2026)"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

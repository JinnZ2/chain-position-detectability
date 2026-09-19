# Validation record — U.S. Steel Clairton

**Case ID:** `us-steel-clairton`
**Validator:** Manus AI
**Verdict:** **Needs correction.** The reconciled record combines the 2003 facility-siting/severity pathway with the water-washing/valve-overpressure pathway used to infer a missing join. The final classification must use one pathway. This validation uses the officially causal **high-pressure water-washing pathway** throughout.[1]

## Corrected values

| Field | Corrected value | Basis and source location |
|---|---|---|
| `signal_present` | **yes** | The established high-pressure water-washing practice is a documented pre-event state directly tied to the initiating overpressure mechanism. Printed pp. 37–39, 63, 65.[1] |
| `signal_reported` | **yes** | The practice was recorded in the battery-isolation procedure and the report says Clairton management approved and implemented that procedure. Printed p. 38.[1] |
| `holder_count_min` | **2** | At minimum, water-washing workers and Clairton management held relevant pathway fragments. Printed pp. 37–38.[1] |
| `holder_count_established` | **false** | The report supports a conservative floor, not a complete enumeration of workers, managers, or contractor holders. |
| `join_assigned` | **unclear** | The report establishes serious planning, procedure, training, and hazard-analysis failures, but does not affirmatively establish that no named role or function had both assigned responsibility and authority to aggregate the relevant cross-holder water-washing information. Printed pp. 23–24, 39–40, 60.[1] |
| `first_signal_date` | **at least 3 years before 2025-08-11** | This preserves the report’s relative precision for the selected water-washing pathway. Printed p. 37.[1] |
| `lead_time_days_min` | **1096** | Three complete calendar years from 2022-08-11 to the 2025-08-11 event, using the report’s “at least three years” lower bound. |
| `lead_time_max_known` | **false** | The practice could have begun earlier; the report gives no bounded start date. |
| `lead_time_days_max` | **0** | Required placeholder for an unquantifiable maximum; it is not a substantive zero-day interval. |
| `sudden_label` | **yes** | The CSB applies “sudden” directly to the relevant valve fracture. Printed p. 30.[1] |
| `pattern_result` | **indeterminate** | Signal, reporting, and a two-holder minimum are established, but the required affirmative showing of **no** assigned cross-holder join is not. Under the codebook, an unresolved necessary element yields `indeterminate`.[2] |

## Coherent-pathway finding

The selected pathway is: workers’ established use of high-pressure water to wash valve seats, management’s recorded knowledge and endorsement, lack of safe procedure and hazard analysis, water pressurization between closed valve gates, catastrophic valve failure, coke-oven-gas release, and explosion. The report expressly identifies this chain as the cause and a contributing set of deficiencies:

> “The CSB determined the cause of the incident was the overpressurization of a double disc gate valve constructed of cast iron, which resulted in the release of flammable coke oven gas that ignited and exploded. … This enclosure was pressurized with water during an operation in which U.S. Steel and its contractor, MPW, were attempting to wash the valve with high-pressure water.” — §5.2, printed p. 65 [1]

> “Contributing to the incident was U.S. Steel’s and MPW’s lack of a procedure detailing how to safely perform the valve washing operation, along with U.S. Steel’s and MPW’s failure to identify or adequately address the potential hazards of the operation.” — §5.2, printed p. 65 [1]

The reconciled 2003 anchor does not belong to this pathway. The report identifies the 2003 PHA recommendation as a missed opportunity to address **facility-siting risks** that increased injury severity, not as a pre-event signal of the water-washing/overpressure mechanism. It states that “the 2003 PHA recommendation and the 2010 coke oven gas explosion both presented key opportunities for U.S. Steel to address facility siting risks,” while separately treating water washing under “Procedures and Hazard Analysis.” — §5.1, printed pp. 63–64 [1] Using the 2003 signal and its PHA/management holders together with a water-washing join finding would combine distinct official hazard pathways.

## Evidence for the corrected pathway fields

The report establishes the pre-event signal and its conservative timing:

> “Over time, water washing became the preferred method for workers to remove coke oven gas residue from valve seats to prepare for purges.” — §4.1.1, printed p. 37 [1]

> “Based on interviews conducted by the CSB, water washing had been conducted as a method to prepare for purges for at least three years before the day of the incident. Despite the facility’s use of high-pressure water to remove coke oven gas residue, it was never proceduralized.” — §4.1.1, printed p. 37 [1]

This is a case-specific documented state and is directionally tied to the mechanism, rather than merely preceding it. It was communicated beyond private awareness:

> “The battery isolation procedure shown in Figure 18 above was approved and implemented by Clairton management, indicating their knowledge and endorsement of the water washing practice.” — §4.1.1, printed p. 38 [1]

Those quotations establish at least two role-level holders: workers performed and treated water washing as the status quo; management knew of and endorsed it. They do not enumerate all relevant holders, so the lower bound is **2** and its completeness is **not established**.

The report does **not** permit `join_assigned = no` under the codebook’s affirmative-evidence standard. It documents that the relevant wash was outside one planning meeting’s scope:

> “The plans made during the meeting did not include exercising, steaming, or washing the Battery 13 isolation valve. None of the workers or contractors who exercised and washed the isolation valve on the day of the incident were present at the meeting.” — §2.2, printed pp. 23–24 [1]

It also finds that management systems enabled task direction without controls:

> “U.S. Steel’s management systems were such that a U.S. Steel supervisor was enabled to arrange and direct the valve washing operation without prior planning, a procedure, training, a work permit, or sufficient hazard analysis and mitigation.” — §4.3, printed p. 60 [1]

These findings show that the hazardous task was not properly planned or controlled. They do not say that no designated function had responsibility **and** authority to aggregate water-washing fragments held across workers, management, and contractor personnel. A supervisor who directed the local task is not, without more, a qualifying cross-holder join; conversely, a missing procedure, hazard analysis, permit, or relevant HJM coverage is not itself proof that no aggregation function was assigned. The required value is therefore **unclear**, not `no`.[2]

Finally, the suddenness label is valid because the wording applies directly to the relevant failure, not merely to an alarm or generic physical movement:

> “External visual examination determined that the crack in the body of the Battery 13 gas isolation valve was fully circumferential, and was visually consistent with sudden, brittle fracture.” — §3, printed p. 30 [1]

## Corrections to the reconciled record

The final record changes `first_signal_date` from `2003` to **`at least 3 years before 2025-08-11`** and changes the lead-time range from **7,894–8,258 days** to a minimum of **1,096 days** with an unquantifiable maximum (`lead_time_max_known = false`; numeric placeholder `0`). It changes `join_assigned` from **`no`** to **`unclear`** and consequently changes `pattern_result` from **`supports`** to **`indeterminate`**. The reconciliation’s `signal_present`, `signal_reported`, holder minimum of 2, unestablished complete holder count, and `sudden_label = yes` remain supported when tied only to the water-washing pathway.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6340 "Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works — CSB Investigation Report No. 2025-03-I-PA, August 2026"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

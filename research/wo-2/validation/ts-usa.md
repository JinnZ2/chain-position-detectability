# WO-2 validation record — TS USA Molten Salt Eruption

**Case ID:** `ts-usa`
**Validation verdict:** **Needs correction**
**Official final report read:** Yes — CSB, *TS USA Molten Salt Eruption—Investigation Report*, published June 2025.[1]
**Pathway test:** **Consistent after correction.** The pathway used here is one cross-facility **water/accumulation-in-cavity → salt-bath overpressure/steam explosion** pathway. It does not substitute the incident-day obstruction/reprocessing pathway for the prior-knowledge pathway.

## Corrected coding record

| Variable | Corrected value | Validation basis |
|---|---:|---|
| `signal_present` | **yes** | The 2018 Mexico event and the corporate risk analysis are pre-event, hazard-related evidence on the same cavity/water/salt-bath mechanism. The CSB says the 2018, 2020, and 2023 events showed that parts trapping material in cavities lead to overpressure explosions in salt baths (p. 55).[1] |
| `signal_reported` | **yes** | TS ETSA “developed a formal report detailing the incident, causal factors, and corrective actions”; an English report was “presented to HEF Groupe” (p. 43).[1] This satisfies recording and communication beyond private awareness, notwithstanding inadequate onward dissemination. |
| `holder_count_min` | **2** | The conservative, coherent lower bound is **TS ETSA** (formal incident report) and **HEF Groupe** (recipient of English report; corporate holder of the risk analyses). The complete count is **not established**. |
| `holder_count_established` | **false** | The report establishes at least two organizational holders, but not a complete holder census. |
| `join_assigned` | **unclear** | The report documents failure of knowledge management and absent dedicated safety resources, but it does **not affirmatively establish that no role/function with both responsibility and authority to aggregate this cross-holder pathway was assigned**. It says HEF Groupe relied on “regional and plant management” to ensure requirements (p. 52), while also finding no dedicated safety resources/roles. This makes `yes` unsupported and, under the codebook’s affirmative-evidence rule for `no`, leaves `no` unsupported. A local operational owner is not treated as a cross-holder join. |
| `first_signal_date` | **unknown** | `2018-01-25` is the earliest **dated** pathway signal, not the report-supported earliest signal. The report also says HEF Groupe developed risk assessments for water introduction into a molten-salt bath “before the 2024 incident,” without dating or ordering them relative to 25 January 2018 (p. 48).[1] Preserve the unresolved chronology rather than choosing the earliest dated item. |
| `lead_time_days_min` | **0** *(unquantifiable placeholder)* | Because the earliest coherent signal is undated and cannot be ordered against 2018, no numeric minimum is defensible. `0` is not a claimed zero-day interval. |
| `lead_time_max_known` | **false** | The undated risk analysis prevents a bounded interval from the actual earliest pathway signal. |
| `lead_time_days_max` | **0** *(unquantifiable placeholder)* | Open/unquantifiable upper bound; not a claimed zero-day interval. |
| `sudden_label` | **unclear** | The report does not characterize the event, relevant failure, or warning pattern as sudden, unexpected, unforeseen, or without warning. Its wording that water “rapidly expanded as steam” and “rapidly boiled” (p. 53) is a physical-process adverb, not a qualifying suddenness label under the supplemental validation rule.[1] |
| `pattern_result` | **indeterminate** | `signal_present=yes`, `signal_reported=yes`, and the two-holder floor are established; however, `join_assigned` remains unresolved. The codebook requires `join_assigned=no` for `supports` and makes a case indeterminate when a necessary element is unresolved.[2] |

## Coherent-hazard-pathway check

The selected pathway is supported from beginning to end by the final report. On **25 January 2018**, TS ETSA had a roller event after water entered during rinsing and was introduced to the nitriding bath; the report describes an overpressure explosion after pressure increased in the roller (p. 42).[1] TS ETSA subsequently determined that “a part with an accumulation hazard was allowed to be processed in the liquid nitriding line” (p. 43).[1] HEF Groupe also retained a risk analysis identifying the “Risk of explosion if water is present in the baths which may be on or in the parts” (p. 48).[1] The CSB’s 2024 causal finding is the same mechanism: water in the roller cavity introduced to the 800°F oxidizing salt bath, producing overpressure, a steam explosion, and a molten-salt eruption (p. 56).[1]

The report’s own synthesis supplies the required connection rather than an engineering inference:

> “All three incidents discussed above—2018 in Mexico, 2020 in France, and 2023 in Chattanooga—show that these parts are susceptible to trapping materials in their cavities, which leads to overpressure explosions when the parts are introduced to the salt baths.” (p. 55)[1]

The holder, reporting, and possible aggregation evidence is evaluated only for that pathway. The validation does **not** use a plant manager’s incident-day reprocessing work as a purported cross-holder join, nor does it infer absence of a join merely from a missing reprocessing procedure.

## Why the reconciled final record needs correction

The reconciled record’s `signal_present=yes`, `signal_reported=yes`, and two-holder lower bound are supported. Its `join_assigned=no`, `first_signal_date=2018-01-25`, exact 2,317-day lead time, `sudden_label=yes`, and `pattern_result=supports` are not all supported under the codebook plus the requested validation rules.

First, the report affirmatively describes poor/ineffective corporate knowledge management, but not an affirmative absence of every responsible-and-authorized cross-holder integration function. Its finding is that HEF Groupe “did not manage safety knowledge throughout the company” and did not ensure subsidiary provision, transfer, and management of developed information (pp. 50, 55).[1] That establishes a failure, but the report also identifies regional and plant management as the arrangement relied on for safety requirements (p. 52).[1] It neither assigns those managers the requisite cross-holder aggregation authority nor affirmatively rules such an assignment out. `unclear` is therefore required rather than converting an ineffective arrangement or absent dedicated role into `no`.

Second, the report’s undated corporate risk assessment is both pathway-relevant and explicitly pre-event. Its timing is only “before the 2024 incident” (p. 48).[1] Because the report does not establish whether it predates the 2018 incident, 2018-01-25 cannot be retained as the actual earliest signal date, and a 2,317-day exact interval cannot be retained. The numeric lead-time fields use `0` solely as the required unquantifiability placeholder; the accompanying maximum-known flag is false.

Third, the CSB’s exact wording is:

> “The retained water boiled inside the roller’s cavity and rapidly expanded as steam. … The water rapidly boiled, creating a violent steam explosion ….” (p. 53)[1]

Those terms describe the reaction’s physical rate; they are not an official sudden/unexpected/unwarned characterization of the event, failure, or warning pattern. The field is therefore `unclear`, not `yes`.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6296 "Explosion, Molten Salt Eruption, and Fatal Injury at TS USA Liquid Nitriding Facility — CSB Investigation Report, June 2025"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/reconciliation-log.md "WO-2 validated reconciliation log"

[4]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/pilot-analysis.md "WO-2 final pilot analysis"

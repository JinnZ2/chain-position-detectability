# WO-2 Evidence Record — Dow Louisiana Operations Explosions

**Coder:** A
**Case ID:** `dow-louisiana-operations`
**Title:** *Dow Louisiana Operations Explosions*
**Event date:** 2023-07-14
**Report publication date:** 2026-02-26
**Official final-report URL:** <https://www.csb.gov/file.aspx?DocumentId=6316>

## Coded values

| Variable | Code | Basis |
| --- | --- | --- |
| `signal_present` | **yes** | A pressure-relief-piping pressure reading of 2.4 psig after the 20 November 2020 maintenance, rather than the procedure's required 5 psig, then declining pressure and negative gauge readings, is a documented pre-event measurement directly connected by CSB to loss of inerting and subsequent ignition. |
| `signal_reported` | **yes** | CSB states that the pressure was **recorded by a transmitter**. This is a recorded signal beyond private awareness even though it was not adequately monitored by Dow. |
| `holder_count_known` | **false** | The report does not establish all pre-event human/organizational holders of the recorded pressure condition or that they reviewed it. |
| `holder_count_min` | **1** | At minimum, the Dow workers who pressurized the line at the end of the 20 November 2020 maintenance constitute one documented work group holding the relevant initial pressure-setting/maintenance fragment. The transmitter also recorded the value, but is not counted as a separate person, role, team, contractor, or organizational unit. |
| `join_assigned` | **unclear** | The report documents missing/effectless monitoring and no effective alerting system, but it does not affirmatively resolve whether a named role or function had both responsibility and authority to aggregate all relevant pre-event fragments (maintenance condition, transmitter record, and loss of inerting). |
| `first_signal_date` | **2020-11-20** | Date of the earliest documented relevant pressure condition following rupture-disc maintenance. |
| `lead_time_days_min` | **966** | Calendar difference from 2020-11-20 to 2023-07-14. |
| `lead_time_max_known` | **true** | Both endpoints are exact dates. |
| `lead_time_days_max` | **966** | Exact-date interval; equal to the minimum. |
| `sudden_label` | **unclear** | The final report does not characterize this incident, its failure, or its pre-event warning pattern as sudden, unexpected, unforeseen, or without warning. Its use of “sudden” is only within a general dictionary definition of “process upset,” not an official label for this event. |
| `pattern_result` | **indeterminate** | Although a reported, hazard-relevant signal is present, the final report does not support a minimum of two documented pre-event holders and does not affirmatively establish the absence of a responsible-and-authorized integration role. The necessary conditions for `supports` therefore remain unresolved. |

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6316 "Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations — CSB Investigation Report No. 2023-03-I-LA, February 2026"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

## Incident mechanism and chronology

CSB determines that metal debris from portable work lights left in the reflux drum punctured a rupture disc; ethylene oxide then entered pressure-relief piping that contained air, ignited, and propagated back to the reflux drum, which catastrophically failed [1]. CSB separately identifies loss of the line's nitrogen inert atmosphere as a contributing condition: after 2020 maintenance, nitrogen leaked out, air entered the piping, and the resulting ethylene-oxide/air mixture could ignite [1].

For the selected earliest signal, CSB reports that, on **November 20, 2020**, Dow replaced the product-cooler rupture disc and workers pressurized the pressure-relief piping with **2.4 psig** nitrogen. The pressure gradually fell over the next two months, reached atmospheric pressure, and at times showed negative gauge pressure; no nitrogen was added between that maintenance and the 2023 incident [1]. The governing procedure required a leak check at 90 psig and reduction to **5 psig** before closing the system [1]. CSB later confirms that process data showed only 2.4 psig at maintenance completion rather than the required 5 psig, followed by a two-month decline indicating leaks [1].

The event itself occurred on **July 14, 2023**. At approximately 6:52 p.m. a reflux pump shut down on a high-high vibration interlock; an operator found apparent insulation and restarted it. CSB's post-incident analysis says the vibration was likely caused by work-light debris. Operators then sought to stabilize process levels until the explosion at approximately 9:17 p.m. [1]. This later vibration indication is corroborative of the debris mechanism, but the earliest date used for the lead-time fields is the explicitly dated 2020 inerting-pressure condition.

## Decisive evidence by variable

### Signal presence — `yes`

> “Upon completing the installation of the rupture disc, Dow workers pressurized the pressure relief piping between the rupture disc and PRV with 2.4 psig of nitrogen … Over the next two months … the nitrogen pressure … gradually decreased, eventually reaching atmospheric pressure and even showing negative gauge pressure …” [1].

The measured pressure was below the specific procedure's required 5 psig end condition [1]. This is not treated merely as a generic maintenance irregularity. CSB expressly connects the same loss of inerting to the event: air entered through the leaks as pressure showed negative readings, and, once the rupture disc opened, ethylene oxide mixed with that air and ignited [1]. Its formal finding is that the piping “did not have adequate inerting nitrogen to prevent the ignition of ethylene oxide” [1]. The measurement is therefore a documented, directionally hazard-relevant pre-event signal under [2].

### Reporting/recording — `yes`

> “The pressure between the rupture disc and PRV was **recorded by a transmitter** but was not adequately monitored by Dow.” [1].

CSB also says that process data showed the 2.4-psig completion reading and subsequent pressure decline [1]. These statements support `yes` for the codebook's recorded/communicated criterion, without claiming that an operator actually noticed or acted on the record. Indeed, CSB reports no evidence that an operator or management official checked the pressure in the two-plus years after the 2020 rupture-disc work; a negative reading did not produce an alarm [1].

### Holders — minimum `1`; count known `false`

The report identifies “Dow workers” who performed the pressurization at the end of the 20 November 2020 maintenance [1], establishing at least one documented work group with the initial pressure-setting fragment. It also establishes a transmitter/process-data record [1]. However, it does **not** identify which persons, roles, teams, or units could access or did access that record before the incident, nor does it establish distinct holders of it. The code therefore uses the conservative lower bound of one and does not infer a second holder from the existence of an instrument or from post-incident analysis.

### Assigned join — `unclear`

There is strong evidence of deficient monitoring: the transmitter had only a high-pressure alarm, no low-pressure alarm, and operations personnel were not required to check pressure periodically [1]. CSB concludes that Dow had no effective system to alert operations about the presence or lack of inerting and that operations were unaware the piping was filled with air [1]. The report also says no PHA or risk assessment from 2011–2023 identified the need for this inert atmosphere [1].

Those facts establish an ineffective alerting/monitoring system, but they do not identify and negate every possible named role/function possessing both the responsibility and authority to integrate all of the relevant signals. Under the stricter rule in [2], they cannot by themselves establish `join_assigned=no`; nor can they establish `yes`. The value is consequently `unclear`.

### Lead time — `2020-11-20`, 966 days minimum and maximum

The report supplies the exact initial date of the relevant 2.4-psig reading/maintenance condition (November 20, 2020) [1] and the exact incident date (July 14, 2023) [1]. The elapsed calendar interval is **966 days**. Because both dates are exact, this is both the defensible minimum and the bounded maximum for this selected earliest documented signal.

### Sudden label — `unclear`

CSB describes the observed pump shutdown, process stabilization efforts, and explosion timing [1], but does not apply a suddenness-equivalent characterization to the event or its warning pattern. The only relevant word use is a quoted dictionary definition that says a process upset may be “a sudden, gradual, or unintended change”; that is a generic definition, not CSB's label for this incident [1]. Therefore no `yes` or `no` suddenness code is defensible.

## Coding limitations

1. **Recorded does not mean reviewed.** The transmitter/process-data record supports `signal_reported=yes` under the codebook's recording rule, but the report affirmatively says it was not adequately monitored and provides no evidence of pre-event human review of the declining/negative readings [1].
2. **Do not promote physical systems to people.** The transmitter and the later CSB analysis are not counted as additional pre-event human/organizational holders. The report does not document at least two distinct qualifying holders of the selected pressure signal.
3. **No inferred integration ownership.** The report supports inadequate procedures and alerting, not a fully enumerated organization chart or an affirmative, case-wide proof that no named authority could join the signals. `join_assigned` remains `unclear` rather than `no`.
4. **Work-light evidence is not used to increase the holder count.** CSB documents that five lights were never returned after the May 2023 turnaround [1] and directly connects lights left in the drum to the rupture-disc failure [1]. But it does not establish which people recognized the non-return before the event; CSB says the lights remained “unbeknownst to the workers” at final closure [1]. This record therefore does not infer pre-event holders from subsequent reconciliation or outcome evidence.
5. **Lead-time scope.** The 966-day interval is anchored to the earliest exact, report-documented relevant pressure measurement, not to an unobserved date when air first entered the piping. No broader open-ended maximum is claimed.

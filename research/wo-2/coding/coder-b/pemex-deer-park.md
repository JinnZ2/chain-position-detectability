# WO-2 evidence record — PEMEX Deer Park Chemical Release

## Case identification

| Field | Value |
| --- | --- |
| Case ID | `pemex-deer-park` |
| Coder | B |
| Official report | *Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery*, CSB No. 2024-05-I-TX, published February 2026 [1] |
| Final-report URL | https://www.csb.gov/file.aspx?DocumentId=6315 |
| Event date | 2024-10-10 |
| Event | At 4:23 p.m., contract workers opened the active ARU7 acid-gas flange rather than the intended isolated ARU6 flange, releasing hydrogen sulfide. The report identifies ineffective positive equipment identification as the cause. [1] |

## Coded values

| Variable | Code | Evidence-based rationale |
| --- | --- | --- |
| `signal_present` | **yes** | Before the event, an intended-equipment identifier for Blind 407 was put on a platform railing rather than directly on the inaccessible blind (October 8). The CSB connects the out-of-sight tag, other inadequate identifiers, and the workers’ choice of ARU7 directly to the wrong-equipment opening. [1] |
| `signal_reported` | **yes** | This was not private awareness: operators physically placed the blind tag as an identifier and conducted a unit walkthrough with the Repcon night-shift foreman; on October 10 an operator gave the blind list and drawing to the day-shift foreman and escorted the foreman and four workers through the unit. The written permit also recorded the acid-gas line-break control, “Ops present for each break,” and the operator said he verbally told the foreman to alert an operator before opening acid-gas piping. [1] |
| `holder_count_known` | **false** | The report documents multiple holders but not an exhaustive count of all people/roles holding relevant fragments. |
| `holder_count_min` | **2** | Conservative distinct-role lower bound: (1) the PEMEX Deer Park operator, who prepared/provided the job materials and issued the permit; and (2) the Repcon day-shift foreman, who received the materials/instruction. The report documents both roles and the transfer between them. [1] |
| `join_assigned` | **unclear** | The permit procedure assigned several roles—equipment owner, permit issuer, permit cosigner, and permit receiver—responsibility to identify/manage risks to other processes. But the report does not establish that one named role/function had both responsibility **and authority** to aggregate the pertinent equipment-identification, contractor-hazard-communication, permit-hold-point, and adjacent-unit-risk fragments. Nor does it affirmatively establish that no such integration point existed. [1] |
| `first_signal_date` | **2024-10-08** | On October 8, operators prepared the blind list/drawing and hung tags; Blind 407’s tag was placed on a nearby railing rather than on the blind. This is the earliest *dated* pre-event condition that the CSB connects to the equipment-identification failure. [1] |
| `lead_time_days_min` | **1** | The source dates the misplaced-tag condition only to October 8, while the release occurred at 4:23 p.m. on October 10. Even placing the October 8 action at the end of that date leaves more than one full day before the release. No stronger whole-day lower bound is warranted without an October 8 time. [1] |
| `lead_time_max_known` | **false** | The report gives no time of day for the October 8 tag placement; therefore a bounded maximum cannot be defended from the report’s stated precision. |
| `lead_time_days_max` | **0** | Required placeholder because the maximum is open/unknown (`lead_time_max_known=false`). |
| `sudden_label` | **no** | The report does not characterize the event, failure, or warning pattern as sudden, unexpected, unforeseen, or without warning. Its sole use of “sudden” concerns the reassignment of workers—not the release or warning pattern—and the causal conclusion instead identifies specific pre-event identification, permitting, contractor-management, and conduct-of-operations deficiencies. [1] |
| `pattern_result` | **indeterminate** | Signal presence, pre-event reporting, and at least two documented holders are supported; however, `join_assigned` remains unresolved under the codebook’s responsibility-and-authority test. Thus the conditions for `supports` are not all established, while no necessary element is affirmatively false. [2] |

## Evidence record and coding rationale

### Incident mechanism and relevant pre-event signals

The CSB determines that the incident was caused by opening incorrect equipment: the workers opened pressurized ARU7 acid-gas piping after mistaking it for the intended ARU6 Blind 407 location. It attributes that error to PEMEX Deer Park’s failure to establish an effective method to identify the equipment before authorizing its opening. [1] This causal determination supplies the required official connection between the selected pre-event signals and the hazard mechanism; this record does not treat mere temporal precedence as relevance.

The earliest date-specific relevant condition appears on **October 8, 2024**. In preparing ARU6 for maintenance, operators made a blind list and drawing and, as their typical practice, put tags on the blinds. For Blind 407, however, the report says that the blind could not be easily accessed and the operators placed its tag “on a nearby railing,” rather than directly on the blind. [1] The CSB later explains that the tag was “out of sight” from the work location and that the workers instead selected ARU7 after observing the misplaced flange-locking device. [1] Its Findings repeat that an unlocked device on ARU7 and the out-of-sight Blind 407 tag led to selection of the wrong active line. [1]

Other documented pre-event fragments reinforce the coding without being used to move the first-signal date earlier. At 8:18 a.m. on October 10, the operator issued a permit for all 15 blinds, gave the list/drawing to the day-shift foreman, and led the foreman and four boilermakers through the unit. [1] The permit required an operator’s presence for pipe openings and imposed supplied-air protection for the final two acid-gas blinds. [1] The CSB reports the permit’s phrase “Ops present for each break,” the operator’s verbal direction to alert an operator before acid-gas opening, and the foreman’s different interpretation of that requirement. [1] It concludes that the undefined hold/stop point led the operators, foreman, and boilermakers to understand the requirement differently and resulted in an active H2S line being opened without an operator present. [1]

### Holders and reporting

The conservative lower-bound count is two roles, rather than attempting to count every operator or craftworker. The operator prepared/provided job materials, issued the permit, and gave the relevant direction. The Repcon day-shift foreman received the job package/instruction. [1] The cited exchanges demonstrate communication/recording beyond a single person and support `signal_reported=yes`. They do not establish a complete total of signal holders, so `holder_count_known=false`.

The report also documents a separate communication gap that is mechanism-relevant: the foreman knew the Amine Unit’s status, but the boilermakers did not receive it; PEMEX policy expected the foreman to relay permit and job requirements. [1] The CSB concludes that PEMEX and Repcon did not sufficiently communicate the relocation from a shutdown unit to an active unit. [1]

### Joining / integration assignment

This record does **not** code `join_assigned=yes`. The report identifies a distributed permit process: the equipment owner, permit issuer, permit cosigner, and permit receiver were responsible for identifying/managing risks to other processes, and the expected documentation was a SIMOPs form. Yet none of the process owners, permit issuers, or reviewers completed that form. [1] That demonstrates deficient implementation and distributed responsibilities, but it does not expressly establish a single role with both responsibility and authority to integrate every relevant cross-holder fragment. It also does not expressly negate the existence of such an authority. The strict codebook rule therefore requires **unclear**, not an inferred `yes` or `no`.

### Lead time and official suddenness language

Only a calendar date—not an October 8 time—is reported for the earliest signal. The 2024-10-10 release time is 4:23 p.m.; therefore one full day is a defensible conservative lower bound, while the maximum is unbounded at the report’s precision. [1] The report calls the worker reassignment “sudden,” but does not apply suddenness language to the event, failure, or pre-event warning pattern. [1] Accordingly, that word is not treated as an official `sudden_label` for this codebook field.

## Limitations

1. The record uses the earliest **dated** mechanism-relevant pre-event condition. The report does not give a time of day for the October 8 tag placement. Consequently, the lower bound is limited to one full day and the maximum lead time is unknown/open.
2. The final report documents several people and roles but does not enumerate every pre-event holder of every relevant fragment. The holder count is a deliberately conservative minimum of two, not an estimated total.
3. The report specifies distributed permit/SIMOPs responsibilities but does not document a named authority empowered to join all pertinent fragments, nor does it definitively say no such function existed. `join_assigned` is therefore `unclear` under the codebook rather than inferred from the operational failure.
4. The report’s one “sudden” reference describes reassignment, not the release/failure/warning pattern. This record does not extend that descriptor beyond the report’s stated referent.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery — CSB Investigation Report No. 2024-05-I-TX, February 2026"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

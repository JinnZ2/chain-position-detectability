# WO-2 evidence record — PEMEX Deer Park Chemical Release

## Case identification

| Field | Value |
| --- | --- |
| Case ID | `pemex-deer-park` |
| Coder | A |
| Incident | PEMEX Deer Park Chemical Release / Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery |
| Event date | 2024-10-10 |
| Final report publication | 2026-02-23 (manifest); report front matter says February 2026 |
| Official final report | [CSB final report][1] |
| Scope of review | Official CSB final report, including incident description (printed pp. 18–25), safety issues (pp. 26–60), findings and cause (pp. 61–63), and front matter. Printed and PDF page numbers coincide in this report. |

## Coding decision

| Variable | Coder A value | Evidence-based rationale |
| --- | --- | --- |
| `signal_present` | **yes** | Before the release, the job was being controlled through an inadequate equipment-identification state: an unclear list/sketch, an out-of-sight Blind 407 tag, and nonstandard/inconsistent physical identifiers. CSB expressly connects these conditions to the wrong-equipment selection and release. This is a documented, incident-specific pre-event state rather than generic knowledge. |
| `signal_reported` | **yes** | The identification materials and permit were recorded and passed from a PEMEX Deer Park operator to the Repcon day-shift foreman; the operator also escorted the foreman and four boilermakers through the locations. Thus, the relevant pre-event information/control state was communicated beyond one holder, even though it was ineffective. |
| `holder_count_known` | **true** |
| `holder_count_min` | **2** | Conservative lower bound: (1) PEMEX Deer Park operations/operator, which prepared/provided the job aids and controlled the active-unit work; and (2) the Repcon day-shift foreman, which received the list/drawing and walkthrough. The report supports these two distinct role-side holders. I do not count individual boilermakers separately because the record is not needed to establish this lower bound. |
| `join_assigned` | **no** | CSB affirmatively documents a fragmented, not integrated, control arrangement: the permit lacked a defined hold/stop point, so operators, the foreman, and boilermakers understood the requirement differently; CSB further found that the parties did not sufficiently communicate the transfer into the active unit. The nominal operator-presence item and the foreman handoff do not meet the codebook’s strict rule for a named role/function with both responsibility and authority to aggregate the relevant cross-holder information: the evidence instead shows partial handoffs and an undefined stop point. |
| `first_signal_date` | **unknown** | The earliest selected signal is the pre-existing inadequate Run-and-Maintain equipment-identification/control system. The report establishes that it predated the event but gives no adoption, discovery, or first-observation date. The report dates one manifestation—the Blind 407 tag placement—to October 8, but that cannot establish the first date of the underlying documented signal state. |
| `lead_time_days_min` | **0** | No numeric lower bound is defensible because the earliest documented signal’s start date is unknown. |
| `lead_time_max_known` | **false** |
| `lead_time_days_max` | **0** | The signal state is open-ended/undated; there is no defensible maximum lead time. |
| `sudden_label` | **unclear** | The report describes an “abrupt shift in the work environment” (printed p. 8), but does not characterize the event, failure, or warning pattern itself as sudden, unexpected, unforeseen, without warning, or a close equivalent. That phrase concerns reassignment, not an official suddenness label for the release/failure. |
| `pattern_result` | **supports** | Necessary conditions are met: documented incident-related pre-event signal (**yes**); it was communicated/recorded beyond one holder (**yes**); at least two role-side holders (**2**); and affirmative evidence of distributed fragments without a qualifying assigned integration point (**no**). |

## Decisive official evidence

### 1. Report-controlled hazard mechanism and connection of the signal to it

CSB identifies the cause as opening incorrect equipment, releasing pressurized hydrogen sulfide, and states that PEMEX Deer Park “did not establish an effective method to clearly identify the correct equipment to open before authorizing opening the equipment.” The report adds that PEMEX Deer Park deviated from policies and procedures that could have prevented the incident.[1]

The safety-issues introduction ties the pre-event control conditions directly to the outcome: deficiencies in physically marking equipment, permitting contractor work, and contractor management “ultimately contributed to the inadvertent opening of piping containing toxic hydrogen sulfide and subsequent worker fatalities.”[1] This is the official causal connection required to treat the identification/control condition as a relevant signal rather than infer relevance from timing alone.

### 2. Documented pre-event signal state

The operator provided Repcon a written blind list and a computer sketch, but the CSB found the materials ineffective: Blind 407’s shown location was not connected to the process and the sketch inaccurately depicted its relationship to Blind 408.[1] The report’s finding is explicit: “PEMEX Deer Park’s job aids—a written list and a process sketch—were insufficient in directing the Repcon workers to the intended pipe opening location.”[1]

The pre-event physical identification state likewise contained a decisive defect. On October 8, 2024, operators prepared ARU6 and hung tags for the blinds. For Blind 407, which could not be easily accessed, they put the tag “on a nearby railing,” rather than directly on the blind.[1] CSB later concluded that the tag was out of sight and that the inconsistent, uncontrolled blind-tag system did not clearly indicate the equipment to open; the boilermakers instead used a misplaced flange-locking device on ARU7.[1]

CSB further found that PEMEX Deer Park had no clearly defined Run-and-Maintain system to identify equipment for opening. In the absence of such a system, the Repcon boilermakers chose flanges where they saw flange-locking devices, and an unlocked device on ARU7 led them to select the active line believing it was Blind 407.[1]

### 3. Reporting/communication and minimum holders

At 8:18 a.m. on October 10, a PEMEX Deer Park operator issued the blind-removal permit. The operator gave the previously developed blind list and drawing to the Repcon day-shift foreman, then escorted that foreman and four day-shift boilermakers through the unit to show the indicated blinds.[1] This supports `signal_reported=yes` and, conservatively, distinct PEMEX operations and Repcon-foreman holders.

The permit also recorded differential hazard information: the last two, acid-gas blinds required supplied-air respirators because of the risk of acid-gas backflow or leak-by; it stated that a PEMEX Deer Park operator would be present for line breaks.[1] CSB observes that the permit recognized the different hazards and specified “Ops present for each break.”[1]

### 4. Why the join is coded **no** under the strict assignment rule

The permit did not create a defined integrator with an unambiguous stop authority across the relevant holders. CSB reports that the permit language “Ops present for each break” was ineffective as a hold/stop point: the permit issuer, permit receiver, and boilermakers recalled/understood the requirement differently. Its conclusion is that the permit “lacked a defined hold or stop point,” and consequently the boilermakers opened an active hydrogen-sulfide line without the operator present.[1]

The contractor-management record supplies affirmative evidence of the resulting distributed fragments. The foreman acknowledged that PEMEX Deer Park communicated the Amine Unit’s status to him, but the boilermakers did not receive it. Under company policy, the foreman was *expected to relay* the information to the crew.[1] CSB’s conclusion is that PEMEX Deer Park and Repcon “did not sufficiently communicate” the move from a shutdown turnaround unit to an active unit or the Run-and-Maintain requirements.[1]

The broader simultaneous-operations process does not cure this under the codebook’s test. The procedure nominally put several people—the equipment owner, permit issuer, permit cosigner, and permit receiver—under responsibility to identify/manage risk to other processes and document it on a SIMOPs form, but the form gave no evaluation/mitigation guidance.[1] No form was completed; CSB found operators generally viewed SIMOPs as a checkbox and had no guidance on performing the evaluation.[1] These are distributed, inadequately structured responsibilities, not evidence of one named role/function with both responsibility and authority to aggregate the operative identification, active-unit-status, and contractor-information fragments. An operator’s responsibility to attend an individual line break is not treated as a qualifying join because the codebook explicitly excludes ownership of one inspection or task alone.

### 5. Lead time and suddenness

The report establishes that the signal state existed before the event, but not when PEMEX Deer Park adopted, recognized, or first observed the ineffective Run-and-Maintain identification system. It therefore cannot establish a numeric lower or upper lead-time bound for the *earliest* signal. The dated October 8 tag placement is a later manifestation, not evidence dating the onset of the system deficiency.[1]

For suddenness, the executive summary calls the reassignment an “abrupt shift in the work environment,”[1] but this does not label the release, failure, or warning pattern as sudden or unforeseeable. No qualifying official event-level suddenness wording was located in the final report.

## Limitations and uncertainty treatment

1. **Undated earliest condition.** The report richly documents the deficient identification/permit system but does not date its inception or first internal recognition. Accordingly, `first_signal_date=unknown`, minimum lead time is conservatively `0`, and maximum lead time is open/unknown (`lead_time_max_known=false`, `0`). The October 8 tag placement should not be mistaken for the first date of the broader signal.
2. **Holder count is a minimum, not a census.** The evidence securely supports two distinct role-side holders (PEMEX operations and the Repcon foreman). The report also names boilermakers and multiple operators, but this record does not turn those references into an exact people count.
3. **Join decision is functional and strict.** The report describes nominal permit, foreman-handoff, and SIMOPs duties, but it does not show a named role/function with demonstrated responsibility **and authority** to aggregate all relevant cross-holder information before the work continued. The `no` code rests on affirmative findings of an undefined hold point, divergent understandings, and inadequate communication; it does not claim there were no procedures at all.
4. **No suddenness inference.** “Abrupt” is retained only as a description of reassignment. It is not extended to an event-level suddenness label.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery — CSB Investigation Report No. 2024-05-I-TX, February 2026"

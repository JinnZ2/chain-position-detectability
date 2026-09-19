# WO-2 evidence record — U.S. Steel Clairton

## Case and coding outcome

| Field | Coder A value |
| --- | --- |
| Case ID | `us-steel-clairton` |
| Incident | United States Steel Corporation Clairton Plant Coke Oven Explosion |
| Event date | `2025-08-11` |
| Official final report | *Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works* (CSB Investigation Report No. 2025-03-I-PA; published August 2026) [1] |
| `signal_present` | **yes** |
| `signal_reported` | **yes** |
| `holder_count_known` | **false** |
| `holder_count_min` | **2** |
| `join_assigned` | **unclear** |
| `first_signal_date` | **2003** |
| `lead_time_days_min` | **7,894** |
| `lead_time_max_known` | **false** |
| `lead_time_days_max` | **0** |
| `sudden_label` | **yes** |
| `pattern_result` | **indeterminate** |

## Incident and applicable hazard mechanism

The CSB determined that the incident resulted from overpressurizing a cast-iron, double-disc gate valve while U.S. Steel and MPW washed it with high-pressure water. When the gates were fully closed, water pressurized the enclosed space between them; the valve then failed, released flammable coke oven gas, and the gas ignited and exploded. The CSB identified the lack of a safe valve-washing procedure and failure to identify or address operational hazards as contributing factors (printed p. 65). [1]

The earliest relevant pre-event signal is the 2003 process-hazards-analysis (PHA) team’s recommendation that site management conduct a facility-siting study of the coke batteries. The CSB explicitly concludes that this recommendation presented a key opportunity to address the facility-siting risks that increased the incident’s severity (printed pp. 48–49, 63–64). [1] The established high-pressure water washing practice is a later, separate signal directly connected to the initiating overpressurization mechanism.

## Basis for each field

### `signal_present = yes`

U.S. Steel’s 2003 PHA team made a written recommendation to site management to conduct a facility-siting study of the coke batteries. The report directly connects the recommendation to the site’s facility-siting hazard: routinely occupied, non-blast-resistant buildings stood less than 20 feet above hazardous coke-oven-gas piping; their failure caused the two deaths and two serious injuries (printed pp. 48–49, 63–64). [1]

> “U.S. Steel’s 2003 PHA team issued a recommendation to site management to conduct a facility siting study of the coke batteries, but Clairton management rejected the recommendation.” — CSB, printed p. 48 [1]

This is a documented pre-event analysis result connected by the CSB to the hazard pathway that made the event fatal. It is not inferred from general background knowledge or temporal precedence. The later water-washing signal independently supports that workers also performed an unproceduralized practice directly connected to the initiating overpressurization (printed pp. 37–39, 65). [1]

### `signal_reported = yes`

The PHA recommendation was communicated to **site management**, which rejected it. The report quotes Clairton management’s written rationale for rejecting the recommendation (printed p. 48). [1] This formal PHA recommendation and management decision constitute recorded communication beyond private awareness.

> “Accordingly, elements of PSM are selectively applied to this system as deemed necessary and appropriate by Clairton Works management. … management does not consider it necessary to conduct the activities as recommended[.]” — Clairton management, quoted by CSB, printed p. 48 [1]

The additional water-washing signal also was recorded in the battery-isolation procedure, which Clairton management approved and implemented, indicating management knowledge and endorsement (printed p. 37). [1]

### `holder_count_known = false`; `holder_count_min = 2`

A conservative minimum of two distinct organizational-role holders is supported:

1. The **2003 PHA team** held and generated the facility-siting-study recommendation (printed p. 48). [1]
2. **Site/Clairton management** received and rejected that recommendation (printed p. 48). [1]

The record also identifies U.S. Steel operators, MPW, and Clairton management as holders of fragments concerning the later water-washing practice (printed pp. 19, 37, 39, 59), but those additional holders are not needed for the lower bound. [1] The report does not enumerate all pre-event holders or establish a complete count; consequently the count is not known.

### `join_assigned = unclear`

The report documents a PHA recommendation and a managerial decision, but does not identify a named role or function that had **both** responsibility and authority to aggregate the PHA’s finding with other relevant cross-holder signals and act before the event.

Although site management had authority to reject the PHA recommendation, the report does not say that it had an assigned responsibility to aggregate relevant fragments. The later planned Hazardous Job Meeting (HJM) likewise did not include valve washing/exercising, and none of the August 11 washing/exercising personnel attended (printed pp. 23–24). [1] The CSB further found that the company’s systems enabled a U.S. Steel supervisor to arrange and direct the washing operation without prior planning, a procedure, training, work permit, or sufficient hazard analysis/mitigation (printed p. 60). [1]

These passages do not establish that a designated integration function was assigned both responsibility and authority to combine the relevant cross-holder fragments. Nor do they affirmatively establish that no such function existed. Under the codebook’s strict rule, the value is therefore **unclear**, not `no`.

### Signal date and lead time

The report gives the earliest selected signal only to year precision: **2003**. The record preserves that precision rather than inventing a date. Taking December 31, 2003—the latest possible date in the stated year—through August 11, 2025 gives a conservative lower bound of **7,894 days**. The report does not give a day in 2003 or a bounded range. Thus `lead_time_max_known = false`; the required numeric `lead_time_days_max` is recorded as **0** to represent the open/unknown maximum, not as a substantive zero-day lead time.

### `sudden_label = yes`

The official report describes the physical valve failure as “visually consistent with **sudden, brittle fracture**” (printed p. 29). [1] This is an official characterization of the failure, so the field is `yes`.

### `pattern_result = indeterminate`

The case satisfies three necessary elements: a relevant pre-event signal was present and reported, and a conservative minimum of two distinct holders is supported. However, `join_assigned` remains unresolved under the named-role/function, responsibility-and-authority rule. The prescribed result is therefore **indeterminate**, rather than `supports` or `does_not_support`.

## Decisive evidence excerpts and locations

| Evidence | Why it matters |
| --- | --- |
| The 2003 PHA team recommended a coke-battery facility-siting study; site management rejected the recommendation (printed p. 48). [1] | Establishes the earliest case-specific, pre-event signal, reporting to management, and two distinct role-level holders. |
| The CSB concludes that the 2003 recommendation and 2010 explosion were key opportunities to address facility-siting risks, but neither prompted action (printed p. 49); it reiterates the finding at printed pp. 63–64. [1] | Directly connects the 2003 signal to the hazard pathway that increased the fatal and serious-injury severity in the investigated event. |
| Water washing had been used for at least three years before the event and was never proceduralized (printed p. 37). [1] | A later, independent pre-event signal tied directly to the initiating valve-overpressurization mechanism. |
| The intended HJM plan did not include exercising, steaming, or washing the valve; none of the August 11 washing/exercising personnel attended (printed pp. 23–24). [1] | Shows that the identified formal planning activity did not integrate this operation. |
| Management systems enabled a supervisor to arrange/direct the operation without prior planning, procedure, training, permit, or sufficient hazard analysis/mitigation (printed p. 60). [1] | Supports uncertainty—not a demonstrated, assigned cross-holder integration function. |
| The causal statement identifies high-pressure-water overpressurization and the lack of a safe procedure/hazard identification as causal/contributing (printed p. 65). [1] | Connects the pre-event water-washing practice to the official incident mechanism. |
| The fracture was “consistent with sudden, brittle fracture” (printed p. 29). [1] | Supplies the required official sudden-equivalent language. |

## Limitations

The CSB gives the selected earliest PHA signal only to year precision: 2003. The 7,894-day minimum deliberately assumes the latest possible 2003 date, and the report gives no lower bound for the actual date within the year; the maximum is therefore open. The report identifies a PHA team and a site-management rejection but does not name a role or function assigned both responsibility and authority to aggregate all relevant cross-holder signals. The HJM documentation does not cure that gap because the later water-washing operation was outside its documented scope. No conclusion that there was *no* integration point is made from this absence of evidence.

The record distinguishes two CSB-identified pathways. The 2003 PHA recommendation is selected because the report directly connects it to the facility-siting risk that made the event fatal and seriously injurious. The later water-washing practice concerns the initiating valve-overpressurization mechanism. Both are case-specific official signals, but the former supplies the earliest supported date.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6340 "Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works — CSB Investigation Report No. 2025-03-I-PA, August 2026"

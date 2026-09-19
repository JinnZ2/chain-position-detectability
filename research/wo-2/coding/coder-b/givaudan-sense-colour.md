# Coder B evidence record — Givaudan Sense Colour Explosion

## Case and coding conclusion

This record independently codes the **Givaudan Sense Colour Explosion** investigated by the U.S. Chemical Safety and Hazard Investigation Board (CSB). The event occurred in Louisville, Kentucky, on **2024-11-12**. It is based only on the official final investigation report cited in the References section. Printed-page locations below are those printed in the report, rather than viewer page counts.

| Field | Code |
| --- | --- |
| `case_id` | `givaudan-sense-colour` |
| `coder` | `B` |
| `title` | `Givaudan Sense Colour Explosion` |
| `event_date` | `2024-11-12` |
| `report_url` | `https://www.csb.gov/file.aspx?DocumentId=6324` |
| `signal_present` | `yes` |
| `signal_reported` | `yes` |
| `holder_count_known` | `false` |
| `holder_count_min` | `2` |
| `join_assigned` | `no` |
| `first_signal_date` | `2012-10-15` |
| `lead_time_days_min` | `4411` |
| `lead_time_max_known` | `true` |
| `lead_time_days_max` | `4411` |
| `sudden_label` | `yes` |
| `pattern_result` | `supports` |

**Conclusion.** The evidence supports the WO-2 pattern. An official, hazard-relevant pre-event signal was recorded on 2012-10-15; it was passed from D.D. Williamson to an outside consultant and used to alter relief systems. At least those two organizational holders are documented. The report affirmatively finds that no process-safety-policy owner was assigned with the required oversight and accountability, and connects that missing ownership to the later Reactor 6 design team’s lack of the test and relief-system information. The earlier signal precedes the 2024 event by exactly 4,411 calendar days. [1]

## Incident chronology and causal analysis

The CSB determined that on 2024-11-12 the Reactor 6 vent valve failed closed. The blockage produced abnormal temperature and pressure, accelerated an exothermic sugar-decomposition reaction, and generated more heat and carbon dioxide. The installed emergency relief system could not adequately relieve the resulting pressure, which rose until the reactor ruptured. The report identifies the cause as high pressure from accelerated sugar decomposition that could not be adequately relieved because the emergency relief system was undersized; it identifies process-safety implementation deficiencies and resulting loss of institutional knowledge as contributors (printed pp. 36, 78). [1]

The event’s immediate warnings were documented rather than absent. At 2:39 p.m. the vent valve failed in the closed position; at 2:52 p.m. the control-room Reactor 6 icon turned red for adverse conditions and the operator acknowledged it; at 2:54 p.m. a maintenance technician tried to open the valve; at 2:55 p.m. pressure exceeded the 75-psig maximum allowable working pressure; and at 2:57:41 p.m. Reactor 6 catastrophically failed (printed p. 89). The narrative likewise records that operators saw abnormal pressure and temperature, that the maintenance technician had been made aware of the condition, and that the valve remained closed despite a command to open (printed p. 29). [1]

## Decisive evidence for each code

### A pre-event signal was present and was relevant to the causal hazard

The earliest defensible signal is **2012-10-15**, the dated timeline entry for D.D. Williamson’s Product 034 reactivity test. The test showed a self-sustained temperature rise and significant pressure rise from non-condensable gases (printed p. 88). The report gives the underlying result more specifically:

> “When heated in an enclosed container, the Product 034 ingredients experienced a large temperature increase due to an exothermic chemical reaction (exotherm), as well as a significant pressure rise due to the formation of non-condensable gases.” (printed p. 26) [1]

This is not treated as merely an earlier, superficially similar observation. The official report directly connects it to the investigated hazard mechanism: the post-incident Product 484 and sugar-only tests “exhibited similar behavior” to the 2012 tests (printed p. 26), and Finding 8 states that further analysis of the 2012 results could have identified self-heating and decomposition of Product 034’s sugar ingredient, led the company to recognize similar reactivity potential in other caramel-coloring products, and supported a Reactor 6 relief system designed for the sugar-decomposition scenario (printed p. 76). These passages satisfy the requirement for an official connection between the signal and the hazard mechanism.

Accordingly, `signal_present = yes` and `first_signal_date = 2012-10-15`.

### The signal was communicated or recorded beyond a private holder

The test result was communicated beyond the organization that produced it. The report says D.D. Williamson “provided the 2012 test results to an outside consultant,” who determined that larger relief systems were needed for reactors producing Product 034. In response, D.D. Williamson enlarged Reactor 3 and 4 relief systems in 2013 (printed p. 26). The timeline independently records the 2012 test, the consultant’s relief-sizing analysis, and the 2013 installation of the increased-area valves (printed p. 88). [1]

This is affirmative evidence of both a record and a cross-organization communication. Therefore, `signal_reported = yes`.

### At least two relevant holders are documented, but their full number is not

The conservative lower bound is two organizational holders: **D.D. Williamson**, which conducted and provided the 2012 results, and the **outside consultant**, which received those results and used them to determine the needed relief-system increase (printed p. 26). [1] The report does not enumerate every individual, team, or later record holder with sufficient precision to establish an exact total. Thus, `holder_count_min = 2` and `holder_count_known = false`.

The record does not add day-of-incident operators and the maintenance technician to this count. They held later operational-warning information, but they are not needed to establish the conservative cross-holder minimum for the dated historical signal used to calculate lead time.

### No qualifying aggregation function was assigned

The report contains affirmative evidence against an assigned join. It states that under both owners the Louisville facility did not sufficiently assign or train an employee “to have oversight responsibility and be accountable” for implementation of its process-safety policies. The Environmental Health and Safety Management System Manual required annual Hazard Identification and Risk Assessments, but “there was no one assigned to oversee that element”; the report adds that an effective system must be overseen by competent persons with authority and knowledge (printed p. 61). [1]

The CSB’s conclusion directly ties this missing owner to the relevant distributed information: the lack of an owner contributed to inconsistent MOC reviews, action-item implementation, and process-hazard evaluations, and directly contributed to the Reactor 5/6 design personnel being unaware of the 2012 test results and Reactor 3/4 relief-sizing increases (printed p. 61). The earlier MOC record did not cure this: the action to update the Reactor 3 HAZOP was not implemented, Reactor 4’s relief change had no MOC analysis, and the result was limited documentation (printed pp. 57–58). [1]

No named role or function is documented as having both responsibility and authority to aggregate the reactivity results, relief-sizing changes, MOC records, and later Reactor 6 design information. To the contrary, the CSB finds the pertinent ownership absent. Therefore, `join_assigned = no`.

### Lead time

The report gives exact dates for both endpoints: the Product 034 test on **2012-10-15** (printed p. 88) and the Reactor 6 rupture on **2024-11-12** (printed p. 89). [1] The calendar-date difference is exactly **4,411 days**. Since neither endpoint is an interval or open date, both defensible minimum and maximum are 4,411: `lead_time_days_min = 4411`, `lead_time_max_known = true`, and `lead_time_days_max = 4411`.

### Official rapid/sudden characterization

The report does not use the literal word “sudden” for the 2024 event. It does officially characterize the event as a “runaway (uncontrolled) reaction resulting in a **rapid** temperature and pressure rise” (printed p. 27), and says the pressure rise “rapid[ly]” ruptured the reactor (printed p. 40). [1] This is a close equivalent of the codebook’s sudden-event language, so `sudden_label = yes`.

### Pattern determination

`pattern_result = supports` because all required elements are resolved positively: a hazard-relevant signal was present; it was communicated; at least two holders are documented; and the source affirmatively finds no qualifying process-safety owner/aggregation point. The CSB’s causal analysis also directly links the missing ownership and loss of the 2012 information to the undersized Reactor 6 relief system and eventual incident (printed pp. 61, 78). [1]

## Limitations and uncertainty handling

The Product 034 test did not identify the reacting component at the time. The final report nevertheless supplies the required official linkage to the later hazard: it says post-incident Product 484 and sugar-only testing exhibited similar behavior and expressly finds that further analysis of the 2012 result could have revealed sugar decomposition and informed prevention of the 2024 event (printed pp. 26, 76). The coding does not infer that connection from timing or engineering resemblance alone. [1]

The report describes an April 2003 caramel-coloring vessel explosion, including overheating and a likely closed vent (printed p. 24), but it does not attribute that earlier event itself to the 2024 sugar-decomposition mechanism. It is therefore not used as the earliest signal. This preserves the codebook rule against treating merely earlier or similar events as mechanism-relevant without an official source connection. [1]

The count of two is a minimum rather than an exact census. The source documents D.D. Williamson and the outside consultant but does not identify all individuals and organizational units that later possessed relevant fragments. `holder_count_known` is consequently false, not an assertion that only two holders existed. [1]

The `sudden_label` rests on the report’s phrase “rapid temperature and pressure rise,” treated as a close equivalent; the report does not literally say “sudden,” “unexpected,” or “without warning.” The documented day-of-event control-room warning and attempts to respond also mean the label does not imply the incident was unwarned. [1]

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6324 "U.S. Chemical Safety and Hazard Investigation Board, Givaudan Sense Colour Explosion Investigation Report"

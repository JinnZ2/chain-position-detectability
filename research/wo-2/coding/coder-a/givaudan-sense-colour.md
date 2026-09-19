# WO-2 evidence record — Givaudan Sense Colour Explosion

## Case and source

| Field | Value |
| --- | --- |
| Case ID | `givaudan-sense-colour` |
| Coder | A |
| Event | Givaudan Sense Colour / D.D. Williamson, Louisville, Kentucky — Reactor 6 explosion |
| Event date | 2024-11-12 |
| Final-report publication | May 2026 (case manifest gives 2026-05-27) |
| Scope | One official CSB final investigation report; no secondary sources used for any code |

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6324 "Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson — CSB Investigation Report No. 2024-06-I-KY, May 2026"

## Incident chronology and causal frame

The batch began normally at 10:22 a.m. on November 12, 2024. The CSB determines that at 2:39 p.m. the vent valve moved closed without a PLC command; the PLC subsequently commanded it fully open but it did not open. Temperature and pressure continued to rise despite automated steam shutoff and cooling-water opening at 2:47 p.m. [1]. Operators saw the abnormal pressure and temperature in the control room; a maintenance technician, informed of the abnormal conditions, attempted to manually open the valve at 2:53–2:54 p.m. but could not move it [1]. The timeline records a red control-room icon at 2:52 p.m., pressure above the 75-psig safe limit at 2:55 p.m., temperature above the 355°F safe limit at 2:56 p.m., and the catastrophic failure at 2:57:41 p.m. [1].

The official causal finding controls the relevance assessment. The CSB finds that a sugar ingredient underwent an uncontrolled exothermic decomposition reaction, producing high temperature and pressure and rupturing Reactor 6; it also finds that the closed vent valve removed an important heat-control mechanism 18 minutes before rupture [1]. The CSB’s stated cause is high pressure from accelerated sugar decomposition that the undersized relief system could not adequately relieve; the undersizing resulted from management’s fundamental lack of understanding of the sugar-reaction hazard [1].

## Pre-event signal, prior history, and communication evidence

### Qualifying earliest signal used for this code

The first qualifying case-specific signal is **2012-10-15**, when D.D. Williamson’s testing of Product 034 ingredients showed “a self-sustained temperature rise (exotherm), as well as a significant pressure rise due to the formation of non-condensable gases” [1]. The body of the report likewise describes a large temperature increase from an exothermic reaction and a significant pressure increase from non-condensable gas formation [1].

This is directionally related to the official mechanism, not merely a temporal antecedent. The CSB concludes that further analysis of this 2012 result, and additional reactivity tests, could have shown that Product 034’s sugar ingredient was self-heating and decomposing to generate the gases, that many of the company’s caramel-color sugar ingredients could have similar reactivity potential, and that such knowledge could have led to Reactor 6 relief design changes that prevented the 2024 event [1]. Its final findings repeat that connection: additional analysis of the 2012 result could have led to discovery of the sugar-ingredient decomposition mechanism and equipment changes, including Reactor 6 relief specifically designed for that scenario [1].

The result was communicated beyond private awareness. The report states that D.D. Williamson **provided the 2012 test results to an outside consultant**; that consultant determined that the Product-034 reactors needed larger relief systems, and the company enlarged the relief systems of Reactors 3 and 4 in 2013 [1]. This directly establishes at least two distinct documented organizational holders of relevant information: **D.D. Williamson** and the **outside consultant**. It also establishes a pre-event record/communication, not merely a later reconstruction.

### Why earlier history is not used to move the first-signal date

The report documents a 2003 fatal caramel-color vessel rupture and a 2008 HAZOP. The 2008 HAZOP considered high-pressure deviations and listed failures such as a blocked vent valve or relief-valve failure, but expressly states that sugar decomposition had **not** been identified as a high-pressure cause [1]. The 2003 narrative describes a likely closed air vent during heating but does not identify the 2024 sugar-decomposition mechanism [1]. Under the rule against inferring relevance without the report’s mechanism connection, these earlier materials are treated as important background rather than an earlier qualifying signal. The 2012 test is the earliest dated observation in this report that the CSB explicitly connects to the sugar-decomposition hazard and the Reactor 6 design outcome.

## Organizational aggregation / ownership evidence

There was no assigned integration point meeting the codebook’s responsibility-and-authority test. The CSB reports that, under both D.D. Williamson and Givaudan, the Louisville facility “did not sufficiently assign or train an employee to have oversight responsibility and be accountable for the implementation of (i.e., ‘to own’) the process safety policies”; while its manual required annual Hazard Identification and Risk Assessments, “there was no one assigned to oversee that element” [1]. The same section says a successful system must be overseen by competent person(s) with authority and knowledge to carry out the assigned duties [1].

This absence directly affected the fragments at issue: the CSB concludes that the lack of a process-safety-policy owner led to inconsistent MOC reviews, action-item implementation, and hazard evaluations, and that the lack of leadership directly contributed to the Reactor 5/6 design personnel being unaware of the 2012 reactivity results and the Reactor 3/4 relief-size increases [1]. The conclusion also records that inadequate MOC documentation meant the Reactor 6 design team was unaware of the 2012 results and relief-size differences [1]. Thus this is affirmative evidence of **no** named function with responsibility and authority to aggregate the relevant information, rather than an inference from a bad outcome.

## Coding decision

| Variable | Code | Decision basis |
| --- | --- | --- |
| `signal_present` | **yes** | The dated 2012 reactivity test observed a self-sustained exotherm and significant gas-driven pressure rise [1]. CSB connects further analysis of that result to discovery of sugar decomposition and prevention-oriented Reactor 6 relief design [1]. |
| `signal_reported` | **yes** | D.D. Williamson provided the results to an outside consultant, which resulted in the consultant’s relief-sizing determination and subsequent relief changes for Reactors 3 and 4 [1]. |
| `holder_count_known` | **false** | The report supports a conservative minimum but does not enumerate every individual/role holding the relevant information. |
| `holder_count_min` | **2** | D.D. Williamson and the outside consultant are separate documented organizational holders of the 2012 results [1]. No unverified design-team member is counted as a holder because the report says that team was unaware [1]. |
| `join_assigned` | **no** | CSB explicitly found no adequately assigned/trained employee accountable to own process-safety-policy implementation, and no one assigned to oversee the annual hazard-assessment element [1]. The unowned functions are the MOC/hazard-evaluation mechanisms that should have carried the 2012 information to the Reactor 6 design [1]. |
| `first_signal_date` | **2012-10-15** | Exact testing date in the official timeline [1]. |
| `event_date` | **2024-11-12** | Report title and timeline [1]. |
| `lead_time_days_min` | **4,411** | Exact calendar-day difference from 2012-10-15 to 2024-11-12. |
| `lead_time_max_known` | **true** | Both endpoints are exact calendar dates; therefore the defensible interval is exact, not open-ended. |
| `lead_time_days_max` | **4,411** | Same exact interval. |
| `sudden_label` | **yes** | The CSB characterizes the incident batch as a “runaway (uncontrolled) reaction resulting in a **rapid temperature and pressure rise**” [1], and describes temperature and pressure increasing “at a rapid rate” after the vent-valve failure [1]. “Rapid” is used here as the report’s close equivalent of a sudden failure progression; it is not coded from an absence-of-warning assumption. |
| `pattern_result` | **supports** | All required conditions are evidenced: signal present = yes; signal reported = yes; minimum distinct holders = 2; and no assigned aggregation owner = no. |

## Decisive evidence excerpts / tight paraphrases

1. **Signal and date:** “10/15/2012 … Testing shows Product 034 ingredients experience a self-sustained temperature rise (exotherm), as well as a significant pressure rise due to the formation of non-condensable gases” [1].
2. **Connection to the causal hazard:** The CSB says further analysis of that test could have identified self-heating/decomposition of the sugar ingredient and similar potential in other caramel-color sugar ingredients; it could have supported a Reactor 6 relief design for the sugar-decomposition scenario [1].
3. **Communication and holders:** “D.D. Williamson provided the 2012 test results to an outside consultant,” who determined the relevant reactors needed larger relief systems; Reactors 3 and 4 were enlarged in 2013 [1].
4. **Unowned join function:** Under both owners, no employee was sufficiently assigned/trained for oversight/accountability to “own” the process-safety policies, and no one was assigned to oversee annual hazard assessments [1].
5. **Consequence of the missing join:** Lack of that owner directly contributed to Reactor 5/6 design personnel being unaware of the 2012 results and earlier relief-size changes [1]; lack of documentation likewise contributed to the design team’s unawareness [1].
6. **Causal analysis:** The CSB identifies the cause as high pressure from accelerated sugar decomposition that the undersized relief system could not relieve [1].
7. **Rapid/sudden-progress label:** The report expressly calls the 2024 outcome a runaway reaction with a “rapid temperature and pressure rise” [1].

## Limitations and uncertainty treatment

* The 2012 test concerned Product 034, not the precise Product 484 batch. The code does not claim that staff had proven Product 484 would decompose; it codes the test as a directionally related signal because the final report itself makes the connection to sugar decomposition, similar potential across sugar ingredients, and potentially preventive Reactor 6 design changes [1].
* The report does not list all individual or functional holders of the result, so the count is an intentionally conservative organizational lower bound of two and `holder_count_known=false`.
* The record does not treat the 2003 rupture or 2008 HAZOP as earlier qualifying signals. Although relevant history, the report says the 2008 HAZOP did not identify sugar decomposition as a high-pressure cause [1], so using them as a signal of the final causal mechanism would require inference beyond the stated connection.
* The 4,411-day lead time is a date arithmetic interval, not proof that the signal’s full meaning or a feasible preventive action was understood for that entire period. The report says additional analysis would have been needed to identify the sugar mechanism [1].
* The `sudden_label=yes` decision rests only on the CSB’s “rapid temperature and pressure rise” characterization [1]. The report also documents observable escalating conditions and a short intervention/evacuation opportunity; it does not say personnel had no warning [1].

## Compact machine-readable handoff

```json
{
  "case_id": "givaudan-sense-colour",
  "coder": "A",
  "title": "Givaudan Sense Colour Explosion",
  "event_date": "2024-11-12",
  "report_url": "https://www.csb.gov/file.aspx?DocumentId=6324",
  "signal_present": "yes",
  "signal_reported": "yes",
  "holder_count_known": false,
  "holder_count_min": 2,
  "join_assigned": "no",
  "first_signal_date": "2012-10-15",
  "lead_time_days_min": 4411,
  "lead_time_max_known": true,
  "lead_time_days_max": 4411,
  "sudden_label": "yes",
  "pattern_result": "supports"
}
```

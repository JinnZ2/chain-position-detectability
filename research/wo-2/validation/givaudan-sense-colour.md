# Independent WO-2 validation — Givaudan Sense Colour Explosion

**Case ID:** `givaudan-sense-colour`
**Validation outcome:** **Valid — no change to the reconciled values.** The official final report supports every retained non-unclear value under the codebook, and the selected evidence forms one coherent **sugar-decomposition / relief-system-design / institutional-knowledge** pathway. This review opened and read the CSB-hosted final report directly.[1]

## Corrected record

| Field | Validated value | Basis |
| --- | --- | --- |
| `signal_present` | `yes` | The 2012 reactivity test recorded an exotherm and gas-driven pressure rise that CSB formally connects to the sugar-decomposition scenario that ruptured Reactor 6.[1] |
| `signal_reported` | `yes` | D.D. Williamson provided the results to an outside consultant.[1] |
| `holder_count_min` | `2` | At least D.D. Williamson and the outside consultant held the relevant 2012 reactivity/relief-sizing information.[1] |
| `holder_count_established` | `false` | This is a conservative lower bound, not a complete census of people, teams, or units holding relevant information. |
| `join_assigned` | `no` | CSB affirmatively identifies no accountable process-safety-policy owner and no assignee to oversee annual hazard identification and risk assessment; it directly links that absence to the Reactor 5/6 team’s lack of the 2012 information.[1] |
| `first_signal_date` | `2012-10-15` | Exact date in the official incident timeline.[1] |
| `event_date` | `2024-11-12` | Exact event date in the same official timeline.[1] |
| `lead_time_days_min` | `4411` | Exact calendar-day interval from 2012-10-15 to 2024-11-12. |
| `lead_time_max_known` | `true` | Both endpoints are exact dates, so the interval is exact. |
| `lead_time_days_max` | `4411` | Same exact interval. |
| `sudden_label` | `yes` | CSB applies the characterization to the incident reaction: “Product 484 ingredients experienced a runaway (uncontrolled) reaction resulting in a **rapid temperature and pressure rise**.”[1] This is event/failure-sequence language, not an alarm label or a generic adverb. |
| `pattern_result` | `supports` | All four codebook conditions are affirmatively established: present, reported, at least two holders, and no assigned responsible-and-authorized integrating function.[2] |

## Coherent hazard-pathway check

The coding uses **one pathway**, rather than combining the historical reactivity/design problem with the separate, immediate vent-valve/control-room-warning sequence:

> **15 October 2012 Product 034 reactivity test** → test results sent to an **outside consultant** → consultant’s relief-sizing determination and 2013 Reactor 3/4 relief changes → inadequate MOC/hazard-analysis knowledge retention and **no process-safety-policy owner** → Reactor 5/6 design personnel unaware of the 2012 results and relief differences → undersized Reactor 6 relief system → 2024 sugar-decomposition overpressure and rupture.[1]

The official report expressly supplies the otherwise necessary connection between Product 034 and the 2024 Product 484 event. It concludes that further analysis of the 2012 result could have discovered “the self-heating and decomposition of Product 034’s sugar ingredient,” identified similar reactivity potential in other caramel-color sugar ingredients, and led to a Reactor 6 relief system “specifically designed for the sugar decomposition reaction scenario.”[1] The causal finding states that the explosion resulted from accelerated decomposition of a sugar ingredient and an undersized relief system.[1]

The earlier 2003 event and 2008 HAZOP are **not** used to move the first-signal date. The report describes the 2003 event as overheating with a likely closed vent,[1] and explicitly says that the 2008 HAZOP had not identified sugar decomposition as a high-pressure cause.[1] They therefore do not displace the first official signal on the selected sugar-decomposition/design pathway.

## Decisive source quotations and locations

| Variable(s) | Exact official-report quotation | Location and validation reading |
| --- | --- | --- |
| Signal; reporting; two-holder minimum | “D.D. Williamson provided the 2012 test results to an outside consultant, who determined that the reactors used to produce Product 034 needed larger relief systems to relieve the pressure and gases that could form from the observed reaction.” | [1]. This is a documented pre-event transmission, not private awareness; the sending organization and the outside consultant establish two distinct organizational holders. |
| Signal date | “10/15/2012 … Testing shows Product 034 ingredients experience a self-sustained temperature rise (exotherm), as well as a significant pressure rise due to the formation of non-condensable gases.” | [1]. Exact date; this is the earliest report-supported signal on the selected pathway. |
| Hazard relevance | “This discovery could have led the company to realize that many of its caramel coloring products’ sugar ingredients could have similar reactivity potential. This, in turn, could have led the company to implement equipment design changes that could have prevented the 2024 incident, including equipping Reactor 6 with an emergency pressure relief system specifically designed for the sugar decomposition reaction scenario.” | [1]. This direct CSB connection satisfies the codebook’s causal-relevance requirement. |
| Absent join | “Under both D.D. Williamson’s and Givaudan’s ownership, the Louisville facility did not sufficiently assign or train an employee to have oversight responsibility and be accountable for the implementation of (i.e., ‘to own’) the process safety policies.” | [1]. This is affirmative absence evidence, rather than an inference from a missing procedure. |
| Absent join; pathway link | “While the facility’s Environmental Health and Safety Management System Manual required Hazard Identification and Risk Assessments to be conducted each year, there was no one assigned to oversee that element” and “[t]he lack of strong company leadership … directly contributed to personnel involved in the Reactor 5 and Reactor 6 design being unaware of the 2012 chemical reactivity testing results … and … relief system sizing increases.” | [1]. The report identifies both no assignment and the precise cross-time information failure. No merely local task owner is counted as a cross-holder join. |
| Event date and endpoint | “11/12/2024 … 2:57:41 p.m. Catastrophic failure of Reactor 6.” | [1]. Together with the exact 2012 date, this fixes the 4,411-day interval. |
| Sudden characterization | “In November 2024, Reactor 6 overpressured and ruptured when Product 484 ingredients experienced a runaway (uncontrolled) reaction resulting in a rapid temperature and pressure rise.” | [1]. The wording characterizes the investigated event’s relevant failure progression. |

## Validation conclusion

`join_assigned = no` is retained only because the report itself affirmatively establishes the lack of an accountable oversight/ownership function **and** ties that lack to the 2012-results/2021-design information gap. It is not inferred from the absence of a procedure, nor is the consultant or any local activity owner treated as an integrating role. The historical test, its report to the consultant, the information-retention failure, the first date, and lead time all remain within the same report-identified hazard pathway. The reconciled case therefore remains `supports`.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6324 "Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson — CSB Investigation Report No. 2024-06-I-KY, May 2026"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/codebook.md "WO-2 pilot codebook"

[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-2/source-manifest.md "WO-2 source manifest"

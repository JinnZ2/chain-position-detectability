# WO-2 evidence record — TS USA Molten Salt Eruption

## Case and source

| Field | Value |
| --- | --- |
| Case ID | `ts-usa` |
| Coder | **B** |
| Title | *TS USA Molten Salt Eruption* |
| Event date | 2024-05-30 |
| Final-report publication date | 2025-06-03 |
| Official final report | [CSB, *TS USA Molten Salt Eruption*, Investigation Report][1] |
| Scope of review | The official final report, including incident chronology (pp. 18–24 and Appendix B), technical analysis (pp. 25–27), safety issues (pp. 28–52), findings/cause (pp. 53–56), and recommendations (pp. 57–59). All page citations below are printed report pages; PDF pages carry the same page number for the cited substantive pages. |

## Coding decision

| Variable | Code | Decisive basis |
| --- | --- | --- |
| `signal_present` | **yes** | The January 2018 TS ETSA/Mexico explosion is a documented pre-event signal that the CSB explicitly connects to the 2024 hazard mechanism: TS ETSA concluded that a part “with an **accumulation hazard** was allowed to be processed in the liquid nitriding line,” and the CSB later found that the 2018, 2020, and 2023 incidents show that parts which trap materials in cavities lead to **overpressure explosions** when introduced to salt baths ([1], pp. 43, 47). The same report identifies the 2024 cause as water in the roller cavity entering the 800°F oxidizing bath, causing overpressure, steam explosion, and molten-salt eruption ([1], p. 56). |
| `signal_reported` | **yes** | TS ETSA investigated the 2018 event and developed a formal report with the incident, causal factors, and corrective actions; a less detailed English report was translated and “presented to HEF Groupe” ([1], p. 43). This is documented recording and communication beyond a private holder. |
| `holder_count_known` | **true** |
| `holder_count_min` | **2** | Conservative minimum of two organizational holders is directly supported: (1) **TS ETSA**, which investigated the 2018 event and developed the formal report, and (2) **HEF Groupe**, to which an English report was presented and which the CSB says was aware the incident had occurred ([1], pp. 43–44). This is a lower bound, not a claim that all holders are identified. |
| `join_assigned` | **no** | The report affirmatively describes the absence of an organizational integration mechanism, not merely a missing description. It concludes that HEF Groupe “did not manage safety knowledge throughout the company” and did not ensure subsidiaries received developed safety information or that it was transferred and managed ([1], pp. 50–51; see also p. 55). It further states that neither TS USA nor HEF USA employed safety professionals at individual facilities; HEF Groupe instead relied on regional and plant management, and the line operator was responsible for the shift’s quality, safety, and productivity ([1], p. 52). The CSB says leadership had not assigned safety resources and responsibilities to dedicated roles ([1], pp. 52, 56). Thus, although specific operational roles participated in the 2024 decision, the source provides affirmative evidence that no named role/function had both responsibility and authority to aggregate prior-incident knowledge and the pertinent cross-holder hazard signals across the organization. |
| `first_signal_date` | **2018-01-25** | “On January 25, 2018, an explosion occurred” at the TS ETSA facility in Mexico ([1], p. 42). The report’s later causal synthesis supplies the required official connection between that incident type and the 2024 accumulation/overpressure mechanism ([1], pp. 47, 56). |
| `event_date` | **2024-05-30** | Appendix B records the explosion and oxidizer-salt eruption at 08:58 on May 30, 2024 ([1], p. 65). |
| `lead_time_days_min` | **2317** | Calendar-day difference from 2018-01-25 to 2024-05-30 is 2,317 days. Both endpoints are stated as ISO calendar dates in the report; no time-of-day precision is imputed for the 2018 event. |
| `lead_time_max_known` | **true** |
| `lead_time_days_max` | **2317** | The earliest signal and event are each stated to a calendar date, producing the same bounded calendar-day interval for this record. |
| `sudden_label` | **yes** | The CSB characterizes the failure sequence as rapid: retained water “rapidly expanded as steam,” and the water “rapidly boiled, creating a violent steam explosion” that drove the uncontrolled molten-salt eruption ([1], p. 27; reiterated in finding 4, p. 53). This is an official close equivalent to a sudden failure characterization. |
| `pattern_result` | **supports** | All rule-required elements are satisfied: relevant pre-event signal present and reported; conservative holder minimum is 2; and the report provides affirmative evidence of no assigned cross-holder safety-knowledge integration function. |

## Evidence narrative

### 1. Mechanism and incident chronology

The CSB determined that the 2024 incident resulted when water retained in a roller cavity was introduced into the 800°F oxidizing salt bath. The water expanded and boiled in the cavity, producing overpressure, a steam explosion, and molten-salt eruption ([1], p. 56). In the immediate chronology, a line operator removed rollers from the 160–180°F rinse bath at 07:09 on May 30. Water could not drain from one roller because a solidified salt plug blocked the hole ([1], pp. 20–21). The plant manager and supervisor observed a roller too hot to touch, saw water draining, believed the drain hole was clogged, and unsuccessfully tried to clear it with wire. The report states that this allowed water to remain in the cavity ([1], p. 21). The plant manager then contacted the process engineer for guidance; the engineer recommended reintroducing the rollers into the oxidizing bath. At 08:58 the chemical mixture erupted ([1], p. 22; Appendix B, p. 65).

These immediate observations independently document a site-level hazard signal and its communication among the plant manager, supervisor, process engineer, and line operator. They are not needed to establish the earliest signal or the conservative two-holder lower bound above, but they corroborate that the operative failure mechanism was visible before the event. The CSB’s cause finding, rather than inference from temporal order, is the basis for treating retained water/accumulation as relevant.

### 2. Earliest relevant pre-event signal and reporting

The earliest identified signal is the **January 25, 2018 Mexico explosion**. The final report explains that the roller there admitted water during rinsing, was preheated, and then underwent an explosion; its subsequent discussion identifies the cause as permitting a part with an accumulation hazard into the liquid nitriding line ([1], pp. 42–43). The report does not rely on an assumed similarity alone: it expressly concludes that the Mexico, France, and Chattanooga precursor events demonstrated that cavity accumulation traps material and causes overpressure explosions when the parts are introduced to salt baths ([1], p. 47).

The signal was recorded and transmitted at least to HEF Groupe. TS ETSA developed a formal investigation report with causal factors and corrective actions. The report says a shortened English version was translated and presented to HEF Groupe ([1], p. 43). Therefore `signal_reported=yes` is based on an official documented report/presentation, even though the CSB found that the fuller causal learning was not effectively shared onward to TS USA. Indeed, the CSB concluded that the Mexico explosion’s causal factors and corrective actions were **not communicated from HEF Groupe to the other facilities**; had they been communicated, TS USA could have recognized the roller accumulation hazard in its pre-processing review ([1], p. 44).

### 3. Distributed holders and absent join

For the conservative holder count, TS ETSA held the incident information it formally investigated, while HEF Groupe held the translated report/awareness of the event. The report also shows the critical failure of onward integration: TS USA plant managers had not received official communication about Mexico; the HEF USA CEO lacked awareness before the CSB investigation; and the CSB found that HEF Groupe had not adequately communicated the event’s findings, causes, and consequences ([1], pp. 43–44). This supports a documented lower bound of two cross-organizational holders, not a speculative count of individuals.

`join_assigned=no` is not inferred from mere communication failure. The CSB affirmatively found that HEF Groupe did not actively engage with facilities to ensure safety knowledge was communicated and risks mitigated ([1], p. 47); did not manage safety knowledge throughout the company ([1], pp. 50–51); and did not provide resources or dedicated safety roles to ensure safety-management systems were in place ([1], pp. 52, 56). The report’s recommended corrective structure—a site safety-management position responsible for incorporating HEF safety information, plus corporate governance and knowledge-management programs—further delineates what was absent before the incident ([1], pp. 52, 57–58). A process engineer gave advice about the immediate obstruction, but the report does not identify that role as responsible and authorized to integrate historical, cross-facility signals; the cited affirmative organizational findings are the basis for the `no` value.

### 4. Suddenness label

The report does not use the literal word “sudden” to describe the 2024 event. It does, however, characterize the causal failure as water that “rapidly expanded as steam” and “rapidly boiled,” creating a violent steam explosion and uncontrolled eruption ([1], pp. 27, 53). This is the report’s official rapid-failure characterization and is treated as a close equivalent under the codebook’s suddenness rule.

## Limitations and uncertainty handling

1. **Date precision:** The 2018 signal and 2024 event are reported as calendar dates, not timestamps for both endpoints. The 2,317-day result is therefore a calendar-day interval; it does not assert hour-level precision. Because both dates are explicit, the interval is bounded for the coding convention used here (`lead_time_max_known=true`).
2. **Holder measure:** `holder_count_min=2` is deliberately conservative. The report establishes at least TS ETSA and HEF Groupe as organizational holders; it does not identify every individual who read, translated, created, or received the materials. The coding does not claim a complete holder census.
3. **Reporting versus dissemination:** `signal_reported=yes` means the Mexico signal was formally recorded and presented to HEF Groupe. It does **not** mean it was effectively disseminated to TS USA; the CSB explicitly found that it was not communicated to other facilities.
4. **Join criterion:** The `no` value rests on explicit CSB findings of absent knowledge-management systems and dedicated safety resources/roles. It does not treat the plant manager’s contact with the process engineer as a qualifying aggregation assignment, because the official report does not assign that role cross-holder historical-signal integration authority.
5. **Suddenness wording:** The report’s wording is “rapidly” and “violent,” rather than literal “sudden” or “without warning.” The `yes` code uses the codebook’s “close equivalent” provision and is limited to the physical failure sequence; it does not claim that the event was unforeseeable.

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6296 "U.S. Chemical Safety and Hazard Investigation Board, *TS USA Molten Salt Eruption*, Investigation Report, published June 3, 2025."
[2]: https://www.csb.gov/ts-usa-molten-salt-eruption/ "U.S. Chemical Safety and Hazard Investigation Board, TS USA Molten Salt Eruption investigation page."

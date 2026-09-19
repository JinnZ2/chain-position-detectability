# WO-2 source manifest: CSB final incident-investigation reports

**Cut-off date:** 19 September 2026
**Prepared by:** Manus AI
**Selection universe:** U.S. Chemical Safety and Hazard Investigation Board (CSB) completed-investigation materials

## Fixed sample

This manifest applies the WO-2 sampling rule without regard to whether an incident may support the WO-2 decomposition. The governing source is the official CSB **Completed Investigations** index, which presents the eligible completed-investigation records in descending `Final Report Released On` order. The newest record on the index at the cut-off was dated 16 September 2026; the eight records below are therefore the eight most recently published qualifying reports available by 19 September 2026.[1]

For every selected record, the official investigation page identifies a specific U.S. incident, gives its event date and final-report release date, and labels the document as a final report. The linked final-report source was opened directly during verification: each returned a readable CSB-hosted PDF (`HTTP 200`, `application/pdf`) rather than an interim product or an inaccessible file. Each full report contains incident chronology sufficient for application of the pre-event evidence rules; this is an eligibility determination only, not a substantive WO-2 coding result.

| Rank | `case_id` | Official investigation title | Event date | Final report released | Investigation page | Final report opened and verified | Eligibility determination |
|---:|---|---|---|---|---|---|---|
| 1 | `shell-polymers` | Shell Polymers Furnace Explosion and Fire | 2025-06-04 | 2026-09-16 | [CSB investigation page][2] | [*Furnace Explosion and Fire at Shell Polymers*][3] | **Eligible.** A specific Monaca, Pennsylvania furnace explosion/fire; the case page records the event and final-report release, and the opened final investigation report includes the event chronology. |
| 2 | `us-steel-clairton` | United States Steel Corporation Clairton Plant Coke Oven Explosion | 2025-08-11 | 2026-08-10 | [CSB investigation page][4] | [*Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works*][5] | **Eligible.** A specific Clairton, Pennsylvania coke-oven explosion; the final investigation report was publicly accessible and contains incident chronology. |
| 3 | `bio-lab-conyers` | Bio-Lab Inc. Conyers Fire and Chemical Release | 2024-09-29 | 2026-07-21 | [CSB investigation page][6] | [*Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility*][7] | **Eligible.** A specific Conyers, Georgia fire and chemical release; the publicly accessible final investigation report includes the incident sequence and chronology. |
| 4 | `givaudan-sense-colour` | Givaudan Sense Colour Explosion | 2024-11-12 | 2026-05-27 | [CSB investigation page][8] | [*Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson*][9] | **Eligible.** A specific Louisville, Kentucky explosion; the opened final investigation report contains an incident timeline and supports chronology review. |
| 5 | `dow-louisiana-operations` | Dow Louisiana Operations Explosions | 2023-07-14 | 2026-02-26 | [CSB investigation page][10] | [*Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations*][11] | **Eligible.** A specific Plaquemine, Louisiana explosion/release incident; the final report was accessible and expressly describes conditions prior to the incident. |
| 6 | `pemex-deer-park` | PEMEX Deer Park Chemical Release | 2024-10-10 | 2026-02-23 | [CSB investigation page][12] | [*Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery*][13] | **Eligible.** A specific Deer Park, Texas hydrogen-sulfide release; the final investigation report was publicly accessible and contains the incident account needed to examine pre-event chronology. |
| 7 | `cuisine-solutions` | Cuisine Solutions Ammonia Release | 2024-07-31 | 2025-09-25 | [CSB investigation page][14] | [*Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility*][15] | **Eligible.** A specific Sterling, Virginia ammonia release; the opened final report identifies a timeline of key events and is suitable for the codebook’s chronology review. |
| 8 | `ts-usa` | TS USA Molten Salt Eruption | 2024-05-30 | 2025-06-03 | [CSB investigation page][16] | [*Explosion, Molten Salt Eruption, and Fatal Injury at TS USA Liquid Nitriding Facility*][17] | **Eligible.** A specific Chattanooga, Tennessee molten-salt eruption and fatality; the publicly accessible final report includes a detailed timeline. |

## Ordering and eligibility method

The selection date is a **publication** date, not an incident date. I used the CSB index’s `Final Report Released On` field to order records descending, then applied the codebook’s inclusion conditions to each record in that order: a specific incident, a public final investigation report, and enough pre-event chronology to apply the instrument. The investigation title and event date above are transcribed from the corresponding official investigation page. Final-report access was checked by opening the CSB document link itself, not merely by relying on a search result or page link. The direct report links in references [3], [5], [7], [9], [11], [13], [15], and [17] are the verified URLs.

The PEMEX investigation page contains a prose-status sentence saying the investigation was released in February 2025, which conflicts with both its displayed `Final Report Released On: 02/23/2026` field and the final report’s own `Published: February 2026` front matter. The manifest uses **2026-02-23**, because the official completed-investigations index determines the ordering and the report corroborates the year.[1] [12] [13]

## Near-boundary and categorical exclusions

The following records were reviewed only to document the boundary. They were not excluded because of their likely WO-2 coding result.

| Record | Official final-report date / status | Disposition and reason |
|---|---|---|
| Honeywell Geismar Chlorine and Hydrogen Fluoride Releases | 2025-05-27 | **Excluded at rank 9.** It is the first completed incident-investigation report after the eight-record cutoff. It was not selected because the fixed sample is limited to the eight most recently published eligible reports, not because of its facts or likely coding result.[1] |
| Marathon Martinez Renewable Fuels Fire | 2025-03-13 | **Excluded at rank 10.** It follows the rank-9 Honeywell record in the same official descending index, so it is outside the fixed eight-record sample.[1] |
| CSB Safety Study: Remote Isolation of Process Equipment | Listed among completed materials, with no `Final Report Released On` incident-report record in this sequence | **Categorically excluded.** It is a safety study rather than one investigated, specific incident with a final incident-investigation report, which the codebook expressly excludes.[1] |

No selected record required replacement for an inaccessible final report.

## References

[1]: https://www.csb.gov/investigations/completed-investigations/ "Completed Investigations | CSB"

[2]: https://www.csb.gov/shell-polymers-furnace-explosion-and-fire/ "Shell Polymers Furnace Explosion and Fire | CSB"

[3]: https://www.csb.gov/file.aspx?DocumentId=6343 "Furnace Explosion and Fire at Shell Polymers"

[4]: https://www.csb.gov/united-states-steel-corporation-clairton-plant-coke-oven-explosion-/ "United States Steel Corporation Clairton Plant Coke Oven Explosion | CSB"

[5]: https://www.csb.gov/file.aspx?DocumentId=6340 "Fatal Coke Oven Gas Explosion at U.S. Steel Clairton Coke Works"

[6]: https://www.csb.gov/bio-lab-inc-conyers-fire-and-chemical-release-/ "Bio-Lab Inc. Conyers Fire and Chemical Release | CSB"

[7]: https://www.csb.gov/file.aspx?DocumentId=6339 "Chemical Decomposition, Fires, and Toxic Gas Release at KIK Consumer Products / Bio-Lab Conyers Facility"

[8]: https://www.csb.gov/givaudan-sense-colour-explosion-/ "Givaudan Sense Colour Explosion | CSB"

[9]: https://www.csb.gov/file.aspx?DocumentId=6324 "Fatal Runaway Reaction and Explosion at Givaudan Sense Colour / D.D. Williamson"

[10]: https://www.csb.gov/dow-louisiana-operations-explosions/ "Dow Louisiana Operations Explosions | CSB"

[11]: https://www.csb.gov/file.aspx?DocumentId=6316 "Explosions, Fires, and Toxic Ethylene Oxide Release at Dow Louisiana Operations"

[12]: https://www.csb.gov/pemex-deer-park-chemical-release-/ "PEMEX Deer Park Chemical Release | CSB"

[13]: https://www.csb.gov/file.aspx?DocumentId=6315 "Fatal Hydrogen Sulfide Release at PEMEX Deer Park Refinery"

[14]: https://www.csb.gov/cuisine-solutions-ammonia-release-/ "Cuisine Solutions Ammonia Release | CSB"

[15]: https://www.csb.gov/file.aspx?DocumentId=6304 "Hazardous Ammonia Release at Cuisine Solutions, Inc. Facility"

[16]: https://www.csb.gov/ts-usa-molten-salt-eruption/ "TS USA Molten Salt Eruption | CSB"

[17]: https://www.csb.gov/file.aspx?DocumentId=6296 "Explosion, Molten Salt Eruption, and Fatal Injury at TS USA Liquid Nitriding Facility"

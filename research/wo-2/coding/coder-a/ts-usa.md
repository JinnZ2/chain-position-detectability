# WO-2 evidence record — TS USA Molten Salt Eruption

**Coder:** A
**Case ID:** `ts-usa`
**Event date:** 2024-05-30
**Official final report:** [CSB final investigation report][1]

## Coding determination

| Variable | Code | Basis |
| --- | --- | --- |
| `signal_present` | **yes** | Before the fatal 2024 event, the 2018 Mexico explosion established that a part with an accumulation hazard processed in a liquid nitriding line could cause a water-driven overpressure explosion. The CSB expressly connects the Mexico, France, and 2023 Chattanooga incidents to trapping materials in cavities and consequent overpressure explosions in salt baths. [1] |
| `signal_reported` | **yes** | TS ETSA made a formal Mexico-incident report with causal factors and corrective actions. A translated English version was presented to HEF Groupe. This is documented communication/recording beyond the originating facility, even though the information was not effectively communicated to TS USA. [1] |
| `holder_count_known` | **true** |
| `holder_count_min` | **2** | The conservative minimum is two organizational holders: **TS ETSA**, which investigated the 2018 event and produced the report, and **HEF Groupe**, to which a translated version was presented and which maintained the related risk analyses at corporate level. The record supports at least these two holders but not a complete count of individuals or units that possessed each relevant fragment. [1] |
| `join_assigned` | **no** | The report affirmatively finds no functional integration point that was assigned and resourced to aggregate and act on cross-facility safety knowledge. It says neither TS USA nor HEF USA employed facility safety professionals, no system was set up to ensure corporate safety requirements at facilities, and dedicated safety roles should have been assigned. It further finds that HEF Groupe did not manage or transfer safety knowledge to subsidiaries. Although regional and plant management existed, the source does not identify them as a function with both authority and responsibility to aggregate the Mexico/corporate-risk information with site-level information; rather, it documents the failure of that arrangement. [1] |
| `first_signal_date` | **2018-01-25** | This is the earliest **dated** relevant signal in the final report: the Mexico explosion. The report also identifies an undated HEF Groupe risk analysis prepared before the September 2023 Chattanooga event; it does not establish its date relative to 2018. [1] |
| `lead_time_days_min` | **2317** | 2,317 days from the dated 2018-01-25 Mexico explosion to the 2024-05-30 event. This is a defensible lower bound because a relevant, causally connected signal existed on that exact date; any genuinely earlier undated signal would only lengthen the interval. [1] |
| `lead_time_max_known` | **false** |
| `lead_time_days_max` | **0** | Per the task rule for an open/unknown upper bound. The report dates the Mexico event but does not date the corporate risk analysis or establish whether it preceded the 2018 event, so it does not support a closed maximum lead time. [1] |
| `sudden_label` | **yes** | The final report characterizes the physical failure as rapid: retained water “**rapidly expanded as steam**” and “**rapidly boiled**,” producing a “**violent steam explosion**” and uncontrolled molten-salt eruption. This is a close official equivalent of a sudden failure characterization. [1] |
| `pattern_result` | **supports** | All required codebook elements are affirmative: a causally relevant pre-event signal was present and reported, at least two organizational holders are evidenced, and the report affirmatively documents that no assigned/resourced integrating safety-knowledge function existed. |

## Decisive official evidence

### The causal mechanism makes the earlier information a relevant signal

The CSB determined that the 2024 cause was water retained in the roller cavity entering an 800°F oxidizing salt bath. The water expanded and boiled in the cavity, producing overpressure, a steam explosion, and a molten-salt eruption. The report identifies lack of awareness of cavity accumulation hazards, inadequate procedures/training/hazard analyses/incident investigations, and ineffective corporate safety-knowledge management as contributors. [1]

The report directly connects the 2018 Mexico incident to that hazard. The Mexico roller passed through rinse baths, water likely entered it, and, after introduction to the 1,040°F nitriding bath, the water expanded until an overpressure explosion ejected molten salt. TS ETSA determined that a part with an accumulation hazard had been allowed into the liquid nitriding line. [1]

The final findings make the connection explicit rather than inferential:

> “TS USA, HEF Groupe, and other TS facilities have repeatedly had reason to understand that parts with accumulation hazards and sealed cavities are not suitable for the liquid nitriding process. All three incidents discussed above—2018 in Mexico, 2020 in France, and 2023 in Chattanooga—show that these parts are susceptible to trapping materials in their cavities, which leads to overpressure explosions when the parts are introduced to the salt baths.” [1]

The CSB separately found that the Mexico causal factors and corrective actions had not been communicated to other facilities, and that communication would have enabled TS USA to identify the accumulation hazard and reject the rollers during pre-processing review. [1]

### Reported status and minimum holders

The report records that TS ETSA investigated the Mexico explosion, created a formal report covering the incident, causal factors, and corrective actions, and required a pre-processing inspection supported by a visual aid. It also records that a shorter English translation was “presented to HEF Groupe.” [1] Therefore, the signal was recorded and communicated from the originating facility to another organizational unit before the 2024 incident. That satisfies `signal_reported=yes`; the variable does not require successful delivery to the ultimately affected Chattanooga workforce.

Two holders are documented without assuming any unreported distribution: TS ETSA held the incident investigation/corrective-action information, while HEF Groupe received the translated report and also maintained process risk analyses at corporate level. Those corporate analyses identified “Risk of explosion if water is present in the baths which may be on or in the parts” and specified controls including prohibition of hollow parts and drying before bath introduction. The report says the analyses and safeguards were never communicated to Chattanooga. [1]

### Chronology and immediate, site-level observations

The detailed timeline gives a second, much shorter sequence of relevant site-level observations. On May 28, 2024, water was observed and drained from a roller after polishing; pressurized air was used to remove water and salt from the cavity. On May 29, water began emptying onto the ground at the polishing station. [1] On May 30, the plant manager and supervisor attempted to clear a salt obstruction and identified a roller too hot to touch; the plant manager contacted the process engineer, instructed the line operator on reprocessing, and the rollers were submerged in the oxidizer vessel at 08:54. The explosion and salt eruption occurred at 08:58. [1]

The causal analysis states that water drained when the manager tried to clear the obstruction, but the lack of continuous drainage led employees to believe only salt remained. In consultation with the process engineer, the rollers were reintroduced to the oxidizer tank and the mandatory preheat/drying step was skipped. The report states that the lack of reprocessing procedures meant the hazards were not identified. [1]

### Communications, roles, and lack of an assigned join

The report identifies a corporate-level information failure. HEF Groupe developed the operating manuals, and management said it generated the hazard analyses and process-safety reviews. Yet the analyses were retained at corporate level, only available in French, and not communicated to TS USA facilities. [1] The final report says that HEF Groupe did not sufficiently share or explain the accumulation-in-cavities hazard with subsidiaries. [1]

The report documents a limited transmission after Mexico: HEF Groupe trained managers about the Mexico explosion at its 2018 annual meeting, but did not train other employees. It did not institutionalize the lessons from Mexico or France. Chattanooga employees were unaware of the previous incidents, water entrapment consequences, and explosion potential. [1] The report also identifies no distributed report or corrective actions for the 2020 France incident and no robust formal investigation of the 2023 Chattanooga incident. [1]

For `join_assigned`, the decisive evidence is affirmative rather than a mere absence of a job title. The report states that HEF Groupe did not establish systems within subsidiaries to ensure corporate safety requirements were implemented. Neither TS USA nor HEF USA employed safety professionals at individual facilities; HEF Groupe instead relied on regional and plant management. It finds that the lack of resources specifically devoted to safety contributed to the event and says dedicated safety resources and responsibilities should have been assigned. [1] Its conclusion is that HEF Groupe did not manage safety knowledge throughout the company or ensure the information developed was provided to and managed at subsidiaries. [1] This satisfies the codebook’s affirmative-evidence standard for `join_assigned=no`; it does not merely treat an incomplete organizational chart as proof.

### Suddenness characterization

The formal technical finding states:

> “The retained water boiled inside the roller’s cavity and rapidly expanded as steam. The increased pressure forcefully ejected the roller’s press fit end, the salt plug, and the water into the molten salt bath. The water rapidly boiled, creating a violent steam explosion that drove an uncontrolled eruption of molten salt from the vessel.” [1]

The words “rapidly expanded,” “rapidly boiled,” and “violent steam explosion” are the report’s close-equivalent characterization of a sudden failure. This coding does not claim the report used the exact word “sudden.”

## Lead-time calculation

The earliest dated causally relevant signal is the **2018-01-25** Mexico explosion. The event date is **2024-05-30**. Calendar-day difference: **2,317 days**. The Mexico report was communicated to HEF Groupe, yet the report also describes an undated corporate risk analysis that had been prepared before the September 2023 Chattanooga incident. Because the source does not date that analysis or order it relative to January 2018, the record preserves 2,317 as the defensible minimum and treats the maximum as open (`lead_time_max_known=false`, `lead_time_days_max=0`).

## Limitations

The record does not claim that 2018-01-25 is the absolute earliest possible organizational knowledge. The official report does not date the corporate risk analysis, so an earlier relevant signal is possible but not dateable. That uncertainty precludes a closed maximum lead time.

`holder_count_min=2` is deliberately conservative. The report describes additional possible holders, including 2023 Chattanooga participants and managers trained in 2018, but does not provide a complete, role-by-role pre-event information map. The code therefore counts only the two organizational holders directly established by the Mexico report’s production and presentation.

The report cannot confirm whether a formal investigation or written report existed for the 2020 France incident. This record does not rely on that uncertain item to establish the signal, reporting, holder minimum, or lead-time minimum; the dated 2018 Mexico event independently supports those values. [1]

`join_assigned=no` concerns an assigned cross-holder integration function before the event. It does not assert that no informal discussions occurred. The report documents some managerial and operational roles, but affirmatively finds the absence of dedicated safety resources, adequate systems, managed knowledge transfer, and effective lines of communication needed to integrate the relevant fragments. [1]

## References

[1]: https://www.csb.gov/file.aspx?DocumentId=6296 "U.S. Chemical Safety and Hazard Investigation Board, TS USA Molten Salt Eruption—Investigation Report, June 2025"

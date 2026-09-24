# WO-5 field protocols for maintenance reporting chains

**Author:** Manus AI

**Status:** Preregistered protocol; not executed in this milestone

## Shared frame

The target chain begins with a machine-state concern noticed by an operator. The concern may enter an application, pass through triage and a work queue, trigger a mechanic dispatch, and end in work or disposition. A breakage override is recorded as a separate bypass path rather than as success of the normal path. The protocols distinguish **pre-entry loss**, which occurs before an observation becomes a system record, from **transit loss**, which occurs after entry.

An observation event is a time-bounded statement about a named asset and an observable condition. Examples include an unusual sound, vibration, smell, temperature, leak, control response, or change under load. A matched app record must refer to the same asset, condition, and shift or a prespecified matching window. Two blinded reviewers adjudicate uncertain matches.

Every study must record the observer who held the machine observation, the person whose credentials appear on the report, whether a proxy typed it, the input device, and whether the available form could encode the observation. Proxy typing is a transmission path, not non-reporting by the observer.

## Test A measures pre-entry loss

Researchers shadow consenting operators for complete sampled shifts and capture every maintenance concern stated spontaneously or in a standardized end-of-task elicitation. The observer log is timestamped before app records are retrieved. Reports filed during the shift and the prespecified lag window are then matched to the verbal concerns.

The primary pre-entry-loss estimate is:

`1 - matched unique concerns entered into the app / eligible unique verbal concerns`.

The denominator excludes non-maintenance remarks under rules fixed before review. The numerator counts a concern once even when several people file it. Results are stratified by direct self-entry, proxy entry with verified originating observer, unresolved proxy attribution, device failure, interface difficulty, literacy or language assistance, time or production pressure, and no stated reason. The study separately reports concerns whose sensory content had no compatible field.

The work order's falsifier is retained. If the paired estimate is near zero within a prespecified practical margin, the proposed pre-entry gates are not load-bearing in that setting and downstream triage becomes the next test. The protocol recommends a ±5 percentage-point equivalence margin, but the host site must justify its operational threshold before collection.

## Test B tests the learned prior

For each verified originating observer, the CMMS history defines eligible prior reports and their dispositions. The principal prior-closure measure is the fraction that received a visible action or reasoned disposition within a fixed window. The primary window is 30 days; seven-day and any-event windows are sensitivity analyses. Silent closure, deletion, duplicate merging without notice, and breakage-override work with no link to the original report remain distinct outcomes.

Current reporting opportunity is measured from Test A's verbal-observation denominator or another independently observed opportunity count. It is not inferred from submitted reports alone. The primary model is a binomial mixed model for entry of an eligible concern, with prior-closure proportion as the focal predictor and site, asset family, shift, tenure, workload, and device access as declared covariates. The result is associational because operators were not randomized to prior histories.

Observers whose reports were proxy-filed without originator provenance cannot receive a valid individual prior from the CMMS. They are excluded from the individual-level primary model and reported as a separate missing-provenance stratum. A secondary attribution-network analysis may reconnect proxy reports only when the originating observer is independently verified.

The learned-prior account is supported only if current entry probability tracks prior visible closure after the declared adjustments and sensitivity checks. A null or reversed association leaves the account unsupported in that site.

## Test C tests disposition transparency

The intervention returns the manager-side disposition of each eligible report to its verified originating observer: destination, status, decision, and reason. A receipt without disposition does not count. The preferred design is a cluster-randomized stepped wedge across shifts or work groups, with transition dates assigned before outcome review. Contamination across closely interacting operators must be assessed.

The primary outcome is the rate of app-entered eligible concerns per independently observed opportunity. If opportunity observation cannot continue, machine-hours are a secondary denominator and must not replace the primary endpoint silently. The primary estimand is the intervention-period change relative to concurrent controls. The work order's advance prediction is operationalized as a nonzero change in reporting rate; the sign is reported rather than assumed. A secondary hypothesis predicts a larger increase among operators with low baseline visible-closure histories when the intervention demonstrates that reports can close.

A practically null effect within a prespecified equivalence margin falsifies transparency as the binding constraint for the studied setting. Report quality, duplicate submissions, maintenance workload, adverse-event reporting, and breakage-override frequency are safety and displacement outcomes.

## Test D locates form-field loss

Test D links concerns observed verbally at the app-entry point to independently recorded breakdowns or corrective work within prespecified seven- and 30-day horizons. The outcome definition is fixed before text or audio features are inspected. Repeated concerns about one asset are grouped to prevent leakage between training and test folds.

Two prediction models use the same cases and grouped cross-validation. The first receives only the structured app record and filed text. The second receives a blinded coding of the original verbal observation, including sensory modality and change under load. Performance is reported with area under the receiver-operating-characteristic curve, calibration, precision-recall measures, and uncertainty. The comparison is descriptive unless the sample is large enough for a prespecified paired test.

If app records separate future breakdown from non-breakdown cases as well as verbal observations, the proposed form-field loss is not supported. If verbal records separate but app records do not, and the difference survives asset and operator controls, the result locates discriminating loss at or before form encoding. Neither result proves that the operator's statement is causal.

## Governance and minimum reporting

Participation must not expose operators to discipline for non-reporting, spelling, device use, or proxy assistance. Consent, data minimization, labor representation where applicable, and an explicit firewall from performance management are required. The host site must publish recruitment, missingness, proxy prevalence, breakdown-override use, matching reliability, deviations, and null findings.

These protocols are instruments, not findings. No plant-level claim is made in this milestone.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-5-hop-distance-and-pre-entry-loss.md "WO-5 — Hop distance and pre-entry loss in reporting chains"

# WO-3 evidence record — information, observation, and control

**Item:** information–observation–control crossing family
**Verdict:** **REFRAME.** The current row joins a property of a physical transfer (**information**) to two process roles (**observation** and **control**). Its current quantity, “bits where measurable; otherwise event count,” cannot represent the probe, readout, standing control condition, and causal effect separately. It is therefore not capable of supporting the stated all-zero decision rule as written.

## What the existing row gets wrong

Information is not an independent physical medium in the same sense as mass or energy. It is a property of a signal or record that has a source, transmitter, channel, receiver, and destination in Shannon’s general communication model.[1] The physical carrier should also be recorded in its carrier family; the information row should describe the **source–destination relation, direction, encoding/ensemble, and record**. Otherwise “one event” makes a one-bit interlock and a large data archive indistinguishable, while a bit count without a specified source distribution or code is undefined.

> “By a communication system we will mean a system of the type indicated schematically in Fig. 1.” Shannon’s schematic contains an information source, transmitter, signal/channel, receiver, and destination.[1]

The metric also treats *observation* as though it were merely an outgoing signal. It misses a distinct **measurement coupling**: a probe or detector interaction can change the candidate system even while an outward readout informs the observer. This is not merely theoretical. Murch *et al.* report an optical cavity mode that was “measured by the cavity’s optical properties, actuated by the cavity optical field and subject to backaction,” and experimentally quantified the backaction through light-induced heating.[3] A single observation therefore has, at minimum, a probe/input, a readout/output, and a possible disturbance; counting only “a measurement event” or its bits loses the direction and the causal change.

The row separately fails to represent **control as intervention**. A command is an information-bearing input, but control can persist with no new message during the horizon: a fixed boundary set-point, enabled interlock, standing authorization, actuator bias, or externally maintained constraint may alter what S can do. Such a coupling can have zero Shannon variability and zero command-event count after `t0`, yet still constrain S. The current definition says a crossing can “constrain,” but its `Qm,in/out` flow measure has no field for a standing control state or causal gain. If the state was installed before `t0`, it is an initial condition for a finite-horizon claim; for whole-life terminality its installation is a prior control crossing.

Finally, a statistical association is not enough to label an information crossing or control coupling. Schreiber introduced transfer entropy precisely because ordinary mutual information does not distinguish actual directed exchange from common input or shared history.[2] Transfer entropy is a useful, model-dependent time-series estimator, not proof of causal intervention; a predeclared intervention or other causal identification assumption is needed before calling a detected association “control.” This is an omission in the decision rule, not a newly discovered medium.

## Required amendment: three process records, plus an exclusion rule

| Record to add | What constitutes a positive witness | Finite-boundary/horizon measurement | Limit that must be reported |
|---|---|---|---|
| **Information-bearing transfer** | A signal or record crosses B between declared endpoints and makes a state of one available to the other. | Yes. Log direction, endpoint, carrier, time, alphabet/code or probability model, payload bits when defined, and event count otherwise. | Bits are not intrinsic without the declared model; carrier flow belongs in its physical-carrier record too. |
| **Observation / measurement coupling** | A probe interacts with S, an external readout is obtained, or the measurement demonstrably disturbs S. Record probe-in and readout-out separately. | Yes, for a stated instrument, calibration, B, and H. Record sensitivity, sampling, false-negative rate, probe dosage, and a disturbance bound or response test. | No finite test excludes effects below its detection/disturbance bound. A null result is not `U = 0`. |
| **Control / actuation coupling** | An external command, set-point, actuator, authority, or boundary condition causally changes or constrains S. | Yes, conditionally. Record command/actuation direction, parameter trajectory, persistence interval, authority path, and a predeclared intervention/response test where safe. | Association alone can be common-cause correlation; a standing condition must be recorded as a state/exposure, not forced into a flow count. |
| **Correlation exclusion rule** | Correlation without a declared cross-B mechanism or causal identification is **not** a positive crossing witness. | Yes: register it as an unresolved hypothesis and test with an intervention or mechanism evidence. | It must not be converted into either a positive information flow or a zero-flow conclusion. |

This amendment stays within the requested family. It does not create a seventh physical medium: probes, readouts, and actuators may use matter, radiation, fields, or people, which can be cross-indexed to other existing rows. Its purpose is to prevent the information row from hiding the direction and intervention structure required for the terminality test.

## Observation versus theory

**Observed.** Murch *et al.* experimentally measured cavity-light-induced heating and reported measurement backaction on a macroscopic mechanical resonator.[3] This is direct evidence that a real observation arrangement can be a coupled actuation/disturbance process, not merely an abstract data record.

**Theory and definitions.** Shannon’s source–channel–receiver construction defines the communication accounting frame.[1] Schreiber’s transfer entropy is a mathematical statistic designed to detect directed exchange while rejecting static-correlation confounding; it does not by itself establish a physical mechanism.[2] Clerk *et al.* review quantum measurement and amplification, including detector output noise, back-action noise, and their constraint; this supports the warning that extraction of measurement information and disturbance are linked in the relevant physical regime, but it is not evidence that every classical observation must cause a detectable new disturbance.[4]

## Can a zero upper bound be verified without an information/measurement crossing?

**No, not as an empirical claim made available outside B.** An external verifier must possess a record correlated with S and the interval H. If that record comes from S during H, it is an outward information-bearing crossing. If an instrument obtains it by probing S, the probe/readout is a measurement coupling; the carrier may be separately recorded elsewhere. Passive remote observation does not rescue the literal zero claim: it may avoid *creating* a new B-crossing, but it relies on an already escaping signal or field, which is itself a positive outward crossing. An internal observer can inspect S without exporting the result, but then the proposition has not been externally empirically verified; exporting the result creates the information crossing.

A model can prove `U = 0` **conditional on its axioms, construction record, and parameter values**. That is a model-level result, not an empirical verification of a physical system. Empirical checks of the construction, identity, boundary, and parameter values require observations. Nor can finite nondetection yield exact zero: with zero events in `n` relevant independent opportunities, Hanley and Lippman-Hand show that the approximate one-sided 95% upper bound is `3/n`, not zero, and urge reporting the maximum risk compatible with the findings.[5] The prerequisite “independent opportunities” and an appropriate event model must be declared.

Accordingly, the work order’s literal falsifier—an empirically established system with zero crossings in every medium—has **no operational empirical form** for this family. A build can falsify it only in the weaker, useful form: *over declared B and finite H, every enumerated information-transfer, observation, and control record is below a stated detection bound, with the inventory and causal assumptions stated.* That result is **unresolved non-detection**, not `U = 0` and not terminality. Positive witnesses remain operationally easy: a single logged readout, command, probe, standing external constraint, or validated causal actuation rejects zero for the declared frame.

## References

[1]: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf "A Mathematical Theory of Communication"

[2]: https://arxiv.org/pdf/nlin/0001042 "Measuring Information Transfer"

[3]: https://arxiv.org/pdf/0706.1005 "Observation of Quantum-Measurement Backaction with an Ultracold Atomic Gas"

[4]: https://clerkgroup.uchicago.edu/PDFfiles/RMP2010.pdf "Introduction to Quantum Noise, Measurement, and Amplification"

[5]: https://jhanley.biostat.mcgill.ca/Reprints/If_Nothing_Goes_1983.pdf "If Nothing Goes Wrong, Is Everything All Right? Interpreting Zero Numerators"

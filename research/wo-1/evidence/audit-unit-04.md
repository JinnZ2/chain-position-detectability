# WO-1 evidence record — TOP10-04

## Determination

**Result: NEGATIVE.** No reviewed clause requires the *executing agent* to receive or query evidence of its predecessor, successor, depth, membership, or another equivalent position in a larger execution chain. The closest language requires lineage metadata for propagated actions, but assigns it forensic, rollback, and accountability purposes without requiring that the metadata be delivered into, queryable by, or usable within an agent's execution boundary.[1]

This is a **DERIVED** result from the source text and the work-order criterion. The source itself is **OBSERVED**. It calls this material “Prevention and Mitigation Guidelines,” rather than using a conformance vocabulary such as “MUST” or “SHALL.” For completeness, this record treats each numbered guideline as a normative-style control statement and separately reviews the one explicit modal “must” sentence in the ASI08 description. That produces **20 clause-level statements reviewed**: nine in ASI07, ten in ASI08, and one descriptive modal statement.

> **Decision rule applied.** A positive result requires a normative requirement that places evidence of chain position **inside the executing agent**: for example, the agent can receive or query a predecessor, successor, depth, membership, or equivalent execution-chain location. Gateway-side lineage, middleware traces, dashboards, audit logs, registries, and post-hoc observability are negative unless the source requires exposure inside that boundary.

## Source and scope

The unit is **ASI07: Insecure Inter-Agent Communication through ASI08: Cascading Failures** in *OWASP Top 10 for Agentic Applications 2026*, Version 2026, December 2025. The full immutable PDF was downloaded from the supplied GitHub commit and read in full for the unit: ASI07 spans printed pp. 27–29 (PDF pp. 28–30); ASI08 spans printed pp. 30–32 (PDF pp. 31–33). The file reviewed has SHA-256 `a2db94cd00b08e0b3a5e5b619afe024bdbcd74503111085705e4f3dd886fcb5c`.[1] The OWASP resource page identifies the publication as the OWASP Top 10 for Agentic Applications for 2026, dated December 9, 2025.[2]

The audit excludes vulnerability examples and attack scenarios as non-normative commentary. The ASI08 descriptive text and all prevention/mitigation guideline entries were nevertheless read, because the former explains the intended propagation model and contains one modal sentence.

## Decisive evidence

ASI08’s logging control is the strongest relevant evidence because it expressly calls for lineage while defining only external/post-hoc uses:

> “**Record all inter-agent messages, policy decisions, and execution outcomes in tamper-evident, time-stamped logs bound to cryptographic agent identities. Maintain lineage metadata for every propagated action to support forensic traceability, rollback validation, and accountability during cascades.**” — ASI08, *Prevention and Mitigation Guidelines* 10, printed p. 32 / PDF p. 33.[1]

The control’s stated locus is **logging/lineage infrastructure**. Its listed functions—“forensic traceability, rollback validation, and accountability”—do not require the active agent to inspect that metadata before or during execution. It does not say the lineage travels with a message, is supplied to an executing agent, or exposes predecessor, successor, depth, or membership. Under the criterion, this is negative, not positive.

ASI08 also describes “rapid fan-out” and “downstream agents or tasks” as observable cascade symptoms, but that is commentary about detection hooks, not a requirement to disclose position to a current agent:

> “**Observable symptoms include rapid fan-out where one faulty decision triggers many downstream agents or tasks in a short time** ... **each providing clear detection hooks that make ASI08 operationally actionable.**” — ASI08, *Description*, printed p. 30 / PDF p. 31.[1]

## Clause-by-clause review

### ASI07 — Insecure Inter-Agent Communication

The ASI07 controls address authenticity, integrity, replay, protocol, discovery, registry, and message-schema security. They may be implemented at an endpoint agent, protocol stack, directory, gateway, middleware, or monitoring plane. None requires a larger-chain position to be exposed in the agent’s own execution context.

| Clause | Exact decisive language | Control locus | Chain-position assessment |
|---|---|---|---|
| 1 | “**Use end-to-end encryption with per-agent credentials and mutual authentication. Enforce PKI certificate pinning, forward secrecy, and regular protocol reviews**” (ASI07, *Prevention and Mitigation Guidelines* 1, printed p. 28 / PDF p. 29).[1] | Communication endpoints and PKI/protocol controls; deployment locus is not otherwise fixed. | **Negative.** Per-agent credentials authenticate identity, not a predecessor/successor relation, depth, or chain membership. The clause does not require identity data to be exposed to the agent’s reasoning or execution boundary. |
| 2 | “**Digitally sign messages, hash both payload and context, and validate for hidden or modified natural-language instructions.**” (ASI07 guideline 2, printed p. 28 / PDF p. 29).[1] | Message integrity/validation layer, potentially endpoint or middleware. | **Negative.** The required evidence concerns message integrity and semantic tampering, not chain position. |
| 3 | “**Protect all exchanges with nonces, session identifiers, and timestamps tied to task windows. Maintain short-term message fingerprints or state hashes to detect cross-context replays.**” (ASI07 guideline 3, printed p. 28 / PDF p. 29).[1] | Session/replay controls and short-term protocol state. | **Negative.** A task window or session identifier can distinguish context/replay but is not a required disclosure of a prior/next agent, chain depth, or membership. The text does not state that an agent can query any resulting state for chain position. |
| 4 | “**Require agent-specific trust negotiation and bind protocol authentication to agent identity. Enforce version and capability policies at gateways or middleware.**” (ASI07 guideline 4, printed p. 29 / PDF p. 30).[1] | Explicitly gateway or middleware for version/capability policy; peer protocol identity for negotiation. | **Negative.** This expressly places part of the control outside agents. Agent identity/trust negotiation is not chain-location evidence and no execution-boundary exposure is required. |
| 5 | “**Reduce the attack surface for traffic analysis by using fixed-size or padded messages where feasible, smoothing communication rates, and avoiding deterministic communication schedules.**” (ASI07 guideline 5, printed p. 29 / PDF p. 30).[1] | Communication fabric/traffic-shaping layer. | **Negative.** The clause reduces externally inferable role/cycle signals; it does not supply position information to an agent. |
| 6 | “**Define and enforce allowed protocol versions** ... **Reject downgrade attempts or unrecognized schemas and validate that both peers advertise matching capability and version fingerprints.**” (ASI07 guideline 6, printed p. 29 / PDF p. 30).[1] | Protocol enforcement at endpoints, middleware, or gateway; source does not choose one. | **Negative.** “Both peers” can support bilateral compatibility validation, but neither identifies a peer as predecessor/successor nor conveys membership/depth in a larger execution chain. The locus is implementation-unspecified, so it cannot establish inside-agent access. |
| 7 | “**Authenticate all discovery and coordination messages using cryptographic identity. Secure directories with access controls and verified reputations, validate identity and intent end-to-end, and monitor for anomalous routing flows.**” (ASI07 guideline 7, printed p. 29 / PDF p. 30).[1] | Discovery directory, routing/monitoring, and end-to-end validation. | **Negative.** Discovery identity/reputation is not mandated chain-position evidence. Directories and routing monitors are external services unless the source requires in-agent exposure; it does not. |
| 8 | “**Use registries or marketplaces that provide digital attestation of agent identity, provenance, and descriptor integrity. Require signed agent cards and continuous verification before accepting discovery or coordination messages.**” (ASI07 guideline 8, printed p. 29 / PDF p. 30).[1] | Registry/marketplace, PKI, and pre-acceptance verification. | **Negative.** Descriptor provenance is provenance of an agent description, not required runtime lineage or location in the particular execution chain. The registry locus is external and no current agent query is required. |
| 9 | “**Use versioned, typed message schemas with explicit per-message audiences. Reject messages that fail validation or attempt schema down-conversion without declared compatibility.**” (ASI07 guideline 9, printed p. 29 / PDF p. 30).[1] | Message-schema validator/protocol layer. | **Negative.** An audience constrains intended recipients, but does not identify the executing agent’s predecessor, successor, depth, membership, or equivalent chain position. |

### ASI08 — Cascading Failures

ASI08 controls fault tolerance, isolation, credential and policy checks, gates, monitoring, limits, testing, and logs. Several describe propagation or downstream behavior, but none makes the current agent aware of its own position in that propagation.

| Clause | Exact decisive language | Control locus | Chain-position assessment |
|---|---|---|---|
| 1 | “**design system with fault tolerance that assumes availability failure of LLM:2025, agentic function components and external sources.**” (ASI08, *Prevention and Mitigation Guidelines* 1, printed p. 32 / PDF p. 33).[1] | System architecture. | **Negative.** Assumed component failure is a system design property, not agent-accessible chain-position evidence. |
| 2 | “**Sandbox agents, least privilege, network segmentation, scoped APIs, and mutual auth. to contain failure propagation.**” (ASI08 guideline 2, printed p. 32 / PDF p. 33).[1] | Agent/container isolation, IAM, network, and API boundaries. | **Negative.** Sandboxing separates agents but does not require any agent to know where it sits in a chain. |
| 3 | “**Issue short-lived, task-scoped credentials for each agent run and validate every high-impact tool invocation against a policy-as-code rule before executing it.**” (ASI08 guideline 3, printed p. 32 / PDF p. 33).[1] | Credential issuer and runtime tool-policy enforcement point. | **Negative.** A task-scoped credential identifies a run’s authorization scope, not its predecessor/successor, depth, or membership. The clause does not require a policy decision or lineage record inside the agent. |
| 4 | “**Separate planning and execution via an external policy engine**” (ASI08 guideline 4, printed p. 32 / PDF p. 33).[1] | **Explicitly external policy engine.** | **Negative.** The source locates enforcement outside the agent rather than supplying an executing agent with chain-position evidence. |
| 5 | “**Checkpoints, governance agents, or human review for high risk before agent outputs are propagated downstream.**” (ASI08 guideline 5, printed p. 32 / PDF p. 33).[1] | Governance/checkpoint/human review gate. | **Negative.** “Downstream” describes propagation, but this clause requires a gate before output propagation, not a disclosure to the source agent that it has a successor or where it lies in a chain. |
| 6 | “**Detect fast-spreading commands and throttle or pause on anomalies.**” (ASI08 guideline 6, printed p. 32 / PDF p. 33).[1] | Monitoring and rate-limiting control plane; implementation locus unstated. | **Negative.** Detecting spread is not a requirement to inform an executing agent of chain position. |
| 7 | “**Implement blast-radius guardrails such as quotas, progress caps, circuit breakers between planner and executor.**” (ASI08 guideline 7, printed p. 32 / PDF p. 33).[1] | Orchestrator/control plane or inter-agent boundary. | **Negative.** A boundary “between planner and executor” restricts propagation but does not require either party to receive chain position, including relation direction, as evidence available inside execution. |
| 8 | “**Track decisions vs baselines and alignment; flag gradual degradation.**” (ASI08 guideline 8, printed p. 32 / PDF p. 33).[1] | Behaviour/governance monitoring. | **Negative.** The required tracking is drift observability, not runtime chain-position disclosure. |
| 9 | “**Re-run the last week’s recorded agent actions in an isolated clone**” and “**Gate any policy expansion on these replay tests passing predefined blast-radius caps before deployment.**” (ASI08 guideline 9, printed p. 32 / PDF p. 33).[1] | Offline digital-twin test and deployment gate. | **Negative.** This is post-hoc/offline system testing, not an executing agent’s ability to inspect its position. |
| 10 | “**Record all inter-agent messages, policy decisions, and execution outcomes in tamper-evident, time-stamped logs**” and “**Maintain lineage metadata for every propagated action to support forensic traceability, rollback validation, and accountability during cascades.**” (ASI08 guideline 10, printed p. 32 / PDF p. 33).[1] | Logging/lineage and forensic/rollback infrastructure. | **Negative.** This is the closest clause, but it mandates lineage for traceability after or around propagation. It neither says the metadata is delivered to an agent nor requires that agent to query it. The criterion expressly excludes such external observability absent in-agent exposure. |

### ASI08 descriptive modal statement

The only explicit “must” found in the ASI07–ASI08 textual unit is not a mitigation control and does not create a chain-position interface:

| Clause | Exact decisive language | Control locus | Chain-position assessment |
|---|---|---|---|
| ASI08 description | “**This leaves some unmitigated risks that the enterprise must evaluate carefully to ensure they are within the overall risk budget for the organization.**” (ASI08, *Description*, printed p. 30 / PDF p. 31).[1] | Enterprise risk governance. | **Negative.** The enterprise evaluates risk; the clause neither identifies an executing agent’s chain position nor mandates delivery of such evidence to the agent. |

## Boundary analysis and uncertainty

**OBSERVED:** The source repeatedly addresses agent identity, message audiences, peer compatibility, task windows, routing, propagation, and action lineage. These concepts can help a system authenticate actors, validate messages, limit spread, and reconstruct events.[1]

**DERIVED:** They do not meet the stated measurand. Identity is not membership in a concrete execution chain. A per-message audience is not the agent’s location in a chain. A task/session identifier is not a required predecessor/successor/depth query. Message provenance, descriptor provenance, and propagated-action lineage can all exist entirely in infrastructure or logs. No clause says that the executing agent receives, can inspect, or can query any of those items to determine its own relation to other chain steps.

**Uncertainty preserved:** Some ASI07 controls could be implemented within an agent’s protocol stack, particularly endpoint authentication, replay state, bilateral fingerprint comparison, and schema validation. ASI08 monitoring or rate limiting could also be placed in an agent implementation. The standard does not fix those deployment loci in all cases. This does **not** make the result ambiguous under the supplied test: even on an in-agent implementation, the required data are authentication, integrity, compatibility, replay, or rate-limit signals—not evidence of predecessor, successor, depth, membership, or an equivalent chain position. There is therefore no genuinely unclear clause satisfying the positive condition.

## Control-locus summary

The reviewed controls fall into the following loci: (1) **communication/protocol endpoints** for encryption, signatures, replay, version, and schema checks; (2) **gateways or middleware**, expressly named for ASI07 version and capability policy; (3) **external registries, directories, PKI, and routing monitors** for discovery, attestation, and routing; (4) **agent/container and infrastructure boundaries** for sandboxing, least privilege, segmented networks, scoped APIs, quotas, and circuit breakers; (5) **credential issuers, policy engines, governance gates, humans, and deployment processes** for authorization and approvals; and (6) **monitoring, digital-twin, logging, lineage, forensic, rollback, and accountability systems** for detection and post-hoc traceability.[1]

None of these clauses requires the relevant chain-position data to cross into the executing agent’s own execution boundary. The result is therefore **negative** rather than positive or ambiguous.

## References

[1]: https://github.com/GenAI-Security-Project/GenAI-Security-Advisor/blob/613bf32a6f1d13eaf7b30040f7e9b779b23cfb7f/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf "OWASP Top 10 for Agentic Applications 2026, Version 2026 (December 2025), immutable GitHub source"

[2]: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ "OWASP Top 10 for Agentic Applications for 2026"

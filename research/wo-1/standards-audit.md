# WO-1 Standards Audit: Detectability of Execution-Chain Position Inside an Agent

**Author:** Manus AI
**Milestone:** WO-1 — Chain position detectability from inside a container
**Audit disposition:** **Null result**
**Completed audit units:** 15 of 15; **failed units:** 0

## Executive finding

This audit found **no reviewed clause that requires an executing agent to receive or query evidence of its own position in a larger execution chain**. The result is **null**, not positive: across the fifteen assigned units, there are **0 positive, 15 negative, and 0 ambiguous** unit determinations. No unit failed, so the complete assigned corpus supports a conclusive result within its stated scope.

The two standards examined do require substantial security and governance instrumentation. They require, for example, policy enforcement, tool authorization, identity controls, provenance, parent–child audit records, SessionContext/audit chains, chain hashes, tracing, inventory reporting, logging, and human approval. The decisive distinction is **control locus**. The reviewed requirements place those mechanisms in frameworks, Guardians, policy engines, gateways, audit chains, trace systems, operator processes, or external observers. They do not require the executing agent to be given a predecessor, successor, depth, membership, parent/child location, or equivalent self-location fact.

This is not proof that chain position **cannot** be made available to an agent. A deployment can voluntarily expose additional context, decode or query audit state, or implement a proprietary topology API. The null result is narrower and stronger as a standards claim: **the audited public requirements do not mandate that exposure.**

## Decision criterion (applied before reviewing results)

> **A positive result requires a normative or normative-style source clause that requires the executing agent itself to receive or query information that establishes its location in a larger execution chain—such as a predecessor, successor, parent/child relation made available to the running agent, ordinal depth, membership, or an equivalent location attribute.**
>
> **A Guardian/server-side ledger, gateway or middleware trace, policy-engine decision, audit log, external dashboard, provenance record, or cryptographic chain commitment is not positive unless the source additionally requires that the executing agent receive or query information sufficient to establish that location.**

For this purpose, **executing agent** means the agent/LLM or its execution context that performs the task, rather than its surrounding framework, hook emitter, middleware, Guardian, or an outside observer. An obligation to emit a record *from* a framework/Observed Agent *to* a Guardian does not itself prove that the running agent receives the record or can inspect its broader-chain position.

Three evidence classes are kept separate throughout:

1. **Explicit requirement.** A normative modal, schema constraint, or OWASP mitigation directive actually directs an actor to do something. It can support a positive result only if it satisfies the criterion above.
2. **Silence.** The absence of a specified agent-facing topology field or query does not prove an implementation is impossible. It does support a null standards finding where the audit scope is complete and no qualifying requirement is present.
3. **Interpretation.** Terms such as *lineage*, *delegation chain*, *provenance*, *parent session*, and `chain_hash` were treated conservatively. They are not equated with agent-visible self-location unless the clause specifies both the needed semantics and delivery/query at the executing-agent boundary.

## Source and version scope

The audit is a textual analysis of the assigned public standards material. It does not assess vendor products, private interfaces, operational deployments, or any future edition.

The OWASP corpus is the version-pinned **OWASP Top 10 for Agentic Applications 2026, version 1.0**, covering ASI01 through ASI10 in five paired audit units. The canonical PDF is fixed to repository commit `613bf32a6f1d13eaf7b30040f7e9b779b23cfb7f`; OWASP identifies the associated resource as the 2026 Agentic Applications Top 10. [1] [2]

The second corpus is the **OWASP Agent Control Standard (ACS) v0.1.0**, fixed to repository commit `dc265475139a922824f0c817e2ecc2a2ce31c06c`. It includes the assigned conformance, Instrument, hooks, extension, concept, Trace, Inspect, and cited v0.1.0 schema material. [3] [4] [5] Where individual units expressly incorporated schemas, those schemas were reviewed as source closure rather than treated as informal implementation examples.

The source vocabulary differs. The OWASP Top 10 uses numbered **Prevention and Mitigation Guidelines**, rather than RFC-style conformance language. To avoid understating the audit, every assigned numbered guideline was treated as a normative-style candidate control. ACS uses RFC-style modals and schema constraints. Candidate-clause totals below are therefore **review counts, not a claim that all sources use the same formal normativity model**. Repeated or cross-referenced source clauses may appear in more than one unit count.

## Results at a glance

| Outcome | Audit units | Meaning |
|---|---:|---|
| **Positive** | 0 | No unit requires agent-visible execution-chain position. |
| **Negative** | 15 | The unit has no clause meeting the decision criterion. |
| **Ambiguous** | 0 | No unit contains a requirement whose recipient/semantics leave a genuine unresolved issue under the criterion. |
| **Failed** | 0 | No assigned unit was unavailable or incomplete. |
| **Candidate clauses reviewed** | **516** | Sum of unit counts; it includes OWASP guidelines, ACS normative statements, and the specified schema constraints where counted by the unit. It is not a deduplicated corpus total. |

The 516 candidate clauses comprise **87** OWASP guideline-style clauses and **429** ACS normative/schema clauses, counted according to each unit’s evidence record. The disposition is based on the 15 unit findings, not on a numerical vote among individual clauses.

## Compact audit table

The following table covers every assigned audit unit. “Negative” means **no qualifying inside-agent requirement was found**; it does not mean the cited security control is absent, ineffective, or unimportant for its stated purpose.

| ID | Standard and audited section | Clauses reviewed | Decisive passage | Express or decisive control locus | Result |
|---|---|---:|---|---|---|
| [TOP10-01](evidence/audit-unit-01.md) | ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation | 17 | “A pre-execution Policy Enforcement Point (PEP/PDP) validates intent and arguments…” [1] | Pre-execution PEP/PDP; tool IAM; approvals; operational monitoring | **Negative** — “delegation chains” is explanatory scope; no agent-facing position input/query is required. |
| [TOP10-02](evidence/audit-unit-02.md) | ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities | 18 | “Monitor when an agent gains new permissions indirectly through delegation chains.” [1] | Monitoring/analytics; IAM; supply-chain and release controls | **Negative** — monitoring delegation behavior or “lineage” does not require exposure inside the executing agent. |
| [TOP10-03](evidence/audit-unit-03.md) | ASI05 Unexpected Code Execution; ASI06 Memory & Context Poisoning | 16 | “Do static scans before execution; enable runtime monitoring … log and audit all generation and runs.” [1] | Code runtime, sandbox, monitoring, memory/retrieval controls | **Negative** — runtime monitoring and memory trust factors do not establish agent chain position. |
| [TOP10-04](evidence/audit-unit-04.md) | ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures | 20 | “Maintain lineage metadata for every propagated action to support forensic traceability, rollback validation, and accountability during cascades.” [1] | Tamper-evident logs, lineage/forensics, rollback, communication controls | **Negative** — required lineage is forensic/audit-side, not required to be supplied to or queried by the agent. |
| [TOP10-05](evidence/audit-unit-05.md) | ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents | 16 | Behavioral manifests are “validated by orchestration services before each action”; keys “must never be directly available to agents.” [1] | Orchestration, key management, human review, policy/verification services | **Negative** — the closest integrity control is expressly outside the executing agent. |
| [ACS-01](evidence/audit-unit-06.md) | Conformance Profiles; ACS-Core; Instrument §§1–3; incorporated schema package | 166 | “The agent **MUST NOT have knowledge of hooks**. Provenance fields … **MUST be populated outside the LLM’s output path**.” [4] | Framework-to-Guardian hooks; Guardian SessionContext/audit chain; schema enforcement | **Negative** — this expressly prevents inferring agent access from hook or provenance fields. |
| [ACS-02](evidence/audit-unit-07.md) | Instrument §4–§4.1: capability negotiation and handshake failure | 34 | The ServerHello requires negotiated version, methods, transport, and timeout configuration; unguarded sessions are recorded in deployment audit logs. [4] [6] | Observed Agent/Guardian handshake; deployment posture; audit/Trace sink | **Negative** — no negotiated field or failure handling requires chain location inside the agent. |
| [ACS-03](evidence/audit-unit-08.md) | Instrument §5; Hooks; Extending MCP; Session Lifecycle—Subagent | 34 | “The audit chain **MUST record** how the subagent’s `Intent.parsed` relates to the parent’s…” [9] | Parent hook/framework, Guardian, Guardian audit chain; MCP response enforcement | **Negative** — the required parent–child relation is recorded in the audit chain, not delivered to a running parent or child. |
| [ACS-04](evidence/audit-unit-09.md) | Instrument §6–§6.4: dispositions, result fields, MODIFY, honoring decisions | 28 | “For every step it submits, the Observed Agent **MUST wait** for the Guardian’s decision … and **MUST apply it**.” [4] | Guardian response envelope; Observed Agent enforcement; audit/replay tooling | **Negative** — a required decision is not a required topology or self-location disclosure. |
| [ACS-05](evidence/audit-unit-10.md) | Instrument §7–§7.2; Provenance and Trust Basis | 16 | “Provenance **MUST be populated by deterministic code outside the LLM’s output path**.” [4] | Deterministic framework boundary, Guardian, receiver-local trust policy | **Negative** — data-origin trust and provenance are distinct from execution-chain position. |
| [ACS-06](evidence/audit-unit-11.md) | Instrument §§8–§9.2; Intent, Agents, Identity, Session Lifecycle | 46 | “The SessionContext container … is **server-side state**”; the Guardian must include the resulting signed `chain_hash` in a response. [4] | Guardian-maintained SessionContext/audit chain; response integrity commitment | **Negative** — an opaque chain head is not a required readable predecessor/successor/depth/membership view or query. |
| [ACS-07](evidence/audit-unit-12.md) | Instrument §§10–11; ACS-Crypto and ACS-Audit profiles | 37 | ACS-Audit requires a `request_hash` on every ContextEntry, while Instrument §1 says the agent must not know hooks. [3] [4] | Transport/signature endpoints; Guardian audit chain; external observer/auditor | **Negative** — integrity/audit commitments remain outside an agent-readable topology interface. |
| [ACS-08](evidence/audit-unit-13.md) | Instrument §§12–13, §§17–17.1: policy/agent layers, liveness, errors | 17 | §12.2: “Receives the same input plus the deterministic layer’s intermediate output”; `system/ping` “carries no enforcement semantics and is not part of the audit chain.” [4] | Guardian deterministic/optional LLM layers; Observed Agent transport; deployment operations | **Negative** — the closest statement is non-modal and does not name chain-position evidence. |
| [ACS-09](evidence/audit-unit-14.md) | ACS-Trace; Trace Events; OpenTelemetry extension failure isolation | 24 | “The Trace pillar is decoupled from enforcement and runs out of the request/response path…” [3] [15] | Trace instrumentation, OTel/OCSF backends, trace sink, Guardian enforcement path | **Negative** — `parent_session_id` is a trace-side span attribute; the agent need not receive or query it. |
| [ACS-10](evidence/audit-unit-15.md) | ACS-Inspect and ACS-Inspect-Dynamic; Inspect wire methods; AgBOM update triggers | 27 | ACS-Inspect requires emitting `agbom/snapshot`; the Guardian must accept it, write it into SessionContext, and serialize it on request. [3] [17] | Observed Agent → Guardian inventory report; Guardian SessionContext and downstream serialization | **Negative** — component inventory/provenance is not execution-chain self-location. |

## Decisive evidence and locus analysis

### OWASP Top 10: the directions create external controls, not an agent-facing topology contract

The Top 10 does recognize multi-step and multi-agent risks. For example, ASI02 describes misuse in “agentic plans and delegation chains.” That statement identifies the problem domain; it does not direct an agent to inspect its chain location. The operative mitigation immediately locates a key control before execution:

> “A pre-execution Policy Enforcement Point (PEP/PDP) validates intent and arguments, enforces schemas and rate limits, issues short-lived credentials, and revokes or audits on drift.” [1]

The control locus is a **policy-enforcement component before action execution**, not the executing agent. Likewise, ASI03 asks operators to monitor indirect permission gains through delegation chains, while ASI04 asks them to monitor behavior, privilege use, lineage, and inter-module telemetry. These are express observability requirements, but neither names an in-agent predecessor, successor, depth, membership, or query mechanism. [1]

ASI08 is the most direct Top 10 near-miss. It directs systems to maintain lineage metadata for propagated actions, bound to cryptographic agent identities, for forensics, rollback validation, and accountability. [1] This is a meaningful lineage requirement. Its stated locus and purpose are **tamper-evident external logs and recovery/accountability systems**. The text does not further require that lineage metadata be resolved for the agent carrying out the action. The conclusion is therefore negative under the stated criterion, rather than an inference that lineage does not exist.

ASI09–ASI10 reinforce the allocation. Signed behavioral manifests are validated by orchestration services, and signing keys are not to be directly available to agents. [1] This is an explicit outside-agent enforcement model, not a topology-awareness requirement.

### ACS hooks and provenance: relationship records are intentionally outside the LLM output path

ACS is more explicit about architecture. Its Instrument specification states:

> “**The agent MUST NOT have knowledge of hooks.** Provenance fields, when emitted, **MUST be populated outside the LLM’s output path.**” [4]

This is decisive because several ACS controls contain relationship-like data. A `subagentStart` hook can include parent and child session fields, and Session Lifecycle requires the audit chain to record how child intent relates to parent intent. [5] [7] [9] Yet ACS assigns those fields to framework-to-Guardian hook traffic and Guardian-maintained audit state. It does not require delivery of the parent identifier, derivation category, chain depth, or membership set into the running child’s context. An audit record of parent–child derivation is therefore **not equivalent to a requirement that the child knows its parent or position**.

The same distinction controls the Provenance and Trust Basis material. ACS requires deterministic boundary code to populate provenance and requires receivers/Guardians to handle trust on the basis of data-origin facts. [4] [10] [11] This concerns **data lineage and trust assessment**, rather than an executing agent’s location among other execution steps. An implementation could combine the two, but the source does not require it.

### SessionContext and `chain_hash`: integrity commitments are not self-location

ACS requires Guardian-maintained SessionContext state and a signed rolling `chain_hash` on responses for steps where the Guardian writes a ContextEntry. [4] The companion schema describes ContextEntry as follows:

> “Append-only entry in a SessionContext’s audit chain. **Maintained server-side by the Guardian; not transmitted in full on the wire** …” [5]

A response chain head is not dismissed as irrelevant; it is a real integrity commitment at the response boundary. However, the required artifact has no required semantics that tell the agent who preceded or follows it, how many entries exist, which agents belong to the chain, or where the recipient lies. The standard does not require the agent to receive ContextEntries, retain prior heads, recompute the ledger, receive an inclusion proof, or query a Guardian for topology. The intended full verifier is an observer/auditor capable of recording traffic or recomputing the chain. [4] [5]

Accordingly, `chain_hash` is classified as **negative under this audit’s criterion**, not as silence. The standard expressly requires a cryptographic commitment, but not a usable agent-side chain-position interface. Treating any opaque commitment as “equivalent location” would erase the decision criterion’s requirement that the executing agent be able to establish its position.

### Handshake, decisions, and liveness: protocol controls do not add topology exposure

The handshake sources require capability/version/transport negotiation and prescribe how an Observed Agent and Guardian should behave on failure. The associated schema does not require a parent, predecessor, successor, membership, or depth field. [4] [6] Its audit and Trace handling exposes unguarded-session behavior to deployment observability, not to a running agent as position evidence.

ACS also requires the Observed Agent to wait for and apply a Guardian decision. [4] That is an enforcement obligation. A disposition, reason code, policy result, or an optional provenance citation can affect what the agent does, but the assigned rules do not require it to contain the agent’s broader-chain location. System liveness (`system/ping`) similarly has no enforcement semantics and is not part of the audit chain. [4]

### Trace and Inspect: observability and inventory stay external

The Trace specification expressly decouples Trace from enforcement and places it out of the request/response path:

> “The Trace pillar is decoupled from enforcement and runs out of the request/response path: deployments emit OpenTelemetry spans … and/or OCSF events to existing observability backends.” [15]

The relevant subagent span can carry `acs.subagent.parent_session_id`. [15] This is strong trace-side parentage information, but the requirement is to emit it to observability systems. No clause requires its return to an executing parent/subagent or grants that agent a trace query. OpenTelemetry failure isolation preserves the Guardian disposition even if the trace sink fails; it does not turn tracing state into an in-agent topology interface. [16]

ACS-Inspect has a parallel structure. The Observed Agent emits an AgBOM snapshot or mutation; the Guardian accepts or can deny it, writes it to the SessionContext audit chain, and serializes it for a downstream consumer. [17] The record may identify registration provenance, components, peers, or component graph changes. Those are inventory and artifact-origin facts. They do not normatively establish an agent’s live predecessor/successor, depth, execution membership, or a means for the agent to discover any of those facts. The server-side ContextEntry restriction remains applicable. [5] [17] [18]

## Why no unit is classified ambiguous

Several features were examined as possible counterexamples: “delegation chains,” required lineage metadata, `parent_session_id`, subagent derivation records, provenance `derived_from` fields, `parent_turn_id`, AgBOM peer/component relationships, and a signed `chain_hash`. None warranted an ambiguous classification because the reviewed text resolves the material issue in one direction: it either assigns the information to audit/trace/framework/Guardian infrastructure, treats it as data/artifact provenance, or does not require its delivery or query at the agent boundary.

The closest case is the signed chain hash. It reaches the response boundary and can be useful to an Observed Agent for integrity checking. But it is not self-describing topology, and the source does not require the agent to possess the other state or query capability needed to derive a position. Therefore the classification rests on an **explicit semantic and locus distinction**, rather than merely on silence.

## Interpretation of the null result

The report makes three limited propositions.

First, **explicit requirements found**: both standards require controls that can reconstruct, validate, constrain, or audit relationships outside the executing agent. The source text is not silent about lineage, delegation, provenance, or control; it provides a substantial external-control architecture. [1] [3] [4]

Second, **specified silence**: no reviewed clause directs that architecture to reveal enough chain topology to the executing agent for it to determine its position. This is the null finding. It applies to the audited versions and sections only.

Third, **interpretation held in reserve**: implementations could expose guardian state, show a policy response to an LLM, supply a parent identifier, issue an inclusion proof, or provide an audit/trace query. Those design choices could satisfy a different, implementation-level test. They do not change this requirements audit because the standards do not mandate them. The report therefore does not claim an inherent impossibility, nor does it infer vendor behavior from a public standard’s silence.

## Limitations

1. **Standards-text scope only.** This is not an implementation, penetration, usability, or vendor-runtime audit. A conforming deployment may voluntarily disclose more topology than the cited clauses require.
2. **Version and unit bounded.** The finding is confined to the 2026 v1.0 Top 10 PDF and ACS v0.1.0 at the stated pinned commits, in the 15 assigned units. Later editions, errata, binding profiles, or extension specifications can change the result.
3. **Different source normativity.** Top 10 guidelines are not RFC-style SHALL/MUST clauses. They were included as candidate requirements on a deliberately inclusive basis. ACS schema constraints and prose modals were counted as documented by each unit; the aggregate 516 is not a normalized or deduplicated measure of formal requirements.
4. **Boundary terminology is not uniformly defined.** OWASP does not define agent execution boundary or chain position. ACS distinguishes Observed Agent, framework, and Guardian, but an implementation may collapse or rearrange these components. This report does not infer a particular architecture beyond the locus expressed by the relevant text.
5. **Opaque commitment interpretation.** A signed `chain_hash` is recognized as agent-boundary integrity evidence. The negative classification depends on the stated criterion: without required entry history, neighbor/depth semantics, an inclusion proof, or a topology query, a hash alone does not establish the agent’s chain position. A broader definition that treats any commitment as “position” would be a different measurand.
6. **Data provenance is not execution topology.** Provenance, trust basis, AgBOM registration provenance, and component graphs could be extended to support chain analysis. The assigned clauses do not require them to encode or be exposed as the executing agent’s position in a wider execution chain.
7. **No failed-unit caveat applies.** All fifteen assigned units supplied a completed negative determination. Because there are no missing units, the overall result is not inconclusive on account of incomplete coverage.

## Conclusion

For the assigned WO-1 corpus, the evidence supports a **null standards result**: the reviewed OWASP Top 10 and ACS requirements mandate external controls for security, audit, lineage, provenance, policy, and traceability, but **do not mandate that an executing agent receive or query sufficient evidence to know its own position in an otherwise unobservable execution chain**.

The result should be used precisely. It demonstrates a public-standards requirement gap under the stated criterion. It does not demonstrate that no architecture can provide in-agent chain awareness, that external controls are ineffective, or that any specific product lacks such awareness.

## References

[1]: https://github.com/GenAI-Security-Project/GenAI-Security-Advisor/blob/613bf32a6f1d13eaf7b30040f7e9b779b23cfb7f/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf "OWASP Top 10 for Agentic Applications 2026, version 1.0"

[2]: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ "OWASP Top 10 for Agentic Applications for 2026"

[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md "OWASP Agent Control Standard v0.1.0 — Conformance Profiles (pinned commit)"

[4]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "OWASP Agent Control Standard v0.1.0 — Instrument Specification (pinned commit)"

[5]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/acs_schema.json "OWASP Agent Control Standard v0.1.0 — Schema aggregator"

[6]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/handshake.json "OWASP Agent Control Standard v0.1.0 — Handshake schema"

[7]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/hooks.md "OWASP Agent Control Standard v0.1.0 — Instrument hooks overview"

[8]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/extend_mcp.md "OWASP Agent Control Standard v0.1.0 — Extending MCP"

[9]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/session-lifecycle.md "OWASP Agent Control Standard v0.1.0 — Session Lifecycle"

[10]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/provenance.md "OWASP Agent Control Standard v0.1.0 — Provenance"

[11]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/trust.md "OWASP Agent Control Standard v0.1.0 — Trust Basis"

[12]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/intent.md "OWASP Agent Control Standard v0.1.0 — Intent"

[13]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/agents.md "OWASP Agent Control Standard v0.1.0 — Agents"

[14]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/identity.md "OWASP Agent Control Standard v0.1.0 — Identity"

[15]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/trace/events.md "OWASP Agent Control Standard v0.1.0 — Trace Events"

[16]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/trace/extend_opentelemetry.md "OWASP Agent Control Standard v0.1.0 — Extending OpenTelemetry"

[17]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/inspect/README.md "OWASP Agent Control Standard v0.1.0 — Inspect specification"

[18]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/agbom/document.json "OWASP Agent Control Standard v0.1.0 — AgBOM document schema"

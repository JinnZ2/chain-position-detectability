# WO-1 evidence record — ACS-07

## Audit identity and outcome

| Field | Record |
|---|---|
| Unit | **ACS-07** |
| Standard | **OWASP Agent Control Standard (ACS) v0.1.0** |
| Pinned source revision | `dc265475139a922824f0c817e2ecc2a2ce31c06c` |
| Scope reviewed | Instrument Specification §§10–11; the ACS-Core signature, canonical-input, and replay statements in Conformance; conditional ACS-Crypto and ACS-Audit profile conditions |
| Classification | **NEGATIVE** |
| Inside-agent chain-position requirement found | **No** |
| Normative statements/designations reviewed | **37** |

> **Criterion applied.** A result is POSITIVE only when a normative requirement puts information about the currently executing agent's position in a larger execution chain *inside that agent*: its predecessor, successor, depth, membership, or an equivalent locational fact must be received or queryable there. Gateway/Guardian lineage, audit state, traces, middleware, and after-the-fact verification are not sufficient unless the standard requires exposure across the agent execution boundary.

The scoped controls require message integrity, canonical serialization, replay rejection, cryptographic algorithm support, portable identifiers, and hashing of audit-request content. They do **not** require the executing agent to receive or query a predecessor, successor, nesting/delegation depth, chain membership, list of other agents, or comparable location. The closest related artifact, the Guardian-published `chain_hash`, is an opaque audit-chain head rather than a required, agent-readable execution-chain location; ACS does not require release of the entries, `previous_hash`, count/depth, membership, or subagent relationship that would make the hash locational. This record therefore remains negative rather than ambiguous.

## Source control and method

I cloned the named repository and read the complete Markdown source at the pinned commit, rather than relying on search snippets. These are Markdown specifications without page numbers; locations below give **document section and pinned-source line range**. Direct quotations preserve the source wording. “Normative statement/designation” includes a MUST/SHOULD/REQUIRED/RECOMMENDED/OPTIONAL term, a categorical prohibition, or a mandatory-format statement in an explicitly normative block. Repeated requirements in the Conformance document are counted as separately reviewed source clauses. The §10.1 registry's ten individual RECOMMENDED/OPTIONAL status designations are included in the count even though none requires chain-position exposure.

The document uses two distinct actors. The **Observed Agent** is “the LLM-backed system being monitored,” while the **Guardian Agent** is “the policy enforcement point.” [1] This matters: a Guardian-side cryptographic or audit control is not evidence inside the observed/executing agent. The standard also states, outside the narrow section scope but directly relevant to boundary interpretation: “**The agent MUST NOT have knowledge of hooks.**” [1]

## Clause-by-clause evidence and locus assessment

| # | Location and exact decisive language | Normative role | Locus of the control | Chain-position assessment |
|---:|---|---|---|---|
| 1 | Instrument §10, lines 332–334: “A signature over the §10 canonical input is **REQUIRED** in ACS-Core.” | Core integrity baseline. | Framework/Observed-Agent transport and Guardian protocol endpoint. | No predecessor, successor, depth, membership, or equivalent execution location is required. |
| 2 | §10, lines 334–336: “The signed input for every algorithm is the RFC 8785 (JCS) canonicalization of the request or response envelope with the `signature` field removed, encoded as UTF-8.” | Mandatory canonical-input definition. | Sender signs; receiver verifies. | The envelope includes a session identifier, but a session identifier and integrity binding do not identify the agent's position among other agents or steps. |
| 3 | §10, line 336: “A verifier **MUST** recompute this canonical form and **MUST** reject a signature that does not cover it.” | Two verification obligations. | Verifier, normally Guardian or recipient endpoint. | Message verification only; no chain-position datum is exposed to the executing agent. |
| 4 | §10, line 336: “The input is fixed by this rule, not declared per message” and “Alternative canonicalization is not permitted in v0.1.” | Fixed-format/prohibition control. | Protocol implementation. | No position data. |
| 5 | §10.1, lines 342–353: the registry designates `HMAC-SHA256` “**RECOMMENDED**”; `ECDSA-P256`, `RSA-PSS-SHA256`, `ML-DSA-65`, `ML-DSA-44`, `ML-DSA-87`, `SLH-DSA-128s`, `SLH-DSA-128f`, `ML-DSA-65+ECDSA-P256`, and `ML-DSA-65+RSA-PSS-SHA256` “**OPTIONAL**.” | Ten reviewed algorithm-status designations. | Deployment cryptographic configuration and protocol endpoints. | Cryptographic choice supplies no agent-local lineage or execution-chain position. |
| 6 | §10.2, line 359: “the `value` field carries the concatenation `len(pqc_sig) || pqc_sig || len(classical_sig) || classical_sig`” and “Verifiers **MUST** verify both component signatures over the canonical input defined in §10.” | Hybrid encoding and both-components verification obligation. | Sender/receiver cryptographic implementation. | No chain topology, ordering depth, or membership information. |
| 7 | §10.3, line 363: “Guardians **MUST** reject requests whose `timestamp` is more than the negotiated skew window … in the past or future.” | Replay/freshness protection. | Guardian. | Time freshness is not a predecessor/successor or chain-depth signal. |
| 8 | §10.3, line 363: Guardians “**MUST** reject duplicate `request_id` values within the session” and “**SHOULD** reject duplicate `nonce` values within a sliding window”; the default skew window is “**RECOMMENDED**” as `300000`. | Replay controls and recommendation. | Guardian replay store; Observed Agent uses the window only “for clock-drift diagnostics.” | A duplicate detector does not disclose which other steps or agents exist, nor where the executing agent sits among them. |
| 9 | §11, lines 365–372: “ACS **MUST** be deployable across IDE, SaaS, on-prem on Linux/Windows/macOS/mobile/browser.” | Portability obligation. | Deployment/platform. | No chain-position evidence. |
| 10 | §11, line 369: “Resource identifiers **MUST** use URI form.” | Portable naming obligation. | Protocol payload/framework. | URI syntax does not entail an execution-chain relationship. |
| 11 | §11, lines 370–372: “Capability vocabulary uses abstract names”; “Identity descriptors carry a `type` discriminator”; and “Authentication mechanism declared in handshake; spec mandates none.” | Remaining explicitly normative portability constraints. | Protocol schema and handshake/deployment. | Identity *type* and authentication declaration do not require disclosure of other chain participants or the current agent's location. |
| 12 | Conformance, §ACS-Core, lines 26–28: “A v0.1.0-conformant deployment **MUST** implement ACS-Core.” | Applicability condition for the Core summary. | Whole deployment. | Does not add an agent-local execution-chain requirement. |
| 13 | Conformance, §ACS-Core, lines 31, 35–36: “`request_id`, `timestamp`, `acs_version`, `metadata` required on every request”; “Guardians **MUST** reject replays”; and “every request and response carries a signature over the canonical envelope.” | Core restatement of envelope, replay, and signature requirements. | Sender/Guardian transport boundary. | Request metadata and signed transport do not reveal predecessor, successor, depth, membership, or equivalent position. |
| 14 | Conformance, §ACS-Crypto, line 80: “A deployment claiming ACS-Crypto **MUST** support at least `ML-DSA-65` … and **SHOULD** support `SLH-DSA-128s`”; “Hybrid composites … are **OPTIONAL**.” | Conditional profile obligations/designation. | Deployment cryptographic capability. | Cryptographic support provides integrity/non-repudiation capabilities, not chain-location visibility inside the executing agent. |
| 15 | Conformance, §ACS-Crypto, lines 81–84: “ACS-Crypto replaces or augments the baseline with asymmetric and post-quantum algorithms, which add the non-repudiation and external verifiability the symmetric baseline cannot give.” | Explanatory profile consequence, not an additional agent-exposure obligation. | External verifier/auditor and cryptographic endpoints. | “External verifiability” is expressly outside the executing-agent boundary and is negative under the criterion. |
| 16 | Conformance, §ACS-Audit, lines 86–88: “A deployment claiming ACS-Audit **MUST** populate `request_hash` … on every ContextEntry, ensuring the chain commits to request content, not just step metadata.” | Conditional audit-chain content-commitment obligation. | Guardian-managed SessionContext/audit chain. | Hashing request content proves/tampers-evidences audit material; it does not require the agent to receive or query chain membership, a predecessor, successor, or depth. |
| 17 | Conformance, §ACS-Audit, line 88: “ACS-Audit deployments **SHOULD** also populate `timestamp` and `provenance_summary` on every ContextEntry.” | Conditional audit enrichment recommendations. | Guardian-managed audit ContextEntry. | `timestamp` and provenance aggregation remain audit-side. Neither is a mandatory agent-local chain-position interface. |

### Count reconciliation

The **37** reviewed atomic statements/designations consist of: seven §10 signature/canonical-input constraints; ten §10.1 algorithm statuses; two §10.2 hybrid encoding/verification constraints; four §10.3 replay/freshness statements; five §11 portability constraints; three ACS-Core applicability/restatement statements; three ACS-Crypto profile statements; and three ACS-Audit profile statements. Several items are grouped into the table for readability but were each assessed independently. The count deliberately includes OPTIONAL/RECOMMENDED statuses because the assignment calls for full normative-clause review; they do not turn into affirmative chain-position duties.

## Nearest adjacent control, and why it does not change the result

The relevant adjacent SessionContext rule is deliberately separated from the scoped signature/audit controls. Instrument §8.6 requires the **Guardian**, for content-bearing steps, to include the resulting `chain_hash` in its response and cover it with the response signature. [4] The standard describes this as allowing “an observer that records traffic” to detect later rewrite, and says an “Observed Agent or external auditor” finding an inconsistent head **SHOULD** treat it as an integrity event. [4]

This is the strongest plausible counterargument to a negative finding. It does put a *hash value* on the wire, and an implementation may retain it. However, it is insufficient under the stated criterion for four reasons.

1. The mandatory disclosure is an opaque **audit-chain head**, not a required presentation of a prior entry, a next entry, agent/subagent parent, successor, depth/count, participant membership, or other locational relationship.
2. SessionContext is explicitly “server-side state” whose container “remains implementation-defined”; the standardized portion is the wire-visible commitment, not a required queryable chain view. [4]
3. The standard directs the Guardian to write and compute entries and mentions an outside observer/external auditor. It does not require the LLM/runtime executing inside a sandbox to inspect, interpret, or be provided the historical chain material needed to turn the digest into position.
4. The Audit profile strengthens only `request_hash`: a JCS hash of request parameters. It commits content, “not just step metadata”; it does not add a positional attribute or agent-facing query interface. [3]

Accordingly, the hash creates tamper-evidence for the Guardian/external audit boundary, not detectability of an otherwise hidden larger execution chain from within the agent boundary. No ambiguity remains in the scoped language: there is no qualifying mandatory exposure requirement.

## Control-locus summary

| Locus | Controls found | Result for criterion |
|---|---|---|
| **Observed-Agent framework / transport endpoint** | Creates or accepts signed envelopes; supplies request ID/timestamp; may use skew window for diagnostics. | Has message metadata, but no required execution-chain location. |
| **Guardian** | Recomputes/verifies canonical signatures; rejects replay; maintains ContextEntry/audit state; populates ACS-Audit hashes. | Primary locus for replay and audit-chain facts; this is outside the executing agent for the criterion. |
| **Deployment / handshake / key management** | Chooses keys/algorithms and platform/authentication implementation; advertises profiles. | Configuration/cryptography, not chain visibility. |
| **External observer/auditor** | Can record traffic and test published chain-head consistency; gains external verifiability with ACS-Crypto. | Explicitly an external audit locus; negative by rule. |
| **Executing LLM/agent** | The standard says it “MUST NOT have knowledge of hooks.” | No normative predecessor/successor/depth/membership interface found. |

## Limitations and preserved uncertainty

This is a requirements audit, not an implementation claim. A vendor can voluntarily expose orchestration topology, an ancestor ID, a subagent tree, or a decoded audit view to an agent; nothing in the reviewed ACS text requires it. Conversely, an opaque `chain_hash` might be paired with proprietary state in a particular system. Such extensions do not change the ACS v0.1.0 normative result. The standard's use of “Observed Agent” includes an LLM-backed system and surrounding framework, so the conclusion is conservative: even at that broader boundary, the required data is only signed message/session/audit material, not usable execution-chain position.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md#L1-L57 "ACS v0.1.0 Instrument Specification — title, design principles, and architecture"
[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md#L332-L372 "ACS v0.1.0 Instrument Specification — §§10–11"
[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md#L26-L45 "ACS Conformance — ACS-Core"
[4]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md#L248-L299 "ACS v0.1.0 Instrument Specification — SessionContext and chain-head publication"
[5]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md#L78-L88 "ACS Conformance — ACS-Crypto and ACS-Audit"

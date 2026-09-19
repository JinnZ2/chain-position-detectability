# ACS-01 — OWASP Agent Control Standard v0.1.0

**Unit.** Conformance Profiles: profile declaration and ACS-Core; Instrument Specification §§1–3; incorporated ACS v0.1.0 schema requirements.

**Result: NEGATIVE.** **No normative requirement was found that makes the executing agent itself receive or query its predecessor, successor, chain depth, membership, or an equivalent location in a larger execution chain.** ACS does require relationship and lineage material in several places, but the requirements locate it in an **Observed Agent framework-to-Guardian hook**, a **Guardian-maintained SessionContext/audit chain**, a **Guardian-derived policy result**, or optional trace/audit material. These are not a mandated interface inside the executing LLM/agent boundary. The standard expressly requires the opposite for hooks: the agent must not know them.[2]

**Status:** OBSERVED. The conclusion is limited to the pinned v0.1.0 sources and the schema package they reference. No implementation behavior is inferred.

## Decision rule applied

A POSITIVE result requires a normative requirement that exposes to the executing agent a predecessor, successor, depth, membership, or comparable location in a wider execution chain. An event emitted by the agent framework to a Guardian is not sufficient. Neither are Guardian policy state, server-side audit records, trace events, or a rolling integrity commitment, unless the standard further requires their topology/position meaning to be available inside the agent execution boundary. Ambiguity would be retained where the source requires such exposure but does not identify the recipient.

The specification distinguishes the **Observed Agent** (the LLM-backed system) from the **Guardian Agent** (the policy enforcement point). It then directs that hooks and deterministic metadata remain out of the LLM output path. I therefore treat a required hook field as a framework/Guardian control unless the source separately mandates delivery to, or query by, the executing agent/LLM.[2]

## Authoritative-source coverage and review count

The repository was checked out at the exact supplied commit `dc265475139a922824f0c817e2ecc2a2ce31c06c`; the public schema entry point reports version `0.1.0` and resolves its modular `$ref` package.[1] [3]

**Clause count reviewed: 166 explicit RFC-style normative-modal occurrences.** This consists of 21 in the complete supplied Conformance Profiles page, 5 in Instrument §§1–3, and 140 in the v0.1.0 modular schema package, including the profile-specific variants referenced by Conformance. In addition, the review inspected all **787 JSON Schema validation-keyword instances** in that package (`required`, `oneOf`, `enum`, `pattern`, `const`, bounds, and related constraints). The latter are schema constraints rather than prose clauses and are reported separately to avoid presenting them as 787 RFC 2119 sentences. Examples, diagrams, and non-normative commentary were read for context but were not treated as requirements.

The profile-specific sections outside ACS-Core were reviewed because they occur in the supplied Conformance page and can add schema strictness. None changes the result: Trace routes facts to trace events, Inspect serializes for the Guardian, Provenance is populated by deterministic boundary code, Crypto signs messages, and Audit commits request material to ContextEntry. None mandates chain-position exposure inside the executing agent.[1]

## Decisive evidence

### 1. The specification excludes hook knowledge from the agent/LLM

Instrument §1, Design Principle 2, states:

> “**The agent MUST NOT have knowledge of hooks.** Provenance fields, when emitted, **MUST be populated outside the LLM's output path.**” [2]

This is the clearest locus rule in the unit. It is a normative prohibition/placement requirement: hook-derived control information is not required to enter the executing LLM. It defeats an inference that a hook event or metadata field automatically makes its contents available to the agent as chain-position evidence.

### 2. ACS-Core requires a Guardian-published chain *commitment*, not a readable chain position

Conformance §ACS-Core requires a SessionContext and an append-only ContextEntry chain “with the **Guardian publishing the chain head** (`chain_hash`) on responses for content-bearing steps.”[1]

The incorporated ContextEntry schema makes the locus explicit:

> “Append-only entry in a SessionContext's audit chain. **Maintained server-side by the Guardian; not transmitted in full on the wire** (the wire-visible commitment is `chain_hash` inside the request envelope's metadata.session_state).” [4]

The response schema further requires the Guardian to put `chain_hash` on a response **only** when it wrote a ContextEntry; the stated function is that “an observer that records traffic” can detect a later rewrite.[5]

A rolling hash is an opaque integrity commitment. It does not specify a predecessor or successor identity, child/parent relation, chain depth, membership list, or a query operation that reveals them. More importantly, its authoritative chain remains Guardian-side. Thus it is negative under the stated rule, not ambiguous.

### 3. The closest apparent counterexample is an audit-hook relationship, not child-side awareness

The `subagentStart` schema requires `subagent_session_id`, `parent_session_id`, `parent_step_id`, and `intent_derivation`.[6]

> “Sessions are per-subagent: each subagent gets its own `session_id` and SessionContext; **the parent–child relation is captured here.**” [6]

The phrase “captured here” is important but not sufficient. Under Instrument §2, the Observed Agent sends hook traffic to the Guardian, which validates the envelope and loads SessionContext; it is not a required child-facing capability.[2] The same schema says that the **subagent's own** later hooks carry its own `metadata.session_id`; it does not require the framework to deliver `parent_session_id` or `parent_step_id` to the subagent's execution context.[6]

The companion `subagentStop` schema is also deliberately parent/audit-side:

> “the parent receives the subagent-stop notification **on its own audit chain**; the subagent's own session has by this point already emitted its `sessionEnd` … This hook lets the parent's audit chain reference the subagent's terminal state **without merging the two chains**.” [7]

This is valuable parent-side audit linkage and may enable Guardian policy. It is nevertheless an audit-chain record, and the child is already terminated. It does not normatively place a predecessor/successor/depth/membership view inside the child or its LLM. **Negative.**

## Clause and control-locus ledger

| Source / normative control | Exact or decisive requirement | Locus of the control | Chain-position result |
|---|---|---|---|
| Conformance, Profile declaration | “Profiles are declared in the handshake.” A Guardian “MAY refuse a session” where a required profile is not declared.[1] | Client/Observed-Agent ClientHello and Guardian ServerHello. | Declares capabilities, not execution-chain location. **Negative.** |
| Conformance, ACS-Core applicability | “A v0.1.0-conformant deployment **MUST implement ACS-Core**.”[1] | Deployment-wide conformance requirement. | Does not expose a chain position. **Negative.** |
| Conformance, ACS-Core envelope/replay/integrity | `request_id`, `timestamp`, `acs_version`, and `metadata` are required; “Guardians **MUST reject replays**”; request/response signatures are required by Core.[1] | Wire envelope and Guardian verification. | Per-request identity/integrity, not predecessor/successor/depth/membership. **Negative.** |
| Conformance, hook taxonomy | Extra hooks “**SHOULD be implemented** when the harness can observe” an event; skill hooks are also SHOULD in the stated condition.[1] | Harness observation and Guardian capability negotiation. | Observation is not mandated exposure to the executing agent. **Negative.** |
| Conformance, decision honoring | Observed Agent “**MUST wait** for the Guardian's decision … and apply it.”[1] | Guardian-to-Observed-Agent decision channel. | Requires a decision, not a topology/position disclosure. **Negative.** |
| Instrument §1, design principle 2 | Agent “**MUST NOT have knowledge of hooks**”; provenance “**MUST** be populated outside the LLM's output path.”[2] | Deterministic framework / boundary code outside LLM. | Explicitly prevents treating hooks as agent-visible chain awareness. **Negative.** |
| Instrument §2, architecture | Observed Agent “sends hook traffic to the Guardian”; Guardian deterministic layer runs first.[2] | Guardian enforcement plane. | Relationship information that hooks carry is sent outward for enforcement. **Negative.** |
| Instrument §3, baseline wire format | Unknown fields are ignored. For batches, Guardian **SHOULD** accept arrays; if it does not, it **MUST** return `-32600`; each request is independently evaluated with no cross-request dependency semantics.[2] | Guardian JSON-RPC endpoint. | It expressly declines cross-request dependency semantics; no chain-position API is defined. **Negative.** |
| Schema, request metadata | Request schema requires `metadata.agent_id` and `metadata.session_id`; optional `parent_turn_id` is a “wire-level shortcut so per-step audit entries don't need to walk the chain.”[8] | Observed-Agent framework to Guardian envelope/audit. | Agent and session identifiers, plus optional intra-turn audit correlation, are not a mandatory view of a larger agent chain. **Negative.** |
| Schema, handshake | Profile fields are arrays; `acs-core` “SHOULD always be included.” `profiles_accepted` is Guardian-selected from client claims.[9] | Handshake negotiation. | Capability negotiation, not location. **Negative.** |
| Schema, ContextEntry and response | ContextEntry is Guardian-maintained and not transmitted in full; response `chain_hash` is a signed commitment after Guardian append.[4] [5] | Guardian SessionContext/audit chain; wire commitment. | No readable or queryable execution-chain position. **Negative.** |
| Schema, subagent start/stop | Parent-child IDs are required on the **parent's spawn hook**; terminal child data goes to the **parent's audit chain**.[6] [7] | Parent framework/Guardian audit processing. | The closest relationship record is not required inside the subagent execution. **Negative.** |
| Schema, turn and skill linkage | Framework **MUST** propagate a `turn_id`; nested `parent_turn_id` is optional. `skillLoad.load_path` allows Guardian depth/containment policy and `parent_step_id` anchors audit replay.[10] [11] | Framework metadata and Guardian policy/audit. | Intra-session/skill causality is optional or Guardian-oriented, not agent self-location in a larger execution chain. **Negative.** |
| Schema, provenance and compaction | Provenance is deterministic boundary code, `derived_from` is data-lineage edges, and summaries/depth are Guardian-computed and optional. Post-compaction lineage is framework-computed and Guardian-enforced.[12] [13] [14] | Data provenance and Guardian policy; LLM excluded. | This is lineage of **data**, not mandated awareness of an agent's predecessor/successor/depth/membership in an execution chain. **Negative.** |

## Treatment of potentially confusing features

**Profile sets are not membership in an execution chain.** `profiles_supported` and `profiles_accepted` state which ACS capabilities a client claims and a Guardian accepts. They can identify a negotiated control profile, but not whether the execution is upstream/downstream of another agent or how many nodes exist.[1] [9]

**Agent/session IDs do not amount to position.** The request envelope requires `agent_id` and `session_id`, but no schema field requires an incoming actor to disclose parent agent identity, downstream agent identity, a route, a hop count, or a full execution membership list to the LLM. A `parent_turn_id` is optional and concerns nesting of turns, not mandated broader agent-chain awareness.[8] [10]

**Data provenance is not execution topology.** `derived_from` is a provenance-ID edge for data. The standard says it is generated at channel boundaries by deterministic code, and the Guardian computes trust against local policy. Even `max_lineage_depth` is optional and refers to a chain of derived data, not an agent's place among executing agents.[2] [12] [13]

**The subagent schemas do not reverse the conclusion.** They are strong Guardian/audit instrumentation: they make it possible to reconstruct a parent–child spawn from events. But the criterion expressly excludes middleware traces and audit logs absent a requirement that the information be exposed within the executing agent boundary. Here the source gives no such requirement and says hooks are unknown to the agent.[2] [6] [7]

## Conclusion and limitations

This unit implements **external, Guardian-centered instrumentation**, including integrity commitments and reconstructable parent-child audit events. It does **not** normatively establish an in-agent query or input for chain position. The strict result is therefore **negative** rather than ambiguous.

The result does not claim that an implementation cannot choose to pass parent/child metadata to a subagent, display the Guardian response to an LLM, or add an application-specific topology API. Those could create inside-agent awareness, but they are deployment extensions rather than requirements of the reviewed v0.1.0 unit. It also does not assess A2A wrapping deferred by the specification to v0.2, or other ACS pages except where the supplied schema package and Conformance page incorporate/describe them.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md "OWASP Agent Control Standard v0.1.0 — Conformance Profiles (pinned commit)"

[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "OWASP Agent Control Standard v0.1.0 — Instrument Specification (pinned commit)"

[3]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/acs_schema.json "ACS Schema v0.1.0 aggregator"

[4]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/context-entry.json "ACS v0.1.0 ContextEntry schema"

[5]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/response-envelope.json "ACS v0.1.0 Response Envelope schema"

[6]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/subagent-start.json "ACS v0.1.0 subagentStart hook schema"

[7]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/subagent-stop.json "ACS v0.1.0 subagentStop hook schema"

[8]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/request-envelope.json "ACS v0.1.0 Request Envelope schema"

[9]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/handshake.json "ACS v0.1.0 Handshake schema"

[10]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/turn-start.json "ACS v0.1.0 turnStart hook schema"

[11]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/skill-load.json "ACS v0.1.0 skillLoad hook schema"

[12]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/provenance.json "ACS v0.1.0 Provenance schema"

[13]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/provenance-summary.json "ACS v0.1.0 Provenance Summary schema"

[14]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/post-compact.json "ACS v0.1.0 postCompact hook schema"

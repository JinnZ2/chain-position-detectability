# ACS-02 — Capability-Negotiation Handshake and Handshake Failure

**Standard and unit.** OWASP Agent Control Standard (ACS) v0.1.0, Instrument §4 and §4.1, including the §4-incorporated `handshake.json` schema. **Result: NEGATIVE.**

## Finding

This unit requires an **Observed Agent** to exchange session-control capabilities with a **Guardian Agent**, and it specifies what the Observed Agent does if no `ServerHello` arrives. It does **not** require the executing agent to receive or query information about its predecessor, successor, depth, membership, parent/child relationship, or any equivalent location in a larger execution chain. Its inbound `ServerHello` is confined to version, methods evaluated, transport, timeout and failure posture, provenance-policy status, supported formats, tracing configuration, and accepted conformance profiles. These are enforcement and deployment-capability facts, not chain-position facts.[1] [2]

The strongest negative evidence is the complete required `ServerHello` shape: `negotiated_version`, `methods_evaluated`, `selected_transport`, and `timeout_config` are required, while every other described field remains a control-plane property; no field represents a predecessor, successor, chain depth, agent membership, delegation parent, or comparable execution-chain location.[2] The authoritative prose reinforces that narrow purpose: “**Required at session start, before any hook traffic.**”[1]

> **Criterion applied.** A positive result would require a normative obligation that puts evidence of chain position **inside the executing agent**—for example, a required field or query that tells it who invoked it, who will consume its result, its depth, its membership, or an equivalent relative location. A gateway/Guardian’s view, deployment log, Trace sink, middleware event, or post-hoc audit record is not enough unless the standard requires disclosure of that information within the agent execution boundary.

## Authority, boundary, and verification

The review is limited to **Instrument §4, including §4.1**, and the versioned handshake schema expressly incorporated by §4. It does not treat other ACS sections as evidence, even where they may discuss provenance or SessionContext. The GitHub source is pinned to commit `dc265475139a922824f0c817e2ecc2a2ce31c06c`; the audited raw file retrieved from that commit had SHA-256 `2677d4be157d0a806546332c3a06c43d77d0825dcb789983e65d03c70aecf`. The separately supplied schema was retrieved at its v0.1.0 URL and had SHA-256 `9fabf14e732372cdcab4923bd977ecd9fcd32896e4e4126cc460a640e0d627ab`.[1] [2]

For the count below, a **clause** is a distinct operative statement or schema constraint in the unit, including RFC-style `MUST`/`SHOULD`/`MAY`, declarative mandatory behavior in the normative §4.1 subsection, and `required` schema predicates. Duplicated requirements occurring once in prose and once in the schema are separately listed so both authoritative sources are fully reviewed. Pure field catalogues, diagrams, explanatory rationale, and version-history commentary are identified but not inflated into separate requirements.

## Complete normative/operative-clause review (34 clauses)

| No. | Location | Exact decisive language | Locus of control | Chain-position result |
|---:|---|---|---|---|
| 1 | §4, opening | “**Required at session start, before any hook traffic.**” | Observed Agent/Guardian protocol boundary | Governs timing only; no chain fact is supplied to the agent. |
| 2 | §4, version sentence | “Version mismatch terminates with `UNSUPPORTED_VERSION` (`-32001`, §17.1).” | Guardian response / protocol | Version compatibility is not predecessor, successor, depth, or membership. |
| 3 | §4, version sentence | “Unknown fields **MUST** be ignored.” | Both wire endpoints | Forward compatibility; does not require an in-agent chain-position extension. |
| 4 | §4, provenance refusal | “the Guardian **MUST** refuse the session at handshake time with `PROVENANCE_REQUIRED` … rather than silently degrading enforcement.” | Guardian | Refusal is made by the policy-enforcement endpoint. The prerequisite is provenance-production mode, not chain location. |
| 5 | §4.1, sentence 1 | “the Observed Agent applies its **startup posture**, configured out of band” when `handshake/hello` fails. | Observed Agent, using deployment configuration | Startup behavior tells the agent only whether to proceed/refuse after no answer. It does not identify another step in an execution chain. |
| 6 | §4.1, sentence 1 | “`proceed` starts the session unguarded, `refuse` does not start it.” | Observed Agent | Local failure posture, not location relative to another agent. |
| 7 | §4.1, sentence 1 | “The default is `proceed`” | Deployment/default applied by Observed Agent | Default availability posture; no chain evidence. |
| 8 | §4.1, sentence 2 | “A Guardian that answers with a refusal … has decided; the startup posture applies only when no answer arrives.” | Guardian and Observed Agent | Distinguishes response states, not chain states. |
| 9 | §4.1, sentence 2 | “A session started unguarded **MUST** be recorded in the deployment’s own audit log” | Deployment audit log, explicitly outside Guardian | Explicitly external audit evidence. It is negative under the criterion and is not required to be exposed inside the agent. |
| 10 | §4.1, sentence 2 | “and **SHOULD** be surfaced on Trace events when the deployment claims ACS-Trace.” | Trace system / deployment | Observability event, not an in-agent chain-position interface. |
| 11 | §4.1, sentence 2 | “The Observed Agent **SHOULD** retry the handshake for subsequent sessions.” | Observed Agent | Retry requirement exposes no predecessor/successor/depth/membership fact. |
| 12 | Schema root description | “Unknown fields **MUST** be ignored at every level.” | Both wire endpoints | Repeats row 3 in the incorporated schema; does not mandate a chain-position field or query. |
| 13 | Schema, `$defs/ClientHello.required` | `acs_versions_supported`, `methods_implemented`, `transports_supported`, and `provenance_producer` are required. | Observed Agent sends ClientHello | Required facts are capability/provenance-mode declarations. None is execution-chain position. |
| 14 | Schema, `methods_implemented` description | “clients **SHOULD** include [ `system/ping` ].” | Observed Agent | Liveness capability, not a chain relation. |
| 15 | Schema, `provenance_producer` description | “`deterministic` is **REQUIRED** for information-flow paradigms and for deployments claiming ACS-Provenance.” | Observed Agent/framework producer | Requires deterministic provenance production, but does not require provenance to identify an agent’s predecessor, successor, depth, or membership. |
| 16 | Schema, `provenance_producer` description | “Guardians whose policies require Provenance **MUST** refuse the session at handshake time rather than silently degrading enforcement.” | Guardian | Same substantive control as row 4, stated by the schema. It places the decision with Guardian, not chain position inside the executing agent. |
| 17 | Schema, `wrapped_protocols` description | “A2A is reserved for v0.2 and **MAY** be advertised for forward-compatibility” | Observed Agent | Permission to advertise a protocol, not a requirement to disclose chain position. |
| 18 | Schema, `profiles_supported` description | “`acs-core` is the mandatory baseline and **SHOULD** always be included.” | Observed Agent | Profile declaration; no chain relation is represented. |
| 19 | Schema, `$defs/ServerHello.required` | `negotiated_version`, `methods_evaluated`, `selected_transport`, and `timeout_config` are required. | Guardian sends; Observed Agent receives | This is the clearest inbound shape. It provides negotiated controls only, not a parent, child, predecessor, successor, depth, or membership fact. |
| 20 | Schema, `negotiated_version` | “**MUST** match the client’s major version.” | Guardian’s selected value / Observed Agent validation | Version relation only. |
| 21 | Schema, `methods_evaluated` | “Clients **MAY** still emit them for audit” | Observed Agent | Permission to emit non-evaluated methods is audit-related and contains no location evidence. |
| 22 | Schema, `methods_evaluated` | “but **MUST** treat them as ALLOW-by-default.” | Observed Agent | Local enforcement default; no chain-position fact. |
| 23 | Schema, `signature_algorithms_supported` | “`HMAC-SHA256` is the v0.1 **RECOMMENDED** default” | Deployment/Guardian capability | Cryptographic selection only. |
| 24 | Schema, `timeout_config.default_ms` | “deployments **SHOULD** budget per-method timeouts against each step’s latency tolerance” | Deployment | Timing policy, not execution-chain location. |
| 25 | Schema, `skew_window_ms` | “the **RECOMMENDED** default is 300000 (5 minutes)” | Guardian/deployment configuration | Replay-window default only. |
| 26 | Schema, `skew_window_ms` | “deployments with well-synchronized clocks **SHOULD** tighten it.” | Deployment | Clock control, not agent-chain awareness. |
| 27 | Schema, `on_decision_failure` | “Every fail-open proceed **MUST** be recorded as an audit event.” | Audit system/deployment | External audit record. No requirement exposes a chain fact to the agent. |
| 28 | Schema, `on_decision_failure` | “A decision that arrives within the timeout **MUST** be honored regardless of this posture.” | Observed Agent | Requires honoring Guardian’s decision; it does not cause the decision to contain chain location. |
| 29 | Schema, `policy_requires_provenance` | “clients with `provenance_producer='none'` **MUST** be rejected before session starts.” | Guardian | Repeats rows 4/16 as a server-policy constraint; no position information is sent to the executing agent. |
| 30 | Schema, `agbom_serializations_supported` | “Deployments claiming ACS-Inspect **MUST** include at least one of `{cyclonedx-1.6, spdx-3.0, swid}` in addition to `canonical`” | Deployment/Guardian rendering capability | Artifact-serialization capability; not an agent-chain relation. |
| 31 | Schema, `agbom_serializations_supported` | “Guardians not claiming ACS-Inspect **MAY** omit this field.” | Guardian | Field-omission permission; no chain evidence. |
| 32 | Schema, `trace_emission` | “Deployments claiming ACS-Trace **MUST** emit Trace events … for every supported ACS step.” | Guardian or co-deployed Trace sink | Explicitly tracing/observability. It remains negative because it does not require exposure inside the executing agent. |
| 33 | Schema, `trace_emission` | “Deployments not claiming ACS-Trace **SHOULD** still emit Trace events where feasible.” | Deployment / Trace sink | Same external observability locus. |
| 34 | Schema, `profiles_accepted` | “A Guardian **MAY** refuse a session if the client does not declare a profile the Guardian’s policy requires.” | Guardian | Profile-policy refusal; it does not provide chain position to the Observed Agent. |

## Relevant wire surfaces and their loci

The ClientHello is an outbound declaration made by the Observed Agent. Its required elements state which ACS versions, methods, transports, and provenance-production mode it supports. `profiles_supported` is optional in the schema; when used, it declares conformance capabilities.[2] This surface neither carries a caller identity nor asks the Guardian for the Observed Agent’s place in a multi-agent execution chain.

The ServerHello is an inbound Guardian response. Its mandatory values are protocol version, method subset, selected transport, and timeouts. Optional values cover signing algorithms, clock skew, failure posture, ASK approver types, whether Guardian policy requires provenance, Inspect serialization, Trace configuration, and profiles accepted.[2] None encodes an agent-chain predecessor, successor, depth, membership, spawn relationship, delegation parent, or return-path consumer. In particular, `methods_evaluated` says only which **method names** Guardian will evaluate. It does not state who caused an individual invocation or where the Observed Agent sits in a larger chain.

The provenance-required condition is a potentially confusing control but does not change the result. It compares the ClientHello’s **producer mode** (`deterministic` or `none`) with a Guardian policy requirement, then refuses where those are incompatible.[1] [2] The unit does not require the executing agent to receive a provenance graph, inspect its own provenance, or infer its execution-chain position from provenance. A provenance policy is therefore not a positive result under this criterion.

The no-ServerHello path is also not a positive result. Section 4.1 requires a locally applied startup posture, sends an unguarded-session record to the **deployment’s own audit log**, and conditionally surfaces a Trace event.[1] The audit and Trace controls may make a deployment observable to operators, but they are expressly not a requirement that chain information be made available inside the agent.

## Non-normative material distinguished from requirements

The §4 sequence diagram is an illustration. Its note that “Hook traffic begins only after negotiation succeeds” depicts the negotiation sequence; the binding session-start requirement and schema constraints are recorded in rows 1 and 13–19. The §4 lists of ClientHello and ServerHello fields are explanatory catalogues; the actual required fields are the schema’s `required` arrays (rows 13 and 19).[1] [2]

In §4.1, “so a Guardian outage does not block new sessions” explains the operational rationale for the default rather than adding a separate chain-position obligation. Likewise, the sentence that mid-flight attachment is “undefined in v0.1” and deferred to v0.2 identifies a scope gap; it does not require the Observed Agent to learn any chain relationship.[1]

## Conclusion and uncertainty

**NEGATIVE.** Across all 34 operative clauses/constraints in this unit, no normative requirement places evidence of the agent’s position in a larger execution chain inside the executing agent. The unit instead establishes a two-party, pre-hook control-plane negotiation and defines Guardian, deployment, audit, and Trace behavior. Its strongest potentially adjacent concept—provenance-required refusal—is a Guardian policy decision about whether deterministic provenance is produced; it is not an in-agent chain-position disclosure.[1] [2]

This is a finding of **absence of a qualifying requirement**, not a claim that deployments cannot add proprietary fields or that an agent can never infer context by other means. In fact, the requirement to ignore unknown fields means a deployment could transmit extensions, but §4 neither requires those extensions nor requires the Observed Agent to use them for chain-position awareness.[1] [2] The result would need revision only if an authoritative normative extension or another assigned unit requires a field/query that provides the executing agent with its predecessor, successor, depth, membership, or equivalent chain location.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "OWASP Agent Control Standard v0.1.0 Instrument Specification, §4–§4.1 (pinned commit dc265475139a922824f0c817e2ecc2a2ce31c06c)"
[2]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/handshake.json "ACS Handshake JSON Schema v0.1.0"

# ACS-08 Evidence Record — Policy/Agent Layers, Liveness, and Error Handling

**Standard:** OWASP Agent Control Standard (ACS) v0.1.0
**Assigned unit:** Instrument §§12–13 and §§17–17.1 — Policy/Agent Layers, Liveness, and Error Handling
**Assessment:** **NEGATIVE**
**Status:** **DERIVED** from the observed source text under the work order’s strict test: a positive result requires a *normative* requirement that exposes an executing agent’s predecessor, successor, depth, membership, or equivalent chain location to that agent.

## Conclusion

No normative requirement in the assigned unit requires chain-position evidence to be placed **inside an executing agent**. Section 12.2 contains the closest language: “**Receives the same input plus the deterministic layer's intermediate output**.” It is an architectural description, not a modal requirement, and it neither requires agent-visible predecessor/successor/depth/membership information nor defines a query by which the agent can obtain it. The mandatory controls in that section instead constrain prompt treatment, isolation from policy code, and decision logging. [1]

The liveness rules deliberately separate `system/ping` from enforcement and from the SessionContext audit chain. The error registry standardizes wire errors and recovery advice for the **Observed Agent** and Guardian boundary, including a `CHAIN_MISMATCH` condition, but does not require the executing agent/LLM to receive an interpretable chain location. A chain hash mismatch is an integrity comparison, not a predecessor, successor, depth, or membership disclosure. [1]

Accordingly, `inside_agent_requirement_found` is **false**. The result is **negative**, rather than ambiguous, because the unit has no normative language that could satisfy the stated positive test. The one potentially suggestive agent-input sentence is expressly non-normative and underspecified as to what, if any, SessionContext state is visible to the agent layer.

## Scope, source control, and counting

This review used the complete pinned Markdown specification at commit `dc265475139a922824f0c817e2ecc2a2ce31c06c` and the complete `system-ping` schema. Markdown sources have no page numbers; locations below therefore give the pinned file, section, and line range. The source terms **Guardian Agent**, **Observed Agent**, and **agent layer** are retained because their separation is material to locus.

I reviewed **17 textual modal clauses** in the assigned sources. Four schema clauses repeat four §13 controls verbatim. De-duplicated by substantive control, this is **13 unique normative obligations or permissions**: four in §12.2, six in §13, and three in §17.1. The §16 roadmap lies between the assigned sections in the file but is outside the assigned unit and is not counted.

> “The agent MUST NOT have knowledge of hooks.” — §1 Design Principle 2, specification line 12. [1]

The preceding statement is outside the assigned section range and is not included in the 17-clause count. It is recorded only as contextual confirmation that ACS distinguishes its LLM/agent boundary from framework hook machinery.

## Decisive evidence on the agent layer

### Architectural statement — relevant but not normative

> “**Input:** request envelope + SessionContext + Intent + provenance. **Output:** decision envelope, plus optional `delegate_to: "agent"`.” — §12.1, specification line 380. [1]

> “Invoked by the deterministic layer's chain config. **Receives the same input plus the deterministic layer's intermediate output. Returns a decision envelope.**” — §12.2, specification line 391. [1]

These sentences describe the deterministic engine and agent-layer interfaces. They do not use `MUST`, `SHOULD`, or another modal keyword, do not require that the LLM itself inspect the named inputs, and do not identify agent-chain position. `SessionContext` may be available to the surrounding Guardian implementation, but §12 does not normatively require a particular SessionContext view inside the agent layer, much less a predecessor, successor, depth, or membership field.

### All unique normative controls in §12.2

| ID | Exact clause and location | Control locus | Chain-position finding |
|---|---|---|---|
| 12.2-1 | “Prompt **MUST** treat untrusted data as data, not instructions.” — §12.2, line 393. [1] | Guardian Agent’s optional LLM agent layer / prompt construction | Governs prompt-injection handling, not execution-chain position. |
| 12.2-2 | “Untrusted fields **MUST** be wrapped/quoted.” — §12.2, line 393. [1] | Guardian Agent’s optional LLM agent layer / prompt construction | Data framing only; no predecessor, successor, depth, or membership. |
| 12.2-3 | “**MUST NOT** have access to deterministic-layer policy code.” — §12.2, line 394. [1] | Guardian Agent’s optional LLM agent layer | A required restriction on the layer. It provides no chain-location evidence. |
| 12.2-4 | “Decisions **MUST** be logged with reasoning, model identifier, confidence (when available).” — §12.2, line 395. [1] | Guardian logging/audit facility | Requires a record outside the LLM’s execution boundary; it does not require chain information to be exposed to the LLM. |

“OPTIONAL for v0.1.0. Deterministic-only deployments are fully conformant.” (§12.2, line 398) confirms that use of the agent layer is optional. It is a conformance-status statement, not a requirement to expose chain position. [1]

## Liveness is expressly not enforcement or audit-chain membership

Section 13 identifies `system/ping` as a liveness method for “connection-health checks, transport-debugging, and timeout tuning,” and says that it “carries no enforcement semantics and is not part of the audit chain.” (§13, line 402.) Its required response is `decision: "allow"` with health/status payload fields. (§13, lines 406–408.) [1]

| ID | Exact clause and location | Control locus | Chain-position finding |
|---|---|---|---|
| 13-1 | “Guardians **MUST** always return `decision: "allow"` for `system/ping` regardless of policy, signature, or session state.” — §13, line 412. [1] | Guardian transport/liveness endpoint | Removes ping from policy enforcement; no agent-local chain evidence. |
| 13-2 | “`system/ping` **MUST NOT** be written into SessionContext as a ContextEntry; it does not participate in the chain hash.” — §13, line 413. [1] | Guardian SessionContext/audit-chain writer | Explicitly excludes the liveness event from the audit chain; no position disclosure. |
| 13-3 | “`system/ping` **MUST NOT** require a signature even if the session otherwise requires signatures.” — §13, line 414. [1] | Guardian request validation | Supports liveness during key failures, not chain observation. |
| 13-4 | “Deployments **SHOULD** monitor hook-path decision failures (§6.4) directly rather than infer enforcement health from ping alone.” — §13, line 415. [1] | Deployment monitoring/operations | Health-versus-enforcement separation. Monitoring sits outside the executing agent. |
| 13-5 | “Connection failure or response timeout for `system/ping` is a transport-level signal that the Observed Agent **MAY** use to renegotiate transport, re-handshake, or fail over.” — §13, line 416. [1] | Observed Agent framework / transport controller | Optional recovery action at the protocol boundary, not a chain-position query by the executing agent. |
| 13-6 | “It **MUST NOT** be interpreted as an enforcement event.” — §13, line 416. [1] | Observed Agent framework / enforcement classification | Requires health status not to be reclassified as enforcement information. |

The schema repeats controls 13-1, 13-2, 13-3, and 13-5 in its one normative `description` field, including that a ping has “no enforcement semantics” and makes “no `chain_hash` advance.” (`system-ping.json`, line 5.) This is a duplicate authoritative expression of the same four controls, not four additional substantive controls. [2]

The source is especially clear that a ping cannot establish enforcement health:

> “The signature exemption means a successful ping does not prove the enforcement path is healthy: a Guardian can answer pings while rejecting every signed hook …” — §13, line 415. [1]

This is commentary explaining the preceding `SHOULD` control. It further distinguishes liveness telemetry from enforcement, but it still does not expose chain position within an agent.

## Error behavior and recovery-data conventions

Section 17 reserves `-32000` through `-32099` for ACS-specific errors, alongside standard JSON-RPC errors. (§17, lines 446–457.) [1] The registry’s only modal data convention is:

> “An error response **MAY** carry a `data` object; when present it **SHOULD** include a machine-readable `reason` and a human-readable `message`, plus the per-code fields noted below.” — §17.1, line 461. [1]

This makes `reason` and `message` optional error metadata, not a required agent-visible chain-position interface. The recovery column is addressed to the **Observed Agent**, not to the Guardian’s optional LLM agent layer.

| Registry entry | Exact raised condition and recovery convention | Locus and relevance to chain position |
|---|---|---|
| `SESSION_REFUSED` (`-32000`) | “Guardian policy refuses the session …”; “Do not retry without a policy or configuration change; read `data.reason`.” — §17.1, line 465. [1] | Guardian policy/session boundary and Observed Agent recovery. An example `agent_id` is authorization identity, not agent-chain membership. |
| `UNSUPPORTED_VERSION` (`-32001`) | “No common `acs_version` at handshake”; “Retry the handshake with a version from `data.supported_versions`.” — §17.1, line 466. [1] | Handshake negotiation, not execution-chain location. |
| `PROVENANCE_REQUIRED` (`-32002`) | Policy requires provenance but client declared `provenance_producer: "none"`; “Re-handshake as a `deterministic` producer, or connect to a Guardian that does not require provenance.” — §17.1, line 467. [1] | Guardian policy and Observed Agent. Provenance producer mode is not a predecessor/successor/depth/membership disclosure. |
| `CAPABILITY_NOT_NEGOTIATED` (`-32003`) | A method or profile was used without handshake negotiation; “Re-handshake to negotiate the method or profile named in `data.method`.” — §17.1, line 468. [1] | Handshake/protocol capability recovery, not a chain position. |
| `SIGNATURE_INVALID` (`-32004`) | Required signature missing, malformed, or invalid; “Re-sign the request; if it persists, re-resolve `key_id`.” — §17.1, line 469. [1] | Request-validation and client recovery. |
| `REPLAY_DETECTED` (`-32005`) | Duplicate `request_id` or `nonce`; “Regenerate `request_id` (and `nonce`) and retry.” — §17.1, line 470. [1] | Replay defense, not topology or execution-chain position. |
| `TIMESTAMP_OUT_OF_WINDOW` (`-32006`) | Timestamp outside negotiated window; `data.skew_window_ms` carries the window; “Correct clock drift and retry within the window.” — §17.1, line 471. [1] | Clock/replay maintenance. |
| `CHAIN_MISMATCH` (`-32007`) | “The client's `chain_hash` does not match the Guardian's computed head”; “Re-fetch session state; a persistent mismatch is an integrity event, not a transient error.” — §17.1, line 472. [1] | Guardian–Observed-Agent/auditor integrity comparison. A hash mismatch signals disagreement with a chain head; it does not reveal a predecessor, successor, ordinal depth, membership, or equivalent location to the executing LLM. |

The following is the remaining unique modal rule in the error material:

| ID | Exact clause and location | Control locus | Chain-position finding |
|---|---|---|---|
| 17.1-1 | “An error response **MAY** carry a `data` object …” — §17.1, line 461. [1] | Guardian/JSON-RPC error serializer | Optional diagnostic payload; no required chain-position field. |
| 17.1-2 | “… when present it **SHOULD** include a machine-readable `reason` and a human-readable `message` …” — §17.1, line 461. [1] | Guardian/JSON-RPC error serializer | Error explanation convention; no chain-location requirement. |
| 17.1-3 | “`system/ping` **MUST NOT** return an ACS-specific error …” — §17.1, line 474. [1] | Guardian liveness/error endpoint | Keeps ping available through signature/key failures; no chain-position disclosure. |

“Every mandated refusal maps to a fixed code, so an SDK can branch on the code without parsing prose.” (§17.1, line 461) is a descriptive interoperability statement preceding the registry. It explains the table’s recovery convention but imposes no additional modal chain-position requirement. [1]

## Chain-position test and locus determination

The work order treats gateway-side lineage, operator dashboards, audit logs, middleware traces, and post-hoc observability as negative unless a requirement exposes the information inside the agent execution boundary. Applying that rule:

| Candidate evidence | Why it does not meet the positive condition |
|---|---|
| `SessionContext` named in the §12.1/§12.2 input description | No normative §12 requirement says that the executing LLM receives a defined SessionContext representation or can query it. The text supplies neither a required predecessor/successor/depth/membership field nor an agent-facing lookup operation. |
| Agent-layer decision log | The mandatory recipient is a log/audit locus. The clause does not require its facts to return to, or be usable by, the executing agent. |
| `system/ping` status and `echo` | §13 requires liveness behavior and excludes it from the audit chain. It is explicitly not an enforcement event. |
| `CHAIN_MISMATCH`, `chain_hash`, and recovery to re-fetch session state | This is an integrity signal at the Guardian–Observed-Agent protocol boundary. A hash cannot by itself identify a chain position, and §17.1 does not require the executing agent to receive interpretable session contents. |
| Error `data.reason` / `message` | Optional generic diagnostics, not a required topology or lineage interface. |

**Control loci found:** (1) the Guardian Agent’s deterministic and optional LLM agent layers; (2) Guardian-managed SessionContext/audit-chain state; (3) the Observed Agent’s framework and transport recovery path; (4) deployment monitoring; and (5) Guardian/JSON-RPC error serialization. None is a normative control locus that places chain-position evidence inside an executing agent.

## Limitations and preserved uncertainty

This is a source-text audit, not an implementation test. ACS implementations may voluntarily provide an agent layer with rich SessionContext access, but voluntary implementation behavior cannot satisfy the requested positive test without a normative source requirement. The §12.2 phrase “Receives the same input” could support a broader implementation design, but it is non-modal and does not specify an agent-visible chain-position field or query; it therefore does not make the classification ambiguous under the work order’s strict rule. The report does not infer semantics from `chain_hash` beyond the explicit integrity behavior stated in the source.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "OWASP Agent Control Standard v0.1.0 — Instrument Specification (pinned commit)"
[2]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/hooks/system-ping.json "OWASP Agent Control Standard v0.1.0 — system/ping payload schema"

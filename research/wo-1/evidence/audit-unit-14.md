# WO-1 Evidence Record — Audit Unit 14 (ACS-09)

## Determination

**Classification: NEGATIVE.** Conditional on an ACS-Trace claim, the cited ACS v0.1.0 material requires trace emission, trace-side decision and provenance capture, and isolation of tracing failure from enforcement. It does **not** normatively require an executing/Observed Agent to receive, query, inspect, or reason over its predecessor, successor, depth, membership, parent, or other location in a broader execution chain.

This is a deliberately narrow conclusion. The documents do specify parent/session/lineage-related telemetry fields in a trace model. Under the WO-1 criterion, however, gateway-side lineage, audit/replay data, tracing middleware, observability tooling, and post-hoc trace trees are negative unless the standard requires their exposure inside the executing agent boundary. The unit instead places these records in spans/events and observability backends, expressly outside the request/response path.

| Audit field | Finding |
|---|---|
| Work order / unit | WO-1 / **ACS-09** |
| Standard and pinned revision | OWASP Agent Control Standard v0.1.0; commit `dc265475139a922824f0c817e2ecc2a2ce31c06c` |
| Audited scope | ACS-Trace profile; Trace Events; OpenTelemetry extension failure isolation |
| Claim condition | Deployment claims **ACS-Trace** |
| Inside-agent chain-position requirement found | **No** |
| Normative requirement occurrences reviewed | **24** (count method below) |
| Classification | **NEGATIVE** |

## Method and classification rule

The authoritative Markdown files named by the unit were retrieved in full from the pinned GitHub commit and independently cloned at that commit. Markdown has no pages; citations therefore use document heading and immutable GitHub line range. The review examined every normative requirement occurrence within the stated ACS-Trace / Trace Events / OpenTelemetry-extension scope, including requirements incorporated by the Trace Events required-attribute table.

A result is **positive** only where normative wording makes chain position available *to the executing agent itself*—for example, requiring it to receive or query a predecessor, successor, depth, membership, or equivalent chain-location fact. A requirement merely to generate, send, store, correlate, or reconstruct a trace is not enough. It is classified **negative** when the locus is a trace emitter, Guardian, collector, SIEM, audit mechanism, or observability tool rather than an interface within the agent’s execution boundary. This record has not treated an implementation possibility as a normative requirement.

**Counting method.** “24” counts each discrete requirement occurrence in the scoped text: 4 in the ACS-Trace conformance section; 11 in *Trace Events* (including its required-attribute/conformance-table rules); and 9 in *Extending OpenTelemetry*. Repeated wording in a second source is counted again as a reviewed occurrence, rather than collapsed. Descriptive statements and examples with no normative force are reviewed as context but are not counted as normative clauses.

## Decisive evidence

The most decisive locus statement is the Trace Events introduction:

> “The Trace pillar is decoupled from enforcement and runs out of the request/response path: deployments emit OpenTelemetry spans (over OTLP/gRPC or OTLP/HTTP) and/or OCSF events to existing observability backends.” — *Trace Events*, ¶3 [2]

The failure-isolation rule independently confirms the separation rather than creating an inside-agent chain-position control:

> “Trace events MUST NOT block enforcement. If the Trace sink is unreachable or returns an error, the Guardian's disposition MUST still be returned to the Observed Agent. The agent's hot path is enforcement; observability is best-effort.” — *Extending OpenTelemetry* §Failure isolation, lines 32–34 [3]

Those clauses require an enforcement response to reach the Observed Agent even when tracing fails. They do not require the Observed Agent to receive the trace, its parent/child links, or a chain-position result.

## Normative-clause review

### A. ACS-Trace profile — Conformance Profiles

The conformance profile binds a **deployment**, not the agent’s own reasoning boundary. Each control below is trace/audit side only.

| ID | Exact normative language and location | What it requires | Control locus | WO-1 assessment |
|---|---|---|---|---|
| C-1 | “Emit at least one of {OTel, OCSF} for every supported ACS step, with the required attributes populated.” — *Conformance Profiles* §ACS-Trace, lines 49–53 [1] | Per-supported-step telemetry with required fields. | Deployment trace instrumentation and OTel/OCSF event stream. | **Negative.** Emission does not require exposing an event or its fields to the executing agent. |
| C-2 | “Record decisions as Trace events.” — §ACS-Trace, lines 49–53 [1] | Trace-side recording of enforcement decisions. | Trace event/audit record. | **Negative.** A decision record is not a chain-position interface for the agent. |
| C-3 | “Carry provenance facts forward onto Trace events.” — §ACS-Trace, lines 49–53 [1] | Copy provenance into telemetry. | Trace event/audit record. | **Negative.** “Forward” is toward the trace, not into agent-visible chain state. |
| C-4 | “Trace events MUST NOT block enforcement.” — §ACS-Trace, line 55 [1] | Failure isolation between observability and enforcement. | Enforcement path relative to trace pipeline. | **Negative.** It preserves enforcement availability; it neither supplies nor requires any location fact inside the agent. |

The statement that ACS-Trace is “Required for deployments that need cross-vendor observability or SIEM integration” immediately precedes C-4 [1]. It is contextual rather than an agent-visibility requirement and reinforces an enterprise-observability locus.

### B. Trace Events — OTel/OCSF vocabulary and ACS-Trace conformance bar

The required-attribute table is incorporated by C-1 (“required attributes populated”). Its row most relevant to a chain-position reading is quoted exactly:

> “`steps/subagentStart`, `steps/subagentStop` | `acs.subagent`, `acs.subagent.end` | `acs.subagent.session_id`, `acs.subagent.parent_session_id`, `acs.subagent.intent_derivation` / `acs.subagent.outcome`, `acs.subagent.final_chain_hash`” — *Trace Events* §OpenTelemetry semantic conventions, line 36 [2]

This is a **near miss**, not a positive. The required `acs.subagent.parent_session_id` is an attribute on an OTel span. The same source defines trace emission as out of the request/response path to observability backends [2]. No clause says a subagent/Observed Agent receives this field, may query it, or must use it to detect its parent or chain position. The standard permits an instrumentation/harness or other deployment component to create/export the record.

| ID | Exact normative language and location | What it requires | Control locus | WO-1 assessment |
|---|---|---|---|---|
| T-1 | “Each ACS step produces a span whose `name` and required attributes are fixed by the table below.” — §OpenTelemetry semantic conventions, line 17; table lines 21–39 [2] | Fixed span names and the stated required attributes for the listed ACS steps. | OTel trace schema/emitter. | **Negative.** The table contains session, parent-session, and optional lineage-depth fields, but makes no field queryable by the executing agent. |
| T-2 | “When Provenance is attached to a hook payload, the resulting span MUST carry `acs.provenance.origin` as an attribute, and SHOULD carry `acs.provenance.source_id` and `acs.provenance.lineage_depth` when populated.” — §OpenTelemetry semantic conventions, line 41 [2] | Origin in span; source identifier and lineage depth in span when populated. | Resulting OTel span/observability data. | **Negative.** The only mandatory target is the span. `acs.provenance.lineage_depth` is conditional and SHOULD-level, and it is not execution-chain position nor agent-visible by requirement. |
| T-3 | “Provenance lineage edges MAY be linked via OTel span links keyed by `provenance_id`.” — line 41 [2] | Optional span-link representation of provenance relations. | OTel trace graph/tools. | **Negative.** Optional post-hoc telemetry linking does not establish an agent query/control. |
| T-4 | “Each ACS step is representable as an OCSF event … Required class-specific attributes are populated from the ACS payload.” — §OCSF event classes, line 45 [2] | Population of OCSF event fields from an ACS payload. | OCSF event/observability pipeline. | **Negative.** Event construction does not make the event visible inside an agent. |
| T-5 | “Emit at least one of {OTel, OCSF} for every ACS step the deployment supports, with the required attributes populated.” — §ACS-Trace conformance bar, lines 74–76 [2] | Same substantive per-step emission obligation as C-1, stated in the Trace Events conformance bar. | Deployment telemetry. | **Negative.** No internal agent exposure. |
| T-6 | “Record every decision as a Trace event carrying the disposition, evaluator identity, and reasoning when present.” — lines 74–78 [2] | Decision trace event, including specified fields. | Trace/audit event. | **Negative.** The record supports audit; it is not a required agent-facing fact. |
| T-7 | “Carry provenance facts forward from the hook payload onto the Trace event so audit replay reconstructs the policy decision without consulting Guardian state separately.” — lines 74–78 [2] | Sufficient event provenance for audit replay. | Trace event and audit replay. | **Negative.** The specified consumer is audit replay, not the executing agent. |
| T-8 | “Trace events MUST NOT block enforcement — failure of the Trace sink MUST NOT change the disposition returned to the Observed Agent.” — line 80 [2] | Trace-sink failure cannot alter the Guardian disposition returned to the Observed Agent. | Trace sink, Guardian disposition, Observed Agent as decision recipient. | **Negative.** The Agent receives a disposition, not trace topology or a chain-position query result. |
| T-9 | “Deployments that do not claim ACS-Trace SHOULD still emit Trace events where feasible; the vocabulary is normative regardless of profile claim.” — line 80 [2] | Recommended emission even without the profile. | Deployment telemetry. | **Negative.** Broader observability encouragement creates no inside-agent exposure obligation. |

**Required-attribute review.** The table’s required groups are session ID/tenant; agent ID/trigger; content types; tool name/capability/exit status; source type/results count; memory-store name/operation; session reason; turn ID/trigger/outcome; compaction count/trigger; subagent session and parent-session IDs plus derivation/outcome/final chain hash; decision fields; and AgBOM fields [2]. It also labels `acs.compact.lineage_depth_after` **optional** (line 35). None is a normative requirement that the executing agent can read or query. The only potentially location-like values—`acs.subagent.parent_session_id`, the trace hierarchy’s `acs.turn.parent_id` (discussed below), and optional `acs.compact.lineage_depth_after`—are telemetry fields.

### C. Extending OpenTelemetry — hierarchy, provenance, transport, and failure isolation

The extension itself directs readers to the Trace Events table as the normative table and says: “This page describes how to *use* the mapping in practice.” — lines 3–5 [3]. Its hierarchy language is descriptive, not a normative agent-interface requirement. The closest statement is:

> “Nested turns (e.g. subagent turns inside a parent turn awaiting `subagentStop`) record `acs.turn.parent_id`.” — *Extending OpenTelemetry* §Span hierarchy, lines 9–14 [3]

This is a trace-tree description without **MUST/SHOULD/MAY**, and it requires neither receipt nor query access by the subagent. The next sentence identifies its purpose as comparable traces across vendors and Guardians [3]. It therefore remains external observability context rather than a positive control.

| ID | Exact normative language and location | What it requires | Control locus | WO-1 assessment |
|---|---|---|---|---|
| O-1 | “When a hook payload carries Provenance, the resulting span MUST carry `acs.provenance.origin` and SHOULD carry `acs.provenance.source_id` and `acs.provenance.lineage_depth`.” — §Provenance attributes, line 20 [3] | Span provenance attributes. | Resulting OTel span. | **Negative.** No agent-visible provenance/chain API is required. |
| O-2 | “The set of provenance ids cited by a Guardian decision … MAY be expressed as OTel span links keyed by `provenance_id`, letting tools that index span links reconstruct the lineage graph without parsing payloads.” — line 20 [3] | Optional telemetry lineage links for indexing tools. | OTel links and indexing tools. | **Negative.** The named consumer is “tools,” not the executing agent. |
| O-3 | “Implementations SHOULD apply the deployment's redaction or hashing policy at attribute-emit time rather than relying on backend-side scrubbing.” — §Sensitive data, line 26 [3] | Handling sensitive tracing attributes at emission. | Telemetry emitter/deployment policy. | **Negative.** No chain-position function. |
| O-4 | “The Guardian's handshake `trace_emission` field MAY advertise an OTLP collector endpoint; when set, the Observed Agent SHOULD route ACS-shaped trace traffic there ….” — §Transport, line 30 [3] | Optional collector-endpoint advertisement and recommended Agent routing. | Guardian handshake and Observed Agent’s telemetry transport. | **Negative.** It gives the agent a destination for exporting telemetry, not predecessor/successor/depth/membership information or a query mechanism. |
| O-5 | “Trace events MUST NOT block enforcement.” — §Failure isolation, line 34 [3] | Non-blocking observability. | Trace/enforcement separation. | **Negative.** No chain-position information. |
| O-6 | “If the Trace sink is unreachable or returns an error, the Guardian's disposition MUST still be returned to the Observed Agent.” — §Failure isolation, line 34 [3] | Guardian-to-Agent decision delivery despite trace-sink failure. | Guardian and Observed Agent decision channel. | **Negative.** The required response is an enforcement disposition only, not lineage/topology. |

## Locus analysis

| Control or datum | Normatively situated at | Is it inside the executing agent under the WO-1 test? |
|---|---|---|
| Per-step OTel/OCSF emission and required attributes | Deployment instrumentation and emitted span/event. | **No.** The emitter is not specified as an agent-visible introspection interface. |
| `acs.subagent.parent_session_id`, `acs.turn.parent_id`, `acs.compact.lineage_depth_after` | OTel span attributes / trace hierarchy; lineage depth is expressly optional in the mapping table. | **No.** Trace representation is not required to be returned to or queryable by the agent. |
| Decision, evaluator, and reasoning record | Parent step span / Trace event. | **No.** The agent is only required to receive the Guardian disposition under failure isolation, not its trace event. |
| Provenance origin/source/lineage depth and provenance links | Span attributes and optional OTel links; audit replay/indexing tools. | **No.** These are trace/audit facts, not an internal chain-position oracle. |
| Trace collector endpoint | Guardian handshake field and Agent telemetry routing. | **No.** Endpoint routing conveys a sink location, not execution-chain location. |
| Failure isolation | Guardian disposition path relative to a trace sink. | **No.** It protects enforcement from telemetry failure; it makes no introspection information available. |

## Result and uncertainty

**Result: NEGATIVE; `inside_agent_requirement_found = false`.** The review found trace evidence that can identify parent/lineage relationships in observability data, including the explicit subagent parent-session attribute. It did not find the decisive additional requirement: that the executing agent itself must receive or can query that evidence. The standard’s own framing—trace out of the request/response path to existing observability backends, tools reconstructing lineage graphs, and best-effort observability isolated from enforcement—makes the negative classification stronger than a mere silence inference.

A limited boundary ambiguity remains at the implementation level: an implementation could place tracer state in the same process as an agent, or voluntarily expose parent/lineage fields to its agent runtime. The cited text does not require either. Under the task’s requirement-based criterion, voluntary architecture cannot convert this result to positive; therefore this ambiguity is not grounds to mark the unit **AMBIGUOUS**.

## Limitations

1. This is a public-standard, requirements-text audit of the three supplied, pinned Markdown sources. It does not test a deployment or assert what a vendor tracer happens to expose at runtime.
2. The linked JSON mappings and the wider Instrument specification were not independent audit sources because they were not among the unit’s three authoritative source URLs. Relevant mapping/table content present in the supplied sources was reviewed.
3. “Agent” can be implemented with a co-resident harness/instrumentation component. The ACS-Trace text does not define that component as an agent-facing query interface; the conclusion preserves that boundary distinction rather than assuming co-residence equals visibility.
4. Markdown source has no stable pages. The permanent commit URL, section heading, and exact source line range are supplied instead.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md#L47-L55 "OWASP Agent Control Standard v0.1.0 — Conformance Profiles, ACS-Trace"

[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/trace/events.md "OWASP Agent Control Standard v0.1.0 — Trace Events"

[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/trace/extend_opentelemetry.md "OWASP Agent Control Standard v0.1.0 — Extending OpenTelemetry"

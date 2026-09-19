# ACS-04 — Instrument §6: Chain-Position Detectability Audit

**Standard:** OWASP Agent Control Standard (ACS) v0.1.0
**Unit audited:** Instrument §6, including §§6.1–6.4 — Disposition Vocabulary, Result Fields, MODIFY Composition, and Honoring Decisions
**Classification:** **NEGATIVE**
**Finding:** This unit requires the Observed Agent to obtain and act on a Guardian’s disposition, but does **not** require the executing agent to receive or query its predecessor, successor, depth, membership, or another usable indicator of its location in a larger execution chain.

## Scope, test, and source control

The test is deliberately narrow. A **POSITIVE** finding would require a normative statement placing chain-position evidence inside the executing agent: for example, a requirement that it receive or query a predecessor or successor identifier, chain depth, membership relation, or equivalent usable location information. Guardian-side lineage, an audit-chain value intended for an observer, policy data that may contain lineage, external audit records, and dashboard/trace visibility do not satisfy the test unless the unit requires their exposure within the executing agent’s boundary.

The complete version-pinned Instrument specification was reviewed for lines 134–202, which comprise §6 through §6.4. The complete cited response-envelope JSON Schema was also reviewed, including its `AcsResult` required set, decision conditionals, and descriptions of the potentially relevant provenance and chain fields. Markdown and JSON have no stable pages; locations below therefore give section and source-line locations for the specification, or JSON Pointer for the schema. The locally downloaded source fingerprints were `2677d4be157d0fd0a806546332c3a06c43d77d0825dcb789983e65d03c70aecf` (specification) and `145f730c80a7a6ca8c870fe4a68b898d0ef6a8fcd0f2cc575f9ca70e6d43d0d9` (schema).

**Conclusion.** The most relevant mandatory behavior is enforcement, not self-location. The Observed Agent must wait for and apply the Guardian decision. The only lineage-adjacent decision fields in §6.1 are optional (`cited_provenance_ids` and free-form `policy_data`); §6.2’s lineage illustrations are examples and its multi-paradigm citation is merely permitted. There is no required agent-side predecessor/successor/depth/membership field, lookup, or interpretation rule. This is a clear **NEGATIVE**, not an ambiguity.

## Decisive evidence and locus

> “For every step it submits, the Observed Agent **MUST wait** for the Guardian's decision, up to the negotiated timeout (`timeout_config`, §4), and **MUST apply** it: `ALLOW` proceeds, `DENY` blocks the action, `MODIFY` proceeds with the modified payload (§6.3), `ASK` pauses for approval, `DEFER` suspends pending resolution.” — §6.4, specification lines 196–198 [1]

This places a decision-enforcement loop at the **Observed Agent ↔ Guardian** boundary. It does not require the Observed Agent to learn how its submitted step relates to another step, nor does it identify another agent or a chain position.

> “`cited_provenance_ids` | no | Array of `provenance_id`s whose facts drove this decision. Standard top-level surface for ‘which provenance objects mattered’.” — §6.1, specification lines 168–176 [1]

The closest lineage-adjacent field is explicitly not required. It denotes provenance objects that drove a Guardian decision, not the Observed Agent’s predecessor, successor, depth, membership, or current position. The schema independently labels the field “Optional” and says it gives **audit tooling** a place to find objects relevant to a verdict; it does not impose an agent-side query or interpretation obligation. — `/$defs/AcsResult/properties/cited_provenance_ids`, response-envelope schema [2]

> “A FIDES P-T denial cites the violating lineage in `cited_provenance_ids` and exposes the violating-argument path in `policy_data`.” — §6.2, specification line 181 [1]

This is explanatory composition text, not a normative `MUST`/`SHOULD` requirement. Even on its stated terms, it concerns a Guardian decision’s evidence, not a compulsory location disclosure to the executing agent.

> “A single decision **MAY** cite all of them …” — §6.2, specification line 181 [1]

The sole normative modality in §6.2 is permission. It neither requires citation nor converts cited provenance into agent-readable chain position.

The response schema also contains a `chain_hash` property whose descriptive text says a Guardian “MUST include it” on certain responses, but that text expressly cross-references Specification §8 and says publication lets “an observer that records traffic” detect later rewrite. It is not a §6 requirement, is not required by the response schema’s own `required` array, and a rolling hash alone does not disclose predecessor, successor, depth, or membership. It is therefore not evidence for a positive result in this exact unit. — `/$defs/AcsResult/properties/chain_hash`, response-envelope schema [2]

## Complete normative-clause ledger

The ledger records **28 atomic normative or schema-enforced constraints** in the assigned unit. Permissions (`MAY`) and recommendations (`SHOULD`/`RECOMMENDED`) are included so that the review does not silently omit weaker normative language. “No chain-position effect” means the clause neither requires the executing agent to receive nor to query the specified information.

| # | Location (page n/a) | Exact normative language or enforced constraint | Control locus | Chain-position effect |
|---:|---|---|---|---|
| 1 | §6 disposition table, line 138 | “`reasoning` **RECOMMENDED** when user-visible audit trails are expected” for `ALLOW`. | Guardian response / user-visible audit consumer. | No chain relation. |
| 2 | §6, line 144 | “DEFER **MUST include** `resolution_method`, `resolution_timeout_ms`, and `timeout_decision` (default `deny`).” | Guardian decision envelope. | Bounded-resolution metadata, not chain location. |
| 3 | §6, line 144 | “Cascading deferrals **MUST be bounded per session**.” | Guardian/session control. | A session bound is not predecessor/successor/depth/membership exposure. |
| 4 | §6.1 table, lines 168–171 | `decision` is required (“yes”); the schema enforces it in the `AcsResult` required set. | Guardian-to-Observed-Agent response contract. | A verdict identifies no chain position. |
| 5 | §6.1, line 171 | Deployments wanting audience-specific text “**SHOULD compose** them client-side from `reasoning` + `policy_data` + `reason_codes`.” | Client presentation/composition. | May process policy facts; no required chain-position facts or query. |
| 6 | §6.1, line 172 | `policy_version` “**SHOULD be populated** when replay or ledger-backed policy state matters.” | Guardian/policy-replay metadata. | Policy-version provenance, not execution-chain location. |
| 7 | §6.1, line 172 | “A single decision **MAY cite** multiple entries when several paradigms reject the same action.” | Guardian decision response / audit replay. | Multiple policy contributions are not agent membership or ordering. |
| 8 | §6.1, line 173 | “UIs and meta-policies **SHOULD switch** on these rather than parsing reasoning text or rule IDs.” | UI or policy layer. | Reason-code consumption only. |
| 9 | §6.1 table, line 177 | `model_id` is “required when `evaluator` is `agent` or `composite`.” | Evaluator metadata producer. | Identifies an evaluator model, not position in a larger execution chain. |
| 10 | §6.2, line 181 | “a single decision **MAY cite** all of them.” | Guardian composition of decision evidence. | Optional policy/provenance citations; no required agent-side chain location. |
| 11 | §6.3, line 187 | A MODIFY with `modified_content` “**MUST NOT** also carry `redactions` or `parameter_overrides`.” | Guardian modification producer. | Payload-shape safety only. |
| 12 | §6.3, line 188 | “`redactions` and `parameter_overrides` **MAY** appear together …” | Guardian modification producer. | Permission to combine disjoint edits; no chain effect. |
| 13 | §6.3, line 188 | “… but their targets **MUST be disjoint**.” | Guardian modification producer. | Deterministic payload application only. |
| 14 | §6.3, line 190 | “A Guardian **MUST NOT emit** a `modifications` object that violates either rule.” | Guardian. | No chain-position information. |
| 15 | §6.3, line 190 | An Observed Agent receiving an invalid object “**MUST fail closed**, treating the decision as `DENY`.” | Observed Agent enforcement. | The agent detects invalid edit composition, not chain position. |
| 16 | §6.3, line 190 | It “**SHOULD record an audit event**.” | Observed Agent / audit record. | Event recording is not required self-exposure of chain topology. |
| 17 | §6.4, line 198 | For every submitted step, the Observed Agent “**MUST wait** for the Guardian’s decision.” | Observed Agent. | Wait state is not information about predecessor, successor, depth, or membership. |
| 18 | §6.4, line 198 | The Observed Agent “**MUST apply**” the disposition. | Observed Agent. | Application of an external verdict does not reveal chain location. |
| 19 | §6.4, line 200 | “A deployment **MAY set** `on_decision_failure: deny` (fail-closed).” | Deployment/handshake configuration. | Failure posture only. |
| 20 | §6.4, line 200 | Registry recovery action that “the agent **MAY attempt** within the remaining budget.” | Observed Agent recovery behavior. | Retry timing is not chain awareness. |
| 21 | §6.4, line 200 | A refused connection “**MAY resolve immediately** rather than waiting out the clock.” | Observed Agent failure handling. | Transport result only. |
| 22 | §6.4, line 202 | “Every step that proceeds without a decision **MUST be recorded as an audit event**.” | Audit-event sink; emitted by the agent/framework. | Required audit visibility after bypass, but no requirement to expose chain position inside the executing agent. |
| 23 | §6.4, line 202 | “the agent **MUST honor** [a timely decision] regardless of the posture.” | Observed Agent. | External decision compliance only. |
| 24 | Schema `/$defs/AcsResult/required` | The response object requires `type`, `acs_version`, `request_id`, and `decision`. | Guardian-to-Observed-Agent wire response, validated by schema. | `request_id` correlates a request/response; it is not a predecessor, successor, depth, or membership requirement. |
| 25 | Schema `/$defs/AcsResult/allOf/0` | If `decision` is `deny`, `reasoning` is required. | Guardian response, schema validator. | Explanation only. |
| 26 | Schema `/$defs/AcsResult/allOf/1` | If `decision` is `modify`, `reasoning` and `modifications` are required. | Guardian response, schema validator. | Payload modification only. |
| 27 | Schema `/$defs/AcsResult/allOf/2` | If `decision` is `ask`, `reasoning` and `ask_details` are required. | Guardian response, schema validator. | Approval pause only. |
| 28 | Schema `/$defs/AcsResult/allOf/3` | If `decision` is `defer`, `reasoning` and `defer_details` are required. | Guardian response, schema validator. | Deferred resolution only. |

## Conditional result fields and the five dispositions

The disposition table and the schema agree on the result envelope’s minimum decision data. `DENY` requires `reasoning`; `MODIFY` requires `reasoning` and `modifications`; `ASK` requires `reasoning` and `ask_details`; and `DEFER` requires `reasoning` and `defer_details`. `ALLOW` has no required payload beyond the common result fields, although reasoning is recommended when user-visible audit trails are expected. The `DEFER` prose additionally requires a resolution method, a resolution timeout, and a timeout decision, and requires cascading deferrals to be bounded per session. These controls state how a Guardian’s decision is formed and how an Observed Agent must pause or apply it. None establishes execution-chain location.

The optional `policy_data` and `cited_provenance_ids` fields are the only potentially chain-adjacent surfaces in this unit. The standard expressly marks both as non-required in §6.1. `policy_data` is free-form; it can contain a FIDES argument path or an AARM lookback state, but its presence and contents are not mandated for every decision. `cited_provenance_ids` can name provenance objects that influenced the Guardian’s decision, but the unit supplies no required relationship traversal, depth calculation, predecessor/successor reference, or agent-facing query mechanism. A provenance identifier alone is not a location in an execution chain.

## Normative requirements versus commentary and examples

The following text was examined but not treated as a separate normative chain-position requirement:

- The sentence explaining that an expired `DEFER` fails closed while a silent Guardian fails open (§6, line 146) is rationale. The immediately preceding two `MUST` statements were captured in ledger entries 2–3.
- The flow diagram and statement that `ASK` and `DEFER` pause a step (§6, lines 148–162) describe the vocabulary. The actual mandatory wait/apply rule is §6.4 and is captured in entries 17–18.
- The FIDES, IBAC, and AARM examples (§6.2, line 181) illustrate what policy data or citations *can* carry. They do not use mandatory language. The `MAY` that follows is captured in entry 10.
- The explanation of why overlapping MODIFY targets are unsafe (§6.3, lines 192–194) is commentary. The enforceable composition rules are captured in entries 11–16.
- The descriptions of decision failure and the fail-open trade-off (§6.4, lines 200–202) explain the failure posture. The actual `MAY` and `MUST` clauses are captured in entries 19–23.

## Control-locus assessment

| Control locus | Required behavior in this unit | Why it does not meet the inside-agent chain-position test |
|---|---|---|
| **Guardian** | Emits a disposition; supplies conditionally required result fields; must create safe MODIFY payloads. | It evaluates/enforces policy, but §6 does not require it to disclose the agent’s execution-chain location to the Observed Agent. |
| **Observed Agent** | Waits for, applies, and honors decisions; fails closed on malformed MODIFY; records specified audit events. | These are enforcement and audit duties. They neither require a predecessor/successor/depth/membership field nor a query to derive one. |
| **Deployment / handshake** | Selects `on_decision_failure` posture and timeout context. | Governs availability/enforcement under Guardian failure, not topology disclosure. |
| **Client, UI, and meta-policy** | May compose audience-specific explanations; should use reason codes. | These are presentation or policy-consumption loci, not a mandated execution-chain interface. |
| **Audit/observer** | Receives required bypass/invalid-modification records; may use decision evidence. | Audit is outward-facing. No §6 clause requires its lineage to be exposed back inside the executing agent. |
| **Response-envelope schema** | Constrains result shape and selected disposition-specific fields. | It carries verdict and optional provenance-related data, but requires no usable chain-position information. |

## Limitations and preserved uncertainty

This is an audit of **only** Instrument §6–§6.4 and the cited response-envelope schema. It does not make claims about other ACS units, including §7 Provenance, §8 SessionContext/audit-chain semantics, §9 approvals, or deployment-specific extensions. The schema’s `chain_hash` annotation was screened solely to prevent overlooking a relevant field; its operative requirement is explicitly delegated to §8 and is not counted as a §6 finding.

The response-envelope schema references `modifications.json`, `ask-details.json`, and `defer-details.json`. Those referenced schemas were not separately audited because they are not among the assigned source URLs and the unit itself states the applicable §6 requirements. This limitation does not create ambiguity about the criterion: no §6 prose or response-envelope constraint requires the executing agent to obtain a predecessor, successor, depth, membership, or equivalent chain-position relation.

The audit evaluates public normative text, not an implementation. A deployment could voluntarily place lineage or orchestration state in `policy_data`, `reasoning`, or an extension. Such behavior would be implementation-specific and cannot convert the unit’s optional surfaces into the required inside-agent evidence demanded by the criterion.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "ACS v0.1.0 Instrument Specification, version-pinned source"

[2]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/response-envelope.json "ACS v0.1.0 Response Envelope JSON Schema"

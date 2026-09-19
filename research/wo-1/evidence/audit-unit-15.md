# ACS-10 — OWASP Agent Control Standard v0.1.0

## Audit identity and conclusion

| Field | Finding |
|---|---|
| Work order / unit | WO-1 / ACS-10 |
| Standard | OWASP Agent Control Standard (ACS) v0.1.0 |
| Audited section | **ACS-Inspect and ACS-Inspect-Dynamic profiles; Inspect Wire Methods through Triggers for AgBOM Updates** |
| Pinned revision | `dc265475139a922824f0c817e2ecc2a2ce31c06c` |
| Decision | **NEGATIVE** |
| Inside-agent chain-position requirement found | **No** |
| Normative-clause instances reviewed | **27** in the Inspect source closure (profile clauses, canonical-document and component schemas, two Inspect wire-method schemas, serialization mapping, and the linked CycloneDX extension). Related baseline SessionContext material was also checked to establish locus, but is not included in this unit count. |

**Criterion applied.** A POSITIVE result requires a normative requirement that puts evidence of an executing agent’s location in a larger execution chain *inside that agent*: e.g., a required predecessor, successor, depth, membership, or a query by which it can obtain an equivalent. Guardian-side lineage, audit chains, gateways, middleware, operator views, and post-hoc records do not qualify unless the standard requires their exposure within the agent execution boundary.

**Finding.** The Inspect profiles require the **Observed Agent** to report its component inventory and mutations *to the Guardian*. They require the **Guardian** to accept, audit, make/return certain decisions, and serialize the inventory for downstream consumers. The standard’s SessionContext audit chain is Guardian-maintained and exposes at most a rolling hash commitment, not a predecessor/successor/depth/membership representation. No reviewed normative clause requires the executing agent to receive or query its location in a larger execution chain. Therefore, even the strongest relevant controls are external observability/inventory controls under the criterion.

## Authority and method

The three user-supplied authorities were read in full: the pinned conformance document, the Inspect specification, and the published canonical AgBOM document schema. The pinned repository was checked out at the supplied commit. Because the Inspect specification normatively binds `agbom/snapshot`, `agbom/changed`, `component.json`, and `inspect/format-mapping.json`, those linked schemas were also read in full as the source closure necessary to assess the named wire methods, provenance, and serialization controls. The linked Inspect serialization-extension documents were also checked; only the CycloneDX extension contained a modal clause. The linked JSON was valid at the pinned revision.

The count records each operative normative-clause **instance** in that closure. Duplicated statements in the prose and schema are separately recorded because they are separate authoritative instances; non-normative trigger descriptions, tables, diagrams, examples, and explanatory text are identified but not counted as requirements. The base SessionContext material is used only to resolve the locus of the required audit integration.

## Decisive evidence

> “A deployment claiming **ACS-Inspect** MUST: 1. Emit `agbom/snapshot` once per session, before content-bearing hooks fire. 2. Have the Guardian accept `agbom/snapshot`, write it into the SessionContext audit chain, and serialize the canonical AgBOM into at least one of {CycloneDX 1.6, SPDX 3.0, SWID} on request.” — Inspect, **ACS-Inspect conformance bar**, lines 67–70 [2]

> “A deployment claiming **ACS-Inspect-Dynamic** additionally MUST: 3. Emit `agbom/changed` on every mutation to the component graph. 4. Write those mutations into the audit chain.” — Inspect, **ACS-Inspect-Dynamic**, lines 72–75 [2]

These are the decisive profile requirements. “Emit” is agent-to-Guardian reporting; acceptance, audit-chain writing, serialization, and policy decision are Guardian-side. Neither clause requires the agent to receive/query a predecessor, successor, depth, membership, or equivalent chain-location fact.

The actor allocation is explicit in the wire schemas:

> “Full Agent Bill of Materials snapshot. **Emitted by the Observed Agent** … `agbom/snapshot` **MUST be written into the SessionContext audit chain** …” — `agbom-snapshot.json`, description, line 5 [4]

> “AgBOM mutation notification. **Emitted by the Observed Agent** … **MUST be written into the SessionContext audit chain** alongside the originating mutation.” — `agbom-changed.json`, description, line 5 [5]

And the audit-chain authority is expressly outside the agent boundary:

> “Append-only entry in a SessionContext’s audit chain. **Maintained server-side by the Guardian; not transmitted in full on the wire** …” — `context-entry.json`, top-level description [8]

The chain-head response is likewise only a commitment, not a location indicator:

> “Rolling SHA-256 audit-chain head … The Guardian MUST include it on every response for a step where it wrote a ContextEntry …” — `response-envelope.json`, `chain_hash` description, lines 88–91 [10]

A hash head can support integrity comparison but does not convey a chain predecessor/successor identity, depth, membership, or an equivalent execution-chain location. No requirement was found to map that hash to such information for the executing agent.

## Complete normative-clause review

### A. Profile and policy trigger requirements

| # | Exact normative language and location | Status | Control locus | Chain-position result |
|---:|---|---|---|---|
| 1 | “When Guardian policy depends on component inventory … the deployment **MUST implement ACS-Inspect**.” — Inspect, lines 7–10 [2] | Normative; conditional policy trigger | Deployment / Guardian-policy architecture | No agent chain-position evidence required. |
| 2 | “Guardians **MAY return** `deny` to refuse a session whose component graph contains a banned component, or to block a hot-swap.” — Inspect, line 21 [2] | Normative permission | Guardian decision point | The Guardian sees inventory; agent receives a disposition, not a chain position. |
| 3 | “A deployment claiming ACS-Inspect **MUST**: 1. Emit `agbom/snapshot` once per session before content-bearing hooks fire.” — Conformance, lines 59–62 [1] | Normative; profile claim | Observed Agent → Guardian wire | Timing of a component-inventory report, not position in an execution chain. |
| 4 | “Have the Guardian serialize the canonical AgBOM into at least one of {CycloneDX 1.6, SPDX 3.0, SWID} on request.” — Conformance, line 62 [1] | Normative; profile claim | Guardian / downstream serialization | No inside-agent exposure. |
| 5 | “A deployment claiming **ACS-Inspect** **MUST**: 1. Emit `agbom/snapshot` once per session, before content-bearing hooks fire.” — Inspect, lines 67–69 [2] | Normative; duplicate source instance of #3 | Observed Agent → Guardian wire | Snapshot timing has no predecessor/successor/depth/membership field. |
| 6 | “Have the Guardian accept `agbom/snapshot`, write it into the SessionContext audit chain, and serialize the canonical AgBOM … on request.” — Inspect, line 70 [2] | Normative; profile claim | Guardian, Guardian-maintained SessionContext, downstream consumer | Audit and serialization remain external to agent execution. |
| 7 | “A deployment claiming **ACS-Inspect-Dynamic** additionally **MUST**: 3. Emit `agbom/changed` on every mutation to the component graph.” — Inspect, lines 72–74 [2] | Normative; every-mutation trigger | Observed Agent → Guardian wire | Mutation reporting says what changed in local components, not where the agent is in a larger run. |
| 8 | “4. Write those mutations into the audit chain.” — Inspect, line 75 [2] | Normative; every-mutation audit | Guardian SessionContext audit chain | Guardian-side record only. |

### B. Component provenance and canonical-document requirements

| # | Exact normative language and location | Status | Control locus | Chain-position result |
|---:|---|---|---|---|
| 9 | “Every component **SHOULD** carry `registration_provenance` (who declared it — framework / configuration / runtime discovery) …” — Inspect, line 42 [2] | Normative recommendation | Component record emitted by Observed Agent; inspected by Guardian | Records origin of a **component registration**, not the executing agent’s predecessor/successor/depth/membership. |
| 10 | “Deployments claiming **ACS-Provenance** **MUST** populate `registration_provenance` on every component.” — Inspect, line 42 [2] | Normative; conditional on another profile | Component record / deployment | Same limitation as #9; it is component provenance, not execution-chain placement. |
| 11 | “A Guardian **MAY** request a specific serialization in the handshake’s AgBOM negotiation …” — Inspect, line 63 [2] | Normative permission | Guardian / handshake | Guardian chooses a representation; no agent position is required. |
| 12 | `agbom_hash` “Lets Guardians and downstream consumers detect AgBOM mutations … **RECOMMENDED**.” — canonical document schema, `agbom_hash` description [3] | Normative recommendation | Artifact integrity for Guardian/downstream consumers | Detects inventory changes, not execution-chain location. |
| 13 | “Stable identifier for this component within the AgBOM. **SHOULD** remain stable across version upgrades …” — `component.json`, `id` description, lines 9–12 [7] | Normative recommendation | Canonical component graph | Stable component identity is not agent chain membership. |
| 14 | “`origin` **SHOULD** be `system` for framework/configuration registrations and `user_input` / `tool_output` for runtime-discovered or user-installed components.” — `component.json`, `registration_provenance` description, lines 25–29 [7] | Normative recommendation | Component provenance | Describes how an inventory component entered the AgBOM, not a runtime agent’s place in a larger chain. |
| 15 | “The body itself **MUST NOT** be required on the wire. Only the reference and digest persist in the AgBOM …” — `component.json`, skill `definition` description, lines 116–118 [7] | Normative prohibition | AgBOM wire representation | Restricts skill artifact representation; no chain position. |
| 16 | “A Guardian **SHOULD** compare this against the union of capabilities exposed by the composed tools and **MAY** deny a skill that declares more than it composes.” — `component.json`, `declared_capabilities`, lines 132–135 [7] | Two normative clauses | Guardian policy/enforcement | Composition is an inventory/capability relation, not a requirement to expose an executing agent’s execution-chain location. |
| 17 | “A skill that loads a skill outside this declared set at runtime **SHOULD** be denied at `steps/skillLoad`.” — `component.json`, `composed_skills`, lines 145–148 [7] | Normative recommendation | Guardian enforcement at skill load | Regulates permitted skill composition, not chain predecessor/successor/depth/membership. |

### C. Wire-method and every-mutation requirements

| # | Exact normative language and location | Status | Control locus | Chain-position result |
|---:|---|---|---|---|
| 18 | “Guardians **MAY** return `deny` to refuse a session whose component graph contains a banned model, tool, peer, or knowledge source.” — `agbom-snapshot.json`, description, line 5 [4] | Normative permission | Guardian response | External policy decision; not an inside-agent chain-location interface. |
| 19 | “`agbom/snapshot` **MUST** be written into the SessionContext audit chain …” — `agbom-snapshot.json`, description, line 5 [4] | Normative requirement | Guardian-side audit chain | Confirmed Guardian-maintained; negative under criterion. |
| 20 | “`agbom/changed` … **MAY** be denied by the Guardian to block a hot-swap …” — `agbom-changed.json`, description, line 5 [5] | Normative permission | Guardian response | Does not require an agent to learn its chain location. |
| 21 | “`agbom/changed` … **MUST** be written into the SessionContext audit chain alongside the originating mutation.” — `agbom-changed.json`, description, line 5 [5] | Normative requirement | Guardian-side audit chain | External audit integration; negative under criterion. |
| 22 | “the resulting AgBOM after applying the diff **MUST** equal the AgBOM the Observed Agent would emit as a fresh snapshot.” — `agbom-changed.json`, diff description, line 14 [5] | Normative requirement | Observed Agent’s report consistency / Guardian validation | Ensures inventory-state equivalence, not execution-chain position. The optional `trigger_step_id` merely identifies an originating action; it does not designate a predecessor/successor or depth. |

### D. Canonical serialization requirements

| # | Exact normative language and location | Status | Control locus | Chain-position result |
|---:|---|---|---|---|
| 23 | “conformant Guardians **MUST** be able to render at least one of these on request from a downstream consumer.” — `inspect/format-mapping.json`, top-level description, line 5 [6] | Normative requirement | Guardian → downstream consumer | The output is outside the executing agent. |
| 24 | “The CycloneDX `metadata.tools` **SHOULD** include the Observed Agent’s framework as the BOM generator.” — format mapping, CycloneDX description, line 10 [6] | Normative recommendation | Guardian-generated CycloneDX serialization | Identifies BOM generator/framework, not execution-chain location. |
| 25 | “Provenance attached to a component **MUST** be carried into CycloneDX `evidence` or `properties` …” — format mapping, CycloneDX description, line 10 [6] | Normative requirement | Guardian serialization / downstream consumer | Carries component provenance outward. It does not place chain membership or neighbor information in the agent. |
| 26 | “For `agbom/changed`, deployments **MAY** emit a CycloneDX VEX-style diff or simply emit a fresh full serialization …” — *Extending CycloneDX*, note, line 74 [11] | Normative permission in linked Inspect extension | Deployment’s external serialization | The option concerns serialization of the mutation report, not evidence of the agent’s execution-chain position. |

**Count clarification.** The modal clause count is 27 when the two modal subclauses in row 16 and the two in the serialization material are counted individually, the repeated profile statements remain distinct source instances, and the linked CycloneDX extension’s optional serialization clause is included. The numbered rows are an evidence index, not a one-row/one-clause arithmetic claim.

## Non-normative material reviewed and kept separate

The following language is relevant context but does **not** itself create a chain-position requirement:

* The method table says `agbom/snapshot` flows **“Observed → Guardian”** and triggers “Once after `sessionStart`, before any content-bearing hook; and after any handshake renegotiation”; it says `agbom/changed` flows **“Observed → Guardian”** whenever a component changes. — Inspect, lines 14–19 [2]
* The listed update triggers (model/MCP/A2A peer/tool/knowledge source/memory store/agent capability changes) are bullets, not modal requirements. — Inspect, lines 79–87 [2]
* “The canonical document is the source of truth; serialized output is a deterministic derivation.” — Inspect, lines 44–48 [2]. This is architecture/commentary; the operative rendering requirement is separately recorded above.
* The AgBOM’s `a2a_peer` component and component-reference graph describe inventory and composition. They do not normatively assert that an A2A peer is the executing agent’s runtime predecessor or successor, nor provide depth or membership in an execution chain. — Inspect, lines 27–40 [2]; `component.json` [7].

## Audit-chain integration and inside-agent boundary analysis

### Locus of the relevant controls

| Control | Required actor / boundary | Why it is not qualifying inside-agent chain-position evidence |
|---|---|---|
| Initial snapshot | Observed Agent emits canonical inventory to Guardian | The agent reports its own component graph. The requirement does not ask it to obtain its position relative to other execution steps/agents. |
| Mutation event | Observed Agent emits change/diff to Guardian | “Every mutation” is comprehensive inventory reporting, not a chain-topology report. |
| Accept, deny, audit | Guardian | The standard assigns acceptance/denial and audit-chain integration to the Guardian. This is exactly gateway-/middleware-side observability excluded by the criterion. |
| Canonical graph and BOM formats | Guardian and downstream consumer | Serialization is produced on request for external consumption. |
| Component provenance | AgBOM component record; Guardian policy/serialization | Registration origin identifies who/what registered a component. It is not the executing agent’s predecessor/successor/depth/membership. |
| SessionContext | Guardian server-side storage; a hash head may travel in response | The chain is session-local and server maintained. A chain hash is a cryptographic commitment, not intelligible chain-position evidence. |

### Related baseline check: does audit integration become agent-visible?

No. The request envelope permits only an **optional** `metadata.session_state.chain_hash`, described as the “Latest known chain hash from the agent’s perspective.” [9] The response requires the Guardian to publish a “Rolling SHA-256 audit-chain head” after relevant entries. [10] The full ContextEntry is explicitly Guardian-maintained and “not transmitted in full on the wire.” [8]

A chain-head hash lets a party detect mismatch/tampering only when compared against appropriate state. It does not, by itself, disclose who preceded/follows the agent, how deep it is, whether it belongs to a broader chain, or an equivalent location property. Crucially, no reviewed Inspect or transitive baseline clause requires a Guardian to resolve that hash into such information **inside the Observed Agent**. This is therefore negative, not ambiguous.

## Why the result is NEGATIVE rather than AMBIGUOUS

The language is sufficiently clear about the relevant control loci: methods are emitted **from Observed Agent to Guardian**, the Guardian accepts/denies/serializes, and SessionContext is maintained server-side. The word “chain” appears in an audit-integrity sense, not as a requirement for an agent to know its location in a larger execution sequence. Component-graph and A2A-peer inventory could be useful external evidence to an implementation, but the standard does not normatively require that those data identify runtime predecessor/successor/depth/membership or be presented to the executing agent as such.

Accordingly there is no genuine interpretive uncertainty under the specified criterion. The result would change only if a future ACS requirement made the Guardian’s lineage/topology data queryable or delivered it to the executing agent with semantics sufficient to identify the agent’s location in a broader chain.

## Limitations

1. This is a standards-text audit, not a claim about what any ACS implementation may voluntarily expose. Implementations can offer more information than the v0.1.0 requirements mandate.
2. The conclusion is conditional on the stated scope: claims of ACS-Inspect/ACS-Inspect-Dynamic or policy dependence on component inventory. It does not classify unrelated ACS profiles except where baseline SessionContext text is needed to locate the Inspect-required audit chain.
3. `a2a_peer`, `trigger_step_id`, component composition, and hash-chain references were considered possible near-misses. None has normative semantics equating it to agent-visible execution-chain position.
4. The cited public schema URL is canonical. The pinned repository copy was used to review linked wire schemas and to create stable line-level citations; it matched the published schema’s role and structure at the audited revision.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/conformance.md#L57-L68 "ACS v0.1.0 conformance — ACS-Inspect and ACS-Inspect-Dynamic"
[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/inspect/README.md#L7-L87 "ACS Inspect specification"
[3]: https://genai-security-project.github.io/agent-control-standard/schema/v0.1.0/agbom/document.json "ACS AgBOM Document schema (v0.1.0)"
[4]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/hooks/agbom-snapshot.json#L1-L18 "agbom/snapshot payload schema"
[5]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/hooks/agbom-changed.json#L1-L67 "agbom/changed payload schema"
[6]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/inspect/format-mapping.json#L1-L21 "AgBOM serialization format mapping"
[7]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/agbom/component.json#L1-L163 "AgBOM component schema"
[8]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/context-entry.json#L1-L46 "ACS ContextEntry schema"
[9]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/request-envelope.json#L60-L81 "ACS request-envelope session state"
[10]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/specification/v0.1.0/response-envelope.json#L88-L95 "ACS response-envelope chain hash"
[11]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/inspect/extend_cyclonedx.md#L70-L74 "Extending CycloneDX — Inspect serialization note"

*Audit completed against pinned revision `dc265475139a922824f0c817e2ecc2a2ce31c06c`.*

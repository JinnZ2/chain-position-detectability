# ACS-06 — OWASP Agent Control Standard v0.1.0

**Audit result: NEGATIVE.** The reviewed requirements construct a Guardian-maintained, server-side audit chain and require a signed rolling `chain_hash` in particular Guardian responses. They do **not** require the executing Observed Agent or a subagent to receive or query its predecessor, successor, ordinal/depth, membership set, parent–child location, or an equivalent representation of its position in a larger execution chain. An opaque chain head can be received at the agent boundary, but it does not itself encode or disclose chain position. The standard assigns useful verification to an observer that records traffic or to an auditor that can recompute the chain, rather than requiring an agent-facing chain-position interface.[1]

## Audit question and decision rule

The question is narrow: does a normative ACS requirement put **evidence of an agent's chain position inside that executing agent**? A positive result requires the agent itself to receive or be able to query its predecessor, successor, depth, chain membership, or an equivalent location in a wider chain. A gateway/Guardian ledger, external audit record, middleware trace, dashboard, or post-hoc reconstruction is not enough. A signed commitment is likewise insufficient unless the requirement makes it usable by the executing agent to establish one of those position facts.

This record reviewed Instrument §§8–9.2 and the supplied Intent, Agents, and Identity concepts, plus the named Session Lifecycle concept. It treats each discrete deontic proposition as a clause, including repeated normative restatements in concept pages. **46 normative clauses were reviewed.** Examples and explanatory paragraphs are identified but are not used as requirements.

## Bottom-line evidence

The strongest locus statement is in Instrument §8:

> “**State the Guardian Agent maintains across a session.**”[1]
>
> “The SessionContext container is intentionally not schematized in v0.1. … the container that holds them is **server-side state** and remains implementation-defined.”[1]

Section 8.6 then requires publication of only the resulting chain head:

> “For every step where the Guardian writes a ContextEntry (the content-bearing steps), the Guardian **MUST include the resulting `chain_hash` in its response**, and that `chain_hash` **MUST be covered by the response signature** (§10).”[1]

That is a Guardian-to-Observed-Agent wire artifact, not an agent-facing view of the ledger. The same section explains the intended verifier: “an observer that records traffic” can detect a later rewrite, and says an “Observed Agent or external auditor” should treat an inconsistency with a *recomputed* chain as an integrity event.[1] No reviewed clause requires an Observed Agent to retain prior heads, receive ContextEntries, receive a predecessor/successor link, ask for the ledger, recompute it, or be told its index/depth. A rolling SHA-256 value is a commitment to state, not a self-describing position: a single head neither exposes the number of prior entries nor identifies them.

The closest subagent requirement is also ledger-directed:

> “When a subagent is spawned, the **audit chain MUST record** how the subagent's `Intent.parsed` relates to the parent's ….”[5]

It requires recording a relationship in the audit chain. It does not require delivery of that relationship, the parent identity, a nesting depth, or a chain-membership fact to the child while it executes. It is therefore negative under the stated rule.

## Normative-clause inventory and control locus

The table records every discrete normative proposition in the assigned unit. “Negative” in the last column means the clause does not meet the inside-agent criterion; it does **not** mean that the security control is absent or ineffective for its stated purpose. “Closest” identifies language that might superficially look relevant, followed by the limiting reason.

| No. | Source and clause | Exact decisive language | Control locus | Chain-position assessment |
|---:|---|---|---|---|
| 1 | Instrument §8 opening paragraph | “The Observed Agent **MAY also send** `session_id` and a `chain_hash` for cross-checking.” | Observed Agent → Guardian request | Negative. Optional cross-check transmission does not require the agent to receive a predecessor, successor, depth, membership, or a queryable chain view. |
| 2 | Instrument §8 opening paragraph | “deployments that do not emit `sessionStart` **MAY allow** the Guardian to implicitly initialize the chain” | Deployment/Guardian | Negative. This permits a Guardian initialization behavior; it provides no agent-facing chain position. |
| 3 | Instrument §8.1 | “**Required:** `entry_id`, `step_id`, `step_type`, `entry_hash`.” | Guardian audit-entry schema | Negative. Entry content is ledger data, not required agent-visible position information. |
| 4 | Instrument §8.1 | “**SHOULD:** `request_hash` … `timestamp`, `provenance_summary`, `previous_hash` ….” | Guardian audit-entry schema | Negative. A `previous_hash` is specified for an entry, but entries are not required to be exposed to the executing agent. |
| 5 | Instrument §8.1 | “deployments claiming the **ACS-Audit** profile **MUST populate** `request_hash`” | Guardian/audit implementation | Negative. Request-content commitment is not chain position. |
| 6 | Instrument §8.1 | “`previous_hash` (**required for every entry except the first**).” | Guardian audit-entry schema | Negative. This describes ledger linkage, not an agent query or delivery requirement. |
| 7 | Instrument §8.2 | “Conformant Guardians **MUST compute** `entry_hash` this way” | Guardian | Negative. Hash computation is Guardian-side. |
| 8 | Instrument §8.2 | “Alternative canonicalization schemes are **not permitted** in v0.1.” | Guardian/implementation | Negative. Interoperable hashing does not expose location to the agent. |
| 9 | Instrument §8.4 | “`parser_provenance` (**REQUIRED if `parsed` present**; `origin` **MUST be** `user_input`)” | Intent wire/schema and framework | Negative. This identifies intent provenance, not execution-chain position. |
| 10 | Instrument §8.4 | “`origin` **MUST be** `user_input`” | Framework/Intent validation | Negative. Same reason as row 7. |
| 11 | Instrument §8.4 | “The framework **MUST enforce** it” | Framework enforcement | Negative. Intent immutability has no position-disclosure requirement. |
| 12 | Instrument §8.4 | “any attempt to modify `Intent.parsed` … **MUST be ignored or rejected**” | Framework enforcement | Negative. This regulates capability mutation, not lineage visibility. |
| 13 | Instrument §8.4 | “and **SHOULD be recorded as an audit event**.” | Audit record | Negative. Post-hoc/audit recording is expressly outside the criterion. |
| 14 | Instrument §8.5 | “Guardian Agents **MAY archive** entries” | Guardian/server-side SessionContext | Negative. This confirms Guardian custody of entries; it creates no agent access. |
| 15 | Instrument §8.5 | “Archival **MUST preserve** `chain_hash`, `provenance_summary`, and `intent`.” | Guardian archival store | Negative. Preserved audit data remains server-side. |
| 16 | Instrument §8.5 | “A mismatched `chain_hash` **SHOULD trigger** an audit event.” | Audit/Guardian | Negative. The required action is an audit event, not an executing agent's position view. |
| 17 | Instrument §8.6 | “the Guardian **MUST include** the resulting `chain_hash` in its response” | Guardian → Observed Agent wire response | **Closest, but negative.** The agent can receive an opaque head, but the requirement gives no predecessor, successor, depth, membership, entry list, or query mechanism. |
| 18 | Instrument §8.6 | “that `chain_hash` **MUST be covered** by the response signature” | Guardian response signature | Negative. Authenticity of a non-positional opaque commitment does not make position knowable. |
| 19 | Instrument §8.6 | “A Guardian … **MAY DENY** … or return the `CHAIN_MISMATCH` error” | Guardian | Negative. This is Guardian enforcement after an optional cross-check. |
| 20 | Instrument §8.6 | “An Observed Agent or external auditor … **SHOULD treat** it as an integrity event” | Observed Agent or external auditor | **Closest, but negative.** It presupposes an inconsistent *recomputed chain*; the standard does not require the executing agent to receive the entries or perform that recomputation. |
| 21 | Instrument §9 | “ASK approvers **MAY be** human, agent, or service.” | Approver-role model | Negative. It assigns eligible approver types, not chain position. |
| 22 | Instrument §9 | “Approver authentication is **REQUIRED**.” | Guardian/Approver trust boundary | Negative. Authentication is distinct from execution-chain location. |
| 23 | Instrument §9 | “Guardian **MUST verify** approver identity against policy.” | Guardian | Negative. Guardian-side policy control. |
| 24 | Instrument §9 | “Approvers **MUST NOT** return ASK.” | Approver | Negative. Single-hop approval limits do not disclose agent-chain relationships. |
| 25 | Instrument §9.1 | “the approver's grant **MAY include** an `intent_extension` field” | Approver → Guardian ASK exchange | Negative. Capability extension is not chain-position evidence. |
| 26 | Instrument §9.1 | “the Guardian **MUST** … Append the capabilities to `Intent.parsed`.” | Guardian/session state | Negative. Session capability state is not a chain-position interface. |
| 27 | Instrument §9.1 | “the Guardian **MUST** … Write a ContextEntry with `step_type: \"intent_extension\"`” | Guardian audit chain | Negative. Records an extension in the ledger only. |
| 28 | Instrument §9.1 | “the Guardian **MUST** … Carry the extension's `provenance` forward” | Guardian/session audit state | Negative. Provenance distinction is not agent position. |
| 29 | Instrument §9.1 | “a Guardian operating under `scope_mode: strict` **MUST NOT honor** extensions” | Guardian/policy | Negative. Policy-enforcement locus. |
| 30 | Instrument §9.2 | “the Guardian **MUST NOT return** `ASK`.” | Guardian | Negative. It changes the disposition sent to incapable clients, not chain data exposed to them. |
| 31 | Instrument §9.2 | “The Guardian **MUST instead substitute** one of” | Guardian | Negative. Same reason as row 28. |
| 32 | Instrument §9.2 | “deployments **SHOULD prefer** `DEFER` … and `DENY` ….” | Deployment policy | Negative. No position exposure. |
| 33 | Concepts › Intent, Immutability | “`Intent.parsed` **MUST NOT be modified** by the runtime LLM, by tool outputs, or by any data crossing an untrusted channel.” | Runtime/framework | Negative. It limits authority changes. |
| 34 | Concepts › Intent, Immutability | “It may grow only through approver action via the ASK flow.” | Approver/Guardian ASK process | Negative. It is an immutability exception, not agent-chain visibility. |
| 35 | Concepts › Intent, Extending Intent | “The sole mechanism for extending `Intent.parsed` … is an Approver's `intent_extension` returned via the ASK flow.” | Approver/Guardian ASK process | Negative. Restates the permitted extension path only. |
| 36 | Concepts › Intent, Extending Intent | “a Guardian **MUST NOT honor** an extension that adds capabilities the deployment policy forbids” | Guardian/policy | Negative. Guardian policy enforcement. |
| 37 | Concepts › Agents, Guardian Agent | “A Guardian **MUST log** every decision with its reasoning, the evaluator's model identifier, and confidence when available.” | Guardian decision log | Negative. Logging/observability is explicitly insufficient under the criterion. |
| 38 | Concepts › Agents, Approver | “An Approver **MAY be** human, agent, or service.” | Approver-role model | Negative. Repeats the role permission in §9. |
| 39 | Concepts › Agents, Approver | “Approver authentication is **REQUIRED**.” | Guardian/Approver trust boundary | Negative. Repeats the §9 authentication requirement. |
| 40 | Concepts › Agents, Approver | “The Guardian **MUST verify** the Approver's identity against policy” | Guardian | Negative. Repeats §9's Guardian-side check. |
| 41 | Concepts › Agents, Approver | “The Approver's grant **MAY extend** `Intent.parsed` through an `intent_extension`” | Approver/Guardian ASK process | Negative. It concerns authorized capability expansion. |
| 42 | Concepts › Agents, Approver | “Approvers **MUST NOT** themselves return `ask`.” | Approver | Negative. Repeats the single-hop limitation. |
| 43 | Concepts › Identity, Principals and descriptors | “Three identities are distinct and **MUST NOT be conflated**” | Identity model/deployment | Negative. It distinguishes roles but provides no execution-chain location. |
| 44 | Concepts › Identity, Authentication | “ACS mandates **no authentication mechanism**.” | Deployment-defined authentication boundary | Negative. It allocates authentication choice to deployment; it is not a chain-position facility. |
| 45 | Concepts › Session Lifecycle, Subagent | “the audit chain **MUST record** how the subagent's `Intent.parsed` relates to the parent's” | Audit chain (Guardian-maintained by §8) | **Closest, but negative.** Parent–child derivation is recorded, not required to be disclosed to the child or parent as execution-time chain position. |
| 46 | Concepts › Session Lifecycle, Subagent | “A Guardian **MAY deny** a spawn whose derivation would grant capabilities the parent's Intent does not authorize.” | Guardian | Negative. Guardian sees/evaluates derivation; no subagent-facing relation or depth is mandated. |

## Interpretive notes on the closest language

### Signed chain-head publication is not self-location

The standard does require that a content-bearing-step response carry a signed `chain_hash`.[1] That requirement places **an opaque chain commitment** at the response boundary, so it should not be described as purely internal observability. It still fails this audit's positive test. The required value has no specified count, index, entry collection, predecessor/successor identifier, parent/child identifier, or inclusion proof. The cited response obligation also does not require the Observed Agent to preserve the prior value or call an endpoint to obtain the ContextEntries. Consequently, an executing agent that cannot observe other steps cannot infer whether other unseen steps exist or where it lies among them from the required artifact alone.

The text itself describes the security effect as allowing “an observer that records traffic” to detect a later rewrite.[1] That is an external, longitudinal observation function. The separate recommendation directed at an Observed Agent applies only when it “finds a published `chain_hash` inconsistent with the recomputed chain.”[1] The standard does not normatively make the full chain, an inclusion proof, or a recomputation capability available to that agent. This is therefore not a positive requirement under the supplied criterion.

### Parent–child derivation is auditable, not necessarily knowable by the child

The Session Lifecycle page says each child has its own session and SessionContext and that “the parent–child relation is recorded.” It follows this with the normative audit-chain rule in row 45.[5] This is useful lineage construction, but the grammar and the Instrument section's defined locus point to an audit record. No clause says the child receives its parent session identifier, a nesting level, a derivation record, a relation proof, or a query handle. No clause requires the parent to receive the child relationship either. The following research-agent/summarizer paragraph is explicitly an *Example* and does not alter that result.[5]

### Intent, identity, approval, and decision controls are not substitute chain-position controls

Intent requirements bind authorized capabilities before untrusted data enters and tightly constrain subsequent changes.[2] Approver requirements authenticate the approver, prohibit recursive ASK, and record session-scope extensions.[1] [3] Identity requires role separation without prescribing an authentication scheme.[4] Guardian decision logging makes adjudication auditable.[3] These are meaningful governance controls, but their loci are the framework, Guardian, policy, Approver, or audit record. None makes an executing agent aware of its place within a broader agent chain.

## Non-normative material deliberately excluded from the finding

The following passages were read to avoid confusing commentary with requirements. They are not treated as independent normative evidence: the §8 explanatory claim that publishing lets an observer detect later rewrites; the §8.6 description of the HMAC baseline and non-repudiation limits; the §9.2 explanation of security preservation for incapable clients; the Intent web-page deletion example; the Agents wire-transfer example; and the Session Lifecycle research-agent/summarizer example.[1] [2] [3] [5] They are consistent with the negative result but do not independently establish it.

## Locus summary

| Locus | What the reviewed standard requires there | Does it put chain position inside the executing agent? |
|---|---|---|
| **Guardian server-side SessionContext/audit chain** | Hashing, ContextEntry construction, archival, intent-extension entries, and subagent derivation recording. | No. §8 expressly defines the container as server-side state. |
| **Guardian response boundary** | A signed rolling `chain_hash` after every ContextEntry-writing step. | No. The required artifact is a bare head, not a self-location representation or queryable ledger. |
| **Observed Agent** | May send a `session_id` and `chain_hash` for cross-checking; should regard a detected inconsistency with a recomputed chain as an integrity event. | No mandatory receipt of entry history, required retention, recomputation, or chain-position query. |
| **Approver** | Authentication, single-hop restriction, possible intent-extension grant. | No. Approval authority is not execution-chain position. |
| **Deployment/policy/framework** | Strict-scope limits, client ASK-capability determination, identity mechanism selection, and Intent immutability. | No. These define enforcement conditions rather than agent-visible chain topology. |
| **External observer/auditor** | The rationale for published heads is detection by a party that records traffic; an auditor may recompute. | No under the criterion, because this is external/post-hoc visibility. |

## Limitations and preserved uncertainty

1. **Opaque-head ambiguity is resolved conservatively.** A response `chain_hash` is evidence that a Guardian has committed to a rolling chain. If “equivalent location” were defined so broadly that any cryptographic commitment counted as position evidence, §8.6 could be read differently. Under the task's concrete examples—predecessor, successor, depth, membership, or equivalent—and its exclusion of external observability, a head without required agent-side history or a query mechanism does not establish position. The classification is therefore negative, not positive.
2. **No implementation behavior was inferred.** An implementation could voluntarily expose ContextEntries, provide a depth field, or give an agent an audit-query API. Such behavior is not required by the reviewed v0.1.0 clauses and cannot change this standards result.
3. **“Audit chain” locus is read with §8.** The Session Lifecycle concept does not restate storage location in its subagent paragraph. Instrument §8 defines SessionContext as Guardian-maintained server-side state, so that definition was used for the named audit chain. The concept page does not override it with a child-facing disclosure obligation.
4. **This is not an audit of other ACS pillars or versions.** Trace, Inspect, A2A v0.2 material, schemas beyond the cited Instrument content, vendor extensions, and runtime implementations were outside the assigned unit.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md "OWASP Agent Control Standard v0.1.0 — Instrument specification, §§8–9.2"

[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/intent.md "OWASP Agent Control Standard v0.1.0 — Intent concept"

[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/agents.md "OWASP Agent Control Standard v0.1.0 — Agents concept"

[4]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/identity.md "OWASP Agent Control Standard v0.1.0 — Identity concept"

[5]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/session-lifecycle.md "OWASP Agent Control Standard v0.1.0 — Session Lifecycle concept"

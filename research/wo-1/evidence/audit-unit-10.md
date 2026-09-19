# ACS-05 — Provenance and trust basis: chain-position detectability audit

**Standard:** OWASP Agent Control Standard (ACS) v0.1.0
**Unit:** Instrument §7, including §§7.1–7.2; Concepts: *Provenance* and *Trust basis*
**Pinned revision:** `dc265475139a922824f0c817e2ecc2a2ce31c06c`
**Result:** **NEGATIVE**
**Status:** **DERIVED** from the observed normative text below.
**Normative clauses reviewed:** **16**. This count includes eleven RFC-keyword clauses in Instrument §7–§7.2, the two expressly normative Provenance statements, the two expressly normative Trust-basis invariants, and the Trust-basis section’s materially prescriptive but lower-case statement that the basis “must travel.” It does not count explanatory prose or examples as requirements.

## Conclusion

No reviewed normative requirement obliges an **executing agent** to receive or query evidence of its own predecessor, successor, depth, membership, or equivalent position in an execution/delegation chain. ACS requires deterministic provenance for **data** and constrains a Guardian or receiver’s treatment of trust labels. These controls can preserve and evaluate data lineage, including across an A2A boundary, but they do not require a chain-coordinate interface within the executing agent’s own decision context.

The closest control is the receiver rule in Instrument §7.1: a receiver, “especially across A2A or multi-Guardian boundaries,” must re-derive a received label from `origin` and `source_id`. That requirement is about local trust evaluation of an inbound datum; it does not require the receiver to learn the prior agent’s identity, its relationship to the receiver, the number of delegation hops, the members of a chain, or any successor. In addition, `source_id` and `derived_from` are optional in the §7 wire shape. The all-or-nothing profile rule concerns whether every **data-bearing field in emitted hook payloads** has a provenance object; it does not add execution-chain position.

> **Classification rule applied.** A positive result requires a normative requirement that places chain-position evidence *inside the executing agent*: evidence of predecessor, successor, depth, membership, or an equivalent location in the wider chain. Gateway-side or Guardian-side lineage, middleware/framework processing, audit records, and post-hoc observability are negative unless the text requires exposure inside that execution boundary.

## Scope and source verification

**OBSERVED.** The three authoritative GitHub sources were read at the pinned commit specified for this unit. Instrument §7 describes the Provenance concept as normative and supplies the wire and trust-classification rules. The two linked concept pages were read in full. Citations below resolve to those pinned source pages and give the section and source-line locations used for this audit. [1] [2] [3]

“Agent” is overloaded in ACS: the Instrument specification calls an LLM-backed system the **Observed Agent** and a policy enforcement point the **Guardian Agent**. This audit uses the work order’s narrower criterion: the relevant locus is the agent that is executing the work and would need to know its own position in the larger chain, not merely an external Guardian, a framework hook producer, or an auditor.

## Clause-by-clause evidence

### Instrument §7 — provenance production and session coverage

1. **OBSERVED — Instrument §7, lines 208–210.**

   > “Under **`deterministic`**, the producer MUST attach a Provenance object to **every** data-bearing field in every hook payload it emits. Partial population within a producing session is non-conformant: provenance is all-or-nothing per session.” [1]

   **Locus:** deterministic producer/framework emitting an outbound hook payload. **Finding:** it requires full per-field coverage for provenance data, not a predecessor/successor/depth/membership fact inside the executing agent. The mandated object can identify origin and optional lineage, but no required field expresses the executing agent’s chain position.

2. **OBSERVED — Instrument §7, lines 210–211.**

   > “A Guardian whose policy requires provenance MUST refuse such a session at handshake time (§4) rather than accept provenance-free payloads.” [1]

   **Locus:** Guardian at session handshake. **Finding:** refusal occurs at the enforcement boundary. It does not expose chain information to the agent doing the work.

3. **OBSERVED — Instrument §7, line 213.**

   > “When a Provenance object is emitted, all of its own required fields MUST be populated.” [1]

   **Locus:** producer/schema conformance. **Finding:** the required object fields are `provenance_id` and `origin`; `source_id` and `derived_from` are optional in the immediately following table (lines 215–220). A unique session-local provenance identifier and origin channel are not a required execution-chain position.

### Instrument §7.1 — optional trust label

4. **OBSERVED — Instrument §7.1, lines 226–228.**

   > “The framework, not the LLM, MUST attach the label, deterministically, based on which channel data crossed. `trust` is never a content judgment and never a producer claim.” [1]

   **Locus:** framework at a channel boundary, expressly outside the LLM’s authorship. **Finding:** this is data-label production, not required delivery of a chain coordinate to the executing agent.

5. **OBSERVED — Instrument §7.1, lines 228–229.**

   > “For data with `origin: agent_generated`, the framework MUST compute `trust` as the minimum trust of the entries in `derived_from` (monotonicity rule). No amount of LLM processing launders untrusted data into trusted data.” [1]

   **Locus:** framework computing a data label. **Finding:** the trust-label monotonicity control preserves the minimum trust of data lineage. It neither identifies an executing agent’s predecessor nor makes chain depth or membership available in its execution context.

6. **OBSERVED — Instrument §7.1, line 230.**

   > “Receivers (especially across A2A or multi-Guardian boundaries) MUST treat the field as a hint and re-derive trust against local policy keyed off `origin` + `source_id` rather than honor a remote-asserted label at face value.” [1]

   **Locus:** receiver’s local trust-policy evaluator; ACS names A2A and multi-Guardian receivers but does not define this receiver as the executing LLM/agent. **Finding:** this is the closest text because it applies on a boundary crossing. Even if a receiver is implemented within an agent runtime, the required inputs are an inbound datum’s channel/origin and optional source identifier; the clause does not require predecessor identity, successor identity, hop depth, chain membership, or an equivalent execution-chain location. **Classification impact:** negative, with the locus ambiguity recorded below.

### Instrument §7.2 — default mapping and producer prohibition

7. **OBSERVED — Instrument §7.2, line 234.**

   > “Deployments MAY override in policy but SHOULD record overrides in audit metadata.” [1]

   **Locus:** deployment policy and audit metadata. **Finding:** this discretionary/SHOULD governance rule does not place information in an executing agent.

8. **OBSERVED — Instrument §7.2, line 246.**

   > “Provenance MUST be populated by deterministic code outside the LLM's output path.” [1]

   **Locus:** deterministic code outside the LLM path. **Finding:** the standard expressly locates provenance generation outside the LLM output path. It is therefore not a requirement that the executing LLM receive an internal chain-position fact.

9. **OBSERVED — Instrument §7.2, line 246.**

   > “Implementations MUST NOT instruct the LLM to produce it.” [1]

   **Locus:** implementation/LLM interface. **Finding:** this prevents the LLM from self-authoring data provenance; it does not supply the LLM with an execution-chain position.

10. **OBSERVED — Instrument §7.2, line 246.**

    > “Guardians whose policies require Provenance MUST refuse the session at handshake time rather than silently degrading enforcement.” [1]

    **Locus:** Guardian handshake enforcement. **Finding:** this repeats the session-refusal control for deterministic versus `none` producers. It supplies no inside-agent chain-position visibility.

11. **OBSERVED — Instrument §7.1 explanatory framing, lines 222–224; §7.2 default table, lines 232–244.** The paragraph says the enum is optional and that v0.1 does not require Guardians to populate it. The table maps origins to default trust and maps `agent_generated` to the minimum trust of `derived_from`. These are **commentary/default mapping**, except for the `MAY`/`SHOULD` sentence counted above. They explain the trust-label rules but add no independent execution-chain-position requirement. [1]

### Provenance concept — lineage and deterministic assignment

12. **OBSERVED — Concepts › Provenance, §“Lineage is transitive,” lines 17–20.**

    > “**Lineage spans derivation (normative).** When data is derived from other data, its `derived_from` lineage is the union of the lineage of its inputs. Summarization and compaction are derivations: the summary that comes out carries the combined lineage of everything that went in.” [2]

    **Locus:** provenance-producing framework/data transformation. **Finding:** transitivity prevents data-lineage loss during summarization and compaction. It preserves where the data came from, not where the current agent sits in an agent chain. The succeeding paragraph and web-page summary example are explanatory; they show a Guardian seeing retrieved-page provenance, not a chain-coordinate API within the executing agent.

13. **OBSERVED — Concepts › Provenance, §“Deterministic assignment,” lines 25–27.**

    > “**Provenance is framework-assigned (normative).** The framework, not the LLM, assigns `origin`, `source_id`, and `derived_from`, based on the code path a value came through. These fields are never inferred by the model, never a content judgment, and never a producer claim.” [2]

    **Locus:** framework/code path, rather than the LLM. **Finding:** the source makes the outside-LLM locus explicit. It requires deterministic origin and lineage assignment, not delivery of execution topology to the agent.

### Trust-basis concept — non-escalation and propagation

14. **OBSERVED — Concepts › Trust basis, §“Invariants,” lines 23–25.**

    > “**The rungs do not collapse (normative).** A Guardian MUST NOT treat an asserted fact as attested. The basis of a fact is part of the fact; relying on a fact above its actual basis is an error.” [3]

    **Locus:** Guardian trust evaluation. **Finding:** this prevents an external policy decision point from elevating a fact’s basis. It has no chain-position disclosure requirement for the executing agent.

15. **OBSERVED — Concepts › Trust basis, §“Invariants,” lines 25–27.**

    > “**Deterministic attachment is not a producer claim (normative).** Where ACS specifies a deterministically attached fact (a Provenance record's `origin` is the canonical case), the framework assigns it from the code path the value came through, never the producer of the data and never the LLM.” [3]

    **Locus:** framework/code path. **Finding:** this forecloses provenance/trust self-assertion by the data producer or LLM; it does not establish that the executing agent can inspect its own execution-chain context.

16. **OBSERVED — Concepts › Trust basis, §“The basis must travel,” line 31.**

    > “When a fact is summarized, written to memory, or passed across a boundary, its trust basis must travel with it. A derivation of asserted content is asserted; it does not become attested by being restated.” [3]

    **Locus:** the cross-boundary data-transfer design. **Finding:** this is materially prescriptive anti-laundering language, but it is not capitalized as a RFC-style MUST, does not identify an enforcing actor, and is not tagged “(normative).” It has been reviewed conservatively because it bears on the requested laundering issue. Even read as binding, it requires preservation of a datum’s basis, not the executing agent’s chain position. The next paragraph is an explanatory example involving a second agent and does not create an additional requirement.

## Control-locus assessment

| Control | Required locus in the source | What is visible or operated on | Why it is not inside-agent chain position |
|---|---|---|---|
| All-or-nothing provenance profile | Producer/framework emitting hook payloads | A Provenance object on each data-bearing field | The object records data origin and possible lineage; it does not require the executing agent to receive its place in an agent chain. |
| Provenance-required session refusal | Guardian handshake | Producer capability declaration and session acceptance/refusal | The Guardian decides whether to admit the session; no agent-chain coordinate is delivered to the worker. |
| Trust label and monotonicity | Framework at data-channel crossing | `trust` label and `derived_from` inputs | This prevents a datum from becoming trusted via LLM processing, but says nothing about predecessor/successor/depth/membership. |
| Local re-derivation | Receiver’s local policy evaluator | `origin` and `source_id` from the received datum | A receiver assesses source channel rather than being told its own execution-chain location. |
| Trust-basis non-escalation | Guardian | Asserted versus attested basis | This governs evaluation by the policy enforcement point, not introspection by the executing agent. |
| Lineage/basis propagation | Framework/data boundary | Data provenance and basis through derivation, memory, or a boundary | The control addresses data lineage laundering; it does not expose the topology of agents that handled the data. |

## Locus distinction and decision rationale

**DERIVED.** The standard uses provenance as an information-flow control. Its required facts are about a value: channel `origin`, potentially a `source_id`, and potentially prior provenance identifiers in `derived_from`. The standard requires this information to be assigned by deterministic framework code and, in a producing session, attached to outbound hook payloads. A Guardian may consume it and a receiver must locally re-derive an optional remote trust label. These are valuable anti-laundering controls for **data**.

They are not evidence that the executing agent can determine *“I am step n in a chain”* or identify other steps. No reviewed clause requires an API, prompt/context field, runtime query, or mandatory metadata that tells the agent who delegated to it, whom it delegates to, how many hops surround it, whether it belongs to an execution chain, or any equivalent chain-location fact. `derived_from` is not an agent-chain field and is optional in the v0.1 object; it identifies prior **Provenance objects** for data, not necessarily the agents or execution steps that created them.

Accordingly, gateway/Guardian/framework lineage and trust processing cannot satisfy the work-order criterion by inference. The decisive negative evidence is the combination of the closest mandatory location clauses: provenance is required “outside the LLM's output path,” the framework rather than the LLM attaches labels and fields, and a Guardian/receiver performs trust enforcement or re-derivation. [1] [2] [3]

## Limitations and preserved uncertainty

1. **“Receiver” is not fully typed.** Instrument §7.1 says “Receivers (especially across A2A or multi-Guardian boundaries)” without defining whether a particular receiver is an LLM-backed observed agent, a framework component, or a Guardian. This makes the enforcement locus somewhat broad. It does not change the result because the required inputs remain data-origin/source facts rather than execution-chain position.
2. **A deployment can add metadata.** The optional `trust` field, optional `source_id`, optional `derived_from`, and deployment policy may carry richer vendor-specific information. The audited v0.1 requirements do not require that information to identify predecessor/successor/depth/membership inside the executing agent, so optional implementation practice cannot support a positive classification.
3. **Data lineage is not execution lineage.** A transitive `derived_from` graph may contain useful evidence about data transformation. The text does not require mapping it to agent identities or a delegation topology. Treating it as proof that an agent knows its chain location would be an unsupported inference.
4. **Concept-page force is partially heterogeneous.** The Provenance and Trust pages explicitly mark four statements as normative. The Trust page’s “basis must travel” sentence is central to the rationale but lacks uppercase MUST, an identified actor, and a normative label. It was included in the clause review rather than silently discounted; it remains non-positive under either reading.
5. **Out of scope.** This is a textual normative audit of the three specified pages at the pinned revision. It does not audit implementation behavior, other ACS sections, Trace, external gateway telemetry, or a vendor extension.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/specification.md#L204-L247 "OWASP Agent Control Standard v0.1.0 — Instrument Specification, §7–§7.2"

[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/provenance.md "OWASP Agent Control Standard v0.1.0 — Provenance concept"

[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/trust.md "OWASP Agent Control Standard v0.1.0 — Trust basis concept"

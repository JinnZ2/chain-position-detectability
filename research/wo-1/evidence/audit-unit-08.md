# WO-1 Evidence Record — ACS-03

## Determination

**Result: NEGATIVE.** The reviewed ACS v0.1.0 unit establishes extensive lifecycle, provenance, and Guardian-facing control points, including a mandatory record of a subagent's Intent derivation. It does **not** normatively require the executing agent to receive or query evidence of its own predecessor, successor, depth, membership, or equivalent position in a larger agent-execution chain. The strongest near-miss is a requirement that **the audit chain** record the child Intent's relation to the parent, coupled with a Guardian's discretionary denial power. That is an audit/control-plane locus, not an explicit inside-agent exposure requirement. [1] [3]

This conclusion uses the WO-1 test strictly. A field that a framework sends at a hook, a Guardian evaluates, or an audit chain retains is not treated as chain-position information available to the executing agent unless the standard requires that availability within the agent execution boundary. No reviewed normative clause does so.

## Scope, source, and locator convention

This audit covers the complete three specified Markdown sources at commit `dc265475139a922824f0c817e2ecc2a2ce31c06c`: **Hooks** (including Overview through `protocols/MCP/*`), **Extending MCP**, and the **Subagent** portion of Session lifecycle. The sources are Markdown and have no fixed pages. Therefore, each location below gives the source heading and immutable-source line number; it is the page-equivalent locator for this revision. The local review copy was checked out at the cited commit rather than relying on search-result excerpts. [1] [2] [3]

I reviewed **34 individual modal propositions** in **22 sentences/entries containing modal language**. The count treats separately stated obligations or permissions in a sentence as separate propositions, such as the two provenance MUSTs in `postCompact`. It includes the lower-case MCP `must` statements because the section directs what agents must do. It also conservatively includes the lower-case explanatory `must` at Hooks line 240 as an **ambiguous-formality near-miss**, because it describes a required record even though it appears in rationale rather than the labelled decision/payload contract; the explicit upper-case requirement in Session lifecycle §Subagent independently covers the same record.

> **WO-1 chain-position test.** A POSITIVE result requires a normative requirement that puts chain-position evidence **inside the executing agent**: the agent itself receives or can query a predecessor, successor, depth, membership, or equivalent location in a larger execution chain. Gateway lineage, Guardian decisions, SessionContext/audit chains, operator views, middleware, and post-hoc records are NEGATIVE unless exposure inside the agent is itself required.

## Decisive evidence and control loci

The principal subagent obligation is explicit about its record-keeper but not about inside-agent availability:

> “When a subagent is spawned, the audit chain MUST record how the subagent's `Intent.parsed` relates to the parent's: inherited in full, a strict subset, derived from a parent directive, or fresh. A Guardian MAY deny a spawn whose derivation would grant capabilities the parent's Intent does not authorize.” — Session lifecycle §Subagent, line 23. [3]

The companion hook names the correlation fields, but frames their destination as an event/audit record: `subagent_session_id`, `parent_session_id`, and `parent_step_id`; it says each subagent has its own SessionContext and audit chain and that “the parent–child relation is captured in the `subagentStart` payload.” — Hooks §`subagentStart`, lines 242–246. [1] These materials require recording and Guardian decision-making. They do not say that the child executes with, receives, or can query `parent_session_id`, the parent Intent, an ancestor chain, a depth, a successor, or membership information.

The unit's other strongest internal-facing language concerns a different subject: MCP-wrapping agents must “understand and enforce ACS responses” before forwarding/consuming MCP traffic. — Extending MCP §“To extend MCP protocol,” line 21. [2] This places a **Guardian disposition** in an MCP agent's enforcement path, but does not require that disposition to convey chain position. It therefore remains NEGATIVE under the stated test.

| Control locus | What the unit requires or permits | WO-1 treatment |
|---|---|---|
| **Framework / hook emitter** | It must emit `toolCallRequest` for every outward action; it creates compaction provenance and emits lifecycle payloads. | Enforcement telemetry/control boundary, not inside-agent chain self-knowledge. |
| **Guardian** | It may deny/modify lifecycle, compaction, skill, AgBOM, and MCP-wrapped operations; it evaluates subagent-Intent derivation. | External policy decision-maker. Negative unless the standard requires it to expose chain position to the executing agent; it does not. |
| **Audit chain / SessionContext** | It records post-compaction state and subagent Intent derivation; it captures parent–child relation. | Chain reconstruction and lineage evidence, not a required agent-query interface. |
| **Executing MCP agent** | Conditional on claiming MCP wrapping, it must deliver wrapped messages to the Guardian and understand/enforce Guardian responses. | The one mandatory internal enforcement behavior, but its required input is a disposition, not predecessor/successor/depth/membership evidence. |
| **LLM** | The framework, “not the LLM,” populates compaction `derived_from`. | Explicitly removes that lineage-population task from the LLM; no self-location requirement follows. |
| **Subagent / parent agent** | The relationship is represented in a hook payload and audit chain. | No requirement that either running agent receive or query the relationship as execution-context information. |

## Complete normative-clause review

The table records every reviewed modal proposition. “Negative locus” means that the proposition has a specified control/audit locus but does not impose inside-agent chain-position availability. “No chain-position content” means the clause is unrelated to the test rather than evidence against it.

| # | Source location | Exact decisive language | Normative character | Locus and WO-1 assessment |
|---:|---|---|---|---|
| 1 | Hooks §`sessionStart`, l. 92 | “A Guardian MAY refuse a session whose identity, policy mode, or platform fails policy checks” | Permission | Guardian. No chain-position content. |
| 2 | Hooks §`sessionStart`, l. 94 | “A deployment that does not emit `sessionStart` MAY allow the Guardian to implicitly initialize the chain at the first content-bearing hook” | Permission | Deployment/Guardian and audit-chain initialization. Negative locus. |
| 3 | Hooks §`agentTrigger`, l. 106 | “Guardian MAY rewrite the trigger payload” | Permission | Guardian. No chain-position content. |
| 4 | Hooks §`turnStart`, l. 120 | “a Guardian MAY deny to block the turn from starting” | Permission | Guardian. No chain-position content. |
| 5 | Hooks §`userMessage`, l. 132 | “Guardian MAY redact content before delivery to the agent” | Permission | Guardian-to-agent content control, not chain position. |
| 6 | Hooks §`knowledgeRetrieval`, l. 156 | “Guardian MAY redact retrieved content before injection into the agent context” | Permission | Guardian-to-agent content control, not chain position. |
| 7 | Hooks §`toolCallRequest`, l. 190 | “Frameworks MUST fire `toolCallRequest` for every action that escapes the agent's reasoning context” | Requirement | Framework-to-Guardian enforcement boundary. It makes outward actions visible to policy; it does not make chain position visible inside the agent. |
| 8 | Hooks §`preCompact`, l. 218 | “Guardian MAY return DENY to block compaction” | Permission | Guardian. No chain-position content. |
| 9 | Hooks §`postCompact`, l. 228 | “`origin` MUST be `agent_generated`” | Requirement | Framework-generated provenance. It identifies a content origin, not agent position in a chain. |
| 10 | Hooks §`postCompact`, l. 228 | “`derived_from` MUST equal the union of `provenance_id`s of every entry in `entries_compacted`” | Requirement | Framework-generated provenance. Lineage of summarized inputs, not agent predecessor/successor/depth/membership. |
| 11 | Hooks §`postCompact`, l. 230 | “A Guardian MAY return MODIFY” | Permission | Guardian. No chain-position content. |
| 12 | Hooks §`postCompact`, l. 230 | “but MAY NOT return DENY” | Prohibition | Guardian. No chain-position content. |
| 13 | Hooks §`postCompact`, l. 230 | “The audit chain MUST record the post-compact state regardless” | Requirement | Audit chain. Explicitly record-oriented and not exposed within the executing agent. |
| 14 | Hooks §`subagentStart`, l. 244 | “Guardian MAY DENY — refuse the subagent spawn” | Permission | Guardian. It may use Intent derivation, but no requirement provides chain data to the spawning or child agent. |
| 15 | Hooks §`skillRegister`, l. 270 | “A Guardian MAY deny registration” | Permission | Guardian. No chain-position content. |
| 16 | Hooks §`skillRegister`, l. 270 | “a denied skill MUST NOT become eligible to load” | Prohibition | Framework/skill-lifecycle gate. No agent-chain position. |
| 17 | Hooks §`skillRegister`, l. 270 | “A Guardian SHOULD compare `declared_capabilities` against the union of capabilities the composed tools expose” | Recommendation | Guardian. Component/capability comparison, not execution-chain position. |
| 18 | Hooks §`skillRegister`, l. 270 | “and MAY deny over-broad declarations” | Permission | Guardian. No chain-position content. |
| 19 | Hooks §`skillLoad`, l. 280 | “A load MUST be correlatable to a prior approved `skillRegister` for the same `(skill_id, digest)`” | Requirement | Guardian/audit record binding. This is artifact-registration lineage, not an executing agent's location in an agent chain. |
| 20 | Hooks §`skillLoad`, l. 280 | “is unverifiable and SHOULD be denied” | Recommendation | Guardian. No chain-position content. |
| 21 | Hooks §`skillLoad`, l. 280 | “The framework MAY send a `digest_verified` hint” | Permission | Framework-to-Guardian hint. No chain-position content. |
| 22 | Hooks §`skillLoad`, l. 286 | “Guardian SHOULD deny a load it cannot correlate to an approved `skillRegister`” | Recommendation | Guardian. No chain-position content. |
| 23 | Hooks §`skillLoad`, l. 286 | “SHOULD deny when `load_path` shows a skill loading another outside its declared `composed_skills`” | Recommendation | Guardian. `load_path` is a **skill-composition** path, not a requirement that a running agent knows its position in an agent execution chain. |
| 24 | Hooks §`skillLoad`, l. 286 | “SHOULD deny when the loaded artifact's digest does not match the one vetted at `skillRegister`” | Recommendation | Guardian. No chain-position content. |
| 25 | Hooks §`agbom/snapshot`, l. 330 | “Guardian MAY DENY to refuse a session whose component graph contains a banned model, tool, or peer” | Permission | Guardian. Component-graph policy, not agent chain position. |
| 26 | Hooks §`agbom/changed`, l. 342 | “Guardian MAY DENY to block a hot-swap” | Permission | Guardian. No chain-position content. |
| 27 | Hooks §`protocols/MCP/*`, l. 360 | “Deployments that only need transport-agnostic tool governance MAY collapse MCP tool calls into `steps/toolCallRequest`” | Permission | Deployment architecture. No chain-position content. |
| 28 | Extending MCP §MCP support, l. 12 | “Deployments MAY collapse MCP `tools/call` traffic into the generic `steps/toolCallRequest` / `steps/toolCallResult` hooks” | Permission | Deployment architecture. No chain-position content. |
| 29 | Extending MCP §MCP support, l. 12 | “Deployments SHOULD use `protocols/MCP/*` when policy needs MCP-level distinctions that generic tool hooks would erase” | Recommendation | Deployment/Guardian policy precision. MCP method distinctions are not chain position. |
| 30 | Extending MCP §“To extend MCP protocol,” l. 20 | “Agents using MCP and claiming MCP wrapping **must** deliver wrapped MCP messages to the Guardian using `protocols/MCP/*`” | Requirement (lower-case/italic in source) | Agent-to-Guardian transport. The agent sends messages but is not required to receive/query its chain position. |
| 31 | Extending MCP §“To extend MCP protocol,” l. 21 | “Agents using MCP wrapping **must** understand and enforce ACS responses before forwarding outbound MCP messages or consuming inbound MCP results” | Requirement (lower-case/italic in source) | Inside the MCP agent's enforcement path. Required responses are Guardian dispositions, not positional evidence; therefore negative. |
| 32 | Session lifecycle §Subagent, l. 23 | “the audit chain MUST record how the subagent's `Intent.parsed` relates to the parent's” | Requirement | Audit chain. This is the closest agent-relationship evidence, but the clause selects the audit chain—not the executing agent—as the required recipient/store. |
| 33 | Session lifecycle §Subagent, l. 23 | “A Guardian MAY deny a spawn whose derivation would grant capabilities the parent's Intent does not authorize” | Permission | Guardian. Parent/child Intent comparison occurs at the Guardian control point; no agent-query/exposure mandate. |
| 34 | Hooks §`subagentStart`, l. 240 | “when a subagent spawns, the audit chain must record whether it inherits the parent's `Intent.parsed`, gets a derived intent, or starts fresh” | **Ambiguous formal status; conservatively reviewed** | Audit chain. Even if read as a requirement, it does not require that the parent or child agent receive/query that relationship. |

### Count reconciliation

The 34 rows are the **34 counted modal propositions**. Multi-modal sentences are split as follows: Hooks line 228 supplies two (rows 9–10); line 230 supplies three (rows 11–13); line 270 supplies four (rows 15–18); line 280 supplies three (rows 19–21); line 286 supplies three (rows 22–24); Extending MCP line 12 supplies two (rows 28–29); and Session lifecycle line 23 supplies two (rows 32–33). Row 34 is the lower-case, ambiguous-formality `must` in Hooks line 240, reviewed conservatively.

## Relevant non-normative context, separated from requirements

Several passages are potentially misleading if treated as requirements. They were reviewed but do not change the result:

- Hooks §Overview says `protocols/A2A/*` is “reserved for v0.2” and that “no normative wrapping semantics are defined in v0.1.” (line 53). Thus A2A provides no v0.1 normative chain-position route in this unit. [1]
- Hooks §`subagentStart` says that “the audit chain must record whether [the subagent] inherits” the parent Intent and names parent/subagent checks (line 240). This lower-case explanatory sentence is **ambiguous as to formal normative status**. It is nevertheless no stronger than the explicit Session lifecycle requirement: both place information in the audit chain and Guardian review path, not inside the executing agent. [1] [3]
- The `subagentStart` payload lists `parent_session_id` and `parent_step_id`; the prose says the parent–child relation is “captured in the `subagentStart` payload” (lines 242–246). This establishes available hook data but not a normative delivery/query obligation for the parent or child agent. [1]
- The skill `load_path` is an ordered list of skills leading to activation, and is expressly so the Guardian can see/contain inter-skill cascades (Hooks §`skillLoad`, lines 278–286). It may resemble a path, but it is neither an agent-chain membership/depth field nor inside-agent positional awareness. [1]
- The illustrated MCP scenarios are expressly under “Examples.” They show Agent A sending wrapped calls and processing decisions, but examples cannot supply the missing normative position-exposure requirement. [2]

## Limitations and uncertainty

1. **No page numbering exists.** Immutable Markdown headings and line numbers are used instead. A future revision could reflow lines, which is why the report identifies the exact commit.
2. **Internal architecture is deliberately unspecified in this unit.** A vendor could choose to expose `parent_session_id` or audit-chain contents to a running agent. That implementation possibility is not a POSITIVE finding because no reviewed clause requires it.
3. **The lower-case `must` at Hooks line 240 is formally less clear than the uppercase RFC-style MUST wording elsewhere.** It was conservatively reviewed as a near-miss. Its stated recipient remains the audit chain, so it cannot make the unit positive under either reading.
4. **The conditional MCP requirement is an agent-side obligation but is not positional.** It requires an agent to enforce Guardian responses, not to receive/query predecessor, successor, depth, membership, or an equivalent agent-execution location.
5. **A2A is excluded by the source itself for v0.1.** The unit says its wrapping semantics are deferred/reserved for v0.2; this audit makes no claim about a later version.

## References

[1]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/hooks.md "OWASP Agent Control Standard v0.1.0 — Instrument Hooks"

[2]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/spec/instrument/extend_mcp.md "OWASP Agent Control Standard v0.1.0 — Extending MCP"

[3]: https://github.com/GenAI-Security-Project/agent-control-standard/blob/dc265475139a922824f0c817e2ecc2a2ce31c06c/docs/concepts/session-lifecycle.md "OWASP Agent Control Standard v0.1.0 — Session lifecycle"

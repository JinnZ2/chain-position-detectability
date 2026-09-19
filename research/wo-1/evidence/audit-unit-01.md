# WO-1 evidence record — TOP10-01

## Determination

**Result: NEGATIVE.** The reviewed unit does not require an executing agent to receive or query its predecessor, successor, depth, membership, or another datum that establishes the agent’s location in an execution chain. This holds even under the deliberately broad review used here: every numbered prescriptive mitigation guideline was treated as a candidate requirement. The unit instead places controls in input handling, tool authorization, a human approval flow, configuration management, a policy-enforcement point, execution infrastructure, credential management, and observability. A few controls may operate near an agent at run time, but none requires **chain-position evidence inside the agent execution boundary**.

The conclusion is not an assertion that an implementation could never provide such information. It is a finding about what this unit requires. In particular, the text’s references to *plans*, *delegation chains*, *tool chaining*, *agent intent*, and an *execution cycle* neither name a chain-position field nor require the agent to be able to inspect one.

## Unit and source control

| Field | Evidence |
|---|---|
| Audit unit | `TOP10-01` |
| Standard | *OWASP Top 10 for Agentic Applications 2026*, version 1.0 |
| Unit section | “ASI01: Agent Goal Hijack” and “ASI02: Tool Misuse and Exploitation” |
| Authoritative source read | The complete 57-page version-pinned PDF at the supplied GitHub commit, not a search-result snippet. Its SHA-256 is `a2db94cd00b08e0b3a5e5b619afe024bdbcd74503111085705e4f3dd886fcb5c`. [1] |
| Publication cross-check | OWASP’s resource page identifies the title as *OWASP Top 10 for Agentic Applications for 2026* and dates it December 9, 2025. [2] |
| Pages in scope | Printed pp. 9–14; PDF pages 10–15. Page references below use the **printed** page number, with the PDF page supplied in parentheses. |
| Clause count reviewed | **17 numbered mitigation guidelines**: ASI01 §§1–9 and ASI02 §§1–8. The surrounding descriptions, examples, attack scenarios, notes, and references were also read to distinguish commentary from requirements. |

## Classification test

For this record, a control is positive only if the source requires the **executing agent itself** to receive or query information proving its position in a larger execution chain: for example, its predecessor, successor, depth, membership, or an equivalent location attribute. Agent-independent lineage, logs, dashboards, policy middleware, gateways, and post-hoc monitoring are negative unless the text requires their information to be exposed inside the executing agent.

This OWASP unit is guidance rather than an RFC-style conformance specification. It labels its directions “Prevention and Mitigation Guidelines,” not SHALL/MUST conformance clauses. To avoid understating the test, all 17 numbered guidelines were nevertheless reviewed as prescriptive candidate controls. Only ASI01 guideline 3 contains the word **“must”**; it concerns configuration management and human approval, not chain position.

## Decisive textual evidence

Two passages show why similar vocabulary does not satisfy the test.

> “While LLM06 focuses on model-level autonomy, ASI02 addresses misuse of legitimate tools within agentic plans and delegation chains.” — ASI02, note under “Prevention and Mitigation Guidelines,” printed p. 13 (PDF p. 14). [1]

This is explanatory scope language, not a requirement. It identifies the existence of delegation chains but does not make chain position available to an agent.

> “A pre-execution Policy Enforcement Point (PEP/PDP) validates intent and arguments, enforces schemas and rate limits, issues short-lived credentials, and revokes or audits on drift.” — ASI02 guideline 4, printed p. 14 (PDF p. 15). [1]

This is a required-control-style recommendation with a named locus **outside the executing agent**: pre-execution policy middleware. It specifies neither chain lineage nor disclosure of any such context to the agent.

The strongest potentially confusing ASI01 wording is also insufficient:

> “At run time, validate both user intent and agent intent before executing goal-changing or high-impact actions.” — ASI01 guideline 4, printed p. 10 (PDF p. 11). [1]

“Agent intent” is not chain position. The immediately following sentence allows the validation to be supplied “via human approval, policy engine, or platform guardrails,” reinforcing that the text does not require a self-aware chain-location function in the executing agent.

## Clause-by-clause review

The quoted text below is exact decisive language from the guideline identified. **Locus** records the component the text expressly names or most directly addresses; “not fixed” means the source does not select an implementation boundary. A locus that could be implemented inside an agent is still negative where the guideline does not require an agent to receive or query chain position.

### ASI01 — Agent Goal Hijack

| Guideline and location | Exact decisive language | Control locus | Chain-position assessment |
|---|---|---|---|
| §1, printed p. 10 (PDF p. 11) | “Treat all natural-language inputs … as untrusted. Route them through the same input-validation and prompt-injection safeguards … before they can influence goal selection, planning, or tool calls.” | Input-validation / prompt-injection safeguard; not fixed to the agent. | **Negative.** It governs untrusted content and its influence, not predecessor, successor, depth, or membership data. |
| §2, printed p. 10 (PDF p. 11) | “Minimize the impact of goal hijacking by enforcing least privilege for agent tools and requiring human approval for high-impact or goal-changing actions.” | Tool authorization and human approval. | **Negative.** Authorization and approval do not make chain location observable by the agent. |
| §3, printed p. 10 (PDF p. 11) | “Define and lock agent system prompts so that goal priorities and permitted actions are explicit and auditable. Changes to changes in goals or reward definitions **must** go through configuration management and human approval.” | Prompt/configuration management and human approval. | **Negative.** This is the unit’s explicit MUST, and it mandates governance of goal/reward changes rather than agent-held execution-chain position. “Auditable” does not say the agent can query audit information. |
| §4, printed pp. 10–11 (PDF pp. 11–12) | “At run time, validate both user intent and agent intent before executing goal-changing or high-impact actions. Require confirmation - via human approval, policy engine, or platform guardrails … Pause or block execution on any unexpected goal shift, surface the deviation for review, and record it for audit.” | Runtime validator; expressly may be human approval, policy engine, or platform guardrails; audit record. | **Negative.** No requirement identifies where validation executes, and none supplies the executing agent with positional chain evidence. The listed human, policy, platform, and audit loci are external/observability controls. |
| §5, printed p. 10 (PDF p. 11) | “When building agents, evaluate use of ‘intent capsule’, an emerging pattern to bind the declared goal, constraints, and context to each execution cycle in a signed envelope, restricting run-time use.” | Agent-design/runtime envelope; optional (“evaluate use”). | **Negative.** A declared goal, constraints, and context may be supplied to a cycle, but the passage does not require predecessor/successor/depth/membership or equivalent position. The eventual location of the envelope is unspecified. |
| §6, printed p. 10 (PDF p. 11) | “Sanitize and validate any connected data source … before the data can influence agent goals or actions.” | Data ingestion/content filtering. | **Negative.** Data provenance and sanitization are not a requirement to expose execution-chain location to the agent. |
| §7, printed pp. 10–11 (PDF pp. 11–12) | “Maintain comprehensive logging and continuous monitoring of agent activity … Track a stable identifier for the active goal where feasible, and alert on any deviations … so that unauthorized goal drift is immediately visible in operations.” | Logging, continuous monitoring, operational alerting. | **Negative.** The active-goal identifier is not chain position, “where feasible” is conditional, and visibility is explicitly “in operations,” not inside the agent. This is the kind of observability the criterion excludes. |
| §8, printed p. 11 (PDF p. 12) | “Conduct periodic red-team tests simulating goal override and verify rollback effectiveness.” | Organization/test and rollback process. | **Negative.** Test evidence and rollback verification do not require agent-accessible lineage. |
| §9, printed p. 11 (PDF p. 12) | “Incorporate AI Agents into the established Insider Threat Program to monitor any insider prompts … and allow for investigation in case of outlier activity.” | Enterprise insider-threat monitoring/investigation. | **Negative.** An organizational monitoring program is not an in-agent chain-position interface. |

### ASI02 — Tool Misuse and Exploitation

| Guideline and location | Exact decisive language | Control locus | Chain-position assessment |
|---|---|---|---|
| §1, printed p. 13 (PDF p. 14) | “Define per-tool least-privilege profiles … and restrict agentic tool functionality and each tool’s permissions and data scope to those profiles … express these profiles as IAM or authorization policy stanzas attached to each tool.” | Tool authorization/IAM policy attached to the tool. | **Negative.** Per-tool scope and permissions do not describe the agent’s place in a multi-agent or delegation chain. |
| §2, printed p. 14 (PDF p. 15) | “Require explicit authentication for each tool invocation and human confirmation for high-impact or destructive actions … Display a pre-execution plan or dry-run diff before final approval.” | Authentication, human approval, and user-facing pre-execution review. | **Negative.** Invocation authentication and plan display do not make a predecessor, successor, depth, or membership queryable by the agent. |
| §3, printed p. 14 (PDF p. 15) | “Run tool or code execution in isolated sandboxes. Enforce outbound allowlists and deny all non-approved network destinations.” | Execution sandbox and network/egress control. | **Negative.** Isolation and egress restrictions do not convey execution-chain location to an agent. |
| §4, printed p. 14 (PDF p. 15) | “Treat LLM or planner outputs as untrusted. A pre-execution Policy Enforcement Point (PEP/PDP) validates intent and arguments, enforces schemas and rate limits, issues short-lived credentials, and revokes or audits on drift.” | Pre-execution PEP/PDP middleware. | **Negative.** This is explicitly an enforcement point before execution. It does not require that its information, much less chain position, be exposed inside the agent. |
| §5, printed p. 14 (PDF p. 15) | “Apply usage ceilings (cost, rate, or token budgets) with automatic revocation or throttling when exceeded.” | Usage/budget enforcement and revocation service. | **Negative.** Resource ceilings are not chain topology or position information. |
| §6, printed p. 14 (PDF p. 15) | “Grant temporary credentials or API tokens that expire immediately after use. Bind keys to specific user sessions to prevent lateral abuse.” | Credential/token and session management. | **Negative.** Binding a key to a user session is not binding the agent to a position in a larger execution chain. |
| §7, printed p. 14 (PDF p. 15) | “Enforce fully qualified tool names and version pins … validate the intended semantics of tool calls … Fail closed on ambiguous resolution and prompt for user disambiguation.” | Tool resolver/semantic firewall and user disambiguation. | **Negative.** Tool identity and resolution do not give the agent chain lineage. |
| §8, printed p. 14 (PDF p. 15) | “Maintain immutable logs of all tool invocations and parameter changes. Continuously monitor for anomalous execution rates, unusual tool-chaining patterns … and policy violations.” | Immutable logs and monitoring/analytics. | **Negative.** “Tool-chaining patterns” occurs only as a monitoring target. The text never requires those patterns or lineage to be available to the executing agent; this is expressly external observability under the test. |

## Non-normative material checked

The ASI01 and ASI02 descriptions and their “Common Examples of the Vulnerability” and “Example Attack Scenarios” mention autonomous series of tasks, multi-step behavior, unsafe delegation, chaining, tool chaining, and agent-to-agent messages. These passages explain risk or illustrate attacks. They do not impose controls. In particular:

> “Risks arise from how the agent chooses and applies tools; agent memory, dynamic tool selection, and delegation can contribute to misuse via chaining, privilege escalation, and unintended actions.” — ASI02 description, printed p. 12 (PDF p. 13). [1]

This identifies a causal risk mechanism, not a requirement to give an executing agent a representation of chain placement. Treating it as a requirement would confuse explanatory description with the numbered mitigation guidance.

## Control-locus synthesis

The unit distributes relevant controls across **input/content safeguards; tool IAM and authorization; human approval and user review; configuration governance; runtime policy engines/platform guardrails; execution sandboxes and egress controls; credentials/session services; tool-resolution controls; logging, monitoring, audit, and investigation**. The two express monitoring controls are system/operations-facing. The one expressly named enforcement component is a **pre-execution PEP/PDP**. No clause requires any of these components to disclose predecessor/successor/depth/membership information to the agent that executes the action.

## Uncertainty and limits

1. The unit does not define “agent execution boundary,” “chain position,” “delegation chain,” or the precise deployment locus of every guideline. Consequently, this record does not infer a vendor architecture from generic wording.
2. ASI01 §5 could be implemented so an intent capsule is consumed by an agent, and ASI01 §4 could be implemented with an in-agent validator. Neither possibility changes the result: the text requires no chain-position datum in either case.
3. “Track a stable identifier for the active goal where feasible” (ASI01 §7) and “unusual tool-chaining patterns” (ASI02 §8) may support external correlation. They remain negative because they are goal/tool activity identifiers and monitoring signals, not a requirement that the agent itself can inspect its larger-chain position.
4. The conclusion is limited to the cited 2026 v1.0 ASI01–ASI02 unit. It does not assess other OWASP documents, the linked reference materials, or implementation-specific controls.

## References

[1]: https://github.com/GenAI-Security-Project/GenAI-Security-Advisor/blob/613bf32a6f1d13eaf7b30040f7e9b779b23cfb7f/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf "OWASP Top 10 for Agentic Applications 2026, version 1.0"

[2]: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ "OWASP Top 10 for Agentic Applications for 2026"

# Audit Unit TOP10-03 — OWASP Top 10 for Agentic Applications 2026

## Determination

**Result: NEGATIVE.** The complete ASI05 and ASI06 entries contain **16 numbered Prevention and Mitigation Guidelines**. None requires an executing agent to receive, retain, or query evidence of its position in a larger execution chain, such as its predecessor, successor, depth, membership, or an equivalent chain-location attribute. Controls operate on generated code, execution environments, approvals, memory content, retrieval, data sources, tenancy, and observability. Some controls are deployed in or adjacent to the agent runtime, but that is not the required condition: the text does not make chain-position information available **to the agent itself**.

This record treats each numbered item under **“Prevention and Mitigation Guidelines”** as a normative clause for audit purposes. The publication calls them guidelines rather than using a uniform RFC-style *shall* formulation, but their operative wording is directive (for example, “Ban,” “Never,” “Require,” “Prevent,” and “Enforce”). The conclusion would not change under a narrower reading because no item—directive or otherwise—requires in-agent chain-position evidence.[1]

## Audit rule applied

A clause is **positive** only when it requires evidence of chain position to be available inside the executing agent. Qualifying evidence would identify or let the agent query its predecessor, successor, depth, membership, or an equivalent location in a broader execution chain. Lineage held only by a gateway, orchestrator, policy engine, memory system, logs, monitoring, or operators does not qualify. A runtime control located in an agent’s container also does not qualify unless it exposes that chain-location evidence to the agent.

## Source and review boundary

The reviewed authoritative artifact is the pinned **OWASP Top 10 for Agentic Applications 2026 v1.0** PDF at the supplied GitHub commit. Its printed pp. 21–23 contain ASI05 and its printed pp. 24–26 contain ASI06. The official OWASP resource page identifies the document as **“OWASP Top 10 for Agentic Applications for 2026,”** dated December 9, 2025.[1] [2]

The review includes every numbered guideline in both entries: ASI05 items 1–7 and ASI06 items 1–9. The descriptions, “Common Examples of the Vulnerability,” and “Example Attack Scenarios” were read as context, not counted as requirements. For example, ASI05 describes “orchestrated multi-tool chains” (printed p. 21), while ASI06 says inputs can include “peer-agent exchanges” (printed p. 24); neither sentence directs that an agent be given chain topology.[1]

## Clause-by-clause evidence

| No. | Exact decisive language and location | Control locus | Chain-position finding |
|---|---|---|---|
| ASI05-1 | “Follow the mitigations of LLM05:2025 Improper Output Handling with input validation and output encoding to sanitize agent-generated code” (ASI05, guideline 1, printed p. 22). | Application input/output and generated-code handling. | **Negative.** Sanitization concerns code content, not an executing agent’s location in a chain. |
| ASI05-2 | “Prevent direct agent-to-production systems and operationalize use of vibe coding systems with pre-production checks” (ASI05, guideline 2, printed p. 22). | Deployment architecture and pre-production assurance. | **Negative.** It restricts an agent-to-system connection; it supplies no predecessor, successor, depth, or membership evidence to the agent. |
| ASI05-3 | “Ban eval in production agents: Require safe interpreters, taint-tracking on generated code.” (ASI05, guideline 3, printed p. 22). | Agent runtime/code-execution environment. | **Negative.** This is a local runtime control. Taint data is about generated code, not execution-chain position, and is not specified as agent-queryable topology. |
| ASI05-4 | “Never run as root. Run code in sandboxed containers with strict limits including network access” and “restrict filesystem access to a dedicated working directory and log file diffs for critical paths.” (ASI05, guideline 4, printed pp. 22–23). | Host/container sandbox, filesystem control, and logging. | **Negative.** The clause constrains execution and creates logs; it neither requires chain metadata nor exposes it inside the agent. |
| ASI05-5 | “Isolate per-session environments with permission boundaries; apply least privilege; fail secure by default; separate code generation from execution with validation gates.” (ASI05, guideline 5, printed p. 23). | Session isolation, permissions, and generation/execution validation architecture. | **Negative.** Per-session isolation is not chain membership, and no chain-position field is required for the agent. |
| ASI05-6 | “Require human approval for elevated runs; keep an allowlist for auto-execution under version control; enforce role and action-based controls.” (ASI05, guideline 6, printed p. 23). | Human approval, version-control process, and access-control policy. | **Negative.** Approval and authorization are external decision controls, not in-agent evidence of chain position. |
| ASI05-7 | “Do static scans before execution; enable runtime monitoring; watch for prompt-injection patterns; log and audit all generation and runs.” (ASI05, guideline 7, printed p. 23). | Build/execution pipeline monitoring and audit logging. | **Negative.** Monitoring and logs may observe executions, but the clause does not require their chain information to be exposed to the executing agent. |
| ASI06-1 | “Baseline data protection: Encryption in transit and at rest combined with least-privilege access” (ASI06, guideline 1, printed p. 25). | Data transport/storage protection and access control. | **Negative.** The control protects data; it specifies no chain-location evidence. |
| ASI06-2 | “Scan all new memory writes and model outputs (rules + AI) for malicious or sensitive content before commit.” (ASI06, guideline 2, printed p. 25). | Memory-write/output commit gate. | **Negative.** The scan evaluates content before persistence, not who precedes/follows the executing agent. |
| ASI06-3 | “Isolate user sessions and domain contexts to prevent knowledge and sensitive data leakage.” (ASI06, guideline 3, printed p. 25). | Session/domain isolation and memory partitioning. | **Negative.** Separation of contexts is not a requirement for the agent to know its own chain position. |
| ASI06-4 | “Allow only authenticated, curated sources; enforce context-aware access per task; minimize retention by data sensitivity.” (ASI06, guideline 4, printed p. 25). | Source admission, task-scoped memory-access policy, and retention management. | **Negative.** “Context-aware access per task” is not defined as execution-chain context and does not require predecessor/successor/depth/membership information inside an agent. |
| ASI06-5 | “Require source attribution and detect suspicious updates or frequencies.” (ASI06, guideline 5, printed p. 25). | Memory provenance and anomaly detection. | **Negative.** Source attribution identifies origin of memory entries. The text does not require that attribution to identify chain position or be supplied to the executing agent. |
| ASI06-6 | “Prevent automatic re-ingestion of an agent’s own generated outputs into trusted memory” (ASI06, guideline 6, printed p. 26). | Memory-ingestion pipeline. | **Negative.** The agent’s relationship to its own output is not predecessor/successor/depth/membership in a larger execution chain. |
| ASI06-7 | “Perform adversarial test, use snapshots/rollback and version control, and require human review for high-risk actions.” Where shared stores operate, “use per-tenant namespaces and trust scores for entries” and support “rollback/quarantine for suspected poisoning.” (ASI06, guideline 7, printed p. 26). | Testing, versioning, human review, shared-memory tenancy, entry scoring, and recovery operations. | **Negative.** Trust scores and namespaces attach to memory entries or tenants, not to the executing agent’s chain location; human review remains external. |
| ASI06-8 | “Expire unverified memory to limit poison persistence.” (ASI06, guideline 8, printed p. 26). | Memory lifecycle/retention control. | **Negative.** Expiration is a storage rule with no chain-position information. |
| ASI06-9 | “Weight retrieval by trust and tenancy: Require two factors to surface high-impact memory (e.g., provenance score plus human-verified tag) and decay low-trust entries over time.” (ASI06, guideline 9, printed p. 26). | Memory retrieval/ranking and provenance/trust metadata. | **Negative.** The factors characterize retrieved memory. They do not identify the executing agent’s predecessor, successor, chain depth, or membership, and the clause does not make such a value queryable by the agent. |

## Control-locus synthesis

The unit assigns controls to five loci. **Generated-code and execution controls** constrain code, interpreters, containers, filesystems, and production access (ASI05-1 through ASI05-5). **Governance and authorization controls** place decisions with humans, allowlists, roles, or validation gates (ASI05-2, ASI05-5 through ASI05-6, and ASI06-7). **Observability controls** create scans, monitoring, logging, auditing, provenance, and anomaly detection (ASI05-7 and ASI06-2/5/9). **Memory and retrieval controls** govern writes, segmentation, sourcing, retention, expiration, tenant namespaces, and entry trust scores (ASI06-1 through ASI06-9). **Recovery controls** use snapshots, rollback, quarantine, and version control (ASI06-7).

No clause moves a control result from any of those loci into an executing agent as required chain-position evidence. In particular, audit logs in ASI05-4/7, source attribution in ASI06-5, and provenance scores in ASI06-9 could support external traceability of payloads or memory items, but the text does not require an agent to receive or query its location in the chain. They are therefore not positives under this work order’s criterion.

## Non-normative material kept separate

The following text is relevant context but does not alter the finding because it is descriptive or illustrative rather than a requirement:

> “This entry builds on LLM01:2025 Prompt Injection and LLM05:2025 Improper Output Handling, reflecting their evolution in agentic systems from a single manipulated output interpreted or executed to orchestrated multi-tool chains that achieve execution through a sequence of otherwise legitimate tool calls.” — ASI05 Description, printed p. 21.[1]

> “Ingestion sources such as uploads, API feeds, user input, or peer-agent exchanges may be untrusted or only partially validated.” — ASI06 Description, printed p. 24.[1]

The former recognizes a chain of tool calls; the latter recognizes peer-agent input. Neither imposes an in-agent interface for chain position. The common examples and attack scenarios likewise show possible attacks, not a required mechanism for self-location by the agent.

## Limitations and uncertainty

The document is an explanatory Top 10 guide, not a formal protocol or interface specification. It does not define an “executing agent boundary,” data schema, or a standard meaning for “context-aware” access. This audit therefore assesses the text actually required, rather than inferring an implementation. “Context-aware access per task” (ASI06-4) and source/provenance language (ASI06-5 and ASI06-9) could be implemented by an organization using workflow lineage, but the clauses do not say so and do not require that information to be available to the agent. That possible implementation is insufficient for a positive finding.

The count of 16 treats every numbered mitigation guideline as a clause. ASI06-1 is a terse baseline noun phrase, rather than a fully modal sentence; counting it is conservative and does not affect the negative conclusion. No inference is made about controls that a vendor might add beyond the published OWASP text.

## References

[1]: https://github.com/GenAI-Security-Project/GenAI-Security-Advisor/blob/613bf32a6f1d13eaf7b30040f7e9b779b23cfb7f/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf "OWASP Top 10 for Agentic Applications 2026 v1.0"

[2]: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ "OWASP Top 10 for Agentic Applications for 2026"

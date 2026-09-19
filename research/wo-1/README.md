# WO-1 execution record

**Status:** In progress
**Work order:** [WO-1 — Chain position detectability from inside a container](../../work-orders/WO-1-chain-position-detectability.md)

## Milestone 1 — standards audit

**Status:** Complete. See the [standards audit](standards-audit.md), [source inventory](source-inventory.md), and [clause-group evidence records](evidence/).

The first milestone audited the **OWASP Agent Control Standard** and the **OWASP Top 10 for Agentic Applications 2026** for any normative requirement that places chain-position information inside the executing agent.

The audit treats a requirement as positive only if the executing agent itself receives or can query evidence that identifies its position, predecessor, successor, depth, or membership in a larger execution chain. Gateway-side lineage, operator dashboards, audit logs, and post hoc observability do not satisfy the criterion unless the standard also requires that information to be exposed inside the agent’s execution boundary.

## Result

The audit covered **15 of 15 units** and reviewed **516 candidate clauses** under the stated counting rules. It found **0 positive, 15 negative, and 0 ambiguous units**, with no failed units. This is a null standards result: the reviewed requirements create substantial external lineage, policy, audit, provenance, and trace controls, but do not require that the executing agent receive or query enough information to determine its own position in a larger execution chain.

The result does not establish that chain-position awareness is impossible or absent from every implementation. It establishes only that the reviewed public requirements do not mandate it.

## Work-order progress

| Step | Deliverable | Status |
| ---: | --- | --- |
| 1 | Clause-level ACS and OWASP ASI 2026 standards audit | Complete |
| 2 | Auditable trust-assignment provenance specification | Next |
| 3 | Horn B container evidence experiment | Not started |
| 4 | Dissimilar-redundancy experiment across model families | Not started |

## Reproducibility rule

Every substantive claim in the audit must point to an authoritative source and a stable clause, section, or page location. Search-result snippets are not evidence. Ambiguous clauses are recorded as ambiguous rather than forced into a positive or negative classification.

# WO-1 execution record

**Status:** In progress
**Work order:** [WO-1 — Chain position detectability from inside a container](../../work-orders/WO-1-chain-position-detectability.md)

## Current milestone

The first milestone audits the **OWASP Agentic Security Initiative Agentic AI Control Standard** and the **OWASP Top 10 for Agentic Applications 2026** for any normative requirement that places chain-position information inside the executing agent.

The audit treats a requirement as positive only if the executing agent itself receives or can query evidence that identifies its position, predecessor, successor, depth, or membership in a larger execution chain. Gateway-side lineage, operator dashboards, audit logs, and post hoc observability do not satisfy the criterion unless the standard also requires that information to be exposed inside the agent’s execution boundary.

## Planned artifacts

1. A source inventory that records document versions and authoritative URLs.
2. A clause-level evidence table with quoted text, location, control locus, and criterion result.
3. A written finding that reports a positive or null result with explicit limitations.
4. Follow-on specifications for trust-assignment provenance, a Horn B evidence experiment, and a cross-model redundancy test.

## Reproducibility rule

Every substantive claim in the audit must point to an authoritative source and a stable clause, section, or page location. Search-result snippets are not evidence. Ambiguous clauses are recorded as ambiguous rather than forced into a positive or negative classification.

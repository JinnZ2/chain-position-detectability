# WO-2 execution record

**Status:** Milestone 1 complete; external blind replication remains open

**Work order:** [WO-2 — “Quiet” failure as a missing aggregation function](../../work-orders/WO-2-quiet-failure-missing-aggregation.md)

## Milestone 1 — bounded pilot corpus

The first milestone tested the four-part WO-2 decomposition against a reproducibly selected public accident-investigation corpus. It used eight U.S. Chemical Safety and Hazard Investigation Board final reports selected by a rule fixed before case coding. Each case was coded independently twice against the same codebook, reconciled, and then independently validated against the official report.

The pilot asks whether each case contains a pre-event signal, whether that signal was reported, how many distinct holders can be documented, whether a named function owned the cross-holder join, and how long the earliest documented signal preceded the event. It also records whether the official material describes the event or warning pattern as sudden, unexpected, unforeseen, or equivalent.

## Work-order progress

| Step | Deliverable | Status |
| ---: | --- | --- |
| 1 | Code an existing accident-investigation corpus | Pilot complete: 1 supports, 7 indeterminate, 0 does not support |
| 2 | Blindly test the decomposition on a sample selected independently of the claim | Partially addressed through independent double coding and validation; external blind selection remains open |
| 3 | Search for an honestly costed and declined aggregation function | Bounded search complete: null result; Army MFOQA records are the strongest follow-up lead |
| 4 | Search for a regulator that explicitly assigns the join to a named role with authority | Complete: FAA safety-management personnel and the EU QPPV are qualifying existence examples |

## Published outputs

The milestone publishes the [source manifest](source-manifest.md), [coding rules](codebook.md), two independent records per case under [`coding/`](coding/), independent case validations under [`validation/`](validation/), a [validated reconciliation log](reconciliation-log.md), a [machine-readable dataset](reconciled-dataset.csv), and the [final pilot analysis](pilot-analysis.md).

The first automated reconciliation is retained as [`initial-reconciliation-log.md`](initial-reconciliation-log.md), together with its [`initial-pilot-analysis.md`](initial-pilot-analysis.md). Those files are superseded and remain only to make the correction path auditable.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-2-quiet-failure-missing-aggregation.md "WO-2 — Quiet failure as a missing aggregation function"

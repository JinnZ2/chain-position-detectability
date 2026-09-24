# CLAUDE.md

Guidance for working in this repository. Public; CC0; nothing here is private.

## What this repository is

A **research program as work orders**: seven markers, each an instrument
spec with a measurand, a falsifier, scope limits and runnable next steps,
plus the execution records for the four that have been run in part. It is not a
code repository and not a thesis.

```text
work-orders/            seven markers, operator-authored; six verbatim, never edited; WO-11 a hash-pinned pointer
   |  WO-1  chain position detectable from inside a container?
   |  WO-2  "quiet" failure = a missing aggregation function?
   |  WO-3  does any TERMINAL system exist (zero crossings, every medium)?
   |  WO-4  one shape under WO-1..3: local correctness + an unowned join; the term gap
   |  WO-5  per-hop loss and pre-entry loss in reporting chains
   |  WO-6  assessor-assessed coupling as a known failure mode
   |  WO-11 benchmark score as an unpartitioned residual (research designs, not a build) -> POINTER to Simulators@4237ac2
   v
research/wo-N/          model-executed milestones (wo-1..3 Manus AI; wo-4 this session), one dir per run order
   |  wo-1  standards audit: 15 units, 516 clauses, 0 positive   NULL RESULT
   |  wo-2  8 CSB reports, double-coded, validated: 1 supports / 7 indeterminate / 0 against
   |  wo-3  3 asymptotes nonterminal-in-frame; 6 cost cases, 0 clear all five gates
   |  wo-4  invariant UNDETECTABLE <=> C1 and C3, checked; 7 faces = 3 assembly + 4 sensing; nothing coined
   v
AUDIT_NOTES.md          this tree audited: CPD_001..014, split MECHANICAL / READING
tools/check_repo.py     recomputes every number the tree states
research/wo-4/invariant.py  the one instrument that models rather than counts; finite, brute-force, selftested
```

Read `READING_PROTOCOL.md` and `AUDIT_CONTRACT.md` in the sibling
`Simulators` repository first. A work order is a marker for a sensed
shape: test the fit, extend it, or report where it breaks. Do not accept
or reject it.

## Hard constraints

```text
delivered files are verbatim     work-orders/WO-*, research/wo-1..3: never edit; findings go in AUDIT_NOTES.md.
                                 WO-11 holds no text: it pins Simulators@4237ac2 by path and sha256; cite the body hash
                                 work-orders/README.md is the index and moves with each milestone
ids are permanent                CPD_nnn never renumbered; a superseded claim keeps its id and gains a status
python >= 3.8, stdlib only       tools/ only; no runtime deps, no network, no build step
no author sections               no "about", working-style or audience prose anywhere (AUDIT_CONTRACT)
license: CC0                     everything, including research output
```

## Energy map

Where a claim enters, where it is held, where it is refused.

```text
operator observes a shape ----> work order: measurand, OBSERVED/DERIVED/PROPOSED tags,
                                falsifier, scope limits, "who could run this"
                                      |
                        run order (step N of the work order)
                                      |
             +------------------------+------------------------+
             v                        v                        v
   WO-1 standards audit      WO-2 corpus pilot          WO-3 metric + screen
   criterion FIRST           sample rule FIXED before   metric PREREGISTERED before
   15 units, 4 states        coding; 2 coders; then     cases; 5 gates, all required;
                             validation vs source       6 medium audits; 3 asymptotes
             |                        |                        |
       null result            1 / 7 / 0                 0 terminal, 0 qualifying
   (external lineage,      (join_assigned is the      (exact zero is model-conditional;
    nothing agent-side)     bottleneck: 7 unclear)      vector, never a scalar)
             |                        |                        |
             +------------------------+------------------------+
                                      v
                       work-orders/README.md status table   <-- the index; root README is NOT
```

Refusals that are deliberate, and where each is written down:

```text
missing evidence          -> unclear, never no              wo-2/codebook.md
one pathway per case      -> fragments from a second pathway cannot fill a field   (post hoc, stated)
join_assigned = no        -> needs AFFIRMATIVE absence, not a missing procedure
owner without view        -> OWNER_BLIND, never DETECTED         wo-4/invariant.py
assembly vs sensing       -> computed from the encoding, never declared by hand
non-detection             -> an upper bound, never Um = 0   wo-3/crossing-metric.md
crossings                 -> gross in + out, never netted
six media                 -> a profile, never one scalar    wo-3/amended-crossing-profile.md
cost categories           -> non-additive, no saving-to-loss ratio
contamination marker      -> UNKNOWN, resolved in neither direction
term gap (WO-4)           -> registered, NOT coined
```

## Status vocabularies (four; no file maps them -- CPD_010)

```text
work orders      OBSERVED / DERIVED / PROPOSED
wo-1             positive / negative / ambiguous / failed
wo-2             supports / does_not_support / indeterminate ; fields: yes / no / unclear
wo-3             OBSERVED / DERIVED / MODELLED-CONDITIONAL / PLANNED / UNRESOLVED
wo-4             JOIN_ENTAILED / DETECTED / OWNER_BLIND / UNDETECTABLE ; kind: assembly / sensing
```

Use the layer's own set. Do not translate one into another in a delivered
file; if a mapping is needed, it is a new table in `work-orders/README.md`.

## Layout

```text
README.md                     byte copy of WO-1 (CPD_001) -- not the index
work-orders/README.md         THE index: seven delivered, one of them a pointer; measurand, status
work-orders/WO-N-*.md         markers
research/wo-1/                standards-audit.md, source-inventory.md, evidence/audit-unit-NN.md (15)
research/wo-2/                codebook.md, source-manifest.md, coding/coder-{a,b}/, validation/,
                              reconciliation-log.md, reconciled-dataset.csv, pilot-analysis.md,
                              inverse-case-search.md, regulatory-join-role-search.md,
                              initial-*.md (superseded, kept as audit trail; never cite as result)
research/wo-3/                crossing-metric.md (preregistered), amended-crossing-profile.md,
                              evidence/, cost-candidates/, validation/, three CSVs,
                              validation-summary.md, workflow-synthesis.md, final-report.md
research/wo-4/                formal-statement.md, invariant.py (step 1); term census in the statement (step 3)
AUDIT_NOTES.md                CPD claims + what would move each open one
tools/check_repo.py           links, sums, dates, CSV-vs-prose, three-rendering agreement
```

## Provenance (CPD_011)

```text
work orders     operator's marker; no author line; tags carry the epistemic class
research        model-executed; "Author: Manus AI"; coders + validators were AI agents under one task design
this audit      same-class model output; MECHANICAL rows recomputable, READING rows declared
```

Audit the operator's claims on their own terms. Treat research prose as
overlay to be checked, never credited. Infer nothing about intent.

## Conventions when editing

- A new work order is `work-orders/WO-N-<slug>.md` plus a row in
  `work-orders/README.md`; a run gets `research/wo-N/README.md` with a
  step-status table mirroring the work order's "Runnable next steps".
- Superseded artifacts stay in the tree under `initial-*` and are named
  superseded where they sit. Nothing is deleted to make a result cleaner.
- A stated count anywhere in `research/` gets a row in
  `tools/check_repo.py` before it is cited elsewhere. A number nothing
  recomputes is a typed number.
- `FLAG` in the checker is a recorded finding that still stands. When a
  repair clears one, the selftest goes red on purpose: update the
  `--selftest` expectation and the CPD status in the same commit.
- Delivered em dashes and curly quotes stay; new authored text is ASCII.

## Commands

```sh
python3 tools/check_repo.py              # 10 checks; exit 0 = no FAIL (FLAGs allowed), 1 = FAIL, 3 = cannot run
python3 tools/check_repo.py --selftest   # plants defects in a copy, proves each check fires, then runs the real tree
python3 tools/check_repo.py --json       # machine-readable rows
python3 research/wo-4/invariant.py --selftest   # WO-4 step 1; prints its own check count
```

Nothing else runs. The three research milestones are
documents; reproducing them means re-reading the cited sources, which
this environment cannot reach (allowlist egress).

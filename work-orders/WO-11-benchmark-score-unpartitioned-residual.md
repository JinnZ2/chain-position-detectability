# WO-11 -- Benchmark score as an unpartitioned residual

STATUS: DELIVERED — CANONICAL TEXT IN Simulators@4237ac2 (pointer, not copy)

This file is a pinned pointer. It carries no copy of the work order, so
there is one text and one hash across the two repositories.

```
registered      2026-09-24 (this repository; slot 7ab162d, copy 2d688d4, pointer now)
delivered       2026-09-18, as one message with WO-12 and WO-13
canonical text  JinnZ2/Simulators @ 4237ac2
                publication-loop-work-orders/WORK_ORDER_11.md
landed          PR #85, merged 2026-09-20; 4237ac2 is in Simulators main
```

Hashes, sha256, verified 2026-09-24 against `git show 4237ac2:...`:

```
whole file      41fbd82eae022feb82061a6378f9747aaf82297c73b4b72854816d47bc34426d
body, line 12+  ada578e2b04f34407de1c4dc61f19df2c1d5f3c71cbddfe4e88fde456db9119d
```

The whole file opens with an eleven-line landing wrapper (its first line
is `# WORK ORDER 11 — delivered verbatim`); the delivered text begins at
line 12 with `# WORK ORDER 11 — Benchmark score as an unpartitioned
residual`. Pin the body hash when citing the marker, the whole-file hash
when citing the landing.

## Rendering variance, recorded

A second rendering of the same delivery reached this repository by paste
on 2026-09-23 and was landed at `2d688d4`. Against the canonical body it
differs in WHITESPACE ONLY: code-block column alignment in the T-2 and
T-4 blocks and one trailing blank line. No word differs.

```
chain      09-18 original ──paste #1──► Simulators, landed 09-19
           09-23 re-emit  ──paste #2──► this repository, landed 09-24
source     unresolved: the re-emit, or either of two manual phone pastes;
           neither rendering can be shown byte-verbatim to the original
canonical  first landed and hash-pinned, not "proven original"
```

Channel rule from here: a work order moves as an ATTACHMENT with its
hash sent alongside, and the receiver verifies before landing. Pastes
are for short instructions, where whitespace carries no meaning.

## What moves this file

```
Simulators moves the file   -> update the path here; the hashes stay
a run order is issued       -> research/wo-11/README.md with a step-status table
the original is recovered   -> compare both renderings to it; record which drifted
```

Audit record: `AUDIT_NOTES.md` CPD_016 and its dated amendment.

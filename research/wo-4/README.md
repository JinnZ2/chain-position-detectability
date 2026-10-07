# WO-4 execution record

**Status:** Step 1 delivered as a checkable module; step 3 bounded census (carried, unverified); steps 2 and 4 open

**Work order:** [WO-4 -- The shape: local correctness with an unowned join](../../work-orders/WO-4-the-shape-and-the-term-gap.md)

## Result

The invariant is stated as `UNDETECTABLE <=> C1 (local correctness does
not entail the join) and C3 (no node evaluates the join with a view that
covers it)`, with C2 (the join spans views) as the cost of closing C3.
Checked over five constructed controls that reach all four verdicts and
over the seven delivered faces, every one of which reaches UNDETECTABLE
under its encoding. The faces then split by repair: three are
**assembly** (a join over existing views detects the failure) and four are
**sensing** (the union of every view is still blind). A hand-declared split
in the first draft was refuted by the module's own selftest and is kept on
record.

The term census finds the two halves named separately and the
conjunction named nowhere among eleven candidates: `named in parts`, not
`named_elsewhere`. Nothing is coined.

## Work-order progress

| Step | Deliverable | Status |
| ---: | --- | --- |
| 1 | Formal statement of the invariant | Delivered: [`formal-statement.md`](formal-statement.md), [`invariant.py`](invariant.py) |
| 2 | Adversarial face-finding by an outside party | Not run: needs a party outside this author line |
| 3 | Cross-language term search | Bounded census from model memory, 11 terms, carried and unverified |
| 4 | Coin or adopt | Not started, per the work order's gate on 1 or 3 |

## Commands

```sh
python3 research/wo-4/invariant.py             # controls, faces, the aggregator repair
python3 research/wo-4/invariant.py --selftest  # prints its own check count
python3 tools/check_repo.py                    # row wo4_invariant cross-checks this folder's stated counts
```

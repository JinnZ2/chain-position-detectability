# WO-4 step 1 -- formal statement of the invariant; step 3 -- bounded term census

**Status:** step 1 delivered as a checkable module; step 3 bounded and carried; steps 2 and 4 open.
**Instrument:** [`invariant.py`](invariant.py). Every number in this file is recomputed by
`python3 tools/check_repo.py` (row `wo4_invariant`); the module prints its own check count.
**Provenance:** model-written, same party encoded the faces and wrote the checker. Every face row
is a READING of one encoding, printed with the encoding so it can be disagreed with variable by variable.

## 1. Statement

```text
S = (N, V, view, c, J, owner)

N        finite node set                    V        finite variable set, finite domains
view(i)  the variables node i can read      c_i      node i's check, over view(i) only
J        the join, a predicate over V       owner    the node that evaluates J, or none
L = AND_i c_i                               "every node is locally correct"

C1  ENTAILMENT FAILS   exists s :  L(s) and not J(s)
C2  JOIN SPANS VIEWS   J is not a function of any single view(i)
C3  JOIN UNOWNED       no node evaluates J with a view covering var(J)

UNDETECTABLE  <=>  C1 and C3            (checked over every instance in the module)
```

C2 is not part of the biconditional. It says what closing C3 costs: when J
spans views, no existing node can be *assigned* J, so the owner has to be
*constructed*. The four verdicts are kept apart because they call for four
different repairs:

```text
JOIN_ENTAILED   L entails J          nothing to detect; local correctness is enough
DETECTED        owner reads var(J)   the join is owned and sighted
OWNER_BLIND     owner lacks a var    responsibility without access   <- WO-1 Horn B, WO-2's "authority", WO-5's proxy
UNDETECTABLE    C1 and C3            the shape
```

## 2. What the statement gives back to the faces it came from

WO-1's two horns fall out of the verdict table rather than being argued:
Horn B (the container asks itself) is `OWNER_BLIND` by construction, since
the container's view is its own task; Horn A (awareness from outside)
constructs an owner with a wide view, which is `DETECTED` in S and
reopens C3 in the larger S' the owner sits in. WO-2's codebook rule that
`join_assigned = yes` needs responsibility *and* authority is the
`DETECTED` / `OWNER_BLIND` distinction stated as a coding rule.

## 3. Faces run through the encoding

```text
controls  5     verdicts reached: UNDETECTABLE, DETECTED, OWNER_BLIND, JOIN_ENTAILED (all four)
faces     7     every face reaches UNDETECTABLE under its encoding
```

| face | join variables | read by | kind | aggregator over all views |
|---|---|---|---|---|
| F1 container/chain (WO-1) | t1 t2 t3 | each by one node | assembly | DETECTED |
| F2 regulation -> exclusion | r1 r2 r3 | each by one node | assembly | DETECTED |
| F3 quiet failure (WO-2) | s1 s2 | each by one node | assembly | DETECTED |
| F4 terminal system (WO-3) | k1 k2 x | x by nobody | sensing | OWNER_BLIND |
| F5 air gap | net usb person | usb, person by nobody | sensing | OWNER_BLIND |
| F6 the frog | other | by nobody | sensing | OWNER_BLIND |
| F7 description / referent | coupled | by nobody | sensing | OWNER_BLIND |

```text
assembly 3   every variable J reads sits in some view; a join over EXISTING views detects the failure
sensing  4   some variable J reads sits in no view; the union of every view is still blind;
             a new sensor is needed before any join
```

That split is the result of step 1 beyond the statement itself: the seven
faces are one shape at the level of C1 and C3 and **two shapes at the level
of the repair**. WO-2's decomposition ("no one is assigned the JOIN") names
the assembly kind exactly. WO-3's boundary, the air gap, the frog and the
decoupled description are the sensing kind: assigning the join to anyone
who exists changes nothing, because the variable the join needs is not
being read.

**A refuted first draft, kept.** The first encoding declared the split by
hand (`state` vs `frame`) and asserted that every "frame" face had its
join variables outside every view. The selftest refuted it on F4: the
accountant reads two of the three. The computed split replaces it; the
hand-assigned one is retained in the module as `FIRST_DRAFT_KINDS` with a
check that it stays refuted (its frame set is a strict subset of the
sensing set, and it filed the air gap on the wrong side).

## 4. Step 3 -- cross-language term census, bounded, carried

Egress is an allowlist, so this is a census from model memory of terms
the model already holds, scored against C1/C2/C3. It is UNVERIFIED as a
literature claim and bounded to eleven candidates. WO-4 said to expect
`named_elsewhere`.

| term | field | names C1 | names C2 | names C3 | both C1 and C3 |
|---|---|---|---|---|---|
| fallacy of composition | logic | yes | no | no | no |
| emergence | systems | yes | partly | no | no |
| Swiss cheese model (Reason) | safety | yes (pictured) | no | no | no |
| normal accidents (Perrow) | sociology of safety | no | yes | no | no |
| problem of many hands (Thompson) | political theory | no | no | yes (after the fact) | no |
| diffusion of responsibility / Verantwortungsdiffusion | social psychology | no | no | yes (with a mechanism) | no |
| organized irresponsibility / organisierte Unverantwortlichkeit (Beck) | sociology | no | no | yes (institutional) | no |
| tatewari gyosei (vertically sliced administration) | Japanese public administration | no | no | yes (structure) | no |
| Schnittstellenproblem / Zustaendigkeitsluecke | German administration | no | no | yes (the gap) | no |
| "nobody's job" / "falls between the cracks" | English idiom | no | no | yes | no |
| common-mode failure / shared node | reliability engineering | no | no | no | no (WO-6's shape, not this one) |

```text
terms 11   name C1 only 3   name C2 only 1   name C3 only 6   name neither 1   name C1 AND C3 0
```

The expected status refines: not `named_elsewhere` but **named in
parts**. The entailment failure has names; the unowned join has names;
the conjunction has none found, and none of the C3 terms carries the
assembly / sensing distinction. That is now the precise statement of the
term gap. Whether the conjunction needs a word or composes from two is a
question the statement raises and does not settle.

## 5. Steps 2 and 4 -- not run, and why

Step 2 (adversarial face-finding) requires someone in an unrelated domain
handed the seven faces. This audit is the same party that encoded them and
cannot supply the eighth face; a candidate from the sibling ecosystem
(the shared node behind nominal redundancy, `effective-redundancy-audit`)
is noted and not counted, since it comes from the same author line and
scores on WO-6 rather than here.

Step 4 (coin or adopt) is gated on 1 or 3 by the work order. Step 1 is
delivered and step 3 is carried; nothing is coined here, per the work
order's own NOT COINED HERE.

## 6. Scope

- The biconditional is checked on finite constructed instances, not proved
  in general. The instances have at most four variables; the state space
  is enumerated.
- The faces are encodings. A different encoding of the same face can land
  in the other kind; the encoding is printed so that disagreement has a
  variable to point at.
- Substrate independence (WO-4's scope limit) is not addressed: seven
  encodings by one hand regenerate nothing.

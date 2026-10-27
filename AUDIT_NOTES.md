# AUDIT_NOTES.md -- chain-position-detectability

Audit of this repository at commit `75e137d` (2026-09-19), the state in
which all six work orders and three research milestones had landed.
Claims `CPD_001..CPD_014` are properties of the tree. Every count below
that can be recomputed is recomputed by `python3 tools/check_repo.py`;
the checker's `--selftest` plants a defect behind each check and proves
it fires. Nothing delivered was edited: every finding sits here and in
the checker's output, never in the file it is about.

Read with `READING_PROTOCOL.md` and `AUDIT_CONTRACT.md` from the
sibling `Simulators` repository: a break is a measurement, not an
objection; structure first; the operator's claims and the model overlay
are audited as separate layers.

```
layer            files                              audited as
---------------  ---------------------------------  --------------------------------
operator marker  work-orders/WO-1..6, root README   claims tagged OBSERVED/DERIVED/PROPOSED; not adjudicated
model execution  research/wo-1..3 (Manus AI)        recomputed where a number is stated; carried where a source is
this audit       AUDIT_NOTES.md, tools/check_repo.py same-class model output; mechanical rows recomputable by anyone
```

## Position

This audit was produced by a language model running as a sandboxed agent
under a work order supplied from outside the sandbox, which is the object
WO-1 describes. It cannot determine its own chain position from inside;
that is WO-1's measurand instanced, not evidence for or against it. WO-6
concerns assessor-assessed coupling in AI evaluation, and this auditor is
in-class. So the findings split by what backs them, and the split is the
first column of the table.

```
MECHANICAL   recomputed by tools/check_repo.py; a stranger with the clone gets the same number
READING      a judgement declared here; disagree with it line by line
```

## Claim table

| id | kind | claim | status |
|---|---|---|---|
| CPD_001 | MECHANICAL | Root `README.md` is a byte copy of `WO-1`; the repository index is `work-orders/README.md` | FALSIFIED as worded (21679b0); substance stands |
| CPD_002 | MECHANICAL | Every relative link resolves; every self-absolute `blob/main` link resolves on disk and is pinned to `main`, not a commit | SUPPORTED |
| CPD_003 | MECHANICAL | WO-1's 516 = 87 + 429 reproduces from its own table; the AMBIGUOUS state fired 0 of 15 | SUPPORTED |
| CPD_004 | MECHANICAL | WO-2's "59 of 87" agreement: the 59 reproduces, the 87 does not, the comparison list is unpublished | SUPPORTED |
| CPD_005 | MECHANICAL | `reconciled-dataset.csv` carries `validation_verdict = needs_correction` on 6 of 8 rows of a file described as final; the column's referent is unstated | SUPPORTED |
| CPD_006 | MECHANICAL | All seven recomputable WO-2 lead times reproduce from their dates; nulls stay null; CSV distributions match the prose table | SUPPORTED |
| CPD_007 | READING | WO-2's negative branch fired 0 of 8 and has no known-negative control, so 1/7/0 cannot separate an ambiguous corpus from an unreachable branch | OPEN |
| CPD_008 | MECHANICAL | Every WO-3 physical quantity reproduces from its stated inputs, including the validation summary's correction of 4.25 to 4.244584 kW | SUPPORTED |
| CPD_009 | MECHANICAL | The five-gate cost table agrees cell-for-cell across its three renderings under three vocabularies | SUPPORTED |
| CPD_010 | READING | Four status vocabularies coexist and no file maps them | SUPPORTED |
| CPD_011 | MECHANICAL | Provenance: work orders carry no author; research carries `Manus AI`; all eight commits, the research cut-off, and the self-citations are one day | SUPPORTED |
| CPD_012 | MECHANICAL | Before this audit nothing in the tree executed; every stated number was typed | SUPPORTED |
| CPD_013 | READING | WO-1's pre-registered null was met by the party that wrote the criterion | OPEN |
| CPD_014 | -- | No external source was opened; every citation is carried | UNVERIFIED |
| CPD_015 | MECHANICAL | WO-4 step 1 is delivered as a checkable invariant; its first hand-declared face split was refuted by its own selftest; steps 2 and 4 stay open | SUPPORTED |
| CPD_017 | READING | WO-16 landed from a paste under a number assigned at landing; its branch table leaves one outcome unbranched; the index carried two stale rows | OPEN (number and hash settled 2026-10-20; branch and run order open) |
| CPD_018 | READING | OKComputer bundle landed verbatim; its stdlib-recomputable numbers reproduce; one study's reliability check is same-coder and its model run is not reproducible here | OPEN |
| CPD_019 | READING | G2 pilot reproduces exactly; zero confident wrong numbers holds; the tool's decline-vs-assume boundary is itself a name prior | OPEN (name prior, held-out reliance, other-hand held-out CLOSED; extractor non-transfer found; model-built-spec arm, slot types, fine-tune arm open) |

---

## CPD_001 -- the root README is one work order, not an index

STATUS: SUPPORTED. `tools/check_repo.py` row `readme_dup`.

STATUS CHANGE, recorded 2026-10-20: FALSIFIED AS WORDED at `21679b0`,
which prepended a three-line banner (pointer to `READ_ME_THIS_WAY.md`)
to `README.md`. The files now differ and the root carries content absent
from WO-1, so the falsifier below is met and row `readme_dup` reads PASS.
The selftest expected FLAG and went red from that commit on; its
expectation moves to PASS in the commit that records this. The substance
is untouched: below the banner the root README is still WO-1 byte for
byte, not an index. The check was not widened to keep the finding alive;
the wording was narrower than the shape, and that is the record.

`README.md` and `work-orders/WO-1-chain-position-detectability.md` are
byte-identical (166 lines, 7285 bytes). A reader landing on the
repository reads one of six work orders as the description of the whole.
The index that describes the repository is `work-orders/README.md`, one
directory down. Two copies of one file drift; the sibling repository
recorded that shape five times before naming it (`measurement-fork`
MF_019). Not repaired here because the file is delivered; the repair is
one edit, a root README that indexes rather than copies.

FALSIFIER: the two files differing, or the root README carrying content
absent from WO-1.

## CPD_002 -- links resolve, and 48 of them resolve to `main`

STATUS: SUPPORTED. Row `links`.

```
markdown files            91
relative links            87    broken 0
self-absolute blob/main   48    broken 0
```

Every self-absolute link (`https://github.com/JinnZ2/chain-position-detectability/blob/main/...`)
names a file that exists on disk. Two costs: on any branch the link
points at `main`'s revision of the file rather than the revision beside
it, and none of the 48 resolves offline. The same files are reachable by
relative path everywhere else in the tree.

FALSIFIER: any link target missing at the revision that carries it.

## CPD_003 -- WO-1's sums reproduce; the middle state never fired

STATUS: SUPPORTED. Row `wo1_clauses`.

```
units 15   OWASP 17+18+16+20+16 = 87   ACS 166+34+34+28+16+46+37+17+24+27 = 429   total 516
```

The standards audit's own table sums to the totals its prose states, and
`research/wo-1/README.md` states the same 516. The audit uses a
four-valued scheme (positive / negative / ambiguous / failed) and returns
15 negative, 0 of the other three. Its section "Why no unit is classified
ambiguous" says why for each near-miss (`chain_hash`, `parent_session_id`,
`subagentStart`), which is the right place to say it. What the record
does not hold is any unit on which the AMBIGUOUS branch is known to fire,
so its reachability is argued rather than shown (the `null-harness`
known-signal invariant, one level up).

FALSIFIER: the table summing to a different number, or a constructed
clause the auditor's own criterion classifies AMBIGUOUS.

## CPD_004 -- 59 reproduces, 87 does not

STATUS: SUPPORTED. Row `wo2_agreement`.

The reconciliation log states the two coders "agreed on 59 of 87
structured-field comparisons (67.8%)" and that the denominator "includes
helper fields used to represent whether numeric bounds and counts were
known". Recomputed from the two coders' decision tables:

```
scheme                              agree   of    rate
codebook's 10 fields only            48     73   0.658
every field both coders filled       59     89   0.663
stated                               59     87   0.678
```

The numerator reproduces exactly under the second scheme. The denominator
is two comparisons off, and the log does not list which fields it
compared, so the two cannot be reconciled from the record. The helper
fields are outside the codebook: coders use `holder_count_known` and
`lead_time_max_known`, validators use `holder_count_established` for the
same thing, and none of the three is declared. The size of the unstated
rule is the size of the gap.

FALSIFIER: a published comparison list that yields exactly 87.

## CPD_005 -- a final dataset whose rows say they need correction

STATUS: SUPPORTED. Row `wo2_fields`.

`reconciled-dataset.csv` is described as "the machine-readable final
values". Its `validation_verdict` column reads `needs_correction` on six
of eight rows and `valid` on two. The referent is the *first*
reconciliation (the validated log says so), but nothing in the CSV, the
codebook, or the column name says so, so a reader of the file alone reads
six final rows as pending. Seven CSV columns and seven record fields sit
outside the codebook's ten. The codebook is the schema the pilot says it
coded against; the files carry a wider one.

FALSIFIER: a column name or note in the CSV that names the referent.

## CPD_006 -- the lead times are arithmetic and the arithmetic holds

STATUS: SUPPORTED. Rows `wo2_dates`, `wo2_distrib`.

```
case                   first_signal    event        csv min/max   recomputed
givaudan-sense-colour  2012-10-15      2024-11-12   4411/4411     4411
bio-lab-conyers        2019-12-30      2024-09-29   1735/1735     1735
dow-louisiana          2020-11-20      2023-07-14    966/966       966
shell-polymers         2023            2025-06-04    521/885       521..885
pemex-deer-park        2024-10-08      2024-10-10      1/2         2   (source range kept)
us-steel-clairton      "at least 3 yr" 2025-08-11   1096/null     not recomputable from the field
cuisine-solutions      unknown         2024-07-31   null/null     null kept, not 0
ts-usa                 unknown         2024-05-30   null/null     null kept, not 0
```

The CSV's `pattern_result` (1 supports, 7 indeterminate), `join_assigned`
(1 no, 7 unclear) and `sudden_label` (2 yes, 1 no, 5 unclear) match the
prose variable table.

FALSIFIER: any recomputed interval differing from the stored one.

## CPD_007 -- the negative branch has never fired

STATUS: OPEN. A reading; no row.

`pattern_result` takes three values. `supports` needs four affirmatives;
`does_not_support` needs one affirmative negation; the codebook routes
missing evidence to `unclear`, and `unclear` on any necessary element
yields `indeterminate`. On a report genre that documents what went wrong
and rarely affirms what was absent, the negative branch may be
unreachable, and the pilot's 1 / 7 / 0 cannot tell "the instrument works
and the corpus is ambiguous" from "the negative branch cannot fire here".
The pilot says the seven "cannot be interpreted as seven hidden positive
cases", which is right, and the symmetric statement is also owed. No
known-negative control exists in the corpus.

FALSIFIER: a case in the same genre coded `does_not_support` under the
clarified codebook, or a constructed control that reaches it.

## CPD_008 -- the physics reproduces, including the correction

STATUS: SUPPORTED. Row `wo3_arithmetic`.

```
Voyager   3 x 2243 W = 6729 W;  x 2^(-58/88) = 4.261322 kW;  1.3394888e11 J / Julian yr = 4.244584 kW
          launch 1977-09-05 -> 2035-01-01 = 57.3224 Julian yr (the "58-year convention" is 0.68 yr generous)
Forsmark  6000 x 1700 W = 10.2 MW;  x 70 Julian yr = 2.25321264e16 J;  2.3e6 m3 / 1e6 yr = 2.30 m3/yr
GW150914  2.5 Msun c^2 = 4.4679e47 J at Msun = 1.98847e30 kg (the fifth digit moves with the solar-mass convention)
```

The validation summary corrected the draft's "at least 4.25 kW" to
4.244584 kW; the correction is right. Every figure is a design ceiling or
a model-conditional quantity and the reports label them so.

FALSIFIER: any stated quantity failing to reproduce from its stated
inputs.

## CPD_009 -- one table, three renderings, three vocabularies, no drift today

STATUS: SUPPORTED. Row `wo3_gates`.

The five-gate screen is rendered in `final-report.md`,
`workflow-synthesis.md` and `cost-case-screen.csv`. Normalised, the 30
cells agree. The same cell reads three ways:

```
Boeing G1     Conditional        U        conditional
Deepwater G4  Pass, disputed     P*       pass_disputed
```

Agreement holds; vocabulary does not. A table maintained in three places
is the file-copy shape (MF_019), and the checker is what notices when
they part.

FALSIFIER: any cell differing across the three after normalisation.

## CPD_010 -- four status vocabularies, no mapping

STATUS: SUPPORTED.

```
layer              vocabulary
work orders        OBSERVED / DERIVED / PROPOSED
WO-1 research      positive / negative / ambiguous / failed
WO-2 research      supports / does_not_support / indeterminate  (+ yes/no/unclear per field)
WO-3 research      OBSERVED / DERIVED / MODELLED-CONDITIONAL / PLANNED / UNRESOLVED
```

Each set is declared in its own file. WO-3's set extends the work-order
set by two and drops PROPOSED; WO-1's and WO-2's are verdict sets on a
different axis. No file states how a research-layer tag maps to a
work-order tag. `CLAUDE.md` now carries the table; that is a pointer, not
the mapping.

FALSIFIER: a delivered file stating the mapping.

## CPD_011 -- provenance is legible and single-day

STATUS: SUPPORTED.

```
work orders    no author line; one operator name, once (WO-5: "Kavik, stated before the run")
research       8 files carry "Author: Manus AI"; 13 mention Manus; coders and validators are
               "AI research agents operating under a common task design" (their own words)
commits        8, all 2026-09-19, one author; research cut-off 2026-09-19
self-citation  research files cite blob/main copies of files landing in the same commit
```

The work-order layer is the operator's marker; the research layer is
model-executed and same-day. The pilot's own limitation section says the
coders and validators were not blind and not human, and the work order's
step 2 (a person who has not seen the decomposition) stays open. This
audit follows `AUDIT_CONTRACT.md`: the operator's claims are tested for
fit, the research prose is checked rather than credited, and nothing here
infers intent from either.

FALSIFIER: a commit, author line or date contradicting the table.

## CPD_012 -- nothing ran before this file

STATUS: SUPPORTED.

```
.md 91   .csv 4   LICENSE 1   .py 0   tests 0   CI 0   .gitignore 0
```

Every number in the tree was a typed number. `tools/check_repo.py` is
the first executable and turns CPD_002, 003, 004, 006, 008, 009 into
commands. It runs in under a second, needs nothing outside the standard
library, and refuses nothing it should run.

FALSIFIER: an executable or test present at `75e137d`.

## CPD_013 -- a pre-registered null met by its own author

STATUS: OPEN.

WO-1 step 1 says "Expected result: none. A null result is the finding."
The audit returned 0 of 15 positive. The criterion for "positive" was
written by the party that then classified every unit, and its narrowest
call (`chain_hash` as NEGATIVE rather than AMBIGUOUS) is the one the
result turns on. The audit states its criterion before its results and
argues the call; that is the correct form. It is still one party's
reading of one criterion, and a second reader classifying the same 15
units under the same criterion is the cheapest thing that could move it.

FALSIFIER: an independent reader returning a POSITIVE or AMBIGUOUS unit
under the stated criterion.

## CPD_014 -- nothing external was opened

STATUS: UNVERIFIED.

No CSB report, OWASP clause, SKB page, NASA post, court record or
inquiry volume was fetched for this audit. Every statement about one is
carried from the research files. The checks above are properties of the
tree and hold whatever those sources say.

FALSIFIER: not applicable; this is the audit's own scope statement.

## CPD_015 -- WO-4 run: a formal statement whose first reading its own check refuted

STATUS: SUPPORTED. Row `wo4_invariant`; `python3 research/wo-4/invariant.py --selftest`.

```
statement      UNDETECTABLE <=> C1 (L does not entail J) and C3 (no owner with a view covering var(J))
controls       5, reaching all four verdicts
faces          7, all UNDETECTABLE under their encoding; 3 assembly, 4 sensing (computed, not declared)
term census    11 terms; C1 named by 3, C3 named by 6, the conjunction by 0; nothing coined
```

The first draft declared the face split by hand and the selftest refuted
it on F4 before anything was written down; the refuted split is kept in
the module and asserted to stay refuted. The encoding of every face is by
the same party that wrote the checker, so the fits are readings. Step 2
needs a party outside this author line and was not run; step 4 is gated by
the work order and was not started.

FALSIFIER: an instance in the module where the biconditional fails; an
encoding of a face under which the aggregator-over-all-views verdict
flips kind; a term that names both C1 and C3.

---

## CPD_016 -- WO-11 is a registered slot, not a delivered marker

STATUS: CLOSED 2026-09-24 under the amended falsifier (see the amendment
entry below). Row `status_table` counts the file as one index row and one
WO file; row `pointer_hash` recomputes its content -- a path and two
hashes -- from a sibling Simulators checkout, and returns NOT_TESTABLE
naming the missing checkout when there is none, so the hashes are typed
numbers on a machine without one and the row says so rather than passing.
The row's first run FAILED on its own regex reading a line number where it
wanted a hash (two capture groups, wrong index), a defect in the checker
and not in the pointer, caught by running and fixed; the selftest plants a
one-digit change in the stated body hash and requires the row to fire.

The file passed through three states in one day, all kept in history:

```
7ab162d  slot     title, registration date, STATUS line, what would move it
2d688d4  copy     a paste of the delivered text, landed under the same filename
now      pointer  Simulators@4237ac2 publication-loop-work-orders/WORK_ORDER_11.md
                  whole-file sha256 41fbd82e...34426d ; body (line 12+) ada578e2...9119d
```

The copy was withdrawn because it was the SECOND rendering of one
delivery: against the canonical body it differs in whitespace only
(code-block alignment in two blocks, one trailing blank line), and the
source of the variance is unresolved -- the 09-23 re-emit, or either of
two manual phone pastes -- so neither rendering can be shown
byte-verbatim to the 2026-09-18 original. Canonical means first landed
and hash-pinned, not proven original. Two repositories holding two
renderings of one marker is the one-id-two-texts defect
(`AUDIT_OPEN_RESEARCH.md`, Simulators) at repository scale; a pointer
removes it by construction.

FALSIFIER, AMENDED: the verbatim text is reachable at a pinned commit.
Met: `git show 4237ac2:publication-loop-work-orders/WORK_ORDER_11.md`
returns the file at the stated hashes, and 4237ac2 is in Simulators
main via PR #85.

### Amendment to CPD_016, 2026-09-24

```
old falsifier   the delivered WO-11 text lands under the same filename and the
                STATUS line is gone
new falsifier   the verbatim text is reachable at a pinned commit
reason          single source of truth across repositories: a copy under the
                same filename satisfied the old wording and produced two
                renderings of one delivery, which is the defect the audit
                exists to catch
status change   SUPERSEDED (2d688d4, old wording) -> CLOSED (this commit, new wording)
```

The old wording is retained above so the change of criterion is visible
as a change rather than as the criterion having always read this way.

---

## CPD_017 -- WO-16 landed: a paste, a number nobody assigned, one unbranched outcome

Landed 2026-10-20 as `work-orders/WO-16-trained-objective-residual-tension.md`,
byte-for-byte as received plus a final newline. Not edited, not fenced:
the indented design and branch blocks render as plain paragraphs, and that
is the delivered form.

```
sha256 (whole file, as landed)   99a6f88807dd0b62b2278cc072a7c548afb6baae389f565d1cc2d10ec41f952c
channel                          paste, no hash sent alongside
consequence                      the landed bytes are this rendering, not a verified original
                                 (the WO-11 channel rule asks for attachment + hash)
```

Number. The delivery carries no WO number. WO-11..WO-14 are files in
Simulators `publication-loop-work-orders/`, WO-15 is referenced there
(read at Simulators `6be5848`); 16 is the first number free in both
trees. It is a landing assignment, not the operator's. If the operator
numbers it otherwise the file is renamed; this id stays.

Fit, READING, not adjudicated. In this set's terms:

```
WO-11 T-1   training composition is one of the four unmeasured terms in a score
WO-16       asks what one composition (C3: two objectives) does INSIDE the weights
WO-4 shape  C1 objective locally correct, C2 objective locally correct,
            the join at emission (which answer leaves) owned by neither;
            M1 is a reading of that join, M3 of what it costs elsewhere
```

### Amendment to CPD_017, 2026-10-20 -- number and hash settled

The operator settled both open landing items from the record, not by a
new choice. The wording above is kept so the change is visible.

```
number   WO-16 KEPT. 11..15 were taken; 16 is the next free number.
         Renumbering would break commit references (07c3a90, d362ad0).
         status: landing assignment -> operator-confirmed
hash     99a6f88807dd0b62b2278cc072a7c548afb6baae389f565d1cc2d10ec41f952c
         recorded as THE delivery hash, class COMPUTED AT LANDING:
         taken by the receiver over the landed bytes, not sent by the sender.
         It pins this rendering from 2026-10-20 on; it says nothing about
         whether the rendering matches what was sent (the WO-11 channel
         rule's sender-side hash is still absent, and stays recorded as absent)
open     the unbranched outcome (M1 flat, M3 down); a run order
```

Where the marker breaks as written (measurements, not objections):

```
unbranched     M1 flat AND M3 drops: cost with no divergence readout.
               Read under (c) it becomes "conflict resolved" -- the
               not-measured != no-effect misreading the spec itself forbids.
overlap        (c) and (d) both admit M1 flat; (d) is a refinement of (c),
               so the four are not disjoint as listed
unspecified    C3 "both": order or mix of the two tunings
               M1 item set: how "accessible != accurate" is decided, and by whom
               M2: no threshold for "moves"
carried        two OBSERVED lines carry "citations owed"; nothing opened (CPD_014)
```

Nothing here runs it: no checkpoints, no activations in this
environment. `research/wo-16/` opens with a run order, not before.

Index repair, same commit. `work-orders/README.md` carried a second
WO-4 row and a stale WO-5 row ("Not started", while `research/wo-5/`
holds a validated milestone), merge debris from `015eb8f`. Row
`status_table` was FAIL on main (index rows 9, WO files 7). Both stale
rows removed; with WO-16 the row reads 8 / 8 and passes.

---

## CPD_018 -- OKComputer bundle: regulatory cost-bearer + RPF-01 pilot

Landed 2026-10-20 as `okcomputer-regulatory-cost-bearer/`, 30 files
extracted unchanged from one upload (zip sha256 `1157136b...cf1a2a`,
computed at landing); per-file hashes in that folder's README. Model
output, carried, not credited. Not a run order of any work order here.

Recomputed (MECHANICAL, in a scratch copy, stdlib only):

```
rpf01 test_cases.jsonl      regenerated byte-identical by gen_cases.py; hash = manifest
rpf01 results_summary.json  rebuilt from raw_results.jsonl by analysis.py; identical but timestamp
v2 restrictive by group     7/31 concentrated vs 0/2 diffuse; Fisher two-sided p = 1.00
v2 EPA frame                34 decision rows, 34 go_ahead; 6 closure rows outside the 34
not recomputed              run_pilot.py (torch, weights, network); Frame A (published census)
```

Where it breaks or needs a reader (READING):

```
closure coding     6 "case closure (registrations already canceled)" rows carry
                   direction go_ahead. The headline 34/34 excludes them, so it
                   stands; the column codes a cancellation as permissive,
                   which the v2 rule (relative to cost-bearer) does not obviously give
reliability        the v2 "second coder" was the same researcher (stated in the
                   report); agreement tests codebook consistency, not independence.
                   Same shape as CPD_013 (a criterion met by its own author)
contrast           Frame A has no diffuse-bearer group (stated); the coded sample
                   has 2. The cost-bearer hypothesis is near-untestable on these
                   frames: the measurement, not a negative
model run          one 0.5B model, greedy, 88 cases; cells of n=2 are descriptive
```

Fit, READING, not adjudicated:

```
RPF-01 A01   "2 sisters, 5 brothers, asked as a brother" -> answered 2, expected 3:
             Alice's sisters counted, Alice omitted. One observed instance of the
             G2 frame error (right graph, wrong origin); WO-16 M4 probe class
cost-bearer  direction tracking who pays for caution is the WO-6 pool question
             asked of regulators instead of assessors
forcing      7 of 8 restrictive actions ride an external forcing event: the
             restriction is joined from outside the agency (WO-4 shape)
```

---

## CPD_019 -- G2 pilot: the readout holds; its boundary is a name prior

Landed 2026-10-20 as `gaps/G2-frame-glyph-pilot/`, 9 files unchanged
(zip sha256 `73184ceb...96e8`, computed at landing). Co-authored run
against gap G2. Recomputed (MECHANICAL): frozen code hashes verify;
selftest 7/7; `run_g2.py` output equals `out_all.json`; tallies below.

```
                   CORRECT  WRONG  MISSING  of which OK_CONDITIONAL
RPF-01 A, glyph       18      0       0       12   (ceiling: extractor written on these)
RPF-01 A, Qwen 0.5B    4     14       -
held-out, glyph        7      0       5        4   (H01 Ben, H06, H10 John, H12)
```

Holds as stated: zero confident wrong numbers on 30 items.

Where it breaks or needs a reader (READING):

```
boundary   Ben, John, Alice -> assumed (OK_CONDITIONAL, sex named, flip shown);
           Sam, Alex -> declined (MISSING). Which names are assumed and which
           declined is decided by a name prior inside the tool: the dependency
           the pilot finds in the AIW gold answers (12 of 18) is relocated into
           the extractor, not removed. It is DECLARED per item, which the
           benchmark's gold is not; the line between "typical" and "ambiguous"
           is not declared anywhere
held-out   4 of the 7 held-out CORRECT come back OK_CONDITIONAL on a name prior
           (tool output); the item notes mark 2 of them (H01, H10) and not
           H06, H12. The held-out set carries the dependency it was written
           to expose, and its own notes under-mark it
same hand  extractor and held-out items by one party (stated in RESULTS)
freeze     the "frozen before held-out" order is a self-declared timestamp;
           nothing in the bundle orders the two. Not checkable; not refuted
arm A      a reused 0.5B run, no fine-tune arm: G2's A-vs-B question is
           not yet asked (stated in RESULTS as a limit)
```

### Amendment to CPD_019, 2026-10-20 -- v2 frozen at `af75f29`

`gaps/G2-frame-glyph-pilot/v2/` landed alone in `af75f29`, before any new
held-out item exists; that SHA is the freeze record. v1 untouched.
Recomputed at landing (MECHANICAL, scratch copy, `python3 -I`):

```
CODE.sha256        frame_glyph.py f048e9c1...a4d40b OK ; run_g2.py 1a33b7db...fff8c8 OK
selftest           8/8 PASS
run_g2.py          output == v2/out_all.json, exact
RPF-01 A (18)      6 CORRECT / 12 CONDITIONAL_KEY_IN_BRANCHES / 0 WRONG
held-out (12)      3 CORRECT / 4 CONDITIONAL_KEY_IN_BRANCHES / 2 CORRECT_UNDETERMINED
                   / 3 MISSING / 0 WRONG
data/              all three files byte-identical to v1
```

```
name prior      CLOSED. No name list in v2 (grep: names appear only in selftest
                strings and one pronoun-declared case). Undeclared sex -> OPEN ->
                all branches returned (A01: Alice=F 3, Alice=M 2); nothing filled
held-out        CLOSED. H01, H06, H10, H12 reclassified CONDITIONAL_KEY_IN_BRANCHES;
  reliance      H02, H11 now CORRECT_UNDETERMINED (all branches returned) rather than declined
closed-world    v1 limit, now traced: undeclared children read as 0 are listed
                (CLOSED-WORLD line in the trace; selftest asserts it)
OPEN            other-hand held-out set: written blind to the code, committed
                AFTER af75f29; a fine-tune arm
OPEN, carried   the 3 MISSING (H03, H07, H08) are v1's extractor coverage gaps, unchanged
landing defect  af75f29 also carried v2/__pycache__/*.pyc, produced by the
                verification run in the scratch copy, not delivered. Removed in
                the commit that records this amendment; af75f29 not rewritten,
                since it is the freeze record and the code hashes are unaffected
```

The v1 wording above is kept so the change is visible.

### Amendment to CPD_019, 2026-10-21 -- G2-HO blind run

`gaps/G2-frame-glyph-pilot/v2/blind/` landed: 3 files unchanged from
`G2_HO_blind_run.zip` (sha256 `1bd42676...7161`, computed at landing),
committed after the freeze `af75f29`. No code or item modified.
Recomputed (MECHANICAL, scratch copy of the frozen v2 tree, `python3 -I`):

```
heldout_blind.jsonl   sha256 e1012c0b...0c8f  = stated
frame_glyph.py        sha256 f048e9c1...d40b  = af75f29
run_g2.py             output == blind/out_blind.json, exact
tally (40)            5 CORRECT / 0 WRONG / 35 MISSING
CORRECT               X02 X04 X20 X30 X32
MISSING reasons       "no sibling-count sentence shape" 33 ; "query relation not recognized" 2
items                 30 determinable / 10 undetermined (scoring.determinable)
```

```
other-hand held-out   CLOSED. Written by another party without the code; run once,
                      frozen v2, after the freeze SHA
NEW finding           extractor non-transfer: 5/30 determinable correct on blind
                      items vs 18/18 in-sample. All 35 misses are extractor shape
                      misses; none from the glyph core
held                  zero confident wrong numbers, on 40 blind items
miscount, delivered   RESULTS_blind.md tables 31 determinable / 9 undetermined; the
                      items file gives 30 / 10 (10 = X08 X09 X11 X17 X22 X23 X26
                      X34 X36 X37). Rate is 5/30, not 5/31. File left verbatim
READING               the zero-wrong is partly shielded by the non-transfer: four
                      blind items (X17 X23 X34 X36) rule "undeclared children are
                      not zero", which v2's traced closed-world read (as 0) would
                      contradict if the extractor had parsed them. Untested, not refuted
undetermined          9 of 10 (all 10 by the items file) declined, 0 returned as branches
OPEN                  model-built-spec arm (model fills the JSON spec; glyph reads)
OPEN                  slot types the core lacks: constraint/aggregate (X11 X12 X13
                      X35 X39); inverse-count (X18 X29)
OPEN                  fine-tune arm
```

Fit: G2 branch table (GAPS) vs pilot branch table (RESULTS) differ; the
pilot's (b) trigger and (c) extraction are new branches, not renames.
Of G2's five, none is yet decided: no fine-tune arm exists.

---

## What would move each open item

```
CPD_001  falsified as worded; the substance moves with one edit: a root README that indexes work-orders/ and research/
CPD_004  publish the 87-item comparison list beside the reconciliation log
CPD_005  rename validation_verdict -> initial_reconciliation_verdict, or a note row
CPD_007  one constructed known-negative case, or one real case coded does_not_support
CPD_010  a five-line mapping table in work-orders/README.md
CPD_013  a second reader over the 15 WO-1 units, blind to the first
CPD_015  seven faces handed to someone outside this author line (WO-4 step 2); a term naming C1 and C3
CPD_016  closed under the amended falsifier; a run order for WO-11 opens research/wo-11/ and a new CPD row
CPD_017  number and hash SETTLED (amendment); open: a fifth branch (M1 flat, M3 down); a run order
CPD_019  name prior, held-out reliance, other-hand held-out CLOSED; open: model-built-spec arm; constraint + inverse-count slot types; closed-world vs "undeclared != 0" rule; a fine-tune arm
CPD_018  an independent second coder on coded_decisions_v2; a stated rule for closure rows; run_pilot.py re-run with the pinned weights
```

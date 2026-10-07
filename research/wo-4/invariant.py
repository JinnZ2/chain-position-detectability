#!/usr/bin/env python3
"""invariant.py -- WO-4 step 1: a formal statement of the shape, made checkable.

WO-4 asks for "minimum conditions under which local correctness plus an
unowned join produces undetectable failure. If it can be stated formally,
it can be checked." This module is the statement and the check.

    S = (N, V, view, c, J, owner)

    N        finite set of nodes
    V        finite set of variables, each with a finite domain
    view(i)  the subset of V node i can read            (its local view)
    c_i      node i's local check, a predicate over view(i) only
    J        the join: a predicate over V                 (the composite)
    owner    which node evaluates J, or None              (unowned)

    L  =  AND_i c_i          "every node is locally correct"

Conditions:

    C1  ENTAILMENT FAILS    some state satisfies L and not J
    C2  JOIN SPANS VIEWS    J is not a function of any single view(i)
    C3  JOIN UNOWNED        no node evaluates J with a view covering var(J)

Claim (checked below on constructed instances, every branch reachable):

    UNDETECTABLE  <=>  C1 and C3
    C2 is what makes C3 expensive to close: when J spans views, closing C3
    means CONSTRUCTING a node with a wider view, not assigning J to one
    that exists.

Verdicts, kept apart:

    JOIN_ENTAILED   no state has L and not J; local correctness suffices
    DETECTED        a witness state exists; an owner with view >= var(J) reads it
    OWNER_BLIND     an owner is named, its view lacks a variable J reads;
                    responsibility without access (WO-2's "responsibility AND
                    authority"; WO-1 Horn B)
    UNDETECTABLE    a witness state exists and nobody evaluates J

Brute force over the state space; instances here have <= 6 boolean
variables. Stdlib only, parses under 3.8, no network.

    python3 research/wo-4/invariant.py             render the face table
    python3 research/wo-4/invariant.py --selftest  controls + faces, count printed
    python3 research/wo-4/invariant.py --json
"""
from __future__ import annotations

import itertools
import json
import sys
from typing import Callable, Dict, List, Optional, Sequence, Tuple

State = Dict[str, int]
Pred = Callable[[State], bool]


class Instance:
    def __init__(self, name: str, variables: Sequence[str], views: Dict[str, Sequence[str]],
                 checks: Dict[str, Pred], join: Pred, join_vars: Sequence[str],
                 owner: Optional[str], owner_view: Optional[Sequence[str]] = None,
                 note: str = "") -> None:
        self.name = name
        self.variables = list(variables)
        self.views = {k: tuple(v) for k, v in views.items()}
        self.checks = checks
        self.join = join
        self.join_vars = tuple(join_vars)
        self.owner = owner
        self.owner_view = tuple(owner_view) if owner_view is not None else (
            self.views.get(owner, ()) if owner else ())
        self.note = note
        for i, vs in self.views.items():
            for v in vs:
                assert v in self.variables, (name, i, v)
        for v in self.join_vars:
            assert v in self.variables, (name, "join", v)

    def states(self) -> List[State]:
        return [dict(zip(self.variables, bits)) for bits in itertools.product((0, 1), repeat=len(self.variables))]

    def analyze(self) -> Dict[str, object]:
        witnesses = []
        for s in self.states():
            local_ok = all(self.checks[i]({v: s[v] for v in self.views[i]}) for i in self.views)
            if local_ok and not self.join(s):
                witnesses.append(s)
        c1 = bool(witnesses)
        # C2: is J a function of any single view? Test each view for determination.
        single = []
        for i, vs in self.views.items():
            table: Dict[Tuple[int, ...], set] = {}
            for s in self.states():
                table.setdefault(tuple(s[v] for v in vs), set()).add(self.join(s))
            if all(len(x) == 1 for x in table.values()):
                single.append(i)
        c2 = not single
        owner_covers = self.owner is not None and set(self.join_vars) <= set(self.owner_view)
        c3 = self.owner is None
        if not c1:
            verdict = "JOIN_ENTAILED"
        elif self.owner is None:
            verdict = "UNDETECTABLE"
        elif owner_covers:
            verdict = "DETECTED"
        else:
            verdict = "OWNER_BLIND"
        return {
            "name": self.name, "nodes": len(self.views), "variables": len(self.variables),
            "C1_entailment_fails": c1, "C2_join_spans_views": c2,
            "C3_join_unowned": c3, "owner": self.owner, "owner_covers_join": owner_covers,
            "witness_states": len(witnesses), "verdict": verdict, "note": self.note,
            "kind": kind_of(self)[0], "join_vars_unread": kind_of(self)[1],
        }


def _all(vs: Sequence[str]) -> Pred:
    return lambda s: all(s[v] for v in vs)


def _true(_: State) -> bool:
    return True


# ------------------------------------------------------------- controls ---
# Constructed. Each exists to reach one verdict, so the checker is shown to
# separate before any face is read through it.

def controls() -> List[Instance]:
    out = []
    # Positive control: three locally benign steps; the composite forms a chain nobody reads.
    out.append(Instance("ctl-undetectable", ["a", "b", "c"],
                        {"n1": ["a"], "n2": ["b"], "n3": ["c"]},
                        {"n1": _true, "n2": _true, "n3": _true},
                        lambda s: not (s["a"] and s["b"] and s["c"]), ["a", "b", "c"], None,
                        note="C1 and C3 hold -> UNDETECTABLE"))
    # Same instance with an owner whose view covers the join.
    out.append(Instance("ctl-detected", ["a", "b", "c"],
                        {"n1": ["a"], "n2": ["b"], "n3": ["c"], "gate": ["a", "b", "c"]},
                        {"n1": _true, "n2": _true, "n3": _true, "gate": _true},
                        lambda s: not (s["a"] and s["b"] and s["c"]), ["a", "b", "c"], "gate",
                        note="owner with full view -> DETECTED"))
    # Owner named but its view lacks a join variable.
    out.append(Instance("ctl-owner-blind", ["a", "b", "c"],
                        {"n1": ["a"], "n2": ["b"], "n3": ["c"]},
                        {"n1": _true, "n2": _true, "n3": _true},
                        lambda s: not (s["a"] and s["b"] and s["c"]), ["a", "b", "c"], "n1",
                        note="owner = n1, view {a} -> OWNER_BLIND"))
    # Negative control: local checks entail the join; no failure state exists.
    out.append(Instance("ctl-entailed", ["a", "b"],
                        {"n1": ["a"], "n2": ["b"]},
                        {"n1": lambda s: s["a"] == 1, "n2": lambda s: s["b"] == 1},
                        lambda s: bool(s["a"] and s["b"]), ["a", "b"], None,
                        note="L entails J -> JOIN_ENTAILED (unowned, and nothing to detect)"))
    # C2 false: one node's view already determines J; C3 is closable by assignment.
    out.append(Instance("ctl-single-view", ["a", "b"],
                        {"n1": ["a", "b"], "n2": ["b"]},
                        {"n1": _true, "n2": _true},
                        lambda s: not (s["a"] and s["b"]), ["a", "b"], None,
                        note="C2 fails: n1 sees var(J); ownership is an assignment, not a construction"))
    return out


# ---------------------------------------------------------------- faces ---
# READINGS. Each face is encoded by the same party that wrote the checker, so
# a verdict here is a property of the encoding. The encoding is printed with
# the verdict so it can be disagreed with variable by variable.

def faces() -> List[Instance]:
    out = []
    # Face 1 / WO-1: containers, each task locally valid; the chain is the join.
    out.append(Instance("F1 container/chain (WO-1)", ["t1", "t2", "t3"],
                        {"c1": ["t1"], "c2": ["t2"], "c3": ["t3"]},
                        {"c1": _true, "c2": _true, "c3": _true},
                        lambda s: not (s["t1"] and s["t2"] and s["t3"]), ["t1", "t2", "t3"], None,
                        note="t_i = my output feeds the next step; chain forms iff all three; no step reads the others"))
    # Face 2: rules each valid; exclusion emerges from their conjunction.
    out.append(Instance("F2 regulation -> exclusion", ["r1", "r2", "r3"],
                        {"a1": ["r1"], "a2": ["r2"], "a3": ["r3"]},
                        {"a1": _true, "a2": _true, "a3": _true},
                        lambda s: not (s["r1"] and s["r2"] and s["r3"]), ["r1", "r2", "r3"], None,
                        note="r_i = rule i excludes class X on its own axis; total exclusion iff all three; no author reads the others"))
    # Face 3 / WO-2: holders each reported; the risk read requires the fragments joined.
    out.append(Instance("F3 quiet failure (WO-2)", ["s1", "s2"],
                        {"h1": ["s1"], "h2": ["s2"]},
                        {"h1": _true, "h2": _true},
                        lambda s: not (s["s1"] and s["s2"]), ["s1", "s2"], None,
                        note="s_i = holder i holds and has reported a fragment; the hazard is live iff both; nobody reads both (join_assigned = no)"))
    # Face 4 / WO-3: cost items inside the boundary accounted; crossings outside it are the join.
    out.append(Instance("F4 terminal system (WO-3)", ["k1", "k2", "x"],
                        {"acct": ["k1", "k2"]},
                        {"acct": lambda s: bool(s["k1"] and s["k2"])},
                        lambda s: bool(s["k1"] and s["k2"] and not s["x"]), ["k1", "k2", "x"], None,
                        note="k_i = in-boundary item accounted; x = a crossing outside the boundary; the accountant's view excludes x by construction"))
    # Face 5: air gap; one channel checked, the join is over all channels.
    out.append(Instance("F5 air gap", ["net", "usb", "person"],
                        {"itsec": ["net"]},
                        {"itsec": lambda s: s["net"] == 0},
                        lambda s: not (s["net"] or s["usb"] or s["person"]), ["net", "usb", "person"], None,
                        note="the local check reads one channel; J is over every channel; nobody reads the others"))
    # Face 6: the frog; two options each valid; the join is frame completeness.
    out.append(Instance("F6 the frog (frame)", ["optA", "optB", "other"],
                        {"chooser": ["optA", "optB"]},
                        {"chooser": lambda s: bool(s["optA"] or s["optB"])},
                        lambda s: not s["other"], ["other"], None,
                        note="STRETCH: the join is 'the presented set is complete', a frame fact; var(J) is outside every view"))
    # Face 7: description decoupled from referent; procedure, mandate, law each valid; coupling to the referent is the join.
    out.append(Instance("F7 description/referent (frame)", ["proc", "mand", "law", "coupled"],
                        {"p": ["proc"], "m": ["mand"], "l": ["law"]},
                        {"p": _true, "m": _true, "l": _true},
                        lambda s: bool(s["coupled"]), ["coupled"], None,
                        note="STRETCH: J = the description still couples to its referent; a frame fact with a time index; no node re-reads it"))
    return out


EXPECTED = {
    "ctl-undetectable": "UNDETECTABLE", "ctl-detected": "DETECTED",
    "ctl-owner-blind": "OWNER_BLIND", "ctl-entailed": "JOIN_ENTAILED", "ctl-single-view": "UNDETECTABLE",
}

# A first draft declared a hand-assigned split (state-join vs frame-join) and asserted that
# every "frame" face had var(J) entirely outside every view. The selftest refuted it on F4:
# the accountant reads two of the three join variables. The split that survives is COMPUTED:
#
#   ASSEMBLY  every variable J reads is in some node's view      -> an aggregator over existing
#             views detects the failure; the repair is a join node
#   SENSING   some variable J reads is in no view at all         -> the union of every view is
#             still blind; the repair needs a new sensor before any join
#
# The hand-assigned kinds are kept here as the refuted prediction, not used by any check.
FIRST_DRAFT_KINDS = {"F1": "state", "F2": "state", "F3": "state", "F4": "frame", "F5": "state", "F6": "frame", "F7": "frame"}


def kind_of(inst: Instance) -> Tuple[str, List[str]]:
    seen = set()
    for vs in inst.views.values():
        seen |= set(vs)
    unread = [v for v in inst.join_vars if v not in seen]
    return ("sensing" if unread else "assembly"), unread


def aggregator_over_all_views(inst: Instance) -> Dict[str, object]:
    """Close C3 by constructing one node whose view is the union of every existing view."""
    union = sorted({v for vs in inst.views.values() for v in vs})
    views = dict(inst.views, aggregator=union)
    checks = dict(inst.checks, aggregator=_true)
    return Instance(inst.name, inst.variables, views, checks, inst.join, inst.join_vars, "aggregator").analyze()


def render(rows: List[Dict[str, object]]) -> str:
    out = ["%-34s %-13s C1 C2 C3  wit  owner  kind      unread" % ("instance", "verdict")]
    for r in rows:
        out.append("%-34s %-13s %s  %s  %s  %3d  %-6s %-9s %s" % (
            r["name"], r["verdict"], "y" if r["C1_entailment_fails"] else "n",
            "y" if r["C2_join_spans_views"] else "n", "y" if r["C3_join_unowned"] else "n",
            r["witness_states"], r["owner"] or "-", r["kind"], ",".join(r["join_vars_unread"]) or "-"))
    return "\n".join(out)


def selftest() -> int:
    n = 0
    ctl = {i.name: i.analyze() for i in controls()}
    for name, want in EXPECTED.items():
        assert ctl[name]["verdict"] == want, (name, ctl[name]["verdict"]); n += 1
    assert set(EXPECTED.values()) == {"UNDETECTABLE", "DETECTED", "OWNER_BLIND", "JOIN_ENTAILED"}; n += 1
    assert ctl["ctl-single-view"]["C2_join_spans_views"] is False; n += 1
    assert ctl["ctl-undetectable"]["C2_join_spans_views"] is True; n += 1
    # Claim: UNDETECTABLE <=> C1 and C3, over every instance in the file.
    for r in list(ctl.values()) + [f.analyze() for f in faces()]:
        assert (r["verdict"] == "UNDETECTABLE") == (r["C1_entailment_fails"] and r["C3_join_unowned"]), r["name"]; n += 1
    # Every face, as encoded, reaches UNDETECTABLE.
    fr = {f.name: f for f in faces()}
    kinds = {}
    for name, inst in fr.items():
        r = inst.analyze()
        assert r["verdict"] == "UNDETECTABLE", (name, r["verdict"]); n += 1
        kinds[name.split()[0]] = r["kind"]
    assert kinds == {"F1": "assembly", "F2": "assembly", "F3": "assembly",
                     "F4": "sensing", "F5": "sensing", "F6": "sensing", "F7": "sensing"}, kinds; n += 1
    # The refuted first draft: its "frame" set is a strict subset of the computed sensing set,
    # and its "state" set wrongly contains F5. Kept as a record, asserted so it cannot be quietly retuned.
    frame = {k for k, v in FIRST_DRAFT_KINDS.items() if v == "frame"}
    sensing = {k for k, v in kinds.items() if v == "sensing"}
    assert frame < sensing and "F5" in sensing - frame; n += 1
    # The repair that separates the kinds: an aggregator over every existing view detects the
    # assembly faces and is still blind on the sensing faces.
    for name, inst in fr.items():
        want = "DETECTED" if kinds[name.split()[0]] == "assembly" else "OWNER_BLIND"
        assert aggregator_over_all_views(inst)["verdict"] == want, (name, want); n += 1
    # Closing C3 on a face by assignment works only where some view already covers var(J).
    f1 = fr["F1 container/chain (WO-1)"]
    for node in f1.views:
        assert Instance(f1.name, f1.variables, f1.views, f1.checks, f1.join, f1.join_vars, node).analyze()["verdict"] == "OWNER_BLIND"; n += 1
    assert Instance(f1.name, f1.variables, dict(f1.views, gate=["t1", "t2", "t3"]), dict(f1.checks, gate=_true),
                    f1.join, f1.join_vars, "gate").analyze()["verdict"] == "DETECTED"; n += 1
    print("selftest: %d checks PASS" % n)
    return 0


def main(argv: List[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    rows = [i.analyze() for i in controls()] + [f.analyze() for f in faces()]
    if "--json" in argv:
        print(json.dumps(rows, indent=1))
        return 0
    print("WO-4 invariant -- controls then faces. Face rows are READINGS of one encoding.\n")
    print(render(rows))
    print("\naggregator over the union of all views:")
    for f in faces():
        print("  %-34s -> %s" % (f.name, aggregator_over_all_views(f)["verdict"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

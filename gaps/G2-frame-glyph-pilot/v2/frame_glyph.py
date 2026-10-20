"""frame_glyph.py v2 -- CC0. stdlib only. co-authored. Status: PROPOSED (pilot).

v2 (closes CPD_019 name-prior finding): no name list. A sex not declared by
pronoun or kin word is OPEN. If it is load-bearing, every branch is read and
returned (status CONDITIONAL); nothing is filled from a prior. Closed-world
reads (undeclared children read as 0) are now traced as CLOSED-WORLD.

Frame-explicit relational readout as a callable tool. No weights touched.

    LABEL FRAME -> PLACE NODES -> EXPAND TREE -> READ PARTITION -> READ FROM QUERIED NODE

Design rules (from the 2026-10-20 thread):
  * Edges are stored ONCE (parent -> child). Every relation is a traversal, so a
    relation can be walked from either end (BOM explosion / where-used). No
    reversal gap by construction.
  * Every attribute is DECLARED (stated in the text), ASSUMED (filled from a
    prior, e.g. name -> sex) and listed in the trace, or OPEN.
  * OPEN only blocks a readout if it sits on the READ PATH (load-bearing).
    Off-path unknowns (cousins' parents, Tom's children's sex) are ignored.
  * If an ASSUMED slot is load-bearing, the readout is returned with the
    assumption named and the alternative readout beside it. The cut is visible.
  * Anything the extractor cannot place returns MISSING. MISSING is a result.

API
  glyph(spec)            -> readout dict (structured in, structured out)
  extract(text)          -> spec dict or {"status": "MISSING", ...}
  solve(text)            -> extract + glyph
"""
import re

# ---------------------------------------------------------------- core graph

def _parents(g, x):
    return [p for p, c in g["edges"] if c == x]

def _children(g, x):
    return [c for p, c in g["edges"] if p == x]

def _siblings(g, x):
    out = []
    for p in _parents(g, x):
        for c in _children(g, p):
            if c != x and c not in out:
                out.append(c)
    return out

STEPS = {"parent": _parents, "child": _children, "sibling": _siblings}


def _closed_world(g, start, path):
    """nodes whose children are read on the path but none were declared"""
    frontier, flagged = [start], []
    for step, filt in path:
        if step == "child":
            flagged += [n for n in frontier if not _children(g, n) and n != "P"]
        nxt = []
        for n in frontier:
            for m in STEPS[step](g, n):
                fits = all(_attr(g, m, k)[0] in (v, None) for k, v in filt.items())
                if fits and m not in nxt:   # keep nodes that pass OR are undeclared
                    nxt.append(m)
        frontier = nxt
    return sorted(set(flagged))


def _attr(g, n, key):
    """returns (value, provenance) ; provenance in DECLARED/ASSUMED/OPEN"""
    a = g["nodes"].get(n, {}).get(key)
    if a is None:
        return None, "OPEN"
    return a  # stored as (value, provenance)


def _walk(g, start, path, sex_override=None):
    """path = [(step, {"sex": "F"} or {}), ...]. Returns (set, load_bearing list)."""
    frontier, used = [start], []
    for step, filt in path:
        nxt = []
        for n in frontier:
            for m in STEPS[step](g, n):
                ok = True
                for k, want in filt.items():
                    if sex_override and m in sex_override and k == "sex":
                        val, prov = sex_override[m], "OVERRIDE"
                    else:
                        val, prov = _attr(g, m, k)
                    used.append((m, k, prov))
                    if val != want:
                        ok = False
                if ok and m not in nxt:
                    nxt.append(m)
        frontier = nxt
    return frontier, used


def glyph(spec):
    g, q = spec, spec["query"]
    frame = q["from"]
    trace = [f"FRAME: reading from {frame} ({g['nodes'][frame].get('label', frame)})",
             f"NODES: {len(g['nodes'])} placed, EDGES: {len(g['edges'])} (stored once)"]
    for n, a in g["nodes"].items():
        s = a.get("sex")
        if s and s[1] == "ASSUMED":
            trace.append(f"ASSUMED: {n}.sex={s[0]} (source: {a.get('assume_src', 'prior')})")
    hits, used = _walk(g, frame, q["path"])
    open_sex = sorted({m for m, k, p in used if p == "OPEN" and k == "sex"})
    open_other = sorted({f"{m}.{k}" for m, k, p in used if p == "OPEN" and k != "sex"})
    assumed_on_path = sorted({m for m, k, p in used if p == "ASSUMED"})
    trace.append("PATH: " + " -> ".join(f"{s}{f or ''}" for s, f in q["path"]))
    closed = _closed_world(g, frame, q["path"])
    if closed:
        trace.append(f"CLOSED-WORLD: no children declared for {closed}; read as 0")
    if open_other or len(open_sex) > 3:
        trace.append(f"OPEN ON READ PATH: {open_other or open_sex}")
        return {"status": "MISSING", "frame": frame, "missing": open_other or open_sex, "trace": trace}
    if open_sex:
        # v2: undeclared sex is never filled. Read every branch; report all.
        import itertools
        branches = {}
        for combo in itertools.product("FM", repeat=len(open_sex)):
            ov = dict(zip(open_sex, combo))
            r, _ = _walk(g, frame, q["path"], sex_override=ov)
            branches[",".join(f"{m}={v}" for m, v in ov.items())] = len(r)
        if len(set(branches.values())) == 1:
            n = next(iter(branches.values()))
            trace.append(f"undeclared {open_sex} not load-bearing; every branch reads {n}")
            out = {"status": "OK", "frame": frame, "count": n, "trace": trace}
        else:
            trace.append(f"UNDECLARED, LOAD-BEARING: {open_sex}; branches {branches}")
            out = {"status": "CONDITIONAL", "frame": frame, "branches": branches,
                   "undeclared": open_sex, "trace": trace}
        if closed:
            out["closed_world"] = closed
        return out
    out = {"status": "OK", "frame": frame, "readout": hits, "count": len(hits), "trace": trace}
    if closed:
        out["closed_world"] = closed
    if assumed_on_path:
        # removal test: flip each assumed sex, see if the count moves
        flip = {m: ("M" if g["nodes"][m]["sex"][0] == "F" else "F") for m in assumed_on_path}
        alt, _ = _walk(g, frame, q["path"], sex_override=flip)
        if len(alt) != len(hits):
            out["status"] = "OK_CONDITIONAL"
            out["assumption"] = {m: g["nodes"][m]["sex"][0] for m in assumed_on_path}
            out["if_assumption_flipped"] = len(alt)
            trace.append(f"LOAD-BEARING ASSUMPTION: {out['assumption']} -> {len(hits)}; flipped -> {len(alt)}")
        else:
            trace.append(f"assumption {assumed_on_path} not load-bearing (count unchanged when flipped)")
    trace.append(f"READ from {frame}: {len(hits)}")
    return out

# ---------------------------------------------------------------- extractor
# Deterministic, rule-based. It is the harness trigger path: no model judgment.
# It returns MISSING rather than guess when a sentence shape is not covered.

NUM = {"no": 0, "zero": 0, "one": 1, "a": 1, "an": 1, "two": 2, "three": 3, "four": 4,
       "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
       "eleven": 11, "twelve": 12, "only": 1}
NUMRX = r"(\d+|no|zero|one|a|an|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)"
F_WORDS = {"sister": "F", "sisters": "F", "girl": "F", "girls": "F", "daughter": "F",
           "daughters": "F", "brother": "M", "brothers": "M", "boy": "M", "boys": "M",
           "son": "M", "sons": "M"}


def _n(tok):
    tok = tok.lower()
    return int(tok) if tok.isdigit() else NUM[tok]


def extract(text):
    t = " " + text.strip() + " "
    low = t.lower()
    miss = lambda why: {"status": "MISSING", "missing": [why], "trace": [f"EXTRACT: {why}"]}

    nodes, edges = {}, [("P", None)]
    edges = []
    nodes["P"] = {"label": "shared parent(s)"}

    # --- anchor + sibling counts -------------------------------------------
    anchor, fam = None, None
    m = re.search(r"\b([A-Z][a-z]+) has " + NUMRX + r" (sisters?)(?:,| and) " + NUMRX + r" (brothers?)", t)
    if m:
        anchor = m.group(1)
        fam = {"anchor_sisters": _n(m.group(2)), "anchor_brothers": _n(m.group(4))}
    m2 = re.search(r"\b([A-Z][a-z]+) has " + NUMRX + r" (brothers?)(?:,| and) " + NUMRX + r" (sisters?)", t)
    if not fam and m2:
        anchor = m2.group(1)
        fam = {"anchor_brothers": _n(m2.group(2)), "anchor_sisters": _n(m2.group(4))}
    m3 = re.search(r"([A-Z][a-z]+)'s family includes " + NUMRX + r" (girls|boys) besides \1,? and " + NUMRX + r" (girls|boys)", t)
    if not fam and m3:
        anchor = m3.group(1)
        a, b = (_n(m3.group(2)), m3.group(3)), (_n(m3.group(4)), m3.group(5))
        d = {a[1]: a[0], b[1]: b[0]}
        fam = {"others_F": d.get("girls", 0), "others_M": d.get("boys", 0), "anchor_in": True}
        nodes[anchor] = {"sex": ("F", "DECLARED"), "label": anchor}  # "girls besides Alice"
    m4 = re.search(r"([A-Z][a-z]+)'s family there are " + NUMRX + r" (daughters|sons) in total and " + NUMRX + r" (daughters|sons)", t)
    if not fam and m4:
        anchor = m4.group(1)
        d = {m4.group(3): _n(m4.group(2)), m4.group(5): _n(m4.group(4))}
        fam = {"total_F": d.get("daughters", 0), "total_M": d.get("sons", 0), "anchor_in": "OPEN"}
    if not fam:
        return miss("no sibling-count sentence shape recognized")

    # --- anchor sex: declared by pronoun, else assumed from name -----------
    if anchor not in nodes and fam.get("anchor_in") != "OPEN":
        if re.search(r"\b(her|she)\b", low):
            nodes[anchor] = {"sex": ("F", "DECLARED"), "label": anchor}
        elif re.search(r"\b(his|he)\b", low):
            nodes[anchor] = {"sex": ("M", "DECLARED"), "label": anchor}
        else:
            nodes[anchor] = {"label": anchor}  # v2: no name prior. sex OPEN, always.

    # --- place the sibling set under one shared parent node ----------------
    kids = []
    def add(prefix, k, sex):
        for i in range(1, k + 1):
            nid = f"{prefix}{i}"
            nodes[nid] = {"sex": (sex, "DECLARED"), "label": f"{prefix}{i}"}
            kids.append(nid)
    if "anchor_sisters" in fam:
        add("S", fam["anchor_sisters"], "F"); add("B", fam["anchor_brothers"], "M")
        kids.append(anchor)
    elif "others_F" in fam:
        add("S", fam["others_F"], "F"); add("B", fam["others_M"], "M")
        kids.append(anchor)
    else:  # totals; anchor membership left open (not placed as a child)
        add("S", fam["total_F"], "F"); add("B", fam["total_M"], "M")
    edges += [("P", k) for k in kids]

    # --- distractors: cousins (parent open, not under P) --------------------
    mc = re.search(NUMRX + r" cousins", low)
    if mc:
        for i in range(1, _n(mc.group(1)) + 1):
            nodes[f"C{i}"] = {"label": "cousin (parent OPEN)"}

    # --- second generation ---------------------------------------------------
    me = re.search(r"each of (?:her|his|" + (anchor or "x").lower() + r"'s) (brothers|sisters) has " + NUMRX + r" (sons|daughters|children)", low)
    if me:
        par_sex = F_WORDS[me.group(1)]
        kid_sex = F_WORDS.get(me.group(3))
        for p in [k for k in kids if nodes[k].get("sex", (None,))[0] == par_sex and k != anchor]:
            for j in range(1, _n(me.group(2)) + 1):
                cid = f"{p}c{j}"
                nodes[cid] = {"sex": (kid_sex, "DECLARED")} if kid_sex else {}
                edges.append((p, cid))
    mt = re.search(r"one of (?:her|his) brothers, ([A-Z][a-z]+), has " + NUMRX + r" (children|sons|daughters)", t)
    if mt:
        nodes["B1"]["label"] = mt.group(1)
        for j in range(1, _n(mt.group(2)) + 1):
            kid_sex = F_WORDS.get(mt.group(3))
            nodes[f"B1c{j}"] = {"sex": (kid_sex, "DECLARED")} if kid_sex else {}
            edges.append(("B1", f"B1c{j}"))

    # --- frame: who is "you"? ------------------------------------------------
    frame = None
    mf = re.search(r"(?:you are|you were|suppose you were) one of (?:" + anchor + r"'s|her|his|the) (brothers|sisters|boys|girls|sons|daughters)", t, re.I)
    if mf:
        want = F_WORDS[mf.group(1).lower()]
        frame = next((k for k in kids if k != anchor and nodes[k]["sex"][0] == want), None)
    elif re.search(r"(?:you are|you were) " + anchor + r"'s (brother|sister)\b", t):
        want = F_WORDS[re.search(r"you are " + anchor + r"'s (brother|sister)", t).group(1) + "s"]
        frame = next((k for k in kids if k != anchor and nodes[k]["sex"][0] == want), None)
    elif re.search(r"how many \w+ does " + anchor + r" have", t, re.I):
        frame = anchor
    elif re.search(r"in " + anchor + r"'s family", t) and re.search(r"counting yourself", low):
        frame = anchor  # set named relative to the anchor; 'you' is a member
    if frame is None:
        return miss("frame (who is reading) not recognized")

    # --- query path -------------------------------------------------------
    path = None
    mq = re.search(r"how many (sisters|brothers|siblings) (?:do you have|does \w+ have|are there)", low)
    mg = re.search(r"how many (girls|boys) in the family would be your (sisters|brothers)", low)
    mn = re.search(r"how many of these (sons|daughters) are (?:nephews|nieces) of yours through your (brothers|sisters)", low)
    mni = re.search(r"how many (nieces|nephews) do you have through your (brothers|sisters)", low)
    mt2 = re.search(r"(?:counting|including) yourself, how many (sisters|brothers|siblings|girls|boys)", low)
    if mt2:   # whole set under the shared parent, self included
        w = mt2.group(1)
        path = [("parent", {}), ("child", {} if w == "siblings" else {"sex": F_WORDS[w]})]
    elif mn:
        path =[("sibling", {"sex": F_WORDS[mn.group(2)]}), ("child", {"sex": F_WORDS[mn.group(1)]})]
    elif mni:
        kid = "F" if mni.group(1) == "nieces" else "M"
        path = [("sibling", {"sex": F_WORDS[mni.group(2)]}), ("child", {"sex": kid})]
    elif mg:
        path = [("sibling", {"sex": F_WORDS[mg.group(2)]})]
    elif mq:
        w = mq.group(1)
        path = [("sibling", {} if w == "siblings" else {"sex": F_WORDS[w]})]
    if path is None:
        return miss("query relation not recognized")

    return {"nodes": nodes, "edges": edges, "query": {"from": frame, "path": path}}


def solve(text):
    spec = extract(text)
    if spec.get("status") == "MISSING":
        return spec
    return glyph(spec)

# ---------------------------------------------------------------- selftest

def selftest():
    r = solve("Alice has two sisters and five brothers. If you are one of Alice's brothers, how many sisters do you have?")
    assert r["status"] == "CONDITIONAL" and r["branches"] == {"Alice=F": 3, "Alice=M": 2}, r
    r = solve("Alice has two sisters and five brothers. How many sisters does Alice have?")
    assert r["status"] == "OK" and r["count"] == 2, r          # Alice's sex not load-bearing here
    r = solve("Alice has no sisters and three brothers. You are one of her brothers. How many sisters do you have?")
    assert r["count"] == 1 and r["status"] == "OK", r          # 'her' declares sex
    r = solve("Sam has two sisters and two brothers. If you are one of Sam's brothers, how many sisters do you have?")
    assert r["status"] == "CONDITIONAL" and r["branches"] == {"Sam=F": 3, "Sam=M": 2}, r
    r = solve("What is the capital of France?")
    assert r["status"] == "MISSING", r
    r = solve("Alice has two sisters and five brothers. Each of her sisters has two daughters. You are one of Alice's brothers. How many nieces do you have through your sisters?")
    assert r["count"] == 4 and r["closed_world"] == ["Alice"], r   # Alice's children: undeclared, traced
    spec = extract("Alice has two sisters and five brothers. Each of her brothers has three sons. You are one of Alice's sisters. How many of these sons are nephews of yours through your brothers?")
    r = glyph(spec); assert r["count"] == 15, r
    son = next(n for n in spec["nodes"] if n.startswith("B1c"))
    spec["query"] = {"from": son, "path": [("parent", {}), ("sibling", {"sex": "F"})]}
    r = glyph(spec); assert r["count"] == 3, r                 # aunts, walked backward
    return "8/8 PASS"


if __name__ == "__main__":
    print(selftest())

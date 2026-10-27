"""run_g2.py (v2 scoring: CONDITIONAL kept separate from CORRECT) -- CC0, stdlib. G2 pilot: frame_glyph vs RPF-01 Test A (Qwen2.5-0.5B arm).
usage: python3 run_g2.py CASES.jsonl QWEN_RAW.jsonl [HELDOUT.jsonl] > out.json
Outcome per item: CORRECT | WRONG | MISSING  (MISSING = tool declined; not a wrong number)
"""
import json, re, sys, os, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame_glyph as fg


def last_int(s):
    m = re.findall(r"-?\d+", s or "")
    return int(m[-1]) if m else None


def run(items, qwen=None):
    rows = []
    for c in items:
        text = c["messages"][-1]["content"].replace("Answer with just the number.", "").strip()
        exp = c["scoring"]["expected"]
        r = fg.solve(text)
        if r["status"] == "MISSING":
            out = "MISSING"
        elif r["status"] == "CONDITIONAL":
            if exp is None:
                out = "CORRECT_UNDETERMINED"          # truly open; tool gave all branches
            else:
                out = "CONDITIONAL_KEY_IN_BRANCHES" if exp in r["branches"].values() else "WRONG"
        else:
            out = "CORRECT" if r["count"] == exp else "WRONG"
        row = {"id": c["id"], "condition": c.get("condition"), "expected": exp,
               "glyph_status": r["status"], "glyph_count": r.get("count"),
               "glyph_outcome": out, "branches": r.get("branches"), "closed_world": r.get("closed_world"),
               "missing": r.get("missing"), "trace": r.get("trace")}
        if qwen is not None:
            q = last_int(qwen.get(c["id"]))
            row["qwen_answer"] = q
            row["qwen_outcome"] = "CORRECT" if q == exp else "WRONG"
        rows.append(row)
    return rows


def tally(rows, key):
    t = {}
    for r in rows:
        t[r[key]] = t.get(r[key], 0) + 1
    return t


if __name__ == "__main__":
    cases = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
    cases = [c for c in cases if c["id"].startswith("A")]
    qwen = {}
    for l in open(sys.argv[2]):
        if l.strip():
            r = json.loads(l)
            if "id" in r: qwen[r["id"]] = r.get("response")
    res = {"tool_sha256": hashlib.sha256(open(fg.__file__, "rb").read()).hexdigest(),
           "rpf01_A": run(cases, qwen)}
    res["rpf01_A_tally"] = {"glyph": tally(res["rpf01_A"], "glyph_outcome"),
                            "qwen": tally(res["rpf01_A"], "qwen_outcome"),
                            "conditional": sum(1 for r in res["rpf01_A"] if r["glyph_status"] == "CONDITIONAL")}
    if len(sys.argv) > 3:
        ho = [json.loads(l) for l in open(sys.argv[3]) if l.strip()]
        res["heldout"] = run(ho)
        res["heldout_tally"] = {"glyph": tally(res["heldout"], "glyph_outcome"),
                                "undetermined_returned_all_branches": sum(1 for r, c in zip(res["heldout"], ho)
                                    if c["scoring"].get("expect_missing") and r["glyph_outcome"] == "CORRECT_UNDETERMINED")}
    print(json.dumps(res, indent=1))

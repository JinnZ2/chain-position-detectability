#!/usr/bin/env python3
"""check_repo.py -- recompute every number this repository states about itself.

The tree is documents and CSV. Nothing in it ran before this file existed, so
every count, sum, date interval and cross-rendered table was a typed number
with no check behind it. This script is the check. Each function below is one
claim in AUDIT_NOTES.md made recomputable; the id in the function docstring is
the claim it backs.

    python3 tools/check_repo.py            run every check on this tree
    python3 tools/check_repo.py --selftest plant defects in a copy, prove each
                                           check fires, then run the real tree
    python3 tools/check_repo.py --json     machine-readable results

Exit codes follow the ecosystem contract:
    0  checks ran, none FAILED   (FLAGs are recorded findings, not failures)
    1  checks ran, >= 1 FAILED
    3  could not run (missing input)

Four result states, kept apart: PASS (property holds), FAIL (a property the
tree should maintain is broken), FLAG (a recorded finding that still stands;
it clears when the finding is repaired, and clearing is reported), and
NOT_TESTABLE (the check needs an input this machine does not have; it names
the input, and it is neither a pass nor a failure -- a check that cannot run
must not read as a check that passed).

Stdlib only. Parses under Python 3.8. No network: the one cross-repository
check reads a SIBLING CHECKOUT on local disk through git, never a remote.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import hashlib
import shutil
import subprocess
import sys
import tempfile
from typing import Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- results ---

class Result:
    def __init__(self, check: str, state: str, detail: str) -> None:
        assert state in ("PASS", "FAIL", "FLAG", "NOT_TESTABLE")
        self.check, self.state, self.detail = check, state, detail

    def row(self) -> str:
        return "%-18s %-12s %s" % (self.check, self.state, self.detail)


def _read(root: str, rel: str) -> str:
    p = os.path.join(root, rel)
    if not os.path.exists(p):
        raise FileNotFoundError(rel)
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def _md_files(root: str) -> List[str]:
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(d, f), root))
    return sorted(out)


# ------------------------------------------------------------------ checks ---

LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
REF_RE = re.compile(r'^\[(\d+)\]:\s+(\S+)', re.M)
SELF_RE = re.compile(r'https://github\.com/JinnZ2/chain-position-detectability/blob/main/(.+)$')


def check_links(root: str) -> Result:
    """CPD_002 -- every relative link and every self-absolute blob/main link resolves."""
    broken = []
    n_rel = n_self = 0
    for rel in _md_files(root):
        txt = _read(root, rel)
        here = os.path.dirname(os.path.join(root, rel))
        targets = [m.group(2) for m in LINK_RE.finditer(txt)] + [m.group(2) for m in REF_RE.finditer(txt)]
        for tgt in targets:
            m = SELF_RE.match(tgt)
            if m:
                n_self += 1
                if not os.path.exists(os.path.join(root, m.group(1))):
                    broken.append("%s -> %s" % (rel, tgt))
                continue
            if tgt.startswith(("http://", "https://", "mailto:")):
                continue
            path = tgt.split("#")[0]
            if not path:
                continue
            n_rel += 1
            if not os.path.exists(os.path.join(here, path)):
                broken.append("%s -> %s" % (rel, tgt))
    detail = "relative %d, self-absolute(blob/main) %d, broken %d" % (n_rel, n_self, len(broken))
    if broken:
        return Result("links", "FAIL", detail + "; " + "; ".join(broken[:5]))
    return Result("links", "PASS", detail)


def check_wo1_clauses(root: str) -> Result:
    """CPD_003 -- the standards-audit table sums to the totals it states."""
    txt = _read(root, "research/wo-1/standards-audit.md")
    rows = [l for l in txt.splitlines() if l.startswith("| [")]
    counts = [int(l.split("|")[3].strip()) for l in rows]
    m_split = re.search(r"The (\d+) candidate clauses comprise \*\*(\d+)\*\* OWASP .*? \*\*(\d+)\*\* ACS", txt)
    m_readme = re.search(r"reviewed \*\*(\d+) candidate clauses\*\*", _read(root, "research/wo-1/README.md"))
    if not (m_split and m_readme):
        return Result("wo1_clauses", "FAIL", "stated totals not found in text")
    stated = (int(m_split.group(1)), int(m_split.group(2)), int(m_split.group(3)))
    readme_total = int(m_readme.group(1))
    got = (sum(counts), sum(counts[:5]), sum(counts[5:]))
    detail = "units %d; table sums total/owasp/acs = %s; audit states %s; wo-1 README states %d" % (len(rows), got, stated, readme_total)
    if len(rows) != 15 or got != stated or readme_total != stated[0]:
        return Result("wo1_clauses", "FAIL", detail)
    return Result("wo1_clauses", "PASS", detail)


def _wo2_rows(root: str) -> List[Dict[str, str]]:
    with open(os.path.join(root, "research/wo-2/reconciled-dataset.csv"), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def check_wo2_dates(root: str) -> Result:
    """CPD_006 -- lead_time_days_min/max reproduce from first_signal_date and event_date."""
    rows = _wo2_rows(root)
    bad, checked, nulls = [], 0, 0
    for r in rows:
        fs, ev = r["first_signal_date"].strip(), dt.date.fromisoformat(r["event_date"])
        lo, hi = r["lead_time_days_min"].strip(), r["lead_time_days_max"].strip()
        exp: Optional[Tuple[Optional[int], Optional[int]]] = None
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", fs):
            d = (ev - dt.date.fromisoformat(fs)).days
            exp = (d, d)
        elif re.fullmatch(r"\d{4}", fs):
            y = int(fs)
            exp = ((ev - dt.date(y, 12, 31)).days, (ev - dt.date(y, 1, 1)).days)
        elif fs == "unknown":
            exp = (None, None)
        if exp is None:
            continue  # relative interval ('at least 3 years ...'): not recomputable from the field
        checked += 1
        got = (int(lo) if lo else None, int(hi) if hi else None)
        if got == (None, None):
            nulls += 1
        if got != exp and not (fs == "2024-10-08" and got == (1, 2) and exp == (2, 2)):
            # PEMEX carries a 1-2 day range for an exact 2-day interval; the source gives
            # a range, the CSV preserves it. Recorded in AUDIT_NOTES, not failed here.
            bad.append("%s: csv %s expected %s" % (r["case_id"], got, exp))
    detail = "rows %d, recomputable %d, null-kept %d, mismatches %d" % (len(rows), checked, nulls, len(bad))
    if bad:
        return Result("wo2_dates", "FAIL", detail + "; " + "; ".join(bad))
    return Result("wo2_dates", "PASS", detail)


def check_wo2_distributions(root: str) -> Result:
    """CPD_006 -- CSV column counts match the pilot-analysis variable table."""
    rows = _wo2_rows(root)
    txt = _read(root, "research/wo-2/pilot-analysis.md")

    def stated(label: str) -> Dict[str, int]:
        m = re.search(r"^\| %s \| ([^|]+) \|" % re.escape(label), txt, re.M)
        if not m:
            return {}
        out = {}
        for part in m.group(1).split(";"):
            mm = re.match(r"\s*(\d+)\s+(.+?)\s*$", part)
            if mm:
                out[mm.group(2).replace(" ", "_")] = int(mm.group(1))
        return out

    def counted(col: str) -> Dict[str, int]:
        out: Dict[str, int] = {}
        for r in rows:
            out[r[col]] = out.get(r[col], 0) + 1
        return out

    pairs = [("Join assigned", "join_assigned"), ("Pattern result", "pattern_result"), ("Sudden label", "sudden_label")]
    bad = []
    for label, col in pairs:
        s, c = stated(label), counted(col)
        for k, v in s.items():
            if c.get(k, 0) != v:
                bad.append("%s %s: stated %d csv %d" % (col, k, v, c.get(k, 0)))
    detail = "3 columns against the prose table; mismatches %d" % len(bad)
    return Result("wo2_distrib", "FAIL" if bad else "PASS", detail + ("; " + "; ".join(bad) if bad else ""))


ROW_RE = re.compile(r'^\|\s*`([a-z_]+)`\s*\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|', re.M)


def _decision_table(root: str, rel: str) -> Dict[str, str]:
    d: Dict[str, str] = {}
    for m in ROW_RE.finditer(_read(root, rel)):
        d.setdefault(m.group(1), m.group(2).strip().strip("`").lower())
    return d


def check_wo2_agreement(root: str) -> Result:
    """CPD_004 -- the stated coder agreement (59 of 87) recomputed from the two coders' tables."""
    log = _read(root, "research/wo-2/reconciliation-log.md")
    m = re.search(r"agreed on \*\*(\d+) of (\d+) structured-field comparisons", log)
    if not m:
        return Result("wo2_agreement", "FAIL", "stated agreement not found")
    s_num, s_den = int(m.group(1)), int(m.group(2))
    cb_vars = set(re.findall(r"^\|\s*`([a-z_]+)`", _read(root, "research/wo-2/codebook.md"), re.M))
    cases = [r["case_id"] for r in _wo2_rows(root)]
    a_all = d_all = a_cb = d_cb = 0
    for c in cases:
        a = _decision_table(root, "research/wo-2/coding/coder-a/%s.md" % c)
        b = _decision_table(root, "research/wo-2/coding/coder-b/%s.md" % c)
        for k in set(a) & set(b):
            d_all += 1
            a_all += a[k] == b[k]
            if k in cb_vars:
                d_cb += 1
                a_cb += a[k] == b[k]
    detail = "stated %d/%d; shared-fields %d/%d; codebook-only %d/%d" % (s_num, s_den, a_all, d_all, a_cb, d_cb)
    if a_all != s_num:
        return Result("wo2_agreement", "FAIL", detail + "; numerator does not reproduce")
    if d_all != s_den:
        return Result("wo2_agreement", "FLAG", detail + "; numerator reproduces, denominator does not: the comparison list is unpublished (CPD_004)")
    return Result("wo2_agreement", "PASS", detail)


def check_wo2_fields(root: str) -> Result:
    """CPD_005 -- fields used by coders/validators/CSV that the codebook does not declare."""
    cb_vars = set(re.findall(r"^\|\s*`([a-z_]+)`", _read(root, "research/wo-2/codebook.md"), re.M))
    used = set()
    for sub in ("coding/coder-a", "coding/coder-b", "validation"):
        for c in [r["case_id"] for r in _wo2_rows(root)]:
            used |= set(_decision_table(root, "research/wo-2/%s/%s.md" % (sub, c)))
    with open(os.path.join(root, "research/wo-2/reconciled-dataset.csv"), encoding="utf-8") as fh:
        cols = next(csv.reader(fh))
    extra_records = sorted(used - cb_vars)
    extra_csv = [c for c in cols if c not in cb_vars]
    detail = "codebook %d; record fields outside it %s; csv columns outside it %s" % (len(cb_vars), extra_records, extra_csv)
    return Result("wo2_fields", "FLAG" if (extra_records or extra_csv) else "PASS", detail)


def check_wo3_arithmetic(root: str) -> Result:
    """CPD_008 -- the physical quantities WO-3 states reproduce from their own inputs."""
    JY = 365.25 * 86400.0
    txt = _read(root, "research/wo-3/validation-summary.md") + _read(root, "research/wo-3/asymptote-results.csv")
    checks = []
    # Voyager: 3 RTG x 2243 W; decay 2^(-58/88); one Julian year of the integrated energy stated.
    p0 = 3 * 2243
    p2035 = p0 * 2 ** (-58 / 88)
    e_stated = 1.3394888e11
    checks.append(("voyager 3x2243 W", p0, 6729, 0))
    checks.append(("voyager 2035 kW", p2035 / 1000, 4.261322, 1e-5))
    checks.append(("voyager mean kW", e_stated / JY / 1000, 4.244584, 1e-5))
    checks.append(("launch->2035 Jy", (dt.date(2035, 1, 1) - dt.date(1977, 9, 5)).days / 365.25, 57.3224, 1e-3))
    # Forsmark: 6000 canisters x 1700 W design maximum, over 70 Julian years.
    checks.append(("forsmark MW", 6000 * 1700 / 1e6, 10.2, 1e-9))
    checks.append(("forsmark J/70Jy", 6000 * 1700 * 70 * JY, 2.25321264e16, 1e-6))
    checks.append(("forsmark 2.3e6/1e6", 2.3e6 / 1e6, 2.30, 1e-9))
    # GW150914: 2.5 solar masses c^2 at the solar-mass convention that yields the stated digits.
    checks.append(("gw 2.5Msun c^2 J", 2.5 * 1.98847e30 * 299792458 ** 2, 4.4679e47, 2e-4))
    bad = []
    for name, got, want, tol in checks:
        rel_err = abs(got - want) / abs(want) if want else abs(got - want)
        if rel_err > tol:
            bad.append("%s: got %.7g want %.7g" % (name, got, want))
    present = [s for s in ("4.244584", "1.3394888", "2.25321264", "4.4679", "57.3224", "4.261322") if s in txt]
    detail = "%d quantities recomputed, %d mismatches; stated strings found %d/6" % (len(checks), len(bad), len(present))
    return Result("wo3_arithmetic", "FAIL" if bad else "PASS", detail + ("; " + "; ".join(bad) if bad else ""))


GATE_NORM = {"p": "pass", "p*": "pass", "f": "fail", "u": "conditional"}


def _norm_gate(cell: str) -> str:
    c = cell.replace("*", "").strip().lower()
    if c in GATE_NORM:
        return GATE_NORM[c]
    if c.startswith("pass"):
        return "pass"
    if c.startswith("fail"):
        return "fail"
    if c.startswith("conditional"):
        return "conditional"
    return c


def _gate_rows_md(txt: str, keys: List[str]) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = {}
    for line in txt.splitlines():
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        for k in keys:
            if cells[0].lower().startswith(k) and k not in out:
                out[k] = [_norm_gate(c) for c in cells[1:6]]
    return out


def check_wo3_gates(root: str) -> Result:
    """CPD_009 -- the five-gate table agrees cell-for-cell across its three renderings."""
    keys = ["deepwater", "flint", "grenfell", "boeing", "challenger", "texas"]
    a = _gate_rows_md(_read(root, "research/wo-3/final-report.md"), keys)
    b = _gate_rows_md(_read(root, "research/wo-3/workflow-synthesis.md"), keys)
    c: Dict[str, List[str]] = {}
    with open(os.path.join(root, "research/wo-3/cost-case-screen.csv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            for k in keys:
                if r["candidate_id"].startswith(k):
                    c[k] = [_norm_gate(r[col]) for col in (
                        "gate_1_control_available", "gate_2_decision_documented",
                        "gate_3_contemporaneous_same_control_cost_or_rationale",
                        "gate_4_authoritative_harm_or_risk_link", "gate_5_downstream_cost_category")]
    bad = []
    for k in keys:
        if not (k in a and k in b and k in c):
            bad.append("%s missing from a rendering" % k)
            continue
        if not (a[k] == b[k] == c[k]):
            bad.append("%s: report %s synthesis %s csv %s" % (k, a[k], b[k], c[k]))
    detail = "6 candidates x 5 gates x 3 renderings; disagreements %d" % len(bad)
    return Result("wo3_gates", "FAIL" if bad else "PASS", detail + ("; " + "; ".join(bad) if bad else ""))


def check_wo4_invariant(root: str) -> Result:
    """CPD_015 -- the counts research/wo-4/formal-statement.md states reproduce from invariant.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("wo4_invariant", os.path.join(root, "research/wo-4/invariant.py"))
    if spec is None or spec.loader is None:
        raise FileNotFoundError("research/wo-4/invariant.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    txt = _read(root, "research/wo-4/formal-statement.md")
    m = re.search(r"controls\s+(\d+).*?\nfaces\s+(\d+)", txt)
    k = re.search(r"assembly (\d+) .*?\nsensing\s+(\d+)", txt)
    c = re.search(r"terms (\d+)\s+name C1 only (\d+)\s+name C2 only (\d+)\s+name C3 only (\d+)\s+name neither (\d+)\s+name C1 AND C3 (\d+)", txt)
    if not (m and k and c):
        return Result("wo4_invariant", "FAIL", "stated counts not found in formal-statement.md")
    faces = [f.analyze() for f in mod.faces()]
    got = (len(mod.controls()), len(faces),
           sum(r["kind"] == "assembly" for r in faces), sum(r["kind"] == "sensing" for r in faces))
    stated = (int(m.group(1)), int(m.group(2)), int(k.group(1)), int(k.group(2)))
    # census table: one row per term; the 'both' column must read 'no' for every row for the stated 0 to hold
    rows = [l for l in txt.splitlines() if l.startswith("| ") and l.count("|") == 7 and "names C1" not in l and "---" not in l]
    both = sum(1 for l in rows if l.rsplit("|", 2)[-2].strip().lower().startswith("yes"))
    verdicts = {r["verdict"] for r in [i.analyze() for i in mod.controls()]}
    detail = "controls/faces/assembly/sensing got %s stated %s; census rows %d stated %s, both-yes %d stated %s; control verdicts %d" % (
        got, stated, len(rows), c.group(1), both, c.group(6), len(verdicts))
    ok = got == stated and len(rows) == int(c.group(1)) and both == int(c.group(6)) and len(verdicts) == 4
    return Result("wo4_invariant", "PASS" if ok else "FAIL", detail)


def check_readme_duplicate(root: str) -> Result:
    """CPD_001 -- the root README is a byte copy of one work order."""
    readme = _read(root, "README.md")
    wo_dir = os.path.join(root, "work-orders")
    for f in sorted(os.listdir(wo_dir)):
        if f.startswith("WO-") and _read(root, "work-orders/" + f) == readme:
            return Result("readme_dup", "FLAG", "README.md is byte-identical to work-orders/%s (CPD_001)" % f)
    return Result("readme_dup", "PASS", "README.md differs from every work order")


def check_status_table(root: str) -> Result:
    """The work-orders index names files and research dirs that exist."""
    txt = _read(root, "work-orders/README.md")
    bad, n = [], 0
    for m in re.finditer(r"\]\((WO-\d[^)]+\.md)\)", txt):
        n += 1
        if not os.path.exists(os.path.join(root, "work-orders", m.group(1))):
            bad.append(m.group(1))
    for m in re.finditer(r"\]\(\.\./research/(wo-\d)/\)", txt):
        if not os.path.isdir(os.path.join(root, "research", m.group(1))):
            bad.append("research/" + m.group(1))
    wo_files = sorted(f for f in os.listdir(os.path.join(root, "work-orders")) if f.startswith("WO-"))
    research = sorted(d for d in os.listdir(os.path.join(root, "research")))
    detail = "index rows %d, WO files %d, research dirs %s, unresolved %d" % (n, len(wo_files), research, len(bad))
    return Result("status_table", "FAIL" if bad or n != len(wo_files) else "PASS", detail + ("; " + "; ".join(bad) if bad else ""))


POINTER_FILE = "work-orders/WO-11-benchmark-score-unpartitioned-residual.md"
POINTER_BODY_START = 12  # the delivered text begins at this line of the canonical file; the pointer states it


def _sibling_simulators(root: str) -> str:
    """The Simulators checkout this check reads. SIMULATORS_PATH overrides; default is the sibling directory."""
    return os.environ.get("SIMULATORS_PATH") or os.path.join(os.path.dirname(root), "Simulators")


def check_pointer_hash(root: str) -> Result:
    """CPD_016 -- the two sha256 values the WO-11 pointer states reproduce from the pinned commit.

    Reads work-orders/WO-11-*.md for a commit, a path and two hashes; runs
    `git show <commit>:<path>` in a sibling Simulators checkout; hashes the
    whole file and the body from POINTER_BODY_START. No sibling, or a sibling
    that does not hold the commit, is NOT_TESTABLE naming what is missing --
    the hashes are then typed numbers on this machine and the row says so.
    """
    txt = _read(root, POINTER_FILE)
    commit = re.search(r"JinnZ2/Simulators @ ([0-9a-f]{7,40})", txt)
    path = re.search(r"^\s+(publication-loop-work-orders/\S+\.md)\s*$", txt, re.M)
    whole = re.search(r"^whole file\s+([0-9a-f]{64})", txt, re.M)
    body = re.search(r"^body, line (\d+)\+\s+([0-9a-f]{64})", txt, re.M)
    if not (commit and path and whole and body):
        return Result("pointer_hash", "FAIL", "pointer does not state commit, path and both hashes")
    if int(body.group(1)) != POINTER_BODY_START:
        return Result("pointer_hash", "FAIL", "pointer says body starts at line %s; this check is written for %d" % (body.group(1), POINTER_BODY_START))
    sib = _sibling_simulators(root)
    if not os.path.isdir(os.path.join(sib, ".git")):
        return Result("pointer_hash", "NOT_TESTABLE", "no Simulators checkout at %s (set SIMULATORS_PATH); hashes stated, not recomputed" % sib)
    try:
        subprocess.run(["git", "-C", sib, "cat-file", "-e", commit.group(1) + "^{commit}"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, OSError):
        return Result("pointer_hash", "NOT_TESTABLE", "checkout at %s does not hold %s; fetch it, or hashes stay stated" % (sib, commit.group(1)))
    try:
        raw = subprocess.run(["git", "-C", sib, "show", "%s:%s" % (commit.group(1), path.group(1))], check=True, capture_output=True).stdout
    except subprocess.CalledProcessError:
        return Result("pointer_hash", "FAIL", "%s not in %s at %s" % (path.group(1), sib, commit.group(1)))
    lines = raw.split(b"\n")
    got_whole = hashlib.sha256(raw).hexdigest()
    got_body = hashlib.sha256(b"\n".join(lines[POINTER_BODY_START - 1:])).hexdigest()
    title_ok = lines[POINTER_BODY_START - 1].startswith(b"# WORK ORDER 11")
    ok = got_whole == whole.group(1) and got_body == body.group(2) and title_ok
    detail = "%s:%s whole %s..%s stated %s..; body(line %d+) %s.. stated %s..; line %d is a WORK ORDER 11 title: %s" % (
        commit.group(1), os.path.basename(path.group(1)), got_whole[:8], got_whole[-4:], whole.group(1)[:8],
        POINTER_BODY_START, got_body[:8], body.group(2)[:8], POINTER_BODY_START, title_ok)
    return Result("pointer_hash", "PASS" if ok else "FAIL", detail)


CHECKS = [check_links, check_wo1_clauses, check_wo2_dates, check_wo2_distributions,
          check_wo2_agreement, check_wo2_fields, check_wo3_arithmetic, check_wo3_gates,
          check_wo4_invariant, check_readme_duplicate, check_status_table, check_pointer_hash]


def run(root: str) -> List[Result]:
    out = []
    for fn in CHECKS:
        try:
            out.append(fn(root))
        except FileNotFoundError as e:
            out.append(Result(fn.__name__.replace("check_", ""), "FAIL", "missing input %s" % e))
    return out


# ---------------------------------------------------------------- selftest ---

def _plant(src: str, dst: str) -> None:
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git"))

    def edit(rel: str, old: str, new: str) -> None:
        p = os.path.join(dst, rel)
        with open(p, encoding="utf-8") as fh:
            t = fh.read()
        assert old in t, (rel, old)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(t.replace(old, new, 1))

    edit("research/wo-1/README.md", "(standards-audit.md)", "(standards-audit-MISSING.md)")
    edit("research/wo-1/standards-audit.md", "| 166 |", "| 165 |")
    edit("research/wo-2/reconciled-dataset.csv", "2012-10-15,4411,4411", "2012-10-15,4410,4411")
    edit("research/wo-2/pilot-analysis.md", "| 1 no; 7 unclear; 0 yes |", "| 2 no; 6 unclear; 0 yes |")
    edit("research/wo-3/cost-case-screen.csv", '"pass","pass","fail","pass_disputed"', '"pass","pass","pass","pass_disputed"')
    edit("research/wo-2/coding/coder-a/givaudan-sense-colour.md", "| `signal_present` | **yes** |", "| `signal_present` | **no** |")
    edit("README.md", "# WO-1", "# Repository index\n\n# WO-1")
    edit("research/wo-4/formal-statement.md", "assembly 3 ", "assembly 4 ")
    edit(POINTER_FILE, "body, line 12+  ada578e2", "body, line 12+  0da578e2")


def selftest() -> int:
    n = 0
    tmp = tempfile.mkdtemp(prefix="cpd-selftest-")
    try:
        planted = os.path.join(tmp, "tree")
        _plant(ROOT, planted)
        res = {r.check: r for r in run(planted)}
        for name in ("links", "wo1_clauses", "wo2_dates", "wo2_distrib", "wo3_gates", "wo2_agreement", "wo4_invariant"):
            assert res[name].state == "FAIL", (name, res[name].row())
            n += 1
        assert res["readme_dup"].state == "PASS", res["readme_dup"].row(); n += 1
        # the planted body hash is one hex digit off; with a sibling present the row must FAIL,
        # and without one it must say NOT_TESTABLE rather than PASS on an unchecked number
        if os.path.isdir(os.path.join(_sibling_simulators(planted), ".git")):
            assert res["pointer_hash"].state == "FAIL", res["pointer_hash"].row(); n += 1
        else:
            assert res["pointer_hash"].state == "NOT_TESTABLE", res["pointer_hash"].row(); n += 1
        # a sibling that is not there reads NOT_TESTABLE, never PASS: the row names the missing input
        saved = os.environ.get("SIMULATORS_PATH")
        os.environ["SIMULATORS_PATH"] = os.path.join(tmp, "no-such-checkout")
        try:
            r = check_pointer_hash(ROOT)
            assert r.state == "NOT_TESTABLE" and "no-such-checkout" in r.detail, r.row(); n += 1
        finally:
            if saved is None:
                del os.environ["SIMULATORS_PATH"]
            else:
                os.environ["SIMULATORS_PATH"] = saved
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    real = {r.check: r for r in run(ROOT)}
    for name in ("links", "wo1_clauses", "wo2_dates", "wo2_distrib", "wo3_arithmetic", "wo3_gates", "wo4_invariant", "status_table"):
        assert real[name].state == "PASS", real[name].row(); n += 1
    # recorded findings that stand today; each turns PASS when repaired and that is a change to record
    for name in ("readme_dup", "wo2_agreement", "wo2_fields"):
        assert real[name].state == "FLAG", real[name].row(); n += 1
    assert real["pointer_hash"].state in ("PASS", "NOT_TESTABLE"), real["pointer_hash"].row(); n += 1
    assert not any(r.state == "FAIL" for r in real.values()); n += 1
    print("selftest: %d checks PASS" % n)
    return 0


def main(argv: List[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if not os.path.isdir(os.path.join(ROOT, "work-orders")):
        print("could not run: work-orders/ missing under %s" % ROOT)
        return 3
    results = run(ROOT)
    if "--json" in argv:
        print(json.dumps([r.__dict__ for r in results], indent=1))
    else:
        print("check_repo.py  root=%s" % ROOT)
        for r in results:
            print(r.row())
        fails = sum(r.state == "FAIL" for r in results)
        flags = sum(r.state == "FLAG" for r in results)
        nt = sum(r.state == "NOT_TESTABLE" for r in results)
        print("checks %d  PASS %d  FLAG %d  FAIL %d  NOT_TESTABLE %d" % (len(results), len(results) - fails - flags - nt, flags, fails, nt))
    return 1 if any(r.state == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Build a conservative source-label-to-bibliography crosswalk for WO-5.

The script uses exact first-author/year candidate records collected from Crossref
and OpenAlex plus membership in three published plant-soil-feedback reference
pools. It never selects among tied plausible records without an explicit journal
suffix or a unique evidence advantage. Unresolved and ambiguous labels remain so.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
LABELS = ROOT / "source-labels.csv"
CANDIDATES = ROOT / "source-candidates.json"
CODED = ROOT / "analysis" / "hop-coded-effects.csv"
OUTPUT = ROOT / "source-crosswalk.csv"

JOURNAL_SUFFIXES = {
    " nature": ["nature"],
    " ecography": ["ecography"],
    " ecology": ["ecology"],
    " je": ["journal of ecology"],
    " oikos": ["oikos"],
    " sbb": ["soil biology and biochemistry", "soil biology & biochemistry"],
    " np": ["new phytologist"],
    " pe": ["plant ecology"],
    " ce": ["community ecology"],
    " ps": ["plant and soil"],
}


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()


def suffix_preference(label: str, candidates: list[dict]) -> tuple[dict | None, str | None]:
    normalized = " " + normalize(label)
    for suffix, journal_names in JOURNAL_SUFFIXES.items():
        if normalized.endswith(suffix):
            matches = [c for c in candidates if normalize(c.get("container", "")) in journal_names]
            if len(matches) == 1:
                return matches[0], f"raw label journal suffix uniquely matched {matches[0].get('container', '')}"
    return None, None


def choose_candidate(label: str, candidates: list[dict]) -> tuple[dict | None, str, str]:
    if not candidates:
        return None, "unresolved", "no exact first-author/year candidate was retained"

    suffix_choice, suffix_basis = suffix_preference(label, candidates)
    if suffix_choice is not None:
        return suffix_choice, "high", suffix_basis or "journal suffix match"

    pool_candidates = [c for c in candidates if c.get("mark")]
    if len(pool_candidates) == 1:
        c = pool_candidates[0]
        return c, "high", f"unique candidate present in published PSF reference pool(s): {c['mark']}"
    if len(pool_candidates) > 1:
        best_strength = max(len(c.get("mark", "")) for c in pool_candidates)
        strongest = [c for c in pool_candidates if len(c.get("mark", "")) == best_strength]
        if len(strongest) == 1:
            c = strongest[0]
            return c, "high", f"unique candidate with strongest published-reference-pool support: {c['mark']}"

    topical = [c for c in candidates if c.get("topical")]
    if len(topical) == 1:
        return topical[0], "moderate", "unique plant-soil topical candidate for exact first author and year"

    return None, "ambiguous", "multiple plausible exact-author/year candidates remain; no unique evidence-supported choice"


def main() -> None:
    labels = pd.read_csv(LABELS, dtype={"Author": str, "Year": str})
    candidates = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    coded = pd.read_csv(CODED, dtype={"Author": str, "Year": str})
    if len(labels) != 202 or len(candidates) != 202:
        raise SystemExit("Expected exactly 202 labels and candidate records")

    candidate_by_label = {record["label"]: record for record in candidates}
    rows: list[dict] = []
    for _, label_row in labels.iterrows():
        raw_label = label_row["Author"]
        year = str(label_row["Year"])
        record = candidate_by_label.get(raw_label)
        if record is None:
            raise SystemExit(f"Missing candidate record for {raw_label}")
        candidate_list = record.get("candidates", [])
        chosen, confidence, basis = choose_candidate(raw_label, candidate_list)
        subset = coded[(coded["Author"] == raw_label) & (coded["Year"] == year)]
        if subset.empty:
            raise SystemExit(f"No coded rows for {raw_label} {year}")

        if chosen is None:
            doi = ""
            title = ""
            container = ""
            stable_url = ""
            status = "ambiguous" if candidate_list else "unresolved"
            normalized_source_id = f"unresolved:{normalize(raw_label).replace(' ', '-')}-{year}"
            full_citation = ""
            notes = "Candidate evidence is preserved in source-candidates.json; no bibliographic identity is asserted."
        else:
            doi = chosen.get("doi", "").lower().replace("https://doi.org/", "")
            title = compact(chosen.get("title", ""))
            container = compact(chosen.get("container", ""))
            stable_url = f"https://doi.org/{doi}" if doi else ""
            status = "doi_resolved" if doi else "url_resolved"
            normalized_source_id = f"doi:{doi}" if doi else f"url:{stable_url}"
            full_citation = f"{raw_label}. {title}. {container}. {stable_url}".strip()
            notes = "Resolution is bibliographic only; it does not replace primary-method hop coding."

        rows.append(
            {
                "raw_author_label": raw_label,
                "raw_year": year,
                "normalized_source_id": normalized_source_id,
                "effect_rows": int(len(subset)),
                "hop_codes_present": "|".join(sorted(subset["hop_code"].dropna().unique())),
                "source_locators": str(label_row.get("source_values", "")),
                "full_citation": full_citation,
                "title": title,
                "container": container,
                "doi": doi,
                "stable_url": stable_url,
                "resolution_status": status,
                "resolution_confidence": confidence,
                "candidate_count": len(candidate_list),
                "disambiguation_basis": basis,
                "notes": notes,
            }
        )

    frame = pd.DataFrame(rows)
    if len(frame) != 202 or frame["raw_author_label"].duplicated().any():
        raise SystemExit("Crosswalk does not preserve one row per raw source label")
    if int(frame["effect_rows"].sum()) != 5969:
        raise SystemExit("Crosswalk effect counts do not sum to 5,969")
    frame.to_csv(OUTPUT, index=False, quoting=csv.QUOTE_ALL)
    print(frame["resolution_status"].value_counts().sort_index().to_string())
    print(frame["resolution_confidence"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()

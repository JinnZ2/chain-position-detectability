# WO-5 source crosswalk: method and coverage

**Prepared:** 19 September 2026

**Scope:** 202 unique `Author`/`Year` labels in the selected plant–soil-feedback release

## Result

The quoted [`source-crosswalk.csv`](source-crosswalk.csv) contains exactly one row for every raw source label and links those rows back to all **5,969** effect records. A conservative automated pass resolves **116 labels to a DOI**, leaves **50 ambiguous**, and leaves **36 unresolved** because no retained exact first-author/year candidate was available. Of the 116 DOI resolutions, 44 have high confidence and 72 have moderate confidence under the rules below. No ambiguous or unresolved label is assigned a guessed citation.

This is a bibliographic crosswalk, not a primary-method coding record. It improves source identity and auditability but does not change the H1/H2/HU codes or prove organism provenance, physical transfer, or experimental design details.

## Evidence assembled

The selected Dryad release contains 5,969 effects and 202 unique raw `Author` labels but no standalone bibliography.[1] The crosswalk workflow therefore assembled:

1. the 202 unique raw labels, years, and extraction locators in [`source-labels.csv`](source-labels.csv);
2. exact first-author/year candidate records from Crossref and OpenAlex;
3. DOI membership in the Jiang synthesis reference list and in two earlier plant–soil-feedback source pools, Xi et al. (2021) and Crawford et al. (2019); and
4. journal suffixes already embedded in some raw labels, such as `Nature`, `Ecography`, `Ecology`, `JE`, `Oikos`, `SBB`, `NP`, `PE`, `CE`, and `PS`.[2] [3] [4]

The compact candidate evidence is preserved in [`source-candidates.json`](source-candidates.json), and the retrieval provenance is summarized in [`source-crosswalk-provenance.md`](source-crosswalk-provenance.md).

## Resolution rules

The deterministic resolver is [`build_source_crosswalk.py`](build_source_crosswalk.py). It applies the following hierarchy:

| Priority | Rule | Confidence |
|---|---|---|
| 1 | An explicit journal suffix in the raw label uniquely matches one exact first-author/year candidate. | High |
| 2 | Exactly one candidate appears in one or more published plant–soil-feedback reference pools. | High |
| 3 | Several candidates appear in source pools, but one has uniquely stronger membership across the three pools. | High |
| 4 | Exactly one exact first-author/year candidate has a plant–soil topical title. | Moderate |
| 5 | More than one plausible candidate remains. | Ambiguous; no citation assigned |
| 6 | No retained candidate exists. | Unresolved; no citation assigned |

The resolver does not select a record merely because it is the only author/year search result if its title is not topically relevant and it has no source-pool or journal-suffix support. It also does not collapse raw labels that may represent different publications. This matters for suffixed entries such as `Bezemer et al. 2006a Ecology` versus `Bezemer et al. 2006b JE` and `Kulmatiski et al. 2011 JE` versus `Kulmatiski et al. 2011 SBB`.

## Output fields

Each row retains the raw label and year, effect-row count, hop codes present, extraction locators, normalized source identifier, full citation, title, journal/container, DOI, stable URL, resolution status, confidence, candidate count, disambiguation basis, and a caution that bibliographic identity does not replace methods coding. Resolved stable URLs use DOI destinations. Unresolved rows receive an explicit `unresolved:` identifier rather than a manufactured publication identity.

## Coverage and limits

| Resolution status | Source labels | Share of 202 labels |
|---|---:|---:|
| DOI resolved | 116 | 57.4% |
| Ambiguous | 50 | 24.8% |
| Unresolved | 36 | 17.8% |
| **Total** | **202** | **100.0%** |

This result is intentionally incomplete. Exact author/year matching cannot safely distinguish some authors with multiple relevant papers in one year. Some release labels refer to original or unpublished contributor data and may not correspond to a citable publication. The public synthesis release does not provide an authoritative one-to-one bibliography. A fully resolved crosswalk would require author confirmation, source-specific supplement inspection, or primary-paper verification for the remaining 86 labels.

The statistical analysis clusters on the release's raw `Author`/`Year` identity and does not depend on the crosswalk's normalized DOI field. Therefore, unresolved bibliography does not change the reproduced estimates. It remains a provenance limitation and should be completed before any claim that depends on primary-study methods or source deduplication.

## Reproduction

From the repository root:

```bash
python3 research/wo-5/build_source_crosswalk.py
```

The script requires pandas and the repository-pinned analysis environment. It validates exactly 202 source rows, unique raw labels, and an effect-row total of 5,969 before writing the crosswalk.

## References

[1]: https://doi.org/10.5061/dryad.n2z34tn35 "Dataset of global plant-soil feedback"

[2]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

[3]: https://doi.org/10.1111/1365-2745.13731 "Xi et al. plant–soil feedback synthesis"

[4]: https://doi.org/10.1111/ele.13278 "Crawford et al. plant–soil feedback meta-analysis"

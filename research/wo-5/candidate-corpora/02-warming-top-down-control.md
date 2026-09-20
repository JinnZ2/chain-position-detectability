# WO-5 candidate-corpus audit: warming and top-down control

**Candidate ID:** `warming-top-down-control`
**Audit finding:** **Not eligible at this audit stage; not recommended.** The underlying corpus is unusually strong on public, machine-readable effect-size data, uncertainty, source identifiers, and experimental venue. It has **175 synthesis-selected usable interactive-effect estimates** (and all 177 rows have a finite `gI` and positive `var_gI`). However, the inspected public files establish only one unique WO-5 hop category: the 138 field rows are `H1`. The 39 rows labelled `laboratory` cannot be assigned uniquely to `H2` versus `H3` from the CSV/README alone. Under the preregistered rule, missing provenance is `HU`, not `H3`. Therefore the required second category with at least ten estimates is **plausible but unverified**, and the literal audit score is **8/11**, not a score that assumes laboratory rows are a qualifying category.

This is a **strict, file-inspection result**, not a judgment that the corpus could not become eligible. The 39 laboratory rows span 20 identified source studies. If primary-study methods show field-origin material moved to a controlled setting (`H2`) or controlled/laboratory history (`H3`) for at least 10 of those rows, the minimum two-category criterion will be met alongside `H1` (138 rows). That work remains mandatory: the codebook prohibits treating missing provenance as `H3` and prohibits final coding by automated rules alone.[1]

## Identity correction and scope

The candidate supplied the paper URL `https://doi.org/10.1007/s00442-017-4011-3`. It is **not the DOI of the title-matched article**: a direct Crossref lookup for that DOI returned HTTP 404 during this audit. The matching peer-reviewed article is Marino, Romero, and Farjalla, *Geographical and experimental contexts modulate the effect of warming on top-down control: a meta-analysis*, **Ecology Letters 21(3):455–466 (2018), DOI `10.1111/ele.12913`**. PubMed identifies it as both “Journal Article” and “Meta-Analysis” and links its Figshare accession `10.6084/m9.figshare.5702812.v1`.[2] [3]

The public Figshare record is a CC BY 4.0 dataset, status `public`, with downloads enabled. Its title has the singular “context,” while the published article has “contexts.” The landing-page description says the file contains all data used for the paper, but no score below is awarded solely on that description: both delivered files were downloaded and inspected.[4]

## Files inspected and reproducibility record

| Public artifact | Exact filename / identifier | Direct inspection result |
|---|---|---|
| Figshare tabular data | `ELE-01230-2017_-_data.csv` (45,022 bytes; Figshare file ID 9996319) | Parsed successfully as a comma-separated table with **177 rows × 33 columns**. Figshare reports MD5 `f78f2cdd5a812a7e626ac8f11bde73d8`; downloaded-file SHA-256 was `120f229c6c5c131a2cf64e1e5dd5d7fc6e94dce8d1d04f5d41793567f0a5d2a5`. |
| Figshare data documentation | `README_-_ELE-01230-2017_-_metadata.docx` (29,705 bytes; file ID 9996331) | DOCX XML extracted and read. It defines the CSV fields, effect-size orientation, and `experimental_venue`. |
| Preregistered codebook | `research/wo-5/ecology-codebook.md`, repository commit `3564d68ab9218ba1569f8e404d0c5dd3d68a3d90` | Read from the public repository at the pinned commit. It supplies the eligibility rule, score, and `H0`–`H3`/`HU` definitions.[1] |
| Publication record | PubMed PMID `29368449`; Crossref DOI `10.1111/ele.12913` | Inspected to verify the peer-reviewed article identity, publication type, journal, DOI, and Figshare accession.[2] [3] |

## What the inspected CSV contains

The CSV has no missing values in any of its 33 columns and no exact duplicate rows. The row unit is unambiguously study-level effect data: the README states:

> “Each row represents an observation from a consumer-resource pair analyzed in one experiment and reported in a given study.”[5]

The data column is named `id_estudo`, although the README calls its corresponding field `study_id`. This documentation/header naming mismatch is a minor reproducibility defect, not an identifier failure: `id_estudo` is complete, has **56 unique values**, and has a one-to-one mapping to the 56 unique (`first_author`, `year`, `journal`) triples in the CSV. The README describes it as: “Each number represents a unique identifier to an independent study.”[5]

### Exact fields supporting the effect-size analysis

| Requirement | Inspected CSV fields and evidence | Audit result |
|---|---|---|
| Native outcome | `gI` is complete (177/177 finite values). `gC` and `gW` are also complete. | **Yes** |
| Outcome meaning and direction | README: `gI` is the factorial Hedges’ *g* interaction of warming and top-down control on resource biomass; positive means warming strengthens top-down control and negative means it weakens it. | **Yes** |
| Sampling uncertainty | `var_gI` is complete and strictly positive for all 177 rows (range 0.1374–2.2593). `var_gW` and `var_gC` are also complete and strictly positive in all rows. README explicitly calls each `var_g*` field the variance of its paired `g*`. | **Yes** |
| Synthesis-selected usable effect rows | `mixed_model_gI` is `TRUE` for **175** rows and `FALSE` for 2; `overall_effect_gI` is `TRUE` for 176. Conservatively, this audit counts **175** `gI`/`var_gI` rows as usable because they were used in the synthesis’s mixed-effects model. | **Yes; 175 ≥ 80** |
| Source-study identifier | Complete `id_estudo`; 56 unique IDs. | **Yes** |
| Primary-study traceability | Complete `first_author`, `year`, and `journal`; the triple creates 56 unique, one-to-one source-study groups, matching `id_estudo`. The tuple is sufficient to retrieve a primary citation, though the data file does not supply title, volume/pages, or a per-row DOI. | **Yes, with a metadata limitation** |
| Experimental-setting field | Complete categorical `experimental_venue`, values `field` and `laboratory`. README: “Describes whether the experiment was conducted in the field or in the laboratory (greenhouse studies included).” | **Yes** |

The full CSV header is:

```text
id_estudo, first_author, year, journal, consumer_ID, resource_ID,
warming_changes, ecosystem_type, nutrient_addition, number_trophic_levels,
experimental_venue, consumer_type, consumer_thermoregulation_strategy,
resource_mobility, consumer_foraging_strategy, openness,
resource_generation_time, resource_trophy, experimental_duration,
mean_annual_temperature, intensity_experimental_warming, gW, var_gW,
gC, var_gC, gI, var_gI, overall_effect_gC, mixed_model_gC,
overall_effect_gW, mixed_model_gW, overall_effect_gI, mixed_model_gI
```

The three `g*`/`var_g*` pairs meet the codebook’s native-metric condition: the codebook retains a zero-centred metric when it has sampling variance, but says metrics that cannot be made commensurate must be analyzed separately.[1] For this candidate, `gI` is the appropriate primary outcome because it directly measures the warming × top-down-control interaction; `gC` and `gW` should not be silently pooled with it.

## Counts, setting distribution, and hop-category assessment

The `experimental_venue` field has no missing values and the exact distribution is **138 `field` rows** and **39 `laboratory` rows**. These correspond to 36 and 20 independent source-study IDs, respectively; no source-study ID appears in both venue values. Every venue row has a finite `gI` and positive `var_gI`. The corpus also covers terrestrial (61 rows), marine (59), and freshwater (57) systems.

The README says the synthesis concerns temperature “experimentally increased.” Consequently, `field` is enough to assign the 138 rows to **`H1` (observed or manipulated field)** provisionally and at high confidence: field organisms remain in field/semi-natural conditions while researchers impose warming. It is not sound to label them `H0`, because `H0` requires ambient/naturally occurring exposure, whereas the corpus’s exposure is experimental warming.[1] [5]

The `laboratory` label is not a hop category. It explicitly combines laboratory and greenhouse studies but contains no field-origin/provenance field, collection location, culture history, or information on when organisms were moved. Thus it does not resolve the codebook’s decisive distinction:

> “Greenhouses and common gardens are `H2` for field-origin organisms. A study is `H3` only when controlled history is supported; missing provenance is `HU`, not `H3`.”[1]

The current **conservative category estimate** is therefore:

| Code / provisional status | Estimate count | Independent source studies | Basis and status |
|---|---:|---:|---|
| `H1` | **138** | 36 | Direct `experimental_venue = field` plus experimental warming; one populated qualifying category. |
| `H2` | 0 confirmed | 0 confirmed | Could occur among laboratory/greenhouse records, but field origin and relocation are absent from the dataset. |
| `H3` | 0 confirmed | 0 confirmed | Could occur among laboratory records, but controlled/laboratory history is absent from the dataset. |
| `HU` (laboratory rows pending primary-method coding) | **39** | 20 | Literal codebook treatment until a primary source provides decisive provenance/method evidence. |
| `H0` | 0 expected | 0 expected | Incompatible with the corpus’s experimental warming framing. |

This makes the threshold calculation clear. The data unquestionably offer **175 usable effects**, well above 80. They also make a second qualifying category **plausibly available**: only one of `H2` or `H3` needs at least 10 of the 39 pending laboratory rows. But `H2`/`H3` cannot be awarded on the `laboratory` label alone. The codebook requires two independent coders, decisive source passages/metadata, reconciliation against public primary study or synthesis metadata, and `HU` if ambiguity remains.[1] The threshold of “at least ten estimates in each of two categories after coding” is therefore not yet verified.[1]

## Literal eligibility and score

The codebook requires public downloadable data, a peer-reviewed ecological synthesis, study-level effect estimates or reconstructable effects, uncertainty or sample-size information, source identifiers, metadata capable of at least two hop categories, at least 80 usable estimates, and at least ten estimates in each of two categories after coding.[1] The underlying title-matched paper is peer-reviewed in *Ecology Letters*, and its public Figshare data are downloadable without credentials.[2] [4]

| Scored criterion | Points | Literal audit evidence |
|---|---:|---|
| Public machine-readable data | 1 | Inspected public CSV, not merely landing-page description. |
| Effect estimate | 1 | Complete `gI` (also `gC`, `gW`) with documented Hedges’ *g* definitions. |
| Sampling variance or reconstructable uncertainty | 1 | Complete positive `var_gI` (also `var_gC`, `var_gW`). |
| Source-study identifier | 1 | Complete `id_estudo`, 56 unique IDs. |
| Traceable primary-study citation | 1 | Complete one-to-one `first_author` + `year` + `journal` metadata for 56 sources; not a full citation/DOI but traceable. |
| At least 80 usable effects | 1 | 175 rows with `mixed_model_gI = TRUE`; all 177 have usable numeric `gI`/positive `var_gI`. |
| Explicit experimental-setting field | 1 | Complete `experimental_venue` with documented field/laboratory values. |
| Populated `H1` category | 1 | 138 field experimental-warming effects. |
| Additional populated hop categories | 0 | `H2`/`H3` cannot be assigned from inspected public dataset documentation alone; laboratory rows remain `HU` pending source-method coding. |
| **Total** | **8 / 11** | One confirmed hop category only. |

**Eligibility: false for the present audit.** The candidate is not excluded for a data-quality failure; it fails the codebook’s minimum-category condition *until* the 39 laboratory records are coded from primary methods and a second category reaches 10. It should be retained as a high-priority **conditional** candidate, not selected or described as eligible yet.

**Recommended: false.** The data backbone is strong, but “recommended” is reserved for a candidate that is both eligible and genuinely strong. The supplied DOI mismatch and unverified `H2`/`H3` allocation mean this candidate does not meet that standard now.

## Critical limits and required next verification

1. **The candidate paper URL is wrong.** Any downstream record must replace `10.1007/s00442-017-4011-3` with `10.1111/ele.12913`; the former could not be confirmed as the claimed paper.
2. **Laboratory is a setting label, not a unique hop code.** The public dataset has no organism provenance/history field. Do not score all 39 as `H2`, `H3`, or both merely because they are labelled laboratory; the README expressly includes greenhouse studies in the same label.[5]
3. **Minimum category counts are unverified, not disproved.** Retrieve and independently code the 20 laboratory primary studies identified by `id_estudo` and the unique (`first_author`, `year`, `journal`) tuple. Record a decisive methods quotation, provenance confidence, and all inherited row IDs for each coding group. Assign `HU` when evidence cannot distinguish field-origin relocation from controlled history.[1]
4. **Traceability is adequate but not ideal.** Add a source-citation table containing title, DOI/URL, and full reference linked to `id_estudo`. The CSV’s author-year-journal tuples are complete and one-to-one, but do not themselves preserve a full bibliographic citation.
5. **Use the stated interaction metric.** Treat `gI`/`var_gI` as the primary outcome. Do not combine the warming main effect (`gW`) or consumer-control main effect (`gC`) with `gI`; the dataset README defines them as different estimands.[5]
6. **Source clustering matters.** The 175 selected effects arise from 56 independent source-study IDs, with 1–24 effect rows per study. Analysis must retain `id_estudo` for clustered inference as the codebook requires.[1]

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/3564d68ab9218ba1569f8e404d0c5dd3d68a3d90/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook (pinned preregistration)"

[2]: https://pubmed.ncbi.nlm.nih.gov/29368449/ "PubMed PMID 29368449 — Geographical and experimental contexts modulate the effect of warming on top-down control: a meta-analysis"

[3]: https://api.crossref.org/works/10.1111/ele.12913 "Crossref work record for Marino, Romero, and Farjalla, Ecology Letters 21(3):455–466"

[4]: https://api.figshare.com/v2/articles/5702812 "Figshare public API record for Data from: Geographical and experimental context modulate the effect of warming on top-down control: a meta-analysis.csv"

[5]: https://ndownloader.figshare.com/files/9996331 "README_-_ELE-01230-2017_-_metadata.docx"

[6]: https://ndownloader.figshare.com/files/9996319 "ELE-01230-2017_-_data.csv"

[7]: https://doi.org/10.1007/s00442-017-4011-3 "Candidate-supplied DOI (does not match the title-matched article)"

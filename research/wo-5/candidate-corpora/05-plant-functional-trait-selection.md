# WO-5 candidate audit: plant functional trait selection

**Candidate ID:** `plant-functional-trait-selection`
**Decision:** **Eligible; recommended as a strong candidate**
**Literal score:** **9/11**
**Audit date:** 2026-09-19

## Conclusion

This corpus clears the preregistered eligibility threshold. Direct inspection of the downloaded master experimental workbook and observational workbook found **1,714 usable study-level effect estimates**: 1,242 standardized directional selection gradients (β) and 472 standardized directional selection differentials (S). Here, “usable” means that an effect value and a positive standard error (SE) are both present; sampling variance is reconstructable as `SE²`. The count deliberately uses the experimental **master** file, not the duplicated analytical file.

The public metadata supports two conservative, non-overlapping usable hop categories without inferring field origin where it is absent. The observational file contains **629** usable effects in explicitly **in situ natural populations** from studies described by its README as unmanipulated; these are `H0` under the codebook. The experimental master file contains **161** usable effects in explicitly **in situ natural populations**; because its README says that this file concerns experiments that manipulate the environment, these are `H1`. Both categories exceed ten effects by a wide margin. The controlled-setting codes are not enough to distinguish field-origin common-garden work (`H2`) from controlled-history/lab-only work (`H3`), so all 924 such effects are conservatively `HU`, not awarded as an additional populated category.

The source data provide effect estimates, SEs, source-paper IDs, and bibliographic fields sufficient to retrieve primary reports. The setting fields are explicit and their category definitions are included in each workbook’s data dictionary. The parent synthesis is a 2020 journal article in the *International Journal of Plant Sciences*, whose publisher describes the journal as peer reviewed. The Dryad release is public and CC0. These findings satisfy the codebook’s public-access, peer-review, data-structure, uncertainty, traceability, minimum-count, and two-category requirements. [1] [2] [3] [4]

## Corpus and file inspection

The Dryad landing page names four public files and links the dataset to the primary article DOI `10.1086/706199`. I downloaded each file through the public browser download links, verified the bytes against Dryad’s API-listed SHA-256 digest, and opened the files. The repository is a public CC0 release. The primary article is recorded by Crossref as a `journal-article`, *International Journal of Plant Sciences* 181(1):44–55 (2020). [2] [3]

| File inspected | Dryad file ID | Type and role | Rows in data sheet | SHA-256 verified against Dryad API |
|---|---:|---|---:|---|
| `Dryad_ReadMe.docx` | 174509 | README/data-package description | n/a | Yes |
| `Plant_functional_traits_experimental_database_master_Dryad.xlsx` | 174506 | **Used for counts**; unique experimental database | 572 data rows | Yes |
| `Plant_functional_traits_experimental_database_duplicated_Dryad.xlsx` | 174507 | Experimental analysis convenience file; **not used for counts** | 1,014 data rows | Yes |
| `Plant_functional_traits_observational_database_Dryad.xlsx` | 174508 | Observational database | 815 data rows | Yes |

The README confirms that the experimental and observational databases include only records reporting directional gradients and/or differentials with their associated SEs. It also states that the duplicated experimental file contains records duplicated to facilitate the manuscript analyses:

> “Only records that report directional selection gradients and/or differentials, as well as their associated standard errors, are included.”
>
> “To facilitate the analyses reported in the associated manuscript, some records of selection have been duplicated.”

The master file was therefore used to avoid a known duplication mechanism. The README describes the observational database as estimates from “observational studies in unmanipulated environments” and the master experimental database as studies that “manipulate the environment and measure selection.” Those statements are used only in conjunction with the inspected row-level setting fields, not in place of them. [2]

## Directly observed columns and their evidentiary role

The experimental master workbook’s `Database` sheet has 572 rows and 26 columns. Its row-level fields include `Paper ID`, `authors`, `pub.year`, `journal`, `vol.page`, `experimental.context`, `grad.linear.value`, `grad.linear.se`, `diff.linear.value`, and `diff.linear.sterr`. Its `Sheet1` data dictionary defines `Paper ID` as “Generic identifier for each paper”; `experimental.context` as “A = indoor controlled environment; B = outdoor semi-controlled environment; C = in situ natural population”; the gradient and differential fields as standardized directional selection estimates; and their respective SE fields as SEs.

The observational workbook’s `Database` sheet has 815 rows and 28 columns, including `StudyID`, `Authors`, `Pub.Year`, `Journal`, `Vol:p-p`, `Population`, `Study context`, `Grad.linear.value`, `Grad.linear.StErr`, `Diff.linear.value`, and `Diff.linear.StErr`. Its `Column coding` worksheet defines `StudyID` as “Generic identifier for each paper”; `Study context` as “B = indoor or outdoor controlled environment; C = in situ natural population”; and the four outcome fields as standardized selection gradients/differentials and their SEs.

The remaining columns preserve useful grouping and design detail. Examples include experimental `within.study.id`, `generic.population`, `generic.treatment`, `agent.selection.defined`, `treatment.defined`, species, trait class, and fitness component; and observational `Generic.Dataset`, `Generic Population`, collection `Year`, `Population`, species, trait class, and fitness component. These support clustered modeling and later source-method review, although they do not alone settle every controlled-setting hop code.

## Effect and uncertainty counts

The count treats each nonmissing β or S field with a positive accompanying SE as one effect estimate. This follows the codebook’s unit—one effect estimate in the synthesis—and preserves both native, zero-centered standardized selection metrics separately rather than pooling them. Sampling variance is reconstructable exactly as `SE²` for every counted effect. [1]

| Data source | β with estimate + positive SE | S with estimate + positive SE | Total usable effects | Relevant setting distribution among usable effects |
|---|---:|---:|---:|---|
| Experimental master | 483 | 250 | 733 | A: 261; B: 311; C: 161 |
| Observational | 759 | 222 | 981 | B: 352; C: 629 |
| **Pooled, counting β and S separately** | **1,242** | **472** | **1,714** | A: 261; B: 663; C: 790, where the C rows are separated by study type below |

The per-setting totals in the table are effects, rather than physical spreadsheet rows, because a row can contain both β and S. All reported effect values in the master and observational workbooks had positive nonmissing SEs whenever the respective effect was nonmissing: 483/483 β and 250/250 S in the master file, and 759/759 β and 222/222 S in the observational file. Thus no imputation or interval reconstruction is necessary.

## Source-study identity and primary-study traceability

Source identity is present at the row level but is workbook-scoped: `Paper ID` has 43 unique values in the experimental master file, and `StudyID` has 74 in the observational file. These IDs must therefore be carried with a dataset indicator. Neither should be treated as globally unique after the two databases are joined.

Primary traceability is stronger than an opaque ID. Every row in both analyzed workbooks has nonblank author, publication year, journal, and volume/page fields. Across the two workbooks, these form **99 unique normalized bibliographic signatures** (44 experimental and 76 observational signatures, with 21 appearing in both files). The source bibliographic fields are therefore sufficient to locate a primary paper; the 99 count is the conservative cross-file citation-signature count used here as the available independent-source-study count. It is not an assertion that all 99 papers are statistically independent designs.

For the conservative usable categories specifically, `H0` contains 42 citation signatures (41 observational `StudyID`s) and `H1` contains 15 citation signatures (15 experimental `Paper ID`s). Eleven citation signatures occur in both `H0` and `H1`, so a future clustered model must use the reconciled source-paper identity rather than treating category-specific source counts as additive.

## Hop coding under the published definitions

The codebook defines `H0` as organisms remaining in a naturally occurring population/community with ambient or naturally occurring exposure and an in-situ response. It defines `H1` as organisms remaining in field or semi-natural conditions while researchers impose a treatment or related field intervention before response measurement. It reserves `H2` for field-origin organisms or material moved to a controlled setting, and requires `HU` if public metadata cannot uniquely resolve the category. [1]

| Operational category | Evidence inspected | Effect counts (β; S; total) | Available source studies | Audit treatment |
|---|---|---:|---:|---|
| `H0` — lived-in field | Observational README: unmanipulated environments; `Study context = C`: in situ natural population | 511; 118; **629** | 42 citation signatures; 41 scoped IDs | Populated and awarded |
| `H1` — observed or manipulated field | Experimental README: experiments manipulate environment; `experimental.context = C`: in situ natural population | 113; 48; **161** | 15 citation signatures; 15 scoped IDs | Populated and awarded |
| `H2` — sampled to controlled setting | No row-level provenance field states that controlled-setting organisms/material originated in the field and were moved before focal response | 0 confirmed | 0 confirmed | Not awarded |
| `H3` — controlled-history/lab-only | No history/provenance field establishes controlled or laboratory-reared history | 0 confirmed | 0 confirmed | Not awarded |
| `HU` — unresolved | Experimental A/B and observational B identify controlled or semi-controlled context but do not establish field origin, relocation, or prior controlled history | 618; 306; **924** | 57 citation signatures; 65 scoped IDs | Retained as unresolved; excluded from category qualification |

The `H0` and `H1` interpretations are deliberately narrow. The setting dictionary independently establishes that C is “in situ natural population”; the README establishes whether the underlying database is unmanipulated observational or environmental manipulation. This supports the two field categories under the codebook. Conversely, it would be a codebook violation to call all indoor/outdoor controlled work `H2`: a common garden is `H2` only for field-origin material, whereas controlled-history work is `H3`, and missing provenance is `HU`. The supplied files lack an origin/history field. [1]

## Literal score and eligibility

| Published scoring criterion | Finding from inspected files | Point |
|---|---|---:|
| Public machine-readable data | Four public files; three structured `.xlsx` workbooks were downloaded, verified, and opened | 1 |
| Effect estimate | Direct standardized β and S value columns in both analyzed workbooks | 1 |
| Sampling variance or reconstructable uncertainty | Direct SE columns paired with all counted effects; variance = `SE²` | 1 |
| Source-study identifier | `Paper ID` and `StudyID`, defined in the respective data dictionaries as paper identifiers | 1 |
| Traceable primary-study citation | Row-level author, publication year, journal, and volume/page fields; 99 normalized signatures | 1 |
| At least 80 usable estimates | 1,714 estimate-and-SE pairs | 1 |
| Explicit experimental-setting field | `experimental.context` and `Study context`, both with explicit category dictionaries | 1 |
| Populated hop category | `H0`: 629 effects | 1 |
| Populated hop category | `H1`: 161 effects | 1 |
| `H2`/`H3` additional categories | Not confirmed from supplied metadata | 0 |
| **Total** | **7 base points + 2 populated categories** | **9/11** |

**Eligibility:** Yes. The corpus is associated with a peer-reviewed ecological synthesis, has public downloadable study-level data, preserves uncertainty and source traceability, contains far more than 80 usable effects, and plausibly supplies at least ten effects in each of two conservatively coded categories. [1] [2] [3] [4]

**Recommendation:** **True.** This is genuinely strong for WO-5 because its field-category evidence is explicit, it retains a large quantity of effect-and-SE pairs, it preserves paper-level clustering variables and bibliographic traceability, and both verified field categories greatly exceed the minimum. The recommendation does not depend on unverified controlled-setting classifications.

## Critical limits and required handling in any downstream analysis

The primary limitation is controlled-setting provenance. The public workbooks distinguish indoor controlled, outdoor semi-controlled, and in-situ natural populations, but do not say whether controlled organisms, propagules, or tissue were field-origin or laboratory-history. Therefore `H2` and `H3` cannot be assigned from these files alone. A later coding stage would need accessible primary methods passages and a source-linked reconciliation record; automated setting-string rules cannot resolve this.

The master and observational files overlap: 21 of 99 bibliographic signatures occur in both, and 11 occur in both confirmed `H0` and `H1`. Paper IDs are not cross-file identifiers. A derived analysis must construct a reconciled citation key and cluster at least by that source study; it must not sum the 41 and 15 category-specific source-ID totals as if independent.

The corpus contains two different native outcomes—β, a direct standardized selection gradient, and S, a standardized selection differential that can include indirect selection. The codebook requires retaining noncommensurate native metrics separately rather than pooling merely by relabeling. Any later model should therefore analyze β and S separately, or explicitly justify an outcome-specific model, while using `SE²` as the within-estimate variance. [1]

The experimental duplicated workbook contains 1,014 rows and was intentionally not used for availability counts, because the README expressly documents duplicated selection records. The counts reported here are reproducible from 572 master experimental rows plus 815 observational rows. The present audit establishes eligibility and availability; it is not a completed independent primary-method hop coding exercise.

## Reproducibility record

The audit downloaded the public files on 2026-09-19. The actual downloaded SHA-256 values matched the Dryad API metadata: `a1f01f3d9baed500f959b58e3b65d623bdfbd40a69b7707e62ff35ff9c7b853b` for `Dryad_ReadMe.docx`; `b03dc481874655d747f59ea41cc4c558b0a1fe5fcf6cebf6f942e6b65b9c6b73` for the experimental master file; `9889b99fbe525dd71612c247ffb867d6d2c5d560cb51077dc46f0816b718ad5f` for the duplicated experimental file; and `b36fea1e7631673b7e6eba777a16be19b554ef0cf28b0d77ddcb7060d39f03f9` for the observational file.

The deterministic inspection and counting inputs were preserved in the audit job workspace: `/home/ubuntu/jobs/bb2dd2ddab53_a5/inspect_workbooks.py`, `/home/ubuntu/jobs/bb2dd2ddab53_a5/analyze_corpus.py`, and `/home/ubuntu/jobs/bb2dd2ddab53_a5/corpus-analysis.json`. The report is the required durable artifact; the job workspace is supporting provenance rather than a repository modification.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"
[2]: https://datadryad.org/dataset/doi:10.5061/dryad.sn02v6x0q "Dryad dataset: A meta-analysis of natural selection on plant functional traits"
[3]: https://api.crossref.org/works/10.1086/706199 "Crossref metadata: A Meta-analysis of Natural Selection on Plant Functional Traits"
[4]: https://www.journals.uchicago.edu/journals/ijps/about "International Journal of Plant Sciences: About the Journal"

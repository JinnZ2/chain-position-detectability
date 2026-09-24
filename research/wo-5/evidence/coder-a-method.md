# Coder A methods record: WO-5 plant–soil-feedback hop coding

## Result

**Coder A** independently coded all **5,969** effect-estimate rows in the supplied WO-5 plant–soil-feedback dataset. The conservative decision rules yielded **326 H1** records, **1,197 H2** records, and **4,446 unresolved** records. No row was coded H0 or H3. The output keeps all 28 original input fields, appends six coding fields, preserves the input row order, and uses a blank `hop_score` for HU because unresolved records have no defensible ordinal score.

| Hop category | Meaning in this coding pass | Rows | Share of 5,969 rows | Distinct source studies* |
|---|---:|---:|---:|---:|
| H0 | Lived-in field | 0 | 0.0% | 0 |
| H1 | Field conditioning and field experimental feedback | 326 | 5.5% | 23 |
| H2 | Field conditioning followed by greenhouse feedback | 1,197 | 20.1% | 91 |
| H3 | Controlled-history or lab-only | 0 | 0.0% | 0 |
| HU | Unresolved | 4,446 | 74.5% | 99 |
| **Total** | **All retained input rows** | **5,969** | **100.0%** | **202** |

*Source study is the retained `(Author, Year)` identifier. A source study can contribute estimates to more than one category, so category-specific study counts do not sum to the total.

## Materials, scope, and unit

The unit of coding was one row/effect estimate in `PSF.data.EL.open.csv`, using the supplied `N` as the immutable row identifier. I used only the supplied raw file and the supplied preregistered codebook; I did not inspect or use another coder’s output. The raw input had SHA-256 `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c`. The exported quoted CSV has SHA-256 `9fcbb27b49169c3d7737f1306dc3dc80f8d5245369219534c41cef844c58a9d8`.

The coding decision used the three phase metadata fields named in the request: `Phase1.m.ori`, `Phase1.m`, and `Experimental.setting`. `Phase1.m.ori=Field` and `Phase1.m=Field` were treated jointly as direct support for a field conditioning phase. `Experimental.setting` was treated as the recorded feedback-response setting. Neither `F.H`, `group`, nor a venue word elsewhere in the record was used to infer an unrecorded phase direction or organism history. This implements the codebook’s relocation-and-provenance distinction rather than a venue-only classification [1].

## Deterministic rule table

| Inherited rule ID | Required metadata pattern | Code / score | Provenance confidence | Rows | Source studies | Decisive basis recorded in CSV |
|---|---|---|---|---:|---:|---|
| `H1-FIELD-CONDITIONING-FIELD-FEEDBACK` | `Phase1.m.ori=Field`; `Phase1.m=Field`; `Experimental.setting=Field` | H1 / 1 | High | 326 | 23 | The three literal metadata values. |
| `H2-FIELD-CONDITIONING-GREENHOUSE-FEEDBACK` | `Phase1.m.ori=Field`; `Phase1.m=Field`; `Experimental.setting=Greenhouse` | H2 / 2 | High | 1,197 | 91 | The three literal metadata values. |
| `HU-UNRESOLVED-PHASE-DIRECTION` | Every other metadata pattern | HU / blank | Low | 4,446 | 99 | The available values plus the statement that they do not establish a unique transfer/history. |

The rules were applied row by row, although repeated rows with the same pattern carry the same inherited rule identifier. The `decisive_basis` cell stores the direct values used in the decision. The inherited identifier therefore records reproducible group-level logic without suppressing row-level provenance.

## Ambiguities resolved conservatively

Rows whose conditioning metadata were greenhouse-labelled but whose `Phase1.m.ori` value was a numeric duration were not assumed to have field-origin material. That pattern cannot establish the physical field-to-controlled relocation needed for H2. It also cannot establish the controlled or laboratory-reared history required for H3. Those records are HU even when an experimental setting is labelled greenhouse.

A field `Experimental.setting` by itself was not enough for H1. H1 was assigned only if both conditioning metadata fields were explicitly `Field` and the feedback setting was explicitly `Field`. Thus **282** field-feedback rows remain HU because their conditioning/provenance direction was not supported by the required field pattern. Similarly, a greenhouse label alone was not used to assign H3, and no row was called H0 because the supplied records describe experimental feedback contrasts rather than an ambient lived-in contrast with an in-situ response.

These decisions intentionally prioritize non-overclaiming. A future reconciliation may consult traceable primary-study methods if it needs to resolve the HU records, but this independent pass does not replace missing phase-direction evidence with an assumption.

## Source-study coverage

The full coding file has **202** distinct `(Author, Year)` source-study identifiers. H1 is represented by 23 source studies; H2 by 91; and HU by 99. Illustrative source identifiers in each nonempty category are shown below solely to make the grouping auditable; every row remains identifiable in the CSV by `N`, `Author`, and `Year`.

| Category | Example source-study identifiers (up to ten, alphabetical) |
|---|---|
| H1 | Bayandala et al. 2016 (2016); Casper and Castelli 2007 (2007); Chung,2019 (2019); Dickie et al. 2007 (2007); Ehlers and Thompson 2004 (2004); Heinze,2016 (2016); Heinze,2019 (2019); Heinze,2020 (2020); Heinze-Joshi,2018 (2018); Hemrova,2016 (2016); … |
| H2 | Ai et al. 2018 (2018); Bajpai et al. 2013 (2013); Bakker,2013 (2013); Beckstead and Parker 2003 (2003); Belnap et al. 2005 (2005); Bennett et al. 2017 (2017); Blank and Sforza 2007 (2007); Bodelier et al. 2006 (2006); Bonanomi et al. 2005 PE (2005); Callaway et al. 2004b Nature (2004); … |
| HU | Agrawal et al. 2005 (2005); Aguilera et al. 2017 (2017); Aldorfova,2020 (2020); Allen et al. 2021 (2021); Batten et al. 2008 (2008); Bauer,2017 (2017); Beck, 2021 (2021); Bergmann et al. 2016 (2016); Bever 1994 (1994); Bezemer et al. 2006a Ecology (2006); … |

## Integrity validation

The automated validation completed successfully before this record was written. The input and output each contain **5,969** data rows. `N` is populated and unique in both files, with the same order in output as input. Every original field was compared value-for-value after re-reading the output; all 28 original columns were preserved. All **5,969** `rr` values are finite. All **5,969** `var` values are finite and strictly positive. The output uses CSV `QUOTE_ALL`, so its header and every field value are quoted.

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/work-orders/WO-5-hop-distance-and-pre-entry-loss.md "WO-5 — Hop distance and pre-entry loss in reporting chains"

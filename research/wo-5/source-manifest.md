# Source retrieval and checksum manifest

**Manifest date:** 19 September 2026
**Corpus ID:** `global-plant-soil-microbe-interactions`
**Dataset title:** *Dataset of global plant-soil feedback*
**Associated publication:** Jiang, F., Bennett, J. A., Crawford, K. M., Heinze, J., Pu, X., Luo, A., & Wang, Z. (2024). “[Global patterns and drivers of plant–soil microbe interactions](https://doi.org/10.1111/ele.14364),” *Ecology Letters*, 27, e14364.
**Dataset DOI:** [10.5061/dryad.n2z34tn35](https://doi.org/10.5061/dryad.n2z34tn35)

## Retrieval record

The selected release is the publicly downloadable Dryad **version 6**, with publication date **18 December 2023**. On 19 September 2026, the release was retrieved through Dryad’s public version-download endpoint, which returned a ZIP delivery bundle containing the CSV and two ancillary files. The primary machine-readable dataset is a single CSV; it was extracted and copied byte-for-byte to the required raw-input location with its native extension. Its local permission mode is `0444` (read-only) to guard against accidental modification. The SHA-256 was recomputed after installation and matches Dryad’s file-inventory digest exactly.

| Role | Exact repository filename | Local preserved filename/path | MIME/type | Repository size | Row count | SHA-256 | Verification |
|---|---|---|---|---:|---:|---|---|
| **Primary machine-readable effect dataset** | `PSF.data.EL.open.csv` | [`analysis/raw-source-data/PSF.data.EL.open.csv`](analysis/raw-source-data/PSF.data.EL.open.csv) | `text/csv` | 1,609,518 bytes | **5,969 data rows**; 1 header row; 28 columns | `bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c` | **Match** between recomputed local SHA-256 and Dryad version-API inventory |
| Ancillary release documentation; not copied as primary raw data | `README.md` | Not separately preserved in `raw-source-data`; read from the retrieved release bundle | `text/markdown` | 1,508 bytes | n/a | `1aeac2d8f58027687422a1336aaa4b9ca6f82cc5c357f6e92fc50db52ad2484b` | Repository-supplied SHA-256 recorded |
| Ancillary analysis script; not copied as primary raw data | `Open_code.R` | Not separately preserved in `raw-source-data`; read from the retrieved release bundle | R source | 32,984 bytes | n/a | `16cd8520a2072592070822db4d72ebce1db483b4cedca8f2797d855c52b5e2bd` | Repository-supplied SHA-256 recorded |

**Row-count method:** the installed CSV was counted as physical records excluding the one header line (`5,970` lines total minus one header). The count agrees with the article and repository statement that the compilation contains 5,969 observations.

## Immutable local raw input

```text
/home/ubuntu/chain-position-detectability/research/wo-5/analysis/raw-source-data/PSF.data.EL.open.csv
```

```text
SHA-256  bb56ba5ac31b13be09cf3df42c1215b53255bb1eb3bb8a91838ab8cb4cb5c82c
Mode     0444 (-r--r--r--)
Bytes    1609518
Rows     5969 data rows; 28 columns
```

The primary CSV is the only required data-table artifact for this selected corpus. It is therefore retained directly as a `.csv`, rather than creating a ZIP that would add an unnecessary container and obscure direct use. The Dryad bundle’s `README.md` and `Open_code.R` are documented above as supporting release materials and their repository checksums are retained for provenance.

## Public source locations and release metadata

| Purpose | Public URL | Release/version relationship |
|---|---|---|
| Dataset landing page and human-readable citation | <https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35> | Dataset DOI record; identifies version 6 as published 18 Dec 2023 |
| Dataset API metadata | <https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.n2z34tn35> | Confirms the stated license and dataset-level metadata |
| Version API record | <https://datadryad.org/api/v2/versions/269740> | Public Dryad version ID `269740`; `versionNumber: 6`; `publicationDate: 2023-12-18` |
| Version file inventory | <https://datadryad.org/api/v2/versions/269740/files> | Authoritative filenames, byte sizes, SHA-256 digests, and individual download links |
| Retrieved public release delivery | <https://datadryad.org/api/v2/versions/269740/download> | Public version bundle endpoint used for the 19 Sep 2026 retrieval |
| Direct primary-file endpoint | <https://datadryad.org/api/v2/files/2789266/download> | File ID `2789266` for `PSF.data.EL.open.csv`; recorded as the individual-file source endpoint |
| Primary paper | <https://doi.org/10.1111/ele.14364> | Jiang *et al.* (2024), *Ecology Letters* 27:e14364 |

## License, citation, and reuse limits

Dryad’s dataset-level API metadata states the license as **[CC0 1.0 Universal](https://spdx.org/licenses/CC0-1.0.html)**. CC0 dedicates the released data to the public domain to the extent permitted by law; thus the repository does not state a copyright-based restriction on copying, modifying, redistributing, or using the released data. The release README nevertheless expressly says, “When using this data, please cite our paper,” and acknowledges the ecologists who contributed original data. This project must therefore cite both the associated Jiang *et al.* paper and the Dryad dataset DOI as a scholarly and provenance requirement.

The released CSV is a synthesis of observations originating in **202 studies**. CC0 applies to this released dataset, but it does not itself establish rights in every underlying primary study, image, figure, or source table from which observations may have been extracted. Reuse under this project is limited to the released records and the stated analytical purpose; no claim is made that the underlying source literature or other unbundled materials are relicensed. Downstream users must preserve the dataset DOI, paper citation, this checksum record, and the original row-level source identifiers (`Author`, `Year`, and `Source`), and must not represent post-retrieval derivatives as the original immutable source.

## Interpretation safeguards

The CSV has direct `rr` (log effect size) and `var` (variance) columns, and it identifies source studies and setting fields. The release’s own R script references raw mean, SD, and sample-size fields that are not present in this CSV. Accordingly, the manifest confirms the integrity of the supplied effect estimates and variances; it does **not** claim they can be independently recalculated from raw group summaries within this release. The later WO-5 workflow must retain source-study clustering and perform its planned independent hop coding and reconciliation before substantive inference.

## References

- Jiang *et al.* (2024), [publisher record](https://doi.org/10.1111/ele.14364).
- [Dryad dataset landing page](https://datadryad.org/dataset/doi:10.5061/dryad.n2z34tn35).
- [Dryad version 269740 file inventory](https://datadryad.org/api/v2/versions/269740/files).
- [CC0 1.0 Universal license identifier](https://spdx.org/licenses/CC0-1.0.html).

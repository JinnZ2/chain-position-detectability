# WO-5 validation correction register

**Prepared:** 19 September 2026

This register maps the independent validation findings to the corrected release. The original validation reports remain unchanged as audit-trail records.

| Validation finding | Release action | Final disposition |
|---|---|---|
| Initial randomization did not preserve the observed H1/H2 source-category margin. | Replaced it with a count-preserving source-level permutation: singleton labels are permuted while retaining 20 H1-only and 88 H2-only sources; labels within each of three dual-category sources may swap. The test fixes \(\tau^2\) and weights across 4,999 draws. | **Corrected.** Two-sided *p* = 0.9824; all draws retain 91 H2 cells. |
| CR1 degrees of freedom may be optimistic because category leverage is uneven. | Added Bell–McCaffrey-style CR2 covariance with contrast-specific Satterthwaite degrees of freedom at effect and source-category levels. | **Corrected with sensitivity.** Primary CR2 CI −0.2181 to 0.2075, df 13.58, *p* = 0.9582; aggregate CR2 CI −0.1931 to 0.1875, df 33.40, *p* = 0.9762. |
| The main contrast is predominantly between sources. | Final report and analysis report now state 20 H1-only, 88 H2-only, and three dual-category sources; the paired result is explicitly non-informative. | **Corrected in interpretation.** |
| Row-level \(\tau^2\) was described too generally. | Final report calls it residual effect heterogeneity under a diagonal working sampling covariance and notes that clustering does not repair missing sampling covariances in likelihood weights. | **Corrected in interpretation.** |
| Broad carry or information-loss language would overclaim. | Final report defines the estimand as a setting-defined signed PSF association and explicitly rejects information-loss, causal-hop, within-source, ecological-realism, and common-signal interpretations. | **Corrected in interpretation.** |
| Practical equivalence was not established. | Final report retains “no detectable difference,” reports the ±log(1.10) margin and TOST result, and rejects “equivalent” wording. | **Retained as a limitation.** |
| HU exclusions create a selected subset. | Final report foregrounds that 4,446 of 5,969 effects and 91 HU-only studies are excluded; generalization is limited to metadata-resolved field conditioning. | **Retained as a limitation.** |
| Analysis report lacked links, figures, and standard references. | Machine-generated report now links code, input, result files, auxiliary tables, environment, and all figures, with numeric references. | **Corrected.** |
| Corpus-selection references were malformed. | Replaced them with standard Markdown reference definitions. | **Corrected.** |
| Discovery inventory and ALAN/HIREC audits were absent. | Added five-corpus discovery inventory and complete audit records for candidates 01 and 04. | **Corrected.** |
| Runtime was not pinned. | Added exact dependency versions, Python/runtime notes, fixed `Agg` backend, `DejaVu Sans`, and a reproducible invocation. | **Corrected.** |
| Downstream artifacts were untracked. | The complete corrected package is committed and pushed after final validation. | **Resolved at publication; does not retroactively prove the pre-discovery chronology.** |
| Full 202-source citation crosswalk was absent. | Added a 202-row crosswalk, deterministic resolver, raw-label inventory, candidate evidence, and methods report. | **Partially resolved.** 116 labels resolve to DOI records, 50 remain ambiguous, and 36 remain unresolved; no unresolved label is guessed. |
| Coding-output equality did not independently prove blind or temporally independent work. | Final report describes equality and verified agreement without claiming independently authenticated blinding. | **Retained as a provenance limitation.** |

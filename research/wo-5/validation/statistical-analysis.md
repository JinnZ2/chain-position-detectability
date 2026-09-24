# Independent validation of the H1-versus-H2 meta-analysis

**Author:** Manus AI
**Role:** Independent meta-analysis statistician
**Validation date:** 19 September 2026

## Overall verdict

The numerical results for the effect-level primary model and the source-category aggregation are **reproducible to numerical precision** from the coded data. I independently implemented generalized least squares, the restricted maximum-likelihood (REML) profile objective, the cluster sandwich estimator, source-category aggregation, leave-one-source-out refitting, equivalence tests, and descriptive summaries. I did not import or execute the supplied analysis functions. My primary contrast differs from the reported value by only \(2.7\times10^{-11}\), and the independently aggregated contrast differs by \(2.3\times10^{-11}\). The reported REML variances, clustered standard errors, confidence intervals, and ordinary *p*-values contain no material arithmetic error.[2] [3] [4]

One inferential routine does require correction or relabeling. The reported “source-level label-swap permutation” independently flips each source's category with probability one-half. That is **not a count-preserving permutation of the observed source labels**. It changes the 23-versus-91 source-category allocation toward approximately equal groups. The reported Monte Carlo value, *p*=0.9730, is exactly reproducible for that algorithm, but its description and null randomization scheme do not match a conventional permutation conditional on the observed allocation. A count-preserving source-level permutation gives *p*=0.9824 with the same seed and 4,999 draws. This issue does not change the substantive conclusion because the observed contrast is almost exactly zero.

The primary model is **algebraically identified**, despite only three sources appearing in both categories. Its design matrix has rank two because H1 and H2 both have observations: 23 sources contribute H1 and 91 contribute H2. However, 20 sources are H1-only, 88 are H2-only, and only 3 provide both categories. The primary coefficient is therefore mainly a **between-source comparison**, not a within-source H1-versus-H2 effect. A paired or source-fixed-effect interpretation depends on only three discordant sources and is too weak for dependable generalization. The supplied report appropriately limits its claim to association rather than causation.[1] [4]

## Data and independent implementation

The input file has SHA-256 `77dc735fa425abd96329acbc55a99c6403f7da77b947f3b1cc7d61a9ec612480`. It contains 5,969 rows. Applying the documented eligibility rule retains 1,523 rows: 326 H1 effects from 23 sources and 1,197 H2 effects from 91 sources. The union contains 111 sources because three occur in both groups. Aggregation creates 114 source-category cells.[1] [2]

I formed a two-column design matrix with an intercept and an H2 indicator. For a candidate heterogeneity variance \(\tau^2\), I used

\[
W(\tau^2)=\operatorname{diag}\{1/(v_i+\tau^2)\},\qquad
\hat\beta(\tau^2)=(X'WX)^{-1}X'Wy.
\]

Apart from constants that do not depend on \(\tau^2\), the minimized negative restricted log-likelihood was

\[
Q_R(\tau^2)=\frac{1}{2}\left[
\sum_i\log(v_i+\tau^2)+
\log|X'W(\tau^2)X|+
(y-X\hat\beta)'W(\tau^2)(y-X\hat\beta)
\right].
\]

This is the appropriate profile REML criterion **if the working sampling covariance is diagonal**. The supplied objective implements the same expression. Its omission of likelihood constants is harmless because they do not affect the optimizer. My optimizer searched much wider intervals than the supplied code and found the same interior optima. The numerical derivative of the twice-objective at each solution was within \(3.8\times10^{-7}\) of zero.

For the sensitivity aggregation, I independently calculated each source-category cell as

\[
\bar y_{gc}=\frac{\sum_{i\in(gc)} y_i/v_i}{\sum_{i\in(gc)}1/v_i},\qquad
\bar v_{gc}=\left(\sum_{i\in(gc)}1/v_i\right)^{-1}.
\]

These formulas reproduce all 114 cells implied by the coded data. They assume zero sampling covariance among effects in a cell. That is a working assumption, not a fact established by the data.

## The primary and aggregated estimates reproduce

| Model and estimand | Independent estimate | Clustered SE | 95% CI | *t* | df | Two-sided *p* | Reported estimate | Absolute estimate discrepancy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Effect level: H1 mean | -0.042872 | 0.038233 | [-0.118641, 0.032897] | -1.1213 | 110 | 0.2646 | -0.042872 | \(1.22\times10^{-10}\) |
| Effect level: H2 mean | -0.048149 | 0.083878 | [-0.214375, 0.118076] | -0.5740 | 110 | 0.5671 | -0.048149 | \(1.49\times10^{-10}\) |
| **Effect level: H2 − H1** | **-0.005277** | **0.092398** | **[-0.188388, 0.177834]** | **-0.0571** | **110** | **0.9546** | **-0.005277** | **\(2.70\times10^{-11}\)** |
| Source-category: H1 mean | -0.053516 | 0.077205 | [-0.206519, 0.099486] | -0.6932 | 110 | 0.4897 | -0.053516 | \(1.02\times10^{-11}\) |
| Source-category: H2 mean | -0.056330 | 0.050721 | [-0.156848, 0.044188] | -1.1106 | 110 | 0.2692 | -0.056330 | \(3.30\times10^{-11}\) |
| **Source-category: H2 − H1** | **-0.002814** | **0.092804** | **[-0.186729, 0.181102]** | **-0.0303** | **110** | **0.9759** | **-0.002814** | **\(2.29\times10^{-11}\)** |

The independent effect-level REML estimate is \(\tau^2=0.3637751413\), versus 0.3637751465 reported. The independent source-category value is \(\tau^2=0.2034229366\), versus 0.2034229337 reported. These differences, \(5.2\times10^{-9}\) and \(2.9\times10^{-9}\), are optimizer tolerances rather than discrepancies. The independent half-objective values are 157.697466 and -25.675602, respectively. The supplied search bounds were 20.0 and 3.877; my bounds were 200 and 100. Both fitted optima are comfortably interior, so the supplied code's failure to test the upper endpoint has no effect here.

On the response-ratio scale, the primary H2-minus-H1 estimate is \(\exp(-0.005277)=0.9947\). Its 95% interval is approximately 0.828 to 1.195. Thus the point estimate is tiny, but the data remain compatible with differences of meaningful size in either direction.

## REML is correct for the stated working model, not a full multilevel model

The REML calculation is computationally correct for independent rows with variances \(v_i+\tau^2\). The limitation is the covariance model. Multiple outcomes, species, treatments, and contrasts from one source can share controls or other design components. The input does not supply their sampling covariances. Consequently, the row-level likelihood treats dependent effects as independent when estimating \(\tau^2\) and the inverse-variance weights.

Clustering the final coefficient covariance by source protects standard errors against some within-source residual dependence. It **does not repair the likelihood used to estimate heterogeneity or the weights**, and it does not turn the row-level \(\tau^2\) into a clean between-study variance. At the effect level, \(\tau^2\) absorbs unexplained row heterogeneity under a diagonal working model. The phrase “residual heterogeneity” is appropriate; “between-study variance” would be too specific.

Aggregation reduces the extreme row-count imbalance, but its cell variance \(1/\sum 1/v_i\) also presumes independent sampling errors. If a source's effects share controls, that variance is too small. The subsequent source-clustered sandwich estimator helps coefficient inference, although only three sources contribute two cells and therefore expose within-source H1/H2 covariance. These are **defensible approximations forced by missing covariance data**, not coding mistakes. A preferred analysis would use reported sampling-covariance matrices or a specified working correlation and a multilevel model.

## The CR1 sandwich is implemented correctly; its degrees of freedom are optimistic for this contrast

The supplied clustered covariance is the common CR1 estimator

\[
\widehat V_{CR1}=\frac{G}{G-1}\frac{n-1}{n-p}
B\left(\sum_{g=1}^{G}s_gs_g'\right)B,
\quad B=(X'WX)^{-1},\quad s_g=X_g'W_g r_g.
\]

I reproduce its finite-sample multiplier: 1.009754 for the 1,523-row primary model and 1.018101 for the 114-cell aggregate. The corresponding CR0 standard errors for the H2-minus-H1 contrast are 0.091951 and 0.091975. Applying CR1 raises them to the reported 0.092398 and 0.092804. The formula is therefore correct.

Using \(G-1=110\) reference degrees of freedom is a familiar cluster-robust convention and is a **defensible methodological choice**, not an arithmetic error. It nevertheless counts all 111 clusters equally for degrees of freedom even though the category coefficient has highly uneven leverage. Only 23 sources inform the H1 side, and one source contributes 240 effect rows. Eleven sources provide half of all eligible rows.

As a diagnostic, I independently applied a Bell–McCaffrey-style CR2 adjustment with contrast-specific Satterthwaite degrees of freedom.[5] It gives the following results:

| Model | CR1 SE and df | CR1 95% CI | CR2 SE | Satterthwaite df | CR2 95% CI | CR2 *p* |
|---|---:|---:|---:|---:|---:|---:|
| Effect level | 0.092398; 110 | [-0.188388, 0.177834] | 0.098931 | 13.58 | [-0.218077, 0.207522] | 0.9582 |
| Source-category aggregate | 0.092804; 110 | [-0.186729, 0.181102] | 0.093572 | 33.40 | [-0.193100, 0.187472] | 0.9762 |

This adjustment widens the primary interval but does not change the conclusion. The final report should either retain CR1/*t*(110) and identify it explicitly as a conventional approximation, or preferably add CR2/Satterthwaite inference as a small-sample sensitivity. The effective degrees of freedom are especially relevant to precision and equivalence, even though they make little difference to the null test when the statistic is only -0.057.

## The model is identified, but within-source overlap is minimal

There are three distinct identification questions.

First, the reported no-study-fixed-effect regression is identified. Both the row-level and aggregate design matrices have rank two. Its coefficient estimates the weighted difference between H2 and H1 observations across all included sources. It does not require every source to contain both categories.

Second, a within-source contrast is only informed by `Heinze,2016||2016`, `Jiang et al. 2022||2022`, and `Schittko et al. 2016||2016`. Their aggregated H2-minus-H1 differences are 0.64076, 0.02708, and 0.10574. The supplied paired model reproduces as 0.24476 with SE 0.18610, \(\tau^2=0.09897\), *t*(2)=1.315, 95% CI [-0.55595, 1.04547], and *p*=0.3190. This intercept-only model is formally identified because three observations leave two residual degrees of freedom. Its heterogeneity estimate and *t* reference are nonetheless extremely fragile. An exact sign-swap calculation has only eight assignments and gives two-sided *p*=0.25.

Third, a source-fixed-effect model with a category coefficient would also be algebraically identified by those three discordant sources, but all category information from the other 108 sources would be absorbed by source effects. Cluster-robust inference based on only three informative clusters would not be dependable. Therefore, the three-source overlap does **not** invalidate the reported between-source association, but it prevents that association from being interpreted as a well-supported within-source effect. The report's confounding warning is essential, not optional.

## Leave-one-source-out results are correct but do not test composition confounding

I independently rebuilt the source-category aggregate model 111 times. The H2-minus-H1 estimates range from **-0.0425617** when `Casper and Castelli 2007||2007` is omitted to **0.0336513** when `Kulmatiski, unpubl. Data||2008` is omitted. These reproduce the stated rounded range of -0.0426 to 0.0337. Every refit has 110 clusters, uses 109 reference degrees of freedom, and has a confidence interval containing zero. Across refits, the smallest lower limit is -0.214343 and the largest upper limit is 0.208134.

This diagnostic correctly shows that no single source creates a detectable contrast. It cannot show that H1 and H2 source compositions are exchangeable. Stable leave-one-out results may coexist with systematic differences across the 20 H1-only and 88 H2-only studies.

## The reported permutation number is reproducible, but the label logic is misnamed

The supplied algorithm draws an independent Bernoulli flip for every source. A source with one category is moved to the other category when flipped. A source represented in both categories has its two labels swapped. The fitted \(\tau^2\) and cell weights are held fixed, and the unstudentized H2 coefficient is recomputed. With seed 20260919, 4,864 of 4,999 simulated coefficients are at least as large in absolute value as the observed -0.002814; the plus-one Monte Carlo calculation is exactly **0.9730**.[3]

The arithmetic is correct, but the randomization does not preserve the observed margins. There are 91 H2 and 23 H1 cells. Because each of the three paired sources always contributes one cell to each group, independent flips produce an expected 57 H2 cells. In the saved 4,999 draws, the H2 count ranges only from 37 to 77 and never reaches the observed 91. Calling this a “permutation” obscures that it tests a hypothetical independent 50:50 Bernoulli assignment, not exchangeability conditional on the observed group counts.

I also ran a count-preserving alternative. It permutes the 20 H1 and 88 H2 labels across the 108 singleton sources, independently swaps the two labels within each of the three dual-category sources, and retains all 91 H2 cells. With 4,999 draws and the same seed, 4,911 draws are at least as extreme, giving **p=0.9824**. Re-estimating \(\tau^2\) in every draw gives the same value to four decimals. Neither permutation approach changes the finding.

This is best classified as an **inferential logic and reporting error**, not a numerical one. The correction is to describe the existing calculation as an independent source-wise label-flip randomization and justify the 50:50 assignment model, or replace it with a clearly defined count-preserving source permutation. Because category is observational and confounded with setting and study composition, neither scheme has a literal randomized-treatment interpretation. The permutation result should remain a robustness calculation rather than be presented as design-based causal evidence. Fixing \(\tau^2\) across draws is a defensible choice if the coefficient under fixed weights is declared as the test statistic; refitting it is preferable as a sensitivity.

## The equivalence statement is correct and conservative

The prespecified practical-equivalence margin is \(\Delta=\log(1.10)=0.095310\), corresponding to a response-ratio interval from \(1/1.10=0.9091\) to 1.10.[1] The primary 95% confidence interval, [-0.18839, 0.17783], is not contained within [-0.09531, 0.09531]. Therefore, the statement that the analysis “shows no detectable contrast but does not establish practical equivalence” is correct.[4]

Conventional two-one-sided-test (TOST) equivalence at \(\alpha=0.05\) is evaluated with a 90% confidence interval. That interval is [-0.15855, 0.14800], which also crosses both equivalence limits. The two one-sided *p*-values are 0.1660 and 0.1393, so the TOST result is *p*=0.1660. Using a 95% interval is more conservative than standard 5% TOST, but it does not alter the decision here. The report should avoid saying the categories are equivalent, the contrast is absent, or the null hypothesis has been proved.

## Descriptive magnitude output is reproduced and appropriately noninferential

| Quantity | H1 | H2 |
|---|---:|---:|
| Effect rows | 326 | 1,197 |
| Sources | 23 | 91 |
| Mean \(|rr|\) across rows | 0.269942 | 0.463899 |
| Median \(|rr|\) across rows | 0.182017 | 0.266430 |
| 25th percentile \(|rr|\) | 0.064887 | 0.109750 |
| 75th percentile \(|rr|\) | 0.324951 | 0.553442 |
| Mean across source-category cells of within-cell mean \(|rr|\) | 0.329897 | 0.477366 |
| Median across source-category cells of within-cell mean \(|rr|\) | 0.242183 | 0.360759 |

Every displayed value reproduces the supplied output. The narrative wording—“after averaging absolute values within each source/category”—is precise. It calculates the cell mean of \(|rr|\), then summarizes those cell values. It does **not** calculate the absolute value of a cell's signed mean. Those alternative quantities are smaller: mean \(|\text{unweighted cell mean}|\) is 0.231813 for H1 and 0.334244 for H2; mean \(|\text{fixed-effect cell mean}|\) is 0.244508 and 0.304703.

The row-level summaries give much more influence to large sources. For example, one H2 source supplies 240 rows, and only 11 of 111 sources supply half of all eligible rows. The source-category summaries answer a useful equal-cell descriptive question, but the three dual-category sources each contribute once to each category. The decision not to attach an inferential test to \(|rr|\) is sound because absolute-value transformation creates a folded distribution and the original sampling variances no longer directly describe it.[1]

## Errors, defensible choices, and required corrections

| Audit item | Classification | Finding and action |
|---|---|---|
| Primary and aggregate coefficients | Confirmed computation | Reproduced to less than \(3\times10^{-11}\) in the contrasts. No correction. |
| REML objective and optimizer | Confirmed computation with minor implementation caveat | Objective is correct for diagonal \(V\). The supplied optimizer does not compare the upper endpoint, but the fitted minima are interior. No numerical correction for these data. |
| Interpretation of \(\tau^2\) | Methodological limitation | Row-level \(\tau^2\) is residual effect heterogeneity under a diagonal working model, not a clean between-study variance. Use precise terminology. |
| CR1 covariance | Confirmed computation | Formula and finite-sample multipliers reproduce. No arithmetic correction. |
| Degrees of freedom | Defensible but improvable choice | \(G-1=110\) is conventional. Add CR2/Satterthwaite because predictor leverage reduces effective df to about 13.6 in the primary contrast. |
| Sparse overlap | Identification/interpretation limitation | Primary model is rank-identified but mainly between-source. State explicitly that only three sources support a within-source contrast. |
| Source-category aggregation | Defensible approximation | Correct under independent within-cell errors. State that unknown shared-control covariances are ignored. |
| Leave-one-source-out | Confirmed computation | Range and interval envelope reproduce. No correction. |
| Source-level permutation | **Logic/reporting error** | Existing *p*=0.9730 is reproducible but is an independent 50:50 flip, not a margin-preserving permutation. Relabel and justify it or replace it; count-preserving *p*=0.9824. |
| Equivalence | Confirmed conclusion | Neither 95% CI nor conventional 90% CI lies within ±log(1.10); TOST *p*=0.1660. Keep “not established.” |
| Descriptive magnitude | Confirmed computation | Values and description reproduce. Continue to label them descriptive and distinguish mean absolute effects from absolute mean effects. |

## Final assessment

The central quantitative conclusion is robust to independent reimplementation: the point estimate for H2 minus H1 is nearly zero at both the effect level and after source-category aggregation, while uncertainty is too wide to establish practical equivalence. The main estimates, clustered CR1 variances, degrees-of-freedom calculation, leave-one-source-out range, equivalence conclusion, and magnitude summaries are internally consistent.

The validation does **not** support a stronger claim that hop category has no association. It also does not support a within-source or causal interpretation because only three studies span both categories and setting is built into the category definition. The two changes most needed are to correct or relabel the permutation routine and to expose the limited effective degrees of freedom through a CR2/Satterthwaite sensitivity. Neither change reverses the reported null result; both make the uncertainty and estimand more accurately described.

## Reproducibility record

The independent code was written without importing the supplied analysis module. The audit calculations and supporting scripts are retained at:

- `/home/ubuntu/jobs/8132ad7a71cf_a0/independent_validation.py`
- `/home/ubuntu/jobs/8132ad7a71cf_a0/independent-results.json`
- `/home/ubuntu/jobs/8132ad7a71cf_a0/cr2_diagnostic.py`
- `/home/ubuntu/jobs/8132ad7a71cf_a0/cr2-results.json`
- `/home/ubuntu/jobs/8132ad7a71cf_a0/structural_diagnostics.py`
- `/home/ubuntu/jobs/8132ad7a71cf_a0/structural-results.json`

## References

[1]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/ecology-codebook.md "WO-5 ecology carry-test codebook"

[2]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/analysis/hop-coded-effects.csv "WO-5 reconciled hop-coded effect-size dataset"

[3]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/analysis/analyze_hop_distance.py "Supplied WO-5 H1-versus-H2 analysis implementation"

[4]: https://github.com/JinnZ2/chain-position-detectability/blob/main/research/wo-5/analysis/analysis-results.md "Supplied WO-5 statistical analysis results"

[5]: https://doi.org/10.1080/07350015.2016.1247004 "Small-Sample Methods for Cluster-Robust Variance Estimation and Hypothesis Testing in Fixed Effects Models"

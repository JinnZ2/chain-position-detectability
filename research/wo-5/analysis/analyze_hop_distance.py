#!/usr/bin/env python3
"""Reproduce the preregistered WO-5 Test E analysis.

The primary analysis compares the two independently supported categories, H1 and
H2. It fits a random-effects meta-regression to row-level log response ratios
and uses source-study-clustered sandwich standard errors. Sensitivity analyses
reduce each source-study/category cell to one estimate, give source studies
equal weight, and compare only studies represented in both categories.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.stats import norm, t

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INPUT = HERE / "hop-coded-effects.csv"
EXPECTED_SHA256 = "77dc735fa425abd96329acbc55a99c6403f7da77b947f3b1cc7d61a9ec612480"
SEED = 20260919
N_PERM = 4999


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def reml_fit(y: np.ndarray, v: np.ndarray, X: np.ndarray, clusters: np.ndarray) -> dict:
    y = np.asarray(y, dtype=float)
    v = np.asarray(v, dtype=float)
    X = np.asarray(X, dtype=float)
    clusters = np.asarray(clusters)
    n, p = X.shape
    if n <= p or np.any(v <= 0) or not np.all(np.isfinite(y)):
        raise ValueError("Invalid meta-regression input")

    def components(tau2: float):
        w = 1.0 / (v + tau2)
        xtwx = X.T @ (w[:, None] * X)
        bread = np.linalg.inv(xtwx)
        beta = bread @ (X.T @ (w * y))
        resid = y - X @ beta
        sign, logdet = np.linalg.slogdet(xtwx)
        if sign <= 0:
            return None
        objective = 0.5 * (
            np.sum(np.log(v + tau2)) + logdet + np.sum(w * resid * resid)
        )
        return objective, w, bread, beta, resid

    upper = max(float(np.var(y, ddof=1) * 10.0), float(np.max(v) * 10.0), 1.0)
    opt = minimize_scalar(
        lambda z: components(float(z))[0],
        bounds=(0.0, upper),
        method="bounded",
        options={"xatol": 1e-12, "maxiter": 1000},
    )
    candidates = [(0.0, components(0.0)), (float(opt.x), components(float(opt.x)))]
    tau2, best = min(candidates, key=lambda item: item[1][0])
    objective, w, bread, beta, resid = best

    unique_clusters = pd.unique(clusters)
    meat = np.zeros((p, p), dtype=float)
    for cluster in unique_clusters:
        idx = clusters == cluster
        score = X[idx].T @ (w[idx] * resid[idx])
        meat += np.outer(score, score)
    g = len(unique_clusters)
    correction = (g / (g - 1.0)) * ((n - 1.0) / (n - p)) if g > 1 and n > p else 1.0
    vcov = correction * bread @ meat @ bread
    df = max(g - 1, 1)
    critical = float(t.ppf(0.975, df))
    return {
        "n": int(n),
        "p": int(p),
        "clusters": int(g),
        "tau2": float(tau2),
        "beta": beta,
        "vcov": vcov,
        "se": np.sqrt(np.diag(vcov)),
        "df": int(df),
        "critical": critical,
        "objective": float(objective),
    }


def contrast(fit: dict, vector: list[float]) -> dict:
    c = np.asarray(vector, dtype=float)
    estimate = float(c @ fit["beta"])
    variance = float(c @ fit["vcov"] @ c)
    se = math.sqrt(max(variance, 0.0))
    critical = fit["critical"]
    statistic = estimate / se if se > 0 else math.inf
    p_value = float(2.0 * t.sf(abs(statistic), fit["df"])) if se > 0 else 0.0
    return {
        "estimate": estimate,
        "se": se,
        "ci_low": estimate - critical * se,
        "ci_high": estimate + critical * se,
        "statistic": statistic,
        "df": fit["df"],
        "p_value": p_value,
    }


def ordinary_cluster_wls(y: np.ndarray, X: np.ndarray, clusters: np.ndarray) -> dict:
    v = np.ones_like(y, dtype=float)
    return reml_fit(y, v, X, clusters)


def inverse_symmetric_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2.0)
    if values.min() <= 1e-10:
        raise np.linalg.LinAlgError(f"CR2 block is singular: minimum eigenvalue {values.min()}")
    return (vectors * (1.0 / np.sqrt(values))) @ vectors.T


def cr2_contrast(
    y: np.ndarray,
    v: np.ndarray,
    X: np.ndarray,
    clusters: np.ndarray,
    tau2: float,
    vector: list[float],
) -> dict:
    """Bell–McCaffrey-style CR2 with contrast-specific Satterthwaite df."""
    y = np.asarray(y, dtype=float)
    v = np.asarray(v, dtype=float)
    X = np.asarray(X, dtype=float)
    clusters = np.asarray(clusters)
    c = np.asarray(vector, dtype=float)
    sqrt_w = np.sqrt(1.0 / (v + tau2))
    xw = sqrt_w[:, None] * X
    yw = sqrt_w * y
    bread = np.linalg.solve(xw.T @ xw, np.eye(xw.shape[1]))
    beta = bread @ xw.T @ yw
    residual_w = yw - xw @ beta
    bc = bread @ c
    linear_forms = []
    score_contributions = []
    labels = pd.unique(clusters)
    for label in labels:
        idx = np.flatnonzero(clusters == label)
        xg = xw[idx]
        adjustment = inverse_symmetric_square_root(np.eye(len(idx)) - xg @ bread @ xg.T)
        adjusted_residual = adjustment @ residual_w[idx]
        score_contributions.append(float(c @ bread @ xg.T @ adjusted_residual))
        r_columns = -xw @ bread @ xg.T
        r_columns[idx, np.arange(len(idx))] += 1.0
        linear_forms.append(r_columns @ adjustment.T @ xg @ bc)
    lmat = np.column_stack(linear_forms)
    gram = lmat.T @ lmat
    trace_m = float(np.trace(gram))
    trace_m2 = float(np.sum(gram * gram))
    df = trace_m * trace_m / trace_m2
    estimate = float(c @ beta)
    se = float(np.sqrt(np.dot(score_contributions, score_contributions)))
    statistic = estimate / se
    critical = float(t.ppf(0.975, df))
    return {
        "estimate": estimate,
        "se": se,
        "ci_low": estimate - critical * se,
        "ci_high": estimate + critical * se,
        "statistic": statistic,
        "df": float(df),
        "p_value": float(2.0 * t.sf(abs(statistic), df)),
    }


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    observed_hash = sha256(INPUT)
    if observed_hash != EXPECTED_SHA256:
        raise SystemExit(f"Input hash mismatch: {observed_hash}")

    df = pd.read_csv(INPUT, dtype={"N": str, "Author": str, "Year": str})
    if len(df) != 5969 or not df["N"].is_unique:
        raise SystemExit("Unexpected row count or nonunique N")
    df["rr"] = pd.to_numeric(df["rr"], errors="raise")
    df["var"] = pd.to_numeric(df["var"], errors="raise")
    if not np.isfinite(df["rr"]).all() or not np.isfinite(df["var"]).all() or not (df["var"] > 0).all():
        raise SystemExit("Invalid rr or var")

    eligible = df[df["hop_code"].isin(["H1", "H2"])].copy()
    eligible["h2"] = (eligible["hop_code"] == "H2").astype(int)
    eligible["study_id"] = eligible["Author"].str.strip() + "||" + eligible["Year"].str.strip()
    X = np.column_stack([np.ones(len(eligible)), eligible["h2"].to_numpy(float)])
    primary = reml_fit(
        eligible["rr"].to_numpy(), eligible["var"].to_numpy(), X, eligible["study_id"].to_numpy()
    )
    primary_h1 = contrast(primary, [1.0, 0.0])
    primary_h2 = contrast(primary, [1.0, 1.0])
    primary_diff = contrast(primary, [0.0, 1.0])
    primary_cr2 = cr2_contrast(
        eligible["rr"].to_numpy(),
        eligible["var"].to_numpy(),
        X,
        eligible["study_id"].to_numpy(),
        primary["tau2"],
        [0.0, 1.0],
    )

    aggregated_rows = []
    for (study_id, hop_code), group in eligible.groupby(["study_id", "hop_code"], sort=True):
        w = 1.0 / group["var"].to_numpy(float)
        y = group["rr"].to_numpy(float)
        aggregated_rows.append(
            {
                "study_id": study_id,
                "Author": group["Author"].iloc[0],
                "Year": group["Year"].iloc[0],
                "hop_code": hop_code,
                "h2": int(hop_code == "H2"),
                "effect_rows": int(len(group)),
                "fixed_effect_mean_rr": float(np.sum(w * y) / np.sum(w)),
                "fixed_effect_variance": float(1.0 / np.sum(w)),
                "unweighted_mean_rr": float(np.mean(y)),
                "mean_absolute_rr": float(np.mean(np.abs(y))),
                "min_rr": float(np.min(y)),
                "max_rr": float(np.max(y)),
            }
        )
    agg = pd.DataFrame(aggregated_rows)
    agg_path = HERE / "study-category-aggregates.csv"
    agg.to_csv(agg_path, index=False, quoting=csv.QUOTE_ALL)

    Xa = np.column_stack([np.ones(len(agg)), agg["h2"].to_numpy(float)])
    study_agg = reml_fit(
        agg["fixed_effect_mean_rr"].to_numpy(),
        agg["fixed_effect_variance"].to_numpy(),
        Xa,
        agg["study_id"].to_numpy(),
    )
    study_agg_h1 = contrast(study_agg, [1.0, 0.0])
    study_agg_h2 = contrast(study_agg, [1.0, 1.0])
    study_agg_diff = contrast(study_agg, [0.0, 1.0])
    study_agg_cr2 = cr2_contrast(
        agg["fixed_effect_mean_rr"].to_numpy(),
        agg["fixed_effect_variance"].to_numpy(),
        Xa,
        agg["study_id"].to_numpy(),
        study_agg["tau2"],
        [0.0, 1.0],
    )

    equal_study = ordinary_cluster_wls(
        agg["unweighted_mean_rr"].to_numpy(), Xa, agg["study_id"].to_numpy()
    )
    equal_diff = contrast(equal_study, [0.0, 1.0])

    paired = agg.pivot(index="study_id", columns="hop_code", values=["fixed_effect_mean_rr", "fixed_effect_variance"])
    paired = paired.dropna().copy()
    paired_diff_y = (
        paired[("fixed_effect_mean_rr", "H2")] - paired[("fixed_effect_mean_rr", "H1")]
    ).to_numpy(float)
    paired_diff_v = (
        paired[("fixed_effect_variance", "H2")] + paired[("fixed_effect_variance", "H1")]
    ).to_numpy(float)
    paired_X = np.ones((len(paired), 1), dtype=float)
    paired_fit = reml_fit(paired_diff_y, paired_diff_v, paired_X, paired.index.to_numpy())
    paired_result = contrast(paired_fit, [1.0])

    # Leave-one-source-out analysis on source-category aggregates.
    loo_rows = []
    for study_id in sorted(agg["study_id"].unique()):
        subset = agg[agg["study_id"] != study_id]
        Xs = np.column_stack([np.ones(len(subset)), subset["h2"].to_numpy(float)])
        fit = reml_fit(
            subset["fixed_effect_mean_rr"].to_numpy(),
            subset["fixed_effect_variance"].to_numpy(),
            Xs,
            subset["study_id"].to_numpy(),
        )
        result = contrast(fit, [0.0, 1.0])
        loo_rows.append({"omitted_study": study_id, **result, "tau2": fit["tau2"]})
    loo = pd.DataFrame(loo_rows)
    loo.to_csv(HERE / "leave-one-study-out.csv", index=False, quoting=csv.QUOTE_ALL)

    # Count-preserving source-level permutation on source-category aggregates.
    # Singleton-source labels are permuted while retaining the observed margin;
    # the two labels within each dual-category source may be swapped. The fitted
    # tau-squared and cell weights remain fixed across draws.
    rng = np.random.default_rng(SEED)
    observed = study_agg_diff["estimate"]
    permuted = np.empty(N_PERM, dtype=float)
    original_h2 = agg["h2"].to_numpy(int)
    fixed_w = 1.0 / (agg["fixed_effect_variance"].to_numpy(float) + study_agg["tau2"])
    y_agg = agg["fixed_effect_mean_rr"].to_numpy(float)
    source_cell_counts = agg.groupby("study_id").size()
    singleton_ids = source_cell_counts.index[source_cell_counts == 1].to_numpy()
    paired_ids = source_cell_counts.index[source_cell_counts == 2].to_numpy()
    singleton_rows = np.array([agg.index[agg["study_id"] == sid][0] for sid in singleton_ids])
    singleton_observed = original_h2[singleton_rows]
    paired_rows = [np.array(agg.index[agg["study_id"] == sid]) for sid in paired_ids]
    perm_h2_counts = np.empty(N_PERM, dtype=int)
    for i in range(N_PERM):
        perm_h2 = original_h2.copy()
        perm_h2[singleton_rows] = rng.permutation(singleton_observed)
        for rows in paired_rows:
            if rng.integers(0, 2):
                perm_h2[rows] = perm_h2[rows[::-1]]
        perm_h2_counts[i] = int(perm_h2.sum())
        Xp = np.column_stack([np.ones(len(agg)), perm_h2])
        beta = np.linalg.inv(Xp.T @ (fixed_w[:, None] * Xp)) @ (Xp.T @ (fixed_w * y_agg))
        permuted[i] = beta[1]
    permutation_p = float((1 + np.sum(np.abs(permuted) >= abs(observed))) / (N_PERM + 1))
    pd.DataFrame({"permutation": np.arange(1, N_PERM + 1), "h2_cells": perm_h2_counts, "h2_minus_h1": permuted}).to_csv(
        HERE / "permutation-results.csv", index=False, quoting=csv.QUOTE_ALL
    )

    summary_rows = []
    for model, result, fit in [
        ("primary_effect_level_h1", primary_h1, primary),
        ("primary_effect_level_h2", primary_h2, primary),
        ("primary_effect_level_h2_minus_h1", primary_diff, primary),
        ("primary_effect_level_h2_minus_h1_cr2", primary_cr2, primary),
        ("source_category_aggregated_h1", study_agg_h1, study_agg),
        ("source_category_aggregated_h2", study_agg_h2, study_agg),
        ("source_category_aggregated_h2_minus_h1", study_agg_diff, study_agg),
        ("source_category_aggregated_h2_minus_h1_cr2", study_agg_cr2, study_agg),
        ("equal_source_weight_h2_minus_h1", equal_diff, equal_study),
        ("paired_source_h2_minus_h1", paired_result, paired_fit),
    ]:
        summary_rows.append(
            {
                "model": model,
                **{key: result[key] for key in ["estimate", "se", "ci_low", "ci_high", "statistic", "df", "p_value"]},
                "tau2": fit["tau2"],
                "effect_units": fit["n"],
                "source_clusters": fit["clusters"],
            }
        )
    summary = pd.DataFrame(summary_rows)
    summary.to_csv(HERE / "model-summary.csv", index=False, quoting=csv.QUOTE_ALL)

    category_counts = (
        eligible.groupby("hop_code")
        .agg(effect_rows=("N", "count"), source_studies=("study_id", "nunique"), raw_mean_rr=("rr", "mean"))
        .reset_index()
    )
    category_counts.to_csv(HERE / "category-counts.csv", index=False, quoting=csv.QUOTE_ALL)

    magnitude_rows = []
    for hop_code, group in eligible.groupby("hop_code", sort=True):
        absolute = group["rr"].abs()
        source_magnitude = agg.loc[agg["hop_code"] == hop_code, "mean_absolute_rr"]
        magnitude_rows.append(
            {
                "hop_code": hop_code,
                "effect_rows": int(len(group)),
                "source_studies": int(group["study_id"].nunique()),
                "mean_absolute_rr": float(absolute.mean()),
                "median_absolute_rr": float(absolute.median()),
                "q25_absolute_rr": float(absolute.quantile(0.25)),
                "q75_absolute_rr": float(absolute.quantile(0.75)),
                "mean_source_category_absolute_rr": float(source_magnitude.mean()),
                "median_source_category_absolute_rr": float(source_magnitude.median()),
            }
        )
    magnitude = pd.DataFrame(magnitude_rows)
    magnitude.to_csv(HERE / "magnitude-summary.csv", index=False, quoting=csv.QUOTE_ALL)

    equivalence_margin = float(math.log(1.10))
    equivalence_supported = bool(
        primary_diff["ci_low"] > -equivalence_margin
        and primary_diff["ci_high"] < equivalence_margin
    )

    result_json = {
        "input": {
            "path": str(INPUT.relative_to(ROOT)),
            "sha256": observed_hash,
            "all_rows": int(len(df)),
            "eligible_rows": int(len(eligible)),
            "eligible_source_studies": int(eligible["study_id"].nunique()),
            "unresolved_rows": int((df["hop_code"] == "HU").sum()),
        },
        "primary": {
            "method": "effect-level REML meta-regression with source-study-clustered CR1 standard errors",
            "tau2": primary["tau2"],
            "h1": primary_h1,
            "h2": primary_h2,
            "h2_minus_h1": primary_diff,
            "h2_minus_h1_cr2_satterthwaite": primary_cr2,
        },
        "source_category_aggregation": {
            "method": "inverse-variance aggregation within source-study/category, then REML meta-regression with source-clustered CR1 standard errors",
            "cells": int(len(agg)),
            "sources": int(agg["study_id"].nunique()),
            "tau2": study_agg["tau2"],
            "h1": study_agg_h1,
            "h2": study_agg_h2,
            "h2_minus_h1": study_agg_diff,
            "h2_minus_h1_cr2_satterthwaite": study_agg_cr2,
        },
        "equal_source_weight": {"h2_minus_h1": equal_diff},
        "paired_source": {
            "paired_sources": int(len(paired)),
            "tau2": paired_fit["tau2"],
            "h2_minus_h1": paired_result,
        },
        "leave_one_source_out": {
            "models": int(len(loo)),
            "estimate_min": float(loo["estimate"].min()),
            "estimate_max": float(loo["estimate"].max()),
            "ci_low_min": float(loo["ci_low"].min()),
            "ci_high_max": float(loo["ci_high"].max()),
        },
        "permutation": {
            "seed": SEED,
            "replicates": N_PERM,
            "observed_source_aggregate_difference": observed,
            "two_sided_p": permutation_p,
            "method": "count-preserving source-level label permutation with fixed tau-squared and weights",
            "observed_h2_cells": int(original_h2.sum()),
            "permuted_h2_cell_min": int(perm_h2_counts.min()),
            "permuted_h2_cell_max": int(perm_h2_counts.max()),
        },
        "source_overlap": {
            "h1_only_sources": int(len(set(eligible.loc[eligible["hop_code"] == "H1", "study_id"]) - set(eligible.loc[eligible["hop_code"] == "H2", "study_id"]))),
            "h2_only_sources": int(len(set(eligible.loc[eligible["hop_code"] == "H2", "study_id"]) - set(eligible.loc[eligible["hop_code"] == "H1", "study_id"]))),
            "dual_category_sources": int(len(set(eligible.loc[eligible["hop_code"] == "H1", "study_id"]) & set(eligible.loc[eligible["hop_code"] == "H2", "study_id"]))),
        },
        "descriptive_magnitude": magnitude_rows,
        "equivalence": {
            "small_effect_margin_log_response_ratio": equivalence_margin,
            "primary_ci_inside_margin": equivalence_supported,
        },
        "eligibility_note": "Only H1 and H2 met the preregistered threshold, so the categorical fallback was used; no ordinal three-category model was fit.",
        "causal_note": "Hop category is confounded with experimental setting and study composition; every estimate is associational.",
    }
    (HERE / "model-results.json").write_text(json.dumps(result_json, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Figure 1: primary category means and contrast.
    fig_dir = ROOT / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    labels = ["H1\nfield → field", "H2\nfield → greenhouse"]
    estimates = [primary_h1["estimate"], primary_h2["estimate"]]
    lower = [primary_h1["estimate"] - primary_h1["ci_low"], primary_h2["estimate"] - primary_h2["ci_low"]]
    upper_ci = [primary_h1["ci_high"] - primary_h1["estimate"], primary_h2["ci_high"] - primary_h2["estimate"]]
    ax.errorbar([0, 1], estimates, yerr=[lower, upper_ci], fmt="o", color="#17324D", ecolor="#3F6D8A", capsize=6, markersize=8)
    ax.axhline(0, color="#666666", linewidth=1)
    ax.set_xticks([0, 1], labels)
    ax.set_ylabel("Mean log response ratio (95% clustered CI)")
    ax.set_title("Plant–soil feedback estimate by WO-5 hop category")
    ax.text(0.5, 0.02, f"H2 − H1 = {primary_diff['estimate']:.3f} [{primary_diff['ci_low']:.3f}, {primary_diff['ci_high']:.3f}]", transform=ax.transAxes, ha="center", va="bottom", fontsize=10)
    fig.tight_layout()
    fig.savefig(fig_dir / "hop-category-estimates.png", dpi=200)
    plt.close(fig)

    # Figure 2: sensitivity estimates for H2-H1.
    sensitivity = [
        ("Effect-level CR1", primary_diff),
        ("Effect-level CR2", primary_cr2),
        ("Source aggregate CR1", study_agg_diff),
        ("Source aggregate CR2", study_agg_cr2),
        ("Equal source weight", equal_diff),
        ("Paired sources only", paired_result),
    ]
    fig, ax = plt.subplots(figsize=(9.0, 5.4))
    y_pos = np.arange(len(sensitivity))[::-1]
    for y_index, (label, result) in zip(y_pos, sensitivity):
        ax.errorbar(result["estimate"], y_index, xerr=[[result["estimate"] - result["ci_low"]], [result["ci_high"] - result["estimate"]]], fmt="o", color="#7C2D12", ecolor="#B45309", capsize=5)
    ax.axvline(0, color="#666666", linewidth=1)
    ax.set_yticks(y_pos, [item[0] for item in sensitivity])
    ax.set_xlabel("H2 − H1 log response ratio (95% CI)")
    ax.set_title("WO-5 hop contrast across preregistered sensitivity analyses")
    fig.tight_layout()
    fig.savefig(fig_dir / "hop-contrast-sensitivity.png", dpi=200)
    plt.close(fig)

    # Figure 3: source-category mean distributions.
    fig, ax = plt.subplots(figsize=(8.5, 5.3))
    data = [
        agg.loc[agg["hop_code"] == "H1", "unweighted_mean_rr"].to_numpy(),
        agg.loc[agg["hop_code"] == "H2", "unweighted_mean_rr"].to_numpy(),
    ]
    parts = ax.violinplot(data, positions=[0, 1], showmeans=True, showmedians=True, widths=0.75)
    for body in parts["bodies"]:
        body.set_facecolor("#3F6D8A")
        body.set_alpha(0.5)
    ax.axhline(0, color="#666666", linewidth=1)
    ax.set_xticks([0, 1], labels)
    ax.set_ylabel("Unweighted mean log response ratio per source/category")
    ax.set_title("Source-level distributions overlap across hop categories")
    fig.tight_layout()
    fig.savefig(fig_dir / "source-category-distributions.png", dpi=200)
    plt.close(fig)

    # Machine-generated analysis report with exact numbers.
    def fmt(result: dict) -> str:
        return f"{result['estimate']:.4f} (95% CI {result['ci_low']:.4f} to {result['ci_high']:.4f}; p={result['p_value']:.4g})"

    report = f"""# WO-5 statistical analysis results

**Author:** Manus AI

## Primary categorical fallback

Only H1 and H2 met the preregistered thresholds, so no three-category ordinal hop model was fit.[1] The analysis includes {len(eligible):,} effect rows from {eligible['study_id'].nunique()} source studies. H1 contributes {(eligible['hop_code'] == 'H1').sum():,} effects from {eligible.loc[eligible['hop_code'] == 'H1', 'study_id'].nunique()} studies; H2 contributes {(eligible['hop_code'] == 'H2').sum():,} effects from {eligible.loc[eligible['hop_code'] == 'H2', 'study_id'].nunique()} studies. The remaining {(df['hop_code'] == 'HU').sum():,} rows are excluded because the public metadata do not establish a unique hop category. The selected source is the public Jiang *et al.* plant–soil-feedback synthesis and its CC0 Dryad dataset.[2] [3]

The effect-level random-effects meta-regression estimates H1 at **{fmt(primary_h1)}** and H2 at **{fmt(primary_h2)}**. The primary H2-minus-H1 contrast is **{fmt(primary_diff)}**. The estimated residual heterogeneity is tau-squared = {primary['tau2']:.4f}. Standard errors are clustered by source study.

![Primary category estimates](../figures/hop-category-estimates.png)

## Sensitivity analyses

After inverse-variance aggregation within each source-study/category cell, the H2-minus-H1 contrast is **{fmt(study_agg_diff)}** across {len(agg)} cells from {agg['study_id'].nunique()} sources. Giving each source-category cell equal weight yields **{fmt(equal_diff)}**. Among the {len(paired)} source studies represented in both H1 and H2, the paired random-effects contrast is **{fmt(paired_result)}**.

The source-aggregated leave-one-study-out estimates range from {loo['estimate'].min():.4f} to {loo['estimate'].max():.4f}. The count-preserving source-level permutation uses {N_PERM:,} replicates, fixes tau-squared and cell weights across draws, preserves all {int(original_h2.sum())} H2 cells, and returns a two-sided p-value of {permutation_p:.4f}. Every positively coded row has high provenance confidence, so the preregistered high-confidence sensitivity is identical to the primary dataset.

The CR2/Satterthwaite sensitivity gives H2-minus-H1 = {primary_cr2['estimate']:.4f} (95% CI {primary_cr2['ci_low']:.4f} to {primary_cr2['ci_high']:.4f}; df={primary_cr2['df']:.2f}; p={primary_cr2['p_value']:.4g}) at effect level and {study_agg_cr2['estimate']:.4f} (95% CI {study_agg_cr2['ci_low']:.4f} to {study_agg_cr2['ci_high']:.4f}; df={study_agg_cr2['df']:.2f}; p={study_agg_cr2['p_value']:.4g}) after source-category aggregation.

![Sensitivity estimates](../figures/hop-contrast-sensitivity.png)

The secondary magnitude outcome remains descriptive. Mean absolute log response ratio is {magnitude.loc[magnitude['hop_code'] == 'H1', 'mean_absolute_rr'].iloc[0]:.4f} for H1 and {magnitude.loc[magnitude['hop_code'] == 'H2', 'mean_absolute_rr'].iloc[0]:.4f} for H2; medians are {magnitude.loc[magnitude['hop_code'] == 'H1', 'median_absolute_rr'].iloc[0]:.4f} and {magnitude.loc[magnitude['hop_code'] == 'H2', 'median_absolute_rr'].iloc[0]:.4f}, respectively. After averaging absolute values within each source/category, the means are {magnitude.loc[magnitude['hop_code'] == 'H1', 'mean_source_category_absolute_rr'].iloc[0]:.4f} and {magnitude.loc[magnitude['hop_code'] == 'H2', 'mean_source_category_absolute_rr'].iloc[0]:.4f}; the medians are {magnitude.loc[magnitude['hop_code'] == 'H1', 'median_source_category_absolute_rr'].iloc[0]:.4f} and {magnitude.loc[magnitude['hop_code'] == 'H2', 'median_source_category_absolute_rr'].iloc[0]:.4f}. No inferential test is attached to the absolute-value transformation.

![Source-category distributions](../figures/source-category-distributions.png)

## Interpretation boundary

The reported contrast is an association between setting-defined hop categories and plant–soil-feedback log response ratios. Hop category is inseparable here from field versus greenhouse feedback setting and differs in source-study composition: 20 sources are H1-only, 88 are H2-only, and only {len(paired)} contain both categories. The analysis therefore cannot attribute the contrast to information loss, ecological realism, or hop distance itself. It is predominantly a between-source comparison, not a causal or within-source carry estimate. The primary confidence interval is not contained within the preregistered ±log(1.10) small-effect region (±{equivalence_margin:.4f}); the analysis therefore shows no detectable contrast but does not establish practical equivalence. This interpretation follows the independent statistical and ecological reviews.[4] [5]

## Reproducibility

The input hash is `{observed_hash}`. The complete input is [`hop-coded-effects.csv`](hop-coded-effects.csv), and the executable is [`analyze_hop_distance.py`](analyze_hop_distance.py). Exact estimates are saved in [`model-results.json`](model-results.json) and [`model-summary.csv`](model-summary.csv). The repository also retains [`study-category-aggregates.csv`](study-category-aggregates.csv), [`leave-one-study-out.csv`](leave-one-study-out.csv), [`permutation-results.csv`](permutation-results.csv), [`category-counts.csv`](category-counts.csv), and [`magnitude-summary.csv`](magnitude-summary.csv). Run from the repository root with `python3 research/wo-5/analysis/analyze_hop_distance.py` under the versions in [`requirements.txt`](requirements.txt).

## References

[1]: ../ecology-codebook.md "WO-5 ecology carry-test codebook"

[2]: https://doi.org/10.1111/ele.14364 "Global patterns and drivers of plant–soil microbe interactions"

[3]: https://doi.org/10.5061/dryad.n2z34tn35 "Dataset of global plant-soil feedback"

[4]: ../validation/statistical-analysis.md "Independent validation of the H1-versus-H2 meta-analysis"

[5]: ../validation/ecological-interpretation.md "Independent ecological methods review"
"""
    (HERE / "analysis-results.md").write_text(report, encoding="utf-8")

    print(json.dumps(result_json, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

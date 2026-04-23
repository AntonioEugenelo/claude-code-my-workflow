import json
import math
from pathlib import Path
import importlib.util

import pandas as pd
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
MCMS_DIR = ROOT / "master_supporting_docs" / "MCMS"
OUTPUT_DIR = ROOT / "explorations" / "section5_unit_elasticity_check" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CURRENT_EXTRA_CHARTS = MCMS_DIR / "output_python" / "extra_charts"
ELASTICITY_TS = CURRENT_EXTRA_CHARTS / "Figure_4_UnitElast_vs_HighElast_TimeSeries.csv"


def load_new_process():
    module_path = MCMS_DIR / "new_process.py"
    spec = importlib.util.spec_from_file_location("mcms_new_process", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    cwd_before = Path.cwd()
    try:
        import os
        os.chdir(MCMS_DIR)
        spec.loader.exec_module(module)
    finally:
        os.chdir(cwd_before)
    return module


def materialize_variant(module, label, suffix, baseline_file):
    out_dir = OUTPUT_DIR / label
    out_dir.mkdir(parents=True, exist_ok=True)

    cwd_before = Path.cwd()
    try:
        import os
        os.chdir(MCMS_DIR)
        module.UNIT_ELAST_SUFFIX = suffix
        module.BASELINE_MAT = str(Path("output_matlab") / baseline_file)
        module.export_standard_jobs_from_mat(
            str(out_dir),
            allowed_fig_ids={"Figure_6"},
            cross_fig_ids={"Figure_6"},
            ts_fig_ids=set(),
        )
        module.create_sectoral_spillover_matrix(str(out_dir), cross_csv=str(out_dir / "Figure_6_Baseline_Bars_CrossSection.csv"))
        module.extract_benchmark_transmission_decomposition(str(out_dir), shock_pair=(4, 2), horizon=module.HORIZON)
    finally:
        os.chdir(cwd_before)

    return {
        "cross": out_dir / "Figure_6_Baseline_Bars_CrossSection.csv",
        "spill": out_dir / "Figure_SectoralSpillover_Matrix.csv",
        "trans": out_dir / "Figure_1_Benchmark_Transmission_Decomposition.csv",
    }


def read_csvs(paths):
    cross = pd.read_csv(paths["cross"])
    spill = pd.read_csv(paths["spill"])
    trans = pd.read_csv(paths["trans"])
    return cross, spill, trans


def normalize_sector_name(name):
    normalized = name.replace("&", "and").replace("  ", " ").strip().lower()
    replacements = {
        "other manuf": "other manufacturing",
        "elec equip": "electrical equipment",
        "agri and forestry": "agri and forestry",
    }
    for src, dst in replacements.items():
        normalized = normalized.replace(src, dst)
    return normalized.title()


def top_sectors(df, column, top_n=3, ascending=True):
    subset = df[["Description", column]].copy()
    subset["Description"] = subset["Description"].map(normalize_sector_name)
    subset = subset.sort_values(column, ascending=ascending).head(top_n)
    return [
        {"sector": row["Description"], "value": float(row[column])}
        for _, row in subset.iterrows()
    ]


def top_positive_sectors(df, column, top_n=3):
    subset = df[["Description", column]].copy()
    subset["Description"] = subset["Description"].map(normalize_sector_name)
    subset = subset.sort_values(column, ascending=False).head(top_n)
    return [
        {"sector": row["Description"], "value": float(row[column])}
        for _, row in subset.iterrows()
    ]


def spillover_summary(spill_df, country_code):
    subset = spill_df.loc[spill_df["country"] == country_code].copy()
    summaries = []
    for sector, group in subset.groupby("shocked_sector"):
        own = float(group.loc[group["shocked_sector"] == group["responding_sector"], "gdp_contribution"].sum())
        total = float(group["gdp_contribution"].sum())
        cross = total - own
        gross_cross_share = abs(cross) / (abs(own) + abs(cross)) if (abs(own) + abs(cross)) else math.nan
        service_mask = group["responding_sector_id"].between(25, 44)
        service_cross_abs = float(group.loc[service_mask & (group["responding_sector"] != group["shocked_sector"]), "gdp_contribution"].abs().sum())
        total_cross_abs = float(group.loc[group["responding_sector"] != group["shocked_sector"], "gdp_contribution"].abs().sum())
        service_share = service_cross_abs / total_cross_abs if total_cross_abs else math.nan
        summaries.append(
            {
                "sector": normalize_sector_name(sector),
                "own": own,
                "cross": cross,
                "total": total,
                "gross_cross_share": gross_cross_share,
                "service_share": service_share,
            }
        )
    result = pd.DataFrame(summaries).sort_values("sector").reset_index(drop=True)
    return result


def aggregate_spill_metrics(spill_summary):
    gross_cross = float(spill_summary["cross"].abs().sum())
    gross_total = float((spill_summary["own"].abs() + spill_summary["cross"].abs()).sum())
    service_share_median = float(spill_summary["service_share"].median())
    service_share_gt_half = int((spill_summary["service_share"] > 0.5).sum())
    cross_gt_own = int((spill_summary["cross"].abs() > spill_summary["own"].abs()).sum())
    return {
        "gross_cross_share": gross_cross / gross_total if gross_total else math.nan,
        "median_service_share": service_share_median,
        "service_share_gt_half_count": service_share_gt_half,
        "cross_gt_own_count": cross_gt_own,
    }


def find_sector(df, sector_name):
    return df.loc[df["Description"].map(normalize_sector_name) == sector_name].iloc[0]


def aggregate_totals(cross_df):
    totals = {}
    for country in ["USA", "CHN", "EA"]:
        totals[country] = {
            "gdp": float(cross_df[f"GDP_{country}_Benchmark"].sum()),
            "cons": float(cross_df[f"Cons_{country}_Benchmark"].sum()),
            "cpi": float(cross_df[f"CPI_{country}_Benchmark"].sum()),
        }
    return totals


def sign_counts(cross_df):
    return {
        "USA_positive_own_va": int((cross_df["Sec_VA_USA_Benchmark"] > 0).sum()),
        "CHN_negative_own_va": int((cross_df["Sec_VA_CHN_Benchmark"] < 0).sum()),
        "EA_positive_own_va": int((cross_df["Sec_VA_EA_Benchmark"] > 0).sum()),
        "EA_positive_own_negative_agg": int(
            ((cross_df["Sec_VA_EA_Benchmark"] > 0) & (cross_df["GDP_EA_Benchmark"] < 0)).sum()
        ),
        "USA_positive_own_negative_agg": int(
            ((cross_df["Sec_VA_USA_Benchmark"] > 0) & (cross_df["GDP_USA_Benchmark"] < 0)).sum()
        ),
    }


def impact_from_elasticity_ts():
    df = pd.read_csv(ELASTICITY_TS)
    row = df.iloc[0]
    return {
        "unit": {
            "USA_gdp": float(row["y_USA_UnitElast"]),
            "CHN_gdp": float(row["y_CHN_UnitElast"]),
            "EA_gdp": float(row["y_EA_UnitElast"]),
            "USA_cons": float(row["c_USA_UnitElast"]),
            "CHN_cons": float(row["c_CHN_UnitElast"]),
            "EA_cons": float(row["c_EA_UnitElast"]),
            "EA_exports": float(row["exp_EA_UnitElast"]),
            "EA_imports": float(row["imp_EA_UnitElast"]),
        },
        "high": {
            "USA_gdp": float(row["y_USA_HighElast"]),
            "CHN_gdp": float(row["y_CHN_HighElast"]),
            "EA_gdp": float(row["y_EA_HighElast"]),
            "USA_cons": float(row["c_USA_HighElast"]),
            "CHN_cons": float(row["c_CHN_HighElast"]),
            "EA_cons": float(row["c_EA_HighElast"]),
            "EA_exports": float(row["exp_EA_HighElast"]),
            "EA_imports": float(row["imp_EA_HighElast"]),
        },
    }


def compare_variants(high_cross, high_spill, high_trans, unit_cross, unit_spill, unit_trans):
    summary = {}

    summary["aggregate_bars"] = {
        "USA_top_negative_gdp": {
            "high": top_sectors(high_cross, "GDP_USA_Benchmark"),
            "unit": top_sectors(unit_cross, "GDP_USA_Benchmark"),
        },
        "CHN_top_negative_gdp": {
            "high": top_sectors(high_cross, "GDP_CHN_Benchmark"),
            "unit": top_sectors(unit_cross, "GDP_CHN_Benchmark"),
        },
        "EA_top_gdp_by_abs": {
            "high": (
                high_cross.assign(abs_val=high_cross["GDP_EA_Benchmark"].abs())
                .sort_values("abs_val", ascending=False)
                .head(3)[["Description", "GDP_EA_Benchmark"]]
                .assign(Description=lambda df: df["Description"].map(normalize_sector_name))
                .rename(columns={"GDP_EA_Benchmark": "value"})
                .to_dict("records")
            ),
            "unit": (
                unit_cross.assign(abs_val=unit_cross["GDP_EA_Benchmark"].abs())
                .sort_values("abs_val", ascending=False)
                .head(3)[["Description", "GDP_EA_Benchmark"]]
                .assign(Description=lambda df: df["Description"].map(normalize_sector_name))
                .rename(columns={"GDP_EA_Benchmark": "value"})
                .to_dict("records")
            ),
        },
        "USA_top_cpi": {
            "high": top_positive_sectors(high_cross, "CPI_USA_Benchmark"),
            "unit": top_positive_sectors(unit_cross, "CPI_USA_Benchmark"),
        },
    }

    high_usa_spill = spillover_summary(high_spill, "USA")
    unit_usa_spill = spillover_summary(unit_spill, "USA")
    high_chn_spill = spillover_summary(high_spill, "CHN")
    unit_chn_spill = spillover_summary(unit_spill, "CHN")

    summary["spillovers"] = {
        "USA_aggregate": {
            "high": aggregate_spill_metrics(high_usa_spill),
            "unit": aggregate_spill_metrics(unit_usa_spill),
        },
        "CHN_aggregate": {
            "high": aggregate_spill_metrics(high_chn_spill),
            "unit": aggregate_spill_metrics(unit_chn_spill),
        },
        "USA_textiles": {
            "high": high_usa_spill.loc[high_usa_spill["sector"] == "Textiles"].iloc[0].to_dict(),
            "unit": unit_usa_spill.loc[unit_usa_spill["sector"] == "Textiles"].iloc[0].to_dict(),
        },
        "USA_electronics": {
            "high": high_usa_spill.loc[high_usa_spill["sector"] == "Electronics"].iloc[0].to_dict(),
            "unit": unit_usa_spill.loc[unit_usa_spill["sector"] == "Electronics"].iloc[0].to_dict(),
        },
        "CHN_textiles": {
            "high": high_chn_spill.loc[high_chn_spill["sector"] == "Textiles"].iloc[0].to_dict(),
            "unit": unit_chn_spill.loc[unit_chn_spill["sector"] == "Textiles"].iloc[0].to_dict(),
        },
        "CHN_electronics": {
            "high": high_chn_spill.loc[high_chn_spill["sector"] == "Electronics"].iloc[0].to_dict(),
            "unit": unit_chn_spill.loc[unit_chn_spill["sector"] == "Electronics"].iloc[0].to_dict(),
        },
    }

    ea_high = {
        "top_negative_gdp": top_sectors(high_cross, "GDP_EA_Benchmark"),
        "top_positive_va": top_positive_sectors(high_cross, "Sec_VA_EA_Benchmark"),
        "aggregate_totals": aggregate_totals(high_cross)["EA"],
        "sign_counts": sign_counts(high_cross),
    }
    ea_unit = {
        "top_negative_gdp": top_sectors(unit_cross, "GDP_EA_Benchmark"),
        "top_positive_va": top_positive_sectors(unit_cross, "Sec_VA_EA_Benchmark"),
        "aggregate_totals": aggregate_totals(unit_cross)["EA"],
        "sign_counts": sign_counts(unit_cross),
    }
    summary["ea"] = {"high": ea_high, "unit": ea_unit}
    summary["aggregate_totals"] = {
        "high": aggregate_totals(high_cross),
        "unit": aggregate_totals(unit_cross),
    }
    summary["impact_totals_from_ts"] = impact_from_elasticity_ts()

    current_claim_checks = {}
    for sector in ["Textiles", "Electronics", "Other Manufacturing"]:
        current_claim_checks[sector] = {
            "USA_gdp_high": float(find_sector(high_cross, sector)["GDP_USA_Benchmark"]),
            "USA_gdp_unit": float(find_sector(unit_cross, sector)["GDP_USA_Benchmark"]),
            "CHN_gdp_high": float(find_sector(high_cross, sector)["GDP_CHN_Benchmark"]),
            "CHN_gdp_unit": float(find_sector(unit_cross, sector)["GDP_CHN_Benchmark"]),
            "USA_va_high": float(find_sector(high_cross, sector)["Sec_VA_USA_Benchmark"]),
            "USA_va_unit": float(find_sector(unit_cross, sector)["Sec_VA_USA_Benchmark"]),
            "CHN_va_high": float(find_sector(high_cross, sector)["Sec_VA_CHN_Benchmark"]),
            "CHN_va_unit": float(find_sector(unit_cross, sector)["Sec_VA_CHN_Benchmark"]),
        }
    summary["claim_checks"] = current_claim_checks

    return summary


def main():
    module = load_new_process()
    high_paths = {
        "cross": CURRENT_EXTRA_CHARTS / "Figure_6_Baseline_Bars_CrossSection.csv",
        "spill": CURRENT_EXTRA_CHARTS / "Figure_SectoralSpillover_Matrix.csv",
        "trans": CURRENT_EXTRA_CHARTS / "Figure_1_Benchmark_Transmission_Decomposition.csv",
    }
    unit_paths = materialize_variant(module, "unit_elast", "_UnitElast", "irf_Het_DCP_Baseline_UnitElast.mat")

    high_cross, high_spill, high_trans = read_csvs(high_paths)
    unit_cross, unit_spill, unit_trans = read_csvs(unit_paths)

    summary = compare_variants(high_cross, high_spill, high_trans, unit_cross, unit_spill, unit_trans)

    (OUTPUT_DIR / "section5_comparison_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    key_rows = []
    for sector in ["Textiles", "Electronics", "Other Manufacturing"]:
        sector_row = summary["claim_checks"][sector]
        key_rows.append(
            {
                "sector": sector,
                "USA_gdp_high": sector_row["USA_gdp_high"],
                "USA_gdp_unit": sector_row["USA_gdp_unit"],
                "CHN_gdp_high": sector_row["CHN_gdp_high"],
                "CHN_gdp_unit": sector_row["CHN_gdp_unit"],
                "USA_va_high": sector_row["USA_va_high"],
                "USA_va_unit": sector_row["USA_va_unit"],
                "CHN_va_high": sector_row["CHN_va_high"],
                "CHN_va_unit": sector_row["CHN_va_unit"],
            }
        )
    pd.DataFrame(key_rows).to_csv(OUTPUT_DIR / "key_sector_comparison.csv", index=False)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

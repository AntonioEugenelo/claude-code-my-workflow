import json
import re
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
MCMS = ROOT / "master_supporting_docs" / "MCMS"
PAPER = ROOT / "master_supporting_docs" / "Tariffs_ECB" / "0_clean" / "sections"
EXTRA = MCMS / "output_python" / "extra_charts"
OUT = ROOT / "explorations" / "full_paper_mcms_audit" / "output"


def avg_3yr(series: pd.Series) -> float:
    return float(series.iloc[:12].mean())


def rolling_4q_sum(series: pd.Series) -> pd.Series:
    return series.rolling(4, min_periods=1).sum()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_first_float(pattern: str, text: str) -> float | None:
    match = re.search(pattern, text, flags=re.MULTILINE)
    return float(match.group(1)) if match else None


def parse_calibration() -> dict:
    text = read_text(MCMS / "a1_calibration.m")

    def line_value(name: str) -> float | None:
        return extract_first_float(rf"{re.escape(name)}\s*=\s*([0-9.]+)", text)

    pcp_match = re.search(r"Ind_PCP\(\[([^\]]+)\]\)\s*=\s*1;", text)
    lcp_match = re.search(r"Ind_LCP\(\[([^\]]+)\]\)\s*=\s*1;", text)

    def expand(expr: str) -> list[int]:
        vals: list[int] = []
        for token in expr.split(","):
            token = token.strip()
            if ":" in token:
                start, end = token.split(":")
                vals.extend(range(int(start), int(end) + 1))
            else:
                vals.append(int(token))
        return vals

    pcp = expand(pcp_match.group(1)) if pcp_match else []
    lcp = expand(lcp_match.group(1)) if lcp_match else []

    armington_household = {}
    armington_firm = {}
    current = None
    for line in text.splitlines():
        if line.strip().startswith("if armington ==") or line.strip().startswith("elseif armington =="):
            current = int(re.search(r"armington == ([0-9]+)", line).group(1))
        elif "Delta_C" in line and "=" in line and current is not None:
            val = float(re.search(r"Delta_C\s*=\s*([0-9.]+)", line).group(1))
            armington_household[current] = val
        elif "Delta_X" in line and "=" in line and current is not None:
            val = float(re.search(r"Delta_X\s*=\s*([0-9.]+)", line).group(1))
            armington_firm[current] = val

    return {
        "countries": int(line_value("Knum")),
        "sectors": int(line_value("Inum")),
        "energy_sectors": int(line_value("Inum_E")),
        "services_sectors": 21,
        "tradeable_manufacturing_sectors": 20,
        "beta": line_value("Beta"),
        "sigma": line_value("Sigma"),
        "varphi": line_value("Varphi"),
        "gamma_star": line_value("Gamma_star"),
        "gamma_c": line_value("Gamma_C"),
        "eta_c": line_value("Eta_C"),
        "iota_c": line_value("Iota_C"),
        "gamma_x": line_value("Gamma_X"),
        "eta_x": line_value("Eta_X"),
        "iota_x": line_value("Iota_X"),
        "theta_w": 0.75,
        "phi_pi": 1.5,
        "phi_y": 0.0,
        "phi_delta_pi": 0.0,
        "phi_delta_y": 0.125,
        "rho_r": 0.7,
        "rho_tau": 0.96,
        "sigma_tau": 1.0,
        "sigma_r": 1.0,
        "pcp_count": len(pcp),
        "lcp_count": len(lcp),
        "dcp_count": 44 - len(pcp) - len(lcp),
        "armington_map_household": armington_household,
        "armington_map_firm": armington_firm,
    }


def build_figure_pipeline() -> dict[str, dict]:
    text = read_text(MCMS / "new_process.py")
    jobs: dict[str, dict] = {}
    current: dict[str, object] | None = None
    collecting_files = False
    file_buffer: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if line == "{":
            current = {}
        elif current is not None and line.startswith("'fig_id':"):
            current["fig_id"] = re.search(r"'fig_id': '([^']+)'", line).group(1)
        elif current is not None and line.startswith("'files':"):
            file_buffer = re.findall(r"'([^']+\.mat)'", line)
            collecting_files = "]" not in line
            if not collecting_files:
                current["files"] = file_buffer
        elif current is not None and collecting_files:
            file_buffer.extend(re.findall(r"'([^']+\.mat)'", line))
            if "]" in line:
                current["files"] = file_buffer
                collecting_files = False
        elif current is not None and line.startswith("'desc':"):
            current["desc"] = re.search(r"'desc': '([^']+)'", line).group(1)
        elif current is not None and line.startswith("'shock_pair':"):
            m = re.search(r"\((\d+),\s*(\d+)\)", line)
            current["shock_pair"] = [int(m.group(1)), int(m.group(2))]
        elif current is not None and line.startswith("'cumulative':"):
            current["cumulative"] = "True" in line
        elif current is not None and line == "},":
            fig_id = current.get("fig_id")
            if fig_id:
                jobs[str(fig_id)] = current
            current = None
    return jobs


def build_benchmark_metrics() -> dict:
    ts = pd.read_csv(EXTRA / "Figure_1_Benchmark_IRFs_TimeSeries.csv")
    rev = pd.read_csv(EXTRA / "Figure_1b_Benchmark_Reverse_IRFs_TimeSeries.csv")
    io = pd.read_csv(EXTRA / "Figure_2_Cumul_IO_Decomposition_TimeSeries.csv")
    io_diff = io.diff()
    io_diff.iloc[0] = io.iloc[0]
    elast = pd.read_csv(EXTRA / "Figure_4_UnitElast_vs_HighElast_TimeSeries.csv")
    peg = pd.read_csv(EXTRA / "Figure_5a_Benchmark_vs_Peg_TimeSeries.csv")
    dcp = pd.read_csv(EXTRA / "Figure_17_DCP_PCP_FullDCP_TimeSeries.csv")
    monpol = pd.read_csv(EXTRA / "Figure_18_Benchmark_vs_NoMonPol_TimeSeries.csv")

    return {
        "benchmark_forward": {
            "us_gdp_q1": float(ts["y_USA_Benchmark"].iloc[0]),
            "us_gdp_q8": float(ts["y_USA_Benchmark"].iloc[7]),
            "chn_gdp_q1": float(ts["y_CHN_Benchmark"].iloc[0]),
            "chn_gdp_q12": float(ts["y_CHN_Benchmark"].iloc[11]),
            "ea_gdp_q1": float(ts["y_EA_Benchmark"].iloc[0]),
            "ea_gdp_q5": float(ts["y_EA_Benchmark"].iloc[4]),
            "us_cpi_q1": float(ts["piC_USA_Benchmark"].iloc[0]),
            "us_cpi_q4_rolling": float(rolling_4q_sum(ts["piC_USA_Benchmark"]).iloc[3]),
            "chn_cpi_q1": float(ts["piC_CHN_Benchmark"].iloc[0]),
            "ea_cpi_q1": float(ts["piC_EA_Benchmark"].iloc[0]),
            "ea_cpi_turns_negative_q": int(np.where(rolling_4q_sum(ts["piC_EA_Benchmark"]).to_numpy() < 0)[0][0] + 1),
            "us_tb_q1": float((ts["exp_USA_Benchmark"] - ts["imp_USA_Benchmark"]).iloc[0]),
            "us_tb_q12": float((ts["exp_USA_Benchmark"] - ts["imp_USA_Benchmark"]).iloc[11]),
            "chn_tb_q1": float((ts["exp_CHN_Benchmark"] - ts["imp_CHN_Benchmark"]).iloc[0]),
            "chn_tb_q12": float((ts["exp_CHN_Benchmark"] - ts["imp_CHN_Benchmark"]).iloc[11]),
            "ea_tb_q1": float((ts["exp_EA_Benchmark"] - ts["imp_EA_Benchmark"]).iloc[0]),
            "us_reer_q1": float(ts["reer_dw_USA_Benchmark"].iloc[0]),
            "chn_reer_q1": float(ts["reer_dw_CHN_Benchmark"].iloc[0]),
            "chn_reer_q12": float(ts["reer_dw_CHN_Benchmark"].iloc[11]),
            "ea_reer_q1": float(ts["reer_dw_EA_Benchmark"].iloc[0]),
            "us_cons_q1": float(ts["c_USA_Benchmark"].iloc[0]),
            "chn_cons_q1": float(ts["c_CHN_Benchmark"].iloc[0]),
            "ea_cons_q1": float(ts["c_EA_Benchmark"].iloc[0]),
            "us_i_q1": float(ts["i_USA_Benchmark"].iloc[0]),
            "ea_i_q1": float(ts["i_EA_Benchmark"].iloc[0]),
            "us_gdp_3yr": avg_3yr(ts["y_USA_Benchmark"]),
            "chn_gdp_3yr": avg_3yr(ts["y_CHN_Benchmark"]),
            "ea_gdp_3yr": avg_3yr(ts["y_EA_Benchmark"]),
            "us_cpi_3yr_avg_4q": avg_3yr(rolling_4q_sum(ts["piC_USA_Benchmark"])),
            "ea_cons_3yr": avg_3yr(ts["c_EA_Benchmark"]),
            "ea_tb_3yr": avg_3yr(ts["exp_EA_Benchmark"] - ts["imp_EA_Benchmark"]),
        },
        "benchmark_reverse": {
            "us_gdp_q1": float(rev["y_USA_Reverse"].iloc[0]),
            "chn_gdp_q1": float(rev["y_CHN_Reverse"].iloc[0]),
            "ea_gdp_q1": float(rev["y_EA_Reverse"].iloc[0]),
            "us_cpi_q11_rolling": float(rolling_4q_sum(rev["piC_USA_Reverse"]).iloc[10]),
            "chn_cpi_q1": float(rev["piC_CHN_Reverse"].iloc[0]),
            "us_tb_q1": float((rev["exp_USA_Reverse"] - rev["imp_USA_Reverse"]).iloc[0]),
            "chn_tb_q1": float((rev["exp_CHN_Reverse"] - rev["imp_CHN_Reverse"]).iloc[0]),
            "ea_tb_q1": float((rev["exp_EA_Reverse"] - rev["imp_EA_Reverse"]).iloc[0]),
            "us_reer_q1": float(rev["reer_dw_USA_Reverse"].iloc[0]),
            "chn_reer_q1": float(rev["reer_dw_CHN_Reverse"].iloc[0]),
            "chn_cons_q1": float(rev["c_CHN_Reverse"].iloc[0]),
            "chn_cons_q2": float(rev["c_CHN_Reverse"].iloc[1]),
        },
        "io_robustness": {
            "chn_gdp_3yr_benchmark": avg_3yr(io_diff["y_CHN_Benchmark"]),
            "chn_gdp_3yr_zero_intl": avg_3yr(io_diff["y_CHN_IO_Zero_Intl"]),
            "chn_gdp_3yr_zero_both": avg_3yr(io_diff["y_CHN_IO_Zero_Both"]),
        },
        "elasticity_robustness": {
            "chn_gdp_3yr_unit": avg_3yr(elast["y_CHN_UnitElast"]),
            "chn_gdp_3yr_high": avg_3yr(elast["y_CHN_HighElast"]),
        },
        "peg_robustness": {
            "usa_gdp_3yr_benchmark": avg_3yr(peg["y_USA_Benchmark"]),
            "chn_gdp_3yr_benchmark": avg_3yr(peg["y_CHN_Benchmark"]),
            "ea_gdp_3yr_benchmark": avg_3yr(peg["y_EA_Benchmark"]),
            "usa_gdp_3yr_peg": avg_3yr(peg["y_USA_Peg"]),
            "chn_gdp_3yr_peg": avg_3yr(peg["y_CHN_Peg"]),
            "ea_gdp_3yr_peg": avg_3yr(peg["y_EA_Peg"]),
        },
        "dcp_robustness": {
            "chn_gdp_3yr_heterogeneous": avg_3yr(dcp["y_CHN_Heterogeneous"]),
            "chn_gdp_3yr_pcp": avg_3yr(dcp["y_CHN_PCP"]),
            "chn_gdp_3yr_full_dcp": avg_3yr(dcp["y_CHN_Full_DCP"]),
            "ea_gdp_3yr_heterogeneous": avg_3yr(dcp["y_EA_Heterogeneous"]),
            "ea_gdp_3yr_pcp": avg_3yr(dcp["y_EA_PCP"]),
            "ea_gdp_3yr_full_dcp": avg_3yr(dcp["y_EA_Full_DCP"]),
        },
        "monpol_robustness": {
            "usa_gdp_3yr_benchmark": avg_3yr(monpol["y_USA_Benchmark"]),
            "usa_gdp_3yr_no_monpol": avg_3yr(monpol["y_USA_NoMonPol"]),
            "chn_gdp_3yr_benchmark": avg_3yr(monpol["y_CHN_Benchmark"]),
            "chn_gdp_3yr_no_monpol": avg_3yr(monpol["y_CHN_NoMonPol"]),
            "ea_gdp_3yr_benchmark": avg_3yr(monpol["y_EA_Benchmark"]),
            "ea_gdp_3yr_no_monpol": avg_3yr(monpol["y_EA_NoMonPol"]),
            "us_cpi_3yr_benchmark": avg_3yr(rolling_4q_sum(monpol["piC_USA_Benchmark"])),
            "us_cpi_3yr_no_monpol": avg_3yr(rolling_4q_sum(monpol["piC_USA_NoMonPol"])),
            "chn_cpi_3yr_benchmark": avg_3yr(rolling_4q_sum(monpol["piC_CHN_Benchmark"])),
            "chn_cpi_3yr_no_monpol": avg_3yr(rolling_4q_sum(monpol["piC_CHN_NoMonPol"])),
            "usa_reer_q1_benchmark": float(monpol["reer_dw_USA_Benchmark"].iloc[0]),
            "usa_reer_q1_no_monpol": float(monpol["reer_dw_USA_NoMonPol"].iloc[0]),
            "ea_reer_q1_benchmark": float(monpol["reer_dw_EA_Benchmark"].iloc[0]),
            "ea_reer_q1_no_monpol": float(monpol["reer_dw_EA_NoMonPol"].iloc[0]),
            "usa_i_q1_benchmark": float(monpol["i_USA_Benchmark"].iloc[0]),
            "usa_i_q1_no_monpol": float(monpol["i_USA_NoMonPol"].iloc[0]),
            "ea_i_q1_benchmark": float(monpol["i_EA_Benchmark"].iloc[0]),
            "ea_i_q1_no_monpol": float(monpol["i_EA_NoMonPol"].iloc[0]),
        },
    }


def build_sectoral_metrics() -> dict:
    cross = pd.read_csv(EXTRA / "Figure_6_Baseline_Bars_CrossSection.csv")
    spill = pd.read_csv(EXTRA / "Figure_SectoralSpillover_Matrix.csv")

    def row(label: str) -> pd.Series:
        return cross.loc[cross["Label"] == label].iloc[0]

    service_ids = set(range(24, 45))
    energy_ids = {1, 2, 3}
    tradeable_ids = set(range(4, 24))

    country_stats: dict[str, dict] = {}
    for country in ["USA", "CHN"]:
        dfc = spill.loc[spill["country"] == country].copy()
        rows = []
        for sid, g in dfc.groupby("shocked_sector_id"):
            agg = float(g["gdp_contribution"].sum())
            own = float(g.loc[g["responding_sector_id"] == sid, "gdp_contribution"].sum())
            cross_term = agg - own
            rows.append((sid, agg, own, cross_term))
        rows_df = pd.DataFrame(rows, columns=["sid", "agg", "own", "cross"])
        abs_own = float(rows_df["own"].abs().sum())
        abs_cross = float(rows_df["cross"].abs().sum())
        cross_only = dfc.loc[dfc["responding_sector_id"] != dfc["shocked_sector_id"]]
        denom = float(cross_only["gdp_contribution"].abs().sum())
        service_shares = []
        for sid, g in cross_only.groupby("shocked_sector_id"):
            denom_i = float(g["gdp_contribution"].abs().sum())
            service_shares.append(
                float(g.loc[g["responding_sector_id"].isin(service_ids), "gdp_contribution"].abs().sum() / denom_i)
            )
        country_stats[country] = {
            "abs_cross_share": abs_cross / (abs_cross + abs_own),
            "cross_domination_count": int((rows_df["cross"].abs() > rows_df["own"].abs()).sum()),
            "service_share_pooled": float(
                cross_only.loc[cross_only["responding_sector_id"].isin(service_ids), "gdp_contribution"].abs().sum() / denom
            ),
            "tradeable_share_pooled": float(
                cross_only.loc[cross_only["responding_sector_id"].isin(tradeable_ids), "gdp_contribution"].abs().sum() / denom
            ),
            "energy_share_pooled": float(
                cross_only.loc[cross_only["responding_sector_id"].isin(energy_ids), "gdp_contribution"].abs().sum() / denom
            ),
            "service_share_min": float(np.min(service_shares)),
            "service_share_median": float(np.median(service_shares)),
            "service_share_max": float(np.max(service_shares)),
            "service_share_above_half_count": int(np.sum(np.asarray(service_shares) > 0.5)),
        }

    usa_textiles = spill.loc[(spill["country"] == "USA") & (spill["shocked_sector_id"] == 9)].copy()
    usa_electronics = spill.loc[(spill["country"] == "USA") & (spill["shocked_sector_id"] == 18)].copy()

    return {
        "aggregate_bars": {
            "usa_top_gdp": {
                "textiles": float(row("13-15")["GDP_USA_Benchmark"]),
                "electronics": float(row("26")["GDP_USA_Benchmark"]),
                "other_manuf": float(row("31-33")["GDP_USA_Benchmark"]),
            },
            "chn_top_gdp": {
                "textiles": float(row("13-15")["GDP_CHN_Benchmark"]),
                "electronics": float(row("26")["GDP_CHN_Benchmark"]),
                "other_manuf": float(row("31-33")["GDP_CHN_Benchmark"]),
            },
            "ea_headline_gdp": {
                "electronics": float(row("26")["GDP_EA_Benchmark"]),
                "pharma": float(row("21")["GDP_EA_Benchmark"]),
                "other_manuf": float(row("31-33")["GDP_EA_Benchmark"]),
            },
            "usa_top_cpi": {
                "textiles": float(row("13-15")["CPI_USA_Benchmark"]),
                "electronics": float(row("26")["CPI_USA_Benchmark"]),
                "other_manuf": float(row("31-33")["CPI_USA_Benchmark"]),
            },
            "chn_top_cpi": {
                "electronics": float(row("26")["CPI_CHN_Benchmark"]),
                "textiles": float(row("13-15")["CPI_CHN_Benchmark"]),
            },
        },
        "own_sector": {
            "usa": {
                "textiles": float(row("13-15")["Sec_VA_USA_Benchmark"]),
                "electronics": float(row("26")["Sec_VA_USA_Benchmark"]),
                "elec_equip": float(row("27")["Sec_VA_USA_Benchmark"]),
            },
            "chn": {
                "other_manuf": float(row("31-33")["Sec_VA_CHN_Benchmark"]),
                "electronics": float(row("26")["Sec_VA_CHN_Benchmark"]),
                "textiles": float(row("13-15")["Sec_VA_CHN_Benchmark"]),
                "elec_equip": float(row("27")["Sec_VA_CHN_Benchmark"]),
            },
            "ea": {
                "electronics": float(row("26")["Sec_VA_EA_Benchmark"]),
                "textiles": float(row("13-15")["Sec_VA_EA_Benchmark"]),
                "other_manuf": float(row("31-33")["Sec_VA_EA_Benchmark"]),
                "positive_own_negative_agg_count": int(
                    ((cross["Sec_VA_EA_Benchmark"] > 0) & (cross["GDP_EA_Benchmark"] < 0)).sum()
                ),
            },
        },
        "spillovers": {
            "usa": country_stats["USA"],
            "chn": country_stats["CHN"],
            "usa_textiles": {
                "agg": float(usa_textiles["gdp_contribution"].sum()),
                "own": float(usa_textiles.loc[usa_textiles["responding_sector_id"] == 9, "gdp_contribution"].sum()),
            },
            "usa_electronics": {
                "agg": float(usa_electronics["gdp_contribution"].sum()),
                "own": float(usa_electronics.loc[usa_electronics["responding_sector_id"] == 18, "gdp_contribution"].sum()),
            },
        },
    }


def find_caption_lines() -> list[dict]:
    text = read_text(PAPER / "55a_benchmark_and_robustness.tex")
    out = []
    for idx, line in enumerate(text.splitlines(), start=1):
        if "Shock:" in line and "tradeable sectors" in line:
            out.append({"line": idx, "text": line.strip()})
    return out


def baseline_mat_state() -> dict:
    path = MCMS / "output_matlab" / "irf_Het_DCP_Baseline.mat"
    return {
        "path": str(path),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else None,
    }


def file_fingerprint(path: Path) -> dict:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    stat = path.stat()
    return {
        "path": str(path),
        "size_bytes": stat.st_size,
        "mtime_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
        "sha256": digest.hexdigest(),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    evidence = {
        "provenance": {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "script": file_fingerprint(Path(__file__).resolve()),
            "key_artifacts": [
                file_fingerprint(EXTRA / "Figure_1_Benchmark_IRFs_TimeSeries.csv"),
                file_fingerprint(EXTRA / "Figure_4_UnitElast_vs_HighElast_TimeSeries.csv"),
                file_fingerprint(EXTRA / "Figure_6_Baseline_Bars_CrossSection.csv"),
                file_fingerprint(EXTRA / "Figure_SectoralSpillover_Matrix.csv"),
                file_fingerprint(MCMS / "output_matlab" / "irf_Het_DCP_Baseline.mat"),
            ],
        },
        "scope": {
            "appendix_excluded": True,
            "paper_files": [
                "11_introduction.tex",
                "43_calibration.tex",
                "55a_benchmark_and_robustness.tex",
                "56_sectoral_channels.tex",
                "60_Conclusions.tex",
            ],
        },
        "calibration": parse_calibration(),
        "figure_pipeline": build_figure_pipeline(),
        "benchmark_metrics": build_benchmark_metrics(),
        "sectoral_metrics": build_sectoral_metrics(),
        "caption_lines": find_caption_lines(),
        "baseline_mat_state": baseline_mat_state(),
    }
    (OUT / "maintext_mcms_evidence.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

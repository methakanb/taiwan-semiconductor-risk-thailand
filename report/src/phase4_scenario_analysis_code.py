from pathlib import Path
import csv
import plotly.graph_objects as go

BASE_DIR = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path(".")
PROCESSED_DIR = BASE_DIR / "data" / "processed"
VISUALS_DIR = BASE_DIR / "visuals"

if not (PROCESSED_DIR / "industry_revenue_at_risk_results.csv").exists():
    PROCESSED_DIR = BASE_DIR / "processed"
if not VISUALS_DIR.exists():
    VISUALS_DIR.mkdir(exist_ok=True)

with open(PROCESSED_DIR / "industry_revenue_at_risk_results.csv", newline="", encoding="utf-8") as f:
    industry_rows = list(csv.DictReader(f))

scenario_defs = [
    {"scenario": "Mild", "severity_pct": 10, "severity_factor": 0.10},
    {"scenario": "Moderate", "severity_pct": 20, "severity_factor": 0.20},
    {"scenario": "Severe", "severity_pct": 40, "severity_factor": 0.40},
]

wide_rows = []
long_rows = []
for row in industry_rows:
    rar = float(row["revenue_at_risk_base_usd_bn"])
    out = {
        "industry": row["industry"],
        "production_value_usd_bn": row["production_value_usd_bn"],
        "revenue_at_risk_base_usd_bn": f"{rar:.6f}",
        "risk_level": row.get("risk_level", ""),
        "confidence_level": row.get("confidence_level", ""),
    }
    for s in scenario_defs:
        impact = rar * s["severity_factor"]
        scen = s["scenario"].lower()
        pct = s["severity_pct"]
        out[f"{scen}_{pct}pct_impact_usd_bn"] = f"{impact:.6f}"
        long_rows.append({
            "industry": row["industry"],
            "scenario": s["scenario"],
            "severity_pct": pct,
            "severity_factor": s["severity_factor"],
            "revenue_at_risk_base_usd_bn": f"{rar:.6f}",
            "estimated_impact_usd_bn": f"{impact:.6f}",
            "risk_level": row.get("risk_level", ""),
            "confidence_level": row.get("confidence_level", ""),
        })
    wide_rows.append(out)

with open(PROCESSED_DIR / "scenario_impact_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(wide_rows[0].keys()))
    writer.writeheader()
    writer.writerows(wide_rows)

with open(PROCESSED_DIR / "scenario_impact_results_long.csv", "w", newline="", encoding="utf-8") as f:
    fields = ["industry", "scenario", "severity_pct", "severity_factor", "revenue_at_risk_base_usd_bn", "estimated_impact_usd_bn", "risk_level", "confidence_level"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(long_rows)

total_rows = []
for s in scenario_defs:
    total = sum(float(r["estimated_impact_usd_bn"]) for r in long_rows if r["scenario"] == s["scenario"])
    total_rows.append({
        "scenario": s["scenario"],
        "severity_pct": s["severity_pct"],
        "severity_factor": s["severity_factor"],
        "estimated_impact_usd_bn": f"{total:.6f}",
    })

with open(PROCESSED_DIR / "scenario_total_impact.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["scenario", "severity_pct", "severity_factor", "estimated_impact_usd_bn"])
    writer.writeheader()
    writer.writerows(total_rows)

industries = [r["industry"] for r in wide_rows]
fig = go.Figure()
fig.add_trace(go.Bar(x=industries, y=[float(r["mild_10pct_impact_usd_bn"]) for r in wide_rows], name="Mild 10%"))
fig.add_trace(go.Bar(x=industries, y=[float(r["moderate_20pct_impact_usd_bn"]) for r in wide_rows], name="Moderate 20%"))
fig.add_trace(go.Bar(x=industries, y=[float(r["severe_40pct_impact_usd_bn"]) for r in wide_rows], name="Severe 40%"))
fig.update_layout(
    title="Scenario Impact by Industry (USD bn)",
    xaxis_title="Industry",
    yaxis_title="Estimated Impact (USD bn)",
    barmode="group",
    template="plotly_white",
)
fig.write_html(VISUALS_DIR / "scenario_impact_by_industry.html", include_plotlyjs="cdn")
print("Phase 4 scenario analysis complete.")

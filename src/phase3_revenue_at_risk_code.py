import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

INPUT_PATH = Path("../data/processed/industry_revenue_at_risk_inputs.csv")
OUTPUT_PATH = Path("../data/processed/industry_revenue_at_risk_results.csv")
VISUALS_DIR = Path("../visuals")
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_PATH)

for case in ["low", "base", "high"]:
    df[f"revenue_at_risk_{case}_usd_bn"] = (
        df["production_value_usd_bn"] *
        df[f"chip_share_{case}"] *
        (df["taiwan_dependency_pct"] / 100)
    )

def risk_level(x):
    if x >= 5:
        return "Very High"
    elif x >= 1:
        return "High"
    else:
        return "Moderate"

df["risk_level"] = df["revenue_at_risk_base_usd_bn"].apply(risk_level)
df = df.sort_values("revenue_at_risk_base_usd_bn", ascending=False).reset_index(drop=True)
df.insert(0, "rank", range(1, len(df) + 1))
df.to_csv(OUTPUT_PATH, index=False)

fig = go.Figure()
fig.add_trace(go.Bar(
    x=df["industry"],
    y=df["revenue_at_risk_base_usd_bn"],
    error_y=dict(
        type="data",
        symmetric=False,
        array=df["revenue_at_risk_high_usd_bn"] - df["revenue_at_risk_base_usd_bn"],
        arrayminus=df["revenue_at_risk_base_usd_bn"] - df["revenue_at_risk_low_usd_bn"]
    ),
    name="Base case"
))
fig.update_layout(
    title="Estimated Semiconductor Revenue at Risk by Thai Industry",
    xaxis_title="Industry",
    yaxis_title="Revenue at Risk (USD bn)",
    template="plotly_white"
)
fig.write_html(VISUALS_DIR / "industry_revenue_at_risk_bar.html")
fig.show(renderer="browser")

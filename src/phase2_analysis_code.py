"""
Phase 2 — Data Cleaning + Taiwan Dependency Index
Project: Assessing Thailand's Exposure to Taiwan Semiconductor Supply Chain Disruption

Input:
    data/raw/TradeData.csv or TradeData.csv

Outputs:
    processed/phase2_clean_hs8542_imports.csv
    processed/taiwan_dependency_index.csv
    processed/top_suppliers_by_year.csv
    visuals/*.html

Methodology note:
    Taiwan/Chinese Taipei is not separately reported in the available UN Comtrade/WITS
    dataset. This analysis uses "Other Asia, nes" as a proxy for Taiwan/Chinese Taipei,
    with limitations clearly stated in the report.
"""

import csv
from pathlib import Path
import plotly.graph_objects as go


BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / "data" / "raw" / "TradeData.csv"
if not RAW_PATH.exists():
    RAW_PATH = BASE_DIR / "TradeData.csv"

PROCESSED_DIR = BASE_DIR / "processed"
VISUALS_DIR = BASE_DIR / "visuals"
PROCESSED_DIR.mkdir(exist_ok=True)
VISUALS_DIR.mkdir(exist_ok=True)


def read_comtrade_csv(path: Path):
    rows = []
    with open(path, encoding="latin1", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row.pop(None, None)
            rows.append(row)
    return rows


def write_csv(path: Path, rows, fieldnames):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


raw_rows = read_comtrade_csv(RAW_PATH)

# Keep useful columns only
clean_rows = []
for r in raw_rows:
    clean_rows.append({
        "year": int(r["refYear"]),
        "partner_country": r["partnerDesc"],
        "trade_value_usd": float(r["primaryValue"] or 0),
        "reporter": r["reporterDesc"],
        "flow": r["flowDesc"],
        "hs_code": r["cmdCode"],
        "commodity": r["cmdDesc"],
    })

clean_rows.sort(key=lambda x: (x["year"], -x["trade_value_usd"], x["partner_country"]))

years = sorted({r["year"] for r in clean_rows})
world_by_year = {}
taiwan_proxy_by_year = {}
country_by_year = {}

for r in clean_rows:
    key = (r["year"], r["partner_country"])
    country_by_year[key] = country_by_year.get(key, 0) + r["trade_value_usd"]

    if r["partner_country"] == "World":
        world_by_year[r["year"]] = world_by_year.get(r["year"], 0) + r["trade_value_usd"]

    if r["partner_country"] == "Other Asia, nes":
        taiwan_proxy_by_year[r["year"]] = taiwan_proxy_by_year.get(r["year"], 0) + r["trade_value_usd"]

# Calculate Taiwan Dependency Index
dependency_rows = []
previous_total = None
previous_taiwan = None

for y in years:
    total = world_by_year.get(y, 0)
    taiwan_proxy = taiwan_proxy_by_year.get(y, 0)
    dependency_pct = taiwan_proxy / total * 100 if total else None

    dependency_rows.append({
        "year": y,
        "total_hs8542_import_usd": total,
        "other_asia_nes_taiwan_proxy_import_usd": taiwan_proxy,
        "taiwan_proxy_dependency_pct": dependency_pct,
        "total_import_yoy_growth_pct": (total / previous_total - 1) * 100 if previous_total else None,
        "taiwan_proxy_yoy_growth_pct": (taiwan_proxy / previous_taiwan - 1) * 100 if previous_taiwan else None,
    })

    previous_total = total
    previous_taiwan = taiwan_proxy

# Top suppliers by year
top_rows = []
for y in years:
    total = world_by_year[y]
    partners = []
    for (year, partner), value in country_by_year.items():
        if year == y and partner != "World" and value > 0:
            partners.append((partner, value))

    partners.sort(key=lambda x: x[1], reverse=True)

    for rank, (partner, value) in enumerate(partners[:15], start=1):
        top_rows.append({
            "year": y,
            "rank": rank,
            "partner_country": partner,
            "trade_value_usd": value,
            "share_of_total_import_pct": value / total * 100 if total else None,
        })

write_csv(
    PROCESSED_DIR / "phase2_clean_hs8542_imports.csv",
    clean_rows,
    ["year", "partner_country", "trade_value_usd", "reporter", "flow", "hs_code", "commodity"],
)

write_csv(
    PROCESSED_DIR / "taiwan_dependency_index.csv",
    dependency_rows,
    [
        "year",
        "total_hs8542_import_usd",
        "other_asia_nes_taiwan_proxy_import_usd",
        "taiwan_proxy_dependency_pct",
        "total_import_yoy_growth_pct",
        "taiwan_proxy_yoy_growth_pct",
    ],
)

write_csv(
    PROCESSED_DIR / "top_suppliers_by_year.csv",
    top_rows,
    ["year", "rank", "partner_country", "trade_value_usd", "share_of_total_import_pct"],
)

# Charts
years_list = [r["year"] for r in dependency_rows]
total_import_b = [r["total_hs8542_import_usd"] / 1e9 for r in dependency_rows]
taiwan_proxy_b = [r["other_asia_nes_taiwan_proxy_import_usd"] / 1e9 for r in dependency_rows]
dependency_pct = [r["taiwan_proxy_dependency_pct"] for r in dependency_rows]

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=years_list, y=dependency_pct, mode="lines+markers", name="Other Asia, nes share (%)"))
fig1.update_layout(
    title="Thailand HS8542 Import Dependency on Other Asia, nes (Taiwan Proxy), 2014–2024",
    xaxis_title="Year",
    yaxis_title="Share of total HS8542 imports (%)",
    template="plotly_white",
    hovermode="x unified",
)
fig1.write_html(VISUALS_DIR / "taiwan_dependency_trend.html", include_plotlyjs="cdn")

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=years_list, y=total_import_b, mode="lines+markers", name="Total HS8542 imports"))
fig2.add_trace(go.Scatter(x=years_list, y=taiwan_proxy_b, mode="lines+markers", name="Other Asia, nes imports"))
fig2.update_layout(
    title="Thailand HS8542 Import Value Trend, 2014–2024",
    xaxis_title="Year",
    yaxis_title="Import value (USD billions)",
    template="plotly_white",
    hovermode="x unified",
)
fig2.write_html(VISUALS_DIR / "total_semiconductor_imports_trend.html", include_plotlyjs="cdn")

latest_year = max(years)
latest_top = [r for r in top_rows if r["year"] == latest_year and r["rank"] <= 10]
fig3 = go.Figure(go.Bar(
    x=[r["share_of_total_import_pct"] for r in latest_top][::-1],
    y=[r["partner_country"] for r in latest_top][::-1],
    orientation="h",
    text=[f'{r["share_of_total_import_pct"]:.1f}%' for r in latest_top][::-1],
    textposition="auto",
))
fig3.update_layout(
    title=f"Top 10 HS8542 Import Suppliers to Thailand, {latest_year}",
    xaxis_title="Share of total HS8542 imports (%)",
    yaxis_title="Partner country",
    template="plotly_white",
)
fig3.write_html(VISUALS_DIR / f"top_suppliers_{latest_year}.html", include_plotlyjs="cdn")

print("Phase 2 completed.")
print(f"Rows cleaned: {len(clean_rows)}")
print(f"Years covered: {min(years)}–{max(years)}")
print(f"Latest dependency: {dependency_rows[-1]['taiwan_proxy_dependency_pct']:.2f}%")

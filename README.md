# Thailand Semiconductor Supply Chain Risk Assessment

## Assessing Thailand's Exposure to Taiwan Semiconductor Supply Chain Disruption

This repository contains an independent, data-driven research project assessing Thailand's exposure to Taiwan-related semiconductor supply chain disruption.

The project uses international trade data, industry-level production estimates, a Taiwan Proxy Dependency Index, a Revenue-at-Risk model, and scenario analysis to estimate how semiconductor supply disruption could affect key Thai manufacturing industries.

---

## Project Overview

Thailand is an important manufacturing hub for electronics, automotive products, hard disk drives, and home appliances. These industries depend heavily on imported semiconductors, especially integrated circuits classified under HS8542.

However, Taiwan/Chinese Taipei is not separately reported in the available UN Comtrade/WITS dataset used in this project. Therefore, the analysis uses **“Other Asia, nes”** as the closest available proxy for Taiwan/Chinese Taipei, with this limitation stated clearly throughout the report.

The goal of this project is not to predict a specific geopolitical event. Instead, it provides a transparent and reproducible framework for measuring Thailand's semiconductor supply chain exposure using public data.

---

## Research Question

**How exposed are Thai industries to Taiwan-related semiconductor supply chain disruption, and which industries face the highest potential impact?**

---

## Key Findings

* Thailand's Taiwan-proxy semiconductor import dependency increased from **22.8% in 2014** to **43.6% in 2024**.
* Total HS8542 semiconductor imports increased from **USD 9.68 billion in 2014** to **USD 24.43 billion in 2024**.
* Imports from the Taiwan proxy category increased from **USD 2.21 billion in 2014** to **USD 10.65 billion in 2024**.
* The base-case Revenue-at-Risk model estimates **USD 8.35 billion** in semiconductor-linked exposure across four Thai industries.
* Electronics is the dominant exposure category, accounting for approximately **69%** of total estimated base-case exposure.
* Under the severe scenario, the estimated disruption impact reaches approximately **USD 3.34 billion**.

---

## Industries Analyzed

The project focuses on four semiconductor-dependent Thai industries:

1. **Electronics**
2. **Automotive**
3. **HDD / Storage**
4. **Home Appliances**

These sectors were selected because they are economically important to Thailand and rely on semiconductor inputs to varying degrees.

---

## Methodology

The analysis is built around three main components.

### 1. Taiwan Proxy Dependency Index

The Taiwan Proxy Dependency Index measures Thailand's annual import dependency on the Taiwan proxy category.

**Formula:**

> TPDI (%) = Imports from Other Asia, nes / Total HS8542 Imports × 100

The index is calculated using Thailand's HS8542 import data from 2014 to 2024.

### 2. Industry Revenue-at-Risk Model

The Revenue-at-Risk model converts trade-level semiconductor dependency into industry-level exposure estimates.

**Formula:**

> Revenue at Risk = Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency

Revenue at Risk should be interpreted as semiconductor-linked exposure, not as a direct forecast of revenue loss.

### 3. Scenario Analysis

The scenario analysis applies three disruption severity assumptions to the base-case Revenue-at-Risk results.

| Scenario | Severity | Interpretation                                              |
| -------- | -------: | ----------------------------------------------------------- |
| Mild     |      10% | Limited allocation issue or short-term disruption           |
| Moderate |      20% | Partial disruption affecting a meaningful share of exposure |
| Severe   |      40% | Major disruption short of a full Taiwan foundry shutdown    |

These scenario severities are stress assumptions, not probability estimates.


---

## Repository Structure

```text
taiwan-semiconductor-risk-thailand/
├── data/
│   ├── raw/
│   │   ├── TradeData.csv
│   │   └── TradeData.xlsx
│   └── processed/
│       ├── phase2_clean_hs8542_imports.csv
│       ├── taiwan_dependency_index.csv
│       ├── top_suppliers_by_year.csv
│       ├── methodology_note_other_asia_nes_proxy.md
│       ├── industry_revenue_at_risk_inputs.csv
│       ├── industry_revenue_at_risk_results.csv
│       ├── scenario_definitions.csv
│       ├── scenario_impact_results.csv
│       ├── scenario_impact_results_long.csv
│       ├── scenario_total_impact.csv
│       └── phase5_recommendations.csv
├── notebooks/
│   ├── 01_phase2_data_cleaning_dependency_index.ipynb
│   ├── 02_industry_revenue_at_risk.ipynb
│   └── 03_scenario_analysis.ipynb
├── src/
│   ├── phase2_analysis_code.py
│   ├── phase3_revenue_at_risk_code.py
│   └── phase4_scenario_analysis_code.py
├── visuals/
│   ├── taiwan_dependency_trend.html
│   ├── total_semiconductor_imports_trend.html
│   ├── top_suppliers_2024.html
│   ├── supplier_mix_stacked_share.html
│   ├── industry_revenue_at_risk_bar.html
│   ├── industry_revenue_at_risk_sensitivity.html
│   ├── production_value_vs_risk.html
│   ├── scenario_impact_by_industry.html
│   ├── total_impact_by_scenario.html
│   └── severe_scenario_ranking.html
├── report/
│   ├── final_report.pdf
│   ├── phase2_findings_summary.md
│   ├── phase3_findings_summary.md
│   ├── phase4_findings_summary.md
│   ├── final_report_outline.md
│   └── executive_summary_draft.md
├── README.md
└── requirements.txt
````

---

## Data Sources

The primary dataset used in this project is Thailand's HS8542 electronic integrated circuit import data from UN Comtrade/WITS.

Key public sources used in the report include:

* UN Comtrade / WITS trade data
* Thailand Board of Investment
* Office of Industrial Economics, Ministry of Industry Thailand
* Thailand Electrical and Electronics Institute
* Reuters
* Axios
* SIA / BCG semiconductor supply chain analysis
* TrendForce semiconductor market research
* WTO and OEC trade references

A full reference list is provided in the final report.

---

## Tools Used

* Python
* pandas
* Plotly
* Excel
* Jupyter Notebook
* UN Comtrade / WITS trade data

---

## How to Reproduce the Analysis

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the notebooks in order:

```text
01_phase2_data_cleaning_dependency_index.ipynb
02_industry_revenue_at_risk.ipynb
03_scenario_analysis.ipynb
```

Alternatively, run the Python scripts in the `src/` folder to reproduce the main calculations.

---

## Key Outputs

The project produces the following outputs:

* Cleaned HS8542 import dataset
* Taiwan Proxy Dependency Index
* Supplier concentration analysis
* Industry Revenue-at-Risk model
* Scenario impact estimates
* Interactive Plotly visualizations
* Final analytical report
* Policy and firm-level recommendations

---

## Limitations

This project includes several important limitations:

1. **Taiwan Proxy Limitation**
   Taiwan/Chinese Taipei is not separately reported in the available UN Comtrade/WITS dataset. “Other Asia, nes” is used as the closest available proxy.

2. **Exposure, Not Forecast**
   Revenue-at-Risk and scenario impact estimates measure exposure. They do not represent certain losses or probability-weighted forecasts.

3. **Cost-Share Assumptions**
   Semiconductor cost-share inputs are based on public benchmarks and product-level reasoning, not firm-level Thailand-specific bill-of-materials data.

4. **Scenario Severity Assumptions**
   The 10%, 20%, and 40% disruption severity levels are analyst-defined stress assumptions informed by historical semiconductor shortage events.

---

## Recommendations

The report recommends five actions for Thai firms and policymakers:

1. Strategic inventory buffering for critical chips
2. Semiconductor supply chain risk monitoring dashboard
3. Supplier diversification where technically feasible
4. Regular semiconductor disruption scenario planning
5. Long-term semiconductor-adjacent capability development

---

## Author

**Methakan Bualuang**<br>
Industrial Engineering, Chulalongkorn University<br>
Independent Research Project, 2026

---

## Project Status

Completed as an independent research project.

Final report, datasets, code, and visualizations are included in this repository.

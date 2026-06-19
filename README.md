# Thailand Semiconductor Supply Chain Risk Assessment

## Research Question
How exposed are Thai industries to Taiwan-related semiconductor supply chain disruption, and which industries are most vulnerable?

## Overview
This independent research project examines Thailand’s semiconductor import dependency using HS Code 8542 (Electronic Integrated Circuits) from the UN Comtrade database (2014–2024).

Due to partner classification limitations in UN Comtrade and WITS, Taiwan is not separately reported in the dataset. Therefore, the category **`Other Asia, nes`** is used as a proxy for Taiwan/Chinese Taipei, with methodological limitations clearly stated.

The objective of this project is to assess Thailand’s exposure to semiconductor supply chain disruption by analyzing trade dependency, supplier concentration, industry-level revenue exposure, and scenario-based impact.

## Methodology
- Trade data sourced from UN Comtrade Database
- HS Code: 8542 (Electronic Integrated Circuits)
- Reporter: Thailand
- Flow: Import
- Years: 2014–2024

### Key Metrics
- **Taiwan Proxy Dependency Index**  
  `Other Asia, nes imports ÷ Total HS8542 imports × 100`

- **Semiconductor-Linked Revenue Exposure**  
  `Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency`

- **Scenario Impact**  
  `Base-Case Revenue at Risk × Disruption Severity`

## Key Findings
- Thailand’s total HS8542 imports increased from **USD 9.68B in 2014** to **USD 24.43B in 2024**.
- Imports from **`Other Asia, nes`** increased from **USD 2.21B** to **USD 10.65B** over the same period.
- Taiwan proxy dependency rose from **22.8%** to **43.6%**.
- Electronics has the highest estimated semiconductor-linked revenue exposure at **USD 5.77B**.
- Under the severe 40% stress scenario, total modeled impact across the four selected industries is approximately **USD 3.34B**.

## Tools & Technologies
- Python
- pandas
- Plotly
- Jupyter Notebook
- Excel
- GitHub

## Data Sources
- UN Comtrade
- World Bank WITS
- Office of Industrial Economics (Thailand)
- Thailand BOI
- TSMC / semiconductor industry reports

## Project Structure

```text
taiwan-semiconductor-risk-thailand/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── visuals/
├── report/
├── phase2_semiconductor_import_analysis.xlsx
├── phase3_revenue_at_risk_analysis.xlsx
├── phase4_scenario_analysis.xlsx
├── README.md
└── requirements.txt
```

## Methodological Notes
This project uses `Other Asia, nes` as a proxy for Taiwan/Chinese Taipei because Taiwan is not separately reported in the available UN Comtrade/WITS dataset. This proxy should be interpreted with caution.

Revenue-at-risk and scenario-impact results are exposure estimates, not forecasts of actual revenue loss or GDP loss.

## Author
Methakan Bualuang  
Industrial Engineering Student  
Chulalongkorn University

# Thailand Semiconductor Supply Chain Risk Assessment

## Research Question
How exposed is Thailand to Taiwan-related semiconductor supply chain disruption, and how has this dependency changed over the past decade?

## Overview
This independent research project examines Thailand’s semiconductor import dependency using HS Code 8542 (Electronic Integrated Circuits) from the UN Comtrade database (2014–2024).

Due to partner classification limitations in UN Comtrade and WITS, Taiwan is not separately reported in the dataset. Therefore, the category **"Other Asia, nes"** is used as a proxy for Taiwan/Chinese Taipei, with methodological limitations clearly stated.

The objective of this project is to assess Thailand’s exposure to semiconductor supply chain disruption by analyzing trade dependency, supplier concentration, and industry vulnerability.

## Methodology
- Trade data sourced from UN Comtrade Database
- HS Code: 8542 (Electronic Integrated Circuits)
- Reporter: Thailand
- Flow: Import
- Years: 2014–2024

### Key Metrics
- Taiwan Proxy Dependency Index  
  = Other Asia, nes imports ÷ Total HS8542 imports × 100

- Supplier Concentration Analysis

- Historical Import Trend Analysis

- Industry Vulnerability Mapping

## Key Findings
- Thailand’s total HS8542 imports increased from **USD 9.68B (2014)** to **USD 24.43B (2024)**
- Imports from **Other Asia, nes** increased from **USD 2.21B** to **USD 10.65B**
- Taiwan proxy dependency rose from **22.8%** to **43.6%**
- Supplier concentration has become significantly more dependent on the Taiwan-related supply chain

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
- TSMC Annual Reports

## Project Structure
taiwan-semiconductor-risk-thailand/
├── data/
├── notebooks/
├── src/
├── visuals/
├── report/
├── README.md
└── requirements.txt

## Author
Methakan Bualuang  
Industrial Engineering Student  
Chulalongkorn University

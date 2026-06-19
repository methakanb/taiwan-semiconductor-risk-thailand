# Final Report Outline — Assessing Thailand's Exposure to Taiwan Semiconductor Supply Chain Disruption

## Title
Assessing Thailand's Exposure to Taiwan Semiconductor Supply Chain Disruption

## Research Question
How exposed are Thai industries to Taiwan-related semiconductor supply chain disruption, and which industries are most vulnerable?

---

## Chapter 1 — Introduction

### 1.1 Background
Taiwan plays a critical role in the global semiconductor supply chain, especially in advanced foundry manufacturing. Thailand is a major manufacturing base for electronics, automotive, HDD/storage, and home appliances, all of which depend on semiconductor inputs to varying degrees.

### 1.2 Problem Statement
Thailand’s semiconductor import structure shows rising concentration in `Other Asia, nes`, used in this project as a Taiwan/Chinese Taipei proxy due to partner classification limitations in UN Comtrade/WITS. This creates potential exposure to Taiwan-related semiconductor supply chain disruption.

### 1.3 Research Question
How exposed are Thai industries to Taiwan-related semiconductor supply chain disruption, and which industries are most vulnerable?

### 1.4 Objectives
- Measure Thailand’s HS8542 import dependency on `Other Asia, nes` from 2014–2024.
- Identify which Thai industries have the highest semiconductor-linked revenue exposure.
- Estimate scenario-based exposure under mild, moderate, and severe disruption assumptions.
- Provide recommendations for firms and policymakers.

### 1.5 Scope and Limitations
The core analysis focuses on HS8542 electronic integrated circuits. `Other Asia, nes` is used as a proxy for Taiwan/Chinese Taipei with limitations. Results should be interpreted as exposure estimates, not direct forecasts of revenue loss or GDP loss.

---

## Chapter 2 — Background

### 2.1 Taiwan’s Role in the Global Semiconductor Supply Chain
Explain Taiwan’s foundry role, TSMC, advanced chips, and why substitution is difficult in the short term.

### 2.2 Thailand’s Semiconductor-Using Industries
Discuss electronics, automotive, HDD/storage, and home appliances as semiconductor-dependent industries.

### 2.3 Historical Disruption Context
Discuss COVID-19 semiconductor shortages, 2021 automotive chip shortage, and why semiconductor supply chains are vulnerable.

---

## Chapter 3 — Methodology

### 3.1 Data Sources
- UN Comtrade HS8542 import data, Thailand, 2014–2024
- WITS / supporting trade classification sources
- BOI / OIE / industry sources for production values
- Public industry benchmarks for semiconductor cost-share assumptions

### 3.2 Taiwan Proxy Dependency Index
Formula:

```text
Taiwan Proxy Dependency = Other Asia, nes HS8542 imports / Total HS8542 imports × 100
```

### 3.3 Industry Revenue-at-Risk Model
Formula:

```text
Revenue at Risk = Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency
```

### 3.4 Scenario Analysis
Formula:

```text
Scenario Impact = Base-Case Revenue at Risk × Disruption Severity
```

Scenario severity levels:
- Mild: 10%
- Moderate: 20%
- Severe: 40%

These are analyst-defined stress assumptions informed by historical semiconductor disruption events. They are not probabilities.

### 3.5 Limitations
- `Other Asia, nes` is a proxy, not an official Taiwan-only figure.
- Semiconductor cost-share values are analytical assumptions, not official Thai industry-wide cost statistics.
- Revenue-at-risk estimates are exposure estimates, not actual losses.

---

## Chapter 4 — Results & Analysis

### 4.1 Thailand HS8542 Import Trend
Total HS8542 imports increased from USD 9.68B in 2014 to USD 24.43B in 2024.

### 4.2 Taiwan Proxy Dependency Trend
The `Other Asia, nes` share increased from 22.8% in 2014 to 43.6% in 2024.

### 4.3 Supplier Concentration
In 2024, `Other Asia, nes` was the largest HS8542 import source for Thailand at 43.6% of total HS8542 imports.

### 4.4 Industry Revenue-at-Risk Ranking
Base-case estimated semiconductor-linked revenue exposure:
1. Electronics: USD 5.77B
2. Automotive: USD 0.92B
3. HDD / Storage: USD 0.87B
4. Home Appliances: USD 0.78B

### 4.5 Scenario Analysis
Total modeled impact across the four selected industries:
- Mild 10%: USD 0.83B
- Moderate 20%: USD 1.67B
- Severe 40%: USD 3.34B

### 4.6 Key Interpretation
Electronics is the most exposed industry in absolute value terms due to its combination of large production value and high semiconductor intensity. Automotive has lower semiconductor cost share but important bottleneck risk.

---

## Chapter 5 — Conclusion & Recommendations

### 5.1 Key Findings
- Thailand’s HS8542 imports have grown substantially over the past decade.
- Dependency on `Other Asia, nes` / Taiwan proxy has nearly doubled as a share of HS8542 imports.
- Electronics has the highest semiconductor-linked revenue exposure.
- Scenario analysis shows that even partial disruption could create billion-dollar exposure across selected industries.

### 5.2 Recommendations
1. Supplier diversification
2. Strategic inventory buffers for critical chips
3. Semiconductor supply chain risk dashboard
4. Local semiconductor-adjacent capability building
5. Regular scenario planning

### 5.3 Future Work
- Add HS8541 as a supplementary robustness check.
- Improve industry exposure estimates using firm-level bill-of-materials data.
- Extend analysis to firm-level supply chain mapping.
- Add interactive dashboard deployment.

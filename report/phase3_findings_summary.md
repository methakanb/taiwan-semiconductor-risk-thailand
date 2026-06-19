# Phase 3 Findings Summary — Industry Revenue at Risk

## Objective
Phase 3 converts the Phase 2 import dependency result into an industry-level exposure estimate.

Instead of assigning subjective 1–10 exposure scores, this phase uses a quantitative Revenue-at-Risk model:

```text
Revenue at Risk = Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency
```

The 2024 Taiwan proxy dependency value from Phase 2 is **43.6%**, based on Thailand's HS8542 imports from `Other Asia, nes` divided by total HS8542 imports.

## Base-Case Results

| Rank | Industry | Production Value (USD bn) | Base Chip Share | Revenue at Risk (USD bn) | Risk Level | Confidence |
|---:|---|---:|---:|---:|---|---|
| 1 | Electronics | 52.89 | 25% | 5.77 | Very High | High for production value; Medium for chip share |
| 2 | Automotive | 53.00 | 4% | 0.92 | Moderate | Medium |
| 3 | HDD / Storage | 13.36 | 15% | 0.87 | Moderate | Low |
| 4 | Home Appliances | 29.88 | 6% | 0.78 | Moderate | Low |


## Main Interpretation
Electronics has the highest estimated revenue at risk because it combines a large production base with high semiconductor intensity. Automotive has lower semiconductor cost share, but remains strategically important because chips can be production bottlenecks: the absence of a small number of chips may delay assembly of a high-value vehicle. HDD/storage has high semiconductor criticality but lower absolute exposure due to a smaller estimated production base. Home appliances show moderate exposure under this model.

## Why Low/Base/High Cases Are Included
Chip share estimates are uncertain and vary by product mix. Therefore, this model uses low/base/high chip share assumptions to avoid relying on a single point estimate. The results should be interpreted as an exposure estimate, not a precise loss forecast.

## Methodological Limitation
This model estimates semiconductor-linked revenue exposure, not direct GDP loss or actual revenue loss. It assumes that Taiwan proxy dependency in HS8542 imports is representative of the semiconductor input risk faced by each industry. This is a defensible portfolio-level risk model but should be improved with firm-level bill-of-materials data if available.

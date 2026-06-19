# Phase 3 Findings Summary — Industry Revenue at Risk

## Objective

Phase 3 converts the Phase 2 import dependency result into an industry-level exposure estimate.

Instead of assigning subjective 1–10 exposure scores, this phase uses a quantitative Revenue-at-Risk model:

```text
Revenue at Risk = Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency
```

The 2024 Taiwan proxy dependency value from Phase 2 is **43.6%**, based on Thailand's HS8542 imports from `Other Asia, nes` divided by total HS8542 imports.

In this project, Revenue at Risk should be interpreted as **estimated semiconductor-linked revenue exposure**, not as a direct forecast of revenue loss, GDP loss, or realized economic damage.

## Base-Case Results

| Rank | Industry        | Production Value (USD bn) | Base Chip Share | Revenue at Risk (USD bn) | Risk Level    | Confidence                                       |
| ---: | --------------- | ------------------------: | --------------: | -----------------------: | ------------- | ------------------------------------------------ |
|    1 | Electronics     |                     52.89 |             25% |                     5.77 | Very High     | High for production value; Medium for chip share |
|    2 | Automotive      |                     53.00 |              4% |                     0.92 | Moderate-High | Medium                                           |
|    3 | HDD / Storage   |                     13.36 |             15% |                     0.87 | Moderate-High | Low                                              |
|    4 | Home Appliances |                     29.88 |              6% |                     0.78 | Moderate      | Low                                              |

## Main Interpretation

Electronics has the highest estimated semiconductor-linked revenue exposure because it combines a large production base with high semiconductor intensity. Automotive has a lower semiconductor cost share, but remains strategically important because chips can become production bottlenecks: the absence of a small number of chips may delay the assembly of a high-value vehicle.

HDD/storage has high semiconductor criticality due to its reliance on controller ICs, read-channel electronics, motor control, and PCB components. However, its absolute exposure is lower than electronics because the estimated production base is smaller. Home appliances show moderate exposure under this model because semiconductors are used in control boards, sensors, inverter modules, and power electronics, while major cost components still include compressors, motors, metals, plastics, and mechanical parts.

## Why Low/Base/High Cases Are Included

Chip share estimates are uncertain and vary by product mix. Therefore, this model uses low/base/high chip share assumptions to avoid relying on a single point estimate.

Semiconductor cost-share assumptions are based on public industry benchmarks, product-level reasoning, and sensitivity ranges. They are not official Thai industry-wide cost-share statistics. The low/base/high cases should be interpreted as sensitivity assumptions rather than probabilities.

The base case is used as the headline estimate, while the low and high cases show how estimated exposure changes under alternative semiconductor-intensity assumptions.

## Methodological Limitation

This model estimates semiconductor-linked revenue exposure, not direct GDP loss or actual revenue loss. It assumes that Taiwan proxy dependency in HS8542 imports is representative of the semiconductor input risk faced by each industry. This is a defensible portfolio-level risk model but should be improved with firm-level bill-of-materials data if available.

Some industry production values, especially HDD/storage and home appliances, should be interpreted as sector-level proxies rather than exact product-level production values. Therefore, the results are most useful for comparing relative exposure across industries, not for estimating precise financial losses.

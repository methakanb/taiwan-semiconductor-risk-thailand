# Executive Summary Draft

This project assesses Thailand’s exposure to Taiwan-related semiconductor supply chain disruption using public trade data, industry production estimates, and scenario-based risk modeling.

The core trade analysis focuses on HS8542 electronic integrated circuits from UN Comtrade for Thailand’s imports between 2014 and 2024. Because Taiwan is not separately reported in the available UN Comtrade/WITS partner classification, this project uses `Other Asia, nes` as a proxy for Taiwan/Chinese Taipei, while clearly stating methodological limitations.

The analysis finds that Thailand’s total HS8542 imports increased from USD 9.68 billion in 2014 to USD 24.43 billion in 2024. Over the same period, imports from `Other Asia, nes` increased from USD 2.21 billion to USD 10.65 billion. As a result, the Taiwan proxy dependency index increased from 22.8% in 2014 to 43.6% in 2024, indicating rising exposure to Taiwan-related semiconductor supply chain risk.

At the industry level, the project applies a revenue-at-risk model:

```text
Revenue at Risk = Production Value × Semiconductor Cost Share × Taiwan Proxy Dependency
```

Under the base-case model, electronics has the highest estimated semiconductor-linked revenue exposure at USD 5.77 billion, followed by automotive at USD 0.92 billion, HDD/storage at USD 0.87 billion, and home appliances at USD 0.78 billion. Electronics is the most exposed industry in absolute value terms because it combines large production value with high semiconductor intensity. Automotive remains strategically important because even low-cost chips can create production bottlenecks for high-value vehicles.

The project then applies an illustrative scenario analysis using analyst-defined stress assumptions of 10%, 20%, and 40% disruption severity. These are not probabilities or direct forecasts, but stress-test levels informed by historical semiconductor disruption events. Across the four selected industries, the total modeled impact ranges from USD 0.83 billion in the mild scenario to USD 3.34 billion in the severe scenario.

The findings suggest that Thailand’s semiconductor supply chain exposure is both concentrated and economically meaningful. Recommended actions include supplier diversification, strategic inventory buffers for critical chips, industry-level risk monitoring, semiconductor-adjacent capability development, and regular scenario planning.

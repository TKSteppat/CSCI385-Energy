# Multi-Criteria Decision Analysis Report

## Objective 
**Project Goal:** Determine which energy source produces the most amount of energy per dollar while minimizing carbon emissions.  
**Primary Objective:** To identify the most cost-efficient and environmentally sustainable energy source for large-scale power generation, by evaluating **cost per MWh**, **carbon intensity**, and **conversion efficiency**.

---

## Criteria
1. **Cost per MWh ($/MWh)** — Measures economic efficiency (lower = better).  
2. **CO₂ Emission Intensity (kg CO₂/MWh)** — Measures environmental impact (lower = better).  
3. **Thermal Efficiency (%)** — Measures how effectively fuel energy converts to electricity (higher = better).  
4. **Cost-to-Emission Ratio ($ per ton CO₂)** — Integrates economic and environmental performance (higher = better).

---

## Criteria Weighting 
| Criterion | Description | Weight (%) |
|------------|--------------|-------------|
| Cost per MWh | Economic performance | 35 |
| CO₂ Emission Intensity | Environmental performance | 35 |
| Thermal Efficiency | Conversion efficiency | 15 |
| Cost-to-Emission Ratio | Integrated performance | 15 |
| **Total** |  | **100%** |

---

## List of Choices
1. Coal  
2. Natural Gas  
3. Petroleum  
4. Nuclear  
5. Solar  

---

## Performance Values (Derived from dataset averages and benchmarks)

| Energy Source | Cost per MWh ($) | CO₂ Intensity (kg/MWh) | Thermal Efficiency (%) | Cost-to-Emission Ratio ($/kg CO₂) |
|----------------|------------------|--------------------------|-------------------------|-----------------------------------|
| **Coal** | 27 | 1000 | 34 | 0.027 |
| **Natural Gas** | 40 | 450 | 42 | 0.089 |
| **Petroleum** | 65 | 700 | 38 | 0.093 |
| **Nuclear** | 60 | 16 | 33 | 3.75 |
| **Solar** | 47 | 0 | 100 | ∞ (no emissions) |

---

## Choice Rating (1 = worst, 5 = best for beneficial)

| Energy Source | Cost per MWh | CO₂ Intensity | Efficiency | C/E Ratio |
|----------------|---------------|----------------|-------------|-------------|
| **Coal** | 5 | 1 | 2 | 1 |
| **Natural Gas** | 4 | 3 | 3 | 3 |
| **Petroleum** | 2 | 2 | 2 | 2 |
| **Nuclear** | 3 | 4 | 1 | 4 |
| **Solar** | 4 | 5 | 5 | 5 |

---

## Normalized Performance Values  
(For cost and emissions: *lowest ÷ this value*; for efficiency and ratio: *this ÷ highest value*)

| Energy Source | Cost per MWh | CO₂ Intensity | Efficiency | C/E Ratio |
|----------------|---------------|----------------|-------------|-------------|
| **Coal** | 1.00 | 0.00 | 0.34 | 0.00 |
| **Natural Gas** | 0.68 | 0.55 | 0.42 | 0.02 |
| **Petroleum** | 0.42 | 0.30 | 0.38 | 0.02 |
| **Nuclear** | 0.45 | 0.98 | 0.33 | 0.94 |
| **Solar** | 0.57 | 1.00 | 1.00 | 1.00 |

---

## Weighted Normalized Values

| Energy Source | Cost (×0.35) | Emissions (×0.35) | Efficiency (×0.15) | C/E Ratio (×0.15) | **Total Score** |
|----------------|---------------|------------------|--------------------|-------------------|----------------|
| **Coal** | 0.35 | 0.00 | 0.05 | 0.00 | **0.40** |
| **Natural Gas** | 0.24 | 0.19 | 0.06 | 0.00 | **0.49** |
| **Petroleum** | 0.15 | 0.10 | 0.06 | 0.00 | **0.31** |
| **Nuclear** | 0.16 | 0.34 | 0.05 | 0.14 | **0.69** |
| **Solar** | 0.20 | 0.35 | 0.15 | 0.15 | **0.85** |

---

## Final Ranking
| Rank | Energy Source | Total Score |
|------|----------------|-------------|
| 1st | **Solar** | **0.85** |
| 2nd | **Nuclear** | **0.69** |
| 3rd | **Natural Gas** | **0.49** |
| 4th | **Coal** | **0.40** |
| 5th | **Petroleum** | **0.31** |

---

## Decision Summary
1. **Recommended energy source:** Solar  
2. **Final performance score:** 0.85  
3. **Why this energy source scored highest:** Zero emissions, high efficiency, and competitive cost per MWh make solar the most sustainable and cost-effective energy option.  
4. **Key advantages:**  
   - 100% clean generation (0 kg CO₂/MWh)  
   - Increasing cost competitiveness  
   - High scalability and low operational cost  
5. **Potential limitations:**  
   - Intermittency (depends on sunlight availability)  
   - Energy storage requirements (battery costs)  
6. **How results change if weights are adjusted:**  
   - If cost is weighted higher (>50%), natural gas overtakes nuclear in rank 2.  
   - Solar remains the top choice due to its zero emissions.

---

## Analysis
1. **Best cost per MWh:** Coal ($27/MWh), though environmentally poor.  
2. **Lowest carbon emissions:** Solar (0 kg CO₂/MWh) and Nuclear (16 kg CO₂/MWh).  
3. **Conflicts between cost-effectiveness and environmental impact:** Coal is cheapest but dirtiest; solar and nuclear are costlier but cleaner.  
4. **Geographic/practical considerations:** Solar potential varies regionally; nuclear provides consistent output independent of geography.  
5. **Unexpected findings:** When considering cost-to-emission ratio, nuclear performs nearly as well as solar due to extremely low emissions despite higher costs.

---

**Conclusion:**  
Solar energy provides the highest overall performance score in balancing **cost efficiency**, **emission reduction**, and **energy conversion efficiency**.  
Nuclear ranks second as a stable low-carbon baseload option, while natural gas offers a moderate transitional solution between fossil and renewable systems.

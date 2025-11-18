# Determine missing values and 0 values
import pandas as pd
import numpy as np

# Load data
df_new = pd.read_csv("datasets/cleaned/cleaned_combined_data_with_derived.csv", encoding="utf-8", delimiter=",")


# Calculate Heat Rate (Btu/kWh)
df_new["Heat_Rate (Btu/kWh)"] = (
    df_new["Total Consumption (millions of MMBtu)"] * 1e6 * 1e6  # millions of MMBtu → Btu
) / (
    df_new["Generation (Thousands of MWh)"] * 1e3 * 1e3          # thousands of MWh → kWh
)
# Calculate efficiency %
df_new["efficiency%"] = 3412 / df_new["Heat_Rate (Btu/kWh)"] * 100


# C02 Emission intensity (kg CO2/MWh)
# Convert emissions from million metric tons to kilograms
total_emissions_kg = df_new["CO2 Emissions (Million Metric Tons)"] * 1e9
# Convert generation to MWh
generation_mwh = df_new["Generation (Thousands of MWh)"] * 1e3
# Intensity in kg per MWh
df_new["CO2_Intensity_kg_per_MWh"] = total_emissions_kg / generation_mwh

# Cost-to-Emission Ratio
# formula: CtoE Ratio = Cost per MWh / Emission Intensity (kg CO2/MWh)
df_new["CtoE_Ratio"] = df_new["Cost ($/MWh)"] / df_new["CO2_Intensity_kg_per_MWh"]
# this integrates cost and environmental impact into one variable
# example: solar's cost/emission ratio is 10x higher than coal's ___ meaning it's much cleaner per dollar spent"
df_new["CtoE_Ratio"] = df_new["CtoE_Ratio"].fillna(0)
df_new.to_csv("datasets/cleaned/cleaned_combined_data_with_derived_fixed.csv", index = False)

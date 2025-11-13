# Determine missing values and 0 values
import pandas as pd
import numpy as np

# Load data
df_new = pd.read_csv("datasets/cleaned/cleaned_combined_data.csv", encoding="utf-8", delimiter=",")

# Calculate Heat Rate (Btu/kWh)
df_new["Heat_Rate (Btu/kWh)"] = (
    df_new["Total Consumption (millions of MMBtu)"] * 1e6 * 1e6  # millions of MMBtu → Btu
) / (
    df_new["Generation (Thousands of MWh)"] * 1e3 * 1e3          # thousands of MWh → kWh
)
# Calculate efficiency %
df_new["efficiency%"] = 3412 / df_new["Heat_Rate (Btu/kWh)"] * 100


# C02 Emission intensity (kg CO2/MWh)
#formula CO2 Emission Intensity = CO2 Emissions (tons) x 1000 / Generation (MWh)
# Map emission factors (kg CO2/MMBtu)
#information found from https://www.eia.gov/environment/emissions/co2_vol_mass.php in the Kilograms (CO2) per million Btu
emission_factors = {
    "all coal products": 95,
    "natural gas": 53,
    "petroleum": 73,
    "nuclear": 0,
    "estimated total solar": 0,
    "onshore wind turbine": 0
}
df_new["Emission_Factor_CO2"] = df_new["fuelTypeDescription"].map(emission_factors)
# Convert consumption to MMBtu
consumption_mmbtu = df_new["Total Consumption (millions of MMBtu)"] * 1e6
generation_mwh = df_new["Generation (Thousands of MWh)"] * 1e3
# CO2 intensity (kg/MWh)
df_new["CO2_Intensity_kg_per_MWh"] = (df_new["Emission_Factor_CO2"] * consumption_mmbtu) / generation_mwh



# Cost-to-Emission Ratio
# formula: CtoE Ratio = Cost per MWh / Emission Intensity (kg CO2/MWh)
df_new["CtoE_Ratio"] = df_new["Cost ($/MWh)"] / df_new["CO2_Intensity_kg_per_MWh"]
# this integrates cost and environmental impact into one variable
# example: solar's cost/emission ratio is 10x higher than coal's ___ meaning it's much cleaner per dollar spent"
# Save once
df_new["CtoE_Ratio"] = df_new["CtoE_Ratio"].fillna(0)
df_new.to_csv("datasets/cleaned/cleaned_combined_data.csv", index = False)

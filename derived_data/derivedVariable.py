import pandas as pd
import numpy as np

# Load your cleaned dataset
df = pd.read_csv("derived_data/cleaned_combined_data.csv")

# Filter only for the three energy sources we care about
energy_sources = ["natural gas", "petroleum", "all coal products", "nuclear"]
energy_sources_df = df[df["fuelTypeDescription"].isin(energy_sources)].copy()

# Convert to base units
energy_sources_df["Generation_MWh"] = energy_sources_df["Generation (Thousands of MWh)"] * 1000
energy_sources_df["Expenditure_USD"] = energy_sources_df["Raw Cost (Millions of $)"] * 1_000_000

# Derive price per MWh (guard against divide by zero)
energy_sources_df["Price_per_MWh"] = np.where(
    energy_sources_df["Generation_MWh"] > 0,
    energy_sources_df["Expenditure_USD"] / energy_sources_df["Generation_MWh"],
    np.nan
)

# Select useful columns for output
energy_sources_df = energy_sources_df[[
    "Year", "State", "fuelTypeDescription",
    "Generation_MWh", "Expenditure_USD", "Price_per_MWh"
]].sort_values(["Year", "State", "fuelTypeDescription"])

# Save results
energy_sources_df.to_csv("derived_data/price_per_mwh.csv", index=False)

# Display first few results
energy_sources_df.head(10)

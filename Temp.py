import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
energy_df = pd.read_csv("datasets/cleaned/cleaned_combined_data.csv", encoding='utf-8', delimiter=',')
print(energy_df.columns)
print(energy_df.shape)
print(energy_df.dtypes)
numerical_means = energy_df.mean(numeric_only=True)
print(f"Means of each feature:\n {numerical_means}")
print("\n")
numerical_median = energy_df.median(numeric_only=True)
print(f"Medians fo each feature:\n {numerical_median}")
print("\n")
numerical_std = energy_df.std(numeric_only=True)
print(f"Standard deviation of each feature:\n {numerical_std}") 
print("\n")
summary = pd.DataFrame({
    'Min': energy_df.min(numeric_only=True),
    'Max': energy_df.max(numeric_only=True),
    'Range': energy_df.max(numeric_only=True) - energy_df.min(numeric_only=True)
})
for i in range(len(summary)):
    print(f"{summary.index[i]} -> Min: {summary['Min'].iloc[i]}, Max: {summary['Max'].iloc[i]}")
print("\n")

if(energy_df.isnull().values.any()):
    print("there is no missing values")

print("\n")
Q1 = energy_df.quantile(0.25, numeric_only=True)
Q3 = energy_df.quantile(0.75, numeric_only=True)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Boolean mask for outliers
outliers = energy_df.lt(lower_bound, axis=1) | energy_df.gt(upper_bound, axis=1)

# Count outliers per column
outlier_counts = outliers.sum()
print(outlier_counts)
print('\n')

# Total power generation per fueltype
# Step 1: Group by fuel type and sum the generation
generation_by_type = energy_df.groupby('fueltypeid', as_index=False)['Generation (Thousands of MWh)'].sum()
# Step 2: Sort for better visualization
generation_by_type = generation_by_type.sort_values(by='Generation (Thousands of MWh)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=generation_by_type,
    x='fueltypeid',
    y='Generation (Thousands of MWh)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total Power Generation by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Generation (Thousands of MWh)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)git 
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/power_generation.png', dpi=300, bbox_inches='tight')


# Total ash content per fuel type
# Step 1: Group by fuel type and sum the ash content
ash_by_type = energy_df.groupby('fueltypeid', as_index=False)['Ash Content (%)'].sum()
# Step 2: Sort for better visualization
ash_by_type = ash_by_type.sort_values(by='Ash Content (%)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=ash_by_type,
    x='fueltypeid',
    y='Ash Content (%)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total Ash Content by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Ash Content (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/ash_content_by_type.png', dpi=300, bbox_inches='tight')


# Total sulfur content per fueltype
# Step 1: Group by fuel type and sum the sulfur content
sulfur_by_type = energy_df.groupby('fueltypeid', as_index=False)['Sulfur Content (%)'].sum()
# Step 2: Sort for better visualization
sulfur_by_type = sulfur_by_type.sort_values(by='Sulfur Content (%)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=sulfur_by_type,
    x='fueltypeid',
    y='Sulfur Content (%)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total sulfur content by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Sulfur Content (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/Sulfur_content.png', dpi=300, bbox_inches='tight')

# Total power consumption per fueltype
# Step 1: Group by fuel type and sum the consumption
consumption_by_type = energy_df.groupby('fueltypeid', as_index=False)['Total Consumption (millions of MMBtu)'].sum()
# Step 2: Sort for better visualization
consumption_by_type = consumption_by_type.sort_values(by='Total Consumption (millions of MMBtu)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=consumption_by_type,
    x='fueltypeid',
    y='Total Consumption (millions of MMBtu)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total Power consumption by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Total Consumption (millions of MMBtu)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/Total Consumption.png', dpi=300, bbox_inches='tight')

# Total cost per fueltype
# Step 1: Group by fuel type and sum the cost
cost_by_type = energy_df.groupby('fueltypeid', as_index=False)['Cost ($/MWh)'].sum()
# Step 2: Sort for better visualization
cost_by_type = cost_by_type.sort_values(by='Cost ($/MWh)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=cost_by_type,
    x='fueltypeid',
    y='Cost ($/MWh)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total cost by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Cost ($/MWh)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/Cost.png', dpi=300, bbox_inches='tight')


# Total raw cost per fueltype
# Step 1: Group by fuel type and sum the raw cost
rawcost_by_type = energy_df.groupby('fueltypeid', as_index=False)['Raw Cost (Millions of $)'].sum()
# Step 2: Sort for better visualization
rawcost_by_type = rawcost_by_type.sort_values(by='Raw Cost (Millions of $)', ascending=False)
# Step 3: Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=rawcost_by_type,
    x='fueltypeid',
    y='Raw Cost (Millions of $)',
    palette='viridis'
)
# Step 4: Customize the plot
plt.title('Total raw cost by Energy Type', fontsize=14, weight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Raw Cost (Millions of $)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Step 5: Layout and save
plt.tight_layout()
plt.savefig('EDA_graphs/Raw_Cost.png', dpi=300, bbox_inches='tight')

# Determine missing values and 0 values
if (energy_df.isnull().values.any()) or ((energy_df == 0).values.any()):
    print("There are missing values or zeros in the DataFrame.")
else:
    print("No missing values or zeros found.")
missing_cols = energy_df.columns[energy_df.isnull().any()]
print("Columns with missing values:", list(missing_cols))
zero_cols = energy_df.columns[(energy_df == 0).any()]
print("Columns with zero values:", list(zero_cols))

# Total missing values
missing_count = energy_df.isnull().sum().sum()
print(f"Total missing values: {missing_count}")

# Total zero values
zero_count = (energy_df == 0).sum().sum()
print(f"Total 0 values: {zero_count}")
print("\n")

missing_summary = energy_df.isnull().sum()
print("Missing values per feature:")
print(missing_summary)
print("Total 0 values per feature:")
missing_0summary = (energy_df == 0).sum()
print(missing_0summary)

print("\n")

# Graph for visualizing the total energy cost per state
cost_by_state = energy_df.groupby('State', as_index=False)['Cost ($/MWh)'].sum()
cost_by_state = cost_by_state.sort_values(by='Cost ($/MWh)', ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(data=cost_by_state, x='State', y='Cost ($/MWh)', palette='viridis')
plt.title('Total Energy Cost per State', fontsize=14, weight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Total Cost ($/MWh)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('EDA_graphs/total_cost_by_state.png', dpi=300)

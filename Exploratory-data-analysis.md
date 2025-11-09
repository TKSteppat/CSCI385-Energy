### The goal of this is to provide the structure, patterns, and quality of the dataset.

## Data summary
1.) Number of rows: 1218 <br>
2.) number of duplicate rows: None <br>
3.) Number of features (Columns): 10 <br> 
4.) Data types of each feature: <br>
Year -                                      int64 <br>
State -                                    object <br>
fueltypeid  -                               object <br>
fuelTypeDescription -                      object <br>
Ash Content (%) -                         float64 <br>
Generation (Thousands of MWh) -           float64 <br>
Sulfur Content (%) -                      float64 <br>
Total Consumption (millions of MMBtu) -   float64 <br>
Cost ($/MWh) -                            float64 <br>
Raw Cost (Millions of $) -                float64 <br>

5.) feature descriptions: <br>
Year - The calendar year during which the data was recorded. Serves as the temporal reference for all other features. <br>
State - The U.S. state where the energy data was collected. Useful for regional comparisons and geographic analysis. <br>
fueltypeid - A categorical identifier for the fuel type used. The meaning of each ID is unclear; let's consider mapping it to descriptive labels using a lookup table or metadata source. <br>
Ash Content (%) - The percentage of ash residue produced from fuel combustion. Indicates fuel quality and environmental impact. <br>
Generation (Thousands of MWh) - The amount of electricity generated, measured in thousands of megawatt-hours. Reflects production scale. <br>
Sulfur Content (%) - The percentage of sulfur in the fuel. High values may correlate with greater emissions and regulatory concerns. <br>
Total Consumption (millions of MMBtu) - The total energy consumed, measured in millions of MMBtu (Million British Thermal Units). Useful for assessing demand and fuel usage. <br>
Cost ($/MWh) - The cost of electricity generation per megawatt-hour. A key metric for economic efficiency.<br> 
Raw Cost (Millions of $) - The total monetary cost of generation, measured in millions of dollars. Helps quantify financial investment or burden.<br>


## Statistical summary
1.) Measures of central tendency (mean, median): <br>
### Means of each feature
Ash Content (%)                              2.151404 <br>
Generation (Thousands of MWh)            13719.256780 <br>
Sulfur Content (%)                           0.465735 <br>
Total Consumption (millions of MMBtu)      152.540228 <br>
Cost ($/MWh)                                36.467761 <br>
Raw Cost (Millions of $)                   412.940125 <br>
### median of each feature
Ash Content (%)                             0.00000 <br>
Generation (Thousands of MWh)            3023.10130 <br> 
Sulfur Content (%)                          0.00000 <br>
Total Consumption (millions of MMBtu)      53.23042 <br>
Cost ($/MWh)                               33.00000 <br>
Raw Cost (Millions of $)                  131.60000 <br>
2.) Measures of dispersion (standard deviation): <br>
Ash Content (%)                              4.144487 <br>
Generation (Thousands of MWh)            25199.190056 <br>
Sulfur Content (%)                           1.107974 <br>
Total Consumption (millions of MMBtu)      249.008661 <br>
Cost ($/MWh)                                15.236307 <br>
Raw Cost (Millions of $)                   923.799378 <br>
3.) min/max values: <br>
Year -> Min: 2016.0, Max: 2023.0 <br>
Ash Content (%) -> Min: 0.0, Max: 26.66 <br>
Generation (Thousands of MWh) -> Min: -188.63227, Max: 256140.17982 <br>
Sulfur Content (%) -> Min: 0.0, Max: 6.01 <br>
Total Consumption (millions of MMBtu) -> Min: 0.00028, Max: 2324.03563 <br>
Cost ($/MWh) -> Min: 13.25, Max: 122.5 <br>
Raw Cost (Millions of $) -> Min: 0.0, Max: 14914.8 <br>
4.) count of missing values: 2307 br>
5.) outliers (This is useful for determining if a distribution is skewed): <br>
Ash Content (%)                          178 <br>
Cost ($/MWh)                              11 <br>
Generation (Thousands of MWh)            104 <br>
Raw Cost (Millions of $)                  60 <br>
State                                      0 <br>
Sulfur Content (%)                       115 <br>
Total Consumption (millions of MMBtu)     62 <br>
Year                                       0 <br>
fuelTypeDescription                        0 <br>
fueltypeid                                 0 <br>

## Distribution analysis
1.) Distribution shape (normal, skewed, bimodal, etc):  <br>
2.) Features with heavy tails or long skews:  <br>
3.) Categorial features with imbalanced class distributions:  <br>
4.) Features with missing values or zero values None <br>
Missing values per feature:
Year                                       0
State                                      0
fueltypeid                                 0
fuelTypeDescription                        0
Ash Content (%)                          399
Generation (Thousands of MWh)              0
Sulfur Content (%)                       388
Total Consumption (millions of MMBtu)    221
Cost ($/MWh)                             881
Raw Cost (Millions of $)                 418
Total 0 values per feature:
Year                                       0
State                                      0
fueltypeid                                 0
fuelTypeDescription                        0
Ash Content (%)                          587
Generation (Thousands of MWh)              0
Sulfur Content (%)                       558
Total Consumption (millions of MMBtu)      0
Cost ($/MWh)                               0
Raw Cost (Millions of $)                  27
## Feature assessment
1.) Strong correlations between features:  <br>
2.) highly colinear features:  <br>
3.) Features with high cardinality that may need encoding:  <br>
4.) Inconsistent units:  None <br>
5.) derived variables:  <br>

## Data quality evaluation
1.) How much variation exists within each energy source (e.g., solar costs vary by location:  <br>
2.) Are the units consistent: Yes <br>
3.) Are there duplicate entries:  No <br>

# Practical 10 - DALYs Analysis Task

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ====================== Importing a dataset ======================
# Set the working directory to the folder containing the CSV file
os.chdir("/Users/wuhanddmm/Desktop") # You can change your path here

# Verify current directory and list files
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Load the dataset into a dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ====================== Working with dataframes ======================
# Display first 5 rows to inspect the dataset
print("\n=== First 5 rows ===")
print(dalys_data.head(5))

# Show structure and data types
print("\n=== Data info ===")
dalys_data.info()

# Show statistical summary
print("\n=== Data description ===")
print(dalys_data.describe())

# ====================== iloc and loc ======================
# Access value at first row, fourth column
print("\nValue at (0,3):", dalys_data.iloc[0, 3])
# Experiment with iloc slicing
print("\n--- iloc examples ---")
print(dalys_data.iloc[2, 0:5])
print(dalys_data.iloc[0:2, :])
print(dalys_data.iloc[0:10:2, 0:5])

# Filter data for Afghanistan
afg = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"]

# Select first 10 rows (first 10 years)
afg_first10 = afg.iloc[0:10][["Year", "DALYs"]]
print("\n--- Afghanistan first 10 rows (Year & DALYs) ---")
print(afg_first10)

# Find the year with maximum DALYs in these 10 rows
max_year_afg = afg_first10.loc[afg_first10["DALYs"].idxmax(), "Year"]
# The year with maximum DALYs in Afghanistan's first 10 records is:
print(f"# Max DALYs year (Afghanistan first 10): {max_year_afg}")

# ====================== Boolean filtering ======================
# Create a boolean mask for Zimbabwe
zimbabwe_mask = dalys_data["Entity"] == "Zimbabwe"
# Extract Zimbabwe data
zimbabwe = dalys_data.loc[zimbabwe_mask, :]

print("\n--- Zimbabwe data (sample) ---")
print(zimbabwe[["Entity", "Year", "DALYs"]].head())

# Find first and last year
zim_min = zimbabwe["Year"].min()
zim_max = zimbabwe["Year"].max()

# First and last year for Zimbabwe data
print(f"# Zimbabwe data: {zim_min} - {zim_max}")

# ====================== Across countries ======================
# Filter data for year 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Find countries with max and min DALYs
max_idx = recent_data["DALYs"].idxmax()
min_idx = recent_data["DALYs"].idxmin()

max_country = recent_data.loc[max_idx, "Entity"]
min_country = recent_data.loc[min_idx, "Entity"]
# Countries with highest and lowest DALYs in 2019
print(f"\n# 2019 highest DALYs: {max_country}")
print(f"# 2019 lowest DALYs: {min_country}")

# ====================== Plot ======================
# Select one country (max DALYs)
target = max_country
data = dalys_data.loc[dalys_data["Entity"] == target]

# Plot DALYs over time
plt.figure(figsize=(8,5))
plt.plot(data["Year"], data["DALYs"], 'b+', label=target)

plt.xticks(data["Year"][::5], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {target}")
plt.legend()
plt.tight_layout()
plt.show()

# ====================== Extra Question ======================
# Question: What was the distribution of DALYs across all countries in 2019?

# Plot boxplot of DALYs in 2019
print("\n--- Extra question: 2019 DALYs distribution ---")

plt.figure(figsize=(6,4))
plt.boxplot(recent_data["DALYs"], vert=False, showfliers=True)
plt.xlabel("DALYs")
plt.title("Distribution of DALYs across countries (2019)")
plt.tight_layout()
plt.show()

# Compute range of DALYs
dalys_range = recent_data["DALYs"].max() - recent_data["DALYs"].min()
print(f"# 2019 DALYs range: {dalys_range:.2f}")
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "Country": ["UK", "China", "Italy", "Brazil", "USA"],
    "Population_2020": [66.7, 1426, 59.4, 208.6, 331.6],
    "Population_2024": [69.2, 1410, 58.9, 212.0, 340.1]
}

df = pd.DataFrame(data)

# Step 1: Calculate percentage change (for printing & sorting)
df["Percent_Change"] = ((df["Population_2024"] - df["Population_2020"]) / df["Population_2020"]) * 100

# Step 2: Calculate actual population change (for bar chart)
df["Population_Change"] = df["Population_2024"] - df["Population_2020"]

# Print percentage changes
print("Percentage population change (2020–2024):")
for index, row in df.iterrows():
    print(f"{row['Country']}: {row['Percent_Change']:.2f}%")
print()

# Sort by percentage change
df_sorted = df.sort_values(by="Percent_Change", ascending=False)

print("Sorted population changes (largest increase to largest decrease):")
for index, row in df_sorted.iterrows():
    print(f"{row['Country']}: {row['Percent_Change']:.2f}%")
print()

# Identify largest increase and decrease
largest_increase = df_sorted.iloc[0]
largest_decrease = df_sorted.iloc[-1]

print(f"Largest increase: {largest_increase['Country']} ({largest_increase['Percent_Change']:.2f}%)")
print(f"Largest decrease: {largest_decrease['Country']} ({largest_decrease['Percent_Change']:.2f}%)")
print()

# Step 3: Create bar chart using ACTUAL population change
plt.figure()
bars = plt.bar(df["Country"], df["Population_Change"])

# Labels and title
plt.xlabel("Country")
plt.ylabel("Population Change (millions)")
plt.title("Population Change from 2020 to 2024")

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f"{height:.1f}", ha='center', va='bottom')

plt.show()
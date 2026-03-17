# Import required library for plotting
import matplotlib.pyplot as plt

# Step 1: Create the list of heart rates
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Step 2: Calculate number of patients and mean heart rate
num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / num_patients

# Print required sentence
print(f"There are {num_patients} patients in the dataset and the mean heart rate is {mean_heart_rate:.2f} bpm.")
print()

# Step 3: Initialize counters for each category
low_count = 0
normal_count = 0
high_count = 0

# Step 4: Categorize each heart rate
for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif 60 <= rate <= 120:
        normal_count += 1
    else:  # rate > 120
        high_count += 1

# Print category counts
print(f"Low (<60 bpm): {low_count} patients")
print(f"Normal (60–120 bpm): {normal_count} patients")
print(f"High (>120 bpm): {high_count} patients")
print()

# Step 5: Determine which category has the largest number
counts = {
    "Low": low_count,
    "Normal": normal_count,
    "High": high_count
}

largest_category = max(counts, key=counts.get)

print(f"The category with the largest number of patients is: {largest_category}")
print()

# Step 6: Create a pie chart
labels = ["Low", "Normal", "High"]
sizes = [low_count, normal_count, high_count]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')# '%1.1f%%' was told during class

# Add title
plt.title("Distribution of Heart Rate Categories")

# Show the plot
plt.show()
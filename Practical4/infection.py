# Simulating Infection Rates Over Time
# 1. Define initial conditions: initial infected, growth rate and total students
# 2. Initialize day counter and current infected count
# 3. Loop: calculate new infections each day until all are infected
# 4. Print daily infection count and final day count

# Initial variables
initial_infected = 5    # Starting number of infected students
growth_rate = 0.4       # 40% growth rate per day
total_students = 91     # Total number of students in IBI1 class

current_infected = initial_infected
day = 0

# Print header
print("Day\tInfected Students")
print("------------------------")

# Simulation loop
while current_infected < total_students:
    day += 1
    # Calculate new infections: current * (1 + growth rate)
    current_infected = current_infected * (1 + growth_rate)
    # Ensure we don't exceed total students
    if current_infected > total_students:
        current_infected = total_students
    # Print daily result
    print(f"{day}\t{current_infected:.1f}")

# Report total days taken
print(f"\nTotal days to infect all {total_students} students: {day} days")
# Creatine Clearance Calculator
# 1. Prompt user for age, weight, gender and creatinine concentration
# 2. Validate input values against specified ranges
# 3. If valid, calculate CrCl using Cockcroft-Gault equation
# 4. Output result or error message

# Step 1: Get user inputs (basic information)
age = int(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
gender = input("Enter gender (male/female): ").lower()
Cr = float(input("Enter creatinine concentration (μmol/l): "))

# Step 2: Validate inputs
valid = True
error_msg = ""

# Check if age is within the valid range 
if age >= 100:
    valid = False
    error_msg += "Age must be less than 100 years.\n"
# Check if weight is within the valid range 
if weight <= 20 or weight >= 80:
    valid = False
    error_msg += "Weight must be between 20 and 80 kg.\n"
# Check if creatinine concentration is within the valid range 
if Cr <= 0 or Cr >= 100:
    valid = False
    error_msg += "Creatinine concentration must be between 0 and 100 μmol/l.\n"
# Check if gender is one of the allowed values 
if gender not in ["male", "female"]:
    valid = False
    error_msg += "Gender must be 'male' or 'female'.\n"

# Step 3: Calculate and output result
if valid:
    # Apply Cockcroft-Gault formula
    if gender == "female":
        # Female patients require a 0.85 correction factor
        Crcl = ((140 - age) * weight * 0.85) / (72 * Cr)
    else:
        Crcl = ((140 - age) * weight) / (72 * Cr)
    # Print the final result with 2 decimal places for readability
    print(f"Creatinine Clearance (CrCl): {Crcl:.2f} mL/min")
else:
    print("Error(s):")
    print(error_msg)
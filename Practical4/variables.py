#4.1_Simple Math
#2004 estimated Scotland population (million)
a=5.08
#2014
b=5.33
#2024
c=5.55
#change between 2004 & 2014
d=b-a
#change between 2014 & 2024
e=c-b
#compare, determine growth trend
if e>d:
    growth_trend = 'accelerating'
else:
    growth_trend = 'decelerating'
#output
print(f"Population change 2004-2014: {d} million")
print(f"Population change 2014-2024: {e} million")
print(f"Population growth trend: {growth_trend}")
#Answer to the question:
#d is larger than e, so population growth in Scotland is decelerating

#4.2_Booleans
# Create two Boolean variables X and Y
X = True
Y = False

# Create a new variable W which represents 'X or Y'
W = X or Y

# Truth table for W (X or Y)
# | X     | Y     | W     |
# |-------|-------|-------|
# | True  | True  | True  |
# | True  | False | True  |
# | False | True  | True  |
# | False | False | False |

# Output the value of W
print(f"The value of W (X or Y) is: {W}")
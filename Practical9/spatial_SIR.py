import numpy as np
import matplotlib.pyplot as plt

# Model Parameters
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# 0 = Susceptible (S), 1 = Infected (I), 2 = Recovered (R) 
population = np.zeros((size, size))

# Initial infection: Choose one random point 
outbreak_coords = np.random.choice(range(size), 2)
population[outbreak_coords[0], outbreak_coords[1]] = 1

print('Please close the chart and the program moves on.')

# Define 8 neighbors (Moore neighborhood) 
neighbor_offsets = [(-1,-1), (-1,0), (-1,1), 
                    (0,-1),           (0,1), 
                    (1,-1),  (1,0),  (1,1)]

# Time course simulation
for t in range(time_steps):
    # Use a copy to ensure all transitions happen based on current state 
    new_population = population.copy()
    
    # Find infected points using numpy 
    infected_indices = np.where(population == 1)
    infected_points = list(zip(infected_indices[0], infected_indices[1]))

    # Step 1: All infected cells spread infection to neighbors FIRST
    for r, c in infected_points:
        for dr, dc in neighbor_offsets:
            ni, nj = r + dr, c + dc
            # Boundary check
            if 0 <= ni < size and 0 <= nj < size:
                if population[ni, nj] == 0:
                    if np.random.random() < beta:
                        new_population[ni, nj] = 1
    
    # Step 2: All infected cells recover SECOND (simultaneous update)
    for r, c in infected_points:
        if np.random.random() < gamma:
            new_population[r, c] = 2
            
    # Update grid for next time step
    population = new_population

    # Plot at required time points 
    # Plot spatial grid at time steps t = [0, 9, 49, 99] (zero‑based Python indexing)
    if t in [0, 9, 49, 99]:
        plt.figure(figsize=(6, 4), dpi=150) 
        plt.imshow(population, cmap='viridis', interpolation='nearest') 
        plt.title(f"Spatial SIR Model - Time {t}")
        plt.colorbar(ticks=[0, 1, 2], label="0:S, 1:I, 2:R")
        plt.show()

print("Simulation finished. Different runs will yield different results due to randomness.")
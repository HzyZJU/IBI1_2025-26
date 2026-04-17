import numpy as np
import matplotlib.pyplot as plt

size = 100
beta = 0.3
gamma = 0.05
time_steps = 100
vaccination_rate = 0.1

population = np.zeros((size, size))

print('Please close the chart and the program moves on.')

# Vaccination 
num_vaccinated = int(size * size * vaccination_rate)
vaccinated_indices = np.random.choice(size * size, num_vaccinated, replace=False)

for idx in vaccinated_indices:
    r = idx // size
    c = idx % size
    population[r, c] = 3  # vaccinated

# Initial infection (avoid vaccinated)
while True:
    outbreak_coords = np.random.choice(range(size), 2)
    if population[outbreak_coords[0], outbreak_coords[1]] == 0:
        break

population[outbreak_coords[0], outbreak_coords[1]] = 1

neighbor_offsets = [(-1,-1), (-1,0), (-1,1), 
                    (0,-1),         (0,1), 
                    (1,-1), (1,0), (1,1)]

for t in range(time_steps):
    new_population = population.copy()

    infected_indices = np.where(population == 1)
    infected_points = list(zip(infected_indices[0], infected_indices[1]))

    # Infection
    for r, c in infected_points:
        for dr, dc in neighbor_offsets:
            ni, nj = r + dr, c + dc
            if 0 <= ni < size and 0 <= nj < size:
                if population[ni, nj] == 0:
                    if np.random.random() < beta:
                        new_population[ni, nj] = 1

    # Recovery
    for r, c in infected_points:
        if np.random.random() < gamma:
            new_population[r, c] = 2

    population = new_population

    if t in [0, 9, 49, 99]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR with Vaccination (t={t})")
        plt.colorbar(ticks=[0,1,2,3], label="0:S,1:I,2:R,3:V")
        plt.show()
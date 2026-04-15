# Practical_9_Task_1

# Background Information：
# SIR models (Susceptible - Infected - Recovered or Resistant) are used to study how infectious diseases spread through a population. 
# In its simplest form, the model assumes that the population being studied falls into three separate groups: Susceptible individuals (S) are healthy, but may contract the disease. 
# Infected people (I) have contracted the disease and can pass it on to suscep-tible people at a rate that depends on an infection probability upon contact β (beta) and on the proportion of infected people in the population. 
# An infected person can recover (R) with recovery probability γ (gamma), and is assumed to be immune to the disease after recovery

import numpy as np
import matplotlib.pyplot as plt

# parameters
N = 10000 # Total number of people in the population
S = N - 1 # Susceptible
I = 1 # Infected
R = 0 # Recovered

beta = 0.3
gamma = 0.05

# storage lists
S_list = [S]
I_list = [I]
R_list = [R]

time_steps = 1000

for t in range(time_steps):

    # infection probability
    infection_prob = beta * (I / N)

    # stochastic transitions
    new_infections = np.random.binomial(S, infection_prob)
    new_recoveries = np.random.binomial(I, gamma)

    # update
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    # store
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# plot
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("SIR Model")
plt.legend()

plt.show()

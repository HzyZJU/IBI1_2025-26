# Task 2
import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccination_percentages = range(0, 101, 10)

plt.figure(figsize=(6,4), dpi=150)

for v_percent in vaccination_percentages:

    vaccinated = int(N * v_percent / 100)

    S = N - vaccinated - 1
    I = 1
    R = vaccinated

    I_list = [I]

    for t in range(time_steps):

        # n > 0
        S = max(S, 0)
        I = max(I, 0)

        # infection probability
        infection_prob = beta * (I / N)
        infection_prob = min(infection_prob, 1)

        # n > 0
        if S > 0:
            new_infections = np.random.binomial(S, infection_prob)
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.random.binomial(I, gamma)
        else:
            new_recoveries = 0

        # update
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        I_list.append(I)

    plt.plot(I_list, label=f"{v_percent}%")

plt.xlabel("Time")
plt.ylabel("Infected")
plt.title("SIR model with different vaccination rates")
plt.legend()

plt.show()

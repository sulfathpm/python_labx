import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the logistic equation
def logistic_model(P, t, r, K):
    dPdt = r * P * (1 - P / K)
    return dPdt

# Parameters
r = 0.1      # Intrinsic growth rate
K = 1000     # Carrying capacity
P0 = 10      # Initial population

# Time points
t = np.linspace(0, 100, 1000)

# Solve the ODE
P = odeint(logistic_model, P0, t, args=(r, K))

# Plot the solution
plt.plot(t, P, label="Population Growth")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Logistic Population Growth Model")
plt.legend()
plt.grid(True)
plt.show()

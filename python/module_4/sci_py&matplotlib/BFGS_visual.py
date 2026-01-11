import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Store optimization steps
path = []

def objective_function(x):
    path.append(x[0])      # Save each x value
    return x[0]**2 + 10*np.sin(x[0])

# Initial guess (must be array)
x0 = [2]

# Perform minimization using BFGS
result = minimize(objective_function, x0, method='BFGS')

# Generate x values for plotting
x = np.linspace(-5, 5, 400)
y = x**2 + 10*np.sin(x)

# Plot the function
plt.plot(x, y, label="Objective Function")

# Plot optimization path
path = np.array(path)
plt.scatter(path, path**2 + 10*np.sin(path), color='red', label="Optimization Path")

# Labels and title
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Optimization using BFGS Algorithm")
plt.legend()
plt.grid()

plt.show()

# Print result
print("Minimum value:", result.fun)
print("Value of x at minimum:", result.x[0])

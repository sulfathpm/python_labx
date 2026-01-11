import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# List to store optimization path
path = []

def objective_function(x):
    path.append(x[0])      # Save current x value
    return x[0]**2 + 10*np.sin(x[0])

# Initial guess (array)
x0 = [-4]

# Minimize using BFGS algorithm
result = minimize(objective_function, x0, method='BFGS')

# Generate x values for plotting function
x = np.linspace(-5, 5, 400)
y = x**2 + 10*np.sin(x)

# Plot the function
plt.plot(x, y, label="Objective Function")

# Plot optimization path
path = np.array(path)
plt.scatter(path, path**2 + 10*np.sin(path), color='red', label="Optimization Path")

# Plot settings
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Visualization of Optimization Path (BFGS)")
plt.legend()
plt.grid()

plt.show()

# Print results
print("Minimum value:", result.fun)
print("Value of x at minimum:", result.x[0])

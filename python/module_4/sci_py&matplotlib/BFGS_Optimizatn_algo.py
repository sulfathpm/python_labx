import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    return x[0]**2 + 10 * np.sin(x[0])

# Initial guess (must be an array)
x0 = [2]

# Minimize using default BFGS method
result = minimize(objective_function, x0, method='BFGS')

print("Minimum value:", result.fun)
print("Value of x at minimum:", result.x[0])

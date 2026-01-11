import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate 1000 random samples from a normal distribution
mu = 10      # Mean
sigma = 3   # Standard deviation
samples = norm.rvs(mu, sigma, size=1000)

# Plot a histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.6)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of 1000 Random Samples from a Normal Distribution')

plt.show()

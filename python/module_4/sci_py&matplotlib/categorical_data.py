import numpy as np
import matplotlib.pyplot as plt

# CO 4, Qs. #4
# Sample data in a NumPy array
data = np.array([25, 15, 30, 10, 20])

# Labels for the data
labels = ['A', 'B', 'C', 'D', 'E']

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, data)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# CO 4, Qs. #4
# Sample data in a NumPy array
data = np.array([25, 15, 30, 10, 20])

# Labels for the data
labels = ['A', 'B', 'C', 'D', 'E']

# Horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(labels, data)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart')

plt.show()

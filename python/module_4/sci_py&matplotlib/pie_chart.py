import numpy as np
import matplotlib.pyplot as plt

# CO 4, Qs. #4
# Sample data in a NumPy array
data = np.array([25, 15, 30, 10, 20])

# Labels for the data
labels = ['A', 'B', 'C', 'D', 'E']

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.show()

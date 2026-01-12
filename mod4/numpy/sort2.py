import numpy as np
a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])
print ("Array elements in sorted order:\n", np.sort(a, axis = None))
print ("Row-wise sorted array:\n", np.sort(a, axis = 1))
print ("Row-wise sorted array:\n", np.sort(a, axis = 0))


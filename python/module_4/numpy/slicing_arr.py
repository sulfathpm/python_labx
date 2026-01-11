import numpy as np
arr = np.array([[-1, 2, 0, 4],
 [4, -0.5, 6, 0],
[2.6, 0, 7, 8],
[3, -7, 4, 2.0]])
# Slicing array
temp = arr[:2, ::2]
print ("arr1:", temp)
temp = arr[2:, :4:1]
print ("arr2:", temp)
temp = arr[1:-1, :2]
print ("arr3:", temp)
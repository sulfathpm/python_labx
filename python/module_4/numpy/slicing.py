import numpy as np
arr = np.array([[-1, 12, 10, 4],
 [4, -2, 6, 20],
[2, 0, 7, 8],
[3, -7, 4, 2.0]])
# Slicing array
temp = arr[:2, ::2]
print ("arr1:", temp)
temp = arr[2::4,:1]
print ("arr2:", temp)
temp = arr[::-1]
print ("arr3:", temp)
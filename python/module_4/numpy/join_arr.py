import numpy as np
array_1 = np.array([[1, 2],[8,9]]) 
array_2 = np.array([[3, 4],[5,6]]) 
array_new = np.concatenate((array_1, array_2)) 
print("arr1:",array_new)
array_1 = np.array([1, 2]) 
array_2 = np.array([3, 4]) 
array_new = np.concatenate((array_1, array_2)) 
print("arr2:",array_new)
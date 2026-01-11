import numpy as np
arr1=np.array([[1,2,3],
              [2,3,1],
              [1,2,1]])
arr2=np.array([[3,4,5],
               [3,2,1],
               [2,3,1]])

print("sum of 2 arrays:",arr1+arr2)
print("Array multiplication:\n", arr1*arr2)
print ("Matrix multiplication:\n", arr1.dot(arr2))


import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("array:",arr)
print("Largest element:",arr.max())
print("Row-wise largest element:",arr.max(axis=1))
print("Column-wise largest element:",arr.max(axis=0))
print("Sum of all elements:",arr.sum())
print("Row-wise sum of element:",arr.sum(axis=1))
print("column-wise sum of element:",arr.sum(axis=0))

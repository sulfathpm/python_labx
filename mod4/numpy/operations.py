import numpy as np
# arr=np.array([[[1,2,3],[3,4,5]],[[4,5,6],[2,3,4]]])
arr=np.array([[1,2,3],[4,5,6]])
print("total-sum:",np.sum(arr))
print("colum-wise sum:",np.sum(arr,0))
print("row-wise sum:",np.sum(arr,1))
print("cumulative-sum:",np.cumsum(arr))
print("cumulative-sum:",np.cumsum(arr,axis=1))


print("min-value:",np.min(arr))
print("column-wise min-value:",np.min(arr,0))
print("row-wise min-value:",np.min(arr,1))

print("max-value:",np.max(arr))
print("column-wise max-value:",np.max(arr,0))
print("row-wise max-value:",np.max(arr,1))

print("row-wise max-value:",arr.max(axis=1))

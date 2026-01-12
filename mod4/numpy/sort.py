import numpy as np
a=np.array([[11,2,34],[4,15,6],[12,32,1],[14,44,21]])
print(a)
print("sorted arr:",np.sort(a))
print("sort column-wise:",np.sort(a,axis=0))
print("sort row-wise:",np.sort(a,axis=1))
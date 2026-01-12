import numpy as np
a=np.array([1,2,3,4,5,6.7,8,9,10])
arr=a[a%2!=0]
print("list of odd numbers:",arr)
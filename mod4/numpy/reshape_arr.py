import numpy as np
arr=np.array([[1,2,3,8],[4,5,6,7]])
print("arr:",arr)
arr1=arr.reshape(4,2)
print("arr1:",arr1)

arr2=arr.reshape(2,2,2)
print("arr2:",arr2)

arr3=arr.reshape(8,1)
print("arr3:",arr3)

arr4=arr.reshape(1,8)
print("arr4:",arr4)

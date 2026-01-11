import numpy as np
arr=np.array([[[1,2,3],
               [5,6,7]],
              [[9,10,11],
               [13,14,15]]])
print("Original array:\n", arr)
reshaped_arr=arr.reshape(3,4)
print("Reshaped array (3x4):\n", reshaped_arr)
reshaped_arr_2=arr.reshape(2,3,2)
print("Reshaped array (2x3x2):\n", reshaped_arr_2)
reshaped_arr_3=arr.reshape(6,2)
print("Reshaped array (6x2):\n", reshaped_arr_3)
reshaped_arr_4=arr.reshape(12)
print("Reshaped array (12,):\n", reshaped_arr_4)
reshaped_arr_5=arr.reshape(-1,4)
print("Reshaped array (-1x4):\n", reshaped_arr_5)

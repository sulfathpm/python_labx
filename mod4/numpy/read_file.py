import numpy as np
filename = 'mod4/numpy/abc.txt'

data_collect=np.loadtxt(filename)
print(data_collect)
print(f'stored in:{type(data_collect)} and data type :{data_collect.dtype}')
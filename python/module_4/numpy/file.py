import numpy as np
filename = r"C:\pgms\python\module_4\numpy\sample.txt"
data_collected = np.loadtxt(filename)
print("data from file:",data_collected)
print(f'Stored in : {type(data_collected)} and data type is : {data_collected.dtype}')
# data_collected_f = np.loadtxt(filename, dtype='float')
# print("data from file:",data_collected_f)
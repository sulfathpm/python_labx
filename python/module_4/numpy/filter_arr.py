import numpy as np
import math
a = np.array([1, 2, 3, 7,40, 50, 100,21])
filter2=(a%2!=0)
print(filter2)
print("array:",a[filter2])
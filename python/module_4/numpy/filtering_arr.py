import numpy as np
a = np.array([1, 2, 3, 40, 50, 100,21])
filter_a=a>20
print(np.array(filter_a))
print(a[filter_a])

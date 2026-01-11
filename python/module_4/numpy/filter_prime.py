import numpy as np
import math

a = np.array([1, 2, 3, 7, 40, 50, 100, 21])

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Vectorized filtering
filter2 = np.array([is_prime(x) for x in a])

print(filter2)
print("array:", a[filter2])

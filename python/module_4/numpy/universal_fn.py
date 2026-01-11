import numpy as np
a = np.array([0, 45, 90])
rad = np.deg2rad(a)
# rad = a * np.pi / 180

print("Radians:", rad)

print ("Sine values of array elements:", np.sin(rad))
print ("Cosine values of array elements:", np.cos(rad))
print ("Tangent values of array elements:", np.tan(rad))

a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))
a=np.array([0,2,3,4,9])
print ("Square root of array elements:", np.sqrt(a))

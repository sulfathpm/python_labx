import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("arr1",a[:1,:2])
a=np.array([[[1,2],[3,4],[11,13]],[[5,6],[7,8],[21,22]]])
print("arr2",a[1:,0:2,:1])
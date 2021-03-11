import numpy as np

array1=np.array([1,2,3])
array2=np.array([4,5,6])
array3=np.concatenate([array1,array2])

print(array3.shape)
print(array3)

array5=np.array([1,2,3,4])
array6=array5.reshape((2,2))

print(array6)


import numpy as np

array=np.array([5,9,20,3,1])
array.sort()
print(array)

print(array[::-1])

array2=np.array([[5,9,10,3,1],[8,3,4,2,5]])
array2.sort(axis=0)
print(array2)
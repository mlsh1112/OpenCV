import numpy as np

array=np.linspace(0,10,5)
print(array)

np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

array1=np.arange(0,10)
array2=array1.copy()
array2[0]=99
print(array1)

array3=np.array([1,1,2,3,3,1])
print(np.unique(array3))
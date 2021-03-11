import numpy as np

array=np.random.randint(1,10,size=4).reshape(2,2)
result_array=array*10
#print(array)
#print(result_array)

array1=np.arange(4).reshape(2,2) #2x2
array2=np.arange(2) #1x2
array3=array1+array2
print(array1)
print(array2)
print(array3)

array4=np.arange(0,8).reshape(2,4)
array5=np.arange(0,8).reshape(2,4)
array6=np.concatenate([array4,array5],axis=0)
array7=np.arange(0,4).reshape(4,1) #4X1

print(array6+array7)

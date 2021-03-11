import numpy as np

array=np.arange(0,10)
#np.save('saved.npy',array)

#result=np.load('saved.npy')
#print(result)

#복수 객체
array1=np.arange(0,10)
array2=np.arange(10,20)
np.savez('saved2.npz',array1=array1,array2=array2)

data=np.load('saved2.npz')
result1=data['array1']
result2=data['array2']

print(result1)
print(result2)


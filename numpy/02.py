import numpy as np

#0~3 배열
array1=np.arange(4)
print(array1)

array2=np.zeros((4,4),dtype=float)
print(array2)

array3=np.ones((3,3),dtype=str)
print(array3)

#random inital (0~9)
array4=np.random.randint(0,10,(3,3))
print(array4)

#평균 0 표준편차 1 표준 정규를 띄는 배열
array5=np.random.normal(0,1,(3,3))
print(array5)

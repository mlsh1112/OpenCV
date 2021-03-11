#이미지 위치 변경
import  cv2
import numpy as np

img=cv2.imread('cat.png')

height,width=img.shape[:2]

M=np.float32([[1,0,50],[0,1,10]])
dst=cv2.warpAffine(img,M,(width,height))
cv2.imshow('img',dst)
cv2.waitKey(0)

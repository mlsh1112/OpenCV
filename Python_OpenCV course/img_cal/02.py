#특정 범위 픽셀 변경
import cv2

image=cv2.imread('cat.png')

#1

#for i in range(0,100):
#    for j in range(0,100):
#        image[i,j]=[255,255,255]

image[0:100, 0:100]=[0,0,0]


cv2.imshow('image',image)
cv2.waitKey(0)
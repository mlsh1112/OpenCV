#이미지 합치기
import cv2

img1=cv2.imread('dog.png')
img2=cv2.imread('cat.png')

#cv2에서 saturation 연산
result=cv2.add(img1,img2)
cv2.imshow('img',result)
cv2.waitKey(0)

#numpy
result=img1+img2
cv2.imshow('img',result)
cv2.waitKey(0)

#이미지 크기 변경
import cv2

img=cv2.imread('cat.png')

cv2.imshow('img',img)
cv2.waitKey(0)

expand=cv2.resize(img,None,fx=2.0,fy=2.0,interpolation=cv2.INTER_CUBIC)
cv2.imshow('expand',expand)
cv2.waitKey(0)

shrink=cv2.resize(img,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_AREA)
cv2.imshow('shrink',shrink)
cv2.waitKey(0)




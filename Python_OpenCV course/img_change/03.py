#이미지 회잔
import cv2

img=cv2.imread('cat.png')

height,width=img.shape[:2]

M=cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
dst=cv2.warpAffine(img,M,(width,height))
cv2.imshow('img',dst)
cv2.waitKey(0)
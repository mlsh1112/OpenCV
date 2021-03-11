#픽셀별로 색상 다루기
import cv2

image=cv2.imread('cat.png')

cv2.imshow('Cat',image[:,:,0])
cv2.waitKey(0)

image[:,:,2]=0
cv2.imshow('Cat',image)
cv2.waitKey(0)


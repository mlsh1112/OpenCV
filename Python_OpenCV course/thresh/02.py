#이미지의 적응 임계점 처리
import cv2

img=cv2.imread('handwriting.png',cv2.IMREAD_GRAYSCALE)

thres1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,3)
thres2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,3)

cv2.imshow('img',thres1)
cv2.waitKey(0)

cv2.imshow('img',thres2)
cv2.waitKey(0)
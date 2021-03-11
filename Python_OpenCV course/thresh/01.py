#이미지의 기본 이진화
import cv2

img=cv2.imread('handwriting.png')

images=[]
ret,thres1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thres2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thres3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thres4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thres5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    cv2.imshow('img',i)
    cv2.waitKey(0)


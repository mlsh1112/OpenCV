import cv2

img=cv2.imread('digit.png')
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,127,255,0)
cv2.imshow('img',thresh)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img=cv2.drawContours(img,contours,-1,(0,255,0),4)
cv2.imshow('img',img)
cv2.waitKey(0)

contour=contours[0]
hull=cv2.convexHull(contour)
img=cv2.drawContours(img,[hull],-1,(255,0,0),4)
#x,y,w,h=cv2.boundingRect(contour)
#img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow('img',img)
cv2.waitKey(0)
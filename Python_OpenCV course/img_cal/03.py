#ROI 추출

import cv2

image=cv2.imread('cat.png')

roi=image[20:150, 70:200]

image[0:130, 0:130]=roi
cv2.imshow('Cat',image)
cv2.waitKey(0)
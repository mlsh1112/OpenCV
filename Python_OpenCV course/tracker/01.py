import cv2
import numpy as np

def change_color(x):
    r = cv2.getTrackbarPos("R","image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    image[:]=[b,g,r]
    cv2.imshow('img',image)

image=np.zeros((600,400,3),np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("R","image",0,255,change_color)
cv2.createTrackbar("G","image",0,255,change_color)
cv2.createTrackbar("B","image",0,255,change_color)

cv2.imshow('img',image)
cv2.waitKey(0)

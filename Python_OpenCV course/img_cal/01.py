#이미지 크기 및 픽셀 확인

import cv2
image=cv2.imread('cat.png')
print(image.shape)
print(image.size)

px=image[100,100]
print(px)


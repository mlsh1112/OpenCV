import cv2
import numpy as numpy
import matplotlib.pyplot as plt


def showimage():
     imgfile="pizza.jpeg"
     img=cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
     
     #img=plt.imread('pizza.jpeg')
     #plt.imshow(a)

     plt.imshow(img, cmap='gray',interpolation='bicubic') #흑백
     plt.xticks([])
     plt.yticks([])
     plt.title('pizza')
     plt.show()

showimage()

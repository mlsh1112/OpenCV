import cv2
import numpy as np


image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 3)

cv2.imshow("img",image)
cv2.waitKey(0)
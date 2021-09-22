import numpy as np
import imageio
import scipy.ndimage
import cv2
import os
os.system('cls')


image = cv2.imread("Myimg.JPG")
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_image)
blur = cv2.GaussianBlur(invert, (25, 25), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_image, invertedblur, scale=200.0)
cv2.imwrite("image.png", sketch)
#cv2.waitKey(0)

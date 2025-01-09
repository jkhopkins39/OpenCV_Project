import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Photos/Mountain.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
orb = cv.ORB.create()

#Find the keypoints and compute descriptors with ORB
kp, des = orb.detectAndCompute(img, None)

#Draw keypoints location
img2 = cv.drawKeypoints(img, kp, None)
plt.imshow(img2),plt.show()
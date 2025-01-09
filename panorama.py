import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

dim=(1024,768)
left = cv.imread('IMG_2343.DNG', cv.IMREAD_COLOR)
left = cv.resize(left, dim, interpolation=cv.INTER_AREA)
left1 = cv.cvtColor(left, cv.COLOR_BGR2RGB)

right = cv.imread('IMG_2344.DNG', cv.IMREAD_COLOR)
right = cv.resize(right, dim, interpolation=cv.INTER_AREA)
right1 = cv.cvtColor(right, cv.COLOR_BGR2RGB)

f, axarr = plt.subplots(1, 2)
axarr[0].imshow(left1)
axarr[1].imshow(right1)
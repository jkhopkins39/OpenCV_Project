import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread("Photos/Mountain.jpg")
cv.imshow('Mountain', img)

#Blurring
average = cv.blur(img, (3,3))
cv.imshow('Smoothing', average)
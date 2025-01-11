import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/Mountain.jpg")
cv.imshow('Mountain', img)
# plt.imshow(img)
# plt.show()

# #BGR to Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# #BGR to LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# #BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# bgr = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
# cv.imshow("HSV to BGR", bgr)

blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

cv.waitKey(0)
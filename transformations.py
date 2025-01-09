import cv2 as cv
import numpy as np

img = cv.imread('Photos/Mountain.jpg')
cv.imshow('Mountain', img)

# #translates the image within the frame, leaving black space behind
# def translate(img, x,y):
#     transMatrix = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMatrix, dimensions)

# # -x --> left
# # -y --> up
# # x --> right
# # y --> down

# translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

#Rotates image
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)

#     rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
#     return cv.warpAffine(img, rotMatrix, dimensions)

# #rotation can be repeated and done on rotated images however there will be data loss. better to just change angle
# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# #1 is for across, 0 is for upside down, -1 is both
# flipped = cv.flip(img, 1)
# cv.imshow('Flipped', flipped)

transposed = cv.transpose(img)

cv.imshow('Transposed', transposed)

cv.waitKey(0)
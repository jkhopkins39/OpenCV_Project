import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("flower.jpg")
cv.imshow("Flower", img)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

weights = np.array([0.114, 0.587, 0.299]) #Order: BGR
dotProductGray = np.dot(img[..., :3], weights)
dotProductGray = np.clip(dotProductGray, 0, 255).astype(np.uint8) #Pass through clip method to correct dimensions and return type

#This version displays the grayscale applied by OpenCV
plt.imshow(gray, cmap='gray')
plt.title("OpenCV Grayscale")
plt.show()

plt.imshow(dotProductGray, cmap='gray')
plt.title("Dot Product Grayscale")
plt.show()


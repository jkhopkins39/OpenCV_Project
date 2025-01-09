import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')

img = cv.imread('Photos/Lenna.png')
inputImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    roi_gray = gray[y:y+h, x: x+w]
    roi_color = img[y:y+h, x: x+w]
    eyes = eyes_cascade.detectMultiScale(roi_gray)

    for (ey,ex,ew,eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255,0), 2)

f, axarr = plt.subplots(1,2)
axarr[0].imshow(inputImg)
axarr[1].imshow(img)

cv.imwrite('face_detection.jpg', img)
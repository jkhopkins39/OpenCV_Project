import cv2 as cv
import numpy as np

#This creates a blank 500x500 frame of data type uint8
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#This takes the blank frame and draws YELLOW (0,255,255) across the parameterized section 200-300 and 300-400
# blank[200:300, 300:400] = 0,255,255
# cv.imshow('Green', blank)

""" This takes the blank frame and defines the origin about which it will be drawn, and the shape can be defined
with size equal to, in this case, 1/3 of the size of the window height and width wise. thickness -1 means FILLED """
# cv.rectangle(blank, (0,0), (blank.shape[0]//3, blank.shape[0]//3), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

""" Drawing a circle
This is similar, here I have explicitly defined each parameter """
# cv.circle(img=blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

#Drawing a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

cv.putText(blank, "HELLO", (225,225), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
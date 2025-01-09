import cv2 as cv
img = cv.imread('Photos/Mountain.jpg')
cv.imshow('Mountain', img)

#Converts to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blurs a given image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# #Edge cascade, threshold 1 and 2 are for the hysteresis procedure, 1 is lowbound for unsure edges and 2 is for sure edges, blur reducing edges detected
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Cany!', canny)

# #Dilates (grows) edges
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilate', dilated)

# #Erodes (shrinks) edges
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# #Essentially forces resizing to the specified size
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resizing', resized)

#Cropping, this essentially gives you a frame that is the defined coordinates of an image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
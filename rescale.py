import cv2 as cv

#this reads in an image using cv.imread and shows it using imshow
img = cv.imread('Photos/Mountain.jpg')
cv.imshow('Mountain', img)

#this method sets your webcam's width and height to the passed parameters 
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

#this method scales your video by the scale parameter with frame being your video or picture frame
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#here we simply rescale a Mountain image with the rescaleFrame method and read it in using imshow
resized_image = rescaleFrame(img)
cv.imshow('Mountain Resized', resized_image)

#this defines capture as the video readin of some DOOM gameplay I did last year
capture = cv.VideoCapture("Videos/DOOM.mp4")

'''this while loop defines frame as the readin of the current frame and runs for each frame in the video.
In this example we define a 0.2 scale frame and run the loop on the normal and scaled versions. The loop
runs until the 'd' key is pressed, or until the last frame of the video is reached.'''
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#once the above loop breaks, this ensures that the capture variable is released and all generated windows go away
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
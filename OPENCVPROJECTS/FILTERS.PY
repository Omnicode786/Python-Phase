import cv2 as cv


img = cv.imread('photos\\personasphoto.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#  since the image is very large lets resize it
#  the resize function
gray = cv.resize(gray,(1080,1920),interpolation=cv.INTER_AREA)

cv.imshow('Grayish', gray)

cv.waitKey(0)
import cv2 as cv


img = cv.imread('photos\\person.jpeg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#  since the image is very large lets resize it
#  the resize function
gray = cv.resize(gray,(1080,1920),interpolation=cv.INTER_AREA)

cv.imshow('Grayish', gray)


blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
# the color science have to be an odd number
cv.imshow('Blue', blur)
# to increase the blur increase the color science
blur2 = cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT)

cv.imshow('Blur', blur2)

# edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)
# we can reduce the edges by inctroducing blur

canny = cv.Canny(blur,125,175)
cv.imshow('Canny2',canny)

# dialating theimage

dialatd = cv.dilate(canny,(7,7), iterations=3)
cv.imshow('dialated',dialatd)
# colo sience makes dialation thicker
# eroding
eroded = cv.erode(dialatd, (3,3) , iterations=1)
cv.imshow('eroded', eroded)

# resize and crop

resized = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
# for enraleging and scale to larger dimension we would use inter linear or cubic cubci is the slower among than all but of higher quality
# for shrinking
# interpolation inter area helps if we are shrinking th image to smaller than that of the orignal image

cv.imshow('Resized',resized)

# cropping
# since images are arrays we can select a specifc pixel area and use that

crop = img[50:200, 200:400]
cv.imshow('cropped',crop ) 

cv.waitKey(0)
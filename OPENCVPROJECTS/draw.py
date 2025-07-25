import cv2 as cv
import numpy as np

# we can also create a blank image using numpy
blank = np.zeros((500,500 ,3),dtype='uint8')
cv.imshow('blank',blank)
# np.zeros() is a NumPy function that creates an array filled with zeros.

# The shape (500, 500,3) means:

# 500 rows (height)

# 500 columns (width)

# the 3 there means the number of color channels

# So, it's a grayscale image with:

# Width = 500 pixels

# Height = 500 pixels

# All pixel values = 0 (which means black in grayscale)

# dtype simply means data type uint8 means unsigned inter 8 bit which allows 0 to 255 its an image data type 

# blank is a 2d array so 
# OpenCV uses BGR, not RGB



blank[:] = 255,0,0
cv.imshow('Blue',blank)
blank[:] = 0,255,0
cv.imshow('Green',blank)

blank[:] = 0,0,255
cv.imshow('Red',blank)

# we can also give a certain portion of the canvas a specific color and rest not 
blank[330:400,200:300] = 0,0,255
# remember how indexing works its a 2d array the np.zeros funciton
cv.imshow('mixed',blank)

# what we can also do is draw shapes on the canvas
blank[:] = 0, 0, 0 
cv.rectangle(blank, (0,0), (455,300), (0,255,0), thickness=2)
cv.imshow('rectangle',blank)
# cv.rectangle(img, pt1, pt2, color, thickness)
# The image you want to draw on. (here: blank)
#  pt 1 = the first is the image to work on the 2nd is the 
# pt 2 = Bottom-right corner of the rectangle (x2, y2)

# color = Color in BGR format, e.g., green = (0, 255, 0)

# what if we want to fill the rectangle
cv.rectangle(blank, (0,0), (455,300), (0,255,0), thickness=cv.FILLED)

# cv.Filled use or we can also use -1

cv.imshow('rectanglefilled',blank)

cv.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,255,0), thickness=2)

cv.imshow('halvedrectangle',blank)

cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2),50,(120,2,222),thickness=-1)
cv.imshow('cicle',blank)


cv.line(blank,(0,0),(blank.shape[1] // 2, blank.shape[0] // 2),(255,255,255),thickness=3)
cv.imshow('line',blank)

# write txt

cv.putText(blank,"Muzammil The BEAST",(120,255),cv.FONT_ITALIC,1.0,(255,255,255), thickness=2)
cv.imshow('BEAST',blank)

# img = cv.imread('OPENCVPROJECTS\\photos\\person.jpeg')

# cv.imshow('Image',img)
cv.waitKey(0)
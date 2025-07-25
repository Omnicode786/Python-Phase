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



# blank[:] = 255,0,0
# cv.imshow('Blue',blank)
# blank[:] = 0,255,0
# cv.imshow('Green',blank)

# blank[:] = 0,0,255
# cv.imshow('Red',blank)

# we can also give a certain portion of the canvas a specific color and rest not 
blank[0:400,0:300] = 0,0,255
# remember how indexing works its a 2d array the np.zeros funciton
cv.imshow('mixed',blank)


# img = cv.imread('OPENCVPROJECTS\\photos\\person.jpeg')

# cv.imshow('Image',img)
cv.waitKey(0)
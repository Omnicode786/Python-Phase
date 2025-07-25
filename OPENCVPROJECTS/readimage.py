import cv2 as cv

from PIL import Image


pixels = cv.imread('OPENCVPROJECTS\photos\person.jpeg')
print (pixels)

# if the image was of the size far greater than the size of your monitor 
# than you can rescale and resize them through different means

# this function basically reads the bits matrix of pixels essentially

cv.imshow('person', pixels)
cv.waitKey(0) #waits for a keyboard press fro infinity

# has two parameters thename of the photo to show and the matrix pixels

# another way of doing the above is through the pil library
# the above opens in a python script file where the below opens in the native photo shower app

img = Image.open('OPENCVPROJECTS\photos\person.jpeg')

img.show()
import cv2 as cv
import numpy as np

#Transformation

def translate(img,x ,y):
    # this takes a list with two lists
    transMat = np.float32([[1,0,x],[0,1,y]])
    # shape 1 gives width and shape 0 gives height 
    dimenstions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimenstions)

# -x values shifting to left 
# +y values measn shifting down 
# +x means shifting to right 
# -y values measn shifting up 


# Rotation 

def rotate(img,angle, rotPoint =None):
    # rot point is the point which we want to roate initializing it to none
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    # the point which we want to rotate the image the angle and the scaling for nwo lets keep it at 1.0
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)






img = cv.imread(r'photos\person.jpeg')

cv.imshow('Photo',img)



trnaslated = translate(img,100,100)
cv.imshow('Transalte img',trnaslated)

rotatedImg = rotate(img,60)
cv.imshow('Rotated image',rotatedImg)


# resizing

resized= cv.resize(img,(1920,1080),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', resized )


# Fliping

flip = cv.flip(img, 1)
# 0 impies fliping the image vertically  1 specifies fliping the image horizontally -1 is both 
cv.imshow('Flipped',flip)

cv.waitKey(0)
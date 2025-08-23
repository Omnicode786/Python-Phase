import cv2 as cv

capture = cv.VideoCapture('OPENCVPROJECTS\\videos\\Paper Background  Reels  Shorts  Edit Elements - Edit Elements (1080p, h264).mp4')

def rescaleFrame(frame, scale = 0.1):
    # scale can vary easily depends onus
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

# frame shape 1 is width and height is 0 
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
    # resizes frame to a particular dimentsion



img = cv.imread('photos\\photo2.jpg')
if img is None:
    print("Image not found!")
else:
    cv.imshow('Image', img)
    resize_image = rescaleFrame(img)
    cv.imshow("Resized Image", resize_image)




while True:
    isTrue, frame = capture.read()
    if not isTrue:   # video ended or error
        print("Video ended or cannot read frame.")
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()
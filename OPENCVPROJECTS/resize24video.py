import cv2 as cv
# this will not work with already existing image or video only works with live videos
# capture = cv.VideoCapture(0)

capture = cv.VideoCapture(0)
def changeRes(capture, widht,height):
    capture.set(3,widht)
    capture.set(4,height)
    # 3 references the width and 4 refrences the height
    
    # The webcam hardware can only be opened by one process or pointer at a time.
# changeRes(capture, 320,240)
changeRes(capture, 1920,1080)
# this wont work because if the webcam can only record to 720 p then it doesnt matter if you chnage the resolution or not


while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("failed to grab the frame")
        break
    resized_frame = cv.resize(frame,(1280,720),interpolation=cv.INTER_AREA)
    cv.imshow("frame",frame)
    cv.imshow("resized",resized_frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break


capture.release()

cv.destroyWindow()
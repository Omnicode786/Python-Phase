import cv2 as cv

video = cv.VideoCapture('OPENCVPROJECTS\\videos\\Paper Background  Reels  Shorts  Edit Elements - Edit Elements (1080p, h264).mp4')
# this will read the video 

# now this will not actually read and show us the video in order to do that we need to use a while loop

while True:
    # we read a video frame by frame
    isTrue, frame = video.read()
    # it returns the frame and the boolean if ithe frame was succesfully read ornot
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


video.release()
cv.destroyAllWindows()

# if we get a cv2 -215 assertion error it simply measn that the cv2 wasnt able to find frames to the specfied path either from the very start or at somepoint

# we have to use a while loop to read the video frame by frame

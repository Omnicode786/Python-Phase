import cv2 as cv
import time
import mediapipe as mp

handsMP = mp.solutions.hands
hands = handsMP.Hands()
drawMP = mp.solutions.drawing_utils

cam = cv.VideoCapture(0)

currentTime = 0
PrevTime = 0

while True:
    isTrue,frame = cam.read()
    imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    currentTime = time.time()
    fps = 1/(currentTime-PrevTime)
    PrevTime = currentTime
    cv.putText(frame,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,255,255),2)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            drawMP.draw_landmarks(frame,handLandmarks, handsMP.HAND_CONNECTIONS)
    cv.imshow('Frame',frame)
    cv.waitKey(1)
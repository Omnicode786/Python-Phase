import cv2 as cv
import time
import mediapipe as mp

handsMP = mp.solutions.hands
hands = handsMP.Hands()
drawMP = mp.solutions.drawing_utils

LANDMARK_NAMES = {
    0: "WRIST",
    1: "THUMB_CMC",
    2: "THUMB_MCP",
    3: "THUMB_IP",
    4: "THUMB_TIP",
    5: "INDEX_MCP",
    6: "INDEX_PIP",
    7: "INDEX_DIP",
    8: "INDEX_TIP",
    9: "MIDDLE_MCP",
    10: "MIDDLE_PIP",
    11: "MIDDLE_DIP",
    12: "MIDDLE_TIP",
    13: "RING_MCP",
    14: "RING_PIP",
    15: "RING_DIP",
    16: "RING_TIP",
    17: "PINKY_MCP",
    18: "PINKY_PIP",
    19: "PINKY_DIP",
    20: "PINKY_TIP"
}

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
            for ind, lm in enumerate(handLandmarks.landmark):
                height,width , c = frame.shape
                cx, cy = int(lm.x*width),int(lm.y*height)
                if ind == 0:
                    # 0 is the wrist
                    cv.circle(frame,(cx,cy),25,(255,0,255),cv.FILLED)

                        # Draws a filled circle on 'frame'
                        # (cx, cy) -> center of the circle
                        # 25 -> radius in pixels
                        # (255, 0, 255) -> color in BGR format (purple here)
                        # cv.FILLED (or -1) -> fill the circle instead of just drawing the outline
                 # Draw a relatively big circle
                cv.circle(frame, (cx, cy), 12, (0, 255, 0), cv.FILLED)

                # Put index number and unique name above the circle
                text = f"{ind}:{LANDMARK_NAMES[ind]}"
                cv.putText(frame, text, (cx + 10, cy - 10),
                cv.FONT_HERSHEY_SIMPLEX, 0.32, (255, 0, 0), 2)


            drawMP.draw_landmarks(frame,handLandmarks, handsMP.HAND_CONNECTIONS)
    cv.imshow('Frame',frame)
    cv.waitKey(1)
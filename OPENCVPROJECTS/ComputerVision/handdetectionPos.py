import cv2 as cv
import time
import mediapipe as mp



class handDEtector():
    def __init__(self,mode=False,maxHands = 2, detectionCon = 0.5, trackCon = 0.5 ):
        self.mode  = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.handsMP = mp.solutions.hands
        self.hands = self.handsMP.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.drawMP = mp.solutions.drawing_utils
    
    def findHands(self,frame, draw = True):
         imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
         results = self.hands.process(imgRGB)

  
    
         if results.multi_hand_landmarks:
            for handLandmarks in results.multi_hand_landmarks:
                   if draw:  

                        self.drawMP.draw_landmarks(frame,handLandmarks, self.handsMP.HAND_CONNECTIONS)
         return frame 








def main():
    cam = cv.VideoCapture(2)
    PrevTime = 0
    currentTime = 0
    detector = handDEtector()
    while True:
         success,frame = cam.read()
         detector.findHands(frame)

    

    currentTime = time.time()
    fps = 1/(currentTime-PrevTime)
    PrevTime = currentTime
    cv.putText(frame,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,255,255),2)
    cv.imshow('Frame',frame)
    cv.waitKey(1)



if __name__ == "__main__":
    main()

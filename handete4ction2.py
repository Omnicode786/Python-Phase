import cv2
import mediapipe as mp
import requests
import time

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

ESP32_IP = "192.168.1.105"

cap = cv2.VideoCapture(0)
cap.set(3, 640)  
cap.set(4, 480) 

last_request_time = 0
request_interval = 1  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # if results.multi_hand_landmarks:
    #     print("Hand detected!")
        
    #     current_time = time.time()
    #     if current_time - last_request_time > request_interval:
    #         try:
    #             requests.get(f'http://{ESP32_IP}/on')
    #             last_request_time = current_time
    #         except:
    #             print("Failed to send request to ESP32")
    # else:
    #     print("No hand detected.")
        
    #     current_time = time.time()
    #     if current_time - last_request_time > request_interval:
    #         try:
    #             requests.get(f'http://{ESP32_IP}/off')
    #             last_request_time = current_time
    #             print("sent..")
    #         except:
    #             print("Failed to send request to ESP32")

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame with detections
    cv2.imshow("Hand Detection", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

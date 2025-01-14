import cv2
import mediapipe as mp
import requests
import time

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# ESP32 IP address
ESP32_IP = "192.168.1.102"

# Initialize webcam with lower resolution
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Throttle time (e.g., send request once every 1 second)
last_request_time = 0
request_interval = 1  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to RGB (required for MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Check if any hand is detected
    if results.multi_hand_landmarks:
        print("Hand detected!")
        
        # Throttle the HTTP requests to avoid overloading
        current_time = time.time()
        if current_time - last_request_time > request_interval:
            try:
                requests.get(f'http://{ESP32_IP}/on')
                last_request_time = current_time
            except:
                print("Failed to send request to ESP32")
    else:
        print("No hand detected.")
        
        # Throttle the HTTP requests to avoid overloading
        current_time = time.time()
        if current_time - last_request_time > request_interval:
            try:
                requests.get(f'http://{ESP32_IP}/off')
                last_request_time = current_time
            except:
                print("Failed to send request to ESP32")

    # Draw landmarks on the frame
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

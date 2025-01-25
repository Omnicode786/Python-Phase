import cv2
import mediapipe as mp
import requests
import time

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# ESP32 IP address
ESP32_IP = "192.168.1.105"

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Throttle time
last_request_time = 0
request_interval = 0.5  # seconds

def send_command(command):
    """Send a command to the ESP32 via HTTP."""
    global last_request_time
    current_time = time.time()
    if current_time - last_request_time > request_interval:
        try:
            requests.get(f'http://{ESP32_IP}/{command}')
            last_request_time = current_time
            print("sent")
        except:
            print(f"Failed to send {command} command to ESP32")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Gesture detection
            if thumb_tip.y < wrist.y and index_tip.y < wrist.y:
                print("Move Forward")
                send_command("forward")
            elif thumb_tip.y > wrist.y and index_tip.y > wrist.y:
                print("Move Backward")
                send_command("backward")
            elif thumb_tip.x < index_tip.x:
                print("Turn Left")
                send_command("left")
            elif thumb_tip.x > index_tip.x:
                print("Turn Right")
                send_command("right")
            else:
                print("Stop")
                send_command("stop")

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        send_command("stop")

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

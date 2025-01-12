import cv2
import requests

hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

ESP32_IP = "192.168.1.105"

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hands = hand_cascade.detectMultiScale(gray, 1.1, 4)

    if len(hands) > 0:
        print("Palm detected! Sending signal to turn LED ON.")
        try:
            requests.get(f'http://{ESP32_IP}/on')
        except:
            print("Failed to send request to ESP32")
    else:
        print("No palm detected. Sending signal to turn LED OFF.")
        try:
            requests.get(f'http://{ESP32_IP}/off')
        except:
            print("Failed to send request to ESP32")

    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Palm Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

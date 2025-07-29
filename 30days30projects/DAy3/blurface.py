import cv2

# Load pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Extract face region from original frame
        face_roi = frame[y:y+h, x:x+w]

        # Blur the face region
        face_roi = cv2.GaussianBlur(face_roi, (99, 99), 60)

        # Replace original face region with blurred version
        frame[y:y+h, x:x+w] = face_roi

    # Show the frame with blurred faces
    cv2.imshow('Face Blur', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

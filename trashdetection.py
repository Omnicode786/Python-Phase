import cv2
import numpy as np
import tensorflow as tf

# Load pre-trained model (e.g., SSD or YOLO with custom weights)
model_path = "path/to/your/model.tflite"  # Replace with your model file
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Labels (adjust based on your model's labels)
labels = {0: "Background", 1: "Paper", 2: "Glass", 3: "Metal"}

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Preprocess the frame for the model
    input_size = input_details[0]['shape'][1:3]  # Model's input size
    resized_frame = cv2.resize(frame, (input_size[1], input_size[0]))
    input_tensor = np.expand_dims(resized_frame, axis=0)
    input_tensor = input_tensor.astype(np.uint8)  # Model expects uint8 input

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_tensor)
    interpreter.invoke()

    # Get detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Bounding boxes
    classes = interpreter.get_tensor(output_details[1]['index'])[0]  # Class IDs
    scores = interpreter.get_tensor(output_details[2]['index'])[0]  # Confidence scores

    # Draw detections on the frame
    height, width, _ = frame.shape
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Confidence threshold
            class_id = int(classes[i])
            label = labels.get(class_id, "Unknown")
            box = boxes[i] * np.array([height, width, height, width])
            (ymin, xmin, ymax, xmax) = box.astype("int")

            # Draw bounding box and label
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Trash Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

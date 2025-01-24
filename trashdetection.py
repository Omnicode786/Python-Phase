import cv2
import numpy as np
import tensorflow as tf

model_path = "tensorflowlite\\model_unquant.tflite"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Output Details:", output_details)

labels = {0: "Paper", 1: "Metal"} 

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    input_size = input_details[0]['shape'][1:3] 
    resized_frame = cv2.resize(frame, (input_size[1], input_size[0]))

    input_tensor = np.expand_dims(resized_frame, axis=0)
    input_tensor = input_tensor.astype(np.float32) 
    input_tensor = input_tensor / 255.0  

    interpreter.set_tensor(input_details[0]['index'], input_tensor)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])[0]  
    
    class_id = np.argmax(output) 
    confidence = output[class_id]  

    # Draw the result on the frame
    label = labels.get(class_id, "Unknown")
    cv2.putText(frame, f"{label}: {confidence:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Trash Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

import cv2
from pyzbar.pyzbar import decode
import webbrowser

def scan_qr_code_and_open():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
    
    print("Point the camera at a QR code...")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read from the camera.")
            break
        
        # Decode the QR codes in the frame
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # Extract data from the QR code
            qr_data = obj.data.decode('utf-8')
            print(f"QR Code Detected: {qr_data}")
            
            # Check if it's a valid URL (simple check)
            if qr_data.startswith("http://") or qr_data.startswith("https://"):
                print(f"Opening URL: {qr_data}")
                webbrowser.open(qr_data)
                cap.release()  # Release the camera
                cv2.destroyAllWindows()  # Close all OpenCV windows
                return
        
        # Display the camera feed
        cv2.imshow("QR Code Scanner", frame)
        
        # Quit the program if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the QR code scanner
scan_qr_code_and_open()
print()
import cv2
from ultralytics import YOLO

image_path = "heavy-traffic.jpg"  
img = cv2.imread(image_path)

FOCAL_LENGTH = 700        #calcualte using ormual simply to calibrate it you need to have  a fixed focal length in order to do this or else because of multiple unknwos we cannot do this
# in simple words meri jan ke tote callibrate kr rhe hen Precieved widht (which comes from the box that we are going to be making but here we are assuming it first) * distance / real widht
# typicaly a car is down
KNOWN_WIDTH = 1.8     #average car is 1.8 m meri jan ke tote     
SAFE_TTC = 2.5           
#on average 2.5 seconds before brake is afe time befdore a collision

model = YOLO("yolov8n.pt")  
#model

def estimate_distance(perceived_width):
    return (KNOWN_WIDTH * FOCAL_LENGTH) / perceived_width
#this is why we need focal length to calculate the estimated distance actually from the cr


# once distance is knwon we can calculate the peed it should go
def calculate_recommended_speed(distance, safe_ttc=SAFE_TTC):
  
    return distance / safe_ttc 


results = model(img)[0]


for box in results.boxes:
    class_id = int(box.cls.item())
# for the cars as only
    confidence = box.conf.item()
# box for confidence
    if class_id == 2 and confidence > 0.5: 
        #  in the youlo id since we are only doing for cars so sertting like if its equalt o 2 in yolo it will return 2 if its a car so only draw boxes for thsoe and if the engine itself is 50% ormore confitdent that it is a car then only give the car 
        
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        perceived_width = x2 - x1
        distance = estimate_distance(perceived_width)
        rec_speed = calculate_recommended_speed(distance)
        rec_speed_kph = rec_speed * 3.6

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"Distance: {distance:.2f} m", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(img, f"Rec Speed: {rec_speed_kph:.1f} km/h", (x1, y2 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Distance and Recommended Speed", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
1
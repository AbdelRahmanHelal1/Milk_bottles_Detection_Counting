import cv2
import cvzone
import numpy as np
from  ultralytics import YOLO
import math

# Initialize YOLO model (make sure the model file path is correct)
model=YOLO(r"yolov8n.pt")
# Open video file (make sure the file path is correct)
cap=cv2.VideoCapture("Milk2.mp4")
#############################
# Initialize counter
counter=0
############################
# Dictionary for class labels
names={39:"bottles"}

# Main loop for object detection
while cap.isOpened():

    ret,frame=cap.read()
    if not ret:
        break

    frame =cv2.resize(frame,(800,500))

    # Draw line and counter on frame
    line=cv2.line(frame,(150,170),(150,280),(255,0,0),3)
    cv2.putText(frame, f"{counter}", (30,40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


    result=model(frame,stream=True)
    for i in result:
        boxes=i.boxes
        for box in boxes:
            x,y,w,z=box.xyxy[0]
            x,y,w,z=int(x),int(y),int(w),int(z)
            w=w-x
            h=z-y

            # X,Y of centroid circle
            cx=x+w//2
            cy=y+z//2

            cls=int(box.cls[0])
            conf=math.ceil(box.conf[0]*100)/100
            if cls in names:
              if names[cls] =="bottles":
                  # Draw the rectangle
                  cvzone.cornerRect(frame,(x,y,w,h))
                  # Draw  centroid circle
                  cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
                  if 148<cx<152:
                      counter+=1

    # Display frame
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) ==ord("q"):
       break
    frist=frame

cap.release()
cv2.destroyAllWindows()



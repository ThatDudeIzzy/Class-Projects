#Version 4 of a multi week adventure rabbithole into the abyss of computer vision and object detection.

from ultralytics import YOLO
import time
from pygame import mixer
import cv2

# x model is extremely accurate but slow
# n model is extremely fast but often inaccurate on non common objects

model = YOLO("yolov8n.pt")
mixer.init()

sound = mixer.Sound('C:/Users/Bleed/Desktop/DontDoIt.mp3')
sound.set_volume(0.7)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        Person = False
        Bottle = False
        results = model.predict(frame, conf=0.5)
        detections = results.xyxy[0]

        for detection in detections:
            class_id = int(detection[5])  # Check if class index is at 5!
            if class_id == 0:
                Person = True
            elif class_id == 39:
                Bottle = True

        annotated_frame = results.render()[0]
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        if Person and Bottle:
            sound.play()
            time.sleep(5)
            Person = False
            Bottle = False

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
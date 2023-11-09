#May need do !pip install ultralytics to make dis werky
#Simple version for testing/finding out how to not be dumb. (Going poorly)
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
        results = model.predict(source=frame, classes = (0,39), conf = 0.5)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Tracking", annotated_frame)
        # Trigger still doesn't work
        '''for result in results[0]:
            if model.predict.classes == 0:
                Person = True
            if model.predict.classes == 39:
                Bottle = True
                if Person == True and Bottle == True:
                    sound.play()
                    time.sleep(5)
                    Person = False
                    Bottle = False'''
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()







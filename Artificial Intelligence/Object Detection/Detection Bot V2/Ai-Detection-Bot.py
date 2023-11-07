#May need do !pip install ultralytics to make dis werky
#Simple version for testing/finding out how to not be dumb. (Going poorly)
from ultralytics import YOLO
import time
from pygame import mixer

model = YOLO("yolov8x.pt")

results = model.predict(source='0', classes = (0,39), conf = 0.6, show=True)
mixer.init()

sound = mixer.Sound('C:/Users/Bleed/Desktop/DontDoIt.mp3')
sound.set_volume(0.7)

last_played = 0

class_0_detected = False
class_39_detected = False

for class_id, conf in results.xyxy[0]:
    if class_id == 0 and conf > 0.6:
        class_0_detected = True
    elif class_id == 39 and conf > 0.6:
        class_39_detected = True

if class_0_detected and class_39_detected:
    print("DANGER!")
    sound.play()

if class_0_detected and class_39_detected:
    print("DANGER!")
    sound.play()


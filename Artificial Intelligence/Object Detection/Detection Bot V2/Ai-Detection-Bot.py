# May need do !pip install ultralytics to make dis werky
# Simple version for testing/finding out how to not be dumb. (Going poorly)
# If cv2 breaks do !pip uninstall opencv-python-headless then full !pip install opencv-python (Guess who just saved you 2 hours of googling)

# Currently 1AM and I'm tired so I'm going to bed......  
# One of these days this print will trigger when class_id 0 and 39 are detected simultaneously.
# When that happens the possbilities sky rocket. Until then... I'm just a caveman banging rocks together. Goodnight.


from ultralytics import YOLO
import time
from pygame import mixer

model = YOLO("yolov8x.pt")
mixer.init()

sound = mixer.Sound('C:/Users/Bleed/Desktop/DontDoIt.mp3')
sound.set_volume(0.7)

last_played = 0

while True:
    results = model.predict(source='0', classes = (0,39), conf = 0.6, show=False)
    if results.xyxy[0] == 0 and results.xyxy[0] == 39:
        print("Dont do it")





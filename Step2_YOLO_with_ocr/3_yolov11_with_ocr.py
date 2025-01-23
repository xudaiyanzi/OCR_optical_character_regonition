from ultralytics import YOLO
import os

# load the trained model
model = YOLO(os.path.join('.','models','best.pt'))

# load the image
img_path = os.path.join('.','datasets','digital_clock_data','validation','data','9c5e87b8b0402568.jpg')

# detect the object
results = model(img_path, save=True, show=True)
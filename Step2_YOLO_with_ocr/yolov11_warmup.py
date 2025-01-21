from ultralytics import YOLO
import os

# load model - create the new model instance with the pre-trained weights YOLO v11
model = YOLO('yolo11n.pt')

# # this only use once to download the pre-trained weights
# # once it is downloaded, you can comment it out
# # train the model - use the coco8.yaml file to train the model for 100 epochs
# model.train(data='coco8.yaml', epochs=100, imgsz=640)

# prediction - now the model is trained, we can use it to make predictions
results = model(os.path.join('..', 'data', 'street_name.jpg'), save=True, show=True)


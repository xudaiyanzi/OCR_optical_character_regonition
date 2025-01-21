As the YOLO development community continues its work, newer YOLO models are consistently being released. Here, we use YOLO v11, which is the lastest version of YOLO (released in Sep, 2024).

To run the model, follow the instruction from [ultralytics](https://github.com/ultralytics/ultralytics) to install the ultralytics in your VM.

```
python -m pip install ultralytics
```

- YOLO v11 has the weights and configuration from previous training based on more than thousand images
- We want to use it to predict our streat_name.
- Due to the nature of training, YOLOv11 can not predict the text but only the object from the image
- it is ok in our situation, what we need to combine this object detection capbility with another ocr model to predict text from image

As noted in the main page README, a dedicated repository will focus solely on object detection (OD).

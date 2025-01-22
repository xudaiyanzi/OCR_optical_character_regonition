## Step2: Read text from images using YOLO and OCR

As the YOLO development community continues its work, newer YOLO models are consistently being released. Here, we use YOLO v11, which is the lastest version of YOLO (released in Sep, 2024).

To run the model, follow the instruction from [ultralytics](https://github.com/ultralytics/ultralytics) to install the ultralytics in your VM.

```
python -m pip install ultralytics
```

- YOLO v11 has the weights and configuration from previous training based on more than thousand images
- Due to the nature of training, YOLOv11 can not predict the text but only the object from the image
- We need to combine this object detection capbility with another ocr model to predict text from image

Here are two script: one is "yolov11_warmup.py", which is an [example script ](https://www.ultralytics.com/blog/using-ultralytics-yolo11-for-automatic-number-plate-recognition)adapted from Utralytics website; another one is "yolov11_with_ocr.py" which combines the OD model with OCR model, to help read the text from an image.

As noted in the main page README, a dedicated repository will focus solely on object detection (OD).

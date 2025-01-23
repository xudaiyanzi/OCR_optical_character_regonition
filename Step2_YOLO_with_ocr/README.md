## Step2: Read text from images using YOLO and OCR

As the YOLO development community continues its work, newer YOLO models are consistently being released. Here, we use YOLO v11, which is the lastest version of YOLO (released in Sep, 2024).

To run the model, follow the instruction from [ultralytics](https://github.com/ultralytics/ultralytics) to install the ultralytics in your VM.

```
python -m pip install ultralytics
```

- YOLO v11 has the weights and configuration from previous training based on more than thousand images
- Due to the nature of training, YOLOv11 can not predict the text but only the object from the image
- We need to combine this object detection capbility with another ocr model to predict text from image

This step includes three sections:

1. "1_yolov11_warmup.py", which is an [example script ](https://www.ultralytics.com/blog/using-ultralytics-yolo11-for-automatic-number-plate-recognition)adapted from Utralytics website, helping beginer to understand how yolov11 detect the object from an image
2. "2_yolov11_train_customized_data.py", which teaches developer to train any desired dataset with YOLO method
   * download images are from [Open Image Data](https://storage.googleapis.com/openimages/web/download_v7.html) using [Fifty-one dataset zoo](https://docs.voxel51.com/tutorials/open_images.html)
     * The data we will use is "digital clock", which has been labeled
     * In the next YOLO project, I will give more detailed method to annotated the images for training and validating purpose
     * follow [Fifty-one documentation](https://github.com/voxel51/fiftyone) to install in VM and then download the open image data with 51
   * train the YOLOv11 model the annotated data with free cloud GPU - [google colab](https://research.google.com/colaboratory/faq.html#:~:text=Colab%20is%20a%20hosted%20Jupyter,%2C%20data%20science%2C%20and%20education.)
     * In the training.ipynb in google colab, download the data from roboflow

       ```
       !pip install roboflowfrom roboflow 

       import Roboflow

       rf = Roboflow(api_key=<YOUR API KEY>)
       project = rf.workspace("research-8rrcu").project("odo-frrwd")
       version = project.version(1)
       dataset = version.download("yolov11")
       ```
     * when the training is done, download the "best.pt" file from google colab into this directory
     * use the downloaded pt file to do inference with test dataset
3. "3_yolov11_with_ocr.py" which combines the OD model with OCR model, to help read the text from an image

As noted in the main page README, a dedicated repository will focus solely on object detection (OD).

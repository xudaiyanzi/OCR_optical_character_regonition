import fiftyone as fo
import fiftyone.zoo as foz
import os

##########################################################################################
## Load and export dataset, just use once to download the dataset
# # Specify dataset details
# dataset_name = "open-images-v7"
# classes = ["Digital clock"]  # Replace with your desired class
# export_dir = os.path.join('.', 'datasets', 'digital_clock_data')  # Base directory to export datasets

# # Ensure the export directory exists
# os.makedirs(export_dir, exist_ok=True)

# # Function to load and export dataset
# def load_and_export(split, export_subdir):
#     # Load the dataset split
#     dataset = foz.load_zoo_dataset(
#         dataset_name,
#         split=split,  # Options: "train", "validation", "test"
#         label_types=["detections"],
#         classes=classes,
#         max_samples=200,  # Optional: Adjust based on your needs
#     )
    
#     # Create a subdirectory for the split
#     split_export_dir = os.path.join(export_dir, export_subdir)
#     os.makedirs(split_export_dir, exist_ok=True)
    
#     # Export the dataset in Open Images format
#     dataset.export(
#         export_dir=split_export_dir,
#         dataset_type=fo.types.FiftyOneDataset,  # Export format for Open Images
#         label_field="ground_truth",  # Use the appropriate label field
#     )
#     print(f"{split.capitalize()} dataset exported to {split_export_dir}")

# # Load and export train, validation, and test datasets
# load_and_export("train", "train")
# load_and_export("validation", "validation")
# load_and_export("test", "test")
##########################################################################################

## we can also use google colab to download the dataset and train the model with yolov11 and roboflow
## the code is in the file "digital_roboflow_yolov11.ipynb"






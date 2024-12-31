import os
import json
from pathlib import Path

# Paths
DATA_DIR = "data"
IMAGES_DIR = os.path.join(DATA_DIR, "probe_images")
OUTPUT_LABELS_DIR = os.path.join(DATA_DIR, "labels")

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_LABELS_DIR, exist_ok=True)

# Load the JSON file
json_file = os.path.join(DATA_DIR, "probe_labels.json")
with open(json_file, "r") as f:
    data = json.load(f)

# Mapping of image_id to file_name, width, height
image_info = {img["id"]: img for img in data["images"]}

# Process each annotation
for annotation in data["annotations"]:
    # Get bounding box and associated image_id
    bbox = annotation["bbox"]  # [x_min, y_min, width, height]
    image_id = annotation["image_id"]

    # Get image details
    image = image_info.get(image_id)
    if not image:
        continue

    file_name = image["file_name"]
    img_width = image["width"]
    img_height = image["height"]

    # Convert bbox to YOLO format
    x_min, y_min, width, height = bbox
    x_center = (x_min + width / 2) / img_width
    y_center = (y_min + height / 2) / img_height
    width_norm = width / img_width
    height_norm = height / img_height

    # YOLO annotation string
    yolo_annotation = f"0 {x_center:.6f} {y_center:.6f} {width_norm:.6f} {height_norm:.6f}"

    # Save annotation to corresponding text file
    label_file = os.path.join(OUTPUT_LABELS_DIR, Path(file_name).stem + ".txt")
    with open(label_file, "a") as f:
        f.write(yolo_annotation + "\n")

print(f"YOLO labels saved to: {OUTPUT_LABELS_DIR}")

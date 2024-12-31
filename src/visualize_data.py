import json
import cv2
import os

# Paths
data_dir = "data/probe_images/"
labels_path = "data/probe_labels.json"

# Load Annotations
with open(labels_path, "r") as f:
    data = json.load(f)

annotations = data["annotations"]
images = {img["id"]: img["file_name"] for img in data["images"]}

# Visualize Bounding Boxes
for annotation in annotations:
    image_id = annotation["image_id"]
    bbox = annotation["bbox"]  # [x_min, y_min, width, height]
    img_path = os.path.join(data_dir, images[image_id])

    # Load image
    img = cv2.imread(img_path)
    x_min, y_min, w, h = map(int, bbox)
    x_max, y_max = x_min + w, y_min + h

    # Draw bounding box
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Show image
    cv2.imshow("Image with Bounding Box", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

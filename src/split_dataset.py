import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
DATA_DIR = "data"
IMAGES_DIR = r"C:\Users\etudiant\Desktop\Deep Learning\data\probe_images"
LABELS_DIR = r"C:\Users\etudiant\Desktop\Deep Learning\data\labels"


# Output folders for train, val, test splits
OUTPUT_DIR = os.path.join(DATA_DIR, "splits")
TRAIN_IMG_DIR = os.path.join(OUTPUT_DIR, "images/train")
VAL_IMG_DIR = os.path.join(OUTPUT_DIR, "images/val")
TEST_IMG_DIR = os.path.join(OUTPUT_DIR, "images/test")

TRAIN_LABEL_DIR = os.path.join(OUTPUT_DIR, "labels/train")
VAL_LABEL_DIR = os.path.join(OUTPUT_DIR, "labels/val")
TEST_LABEL_DIR = os.path.join(OUTPUT_DIR, "labels/test")

# Create directories
for folder in [TRAIN_IMG_DIR, VAL_IMG_DIR, TEST_IMG_DIR, TRAIN_LABEL_DIR, VAL_LABEL_DIR, TEST_LABEL_DIR]:
    os.makedirs(folder, exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".jpg")]

# Split data into train, val, and test (80%, 10%, 10%)
train_files, temp_files = train_test_split(image_files, test_size=0.2, random_state=42)
val_files, test_files = train_test_split(temp_files, test_size=0.5, random_state=42)

# Function to copy images and corresponding labels
def copy_files(file_list, src_img_dir, src_label_dir, dest_img_dir, dest_label_dir):
    for file_name in file_list:
        # Copy image
        src_img_path = os.path.join(src_img_dir, file_name)
        dest_img_path = os.path.join(dest_img_dir, file_name)
        shutil.copy(src_img_path, dest_img_path)

        # Copy corresponding label file
        label_file_name = os.path.splitext(file_name)[0] + ".txt"
        src_label_path = os.path.join(src_label_dir, label_file_name)
        dest_label_path = os.path.join(dest_label_dir, label_file_name)

        if os.path.exists(src_label_path):  # Ensure label exists
            shutil.copy(src_label_path, dest_label_path)

# Copy files into respective folders
copy_files(train_files, IMAGES_DIR, LABELS_DIR, TRAIN_IMG_DIR, TRAIN_LABEL_DIR)
copy_files(val_files, IMAGES_DIR, LABELS_DIR, VAL_IMG_DIR, VAL_LABEL_DIR)
copy_files(test_files, IMAGES_DIR, LABELS_DIR, TEST_IMG_DIR, TEST_LABEL_DIR)

print("Data split completed!")
print(f"Train: {len(train_files)} images")
print(f"Validation: {len(val_files)} images")
print(f"Test: {len(test_files)} images")

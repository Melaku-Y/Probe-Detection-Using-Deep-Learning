import json

# Path to JSON file
labels_path = "data/probe_labels.json"

# Open and load the JSON
with open(labels_path, "r") as f:
    data = json.load(f)

# Print structure
print("Annotations:")
for annotation in data["annotations"][:3]:  # Print first 5 annotations
    print(annotation)

print("\nImages:")
for image in data["images"][:3]:  # Print first 5 images
    print(image)

# Probe Detection Using YOLOv5

## Introduction

This project focuses on using the YOLOv5 deep learning framework for detecting ultrasonic thickness measurement probes in images captured by the Elios3 drone. The system outputs bounding boxes around detected probes or notifies when no probe is present.

### Tools and Technologies

- **Framework**: YOLOv5 (PyTorch)
- **Programming Language**: Python
- **Development Environment**: Anaconda, Visual Studio Code
- **Version Control**: Git

---

## System Selection and Setup

### Selected System

**YOLOv5** was selected due to its efficiency, speed, and real-time object detection capabilities. It supports pre-trained weights, transfer learning, and modular design, making it ideal for the specific task. Additionally, YOLOv5's compatibility with IoT devices like NVIDIA Jetson boards ensures deployment feasibility.

---

## Training and Fine-Tuning

### Dataset

- **Images**: 308 total, annotated with bounding boxes.
- **Splits**: Training (80%), Validation (10%), Test (10%).
- **Preprocessing**: JSON annotations were converted to YOLO format, and data subsets were split programmatically.

### Training Configuration

- **Model**: YOLOv5s (small version)
- **Pre-trained Weights**: yolov5s.pt
- **Batch Size**: 16
- **Image Size**: 640x640
- **Epochs**: 50

---

## Evaluation



Below are examples of detected and undetected probes during the evaluation process:

![No Detection](https://github.com/Melaku-Y/Probe-Detection-Using-Deep-Learning/blob/main/results/detect/exp_detect/EL300858804493_00193_048_1flight_1500_0.jpg)

*Example of no detection from the dataset.*

![Detection](https://github.com/Melaku-Y/Probe-Detection-Using-Deep-Learning/blob/main/results/detect/exp_detect/E300PREMP00002_00725_216_1flight_1500_2.jpg)

*Example of a successful probe detection with a confidence score of 0.93.*

### Detail results are discussed in the paper [Prob Detection Report](https://github.com/Melaku-Y/Probe-Detection-Using-Deep-Learning/blob/main/Prob%20Detection%20Report.pdf)


---

## Usage Instructions

If you want to see results and conclusions, feel free to explore the folders. If you want to try them on your machine, follow these steps:

### Clone YOLOv5 to Your Working Folder

```bash
git clone https://github.com/ultralytics/yolov5.git
```

### Step 1: Create an Anaconda Environment for YOLOv5

1. Open the Anaconda Prompt.
2. Create a new environment (if not already created):
   ```bash
   conda create -n yolov5 python=3.8 -y
   ```
3. Activate the environment:
   ```bash
   conda activate yolov5
   ```

If you want to use Visual Studio Code, make sure you have the latest Python installed and activate the virtual environment.

### Step 2: Install YOLOv5 Requirements

1. Navigate to your YOLOv5 folder:
   ```bash
   cd path/to/yolov5
   ```
2. Install the required dependencies using this command:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Verify YOLOv5 Setup

Run a quick test to confirm YOLOv5 is set up:

```bash
python detect.py --source data/images --weights yolov5s.pt --conf 0.5
```

### Step 4: Train, Validate, Test, and Detect

Ensure the paths for saving results and navigating `train.py`, `val.py`, `detect.py`, and `probe_detection.yaml` are correct.

#### Train Command

```bash
python yolov5/train.py --data src/probe_detection.yaml --cfg yolov5s.yaml --weights yolov5s.pt --epochs 50 --batch-size 16 --project results/train --name exp
```

#### Validation Command

```bash
python yolov5/val.py --weights results/train/exp/weights/best.pt --data src/probe_detection.yaml --batch-size 16 --imgsz 640 --project results/val --name exp_val --save-txt --save-conf
```

#### Test Command

```bash
python yolov5/val.py --weights results/train/exp/weights/best.pt --data src/probe_detection.yaml --task test --batch-size 16 --imgsz 640 --project results/test --name exp_test --save-txt --save-conf
```

#### Detect Command

```bash
python yolov5/detect.py --weights results/train/exp/weights/best.pt --source data/splits/images/test --save-crop --project results/test --name exp_detect
```

Thank you!


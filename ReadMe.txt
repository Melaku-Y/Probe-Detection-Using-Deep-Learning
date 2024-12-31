If you want to see results and conclusions feel free to explore the folders or if you want to try them in your machine follow these steps.
Clon YOLOv5 to your working folder 

git clone https://github.com/ultralytics/yolov5.git


Step 1: Create an Anaconda Environment for YOLOv5

	 1. Open the Anaconda Prompt.
	 2. Create a new environment (if not already created)
		  conda create -n yolov5 python=3.8 -y

     3. Activate the environment:

           conda activate yolov5
		   
If you want to use Vs code make sure you installed the latest Python and activate virtual environment.

Step 2: Install YOLOv5 Requirements
	1. Navigate to your YOLOv5 folder:
		cd path/to/yolov5

    2. Install the required dependencies using this command

		pip install -r requirements.txt

Step 3: Verify YOLOv5 Setup
	Run a quick test to confirm YOLOv5 is set up:
	
	python detect.py --source data/images --weights yolov5s.pt --conf 0.5
	
Step 4: Train, validate, test, and detect using the following commands

Ensure the path you want to save the results and correctly navigate train.py, val.py, detect.py, and probe_detection.yaml.


Train Command

python yolov5/train.py --data src/probe_detection.yaml --cfg yolov5s.yaml --weights yolov5s.pt --epochs 50 --batch-size 16 --project results/train --name exp

Validation Command

python yolov5/val.py --weights results/train/exp/weights/best.pt --data src/probe_detection.yaml --batch-size 16 --imgsz 640 --project results/val --name exp_val --save-txt --save-conf

Test Command 

python yolov5/val.py --weights results/train/exp/weights/best.pt --data src/probe_detection.yaml --task test --batch-size 16 --imgsz 640 --project results/test --name exp_test --save-txt --save-conf

Detect Command

python yolov5/detect.py --weights results/train/exp/weights/best.pt --source data/splits/images/test --save-crop --project results/test --name exp_detect

Thank you!







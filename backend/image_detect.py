from pathlib import Path
import cv2
from ultralytics import YOLO

# project root
project_root = Path(__file__).resolve().parents[1]

# paths
model_path = r"D:\Model Demo\models\YOLOv8_Small_RDD.pt"
image_path = r"D:\Model Demo\demo_media\pathole2.jpg"
output_path = r"D:\Model Demo\uploads\pathole2_annotated.jpg"

# load model
model = YOLO(model_path)

# load image
img = cv2.imread(image_path)

if img is None:
    raise Exception("Image not loaded")

# run detection (important parameters)
results = model.predict(
    source=img,
    conf=0.25,   # lower confidence threshold
    imgsz=640
)

# annotated image
annotated = results[0].plot()

# try displaying
try:

    cv2.imshow("RoadGuardian AI Image Detection", annotated)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

except:

    cv2.imwrite(output_path, annotated)

    print("Saved annotated image:", output_path)
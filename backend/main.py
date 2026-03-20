from pathlib import Path

import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from ultralytics import YOLO

app = FastAPI()

project_root = Path(__file__).resolve().parents[1]
model_path = project_root / "models" / "YOLOv8_Small_RDD.pt"

if not model_path.exists():
    raise FileNotFoundError(f"Model file not found: {model_path}")

model = YOLO(str(model_path))

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload a valid image file.")

    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    nparr = np.frombuffer(image_bytes, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Unable to decode image data.")

    try:
        results = model(img)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Model inference failed: {exc}") from exc

    detections = []

    for r in results:

        for box in r.boxes:

            conf = float(box.conf.item())
            cls = int(box.cls.item())

            # bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            width = x2 - x1
            height = y2 - y1

            area = width * height

            # severity logic
            if area > 20000:
                severity = "High"
                priority = "Urgent Repair"
            elif area > 8000:
                severity = "Medium"
                priority = "Scheduled Repair"
            else:
                severity = "Low"
                priority = "Monitor"

            detections.append({
                "class": cls,
                "label": model.names.get(cls, str(cls)),
                "confidence": conf,
                "severity": severity,
                "priority": priority
            })

    return {
        "detections": detections
    }
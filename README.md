# 🚧 RoadGuardian AI – Demo Prototype

RoadGuardian AI is a computer vision–based demo system built for detecting road damage (especially potholes) using YOLOv8.

This repository represents a **separate experimental/demo model implementation**, created specifically for testing, validation, and showcasing core AI capabilities before integrating into a full-scale production system.

---

## 🎯 Project Purpose

This demo was developed as a **proof-of-concept** to:

* Validate road damage detection using YOLOv8
* Test real-time and image-based inference pipelines
* Simulate how AI can assist in smart road monitoring systems
* Serve as a base model for future integration into a larger platform (NRIP)

> ⚠️ Note: This is not the final production system. It is an isolated demo model built for experimentation and testing.

---

## 🧠 Core Capabilities

* 🚀 YOLOv8-based pothole detection model
* 🖼️ Image inference via FastAPI (`/predict` endpoint)
* 🎥 Real-time detection using webcam and video (OpenCV)
* 📊 Severity classification based on bounding box size
* 🗺️ Basic map visualization using Leaflet

---

## 🧩 Project Structure

```text
backend/
  image_detect.py
  main.py
  new.py
  video_detect.py
  webcam_detect.py

frontend/
  index.html

models/
  YOLOv8_Small_RDD.pt

demo_media/
```

---

## ⚙️ Tech Stack

* **Language:** Python 3.x
* **Backend:** FastAPI
* **AI Model:** Ultralytics YOLOv8
* **Computer Vision:** OpenCV
* **Numerical Processing:** NumPy
* **Frontend Map:** Leaflet.js

---

## ⚡ Features Explained

### 🔍 Detection System

The model detects potholes and road damage using YOLOv8 and returns structured output including class, confidence, and bounding box.

### 📊 Severity Classification Logic

Severity is determined based on detected object size:

* **High → Urgent Repair**
* **Medium → Scheduled Repair**
* **Low → Monitor**

This helps simulate real-world prioritization of road repairs.

### 🌐 API Support

FastAPI backend provides a `/predict` endpoint for image-based inference.

### 🎥 Real-Time Processing

* Webcam detection
* Video file detection

---

## 🛠️ Setup Instructions

### 1️⃣ Create Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2️⃣ Install Dependencies

```powershell
pip install fastapi uvicorn ultralytics opencv-python numpy python-multipart
```

---

## 🚀 Running the API

```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Open API docs:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Usage

### POST `/predict`

Upload an image using multipart form-data (`file` field).

```powershell
curl.exe -X POST "http://127.0.0.1:8000/predict" ^
  -H "accept: application/json" ^
  -H "Content-Type: multipart/form-data" ^
  -F "file=@demo_media/pathole2.jpg"
```

### 🔁 Response Includes

* `class`
* `label`
* `confidence`
* `severity`
* `priority`

---

## 🎬 Running Detection Scripts

### Image Detection

```powershell
python backend/image_detect.py
```

### Video Detection

```powershell
python backend/video_detect.py
```

### Webcam Detection

```powershell
python backend/webcam_detect.py
```

---

## ⚠️ Notes & Improvements

* Replace absolute paths with relative paths using `pathlib`
* Add `requirements.txt` for easier setup
* Improve model accuracy with larger datasets
* Integrate GPS tagging for real-world deployment
* Expand dashboard with analytics and reporting

---

## 👨‍💻 Author

Mandeep Kumar

---

## ⭐ Final Note

This repository is intentionally structured as a **demo model project** to showcase AI capabilities independently before scaling into a production-grade intelligent infrastructure system.

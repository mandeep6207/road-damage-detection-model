# RoadGuardian AI Demo Model

RoadGuardian AI is a computer-vision project for road damage detection using YOLOv8.
It supports image inference through a FastAPI backend, real-time webcam/video detection with OpenCV, and a simple map view for pothole location display.

## Suggested Project Name

RoadGuardian AI is the strongest name for this project because it is:
- Clear about domain: road safety and monitoring
- Product-like and memorable
- Already aligned with existing script window titles

Alternative: RoadDamage Vision AI

## Project Structure

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

## Features

- YOLOv8 road damage (pothole) detection
- FastAPI endpoint for image prediction: `/predict`
- Severity tagging from detected box area:
  - High -> Urgent Repair
  - Medium -> Scheduled Repair
  - Low -> Monitor
- OpenCV real-time webcam and video inference scripts
- Basic Leaflet map for detected location display

## Tech Stack

- Python 3.x
- FastAPI
- Ultralytics YOLOv8
- OpenCV
- NumPy
- Leaflet (frontend map)

## Setup

1. Create and activate virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install fastapi uvicorn ultralytics opencv-python numpy python-multipart
```

## Run The API

From project root:

```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Open docs at:

- http://127.0.0.1:8000/docs

## API Usage

### POST /predict

Upload an image file using multipart form-data (`file` field).

Example with PowerShell:

```powershell
curl.exe -X POST "http://127.0.0.1:8000/predict" ^
  -H "accept: application/json" ^
  -H "Content-Type: multipart/form-data" ^
  -F "file=@demo_media/pathole2.jpg"
```

Response includes detections with:
- `class`
- `label`
- `confidence`
- `severity`
- `priority`

## Run Detection Scripts

Image detection:

```powershell
python backend/image_detect.py
```

Video detection:

```powershell
python backend/video_detect.py
```

Webcam detection:

```powershell
python backend/webcam_detect.py
```

## Frontend Map

Open the file directly in a browser:

```text
frontend/index.html
```

## Notes And Improvements

- Some backend scripts currently use absolute Windows paths. For portability, convert to relative paths using `pathlib`.
- Keep model file at `models/YOLOv8_Small_RDD.pt`.
- Consider adding a `requirements.txt` and test cases for API validation.


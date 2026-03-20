from ultralytics import YOLO
import cv2
import winsound

# -----------------------------
# Load Model
# -----------------------------
model = YOLO(r"D:\Model Demo\models\YOLOv8_Small_RDD.pt")

# -----------------------------
# Load Video
# -----------------------------
cap = cv2.VideoCapture(r"D:\Model Demo\demo_media\road_video.mp4")

alert_played = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Run Detection
    # -----------------------------
    results = model(frame)[0]

    alert = False

    for box in results.boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf)

        width = x2 - x1
        height = y2 - y1
        area = width * height

        # -----------------------------
        # Severity Calculation
        # -----------------------------
        if area < 4000:
            severity = "LOW"
            color = (0,255,255)

        elif area < 15000:
            severity = "MEDIUM"
            color = (0,165,255)

        else:
            severity = "HIGH"
            color = (0,0,255)

        # -----------------------------
        # Draw Bounding Box
        # -----------------------------
        cv2.rectangle(frame,(x1,y1),(x2,y2),color,3)

        label = f"Pothole {severity} {conf:.2f}"

        cv2.putText(frame,
                    label,
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2)

        alert = True

    # -----------------------------
    # ALERT SYSTEM
    # -----------------------------
    if alert:

        cv2.rectangle(frame,(0,0),(frame.shape[1],60),(0,0,255),-1)

        cv2.putText(frame,
                    "ALERT : POTHOLE DETECTED",
                    (30,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,255,255),
                    3)

        if not alert_played:
            winsound.Beep(1800,500)
            alert_played = True

    else:
        alert_played = False

    # -----------------------------
    # Show Video (Camera Style)
    # -----------------------------
    cv2.imshow("RoadGuardian AI Video Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

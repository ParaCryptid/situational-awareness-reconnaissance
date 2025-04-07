
import cv2
import os
import datetime

RECORD_DIR = "/opt/training-system/logs/surveillance"

def record_video():
    os.makedirs(RECORD_DIR, exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[OpenCV] Camera not found.")
        return

    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".avi"
    out_path = os.path.join(RECORD_DIR, filename)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, 20.0, (640, 480))

    print(f"[OpenCV] Recording started: {out_path}")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Recording - Press Q to Stop', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

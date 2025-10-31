import cv2
import time
from ultralytics import YOLO
import numpy as np


def main(args=None):
    # Initialize YOLO model
    PT_MODEL = "yolov11n.pt"
    model = YOLO(PT_MODEL)
   
    # Start video capture stream
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: unable to open camera")
        return

    while True:
        # Capture video frame
        ret, frame = cap.read()
        if not ret:
            break

        # Inference from captured frame
        start = time.time()
        results = model(frame)  
        end = time.time()
        annotated_frame = results[0].plot()

        # Print FPS on frame
        fps = 1 / (end - start)
        cv2.putText(annotated_frame,
                     f"FPS: {fps:.1f}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        # Show annotated frame captured from cideo
        cv2.imshow("YOLOv11 Desktop Demo", annotated_frame)
        
        # Stop program on key press: ESC
        if cv2.waitKey(1) == 27: 
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
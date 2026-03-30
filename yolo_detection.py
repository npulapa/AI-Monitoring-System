from ultralytics import YOLO
import cv2

def main():
    # Load YOLOv8 model (downloads automatically first time)
    model = YOLO("yolov8n.pt")

    # Start webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    print("Press 'q' to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection
        results = model(frame)

        # Get annotated frame
        annotated_frame = results[0].plot()

        # Count number of persons
        person_count = 0
        for box in results[0].boxes:
            cls = int(box.cls[0])
            if model.names[cls] == "person":
                person_count += 1

        # Display person count
        cv2.putText(annotated_frame,
                    f"People Count: {person_count}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)

        # Show output
        cv2.imshow("YOLOv8 Object Detection", annotated_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

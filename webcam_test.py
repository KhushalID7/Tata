import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Webcam Test", frame)
    if cv2.waitKey(1) in [27, ord('q')]:  # ESC or q
        break

cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarCascade\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("haarCascade\eye.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_frame = frame[y: y + h, x: x + w]
        roi_gray = gray[y: y + h, x: x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        for (a, b, c, d) in eyes:
            cv2.rectangle(roi_frame, (a, b), (a + c, b + d), (0, 255, 0), 1)

    cv2.imshow("webcam", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

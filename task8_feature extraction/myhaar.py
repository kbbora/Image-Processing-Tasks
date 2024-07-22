import cv2

cap = cv2.VideoCapture(0)
my_cascade= cv2.CascadeClassifier("haarCascade\myhaar.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    my = my_cascade.detectMultiScale(gray,1.2,4)

    for (x, y, w, h) in my:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255,0,0), 3)

    cv2.imshow("webcam", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
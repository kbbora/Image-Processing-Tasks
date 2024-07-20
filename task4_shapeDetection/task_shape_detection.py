import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype="uint8") + 255

# Geometrik şekillerin çizimi
cv2.rectangle(canvas, (40, 100), (150, 250), (255, 255, 0), thickness=-1)
cv2.rectangle(canvas, (500, 500), (400, 400), (155, 155, 0), thickness=-1)
cv2.circle(canvas, (400, 100), 70, (255, 0, 255), thickness=-1)

points = np.array([[256, 150], [156, 400], [356, 400]])
cv2.fillPoly(canvas, [points], (0, 0, 0))

cv2.imshow("Before", canvas)

gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

# Kenarları bulmak için kenar algılama
edges = cv2.Canny(gray, 50, 150)

# Konturları bulma
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tanımlama ve sınıflandırma
for contour in contours:
    # Kontur alanı çok küçükse yoksaymak için
    if cv2.contourArea(contour) < 100:
        continue

    # Konturu çevreleyen min. dikdörtgen
    x, y, w, h = cv2.boundingRect(contour)

    # Konturu çevreleyen approx çokgen
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"
    elif len(approx) > 4:
        shape = "Circle"

    # Şekli ve sınıfını çizdirmek
    cv2.putText(canvas, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.drawContours(canvas, [contour], -1, (0, 0, 255), 2)

cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

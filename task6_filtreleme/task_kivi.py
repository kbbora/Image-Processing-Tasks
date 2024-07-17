import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\kivi.jpeg")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_mask = np.array([25, 55, 0])
upper_mask = np.array([45, 255, 255])

mask = cv2.inRange(img_hsv, lower_mask, upper_mask)
source = cv2.bitwise_and(img, img, mask=mask)  # belirtilen renk aralığındaki pikselleri aldık.

gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
blur = cv2.medianBlur(thresh, 29)

kernel = np.ones((19, 15), np.uint8)
kernel2 = np.ones((21, 17), np.uint8)

erosion = cv2.erode(blur, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel2, iterations=1)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Before')

plt.subplot(1, 2, 2)
plt.imshow(dilation, cmap='gray')
plt.title('After')

plt.show()

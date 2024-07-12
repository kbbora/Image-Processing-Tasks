import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\birds.jpg", 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

cv2.imshow("Image", img)

plt.plot(hist)
plt.title('Histogram Hesaplama')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

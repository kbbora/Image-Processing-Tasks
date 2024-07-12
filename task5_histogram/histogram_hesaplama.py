import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\birds.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Gray Image')

plt.subplot(1, 2, 2)
plt.plot(hist)
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')

plt.show()

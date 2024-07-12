import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\hist_equ.jpg", 0)

equ = cv2.equalizeHist(img)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')

plt.show()

import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\birds.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

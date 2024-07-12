import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\birds.jpg")

cv2.imshow("Image", img)

plt.hist(img.ravel(), 256, [0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

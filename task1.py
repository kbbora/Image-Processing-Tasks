import cv2
import numpy as np


image_path = 'gulresmi.jpeg'
image = cv2.imread(image_path)

# görseli rgb ye çevirdim
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# gülün tespiti için hsv renk uzayına dönüşüm
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# kırmızı rengin aralıkları
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)

# maske birleştirme
mask = mask1 | mask2

# arkaplan
image_rgb[mask == 0] = [0, 0, 0]


image_hsv[mask > 0, 0] = 140  # Hue değerini 140 yaparak mavi-mor arası bir renk elde edilir
image_morphed = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

# maske ile orijinal görseli birleştirme
final_image = np.where(mask[:, :, None] > 0, image_morphed, 0)


original_image_path = 'gulresmi.jpeg'
original_image = cv2.imread(original_image_path)


morphed_image_path = 'morphed_rose.jpeg'
morphed_image = cv2.imread(morphed_image_path)

# iki görüntüyü birleştir
combined_image = np.hstack((original_image, morphed_image))


cv2.imshow('Original vs Morphed', combined_image)
cv2.imwrite('compareimg.jpeg',combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


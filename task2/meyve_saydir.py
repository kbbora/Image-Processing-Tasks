import cv2

image_path = 'meyve.jpg'
org_image = cv2.imread(image_path)
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# binary görüntü için threshold
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

# kontur bulma
contours,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# konturları çizme ve numaralandırma
for i, contour in enumerate(contours):
    # konturu çizme
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    # kontur merkezi
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    # numaralama
    cv2.putText(image, str(i+1), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)


output_path = 'numbered_fruits.jpg'
cv2.imwrite(output_path, image)


cv2.imshow('Saydirma', image)
cv2.imshow('Orijinal', org_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

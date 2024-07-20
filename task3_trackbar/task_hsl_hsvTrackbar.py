import cv2
import numpy as np
import colorsys


def nothing(x):
    pass


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        bgr = img[y, x]  # Tıklanılan pikselin bgr değerlerini almak için
        b, g, r = int(bgr[0]), int(bgr[1]), int(bgr[2])

        hsv = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
        h, s, v = int(hsv[0]), int(hsv[1]), int(hsv[2])

        hsl = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
        h_hsl, l_hsl, s_hsl = int(hsl[0] * 179), int(hsl[1] * 255), int(hsl[2] * 255)

        # Resmin üzerine yazı
        img_display[:] = img[:]  # görüntüyü orijinal haline sıfırlar
        text_hsv = f"HSV: H={h}, S={s}, V={v}"
        text_hsl = f"HSL: H={h_hsl}, S={s_hsl}, L={l_hsl}"
        cv2.putText(img_display, text_hsv, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.putText(img_display, text_hsl, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.imshow("Image", img_display)


img = cv2.imread(r'C:\Users\BORA\PythonProjeleri\PythonProjeleri\images\opencv.png')
img_display = img.copy()  # metin görüntülemek için kopyalama

# Pencere oluşturma
cv2.namedWindow("Image")
cv2.namedWindow("HSV Trackbar")
cv2.namedWindow("HSL Trackbar")

cv2.setMouseCallback("Image", mouse_callback)

#  HSV Trackbarların oluşturulması
cv2.createTrackbar("H", "HSV Trackbar", 0, 179, nothing)
cv2.createTrackbar("S", "HSV Trackbar", 0, 255, nothing)
cv2.createTrackbar("V", "HSV Trackbar", 0, 255, nothing)

# HSL Trackbarların oluşturulması
cv2.createTrackbar("H", "HSL Trackbar", 0, 179, nothing)
cv2.createTrackbar("S", "HSL Trackbar", 0, 255, nothing)
cv2.createTrackbar("L", "HSL Trackbar", 0, 255, nothing)

while True:
    # HSV trackbar pozisyonları
    h_hsv = cv2.getTrackbarPos("H", "HSV Trackbar")
    s_hsv = cv2.getTrackbarPos("S", "HSV Trackbar")
    v_hsv = cv2.getTrackbarPos("V", "HSV Trackbar")

    hsv = np.uint8([[[h_hsv, s_hsv, v_hsv]]])
    bgr_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    img_hsv = np.zeros((256, 256, 3), np.uint8)
    img_hsv[:] = bgr_hsv

    # HSL trackbar pozisyonları
    h_hsl = cv2.getTrackbarPos("H", "HSL Trackbar") / 179.0
    s_hsl = cv2.getTrackbarPos("S", "HSL Trackbar") / 255.0
    l_hsl = cv2.getTrackbarPos("L", "HSL Trackbar") / 255.0

    r_hsl, g_hsl, b_hsl = colorsys.hls_to_rgb(h_hsl, l_hsl, s_hsl)
    r_hsl, g_hsl, b_hsl = int(r_hsl * 255), int(g_hsl * 255), int(b_hsl * 255)
    img_hsl = np.zeros((256, 256, 3), np.uint8)
    img_hsl[:] = [b_hsl, g_hsl, r_hsl]

    cv2.imshow("Image", img_display)
    cv2.imshow("HSV Trackbar", img_hsv)
    cv2.imshow("HSL Trackbar", img_hsl)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np


cap = cv2.VideoCapture('video/zx.mp4')

while True:
    success, img = cap.read()

    # img = cv2.resize(img, (img.shape[1] // 1, img.shape[0] // 1))
    #
    img = cv2.GaussianBlur(img, (11, 9), 0)
    #
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    img = cv2.Canny(img, 90, 90)
    #
    kernel = np.ones((5, 5), np.uint8)
    #
    img = cv2.dilate(img, kernel, iterations=1)
    #
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("res", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break





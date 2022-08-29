import cv2

capp = cv2.VideoCapture('video/zx.mp4')

while True:
    success, img = capp.read()
    cv2.imshow('Result', img)

    # фпс, отслеживает клавишу q ее код




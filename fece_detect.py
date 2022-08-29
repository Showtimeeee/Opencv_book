import cv2

# обращаемся к основной камере
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

while True:
    succes, img = cap.read()
    cv2.imshow('Res', img)

    # фпс &  отслеживает клавишу q ее код для выхода
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pass
import cv2
import numpy as np


# черное полотно
photo = np.zeros((500, 600, 3), 'uint8')

# зеленый квадратик на черном полотне
# кортеж начального расположения фигуры(0,0)-левый верхний угол, размер, цвет, тип, толщина обводки
cv2.rectangle(photo, (50, 70), (100, 100), (31, 237, 230), thickness=3)

# линия на весь экран на черном полотне
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 250, 250), thickness=3)

# Круг, FILLED закрашивает фигуру
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (88, 235, 26), thickness=cv2.FILLED)

# Вывод текста
cv2.putText(photo, 'I Love Pyhton', (100, 100), cv2.FONT_HERSHEY_PLAIN, 4, (88, 235, 26), 2)


cv2.imshow('Photo', photo)
cv2.waitKey(0)
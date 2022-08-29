# РАБОТА С КАРТИНКАМИ
import cv2
import numpy as np


img = cv2.imread('images/dogy1.jpg')
# cv2.imshow("dog", img)

# изменение размера картинки
img = cv2.resize(img, (img.shape[1] // 1, img.shape[0] // 1))

# размытие картинки
img = cv2.GaussianBlur(img, (11, 9), 0)

# конверт в серый цвет
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# нахождение углов (серая обводка)
img = cv2.Canny(img, 90, 90)

# numpy матрица для нахождения точек ones ((5 списков по 5 эл))
# np.uint8 - тип данных - целые числа
kernel = np.ones((5, 5), np.uint8)

# iteration - обводка
img = cv2.dilate(img, kernel, iterations=1)

# обводка тоньше
img = cv2.erode(img, kernel, 1)





cv2.imshow("show_me_dog", img)

# постоянное воспроизведение картинки
cv2.waitKey(0)

# размер текущей картинки
print(img.shape)
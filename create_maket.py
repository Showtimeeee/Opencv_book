import cv2
import numpy as np


""" zeros метод - матрица из 0
матинца 500 на 600 , 3 слоя, формат-числа
получается изображение 500х600 черный из-за 0 """

photo = np.zeros((500, 600, 3), 'uint8')

# обращамеся ко всем эл, что бы окарсить пикс
# RGB = BGR
# фиолет
photo[:] = 196, 55, 116


cv2.imshow('Photo', photo)
cv2.waitKey(0)

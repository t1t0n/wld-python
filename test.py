import cv2
from descriptors import weber

grayscale_image = cv2.imread('test.jpg', 0)
descriptor = weber(grayscale_image)
cv2.imshow('win', descriptor)
cv2.waitKey(0)
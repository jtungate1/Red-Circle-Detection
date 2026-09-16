import cv2
import matplotlib.pyplot as plt
import numpy as np

imagePath = "./images/sample.jpg"

image = cv2.imread(imagePath)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(hsv_image, lower_red, upper_red)


result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Binary Mask Only', mask)
cv2.imshow('Mask Applied (Color Isolated)', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
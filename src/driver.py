import cv2
import matplotlib.pyplot as plt
import numpy as np

imagePath = "./images/ManyCircles.jpg"

image = cv2.imread(imagePath)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# making a mask for red color in the image
lower_red1 = np.array([0, 20, 20])
upper_red1 = np.array([4, 255, 255])
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)

# making a secondary mask to catch compression artifacts and other red shades
lower_red2 = np.array([176, 20, 20])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# combining the two masks to get a final mask for red color
mask = cv2.bitwise_or(mask1, mask2)

# blurring the mask to reduce noise and improve circle detection
gray = cv2.medianBlur(mask, 5)
cv2.imshow('gray', gray)

# detecting circles in the image using Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=40, minRadius=30, maxRadius=500)

if circles is not None:
    print(f"Detected {len(circles[0])} circles")
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        # Draw the outer circle
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        
        # Draw a cross at the center
        cross_size = 10
        cv2.line(image, (x - cross_size, y), (x + cross_size, y), (255, 0, 0), 2)
        cv2.line(image, (x, y - cross_size), (x, y + cross_size), (255, 0, 0), 2)

    cv2.imshow('Detected Circle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles detected")

cv2.waitKey(0)
cv2.destroyAllWindows()

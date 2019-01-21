import cv2
import numpy as np

image = cv2.imread('./Course_materials/Master_OpenCV/images/opencv_inv.png')
cv2.imshow('Original Image', image)
cv2.waitKey(2000)

kernel = np.ones((5,5), np.uint8)

#dilation - Adds pixels at the boundaries in an image
dilate = cv2.dilate(image, kernel, iterations=1) 
cv2.imshow('Dilate', dilate)
cv2.waitKey(2000)

#erosion - Removes pixels at the boundaries in an image
erosion = erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(2000)

#opening - Erosion and then Dilation - Good for removing noise
opening = erosion = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(2000)

#closing - Dilation and then Erosion - Good for removing noise
closing = erosion = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(2000)

cv2.destroyAllWindows()

#Dilation and Erosion might cause opposite effects in an B/W image - Adds white pixels in a white over black background image
#Check out other morphoilogy operations - They might not be very useful though

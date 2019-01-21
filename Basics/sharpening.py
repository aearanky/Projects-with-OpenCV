import cv2
import numpy as np

image= cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')
cv2.imshow('Original image', image)

sharpen_filter = np.array([[-1, -1, -1],
					 [-1, 9, -1],
					 [-1, -1, -1]])

sharpened = cv2.filter2D(image, -1, sharpen_filter)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(2000)
cv2.destroyAllWindows()

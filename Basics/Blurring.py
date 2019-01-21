import cv2
import numpy as np

image = cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey(2000)

kernel_3x3 = np.ones((3,3), dtype=np.float32) / 9
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow("3X3 Blur", blurred)
cv2.waitKey(2000)
cv2.destroyAllWindows()

kernel_5x5 = np.ones((5,5), dtype=np.float32) / 25
blurred = cv2.filter2D(image, -1, kernel_5x5)
cv2.imshow("5X5 Blur", blurred)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#blurring using cv2 functions
blur = cv2.blur(image, (3,3))
cv2.imshow("3x3 blurring using cv2.blur Averaging", blur)
cv2.waitKey(2000)
cv2.destroyAllWindows()

gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("7x7 blurring using cv2.GaussianBlur Averaging", gaussian)
cv2.waitKey(2000)
cv2.destroyAllWindows()

median = cv2.medianBlur(image, 5)
cv2.imshow("5x5 blurring using cv2.medianBlur Averaging", median)
cv2.waitKey(2000)
cv2.destroyAllWindows()

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("blurring using cv2.bilateralFilter Averaging", bilateral)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#Read about image de-noising using cv2

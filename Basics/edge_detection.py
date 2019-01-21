import cv2
import numpy as np

image=cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)
cv2.waitKey(2000)

#extract sobel edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('sobel_x', sobel_x)
cv2.waitKey(2000)

sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow('sobel_y', sobel_y)
cv2.waitKey(2000)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel_OR', sobel_OR)
cv2.waitKey(2000)

#extract laplacian edges
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(2000)

#extract Canny edges
canny = cv2.Canny(image, 20, 170) #cv2.Canny(image, minVal, maxVal)
cv2.imshow('Canny', canny)
cv2.waitKey(2000)

cv2.destroyAllWindows()
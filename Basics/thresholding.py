import cv2
import numpy as np

image = cv2.imread('./Course_materials/Master_OpenCV/images/gradient.jpg')
cv2.imshow('Original image', image)

#Thresholding, Binarization and Adaptive thresholding

#Thresholding is the act of converting an image to a binary form
#image needs to be converted to grayscale before thresholding

#cv2.threshold(image, threshold value, max value, threshold type)

ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)
cv2.waitKey(2000)

ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse', thresh2)
cv2.waitKey(2000)

ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC ', thresh3)
cv2.waitKey(2000)

ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO ', thresh4)
cv2.waitKey(2000)

ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV', thresh5)
cv2.waitKey(2000)

cv2.destroyAllWindows()

#read up on adaptive thresholding -- Use it for scanning books
#cv2.adaptiveThreshold(image ,Max Value, Adaptive type (Example: ADAPTIVE_THRESH_MEAN_C), Threshold Type (Example: cv2.THRESH_BINARY), Block Size, Constant that is subtracted from mean) 
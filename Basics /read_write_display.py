import cv2
import numpy as np

# Read image in RGB color space format 
# -------------------------------------------
input = cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')
cv2.imshow('Hello world', input)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# Image dimensions
# -------------------------------------
print input.shape
print 'Height of Image: ', int(input.shape[0]), 'pixels'
print 'Width of Image: ', int(input.shape[1]), 'pixels'


# Writing to a file 
# -------------------------------------
cv2.imwrite('./Outputs/output.jpg', input);

# Convert to grayscale 
# ----------------------------------
gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale1', gray_image)
cv2.waitKey(1500)
cv2.imwrite('./Outputs/output_gray.jpg', gray_image);

#faster method
gray_image_2 = cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg', 0)
cv2.imshow('Grayscale2', gray_image_2)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#-------------------------------------------------------

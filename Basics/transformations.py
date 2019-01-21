import cv2
import numpy as np

# Translations
# [1 0 Tx; 0 1 Ty] cv2.warpAffine

image = cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey(2000)

#store height and width of the image
height, width = image.shape[:2]
print image.shape
print height, width

# T is our translation matrix
q_height = height/4
q_width = width/4

T = np.float32([[1,0, q_height],[0,1,q_width]])
print T

translated_image = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', translated_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#rotation
T = cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
print 'Rotation Matrix' +  '\n' + str(T)
rotated_image = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Rotation', rotated_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#resize (using interpolation)
image_scaled = cv2.resize(image, None, fx=0.25, fy=1)
cv2.imshow('Scaling - Linear Interpolation', image_scaled)
cv2.waitKey(2000)

image_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', image_scaled)
cv2.waitKey(2000) 

image_scaled = cv2.resize(image, (300, 500), interpolation=cv2.INTER_AREA) 
cv2.imshow('Scaling - Skewed Size', image_scaled)
cv2.waitKey(2000)
cv2.destroyAllWindows()


#creating image pyramids - useful in object detection
smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(image) 

cv2.imshow('smaller', smaller)
cv2.waitKey(2000)

cv2.imshow('larger', larger)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#cropping
start_row, start_col = int(height*0.25), int(width * 0.25)
end_row, end_col = int(height*0.75), int(width * 0.75)

cropped_image = image[start_row:end_row, start_col:end_col]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#arithmetic operations

#bitwsie operations

#blurring
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


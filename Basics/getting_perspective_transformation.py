import cv2
import numpy as np

image = cv2.imread('./Course_materials/Master_OpenCV/images/scan.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(2000)

# assume we know the 4 corners of the non-affine transformed image --> Parallelism is not preserved
points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])

# we need to move to these points (1:1.41) for an A4 size paper
points_B = np.float32([[0,0],[420,0],[0,594],[420,594]])

# find the perspective transformation -> Use the 2 sets of 4 points
# for affine transform, you need 2 sets of 3 points 
M = cv2.getPerspectiveTransform(points_A, points_B)

warped = cv2.warpPerspective(image, M, (420, 594))
cv2.imshow('Warped Image', warped)
cv2.waitKey(2000)

cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

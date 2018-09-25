import cv2
import numpy as np

from matplotlib import pyplot as plt

# Read image in RGB color space format 
# -------------------------------------------
image = cv2.imread('./Course_materials/Master_OpenCV/images/input.jpg')

# Calculate and plot histogram 
# -------------------------------
#paramaters - image is 2D, channels (currently blue), masking, Max Value, Range
histogram = cv2.calcHist([image], [0], None, [256], [0,256])

#ravel flattens 2D into 1D
plt.hist(image.ravel(), 256, [0,256])
plt.show()

# Viewing separate components
# ------------------------------
color = ('b', 'g', 'r')

for i, col in enumerate(color):
	histogram2 = cv2.calcHist([image], [i], None, [256], [0,256])
	plt.plot(histogram2, color = col)
	plt.xlim([0,256])
	
plt.show()



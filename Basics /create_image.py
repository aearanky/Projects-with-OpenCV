import cv2
import numpy as np

# Create a black image
# --------------------
image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('Black rectangle (Color)', image)
cv2.waitKey(1000)

# Convert the image to black and white
image_bw = np.zeros((512, 512), np.uint8)
cv2.imshow('Black rectangle (BW)', image_bw)
cv2.waitKey(1000)

# Draw a line
# ------------
#parameters - input image, lowerbounds, upperbounds, color of line, thickness
cv2.line(image, (0,0), (511, 511), (255, 127, 0), 5)
cv2.imshow('Blue line', image)
cv2.waitKey(1000)

# Draw a rectangle
# ----------------
#parameters - input image, lowerbounds, upperbounds, color of line, thickness
cv2.rectangle(image, (100,100), (300, 250), (127, 50, 127), 5)
cv2.imshow('Blue rectangle', image)
cv2.waitKey(1000)

# Draw a circle
# ----------------
#parameters - input image, lowerbounds, radius, color of line, thickness
cv2.circle(image, (350,350), 100, (20, 50, 20), -1)
cv2.imshow('Blue rectangle', image)
cv2.waitKey(1000)

cv2.destroyAllWindows()

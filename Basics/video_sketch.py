import cv2
import numpy as np

def sketch(img):
	#convert image to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#clean up the image using gaussian blur
	gaussian = cv2.GaussianBlur(img, (5,5), 0)

	#detect edges using canny
	canny = cv2.Canny(gaussian, 20, 170)

	#binarize the image
	ret, mask = cv2.threshold(canny, 20, 255, cv2.THRESH_BINARY)
	return mask

cap = cv2.VideoCapture(0)

while 1:
	ret, frame = cap.read()
	cv2.imshow('Our Live Sketcher', sketch(frame))
	if cv2.waitKey(1)==13:
		break

#release camera and webcam
cap.release()
cv2.destroyAllWindows()
# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of it
(h, w) = image.shape[:2]
(cX, cY) = (w/2, h/2)

# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 degrees", rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by offset & 45 degrees", rotated)

M = cv2.getRotationMatrix2D((cX, cY), -30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[254, 335]
print "Pixel at (335, 254) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

M = cv2.getRotationMatrix2D((cX, cY), 110, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[136, 312]
print "Pixel at (312, 136) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
(b, g, r) = rotated[10, 10]
print "Pixel at (10, 10) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)


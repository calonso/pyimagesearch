# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped horizontally", flipped)
(b, g, r) = flipped[235, 259]
print("Pixel value at [259, 235] = ({r}, {g}, {b})").format(r=r, g=g, b=b)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped vertically", flipped)

# flip image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped horizontally & vertically", flipped)

# flip it horizontally
ex2 = cv2.flip(image, 1)
# then rotate it 45 degree counter-clockwise
(h, w) = ex2.shape[:2]
(cX, cY) = (w/2, h/2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
ex2 = cv2.warpAffine(ex2, M, (w, h))

# finally, flip it vertically
ex2 = cv2.flip(ex2, 0)
(b, g, r) = ex2[189, 441]
print("Pixel value at [441, 189] = ({r}, {g}, {b})").format(r=r, g=g, b=b)

cv2.waitKey(0)

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# impages are NumPy arrays, stored as unsigned 8bit integers -- this
# implies that the values of our pixels will be in the range of [0, 255]; when
# using functions like cv2.add and cv2.subtract, values will be clipped
# to this range, even if the added or subtracted values fall outside the
# range of [0, 255]. Check out an example:
print "max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))
print "min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100])))

# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulos (wrap around) instead of being clipped to the [0, 255]
# range. This is important to keep in mind when working with images
print "wrap around: " + str(np.uint8([200]) + np.uint8([100]))
print "wrap around: " + str(np.uint8([50]) - np.uint8([100]))

# let's increase the intensity of all pixels in our image by 100 -- we
# accomplish this by constructing a NumPy array that is the same size of
# our matrix (fillez with ones) and the multiplying it by 100 to create an
# array filled with 100's, then we simply add the images together; notice
# how tie image is "brighter"
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

# similarly, we can subtract 50 from all pixels in our image and make it darker
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
print str(image.shape)

# for the exercise, add 75 to all pixels of the grand_canyon.png image using
# cv2.add and get the value at x=61, y=152
M = np.ones(image.shape, dtype="uint8") * 75
added = cv2.add(image, M)
(b, g, r) = added[152, 61]
print "Value at pixel [61, 152]: {r}, {g}, {b}".format(r=r, g=g, b=b)
cv2.waitKey(0)

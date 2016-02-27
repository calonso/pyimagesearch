# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
# cv2.imshow("Original", image)

# we need to keep in mind aspect ratio, so the image does not look skewed
# or disrtorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels.
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# what if we wanted to adjust the height of the image? We can apply
# the same concept, again keeping in mind the aspect ratio, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels
r = float(image.shape[1]) / float(image.shape[0])
dim = (int(50.0 * r), 50)

# peform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

# construct the list of interpolation methods
methods = [
  ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
  ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
  ("cv2.INTER_AREA", cv2.INTER_AREA),
  ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
  ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

# loop over the interpolation methods
for (name, method) in methods:
  # increase the size of the image by 3x using the current interpolation metrhod
  resized = cv2.resize(image, (int(image.shape[0] * 3), int(image.shape[1] * 3)), interpolation=method)
  cv2.imshow(name, resized)

cv2.waitKey(0)

wratio = float(image.shape[0]) / float(image.shape[1])
resized = cv2.resize(image, (100, int(wratio * 100)), interpolation=cv2.INTER_NEAREST)
(b, g, r) = resized[74, 20]
print "Pixel value at [20, 74] is {r}, {g}, {b}".format(r=r, g=g, b=b)

resized = imutils.resize(image, width=100, inter=cv2.INTER_NEAREST)
(b, g, r) = resized[74, 20]
print "Pixel value at [20, 74] is {r}, {g}, {b}".format(r=r, g=g, b=b)

resized = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2), interpolation=cv2.INTER_CUBIC)
(b, g, r) = resized[367, 170]
print "Pixel value at [170, 367] is {r}, {g}, {b}".format(r=r, g=g, b=b)

resized = imutils.resize(image, width=image.shape[1] * 2, height=image.shape[0] * 2, inter=cv2.INTER_CUBIC)
(b, g, r) = resized[367, 170]
print "Pixel value at [170, 367] is {r}, {g}, {b}".format(r=r, g=g, b=b)


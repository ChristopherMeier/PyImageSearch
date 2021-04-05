import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

# open image
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

print('max of 255: {}'.format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print('min of 0: {}'.format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))

# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulo (wrap around) instead of being  clipped to the [0, 255]
# range. This is important to keep in mind when working with images.
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

M = np.ones(image.shape, dtype = "uint8") * 75
added = cv2.add(image, M)
cv2.imshow("Added", added)

print(added[152][61])
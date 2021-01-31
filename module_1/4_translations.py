
import numpy as np
import argparse
import imutils
import cv2


# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

print(image.shape)


# using the translation matrix to shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted down and right', shifted)
cv2.waitKey(0)

# shifting 50 pixels to the left and 90 pixels up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted up and left', shifted)
cv2.waitKey(0)

test = imutils.translate(image, 100, -50)
cv2.imshow('shifted up and left', test)
cv2.waitKey(0)
import numpy as np
import argparse
import imutils
import cv2

# construction of an argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# lets resize the image with a width of 150 pixels
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('resized (width)', resized)
cv2.waitKey(0)

# lets resize the image with a width of 150 pixels
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow('resized (width)', resized)
cv2.waitKey(0)

print(resized[74][20])

# lets resize the image twice as the original image
#r = 2 * image.shape[1]
dim = (2*image.shape[1], 2*image.shape[0])

resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow('resized 2x original', resized)
cv2.waitKey(0)

print(resized[367][170])
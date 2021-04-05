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

# grab the dimension of the image and calculate the center

# numpy shape gives us the y and x component

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# rotate the image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('rotated by 45 deg', rotated)
cv2.waitKey(0)

# rotate the image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('rotated by -90 deg', rotated)
cv2.waitKey(0)

# rotation with imutils package
rotated = imutils.rotate(image, 110)
cv2.imshow('rotated by 180 deg', rotated)
cv2.waitKey(0)

# rotate the image by 45 degrees
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('rotated by 45 deg', rotated)
cv2.waitKey(0)


print(rotated[10][10])


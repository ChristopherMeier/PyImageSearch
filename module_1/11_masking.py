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

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

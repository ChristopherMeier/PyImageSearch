# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image, display it, and initialize the list of kernel sizes
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# loop over all kernels and apply a "blurring" operation to the image
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow('Average: ({}, {})'.format(kX, kY), blurred)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over all kernels and apply a "gaussian blur" operation to the image
for (kX, kY) in kernelSizes:
    gaussian = cv2.GaussianBlur(image,(kX, kY), 0)
    cv2.imshow('Gaussian: ({}, {})'.format(kX, kY), gaussian)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over all kernels and apply a "median blur" operation to the image
for k in (3, 9, 15):
    median = cv2.medianBlur(image, k)
    cv2.imshow('Median blur: {}'.format(k), median)
    cv2.waitKey(0)

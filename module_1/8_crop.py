import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# cropping is achieved by simply slicing the numy array
face = image[85:250, 85:220]
cv2.imshow('face', face)
cv2.waitKey(0)

# cropping the entire body
body = image[90:450, 0:290]
cv2.imshow('body', body)
cv2.waitKey(0)

# cropping peaple in the back
people = image[173:235, 13:81]
cv2.imshow('people in the back', people)
cv2.waitKey(0)

# cropping the boat
boat = image[124:212, 225:380]
cv2.imshow('boat', boat)
cv2.waitKey(0)

 
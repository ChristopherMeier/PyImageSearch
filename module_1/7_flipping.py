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

""" # flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow('image flipped horizontally', flipped)
cv2.waitKey(0)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow('image flipped horizontally', flipped)
cv2.waitKey(0) """

# flip the image on both axis
flipped_quiz = cv2.flip(image, 1)
cv2.imshow('image flipped horizontally according to the quiz', flipped_quiz)
cv2.waitKey(0)

rotation_quiz = imutils.rotate(flipped_quiz, 45)
cv2.imshow('image rotated -45 deg according to the quiz', rotation_quiz)
cv2.waitKey(0)

flipped_vertical = cv2.flip(rotation_quiz, 0)
cv2.imshow('image flipped vertically according to the quiz', flipped_vertical)
cv2.waitKey(0)

print(flipped_vertical[188][440])
# import necessary packages
import argparse
import cv2

# construct the argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, grab its dimensions
image = cv2.imread(args['image'])
(h, w) = image.shape[:2]
cv2.imshow('Original', image)
cv2.waitKey()

# images are numpy arrays
(b, g, r) = image[224, 110]
print('Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}'.format(r=r, g=g, b=b))

# lets change the (0,0) pixel and make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print('Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}'.format(r=r, g=g, b=b))

# compute the center of the image

(cX, cY) = (w // 2, h // 2)
tl = image[0:cY, 0:cX]
cv2.imshow('Top-left-corner', tl)
cv2.waitKey()

tr = image[0:cY, cX:w]
bl = image[cY:h, 0:cX]
br = image[cY:h, cX:w]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey()
# import necessary packages
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from top-left corner to the bottom-right

green = (0, 255, 0)
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow('line', canvas)
cv2.waitKey()

# drawing a 3 pixel thick red line from the top-right to the bottom-left
red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red, 3)
cv2.imshow('line_red', canvas)
cv2.waitKey()

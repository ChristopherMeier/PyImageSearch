# import necessary packages
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from top-left corner to the bottom-right

green = (0, 255, 0)
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow('line', canvas)
cv2.waitKey(0)

# drawing a 3 pixel thick red line from the top-right to the bottom-left
red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red, 3)
cv2.imshow('line_red', canvas)
cv2.waitKey(0)


# drawing a green rectangle starting at point (10, 10) 
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# drawing a red rectangle and 5pt thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# draw a last rectnagle -> blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

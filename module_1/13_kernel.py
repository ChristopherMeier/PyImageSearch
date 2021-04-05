#import cv2
import numpy as np
from scipy import signal



matrix_A = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
matrix_B = np.array([[202, 119, 154], [106, 119, 11], [186, 48, 250]])
print(matrix_A)
print(matrix_B)
print(matrix_B.shape)

print(matrix_A[2][0])

erg = signal.convolve2d(matrix_A, matrix_B, mode='same', boundary='fill', fillvalue=0)

print(erg[])
print(matrix_A.shape)

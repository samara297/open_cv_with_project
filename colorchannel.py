import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)

# Split the image into B, G, R channels
b, g, r = cv.split(img)

# Create blank (black) channel for merging
zeros = np.zeros_like(b)

# Show each channel in color
blue_image = cv.merge([b, zeros, zeros])
green_image = cv.merge([zeros, g, zeros])
red_image = cv.merge([zeros, zeros, r])

# Show original and the individual color channels
cv.imshow('Original', img)
cv.imshow('Blue Channel', blue_image)
cv.imshow('Green Channel', green_image)
cv.imshow('Red Channel', red_image)

cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
#averaging
blurred = cv.blur(img, (5, 5))
cv.imshow("Averaging Blurred", blurred)
# Gaussian 
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("Gaussian Blurred", gaussian_blur)
# median
median_blur = cv.medianBlur(img, 5)
cv.imshow("Median Blurred", median_blur)
# Apply Bilateral Filter
bilateral_filtered = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow("Bilateral Filtered", bilateral_filtered)

cv.waitKey(0)
cv.destroyAllWindows()
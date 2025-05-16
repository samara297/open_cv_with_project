#Thresholding turns a grayscale image into a black and white image.
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
# #simple thresholding
threshold,thresh=cv.threshold(grey,150,255,cv.THRESH_BINARY)
cv.imshow("Simple Threshold",thresh)
#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Adaptive Threshold",adaptive_thresh)

cv.waitKey(0)
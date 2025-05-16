import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
#blank
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)
# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
# #blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)
#canny
canny=cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)
#thresh
thresh=cv.threshold(grey,125,255,cv.THRESH_BINARY)[1]
cv.imshow("Threshold",thresh)
#ccontours
contours,hierarchy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
# #draw contours
cv.drawContours(blank, contours, -1, (255, 255, 255), 1)
cv.imshow("Contours Drawn",blank)

cv.waitKey(0)
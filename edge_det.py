#The Laplacian is a math tool used in OpenCV to detect edges in images.import cv2 as cv
import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
#laplacian
lap=cv.Laplacian(grey,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)
#sobel
sobel_x=cv.Sobel(grey,cv.CV_64F,1,0)
sobel_y=cv.Sobel(grey,cv.CV_64F,0,1)
sobel_x=np.uint8(np.absolute(sobel_x))
sobel_y=np.uint8(np.absolute(sobel_y))
cv.imshow("Sobel X",sobel_x)
cv.imshow("Sobel Y",sobel_y)
cv.waitKey(0)
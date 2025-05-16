import cv2 as cv
import cv2 as cv
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
# #blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)
#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)
#dilated
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)
#eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)
#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
#cropped
cropped=img[50:200,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
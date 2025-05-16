import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)

# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
#BGR TO HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)
#BGR TO LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)
#BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
plt.imshow(rgb)
plt.show()
#hsv to bgr
hsv_to_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_to_bgr)



cv.waitKey(0)
#A histogram in OpenCV shows how many pixels are light or dark in a picture.
#It's useful to check the brightness, fix contrast, and help computers find objects in images.
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
# #converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",grey)
#grayscale histogram
gray_hist=cv.calcHist([grey],[0],None,[256],[0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

# #color histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
colors=("b","g","r")
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
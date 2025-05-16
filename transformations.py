import cv2 as cv 
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)

#translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
#-x-->left
#-y-->up
#x-->right
#y-->down
translated=translate(img,100,100)
cv.imshow("Translated",translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (h,w)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(w//2,h//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(w,h)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45)
cv.imshow("Rotated",rotated)

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)
#flipping
flipped=cv.flip(img,0) #0=vertical,1=horizontal,-1=both
cv.imshow("Flipped",flipped)

#cropping
cropped=img[50:200,200:400]
cv.imshow("Cropped",cropped)
cv.waitKey(0)
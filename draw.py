import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blank)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
# cv.imshow("rectangle",blank)

cv.putText(blank,"Mahirat",(225,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)
cv.waitKey(0)

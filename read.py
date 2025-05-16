import cv2 as cv
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
cv.waitKey(0)



# import cv2 as cv
# capture=cv.VideoCapture("C:\\Users\\ACER\\Desktop\\opencv\\mahiratvid.mp4")
# while True:
#     isTrue,frame=capture.read()
#     cv.imshow("Video",frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
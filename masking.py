import cv2 as cv
import numpy as np
img=cv.imread("C:\\Users\\ACER\\Desktop\\opencv\\mahirat.jpg")
cv.imshow("Mahirat",img)
# #masking
# mask = np.zeros(img.shape[:2], dtype="uint8")

# # Draw a white circle on the mask
# cv.circle(mask, (200, 200), 100, 255, -1)  

# # Apply the mask to the image
# masked_image = cv.bitwise_and(img, img, mask=mask)

# # Show the results
# cv.imshow("Original", img)
# cv.imshow("Mask", mask)
# cv.imshow("Masked Image", masked_image)

cv.waitKey(0)
cv.destroyAllWindows()

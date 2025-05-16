# AND: Combines two images where both pixels must be non-zero.

# OR: Combines two images where either pixel can be non-zero.

# XOR: Combines two images where pixels are different.

# NOT: Inverts the pixel values (flips 0 to 255 and vice versa
import cv2
import numpy as np

# Create two simple images (black square and white circle)
image1 = np.zeros((400, 400), dtype="uint8")
cv2.rectangle(image1, (50, 50), (350, 350), 255, -1)  # White square

image2 = np.zeros((400, 400), dtype="uint8")
cv2.circle(image2, (200, 200), 150, 255, -1)  # White circle

# Bitwise AND: Intersection (where both images are white)
bitwise_and = cv2.bitwise_and(image1, image2)

# Bitwise OR: Union (where either image is white)
bitwise_or = cv2.bitwise_or(image1, image2)

# Bitwise XOR: Difference (where the images are different)
bitwise_xor = cv2.bitwise_xor(image1, image2)

# Bitwise NOT: Inverts the first image
bitwise_not = cv2.bitwise_not(image1)

# Show the images
cv2.imshow("Image 1 (Square)", image1)
cv2.imshow("Image 2 (Circle)", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()

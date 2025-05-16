import cv2

# Load pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read an image
img = cv2.imread("C:\\Users\\ACER\\Desktop\\opencv\\5-Malayalam-movies-to-watch-this-month-5-1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show the result
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


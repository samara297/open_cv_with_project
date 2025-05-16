import cv2

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load image
image = cv2.imread('C:\\Users\\ACER\Desktop\\opencv\\mahirat.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangle and put name label for each face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(image, 'Person', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                0.9, (255, 0, 0), 2)

# Show the image
cv2.imshow('Face Detection with Names', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

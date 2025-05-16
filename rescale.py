# import cv2 as cv

# # Read the image (with corrected path)
# img = cv.imread(r"C:\Users\ACER\Desktop\opencv\mahirat.jpg")
# cv.imshow("Original Mahirat", img)

import cv2 as cv

# Rescale function
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# --- VIDEO RESIZE PART ---

# Open video file
capture = cv.VideoCapture(r"C:\Users\ACER\Desktop\opencv\mahiratvid.mp4")

while True:
    isTrue, frame = capture.read()
    
    # If video has ended or can't read the frame
    if not isTrue:
        break

    # Resize the current frame
    frame_resized = rescale_frame(frame, scale=0.5)

    # Show both original and resized frames
    cv.imshow("Original Video", frame)
    cv.imshow("Resized Video", frame_resized)

    # Press 'd' to exit
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release video and destroy all windows
capture.release()
cv.destroyAllWindows()

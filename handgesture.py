import cv2
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hand Detection
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Initialize Webcam
cap = cv2.VideoCapture(0)

# Initialize Pycaw for Volume Control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

while True:
    success, img = cap.read()
    if not success:
        break

    # Flip for natural interaction
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        lmList = []

        for id, lm in enumerate(handLms.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append((cx, cy))

        # Draw landmarks
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        # Get coordinates of Thumb Tip and Index Tip
        x1, y1 = lmList[4]   # Thumb tip
        x2, y2 = lmList[8]   # Index tip

        # Draw circles and line between tips
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)

        # Calculate distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Map distance to volume range
        vol = np.interp(length, [20, 200], [volMin, volMax])
        volPercent = np.interp(length, [20, 200], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        # Draw volume bar
        cv2.rectangle(img, (30, 150), (50, 400), (0, 255, 0), 3)
        volBar = np.interp(length, [20, 200], [400, 150])
        cv2.rectangle(img, (30, int(volBar)), (50, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPercent)} %', (30, 430), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

    cv2.imshow("Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

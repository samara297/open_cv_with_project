import cv2
import numpy as np
import mediapipe as mp

# Setup
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

keys = ['A', 'B', 'C']
key_positions = [(100, 100), (200, 100), (300, 100)]
typed_text = ""
clicked = False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0]
        lmList = []
        for id, l in enumerate(lm.landmark):
            h, w, _ = img.shape
            lmList.append((int(l.x * w), int(l.y * h)))
        mpDraw.draw_landmarks(img, lm, mpHands.HAND_CONNECTIONS)

        x1, y1 = lmList[8]   # Index tip
        x2, y2 = lmList[12]  # Middle tip
        dist = np.hypot(x2 - x1, y2 - y1)

        for i, (x, y) in enumerate(key_positions):
            cv2.rectangle(img, (x, y), (x+60, y+60), (255, 0, 255), cv2.FILLED)
            cv2.putText(img, keys[i], (x+15, y+45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

            if x < x1 < x+60 and y < y1 < y+60:
                if dist < 40 and not clicked:
                    typed_text += keys[i]
                    clicked = True
        if dist > 40:
            clicked = False

    # Display typed text
    cv2.putText(img, typed_text, (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

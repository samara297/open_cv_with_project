import cv2
import numpy as np
from collections import OrderedDict

# Simple CentroidTracker class to track objects across frames
class CentroidTracker:
    def __init__(self, max_disappeared=50):
        self.next_object_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.max_disappeared = max_disappeared

    def register(self, centroid):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update(self, input_centroids):
        if len(input_centroids) == 0:
            # Mark all objects as disappeared
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1
                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)
            return self.objects

        if len(self.objects) == 0:
            for centroid in input_centroids:
                self.register(centroid)
        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            # Compute distance between each pair of old and new centroids
            D = np.linalg.norm(np.array(object_centroids)[:, np.newaxis] - np.array(input_centroids), axis=2)

            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            used_rows = set()
            used_cols = set()

            for (row, col) in zip(rows, cols):
                if row in used_rows or col in used_cols:
                    continue
                if D[row, col] > 50:  # Max distance threshold to match
                    continue

                object_id = object_ids[row]
                self.objects[object_id] = input_centroids[col]
                self.disappeared[object_id] = 0

                used_rows.add(row)
                used_cols.add(col)

            unused_rows = set(range(len(object_centroids))) - used_rows
            unused_cols = set(range(len(input_centroids))) - used_cols

            for row in unused_rows:
                object_id = object_ids[row]
                self.disappeared[object_id] += 1
                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)

            for col in unused_cols:
                self.register(input_centroids[col])

        return self.objects

def get_center(x, y, w, h):
    return int(x + w / 2), int(y + h / 2)

cap = cv2.VideoCapture('C:\\Users\\ACER\\Desktop\\opencv\\WhatsApp Video 2025-05-10 at 8.09.41 AM.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

line_position = 300
offset = 10
car_count = 0

ct = CentroidTracker()
counted_ids = set()
previous_centroids = {}  # To store previous Y positions of tracked objects

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    mask = fgbg.apply(blur)

    _, thresh = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    centers = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w >= 50 and h >= 50:
            centers.append(get_center(x, y, w, h))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    objects = ct.update(centers)

    cv2.line(frame, (0, line_position), (800, line_position), (255, 0, 0), 2)

    for object_id, centroid in objects.items():
        cv2.circle(frame, centroid, 4, (0, 0, 255), -1)
        cv2.putText(frame, f"ID {object_id}", (centroid[0] - 10, centroid[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        previous_y = previous_centroids.get(object_id, None)
        current_y = centroid[1]

        if previous_y is not None:
            # Check if the object crossed the line downward
            if previous_y < line_position <= current_y:
                if object_id not in counted_ids:
                    car_count += 1
                    counted_ids.add(object_id)

        # Update the previous y position
        previous_centroids[object_id] = current_y

    cv2.putText(frame, f"Cars Counted: {car_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow('Car Counter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



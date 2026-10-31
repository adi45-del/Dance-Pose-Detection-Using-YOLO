
from ultralytics import YOLO
import cv2
import numpy as np
import os

folder = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(folder, "dance (2).mp4")
output_path = os.path.join(folder, "dance_output.mp4")

model = YOLO("yolo26n-pose.pt")

cap = cv2.VideoCapture(input_path)

if not cap.isOpened():
    raise ValueError("Input video not found. Check dance (2).mp4.")

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 30

if w <= 0 or h <= 0:
    raise ValueError("Could not read video dimensions.")

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

if not out.isOpened():
    raise ValueError("Could not create output video.")

frame_count = 0
detected_frames = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    r = model(frame, verbose=False)[0]

    black = np.zeros_like(frame)

    if r.keypoints is not None:

        people = r.keypoints.xy.cpu().numpy().astype(int)

        if len(people) > 0:
            detected_frames += 1

        for person in people:

            for x, y in person:

                if 0 <= x < w and 0 <= y < h:

                    cv2.circle(
                        black,
                        (x, y),
                        4,
                        (255, 255, 255),
                        -1
                    )

    out.write(black)
    frame_count += 1

cap.release()
out.release()

print("Total frames processed:", frame_count)
print("Frames with detected poses:", detected_frames)
print("Output video path:", output_path)

if os.path.exists(output_path) and os.path.getsize(output_path) > 0:

    print("Video saved successfully!")
    os.startfile(output_path)

else:

    print("Output video could not be created.")



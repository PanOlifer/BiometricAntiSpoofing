# TODO:  fix the code to make it works?
import cv2
import time
import os

# Path to the output directory
output_dir = 'C:/Users/User/Documents/GitHub/BiometricAntiSpoofing/src/pics/'

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

# Set video capture properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(fps * 10)  # Capture video for 10 seconds
frame_count = 0

# Initialize empty list to store frames
frames = []

# Iterate over frames until desired length is reached
while frame_count < total_frames:
    # Read frame from webcam
    ret, frame = cap.read()

    # If frame read is successful, add it to the frames list
    if ret:
        frames.append(frame)
        frame_count += 1

    # Display the frame (optional, comment out if not needed)
    cv2.imshow('Video', frame)
    cv2.waitKey(1)

    # Delay to match the desired video length (10 seconds)
    time.sleep(1 / fps)

# Release video capture and close window
cap.release()
cv2.destroyAllWindows()

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save extracted frames as individual images
for i, frame in enumerate(frames):
    filename = f'frame_{i}.jpg'
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, frame)
    print(f"Saved frame {i + 1} as {filepath}")
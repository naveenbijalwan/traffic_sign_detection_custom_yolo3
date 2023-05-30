import cv2
import os

def video_to_images(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read and save frames until the video ends
    frame_count = 0
    while True:
        # Read the current frame
        ret, frame = video.read()

        # If the frame was not successfully read, the video has ended
        if not ret:
            break

        # Save the frame as an image
        output_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(output_path, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video file
    video.release()

# Usage example
video_path = "JMT_DelDOT_Sample_Video.mp4"
output_folder = "images_bk"

video_to_images(video_path, output_folder)

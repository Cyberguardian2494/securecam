# modules/webcam.py

import cv2  # OpenCV library for computer vision (used to access the webcam and process images)
import os  # Used to check/create directories for saving images
from datetime import datetime  # For generating timestamped filenames


def open_camera(camera_index=0):
    """
    Initializes and returns the webcam capture object.

    Parameters:
        camera_index (int): Index of the camera (0 is usually the default webcam)

    Returns:
        cap (cv2.VideoCapture): The video capture object
    """
    cap = cv2.VideoCapture(camera_index)  # Try to access the webcam at index 0
    if not cap.isOpened():
        raise IOError("Cannot access the camera")  # Throw an error if webcam fails to open
    return cap


def show_preview_and_capture(cap, save_dir="storage/captured"):
    
    #Displays a live preview window from the webcam.
    #Lets you capture images by pressing the spacebar, and exit with the ESC key.

    #Parameters:
        #cap (cv2.VideoCapture): The video capture object
        #save_dir (str): Path to the folder where captured images should be saved
    

    # Make sure the save directory exists (create it if not)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print("📸 Live preview started — Press SPACE to capture an image, ESC to exit.")

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam (ret is True if it succeeds)
        if not ret:
            print("⚠️ Failed to grab frame from webcam.")
            break

        cv2.imshow("Live Preview", frame)  # Display the current frame in a window

        key = cv2.waitKey(1)  # Wait for a key press (1 ms delay between frames)

        if key % 256 == 27:  # ESC key pressed (ASCII 27)
            print("👋 Exiting preview.")
            break

        elif key % 256 == 32:  # SPACE key pressed (ASCII 32)
            # Generate a filename with a timestamp
            filename = datetime.now().strftime("img_%Y%m%d_%H%M%S.jpg")
            filepath = os.path.join(save_dir, filename)

            # Save the captured frame as an image
            cv2.imwrite(filepath, frame)
            print(f"✅ Image saved as: {filepath}")

def capture_image(save_dir="modules/storage/captured"):
        """
        Captures a single frame from the webcam and saves it to disk without preview.

        Returns:
            filepath (str): Path to the saved image or None if it fails.
        """
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            timestamp = datetime.now().strftime("intruder_%Y%m%d_%H%M%S.jpg")
            os.makedirs(save_dir, exist_ok=True)
            filepath = os.path.join(save_dir, timestamp)
            cv2.imwrite(filepath, frame)
            print(f"📸 Silent snapshot saved: {filepath}")
            return filepath
        else:
            print("❌ Failed to access webcam.")
            return None
    # Cleanup: release the camera and close any OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

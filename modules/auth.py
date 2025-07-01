# modules/auth.py

import modules.emailer as emailer
import modules.hasher as hasher
import modules.logger as logger
from modules import webcam
#import getpass
import os
from datetime import datetime

# Stored username and hashed password
VALID_USERNAME = "admin"
VALID_PASSWORD_HASH = "54d5cb2d332dbdb4850293caae4559ce88b65163f1ea5d4e4b3ac49d772ded14" #original password=asd123
#print(hasher.hash_password("asd123")) #copy the hash and paste above

# Optional: location to log locked-out snapshots
SNAPSHOT_DIR = "storage/captured"

def check_credentials():
    """
    Prompts the user to enter a username and password.
    Allows 3 attempts. On the 3rd failure, captures an image and locks the system.
    """

    attempt = 1
    max_attempts = 3

    while attempt <= max_attempts:
        print(f"\n🔐 Login Attempt {attempt} of {max_attempts}")
        username = input("Username: ")
        #password = getpass.getpass("Password: ")  # Hides password input in terminal
        # TEMPORARY for testing only:
        password = input("Password: ")

        if username == VALID_USERNAME and hasher.hash_password(password) == VALID_PASSWORD_HASH:
            print("✅ Access granted.")
            logger.log_attempt(username, "SUCCESS")
            return True

        else:
            print("❌ Wrong credentials. Try again.")
            logger.log_attempt(username, "FAILED")
            attempt += 1

    # If we reach here, it means 3 failed attempts
    print("\n🚫 Too many failed attempts. You have been locked out.")

    try:
        cap = webcam.open_camera()
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"intruder_{now}.jpg"
        filepath = os.path.join(SNAPSHOT_DIR, filename)
        #print("📸 Capturing intruder image...")
        ret, frame = cap.read()

        if ret:
            if not os.path.exists(SNAPSHOT_DIR):
                os.makedirs(SNAPSHOT_DIR)
            cv2 = webcam.cv2  # Access OpenCV from inside webcam module
            cv2.imwrite(filepath, frame)
            emailer.send_intruder_alert("anson.anson2494@gmail.com", filepath)
            #print(f"📁 Intruder image saved to: {filepath}")
        else:
            print("⚠️ Failed to capture image.")

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"⚠️ Error capturing image: {e}")

    return False  # Login ultimately failed

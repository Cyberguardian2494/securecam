# modules/emailer.py

import smtplib
import os
from email.message import EmailMessage


SENDER_EMAIL = "ansonantony.pbox@gmail.com"
APP_PASSWORD = "qzqjkxtubdgnfrvs"

def send_intruder_alert(recipient_email: str, image_path: str):
    """
    Sends an email alert with an attached intruder image.

    Args:
        recipient_email (str): Where to send the alert
        image_path (str): Full path to the image to attach
    """
    msg = EmailMessage()
    msg['Subject'] = "🚨 SecureCam Alert: Failed Login Detected"
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content("A failed login attempt was detected. See attached image.")

    try:
        # Attach the image
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            img_name = os.path.basename(image_path)
            msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename=img_name)

        # Send the message via Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            #print("📤 Intruder alert sent!")

    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")

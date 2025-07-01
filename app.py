from modules import emailer, logger
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/submit-login', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    image_data = request.form.get('image_data')

    print(f"Login attempt: {username}")
    VALID_USERNAME = "admin"
    VALID_PASSWORD = "asd123"
    login_success = (username == VALID_USERNAME and password == VALID_PASSWORD)
    # Decode the base64 image
    try:
        import base64, re, os
        from datetime import datetime

        match = re.search(r"data:image\/jpeg;base64,(.*)", image_data)
        if match:
            img_bytes = base64.b64decode(match.group(1))

            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"intruder_{now}.jpg"
            filepath = os.path.join("storage", "captured", filename)
            os.makedirs("captured", exist_ok=True)

            with open(filepath, 'wb') as f:
                f.write(img_bytes)

            print(f"📸 Saved captured image to: {filepath}")
            # Send email alert
            #recipient = "anson.anson2494@gmail.com"  # Or import from config.py later
            #emailer.send_intruder_alert(recipient, filepath)
            # Log the attempt
            #logger.log_attempt(username=username, success=login_success, image_path=filepath)
        else:
            print("⚠️ Could not parse image data.")

    except Exception as e:
        print(f"❌ Error saving image: {e}")
    try:
        if filepath:
            logger.log_attempt(username=username, success=login_success, image_path=filepath)
            if not login_success:
                recipient = "your@email.com"  # Replace this
                emailer.send_intruder_alert(recipient, filepath)
    except Exception as e:
        print(f"⚠️ Logger/emailer error: {e}")
    return "Login submitted."

if __name__ == '__main__':
    app.run(debug=True)

# 🔐 SecureCam Desktop

**SecureCam Desktop** is a lightweight security login system for personal or shared computers. It tracks login attempts, captures intruder photos after multiple failures, and stores logs securely. Built in Python, it's modular and ready to scale with GUI or web components in future releases.

## ✨ Features

- ✅ Secure credential check using password hashing (SHA-256)
- 🕵️ Lockout after 3 failed login attempts
- 📸 Webcam photo capture of intruder after lockout
- 📝 Detailed log file with timestamp, status, and optional image path
- 🗃️ Modular structure (logger, webcam, hashing)
- 💡 Designed to extend with GUI or email alerts

## 🧠 How It Works

1. User runs `main.py`
2. Enters a username and password
3. If login fails 3 times:
   - Webcam silently captures a photo
   - An entry is logged to `access_log.txt`
   - The intruder image is stored in `modules/storage/captured/`

## 🛠️ Requirements

- Python 3.8+
- OpenCV

Install dependencies:

```bash
pip install -r requirements.txt

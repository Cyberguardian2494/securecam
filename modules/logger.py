# modules/logger.py

import os
from datetime import datetime

# Set the log directory and file path
# Always base the path from the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(PROJECT_ROOT, "storage", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "access_log.txt")

#LOG_DIR = "storage/logs"
#LOG_FILE = os.path.join(LOG_DIR, "access_log.txt")

def log_attempt(username: str, status: str):
    """
    Logs a login attempt with timestamp, username, and result.

    Args:
        username (str): The entered username
        status (str): Result of the attempt — 'SUCCESS' or 'FAILED'
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Username: {username} | Status: {status}\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

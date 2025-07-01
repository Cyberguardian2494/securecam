import os
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, Text, END, WORD, BOTH
from modules import hasher
from modules import webcam
from modules import logger

# Configurable credentials
VALID_USERNAME = "admin"
VALID_PASSWORD_HASH = hasher.hash_password("asd123")

# Track login attempts
attempts = 0

def check_credentials():
    global attempts
    username = username_entry.get()
    password = password_entry.get()

    if attempts >= 3:
        update_message("Too many failed attempts. You have been locked out", "red")
        return
    success = (username == VALID_USERNAME and hasher.hash_password(password) == VALID_PASSWORD_HASH)

    if success:
        update_message("Access granted", "green")
        logger.log_attempt(username, success=True, image_path=None)
    #if username == VALID_USERNAME and hasher.hash_password(password) == VALID_PASSWORD_HASH:
        #update_message("Access granted", "green")
    else:
        attempts += 1
        if attempts == 3:
            update_message("Too many failed attempts. You have been locked out", "red")
            image_path = webcam.capture_image()
            logger.log_attempt(username, success=False, image_path=image_path)
        else:
            update_message("Wrong credentials. Try again", "red")
            logger.log_attempt(username, success=False, image_path=None)
def update_message(text, color):
    message_label.config(text=text, fg=color)
def show_logs():
    log_path = os.path.join("modules", "storage", "logs", "access_log.txt")

    if not os.path.exists(log_path):
        messagebox.showinfo("Log Viewer", "No logs found.")
        return

    with open(log_path, 'r') as file:
        log_content = file.read()

    log_window = Toplevel(root)
    log_window.title("Access Log")
    log_window.geometry("500x300")

    text_area = Text(log_window, wrap=WORD)
    text_area.insert(END, log_content)
    text_area.config(state="disabled")
    text_area.pack(expand=True, fill=BOTH)
# GUI setup
root = tk.Tk()
root.title("SecureCam Login")
root.geometry("300x180")
root.resizable(False, False)

# Username
tk.Label(root, text="Username:").pack(pady=(10, 0))
username_entry = tk.Entry(root)
username_entry.pack()

# Password
tk.Label(root, text="Password:").pack(pady=(10, 0))
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=check_credentials).pack(pady=10)

#view logs button
tk.Button(root, text="📂 View Logs", command=show_logs).pack(pady=(0, 10))

# Message output
message_label = tk.Label(root, text="", font=("Helvetica", 10, "bold"))
message_label.pack()

root.mainloop()
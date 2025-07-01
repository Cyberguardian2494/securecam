from modules import webcam, auth

def main():
    if auth.check_credentials():
        #cap = webcam.open_camera()
        #webcam.show_preview_and_capture(cap)
        pass
if __name__ == "__main__":
    main()

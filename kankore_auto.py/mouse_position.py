import pyautogui
import time
import sys

def get_mouse_position():
    return pyautogui.position()

def main():
    while True:
        x, y = get_mouse_position()
        print(f"Mouse Position: ({x}, {y})")
        time.sleep(1)

if __name__ == "__main__":
    main()

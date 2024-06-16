import pyautogui
import time

def get_mouse_position():
    while True:
        x, y = pyautogui.position()
        with open('mouse_position.txt', 'w') as file:
            file.write(f"{x},{y}")
        time.sleep(1)

if __name__ == "__main__":
    get_mouse_position()

import sys
import pyautogui

def messagePrint(message):
    """
    指定されたメッセージを標準出力に書き込み、メッセージ長を一定に保つ。
    Args:
        message (str): 表示するメッセージ。
    """
    # メッセージを100文字にフォーマット
    formatted_message = f"{message:<100}"
    sys.stdout.write(f"\r{formatted_message}")
    sys.stdout.flush()

def moveAndClick(x, y, button='left', clicks=1):
    """
    指定された座標にマウスを移動し、指定されたボタンでクリックする。
    Args:
        x (int): X座標。
        y (int): Y座標。
        button (str, optional): クリックするマウスボタン（'left'、'right'）。デフォルトは 'left'。
        clicks (int, optional): クリック回数。デフォルトは 1。
    """
    pyautogui.moveTo(x, y)
    pyautogui.click(button=button, clicks=clicks)

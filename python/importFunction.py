import sys
import pyautogui

# messageを引数に取り標準出力を書き換えながら表示していく関数
def messagePrint(message):
    # メッセージを受け取ってパディングする
    messageLength = len(message)
    # 100 - メッセージの長さで確実に上書きできるように修正
    spaceToAdd = 100 - messageLength
    if spaceToAdd > 0:
        message += ' ' * spaceToAdd
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

# x座標とy座標を引数にとり移動した直後にクリックをする関数
def moveAndclick(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
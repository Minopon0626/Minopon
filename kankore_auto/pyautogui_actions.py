import pyautogui
import time

def perform_actions_a():
    """
    タイマーAが開始されたときの動作を定義
    例: 画面の特定の位置をクリックしたり、キーボード操作をする
    """
    print("タイマーA開始時の動作を実行中...")
    # 例として、100, 200の位置をクリック
    pyautogui.click(x=100, y=200)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーA開始中', interval=0.25)

def perform_actions_b():
    """
    タイマーBが開始されたときの動作を定義
    """
    print("タイマーB開始時の動作を実行中...")
    # 例として、200, 300の位置をクリック
    pyautogui.click(x=200, y=300)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーB開始中', interval=0.25)

def perform_actions_c():
    """
    タイマーCが開始されたときの動作を定義
    """
    print("タイマーC開始時の動作を実行中...")
    # 例として、300, 400の位置をクリック
    pyautogui.click(x=300, y=400)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーC開始中', interval=0.25)

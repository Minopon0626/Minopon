import pyautogui
import time

def perform_actions_a():
    """
    タイマーAが開始されたときの動作を定義
    例: 画面の特定の位置をクリックしたり、キーボード操作をする
    """
    print("タイマーA開始時の動作を実行中...")
    # 例として、100, 200の位置をクリック
    #pyautogui.click(x=100, y=200)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーA開始中', interval=0.25)

def perform_actions_b():
    """
    タイマーBが開始されたときの動作を定義
    """
    print("タイマーB開始時の動作を実行中...")
    # 例として、200, 300の位置をクリック
    #pyautogui.click(x=200, y=300)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーB開始中', interval=0.25)

def perform_actions_c():
    """
    タイマーCが開始されたときの動作を定義
    """
    print("タイマーC開始時の動作を実行中...")
    # 例として、300, 400の位置をクリック
    #pyautogui.click(x=300, y=400)
    time.sleep(1)
    # 他の動作を追加
    pyautogui.write('タイマーC開始中', interval=0.25)

def expedition_receive(app):
    """
    遠征受取の操作: x=1100, y=230の座標をクリックし、"現在すること"を更新
    """
    # 現在することの部分を更新
    app.update_display(current_task="遠征受取中")

    # 遠征受取のクリック操作
    pyautogui.click(x=1100, y=230)
    time.sleep(5)
    pyautogui.click(x=1100, y=230)
    time.sleep(5)
    pyautogui.click(x=1100, y=230)

def open_formation(app):
    """
    編成を開く操作: x=300, y=360の座標をクリックし、"現在すること"を更新
    """
    app.update_display(current_task="編成を開く中")
    pyautogui.click(x=300, y=360)

def supply(app):
    """
    補給をする操作:
    1. x=100, y=490をクリック
    2. 4秒の遅延
    3. x=180, y=340をクリック
    4. 4秒の遅延
    5. x=260, y=340をクリック
    6. 4秒の遅延
    7. x=310, y=340をクリック
    8. 4秒の遅延
    9. x=355, y=340をクリック
    10. 4秒の遅延
    11. 母港に戻る
    """
    app.update_display(current_task="補給中")
    
    # 最初のクリック
    pyautogui.click(x=100, y=490)
    time.sleep(4)
    
    # 2番目のクリック
    pyautogui.click(x=180, y=340)
    time.sleep(4)
    
    # 3番目のクリック
    pyautogui.click(x=260, y=340)
    time.sleep(4)
    
    pyautogui.click(x=180, y=340)
    time.sleep(4)
    
    # 4番目のクリック
    pyautogui.click(x=310, y=340)
    time.sleep(4)
    
    pyautogui.click(x=180, y=340)
    time.sleep(4)
    
    # 5番目のクリック
    pyautogui.click(x=355, y=340)
    time.sleep(4)
    
    pyautogui.click(x=180, y=340)
    time.sleep(4)
    
    # 母港に戻る
    return_to_port(app)

def return_to_port(app):
    """
    母港に戻る操作: x=65, y=230の座標をクリックし、"現在すること"を更新
    """
    app.update_display(current_task="母港に戻る中")
    pyautogui.click(x=65, y=230)
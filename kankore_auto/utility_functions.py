import pyautogui

def delayed_click(root, x, y):
    """
    Tkinterのafterメソッドのみを利用して、指定した座標 (x, y) に
    3秒後にマウスを移動させ、さらに2秒後にクリックする関数。
    
    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param x: クリックするX座標
    :param y: クリックするY座標
    """
    # 3秒後にマウスを移動
    root.after(3000, lambda: pyautogui.moveTo(x, y))
    print(f"マウスを移動予定 - 座標 ({x}, {y})")

    # さらに2秒後にクリック
    root.after(5000, lambda: pyautogui.click(x, y))
    print(f"クリック予定 - 座標 ({x}, {y})")

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
    root.after(3000, lambda: [
        pyautogui.moveTo(x, y),  # マウスを移動させて
        print(f"マウスを移動しました - 座標 ({x}, {y})"),

        # さらに2秒後にクリック
        root.after(2000, lambda: [
            pyautogui.click(x, y),
            print(f"クリック完了 - 座標 ({x}, {y})")
        ])
    ])


def delayed_update(root, label, delay_ms, new_text):
    """
    Tkinterのafterメソッドを使用して、指定された時間（ミリ秒）の遅延後に
    ラベルの表示内容を変更する関数。

    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param label: 表示内容を変更するTkinterのラベル
    :param delay_ms: 遅延時間（ミリ秒）
    :param new_text: 遅延後に表示するテキスト

    使用例:
    delayed_update(root, current_task_label, 5000, "ボーキ完了")

    また遅延秒数を0とすると即座に反映される
    """
    root.after(delay_ms, lambda: label.config(text=new_text))
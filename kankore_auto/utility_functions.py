import pyautogui
import cv2
import numpy as np
import os

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

def delayed_drag_and_drop(root, start_x, start_y, end_x, end_y, duration=1):
    """
    Tkinterのafterメソッドを使用して、指定した座標 (start_x, start_y) から
    (end_x, end_y) にドラッグ・アンド・ドロップを行う関数。
    
    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param start_x: ドラッグを開始するX座標
    :param start_y: ドラッグを開始するY座標
    :param end_x: ドロップを行うX座標
    :param end_y: ドロップを行うY座標
    :param duration: マウス移動にかかる時間（秒）
    """
    # 3秒後にマウスをドラッグ開始位置に移動し、ドラッグを開始
    def start_drag():
        pyautogui.moveTo(start_x, start_y, duration=0.5)  # 開始位置に移動
        print(f"ドラッグ開始位置に移動 - 座標 ({start_x}, {start_y})")
        pyautogui.mouseDown()  # マウスボタンを押す
        print("マウスダウン")

    # さらに2秒後にドラッグを実行し、ドロップ
    def drop():
        pyautogui.moveTo(end_x, end_y, duration=duration)  # ドロップ位置にゆっくり移動
        print(f"ドラッグ終了位置に移動 - 座標 ({end_x}, {end_y})")
        pyautogui.mouseUp()  # マウスボタンを離す
        print("マウスアップ - ドロップ完了")

    # 3秒後にドラッグを開始
    root.after(3000, start_drag)

    # ドラッグ後に2秒遅延してドロップ
    root.after(5000, drop)

def compare_screen_to_image(top_left_x, top_left_y, button_name, threshold=0.8):
    """
    特定のボタンに対応する子ディレクトリから画像を取得し、左上の座標からその画像サイズ分の画面範囲を比較する関数。
    
    :param top_left_x: スクリーンショットを取得する左上のX座標
    :param top_left_y: スクリーンショットを取得する左上のY座標
    :param button_name: 押されたボタン名に基づき対応する子ディレクトリを参照
    :param threshold: 類似度の閾値（0〜1、デフォルトは0.8）
    :return: 類似度が閾値以上であればTrue、そうでなければFalse
    """
    
    # ディレクトリ名を固定
    image_directory = "comparison_image"
    
    # 押されたボタン名に基づいて、対応する子ディレクトリのパスを取得
    subdirectory = os.path.join(image_directory, button_name)
    
    # 子ディレクトリ内の画像ファイルを取得（1つの画像ファイルのみを使用する前提）
    image_files = [f for f in os.listdir(subdirectory) if os.path.isfile(os.path.join(subdirectory, f))]
    
    if not image_files:
        raise FileNotFoundError(f"ディレクトリ '{subdirectory}' に画像ファイルが見つかりません")
    
    # 比較用画像のファイルパスを取得
    image_path = os.path.join(subdirectory, image_files[0])
    
    # 比較用の画像を読み込む
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # 画像サイズを取得
    template_height, template_width = template.shape[:2]

    # 指定した範囲のスクリーンショットを取得（画像のサイズに基づく）
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, template_width, template_height))
    
    # スクリーンショットをOpenCV形式に変換
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    # テンプレートマッチングを使用して類似度を計算
    result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
    
    # 最も高い類似度を取得
    max_val = np.max(result)
    
    # 類似度が閾値以上かどうかを判定
    print("類似度:", max_val)
    return max_val >= threshold

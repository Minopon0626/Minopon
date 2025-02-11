import pyautogui
import cv2
import numpy as np
import os
import time

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

def compare_screen_to_image(top_left_x, top_left_y, button_name, image_file_name, threshold=0.8):
    """
    特定のボタンに対応する子ディレクトリから指定された画像を取得し、左上の座標からその画像サイズ分の画面範囲を比較する関数。
    
    :param top_left_x: スクリーンショットを取得する左上のX座標
    :param top_left_y: スクリーンショットを取得する左上のY座標
    :param button_name: 押されたボタン名に基づき対応する子ディレクトリを参照
    :param image_file_name: 比較する画像のファイル名
    :param threshold: 類似度の閾値（0〜1、デフォルトは0.8）
    :return: 類似度が閾値以上であればTrue、そうでなければFalse
    """
    
    # ディレクトリ名を固定
    image_directory = "comparison_image"
    
    # 押されたボタン名に基づいて、対応する子ディレクトリのパスを取得
    subdirectory = os.path.join(image_directory, button_name)
    
    # 画像ファイルのパスを取得
    image_path = os.path.join(subdirectory, image_file_name)
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"画像ファイル '{image_file_name}' がディレクトリ '{subdirectory}' に見つかりません")
    
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

def timed_compare_and_click(root, top_left_x, top_left_y, button_name, image_file_name, threshold, click_x, click_y):
    """
    compare_screen_to_imageの類似度が引数で指定された値を超え、かつ呼び出されて2秒以上経過した場合にクリック座標をクリック。
    この関数が終了するのは呼び出されてから5秒後。
    
    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param top_left_x: 比較画像の左上X座標
    :param top_left_y: 比較画像の左上Y座標
    :param button_name: 押されたボタンの名前
    :param image_file_name: 比較する画像のファイル名
    :param threshold: 類似度の閾値
    :param click_x: クリックするX座標
    :param click_y: クリックするY座標
    """
    
    start_time = time.time()  # 関数が呼び出された時刻を記録

    def check_similarity():
        # 2秒以上経過しているか確認
        if time.time() - start_time >= 2:
            # compare_screen_to_imageを使用して類似度を確認
            if compare_screen_to_image(top_left_x, top_left_y, button_name, image_file_name, threshold):
                # 類似度が指定された値を超えた場合、クリックを実行
                pyautogui.click(click_x, click_y)
                print(f"クリックしました: 座標 ({click_x}, {click_y})")
        
        # 5秒後に終了
        if time.time() - start_time < 5:
            root.after(10, check_similarity)
        else:
            print("関数終了（5秒経過）")

    # 最初のチェックを開始（非同期）
    root.after(10, check_similarity)

def return_to_home_port(root, current_task_label):
    """
    母港に戻る一連の処理を行う関数。
    ラベルを「母港に戻る」に更新し、指定された座標でクリックする。

    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param current_task_label: ラベルを更新するTkinterラベル
    """
    # 「母港に戻る」と表示を更新し、指定座標でクリック
    delayed_update(root, current_task_label, 0, "母港に戻る")
    delayed_click(root, 60, 210)

def supply_fleets(root, current_task_label):
    """
    補給処理を行う関数。
    順番に遅延させて艦隊の補給を行い、最後に母港に戻る。

    :param root: Tkinterのrootウィンドウ（afterメソッドを利用するため）
    :param current_task_label: ラベルを更新するTkinterラベル
    """
    # 補給画面への移動
    delayed_click(root, 120, 500)
    delayed_update(root, current_task_label, 0, "母港から補給画面へ移動")

    # 5秒後: 第一艦隊の補給
    root.after(5000, lambda: (
        delayed_update(root, current_task_label, 0, "補給画面で第一艦隊を補給"),
        delayed_click(root, 170, 340)
    ))

    # 10秒後: 第二艦隊に切り替え
    root.after(10000, lambda: (
        delayed_update(root, current_task_label, 0, "第二艦隊に切り替え"),
        delayed_click(root, 260, 340)
    ))

    # 15秒後: 第二艦隊の補給
    root.after(15000, lambda: (
        delayed_update(root, current_task_label, 0, "補給画面で第二艦隊を補給"),
        delayed_click(root, 170, 340)
    ))

    # 20秒後: 第三艦隊に切り替え
    root.after(20000, lambda: (
        delayed_update(root, current_task_label, 0, "第三艦隊に切り替え"),
        delayed_click(root, 310, 340)
    ))

    # 25秒後: 第三艦隊の補給
    root.after(25000, lambda: (
        delayed_update(root, current_task_label, 0, "補給画面で第三艦隊を補給"),
        delayed_click(root, 170, 340)
    ))

    # 30秒後: 第四艦隊に切り替え
    root.after(30000, lambda: (
        delayed_update(root, current_task_label, 0, "第四艦隊に切り替え"),
        delayed_click(root, 355, 340)
    ))

    # 35秒後: 第四艦隊の補給
    root.after(35000, lambda: (
        delayed_update(root, current_task_label, 0, "補給画面で第四艦隊を補給"),
        delayed_click(root, 170, 340)
    ))

    # 40秒後: 母港に戻る
    root.after(40000, lambda: (
        return_to_home_port(root, current_task_label)
    ))

def delayed_click_with_countdown(root, label, x, y, display_text):
    """
    最初に delayed_click を呼び出し、その後1秒ごとに表示を変更する関数。

    :param root: Tkinterのrootウィンドウ
    :param label: ラベルを更新するTkinterのラベル
    :param x: クリックするX座標
    :param y: クリックするY座標
    :param display_text: 表示する基本のテキスト
    """
    # 最初に delayed_click を呼び出す
    delayed_click(root, x, y)

    def update_display(remaining_time):
        if remaining_time > 0:
            delayed_update(root, label, 0, f"「{display_text}」{remaining_time}秒後クリック")
            root.after(1000, lambda: update_display(remaining_time - 1))
        else:
            delayed_update(root, label, 0, f"「{display_text}」クリック完了")

    # 5秒からカウントダウンを開始
    update_display(5)

def delayed_drag_and_drop_with_countdown(root, label, start_x, start_y, end_x, end_y, display_text):
    """
    最初に delayed_drag_and_drop を呼び出し、その後1秒ごとに表示を変更する関数。

    :param root: Tkinterのrootウィンドウ
    :param label: ラベルを更新するTkinterのラベル
    :param start_x: ドラッグ開始のX座標
    :param start_y: ドラッグ開始のY座標
    :param end_x: ドラッグ終了のX座標
    :param end_y: ドラッグ終了のY座標
    :param display_text: 表示する基本のテキスト
    """
    # 最初に delayed_drag_and_drop を呼び出す
    delayed_drag_and_drop(root, start_x, start_y, end_x, end_y)

    def update_display(remaining_time):
        if remaining_time > 0:
            delayed_update(root, label, 0, f"「{display_text}」{remaining_time}秒後ドラッグ＆ドロップ")
            root.after(1000, lambda: update_display(remaining_time - 1))
        else:
            delayed_update(root, label, 0, f"「{display_text}」ドラッグ＆ドロップ完了")

    # 5秒からカウントダウンを開始
    update_display(5)

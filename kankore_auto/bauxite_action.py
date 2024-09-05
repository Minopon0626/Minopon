import time
import pyautogui
from pyautogui_actions import supply, open_formation, return_to_port
import os
import cv2
import numpy as np


def bauxite_action(app):
    # ボーキボタンがクリックされたときの処理を記述
    app.update_display(current_task="ボーキ実行中")
    
    """
    ボーキボタンが押されたときに実行される動作:
    1. 補給を実行
    2. 編成を開く
    3. ドラッグ・アンド・ドロップ (x = 560, y = 410 から x = 1060, y = 590 へ) : 旗艦を3番艦に変更
    4. 母港に戻る
    5. x = 300, y = 550 をクリック : 出撃をクリック
    6. 4秒待機
    7. x = 340, y = 490 をクリック : 出撃をクリック
    8. 4秒待機
    9. x = 510, y = 840 をクリック : 海域を南西海域に変更
    10. 4秒待機
    11. x = 1010, y = 700 をクリック : 出撃海域をクリック
    """
    # 補給を実行
    supply(app)
    
    time.sleep(4)
    
    # 編成を開く
    open_formation(app)
    
    time.sleep(4)
    
    # ドラッグ・アンド・ドロップ操作
    pyautogui.moveTo(560, 410)
    pyautogui.dragTo(1060, 590, duration=1)
    
    time.sleep(4)
    
    # 母港に戻る
    return_to_port(app)
    
    time.sleep(4)
    
    # x = 300, y = 550 をクリック
    # 母港から出撃を選択
    pyautogui.click(x=300, y=550)
    time.sleep(4)  # 4秒待機
    
    # x = 340, y = 490 をクリック
    # 出撃から出撃を選択
    pyautogui.click(x=340, y=490)
    time.sleep(4)  # 4秒待機
    
    # x = 510, y = 840 をクリック
    # 南西海域を選択
    pyautogui.click(x=510, y=840)
    time.sleep(4)  # 4秒待機
    
    # x = 1010, y = 700 をクリック
    # 7-4をクリック
    pyautogui.click(x=1010, y=700)
    time.sleep(4)  # 4秒待機
    
    # 決定をクリック
    pyautogui.click(x=1010, y=840)
    time.sleep(4)  # 4秒待機
    
    # 出撃決定をクリック
    pyautogui.click(x=920, y=830)
    time.sleep(4)  # 4秒待機
    
    """
    出撃開始
    """
    time.sleep(5)
    
    # 羅針盤を回す
    pyautogui.click(x=1100, y=230)
    time.sleep(5)
    
    """
    戦闘Cマス
    """
    
    if wait_for_image('tuigeki_or_tettai.png', threshold=0.9, timeout=120):
        pyautogui.click(x=440, y=520)
    time.sleep(5)
    
    """
    一戦目の追撃不要部分まで完成
    
    """
    
    # いずれかのタイマーが終了したかどうかを確認し、終了しているタイマーを起動
    if not app.timer.timer_running_a or not app.timer.timer_running_b or not app.timer.timer_running_c:
        app.update_display(current_task="いずれかのタイマーが終了")

        # 終了しているタイマーを再起動
        if not app.timer.timer_running_a:
            print("タイマーAが終了しました。再起動します。")
            app.start_timer_a()  # タイマーAを開始

        if not app.timer.timer_running_b:
            print("タイマーBが終了しました。再起動します。")
            app.start_timer_b()  # タイマーBを開始

        if not app.timer.timer_running_c:
            print("タイマーCが終了しました。再起動します。")
            app.start_timer_c()  # タイマーCを開始

"""
REGION_X = 0  # x座標の開始位置
    REGION_Y = 160  # y座標の開始位置
    REGION_WIDTH = 1200  # 領域の幅
    REGION_HEIGHT = 720  # 領域の高さ
    """

def wait_for_image(image_filename, threshold=0.9, timeout=30):
    """
    指定された画像が、指定された画面領域内に現れるまで待機します。
    
    :param image_filename: 比較したい画像ファイル名（子ディレクトリ 'comparison_image' 内）
    :param threshold: 類似度のしきい値（0〜1）
    :param timeout: タイムアウトまでの最大秒数
    :return: True: 画像が見つかった, False: タイムアウト
    """

    # 現在のディレクトリを取得し、'comparison_image'ディレクトリ内の画像パスを設定
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_directory = os.path.join(current_directory, "comparison_image")
    template_path = os.path.join(image_directory, image_filename)
    
    # 定数で領域を指定
    REGION_X = 0  # x座標の開始位置
    REGION_Y = 160  # y座標の開始位置
    REGION_WIDTH = 1200  # 領域の幅
    REGION_HEIGHT = 720  # 領域の高さ

    start_time = time.time()

    # テンプレート画像を読み込む（カラー画像として）
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    if template is None:
        print(f"画像 '{template_path}' が見つかりません。")
        return False

    while True:
        # 指定した領域のスクリーンショットを取得
        screenshot = pyautogui.screenshot(region=(REGION_X, REGION_Y, REGION_WIDTH, REGION_HEIGHT))
        
        # スクリーンショットをOpenCV用に変換
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # テンプレートマッチングを行う
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 最大類似度を取得
        _, max_val, _, _ = cv2.minMaxLoc(res)

        # 類似度がしきい値を超えたら終了
        if max_val >= threshold:
            print(f"画像が{max_val:.2f}の類似度で一致しました。")
            return True

        # タイムアウトチェック
        if time.time() - start_time > timeout:
            print("画像を見つけるタイムアウトです。")
            return False

        # 短時間待機して再試行
        time.sleep(1)
import pyautogui
import cv2
import numpy as np
import os

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


compare_screen_to_image(0, 160, "bauxite", 0.8)
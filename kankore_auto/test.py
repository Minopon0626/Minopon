import cv2
import pytesseract
import pyautogui
import os
from PIL import Image

# Tesseract OCR のパスを設定 (例: Windowsの場合)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# スクリーンショットを指定範囲で撮影
def capture_screenshot(x, y, w, h):
    screenshot = pyautogui.screenshot(region=(x, y, w, h))  # スクリーンショットの範囲を指定
    screenshot = screenshot.convert('RGB')  # Pillow 形式でスクリーンショットを保存
    return screenshot

# 認識対象範囲の数字のみを認識して座標を記録し、結果を保存する
def recognize_numbers_in_region_from_screenshot(x, y, w, h, output_dir='recognized_text'):
    recognized_numbers_info = []

    # スクリーンショットを撮影
    screenshot = capture_screenshot(x, y, w, h)
    
    # 一時的なファイルに保存してOpenCVで読み込む
    temp_image_path = 'temp_screenshot.png'
    screenshot.save(temp_image_path)
    
    # スクリーンショットをOpenCV形式で読み込む
    img = cv2.imread(temp_image_path)

    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 画像から数字のみを認識 (config='digits' オプションを使用)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)

    # 認識結果を元画像に描画
    for i, text in enumerate(data['text']):
        if text.strip().isdigit():  # 数字かどうか確認
            x_coord = data['left'][i] + x  # スクリーン全体の座標に変換
            y_coord = data['top'][i] + y
            w_coord = data['width'][i]
            h_coord = data['height'][i]
            
            # 認識された数字を囲む四角形を描画
            cv2.rectangle(img, (data['left'][i], data['top'][i]), 
                          (data['left'][i] + data['width'][i], data['top'][i] + data['height'][i]), 
                          (0, 255, 0), 2)
            
            # 認識した数字の情報を記録
            recognized_numbers_info.append({
                'text': text,
                'x': x_coord,
                'y': y_coord,
                'width': w_coord,
                'height': h_coord
            })

    # 認識した文字を囲った画像を保存
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_image_path = os.path.join(output_dir, 'recognized_screenshot.png')
    cv2.imwrite(output_image_path, img)

    # 一時ファイルを削除
    os.remove(temp_image_path)

    return recognized_numbers_info

# 例: 中央左部分にある"45"付近の範囲を指定 (x, y, w, h の値を調整)
x, y, w, h = 200, 400, 35, 360  # "45" があると思われるスクリーン上の座標とサイズを指定
recognized_info = recognize_numbers_in_region_from_screenshot(x, y, w, h)

# 認識した結果を出力
for info in recognized_info:
    print(f"Text: {info['text']}, Coordinates: ({info['x']}, {info['y']}), Size: ({info['width']}x{info['height']})")

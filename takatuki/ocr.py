import pytesseract
from PIL import Image

# Tesseractのインストールパスを指定（必要な場合）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def perform_ocr(image: Image.Image) -> str:
    # 画像が正しく受け取られているか確認
    image.show()  # デバッグ用: 画像を表示

    # OCR処理を実行
    try:
        text = pytesseract.image_to_string(image)
        print("OCR認識結果:", text)  # デバッグ用: 結果を表示
        return text
    except Exception as e:
        print("OCR処理中にエラーが発生しました:", str(e))
        return ""

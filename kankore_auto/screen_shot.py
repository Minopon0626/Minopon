from PIL import ImageGrab

def take_screenshot(left, top, width, height, save_path="screenshot.png"):
    # 左上の座標 (left, top) と指定した範囲 (width, height) を使ってスクリーンショットを撮影
    right = left + width
    bottom = top + height

    # 画面の指定した範囲をキャプチャ
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # 画像を保存
    screenshot.save(save_path)

    print(f"スクリーンショットを保存しました: {save_path}")

if __name__ == "__main__":
    # ユーザーに入力を求める
    left = int(input("左上のx座標を入力してください: "))
    top = int(input("左上のy座標を入力してください: "))
    width = int(input("幅を入力してください: "))
    height = int(input("高さを入力してください: "))
    save_path = input("保存ファイル名を入力してください（デフォルト: screenshot.png）: ") or "screenshot.png"

    # スクリーンショットを撮影
    take_screenshot(left, top, width, height, save_path)

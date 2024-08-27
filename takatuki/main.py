import os
from directory import ensure_directory

def display_image_with_selection(picture_dir):
    ensure_directory(picture_dir)  # ディレクトリが存在しない場合は作成
    from app import ImageSelectorApp  # Tkinterアプリケーションをインポート
    
    import tkinter as tk
    root = tk.Tk()
    root.title("画像表示と範囲指定")
    
    app = ImageSelectorApp(root, picture_dir)
    root.mainloop()

def main():
    picture_dir = "picture"  # 画像ディレクトリのパス
    display_image_with_selection(picture_dir)

if __name__ == "__main__":
    main()

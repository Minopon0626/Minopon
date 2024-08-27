import os
from tkinter import messagebox

def check_or_create_picture_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    picture_dir = os.path.join(current_dir, 'picture')

    if not os.path.isdir(picture_dir):
        os.makedirs(picture_dir)
        messagebox.showinfo("情報", "pictureディレクトリが作成されました。画像ファイルを追加してください。")
        return picture_dir

    return picture_dir

def ensure_directory(directory):
    """指定したディレクトリが存在しない場合は作成する関数"""
    if not os.path.exists(directory):
        os.makedirs(directory)

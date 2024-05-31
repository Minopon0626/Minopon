import tkinter as tk
from PIL import Image, ImageTk

"""
画像の上でマウスカーソルを動かすと、その座標を表示するプログラム
ウィンドウの名前が座標を表示するようになっている
"""

def motion(event):
    x, y = event.x, event.y
    window.title(f'Mouse Position: x={x}, y={y}')

# Tkinterウィンドウを作成
window = tk.Tk()
window.title('Image with Mouse Position')

# 画像を開いて表示
img = Image.open('screenshot.png')
photo = ImageTk.PhotoImage(img)
label = tk.Label(window, image=photo)
label.pack()

# マウスカーソルの動きに応じて座標を更新
label.bind('<Motion>', motion)

# ウィンドウを表示
window.mainloop()

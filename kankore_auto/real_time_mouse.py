import tkinter as tk
from pynput.mouse import Listener

class MouseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("リアルタイムマウス座標表示")
        
        self.label = tk.Label(root, text="マウス座標: (0, 0)", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.start_mouse_listener()

    def update_label(self, x, y):
        # 座標ラベルを更新
        self.label.config(text=f"マウス座標: ({x}, {y})")

    def start_mouse_listener(self):
        # マウスの位置を検知するリスナーを開始
        self.listener = Listener(on_move=self.on_move)
        self.listener.start()

    def on_move(self, x, y):
        # マウスが動いた時に呼ばれる
        self.update_label(x, y)

    def on_close(self):
        # GUIが閉じられた時にリスナーを停止
        self.listener.stop()
        self.root.quit()

# Tkinterウィンドウの設定
root = tk.Tk()
app = MouseTracker(root)

# ウィンドウを閉じる処理を設定
root.protocol("WM_DELETE_WINDOW", app.on_close)

# Tkinterのメインループを開始
root.mainloop()

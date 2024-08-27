import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
from ocr import perform_ocr  # 文字認識処理を別ファイルからインポート

class ImageSelectorApp:
    def __init__(self, root, image_dir):
        self.root = root
        self.image_dir = image_dir
        self.image_files = []
        self.current_image_index = 0
        self.original_image = None
        self.tk_image = None
        self.selection = None
        self.scaled_image = None
        self.cropped_image = None  # 切り抜いた画像を保存する変数

        self.root.title("画像選択アプリ")
        self.root.geometry("1200x800")  # アプリケーションのサイズ

        # キャンバスとスクロールバーの作成
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.scroll_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # 切り抜き後画像を表示するためのキャンバス
        self.right_canvas = tk.Canvas(root, bg="lightgrey")
        self.right_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ボタンの作成
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.previous_button = tk.Button(button_frame, text="前の画像", command=self.previous_image)
        self.previous_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(button_frame, text="次の画像", command=self.next_image)
        self.next_button.pack(side=tk.LEFT)
        self.confirm_button = tk.Button(button_frame, text="範囲確定", command=self.confirm_selection)
        self.confirm_button.pack(side=tk.LEFT)
        self.clear_button = tk.Button(button_frame, text="範囲クリア", command=self.clear_selection)
        self.clear_button.pack(side=tk.LEFT)
        self.ocr_button = tk.Button(button_frame, text="文字認識", command=self.perform_ocr)
        self.ocr_button.pack(side=tk.LEFT)

        self.load_image_files()
        if self.image_files:
            self.load_image(self.image_files[self.current_image_index])

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def load_image_files(self):
        import os
        for file_name in os.listdir(self.image_dir):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                self.image_files.append(os.path.join(self.image_dir, file_name))

    def load_image(self, image_path):
        self.original_image = Image.open(image_path)
        self.update_image_display()

    def update_image_display(self):
        if self.original_image:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image_width, image_height = self.original_image.size

            # スケーリングファクターの計算
            scaling_factor = min(canvas_width / image_width, canvas_height / image_height)
            new_size = (int(image_width * scaling_factor), int(image_height * scaling_factor))

            # 新しいサイズが正の値であることを確認
            if new_size[0] > 0 and new_size[1] > 0:
                self.scaled_image = self.original_image.resize(new_size, Image.Resampling.LANCZOS)
                self.tk_image = ImageTk.PhotoImage(self.scaled_image)
                self.canvas.delete("all")
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
                self.canvas.config(scrollregion=self.canvas.bbox("all"))
                self.selection = None
            else:
                print("Error: Image size is not valid for scaling.")

    def on_click(self, event):
        self.selection = [event.x, event.y, event.x, event.y]

    def on_drag(self, event):
        if self.selection:
            self.selection[2] = event.x
            self.selection[3] = event.y
            self.update_selection()

    def on_release(self, event):
        if self.selection:
            self.selection[2] = event.x
            self.selection[3] = event.y
            self.update_selection()

    def update_selection(self):
        self.canvas.delete("selection")
        if self.selection:
            self.canvas.create_rectangle(self.selection[0], self.selection[1],
                                         self.selection[2], self.selection[3],
                                         outline="red", tags="selection")

    def clear_selection(self):
        self.selection = None
        self.canvas.delete("selection")

    def confirm_selection(self):
        if self.selection and self.original_image:
            left, top, right, bottom = self.selection
            if left > right:
                left, right = right, left
            if top > bottom:
                top, bottom = bottom, top

            # キャンバス上での座標をスケーリングされた画像の座標に変換
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image_width, image_height = self.original_image.size
            scaled_width, scaled_height = self.scaled_image.size

            left = int(left * image_width / scaled_width)
            right = int(right * image_width / scaled_width)
            top = int(top * image_height / scaled_height)
            bottom = int(bottom * image_height / scaled_height)

            self.cropped_image = self.original_image.crop((left, top, right, bottom))
            self.display_cropped_image(self.cropped_image)
            self.clear_selection()

    def display_cropped_image(self, cropped_image):
        self.right_canvas.delete("all")
        cropped_image_tk = ImageTk.PhotoImage(cropped_image)
        self.right_canvas.create_image(0, 0, anchor=tk.NW, image=cropped_image_tk)
        self.right_canvas.image = cropped_image_tk  # 画像参照を保持するために必要
        self.right_canvas.config(scrollregion=self.right_canvas.bbox("all"))

    def previous_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
            self.load_image(self.image_files[self.current_image_index])

    def next_image(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
            self.load_image(self.image_files[self.current_image_index])

    def perform_ocr(self):
        if self.cropped_image:  # 切り抜いた画像がある場合
            # 切り抜いた画像を表示するデバッグ用ウィンドウを作成
            debug_window = tk.Toplevel(self.root)
            debug_window.title("デバッグ: 切り抜いた画像")
            debug_canvas = tk.Canvas(debug_window, bg="lightgrey")
            debug_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            cropped_image_tk = ImageTk.PhotoImage(self.cropped_image)
            debug_canvas.create_image(0, 0, anchor=tk.NW, image=cropped_image_tk)
            debug_canvas.image = cropped_image_tk  # 画像参照を保持するために必要
            debug_canvas.config(scrollregion=debug_canvas.bbox("all"))

            # OCR処理
            text = perform_ocr(self.cropped_image)  # 切り抜いた画像をOCR処理に渡す
            ocr_window = tk.Toplevel(self.root)
            ocr_window.title("OCR結果")
            text_widget = tk.Text(ocr_window, wrap=tk.WORD, height=10, width=50)
            text_widget.pack(expand=True, fill=tk.BOTH)
            text_widget.insert(tk.END, text)
            text_widget.config(state=tk.DISABLED)
        else:
            print("Error: No cropped image available for OCR.")

def display_image_with_selection(picture_dir):
    root = tk.Tk()
    app = ImageSelectorApp(root, picture_dir)
    root.mainloop()

def main():
    picture_dir = "./picture"  # ここで画像ディレクトリを指定
    display_image_with_selection(picture_dir)

if __name__ == "__main__":
    main()

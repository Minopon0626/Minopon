import tkinter as tk
import time

class InfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("情報表示アプリ")  # ウィンドウのタイトルを設定
        self.root.geometry("400x200")  # ウィンドウのサイズを設定
        self.root.configure(bg="lightgray")  # ウィンドウの背景色を薄いグレーに設定

        # ラベルと値の初期表示内容
        self.current_task_text = "表示内容A"
        self.next_time_text = "表示内容B"
        self.next_click_text = "表示内容C"

        # テーブルの行を作成
        self.row1_label, self.row1_value = self.create_table_row("現在すること", self.current_task_text)
        self.row2_label, self.row2_value = self.create_table_row("次の稼働時間まで", self.next_time_text)
        self.row3_label, self.row3_value = self.create_table_row("次クリックする場所", self.next_click_text)
        
        # 各行を表示
        self.row1_label.grid(row=0, column=0, sticky="nsew")
        self.row1_value.grid(row=0, column=1, sticky="nsew")
        
        self.row2_label.grid(row=1, column=0, sticky="nsew")
        self.row2_value.grid(row=1, column=1, sticky="nsew")
        
        self.row3_label.grid(row=2, column=0, sticky="nsew")
        self.row3_value.grid(row=2, column=1, sticky="nsew")

        # グリッドのカラムのウェイトを設定して、列幅を均等にする
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # グリッドの行のウェイトを設定して、行高さを均等にする
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

    def create_table_row(self, label_text, value_text):
        # 1列目はグレーの背景、2列目は白の背景
        label_frame = tk.Frame(self.root, bg="lightgray", padx=10, pady=5, borderwidth=1, relief="solid")
        label = tk.Label(label_frame, text=label_text, bg="lightgray", font=("Arial", 12))
        label.pack(fill="both", expand=True)

        value_frame = tk.Frame(self.root, bg="white", padx=10, pady=5, borderwidth=1, relief="solid")
        value_label = tk.Label(value_frame, text=value_text, bg="white", font=("Arial", 12))
        value_label.pack(fill="both", expand=True)
        
        return label_frame, value_frame

    def update_display(self, current_task=None, next_time=None, next_click=None):
        # 表示内容を更新する
        if current_task is not None:
            self.current_task_text = current_task
            self.row1_value.winfo_children()[0].config(text=self.current_task_text)
        
        if next_time is not None:
            self.next_time_text = next_time
            self.row2_value.winfo_children()[0].config(text=self.next_time_text)
        
        if next_click is not None:
            self.next_click_text = next_click
            self.row3_value.winfo_children()[0].config(text=self.next_click_text)

def main():
    root = tk.Tk()
    app = InfoApp(root)

    root.mainloop()

    # テスト用の表示更新
    app.update_display(current_task="新しい表示内容A", next_time="新しい表示内容B", next_click="新しい表示内容C")

    time.sleep(1)

    app.update_display(current_task="A", next_time="B", next_click="C")

if __name__ == "__main__":
    main()

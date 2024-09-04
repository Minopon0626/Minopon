import tkinter as tk
from start_action import start_action
from stop_action import stop_action
from timer import Timer
from pyautogui_actions import perform_actions  # pyautogui操作をインポート

class InfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("情報表示アプリ")
        self.root.geometry("400x400")  # ウィンドウの高さを少し増やしました
        self.root.configure(bg="lightgray")

        self.current_task_text = "表示内容A"
        self.next_time_text = "表示内容B"
        self.next_click_text = "表示内容C"

        self.row1_label, self.row1_value = self.create_table_row("現在すること", self.current_task_text)
        self.row2_label, self.row2_value = self.create_table_row("次の稼働時間まで", self.next_time_text)
        self.row3_label, self.row3_value = self.create_table_row("次クリックする場所", self.next_click_text)
        
        self.row1_label.grid(row=0, column=0, sticky="nsew")
        self.row1_value.grid(row=0, column=1, sticky="nsew")
        
        self.row2_label.grid(row=1, column=0, sticky="nsew")
        self.row2_value.grid(row=1, column=1, sticky="nsew")
        
        self.row3_label.grid(row=2, column=0, sticky="nsew")
        self.row3_value.grid(row=2, column=1, sticky="nsew")

        self.create_buttons()
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)  # 新しいボタンの行を設定

        self.timer = Timer(self)

    def create_table_row(self, label_text, value_text):
        label_frame = tk.Frame(self.root, bg="lightgray", padx=10, pady=5, borderwidth=1, relief="solid")
        label = tk.Label(label_frame, text=label_text, bg="lightgray", font=("Arial", 12))
        label.pack(fill="both", expand=True)

        value_frame = tk.Frame(self.root, bg="white", padx=10, pady=5, borderwidth=1, relief="solid")
        value_label = tk.Label(value_frame, text=value_text, bg="white", font=("Arial", 12))
        value_label.pack(fill="both", expand=True)
        
        return label_frame, value_frame

    def create_buttons(self):
        self.start_button = tk.Button(self.root, text="遠征スタート", command=self.start_action)
        self.start_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.stop_button = tk.Button(self.root, text="タイマーストップ", command=self.stop_action, state=tk.DISABLED)
        self.stop_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # 新しいボタンの追加
        self.ammo_button = tk.Button(self.root, text="弾薬", command=self.expedition_action)
        self.ammo_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        self.bauxite_button = tk.Button(self.root, text="ボーキ", command=self.bauxite_action)
        self.bauxite_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    def start_action(self):
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_display(current_task="アクション中")
        
        perform_actions()  # pyautogui アクションを即座に実行
        self.timer.start_timer()  # タイマーを即座に開始

    def stop_action(self):
        self.timer.stop_timer()
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def expedition_action(self):
        # 弾薬ボタンがクリックされたときの処理を記述
        self.update_display(current_task="弾薬実行中")

    def bauxite_action(self):
        # ボーキボタンがクリックされたときの処理を記述
        self.update_display(current_task="ボーキ実行中")

    def update_display(self, current_task=None, next_time=None, next_click=None):
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

if __name__ == "__main__":
    main()

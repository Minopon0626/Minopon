import tkinter as tk
from start_action import start_action
from stop_action import stop_action
from timer import Timer
from pyautogui_actions import perform_actions_a, perform_actions_b, perform_actions_c, expedition_receive, open_formation, supply  # pyautoguiの動作をインポート
from ammo_action import ammo_action  # ammo_actionをインポート
from bauxite_action import bauxite_action  # bauxite_actionをインポート

class InfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("情報表示アプリ")
        self.root.geometry("400x600")
        self.root.configure(bg="lightgray")

        self.current_task_text = "表示内容A"
        self.next_click_text = "表示内容C"
        self.timer_a_text = "3時間20分"
        self.timer_b_text = "2時間45分"
        self.timer_c_text = "2時間55分"

        self.row1_label, self.row1_value = self.create_table_row("現在すること", self.current_task_text)
        self.row2_label, self.row2_value = self.create_table_row("次クリックする場所", self.next_click_text)
        self.timer_a_label, self.timer_a_value = self.create_table_row("タイマーA", self.timer_a_text)
        self.timer_b_label, self.timer_b_value = self.create_table_row("タイマーB", self.timer_b_text)
        self.timer_c_label, self.timer_c_value = self.create_table_row("タイマーC", self.timer_c_text)

        self.row1_label.grid(row=0, column=0, sticky="nsew")
        self.row1_value.grid(row=0, column=1, sticky="nsew")
        
        self.row2_label.grid(row=1, column=0, sticky="nsew")
        self.row2_value.grid(row=1, column=1, sticky="nsew")

        self.timer_a_label.grid(row=2, column=0, sticky="nsew")
        self.timer_a_value.grid(row=2, column=1, sticky="nsew")

        self.timer_b_label.grid(row=3, column=0, sticky="nsew")
        self.timer_b_value.grid(row=3, column=1, sticky="nsew")

        self.timer_c_label.grid(row=4, column=0, sticky="nsew")
        self.timer_c_value.grid(row=4, column=1, sticky="nsew")

        self.create_buttons()

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

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
        self.start_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.stop_button = tk.Button(self.root, text="タイマーストップ", command=self.stop_action, state=tk.DISABLED)
        self.stop_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # 「弾薬」および「ボーキ」ボタン
        self.ammo_button = tk.Button(self.root, text="弾薬", command=lambda: ammo_action(self))
        self.ammo_button.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

        self.bauxite_button = tk.Button(self.root, text="ボーキ", command=lambda: bauxite_action(self))
        self.bauxite_button.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

    def start_action(self):
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_display(current_task="遠征中")
        
        # タイマーA, B, Cをすべて開始し、対応するpyautogui動作と遠征受取を実行
        self.start_timer_a()
        self.start_timer_b()
        self.start_timer_c()

    def start_timer_a(self):
        # タイマーA開始時の表示を更新
        self.update_display(current_task="タイマーA開始中")
        expedition_receive(self)  # 遠征受取操作
        perform_actions_a()  # タイマーAの動作を実行
        self.timer.start_timer_a()

    def start_timer_b(self):
        # タイマーB開始時の表示を更新
        self.update_display(current_task="タイマーB開始中")
        expedition_receive(self)  # 遠征受取操作
        perform_actions_b()  # タイマーBの動作を実行
        self.timer.start_timer_b()

    def start_timer_c(self):
        # タイマーC開始時の表示を更新
        self.update_display(current_task="タイマーC開始中")
        expedition_receive(self)  # 遠征受取操作
        perform_actions_c()  # タイマーCの動作を実行
        self.timer.start_timer_c()

    def stop_action(self):
        self.timer.stop_timer()
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def update_display(self, current_task=None, next_click=None, timer_a=None, timer_b=None, timer_c=None):
        if current_task is not None:
            self.current_task_text = current_task
            self.row1_value.winfo_children()[0].config(text=self.current_task_text)
        
        if next_click is not None:
            self.next_click_text = next_click
            self.row2_value.winfo_children()[0].config(text=self.next_click_text)

        if timer_a is not None:
            self.timer_a_text = timer_a
            self.timer_a_value.winfo_children()[0].config(text=self.timer_a_text)

        if timer_b is not None:
            self.timer_b_text = timer_b
            self.timer_b_value.winfo_children()[0].config(text=self.timer_b_text)

        if timer_c is not None:
            self.timer_c_text = timer_c
            self.timer_c_value.winfo_children()[0].config(text=self.timer_c_text)

def main():
    root = tk.Tk()
    app = InfoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

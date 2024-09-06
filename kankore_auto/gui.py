import tkinter as tk
from expedition_action import expedition_action  # 遠征ボタンの動作をインポート

def create_gui():
    root = tk.Tk()
    root.title("艦隊アプリ")

    # ラベルのテーブル部分
    label_style = {'bg': 'lightgray', 'width': 20, 'anchor': 'w'}
    value_style = {'width': 20, 'anchor': 'w'}

    # 現在すること
    label_current_task = tk.Label(root, text="現在すること:", **label_style)
    label_current_task.grid(row=0, column=0, padx=5, pady=5)
    value_current_task = tk.Label(root, text="XXXX", **value_style)
    value_current_task.grid(row=0, column=1, padx=5, pady=5)

    # 第二艦隊
    label_second_fleet = tk.Label(root, text="第二艦隊:", **label_style)
    label_second_fleet.grid(row=1, column=0, padx=5, pady=5)
    value_second_fleet = tk.Label(root, text="XXXX", **value_style)
    value_second_fleet.grid(row=1, column=1, padx=5, pady=5)

    # 第三艦隊
    label_third_fleet = tk.Label(root, text="第三艦隊:", **label_style)
    label_third_fleet.grid(row=2, column=0, padx=5, pady=5)
    value_third_fleet = tk.Label(root, text="XXXX", **value_style)
    value_third_fleet.grid(row=2, column=1, padx=5, pady=5)

    # 第四艦隊
    label_fourth_fleet = tk.Label(root, text="第四艦隊:", **label_style)
    label_fourth_fleet.grid(row=3, column=0, padx=5, pady=5)
    value_fourth_fleet = tk.Label(root, text="XXXX", **value_style)
    value_fourth_fleet.grid(row=3, column=1, padx=5, pady=5)

    # ボタンの設定
    expedition_button = tk.Button(root, text="遠征", command=lambda: expedition_action(value_current_task))
    expedition_button.grid(row=4, column=0, padx=5, pady=10)

    bauxite_button = tk.Button(root, text="ボーキ", command=lambda: update_label(value_current_task, "ボーキ処理"))
    bauxite_button.grid(row=4, column=1, padx=5, pady=10)

    root.mainloop()

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)

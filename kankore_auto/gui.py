import tkinter as tk
from bauxite_action import bauxite_click
from expedition_action import start_expedition, receive_reward
from datetime import datetime, timedelta

# グローバル変数としてタイマーを管理するための変数を追加
bauxite_cycle_timer = None
cycle_end_time = None

def start_bauxite_cycle(root, label, current_task_label):
    """
    ボタンが押された時点から30分間だけボーキ処理を繰り返す関数。

    :param root: Tkinterのrootウィンドウ
    :param label: 押した時間を表示するラベル
    :param current_task_label: タスクのラベル（更新用）
    """
    global bauxite_cycle_timer, cycle_end_time

    # ボタンを押した時点の時間を記録
    start_time = datetime.now()
    cycle_end_time = start_time + timedelta(minutes=30)
    label.config(text=f"開始時間: {start_time.strftime('%H:%M:%S')}")

    # ボーキクリックを繰り返す処理
    def repeat_bauxite_click():
        global bauxite_cycle_timer, cycle_end_time
        current_time = datetime.now()

        # 30分経過した場合、繰り返しを停止
        if current_time >= cycle_end_time:
            label.config(text="サイクル終了")
            return

        # ボーキ処理を実行
        bauxite_click(root, current_task_label)

        # 次の繰り返しを460秒後に設定
        bauxite_cycle_timer = root.after(460000, repeat_bauxite_click)

    # 最初の繰り返しを設定
    repeat_bauxite_click()

# GUIの作成部分
def create_gui():
    root = tk.Tk()
    root.title("艦隊アプリ")

    # ラベルのスタイル
    label_style = {'bg': 'lightgray', 'width': 20, 'anchor': 'w'}
    value_style = {'width': 20, 'anchor': 'w'}

    # 現在すること
    label_current_task = tk.Label(root, text="現在すること:", **label_style)
    label_current_task.grid(row=0, column=0, padx=5, pady=5)
    value_current_task = tk.Label(root, text="XXXX", **value_style)
    value_current_task.grid(row=0, column=1, padx=5, pady=5)

    # 第二艦隊
    label_second_fleet_title = tk.Label(root, text="第二艦隊:", **label_style)
    label_second_fleet_title.grid(row=1, column=0, padx=5, pady=5)
    value_second_fleet = tk.Label(root, text="10:00", **value_style)
    value_second_fleet.grid(row=1, column=1, padx=5, pady=5)

    # 第三艦隊
    label_third_fleet_title = tk.Label(root, text="第三艦隊:", **label_style)
    label_third_fleet_title.grid(row=2, column=0, padx=5, pady=5)
    value_third_fleet = tk.Label(root, text="20:00", **value_style)
    value_third_fleet.grid(row=2, column=1, padx=5, pady=5)

    # 第四艦隊
    label_fourth_fleet_title = tk.Label(root, text="第四艦隊:", **label_style)
    label_fourth_fleet_title.grid(row=3, column=0, padx=5, pady=5)
    value_fourth_fleet = tk.Label(root, text="1:20:00", **value_style)
    value_fourth_fleet.grid(row=3, column=1, padx=5, pady=5)

    # 遠征ボタン
    expedition_button = tk.Button(
        root, text="遠征",
        command=lambda: start_expedition(
            root, value_current_task, value_second_fleet, value_third_fleet, value_fourth_fleet
        )
    )
    expedition_button.grid(row=4, column=0, padx=5, pady=10)

    # 受け取りボタン
    receive_button = tk.Button(root, text="受け取り", command=lambda: receive_reward(root, value_current_task))
    receive_button.grid(row=4, column=1, padx=5, pady=10)

    # ボーキボタン
    bauxite_button = tk.Button(root, text="ボーキ", command=lambda: bauxite_click(root, value_current_task))
    bauxite_button.grid(row=4, column=2, padx=5, pady=10)

    # 新しいボタンとその時間表示ラベル（ボーキサイクル開始）
    label_bauxite_time = tk.Label(root, text="未開始", **value_style)
    label_bauxite_time.grid(row=5, column=1, padx=5, pady=5)

    start_bauxite_button = tk.Button(root, text="ボーキサイクル開始", command=lambda: start_bauxite_cycle(root, label_bauxite_time, value_current_task))
    start_bauxite_button.grid(row=5, column=0, padx=5, pady=10)

    root.mainloop()
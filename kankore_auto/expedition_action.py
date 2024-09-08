from timer import start_independent_timer
from utility_functions import delayed_click, delayed_update, return_to_home_port, supply_fleets
import tkinter as tk

# それぞれの艦隊の処理を実行する関数
def start_second_fleet(root, current_task_label, label_second_fleet):
    """
    第二艦隊のタイマーを開始する処理
    前提として遠征の受取及び補給は完了しているとする
    タイマー29分
    """

    supply_fleets(root, current_task_label)

    # 第二艦隊のタイマーを開始
    start_independent_timer(1740, label_second_fleet)  # 29分 = 1740秒

def start_third_fleet(root, label_third_fleet):
    """
    第三艦隊のタイマーを開始する処理
    前提として遠征の受取及び補給は完了しているとする
    """

    start_independent_timer(1200, label_third_fleet)  # 20分 = 1200秒

def start_fourth_fleet(root, label_fourth_fleet):
    """
    第四艦隊のタイマーを開始する処理
    前提として遠征の受取及び補給は完了しているとする
    """

    start_independent_timer(4800, label_fourth_fleet)  # 1時間20分 = 4800秒

# 遠征の全体処理をまとめた関数
def start_expedition(root, current_task_label, label_second_fleet, label_third_fleet, label_fourth_fleet):
    """
    遠征を順次スタートさせる。第二艦隊 -> 5秒遅延 -> 第三艦隊 -> 5秒遅延 -> 第四艦隊
    """
    # 第二艦隊のタイマーをスタート
    start_second_fleet(root, current_task_label, label_second_fleet)

    # 5秒後に第三艦隊をスタート
    root.after(5000, lambda: start_third_fleet(root, label_third_fleet))

    # さらに5秒後に第四艦隊をスタート
    root.after(10000, lambda: start_fourth_fleet(root, label_fourth_fleet))

def receive_reward(root, current_task_label):
    """
    受け取りボタンの処理を実行する関数。
    遠征報酬受取処理 (expedition_reward) を25秒毎に3回繰り返す。
    """
    # 1回目の遠征報酬受取処理
    expedition_reward(root, current_task_label)

    # 20秒後に2回目を実行
    root.after(25000, lambda: expedition_reward(root, current_task_label))

    # さらに20秒後に3回目を実行
    root.after(50000, lambda: expedition_reward(root, current_task_label))

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)

# 遠征報酬受取処理をまとめた関数
def expedition_reward(root, current_task_label):
    """
    遠征報酬受取処理をまとめた関数。
    順番に遅延させてクリックとラベルの更新を行う。
    """
    # 0秒: 最初のクリックと「遠征受取を開始」の更新
    delayed_click(root, 1100, 230)
    delayed_update(root, current_task_label, 0, "遠征受取を開始")

    # 5秒後: 「評価更新」の更新とクリック
    root.after(5000, lambda: (
        delayed_update(root, current_task_label, 0, "評価更新"),
        delayed_click(root, 1100, 230)
    ))

    # 10秒後: 「報酬受け取り」の更新とクリック
    root.after(10000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬受け取り"),
        delayed_click(root, 1100, 230)
    ))

    # 15秒後: 「報酬受け取り(予備クリック)」の更新とクリック
    root.after(15000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬受け取り(予備クリック)"),
        delayed_click(root, 1100, 230)
    ))

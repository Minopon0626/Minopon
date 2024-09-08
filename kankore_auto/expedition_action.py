from timer import start_independent_timer
from utility_functions import delayed_click, delayed_update
import tkinter as tk

# それぞれの艦隊の処理を実行する関数
def start_second_fleet(root, current_task_label, label_second_fleet):
    """
    第二艦隊のタイマーを開始する処理
    タイマー29分
    """
    delayed_click(root, 1100, 230)
    delayed_update(root, current_task_label, 0, "遠征受取を開始")

    # 5秒後に報酬を受け取る処理とクリック
    root.after(5000, lambda: (
        delayed_update(root, current_task_label, 0, "評価更新"),
        delayed_click(root, 1100, 230)
    ))

    root.after(10000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬受け取り"),
        delayed_click(root, 1100, 230)
    ))

    root.after(10000, lambda: (
        delayed_update(root, current_task_label, 0, "報酬受け取り(予備クリック)"),
        delayed_click(root, 1100, 230)
    ))


    # 第二艦隊のタイマーを開始
    start_independent_timer(1740, label_second_fleet)  # 29分 = 1740秒

def start_third_fleet(root, label_third_fleet):
    """
    第三艦隊のタイマーを開始する処理
    """
    print("第三艦隊の遠征を開始")
    start_independent_timer(1200, label_third_fleet)  # 20分 = 1200秒

def start_fourth_fleet(root, label_fourth_fleet):
    """
    第四艦隊のタイマーを開始する処理
    """
    print("第四艦隊の遠征を開始")
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

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)

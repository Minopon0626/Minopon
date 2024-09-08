from timer import start_independent_timer
import tkinter as tk

# それぞれの艦隊の処理を実行する関数
def start_second_fleet(label_second_fleet):
    """
    第二艦隊のタイマーを開始する処理
    """
    print("第二艦隊の遠征を開始")
    start_independent_timer(600, label_second_fleet)  # 10分 = 600秒

def start_third_fleet(label_third_fleet):
    """
    第三艦隊のタイマーを開始する処理
    """
    print("第三艦隊の遠征を開始")
    start_independent_timer(1200, label_third_fleet)  # 20分 = 1200秒

def start_fourth_fleet(label_fourth_fleet):
    """
    第四艦隊のタイマーを開始する処理
    """
    print("第四艦隊の遠征を開始")
    start_independent_timer(4800, label_fourth_fleet)  # 1時間20分 = 4800秒

# 遠征の全体処理をまとめた関数
def start_expedition(root, label_second_fleet, label_third_fleet, label_fourth_fleet):
    """
    遠征を順次スタートさせる。第二艦隊 -> 5秒遅延 -> 第三艦隊 -> 5秒遅延 -> 第四艦隊
    """
    # 第二艦隊のタイマーをスタート
    start_second_fleet(label_second_fleet)

    # 5秒後に第三艦隊をスタート
    root.after(5000, lambda: start_third_fleet(label_third_fleet))

    # さらに5秒後に第四艦隊をスタート
    root.after(10000, lambda: start_fourth_fleet(label_fourth_fleet))

# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)
from timer import start_independent_timer  # 修正：start_independent_timer をインポート
import tkinter as tk

def start_expedition(root, label_second_fleet, label_third_fleet, label_fourth_fleet):
    """
    遠征を順次スタートさせる。第二艦隊 -> 5秒遅延 -> 第三艦隊 -> 5秒遅延 -> 第四艦隊
    """
    # 第二艦隊のタイマーをスタート
    start_independent_timer(600, label_second_fleet)  # 10分 = 600秒
    print("第二艦隊のタイマー開始")
    
    # 5秒後に第三艦隊をスタート
    root.after(5000, lambda: start_independent_timer(1200, label_third_fleet))  # 20分 = 1200秒
    print("第三艦隊のタイマー開始予定")

    # さらに5秒後に第四艦隊をスタート
    root.after(10000, lambda: start_independent_timer(4800, label_fourth_fleet))  # 1時間20分 = 4800秒
    print("第四艦隊のタイマー開始予定")


# ラベルを更新する関数
def update_label(label, new_value):
    label.config(text=new_value)

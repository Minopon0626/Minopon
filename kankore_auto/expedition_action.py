from timer import start_independent_timer
from utility_functions import delayed_click, delayed_update, return_to_home_port, supply_fleets
import tkinter as tk

fleet_timers_active = {
    "second_fleet": False,
    "third_fleet": False,
    "fourth_fleet": False
}

def start_second_fleet(root, current_task_label, label_second_fleet):
    """
    第二艦隊のタイマーを開始する処理
    タイマー29分
    """
    if fleet_timers_active["second_fleet"]:
        return  # すでにタイマーが動作している場合、処理を終了

    fleet_timers_active["second_fleet"] = True
    start_independent_timer(1740, label_second_fleet)  # 29分 = 1740秒
    # タイマーが終了した後、フラグをリセット
    root.after(1740000, lambda: fleet_timers_active.update({"second_fleet": False}))

def start_third_fleet(root, label_third_fleet):
    """
    第三艦隊のタイマーを開始する処理
    タイマー20分
    """
    if fleet_timers_active["third_fleet"]:
        return  # すでにタイマーが動作している場合、処理を終了

    fleet_timers_active["third_fleet"] = True
    print("第三艦隊の遠征を開始")
    start_independent_timer(1200, label_third_fleet)  # 20分 = 1200秒
    # タイマーが終了した後、フラグをリセット
    root.after(1200000, lambda: fleet_timers_active.update({"third_fleet": False}))

def start_fourth_fleet(root, label_fourth_fleet):
    """
    第四艦隊のタイマーを開始する処理
    タイマー1時間20分
    """
    if fleet_timers_active["fourth_fleet"]:
        return  # すでにタイマーが動作している場合、処理を終了

    fleet_timers_active["fourth_fleet"] = True
    print("第四艦隊の遠征を開始")
    start_independent_timer(4800, label_fourth_fleet)  # 1時間20分 = 4800秒
    # タイマーが終了した後、フラグをリセット
    root.after(4800000, lambda: fleet_timers_active.update({"fourth_fleet": False}))

def start_expedition(root, current_task_label, label_second_fleet, label_third_fleet, label_fourth_fleet):
    """
    遠征を順次スタートさせる。各艦隊のタイマーが既に動作している場合は新しく作成しない。
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

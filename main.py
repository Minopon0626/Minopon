import threading
import time

# 自作したプログラムをインポートする
import custom_print

# タイマーの残り時間を保存する辞書
timer_remaining = {}

# タイマーのカウントダウンを行う関数
def timer_function(timer_id, duration):
    global timer_remaining

    remaining_time = duration
    while remaining_time > 0:
        # 残り時間を辞書に保存
        timer_remaining[timer_id] = remaining_time

        # 残り時間を表示（custom_printを使用）
        line1 = f"Timer 1: {timer_remaining.get(1, 0)} seconds remaining"
        line2 = f"Timer 2: {timer_remaining.get(2, 0)} seconds remaining"
        line3 = f"Timer 3: {timer_remaining.get(3, 0)} seconds remaining"
        custom_print.custom_print(line1, line2, line3)
        time.sleep(1)
        remaining_time -= 1

    # タイマーが終了した場合の処理
    timer_remaining[timer_id] = 0
    # print(f"Timer {timer_id} finished")

# タイマーを開始する関数
def start_timers(durations):
    threads = []
    for timer_id, duration in durations.items():
        # 各タイマーごとにスレッドを作成して開始
        thread = threading.Thread(target=timer_function, args=(timer_id, duration))
        threads.append(thread)
        thread.start()

    # 全てのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

# 使用例: 各タイマーの時間を設定して開始
durations = {1: 10, 2: 15, 3: 20}
custom_print.start_cutom_print()
start_timers(durations)

import threading
import time
import custom_print
from mouse_position import get_mouse_position

# タイマーの残り時間を保存する辞書
timer_remaining = {}

# タイマーのカウントダウンを行う関数
def timer_function(timer_id, duration, callback):
    global timer_remaining

    remaining_time = duration
    while remaining_time > 0:
        # 残り時間を辞書に保存
        timer_remaining[timer_id] = remaining_time

        time.sleep(1)
        remaining_time -= 1

    # タイマーが終了した場合の処理
    timer_remaining[timer_id] = 0
    callback(timer_id)  # コールバック関数を呼び出し

def start_timers(durations, callback):
    threads = []
    for timer_id, duration in durations.items():
        # 各タイマーごとにスレッドを作成して開始
        thread = threading.Thread(target=timer_function, args=(timer_id, duration, callback))
        threads.append(thread)
        thread.start()

    while any(thread.is_alive() for thread in threads):
        # 残り時間を表示（custom_printを使用）
        mouse_x, mouse_y = get_mouse_position()
        line1 = f"Timer 1: {timer_remaining.get(1, 0)} seconds remaining"
        line2 = f"Timer 2: {timer_remaining.get(2, 0)} seconds remaining"
        line3 = f"Timer 3: {timer_remaining.get(3, 0)} seconds remaining"
        line4 = f"Mouse Position: ({mouse_x}, {mouse_y})"
        custom_print.custom_print(line1, line2, line3, line4)
        time.sleep(1)

    # 全てのスレッドが終了するまで待機
    for thread in threads:
        thread.join()

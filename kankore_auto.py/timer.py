import threading
import time
import custom_print
from mouse_position import get_mouse_position

# タイマーの残り時間を保存する辞書
timer_remaining = {}
timer_lock = threading.Lock()

# タイマーのカウントダウンを行う関数
def timer_function(timer_id, duration, callback):
    global timer_remaining

    remaining_time = duration
    while remaining_time > 0:
        with timer_lock:
            # 残り時間を辞書に保存
            timer_remaining[timer_id] = remaining_time

        time.sleep(1)
        remaining_time -= 1

    # タイマーが終了した場合の処理
    with timer_lock:
        timer_remaining[timer_id] = 0
    callback(timer_id)  # コールバック関数を呼び出し

# タイマーを開始する関数
def start_timer(timer_id, duration, callback):
    thread = threading.Thread(target=timer_function, args=(timer_id, duration, callback))
    thread.start()

def start_timers(durations, callback):
    global timer_remaining
    timer_remaining = durations.copy()
    threads = []
    for timer_id, duration in durations.items():
        # 各タイマーごとにスレッドを作成して開始
        thread = threading.Thread(target=timer_function, args=(timer_id, duration, callback))
        threads.append(thread)
        thread.start()

    while True:
        # 残り時間を表示（custom_printを使用）
        with timer_lock:
            mouse_x, mouse_y = get_mouse_position()
            line1 = f"タイマー 1: 残り {timer_remaining.get(1, 0)} 秒"
            line2 = f"タイマー 2: 残り {timer_remaining.get(2, 0)} 秒"
            line3 = f"タイマー 3: 残り {timer_remaining.get(3, 0)} 秒"
            line4 = f"マウスの位置: ({mouse_x}, {mouse_y})"
        custom_print.custom_print(line1, line2, line3, line4)
        time.sleep(1)

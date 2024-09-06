import time
import threading

def start_timer(seconds, label):
    # タイマーをスレッドで実行
    def update_timer():
        remaining_time = seconds
        while remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            hours, mins = divmod(mins, 60)
            time_format = f"{hours}:{mins:02d}:{secs:02d}" if hours > 0 else f"{mins:02d}:{secs:02d}"
            label.config(text=time_format)
            time.sleep(1)
            remaining_time -= 1
        label.config(text="完了")

    # タイマーをスレッドで開始
    threading.Thread(target=update_timer).start()

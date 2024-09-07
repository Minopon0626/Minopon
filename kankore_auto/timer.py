import time
import threading

def start_independent_timer(seconds, label):
    """
    独立したタイマーを開始し、残り時間をラベルに表示する。
    
    :param seconds: タイマーの秒数
    :param label: 残り時間を表示するTkinterのラベル
    """
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

    # 独立したスレッドでタイマーを開始
    threading.Thread(target=update_timer).start()

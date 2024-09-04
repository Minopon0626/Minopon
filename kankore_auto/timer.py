import time
import threading

class Timer:
    def __init__(self, app):
        self.app = app
        self.timer_running = False
        self.timer_thread = None
        self.end_time = None

    def start_timer(self):
        if self.timer_running:
            return  # タイマーがすでに動作している場合は何もしない
        
        # タイマーを即座に開始
        self._start_timer()

    def _start_timer(self):
        self.end_time = time.time() + (3 * 3600 + 20 * 60)
        self.app.update_display(current_task="タイマー待機中", next_time="3時間20分")

        # タイマーを定期的に更新するスレッドを開始
        self.timer_running = True
        self.timer_thread = threading.Thread(target=self._update_timer)
        self.timer_thread.daemon = True  # スレッドがバックグラウンドで動作するようにする
        self.timer_thread.start()

    def _update_timer(self):
        while self.timer_running and time.time() < self.end_time:
            remaining_time = int(self.end_time - time.time())
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours}時間 {minutes}分 {seconds}秒"
            
            # メインスレッドに通知してGUIを更新する
            self.app.root.after(0, lambda: self.app.update_display(next_time=time_str))
            time.sleep(1)
        
        # タイマーが終了したときに表示を更新
        if self.timer_running:
            self.app.root.after(0, lambda: self.app.update_display(next_time="終了"))
            self.timer_running = False  # タイマーが停止したことを示す

    def stop_timer(self):
        self.timer_running = False  # タイマーの停止フラグを設定
        self.app.update_display(current_task="タイマー停止中", next_time="タイマー停止")

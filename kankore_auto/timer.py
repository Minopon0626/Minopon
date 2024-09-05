import time
import threading

class Timer:
    def __init__(self, app):
        self.app = app
        self.timer_running_a = False
        self.timer_running_b = False
        self.timer_running_c = False
        self.timer_thread_a = None
        self.timer_thread_b = None
        self.timer_thread_c = None
        self.end_time_a = None
        self.end_time_b = None
        self.end_time_c = None

    def start_timer_a(self):
        if self.timer_running_a:
            return  # タイマーAがすでに動作している場合は何もしない
        
        self.end_time_a = time.time() + (3 * 3600 + 20 * 60)  # タイマーAは3時間20分
        self.timer_running_a = True
        self.timer_thread_a = threading.Thread(target=self._update_timer_a)
        self.timer_thread_a.daemon = True
        self.timer_thread_a.start()

    def start_timer_b(self):
        if self.timer_running_b:
            return  # タイマーBがすでに動作している場合は何もしない
        
        self.end_time_b = time.time() + (2 * 3600 + 45 * 60)  # タイマーBは2時間45分
        self.timer_running_b = True
        self.timer_thread_b = threading.Thread(target=self._update_timer_b)
        self.timer_thread_b.daemon = True
        self.timer_thread_b.start()

    def start_timer_c(self):
        if self.timer_running_c:
            return  # タイマーCがすでに動作している場合は何もしない
        
        self.end_time_c = time.time() + (2 * 3600 + 55 * 60)  # タイマーCは2時間55分
        self.timer_running_c = True
        self.timer_thread_c = threading.Thread(target=self._update_timer_c)
        self.timer_thread_c.daemon = True
        self.timer_thread_c.start()

    def _update_timer_a(self):
        while self.timer_running_a and time.time() < self.end_time_a:
            remaining_time = int(self.end_time_a - time.time())
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours}時間 {minutes}分 {seconds}秒"
            self.app.root.after(0, lambda: self.app.update_display(timer_a=time_str))
            time.sleep(1)
        
        self.timer_running_a = False
        self.app.root.after(0, lambda: self.app.update_display(timer_a="終了"))

    def _update_timer_b(self):
        while self.timer_running_b and time.time() < self.end_time_b:
            remaining_time = int(self.end_time_b - time.time())
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours}時間 {minutes}分 {seconds}秒"
            self.app.root.after(0, lambda: self.app.update_display(timer_b=time_str))
            time.sleep(1)
        
        self.timer_running_b = False
        self.app.root.after(0, lambda: self.app.update_display(timer_b="終了"))

    def _update_timer_c(self):
        while self.timer_running_c and time.time() < self.end_time_c:
            remaining_time = int(self.end_time_c - time.time())
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours}時間 {minutes}分 {seconds}秒"
            self.app.root.after(0, lambda: self.app.update_display(timer_c=time_str))
            time.sleep(1)
        
        self.timer_running_c = False
        self.app.root.after(0, lambda: self.app.update_display(timer_c="終了"))

    def stop_timer(self):
        self.timer_running_a = False
        self.timer_running_b = False
        self.timer_running_c = False
        self.app.update_display(current_task="タイマー停止中", timer_a="タイマー停止", timer_b="タイマー停止", timer_c="タイマー停止")

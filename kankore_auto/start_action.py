import time
import threading

def start_action(app):
    # スタートボタンが押された際にタイマーを即座に開始
    app.update_display(current_task="アクション中")
    start_timer(app)  # 10秒の遅延を取り除き、即座にタイマーを開始

def start_timer(app):
    # タイマーをスタート
    app.end_time = time.time() + (3 * 3600 + 20 * 60)
    app.update_display(current_task="タイマー待機中", next_time="3時間20分")

    # タイマーを定期的に更新するスレッドを開始
    if not hasattr(app, 'timer_thread') or not app.timer_thread.is_alive():
        app.timer_thread = threading.Thread(target=update_timer, args=(app,))
        app.timer_thread.daemon = True  # スレッドがバックグラウンドで動作するようにする
        app.timer_thread.start()

def update_timer(app):
    while time.time() < app.end_time:
        remaining_time = int(app.end_time - time.time())
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours}時間 {minutes}分 {seconds}秒"
        
        # メインスレッドに通知してGUIを更新する
        app.root.after(0, lambda: app.update_display(next_time=time_str))
        time.sleep(1)
    
    # タイマーが終了したときに表示を更新
    app.root.after(0, lambda: app.update_display(next_time="終了"))
    app.start_button.config(state="normal")  # タイマー終了後に「スタート」ボタンを再度有効にする
    app.stop_button.config(state="disabled")  # 「ストップ」ボタンを無効にする

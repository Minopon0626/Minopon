# 自作したプログラムをインポートする
import custom_print
import timer
import time

# タイマー終了時に呼び出されるコールバック関数
def timer_finished(timer_id):
    # タイマーが終了したときの処理を追加
    if timer_id == 1:
        # print("タイマー 1 のカウントダウンが完了しました。タイマーをリセットします。")
        # 特定の処理をここで実行
        # ...
        time.sleep(1)
        # タイマーをリセット
        timer.start_timer(1, durations[1], timer_finished)
    elif timer_id == 2:
        # print("タイマー 2 のカウントダウンが完了しました。タイマーをリセットします。")
        # 特定の処理をここで実行
        # ...
        time.sleep(2)
        # タイマーをリセット
        timer.start_timer(2, durations[2], timer_finished)
    elif timer_id == 3:
        # print("タイマー 3 のカウントダウンが完了しました。タイマーをリセットします。")
        # 特定の処理をここで実行
        # ...
        time.sleep(3)
        # タイマーをリセット
        timer.start_timer(3, durations[3], timer_finished)

# 使用例: 各タイマーの時間を設定して開始
durations = {1: 10, 2: 15, 3: 20}
custom_print.start_custom_print()
timer.start_timers(durations, timer_finished)

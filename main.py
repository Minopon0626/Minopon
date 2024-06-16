# 自作したプログラムをインポートする
import custom_print
import timer

# タイマー終了時に呼び出されるコールバック関数
def timer_finished(timer_id):
    # print(f"Timer {timer_id} finished!")
    # ここに各タイマーが終了したときの処理を追加
    if timer_id == 1:
        print("Timer 1 has completed its countdown.")
    elif timer_id == 2:
        print("Timer 2 has completed its countdown.")
    elif timer_id == 3:
        print("Timer 3 has completed its countdown.")

# 使用例: 各タイマーの時間を設定して開始
durations = {1: 10, 2: 15, 3: 20}
custom_print.start_custom_print()
timer.start_timers(durations, timer_finished)

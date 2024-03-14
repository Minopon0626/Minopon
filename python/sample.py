from multiprocessing import Process, Manager
import time
import os
import platform

def clear_console():
    """コンソールの内容をクリアする"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def timer(timers_dict, timer_id, duration_seconds):
    """指定された時間のタイマーを実行し、残り時間を更新する"""
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, duration_seconds - elapsed_time)
        timers_dict[timer_id] = remaining_time
        if remaining_time <= 0:
            break
        time.sleep(1)
    del timers_dict[timer_id]

def display_timers(timers_dict):
    """アクティブなタイマーの残り時間をクリアしてから表示する"""
    try:
        while True:
            clear_console()
            if not timers_dict:
                print("アクティブなタイマーはありません。")
            else:
                for timer_id, remaining_time in list(timers_dict.items()):
                    minutes, seconds = divmod(int(remaining_time), 60)
                    print(f"{timer_id}: 残り{minutes}分{seconds}秒", end='; ')
                print('')
            time.sleep(1)
    except KeyboardInterrupt:
        print("表示プロセスが終了しました。")

def main():
    with Manager() as manager:
        timers_dict = manager.dict()

        # タイマー表示プロセス
        display_process = Process(target=display_timers, args=(timers_dict,))
        display_process.start()

        timer_durations = {"1": 140, "2": 210, "3": 220}  # 入力値と対応する秒数

        try:
            while True:
                input_str = input("タイマーの設定（1: 2分20秒, 2: 3分30秒, 3: 3分40秒, 'exit'で終了）: ")
                if input_str.lower() == 'exit':
                    break
                if input_str not in timer_durations:
                    print("有効な入力値を入力してください（1, 2, 3）。")
                    continue
                duration_seconds = timer_durations[input_str]
                timer_id = f"{input_str}番のタイマー"
                p = Process(target=timer, args=(timers_dict, timer_id, duration_seconds))
                p.start()
        except KeyboardInterrupt:
            print("メインプロセスが終了しました。")

        display_process.terminate()

if __name__ == '__main__':
    main()
    print("プログラムが終了しました。")
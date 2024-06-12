import threading
import queue
import time
import os
import sys

# キューの作成
message_queue = queue.Queue()

# コンソールをクリアする関数
def clear_console():
    if os.name == 'nt':  # Windowsの場合
        os.system('cls')
    else:  # Linux / Mac の場合
        os.system('clear')

# print_and_clearスレッドが実行する関数
def print_and_clear():
    last_message = None  # この関数内で最後のメッセージを保持
    while True:
        if not message_queue.empty():
            # 既存の表示内容を削除
            clear_console()
            # キューからメッセージを1つ取得し表示
            last_message = message_queue.get()
            print(last_message)
            message_queue.task_done()
            time.sleep(1)  # 表示を見やすくするために少し待つ
        else:
            # キューが空の場合、最後に表示したメッセージを再表示
            if last_message is not None:
                clear_console()
                print("キューが空です。最後のメッセージを再表示します:")
                print(last_message)
            time.sleep(1)  # 次のチェックまで少し待つ

# inputスレッドが実行する関数
def input_thread():
    while True:
        user_input = input("入力してください: ")
        message_queue.put(user_input)

# mainスレッドが実行する関数
def main_thread():
    while True:
        time.sleep(10)  # 何かしらのメイン処理を想定
        message_queue.put("メイン処理を実行中...\n")
        message_queue.put("A")
        message_queue.put("B")
        message_queue.put("C")
        message_queue.put("メイン処理が完了しました。\n")
        # ここにメインの処理を追加する

# スレッドの作成と開始
print_and_clear_thread = threading.Thread(target=print_and_clear, daemon=True)
input_thread = threading.Thread(target=input_thread, daemon=True)

print_and_clear_thread.start()
input_thread.start()

main_thread()  # メインスレッドの処理を実行

import os
import pyautogui
import threading
import queue
import time
import sys

subdirectory_path = os.path.join(os.getcwd(), 'time_of_an_expedition')

time_dict = {}

# キューの作成
q = queue.Queue()

def main(queue_a, queue_b, queue_c):
    queue_a.put('システム開始')  # キューにメッセージを追加

    try:
        file_names = subdirectory_file_name_get()  # ファイル名のリストを取得
    except Exception as e:
        print(f"ファイルリストの取得中にエラーが発生しました: {e}")
        queue_a.put('システムエラー終了')
        queue_a.put(None)
        return -1

    for file_name in file_names:  # リスト内の各ファイル名に対して関数を実行
        try:
            extract_id(os.path.join(subdirectory_path, file_name), time_dict)
        except Exception as e:
            print(f"ファイル {file_name} の処理中にエラーが発生しました: {e}")
            continue

    display_time_dict(time_dict)

    queue_a.put('システム終了')
    queue_a.put(None)
    queue_b.put(None)
    queue_c.put(None)
    return 0

def user_input_handler(input_queue):
    while True:
        user_input = input("コマンドを入力してください（'exit'でプログラムを終了）: ")
        input_queue.put(user_input)
        if user_input == "exit":
            sys.exit()  # ユーザーが 'exit' を入力した場合、プログラムを終了

def sub(queue_a, queue_b, queue_c):
    queue_a_done = False
    queue_b_done = False
    queue_c_done = False

    # 各キューの最後のメッセージを保持する辞書
    last_messages = {'A': None, 'B': None, 'C': None}

    while True:
        should_display = False  # 今回のループでメッセージを表示するかどうかのフラグ

        if not queue_a_done or last_messages['A'] is not None:
            try:
                msg_a = queue_a.get_nowait()
                if msg_a is None:
                    queue_a_done = True
                else:
                    last_messages['A'] = f"A: {msg_a}"
                should_display = True
            except queue.Empty:
                pass

        if not queue_b_done or last_messages['B'] is not None:
            try:
                msg_b = queue_b.get_nowait()
                if msg_b is None:
                    queue_b_done = True
                else:
                    last_messages['B'] = f"B: {msg_b}"
                should_display = True
            except queue.Empty:
                pass

        if not queue_c_done or last_messages['C'] is not None:
            try:
                msg_c = queue_c.get_nowait()
                if msg_c is None:
                    queue_c_done = True
                else:
                    last_messages['C'] = f"C: {msg_c}"
                should_display = True
            except queue.Empty:
                pass

        if should_display:
            clear_console()
            for key in last_messages:
                if last_messages[key]:  # 空のメッセージは表示しない
                    print(last_messages[key])

        # 全てのキューがNoneを受け取った場合、ループを抜けて終了
        if queue_a_done and queue_b_done and queue_c_done and all(value is None for value in last_messages.values()):
            break

        # タイマーを使って定期的に更新するならここに処理を書く
        time.sleep(1)


def clear_console():
    """
    コンソールの出力をクリアする関数。
    OSに応じて適切なコマンドを実行します。
    """
    # Windowsの場合
    if os.name == 'nt':
        os.system('cls')
    # MacOSやLinuxの場合
    else:
        os.system('clear')

def subdirectory_file_name_get():
    """
    サブディレクトリ内のファイル名を取得する関数
    """
    file_names = [f for f in os.listdir(subdirectory_path) if os.path.isfile(os.path.join(subdirectory_path, f))]
    return file_names

def extract_id(file_name, time_dict):
    """
    ファイルからIDと時間のペアを抽出して辞書に追加する関数
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            # 行をスペースで分割して、IDと時間のペアを抽出
            parts = line.strip().split()
            if parts:  # 空行は無視する
                id_part = parts[0].rstrip(',')  # 最初の要素はID、末尾のコンマを取り除く
                time_part = parts[-1]  # 最後の要素は時間
                time_dict[id_part] = time_part  # 辞書に追加

def display_time_dict(time_dict):
    """
    辞書の内容を表示する関数
    """
    if time_dict:
        queue_b.put("ID and Time Pairs:")
        for id_key, time_value in time_dict.items():
            queue_b.put(f'ID: {id_key}, Time: {time_value}')
    else:
        queue_b.put("The dictionary is empty.")

def move_and_click(x, y):
    """
    マウスカーソルを指定の座標に移動してクリックする関数
    """

    pyautogui.moveTo(x, y, duration=0.5)  # 移動
    pyautogui.click()  # クリック

def back_to_port():
    """
    母港に戻るボタンの座標 x = 100, y = 200
    """
    move_and_click(100, 200)
    move_and_click(100, 200)
    move_and_click(100, 200)

def finish_expeditionary():
    """
    母港から遠征を受取画面に移動 x = 1100, y = 200
    遠征を受取る, 母港に戻る x = 1100, y = 200
    """

if __name__ == "__main__":
    # キューの作成
    queue_a = queue.Queue() #現在行おうとしている行動
    queue_b = queue.Queue() #操作内容
    queue_c = queue.Queue() #次の実行までの時間
    input_queue = queue.Queue() #ユーザー入力

    # サブスレッドでsub関数を実行
    sub_thread = threading.Thread(target=sub, args=(queue_a, queue_b, queue_c))
    # サブスレッドの開始
    sub_thread.start()

    # ユーザー入力を受け付けるスレッドを開始
    input_thread = threading.Thread(target=user_input_handler, args=(input_queue,))
    # ユーザー入力スレッドの開始
    input_thread.start()
    # メインスレッドでmain関数を実行
    main(queue_a, queue_b, queue_c)
    # サブスレッドの終了を待つ
    sub_thread.join()


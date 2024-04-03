import os
import pyautogui
import threading
import queue
import time

subdirectory_path = os.path.join(os.getcwd(), 'time_of_an_expedition')

time_dict = {}

# キューの作成
q = queue.Queue()

def main(q):
    q.put('システム開始')  # キューにメッセージを追加

    file_names = subdirectory_file_name_get()  # ファイル名のリストを取得

    for file_name in file_names:  # リスト内の各ファイル名に対して関数を実行
        extract_id(os.path.join(subdirectory_path, file_name), time_dict)

    display_time_dict(time_dict)

    q.put('システム終了')
    q.put(None)
    return 0

def sub(q):
    while True:
        message = q.get()  # キューからメッセージを取得
        if message is None:  # Noneが送られてきたらループを抜ける
            break

        clear_console()

        print(message)
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
        q.put("ID and Time Pairs:")
        for id_key, time_value in time_dict.items():
            q.put(f'ID: {id_key}, Time: {time_value}')
    else:
        q.put("The dictionary is empty.")

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

def finish_expeditionary():
    """
    遠征を受取画面に移動 x = 1100, y = 200
    遠征を受取る, 母港に戻る x = 1100, y = 200
    """

if __name__ == "__main__":
    # サブスレッドでsub関数を実行
    sub_thread = threading.Thread(target=sub, args=(q,))

    # サブスレッドの開始
    sub_thread.start()
    main(q)
    # サブスレッドの終了を待つ
    sub_thread.join()


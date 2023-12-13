import sys
import pyautogui
import time

# 引数が一つ必要なものとする

# 初期起動をする
def startUp():
    # leveling等このプログラムを実行した際に最初に実行される部分
    waitMoniter = 5             # 開始する際にモニター等の待機時間
    for i in range(waitMoniter):
        messagePrint(f"モニターの準備をしてください。{waitMoniter - i}秒後開始します")
        time.sleep(1)

    messagePrint("実行完了")

# 引数に停止する時間を入れてとめる
def sleepTime(times):
    # times秒だけプログラムを停止と同時に
    for i in range(times):
        # メッセージを出力
        messagePrint(f"{times - i}秒待機")
        time.sleep(1)           # 1秒待機
    messagePrint("待機完了")


# messageに出力したいものを入れて呼び出すと出力してくれる
def messagePrint(message):
    # メッセージを受け取ってパディングする
    messageLength = len(message)
    # 50 - メッセージの長さで50も自分確定で初期化
    spaceToAdd = 50 - messageLength
    if spaceToAdd > 0:
        message += ' ' * spaceToAdd
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

if __name__ == "__main__":
    # 引数をチェックする部分
    if len(sys.argv) > 1:       # 引数が一つ以上であれば
        try:
            # = int(sys.argv[1]) # 最初の引数
            print("引数設定が正確にうまく行っています")
            startUp()           # 初期起動部分に関する関数に以降
        except ValueError:
            # 引数が整数でない場合
            print("引数は整数である必要があります。")
    else:
        # 引数が不足している場合
        print("引数が不足しています。")
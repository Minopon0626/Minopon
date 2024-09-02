import sys
import time

"""
完成済み！！！！！！！！

現在の最新の行を一度削除する。その後引数に入れてある文字列を表示するプログラム
"""

def print_message_and_clear_last_line(message):
    # カーソルを一つ上の行に移動
    sys.stdout.write("\033[F")  # ANSIエスケープコードでカーソルを上に移動
    sys.stdout.write("\r" + " " * 80)  # 行を空白で消去
    sys.stdout.write("\r" + message)  # 新しいメッセージを表示
    sys.stdout.flush()  # バッファをフラッシュして即座に表示

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法: python script.py <message>")
    else:
        print("消えるよ", end='', flush=True)  # 初めのメッセージを表示
        time.sleep(2)  # 2秒待機
        print_message_and_clear_last_line(sys.argv[1])  # 一つ上の行を消去し、新しいメッセージを表示

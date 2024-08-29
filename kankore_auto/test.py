import sys
import time
import os
"""
現在の最新の行を一度削除する。その後引数に入れてある文字列を表示するプログラム
"""


def print_message_and_clear_last_line(message):
    # 現在の内容を記録するために、エスケープシーケンスを使用
    sys.stdout.write("\r" + " " * 80)  # 現在の行を空白で消去
    sys.stdout.write("\r" + message)  # 新しいメッセージを表示
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法: python script.py <message>")
    else:
        message = sys.argv[1]
        print_message_and_clear_last_line(message)

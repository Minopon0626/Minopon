import sys


# messageを引数に取り標準出力を書き換えながら表示していく関数
def messagePrint(message):
    # メッセージを受け取ってパディングする
    messageLength = len(message)
    # 100 - メッセージの長さで50も自分確定で初期化
    spaceToAdd = 100 - messageLength
    if spaceToAdd > 0:
        message += ' ' * spaceToAdd
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()
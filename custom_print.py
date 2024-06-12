import sys

def start_cutom_print():
    """
    cutom_print関数を利用するうえで3行分の改行が必要なのでそれを行う関数
    """
    sys.stdout.write('\n' * 3)  # 3行分の改行を挟む

def custom_print(line1_str, line2_str, line3_str):
    """
    最新の3行の内容を指定された文字列で書き換える関数。
    いずれかの行に"/return"が含まれている場合、更新作業を行わずに3行分の改行のみを行う。
    Args:
    line1_str (str): 最新の3行のうち最も古い行の内容に書き換える文字列。
    line2_str (str): 最新の3行のうち2番目に古い行の内容に書き換える文字列。
    line3_str (str): 最新の3行のうち最も新しい行の内容に書き換える文字列。
    """
    # 標準出力をフラッシュしてすべてのデータが書き込まれるようにする
    sys.stdout.flush()

    # 改行フラグをチェック
    if "/return" in [line1_str, line2_str, line3_str]:
        sys.stdout.write('\n' * 3)  # 3行分の改行を挟む
    else:
        # 最新の3行を指定された内容で書き換えるために、カーソルを3行分上に移動
        for _ in range(3):
            sys.stdout.write('\x1b[1A')  # カーソルを一行上に移動
            sys.stdout.write('\x1b[2K')  # 行をクリア

        # 新しい内容を逆順に出力（最新の行から順に出力）
        sys.stdout.write(line1_str + '\n')
        sys.stdout.write(line2_str + '\n')
        sys.stdout.write(line3_str + '\n')

# 例としての使用方法
if __name__ == "__main__":
    import time

    start_cutom_print()
    time.sleep(1)
    custom_print("Line 1", "Line 2", "Line 3")
    time.sleep(1)
    # 最新の3行を新しい内容に置き換える
    custom_print("New Line 1", "New Line 2", "New Line 3")
    time.sleep(1)  # 1秒間待機
    # 改行を含むケースのテスト
    time.sleep(1)  # 1秒間待機
    custom_print("Line 5", "/return", "Line 6")
    time.sleep(1)  # 1秒間待機
    custom_print("Line 5", "Line 6", "Line 7")
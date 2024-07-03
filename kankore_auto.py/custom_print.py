import sys

def start_custom_print():
    """
    custom_print関数を利用するうえで4行分の改行が必要なのでそれを行う関数
    """
    sys.stdout.write('\n' * 4)  # 4行分の改行を挟む
    sys.stdout.flush()

def custom_print(line1_str, line2_str, line3_str, line4_str):
    """
    最新の4行の内容を指定された文字列で書き換える関数。
    いずれかの行に"/return"が含まれている場合、更新作業を行わずに4行分の改行のみを行う。
    Args:
    line1_str (str): 最新の4行のうち最も古い行の内容に書き換える文字列。
    line2_str (str): 最新の4行のうち2番目に古い行の内容に書き換える文字列。
    line3_str (str): 最新の4行のうち3番目に古い行の内容に書き換える文字列。
    line4_str (str): 最新の4行のうち最も新しい行の内容に書き換える文字列。
    """
    try:
        # 標準出力をフラッシュしてすべてのデータが書き込まれるようにする
        sys.stdout.flush()

        # 改行フラグをチェック
        if "/return" in [line1_str, line2_str, line3_str, line4_str]:
            sys.stdout.write('\n' * 4)  # 4行分の改行を挟む
        else:
            # 最新の4行を指定された内容で書き換えるために、カーソルを4行分上に移動
            for _ in range(4):
                sys.stdout.write('\x1b[1A')  # カーソルを一行上に移動
                sys.stdout.write('\x1b[2K')  # 行をクリア

            # 色の指定
            RED = '\033[91m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RESET = '\033[0m'

            def colorize_text(text, color, char_to_color):
                """
                特定の文字だけ色を変える関数。
                Args:
                text (str): 色を変えたい文字列。
                color (str): 文字に適用する色。
                char_to_color (str): 色を変えたい文字。
                Returns:
                str: 色が変わった文字列。
                """
                return ''.join([f"{color}{char}{RESET}" if char == char_to_color else char for char in text])

            # 特定の文字だけ色を変える
            line1_str = colorize_text(line1_str, RED, '改')
            line1_str = colorize_text(line1_str, RED, '行')
            line2_str = colorize_text(line2_str, GREEN, '*')
            line3_str = colorize_text(line3_str, YELLOW, '*')

            # 新しい内容を逆順に出力（最新の行から順に出力）
            sys.stdout.write(line1_str + '\n')
            sys.stdout.write(line2_str + '\n')
            sys.stdout.write(line3_str + '\n')
            sys.stdout.write(line4_str + '\n')
        sys.stdout.flush()
    except Exception as e:
        sys.stdout.write(f"エラーが発生しました: {e}\n")
        sys.stdout.flush()

# 例としての使用方法
if __name__ == "__main__":
    import time

    start_custom_print()
    time.sleep(1)
    custom_print("5", "-----", "5秒後に改行します", "Line 1")
    time.sleep(1)
    # 最新の4行を新しい内容に置き換える
    custom_print("4", "*----", "4秒後に改行します", "Line 2")
    time.sleep(1)  # 1秒間待機
    custom_print("3", "**---", "3秒後に改行します", "Line 3")
    time.sleep(1)  # 1秒間待機
    custom_print("2", "***--", "2秒後に改行します", "Line 4")
    time.sleep(1)  # 1秒間待機
    custom_print("1", "****-", "1秒後に改行します", "Line 5")
    time.sleep(1)  # 1秒間待機
    custom_print("0", "*****", "0秒後に改行します", "Line 6")
    time.sleep(1)  # 1秒間待機
    # 改行を含むケースのテスト
    time.sleep(1)  # 1秒間待機
    custom_print("Line 5", "/return", "Line 6", "Line 7")
    time.sleep(1)  # 1秒間待機
    custom_print("改行", "完了", "しました", "Line 7")

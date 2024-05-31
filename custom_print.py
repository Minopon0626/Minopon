import sys

def custom_print(input_string):
    """
    受け取った文字列を標準出力に出力する関数。
    引数に"/return"という文字列を取った場合は、最新の一行を削除せずに改行を行う。
    それ以外の文字列を取った場合は、既存の標準出力の最新の一行を削除して新しい文字列を出力する。
    Args:
    input_string (str): 出力する文字列。"/return"の場合は改行を行う。
    """
    # 標準出力をフラッシュしてすべてのデータが書き込まれるようにする
    sys.stdout.flush()
    if input_string == "/return":
        # "/return" 文字列が渡された場合、最新の一行を削除せずに改行する
        sys.stdout.write('\n')  # 改行
    else:
        # カーソルを一行上に移動してその行をクリアする
        sys.stdout.write('\x1b[1A')  # カーソルを一行上に移動
        sys.stdout.write('\x1b[2K')  # 行をクリア
        print(input_string, end='')  # 新しい文字列を改行なしで出力
        sys.stdout.write('\n')  # 改行を手動で追加

# 例としての使用方法
if __name__ == "__main__":
    import time

    # 初期の行を表示
    print("Line 1")
    time.sleep(1)  # 1秒間待機
    print("Line 2")
    time.sleep(1)  # 1秒間待機
    
    # "Line 2" を "New Line 2" に置き換える
    custom_print("New Line 2")
    time.sleep(1)  # 1秒間待機
    
    # 最新の一行を削除せずに改行
    custom_print("/return")
    
    # 新しい行を追加
    print("Line 3")

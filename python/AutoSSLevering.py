import sys
import pyautogui
import time
import random
import numpy as np

def leveling(times, ship_number):
    print("レベリング実行回数:" + str(times))
    autosupply()
    Leveling5to2(ship_number)


# 5-2自動レベリングの処理内容
def Leveling5to2(ship_number):
    messagePrint("   出撃を実行")

    autosortie()

    messagePrint("   南方海域を選択")

    # 海域選択画面から南方海域を選択
    moveAndclick(705, 835)
    # 南方海域に遷移完了

    # 南方海域から珊瑚諸島沖海戦(5-2)を選択
    moveAndclick(900, 480)
    # 珊瑚諸島沖海戦に遷移完了

    # 出撃を決定
    moveAndclick(1000, 820)
    moveAndclick(915, 830)
    # 出撃

    # 戦闘開始(羅針盤)
    moveAndclick(600, 520)
    # 羅針盤回転
    time.sleep(20)

    if ship_number > 1:
        messagePrint("   艦隊陣形選択")
        time.sleep(30)
        # 艦隊が先頭領域に突入
        moveAndclick(1090, 430)
        # 艦隊陣形を選択

    messagePrint("   戦闘終了まで待機中")
    # 渦巻と戦闘それぞれ待機
    time.sleep(30)
    # 戦闘終了

    messagePrint("   戦闘終了までの待機時間経過")

    # 戦闘結果をクリックして進める
    # 完全勝利Sを消費
    moveAndclick(1150, 200)
    # 完全勝利Sを消費完了

    # 次を選択
    moveAndclick(1150, 200)
    # 次を選択完了

    messagePrint("   撤退を選択")
    # 撤退を選択
    moveAndclick(760, 520)
    # 撤退を選択完了
    messagePrint("   出撃完了")

# 母港から海域選択画面までの遷移をする関数
def autosortie():
    messagePrint("   海域選択画面まで遷移")

    # 母港から出撃を選択
    moveAndclick(300, 550)
    # 出撃画面に遷移完了

    # 出撃画面から海域選択画面に遷移
    moveAndclick(340, 490)
    # 海域選択画面に遷移完了

    messagePrint("   海域選択画面まで遷移完了")

# 補給自動化
def autosupply():
    messagePrint("   補給を実行")

    # 母港から補給画面に遷移
    moveAndclick(110, 480)
    # 補給画面に遷移完了

    # 補給画面から全補給
    moveAndclick(175, 340)
    # 全補給完了

    # 補給画面から母港に遷移
    moveAndclick(65, 220)
    # 母港に遷移完了

    messagePrint("   補給完了")

# 引数にx, y座標をもらい移動した後に一定の遅延を挟みクリックする関数
def moveAndclick(x, y):
    pyautogui.moveTo(x, y)
    randomsleep()
    pyautogui.click()

def sleeplong(times):
    messagePrint("      ")
    for _ in range(times):
        messagePrint("*", end="", flush=True)
        times.sleep(10)

# U字分布を作成
def generate_u_shaped_random(min_value, max_value):
    # U字分布に基づく乱数を生成
    uniform_data = np.random.uniform(0, 1)
    u_shaped_value = min_value + (max_value - min_value) * np.minimum(uniform_data, 1 - uniform_data)
    return u_shaped_value

# ランダムな秒数停止する関数:実行ごとに挟んで検知しにくくする
def randomsleep():
    randomMax = 15.0
    randomMin = 8.0
    sleeptime = generate_u_shaped_random(randomMax, randomMin)

    remaining_time = sleeptime
    while remaining_time > 0:
        sys.stdout.write("      残り {:2} 秒".format(int(remaining_time)))  # 残り時間を表示
        sys.stdout.flush()
        time.sleep(1)
        remaining_time -= 1  # 残り時間を1秒減らす

    sys.stdout.write("      待機終了        \n")  # 待機時間終了
    sys.stdout.flush()


def repeat_function(times, ship_number):
    try:
        messagePrint("実行開始。モニター、ブラウザの準備をしてください。3秒後に開始します。\n")

        remaining_time = 3
        while remaining_time > 0:
            sys.stdout.write("準備中 {:2} 秒".format(remaining_time))
            sys.stdout.flush()
            time.sleep(1)
            remaining_time -= 1

        sys.stdout.write("準備完了        ")
        sys.stdout.flush()

        for i in range(times):
            leveling(i + 1, ship_number)  # leveling関数に新しい引数を渡す
            time.sleep(1)  # 操作間の待機時間（秒単位）
        autosupply()
        print(str(times) + "回のレベリングが完了しました")
    except KeyboardInterrupt:
        print("\n中断されました。現在のレベリング回数: " + str(i + 1))
        sys.exit(0)

def messagePrint(message):
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush

if __name__ == "__main__":
    if len(sys.argv) > 2:  # 引数が2つ以上あるかチェック
        try:
            repeat_times = int(sys.argv[1])  # 最初の引数を繰り返し回数として取得
            ship_number = int(sys.argv[2])  # 二番目の引数を取得
            repeat_function(repeat_times, ship_number)  # repeat_functionに二番目の引数も渡す
        except ValueError:  # 引数が整数でない場合のエラーハンドリング
            print("引数は整数である必要があります。")
    else:  # 必要な引数が指定されていない場合
        print("引数に繰り返し回数と艦隊の所有艦艇数を指定してください。")

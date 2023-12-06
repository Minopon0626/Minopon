import sys
import pyautogui
import time
import random

def leveling(times, ship_number):
    # ここに実行したい操作を記述
    print("レベリング実行回数:" + str(times))
    autosupply()
    Leveling5to2(ship_number)


# 5-2自動レベリングの処理内容
def Leveling5to2(ship_number):
    print("   出撃を実行")



    autosortie()

    print("   南方海域を選択")

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
        print("   艦隊陣形選択")
        time.sleep(30)
        # 艦隊が先頭領域に突入
        moveAndclick(1090, 430)
        # 艦隊陣形を選択

    print("   戦闘終了まで待機中")
    # 渦巻と戦闘それぞれ待機
    time.sleep(30)
    # 戦闘終了

    print("   戦闘終了までの待機時間経過")

    # 戦闘結果をクリックして進める
    # 完全勝利Sを消費
    moveAndclick(1150, 200)
    # 完全勝利Sを消費完了

    # 次を選択
    moveAndclick(1150, 200)
    # 次を選択完了

    print("   撤退を選択")
    # 撤退を選択
    moveAndclick(760, 520)
    # 撤退を選択完了
    print("   出撃完了")

# 母港から海域選択画面までの遷移をする関数
def autosortie():
    print("   海域選択画面まで遷移")

    # 母港から出撃を選択
    moveAndclick(300, 550)
    # 出撃画面に遷移完了

    # 出撃画面から海域選択画面に遷移
    moveAndclick(340, 490)
    # 海域選択画面に遷移完了

    print("   海域選択画面まで遷移完了")

# 補給自動化
def autosupply():
    print("   補給を実行")

    # 母港から補給画面に遷移
    moveAndclick(110, 480)
    # 補給画面に遷移完了

    # 補給画面から全補給
    moveAndclick(175, 340)
    # 全補給完了

    # 補給画面から母港に遷移
    moveAndclick(65, 220)
    # 母港に遷移完了

    print("   補給完了")

# 引数にx, y座標をもらい移動した後に一定の遅延を挟みクリックする関数
def moveAndclick(x, y):
    pyautogui.moveTo(x, y)
    randomsleep()
    pyautogui.click()

def sleeplong(times):
    print("      ")
    for _ in range(times):
        print("*", end="", flush=True)
        times.sleep(10)

# ランダムな秒数停止する関数:実行ごとに挟んで検知しにくくする
def randomsleep():
    randomMax = 15.0
    randomMin = 5.0
    sleeptime = random.uniform(randomMin, randomMax)
    print("      行動遅延中:" + str(sleeptime))  # 改行せずに出力を開始
    print("****1****2****3")

    for _ in range(int(sleeptime)):  # sleeptime秒間、ループを実行
        print("*", end="", flush=True)  # * を出力し、すぐにフラッシュ（表示）
        time.sleep(1)  # 1秒待機

    print(" 完了")  # 待機終了後に完了メッセージを出力

def repeat_function(times, ship_number):
    try:
        print("実行開始.3秒後までにモニター, ブラウザの準備をしてください")
        time.sleep(3)
        for i in range(times):
            leveling(i + 1, ship_number)  # leveling関数に新しい引数を渡す
            time.sleep(1)  # 操作間の待機時間（秒単位）
        autosupply()
        print(str(times) + "回のレベリングが完了しました")
    except KeyboardInterrupt:
        print("\n中断されました。現在のレベリング回数: " + str(i + 1))
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) > 2:  # 引数が2つ以上あるかチェック
        try:
            repeat_times = int(sys.argv[1])  # 最初の引数を繰り返し回数として取得
            ship_number = int(sys.argv[2])  # 二番目の引数を取得
            repeat_function(repeat_times, ship_number)  # repeat_functionに二番目の引数も渡す
        except ValueError:  # 引数が整数でない場合のエラーハンドリング
            print("最初の引数は整数である必要があります。")
    else:  # 必要な引数が指定されていない場合
        print("引数に繰り返し回数と艦隊の所有艦艇数を指定してください。")

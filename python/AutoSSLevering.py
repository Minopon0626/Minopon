import sys
import pyautogui
import time
import random

def leveling(times):
    # ここに実行したい操作を記述
    print("レベリング実行回数:" + str(times))
    autosupply()
    Leveling5to2()


# 5-2自動レベリングの処理内容
def Leveling5to2():
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

    print("   戦闘終了まで待機中")
    # 渦巻と戦闘それぞれ待機
    time.sleep(60)
    # 戦闘終了

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


# ランダムな秒数停止する関数:実行ごとに挟んで検知しにくくする
def randomsleep():
    randomMax = 10.0
    randomMin = 5.0
    sleeptime = random.uniform(randomMin, randomMax)
    print("      行動遅延中:" + str(sleeptime))  # 改行せずに出力を開始

    for _ in range(int(sleeptime)):  # sleeptime秒間、ループを実行
        print("*", end="", flush=True)  # * を出力し、すぐにフラッシュ（表示）
        time.sleep(1)  # 1秒待機

    print(" 完了")  # 待機終了後に完了メッセージを出力

def repeat_function(times):
    print("実行開始.3秒後までにモニター, ブラウザの準備をしてください")
    time.sleep(3)
    for i in range(times):
        leveling(i + 1)
        time.sleep(1)  # 操作間の待機時間（秒単位）
    autosupply()
    print(str(times) + "回のレベリングが完了しました")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            repeat_times = int(sys.argv[1])  # コマンドライン引数から繰り返し回数を取得
            repeat_function(repeat_times)
        except ValueError:  #引数が整数でない場合
            print("引数は整数である必要があります。")
    else:   #引数が指定されていない場合
        print("引数に繰り返し回数を指定してください。")

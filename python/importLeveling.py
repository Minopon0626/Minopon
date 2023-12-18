import importFunction
import time
import random

# 係数と少数第N位を引数にとり係数 * 1.5を最低5 ~ 最高10に対して掛け算をし少数第N位まで絞り返す関数
def randomNumber(coefficient, n):
    coefficient = coefficient * 1.5
    randomMin =  5 * coefficient
    randomMax = 10 * coefficient
    # RandomMin ~ RandomMaxまでの少数を生成
    randomNumber = random.uniform(randomMax, randomMin)
    # RandomNumberを少数第二位までまとめる
    randomNumber = round(randomNumber, n)
    return randomNumber

# 一秒ごとに待機して残っている時間を返す関数:待機した後に時間を返すので注意
def sleepFunction(sleepTime):
    # sleepTimeが1秒以上の場合は1秒待機
    if sleepTime >= 1:
        time.sleep(1)
        sleepTime -= 1
    # sleepTimeが1秒未満の場合は残りの時間だけ待機
    else:
        time.sleep(sleepTime)
        sleepTime = 0
    return sleepTime


# x座標, y座標, 係数, 少数第n位を引数に取り係数と少数n位秒を待機した後にx座標, y座標に移動とクリックを行う関数
def RandomSleepAndmoveAndclick(x, y, coefficient, n):
    # 待機する時間を決定(Remaining:残っている)
    RemainingTime = randomNumber(coefficient, n)
    # sleepTimeが0になるまで待機させると同時に残り時間を返す
    while RemainingTime > 0:
        sleepFunction(RemainingTime)
    # 待機が完了したので移動とクリックを行う
    importFunction.moveAndclick(x, y)
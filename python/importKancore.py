import importFunction
import time
import random

def randomNumber(coefficient, n):
    """
    係数に基づいてランダムな数を生成し、指定された小数点以下の桁数で丸める。
    Args:
        coefficient (float): 乗算係数。
        n (int): 小数点以下の桁数。
    Returns:
        float: 生成されたランダム数。
    """
    coefficient = coefficient * 1.5
    randomMin =  1
    randomMax = 10 * coefficient
    randomNumber = random.uniform(randomMin, randomMax)
    return round(randomNumber, n)

def autoSupply():
    """
    自動補給の一連の動作を実行する。
    """
    importFunction.messagePrint("   補給を実行")
    importFunction.moveAndClick(110, 480)
    importFunction.moveAndClick(175, 340)
    importFunction.moveAndClick(65, 220)
    importFunction.messagePrint("   補給完了")

def ReturnHomePort():
    """
    母港に戻る
    """
    randomSleepAndMoveAndClick(90, 220, 0.3, 2, "母港に戻る")

def randomSleepAndMoveAndClick(x, y, coefficient, n, actionDescription):
    """
    指定された係数と小数点以下の桁数に基づいてランダムな時間を計算し、その時間待機しながら
    次に実行するアクションとその待機秒数を表示した後、指定された座標に移動してクリックする。

    Args:
        x (int): X座標。
        y (int): Y座標。
        coefficient (float): 待機時間の乗算係数。
        n (int): 小数点以下の桁数。
        actionDescription (str): 実行するアクションの説明。
    """
    # 待機する時間を計算
    remainingTime = randomNumber(coefficient, n)

    # 残り時間が0になるまで待機
    while remainingTime > 0:
        # 次に実行する内容と待機秒数を表示
        importFunction.messagePrint(f"{actionDescription}: {remainingTime:.1f}秒")

        # 0.1秒待機
        time.sleep(0.1)
        remainingTime -= 0.1

    # 実行が完了したことを表示し、改行
    importFunction.messagePrint(f"{actionDescription}が完了しました\n")
    # print("\n")

    # 指定された座標でクリック
    importFunction.moveAndClick(x, y)

# 例: X=100, Y=200の座標で、係数1.0、小数点以下2桁でランダムな時間待機してクリック
# randomSleepAndMoveAndClick(100, 200, 1.0, 2, 補給)
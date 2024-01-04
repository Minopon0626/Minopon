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

    # 指定された座標でクリック
    importFunction.moveAndClick(x, y)

    # 例: X=100, Y=200の座標で、係数1.0、小数点以下2桁でランダムな時間待機してクリック
    # randomSleepAndMoveAndClick(100, 200, 1.0, 2, 補給)

def missionClick(missionNumber):
    """
    任務画面から指定された番号の任務をクリックする
    missionNumberに基づいて処理を実行する関数。
    まず、missionNumberを5で割った商に基づいて処理Aを実行し、
    次に余りに基づいて処理0、1、2、3、または4を実行する。

    Args:
    missionNumber (int): 処理を決定するための数値
    """

    # 5で割った商だけ処理Aを実行
    for _ in range(missionNumber // 5):
        randomSleepAndMoveAndClick(930, 860, 0.1, 2, "任務ページを変更")

    # 5で割った余りに基づいて処理B, C, D, E, Fのいずれかを実行
    remainder = missionNumber % 5
    if remainder == 0:
        randomSleepAndMoveAndClick(520, 370, 0.2, 2, "任務を受注")
    elif remainder == 1:
        randomSleepAndMoveAndClick(520, 470, 0.2, 2, "任務を受注")
    elif remainder == 2:
        randomSleepAndMoveAndClick(520, 570, 0.2, 2, "任務を受注")
    elif remainder == 3:
        randomSleepAndMoveAndClick(520, 670, 0.2, 2, "任務を受注")
    else:
        randomSleepAndMoveAndClick(520, 770, 0.2, 2, "任務を受注")

def missionSolt(missionDisplay, missionType=0):
    """
    missionDisplay = デイリーやウィークリーなど
    missionType    = 表示内容を切り替える, デフォルトは0で全表示
    """
    randomSleepAndMoveAndClick(90, (360 + (40 * missionDisplay)), 0.2, 2, f"表示内容を{missionDisplay}番に変更")

    if missionType != 0:
        randomSleepAndMoveAndClick((730 + (missionType * 100)), 285, 0.1, 2, f"表示を{missionType}番に変更")
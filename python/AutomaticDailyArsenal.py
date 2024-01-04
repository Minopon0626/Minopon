"""
前提
    1.母港画面から開始
    2.プログラムを実行してから秘書艦の艦種, 開発レシピを指定させる
    3.任務を受注する
    4.開発→建造→開発*3→建造*3を行う
    5.すでに受けている任務は一度すべてキャンセルする
予定
    1.必要な情報を受け取る
        1.秘書艦のタイプ
            1.艦種を指定させる
                0 = 戦艦
                1 = 空母
                2 = 重巡
                3 = 軽巡
                4 = 駆逐
                5 = 海防艦
                6 = 潜水艦
                7 = 補助艦艇
            2.艦種の入力を受け付ける
        2.開発レシピ
            1.秘書艦のタイプから読み出すファイルを選択しファイルを読み込む
            2.レシピ一覧を表示させる
                1.上から順番に数字が割り振る
            3.数字を入力させる
        3.建造レシピ
            1.大型建造を入力させる
                1.もしするのであれば最初の建造で行う
                2.建造レシピを入力させる(これは数値を入力させる)
            2.建造レシピを表示させる
            3.数字を入力させる
        4.任務の位置を入力させる
    2.秘書艦を指定する
        1.編成を開く
        2.旗艦の変更ボタンを押す
        3.艦種を指定(入力された内容から)
        4.一番上の船を選択
        5.母港にもどる
    3.任務を受注する
        1.任務をキャンセルする
        2.任務をクリックする
        3.指定された位置の任務を受注する
        4.母港に戻る
    4.開発を行う
    5.任務
    6.建造
    7.任務
    8.開発*3
    9.任務
    10.建造*3
    11.任務
"""
import pyautogui
import importFunction
import importKancore
import time

# 以下の変数はプログラム全体で使用されるため、グローバル変数として宣言
global secretaryShipType
global developmentRecipe
global buildingRecipe
global largeBuildCount
global largeBuildRecipe

# 変数全てに初期値-1を代入する
secretaryShipType = -1
developmentRecipe = -1
buildingRecipe = -1
largeBuildCount = -1
largeBuildRecipe = -1

"""
FFFFFFF U   U NN   NN CCCC TTTTTTTT IIIII OOOOO  NN   NN
FF      U   U NNN  NN C       TT      I   OO   OO NNN  NN
FFFFF   U   U NN N NN C       TT      I   OO   OO NN N NN
FF      U   U NN  NNN C       TT      I   OO   OO NN  NNN
FF       UUU  NN   NN CCCC    TT    IIIII  OOOOO  NN   NN
"""

def selectSecretaryShip():
    """
    ユーザーに秘書艦のタイプを選択させる。
    正しい入力が得られるまで繰り返す。
    """
    while True:
        try:
            shipType = int(input("秘書艦の艦種を指定してください。\nBB = 0, CV = 1, CA = 2, CL = 3, DD = 5, DE = 6, SS = 7, AV = 8\n入力: "))
            if 0 <= shipType <= 8:
                return shipType
            else:
                print("\n無効な入力です。0から8の範囲で入力してください。\n")
        except ValueError:
            print("\n数値を入力してください。\n")

def readDevelopmentRecipe(fileIndex, fileType, lineNumbers=None):
    """
    指定された秘書艦タイプに基づいてレシピを含むファイルを読み込み、指定された行があればそれを返し、
    なければ全行を表示する。

    Parameters:
    fileIndex (int): ファイルインデックス。
    fileType (int): ファイルタイプ（0 = 開発、1 = 建造、2 = 大型建造）。
    lineNumbers (list of int, optional): 読み込みたい行番号のリスト。デフォルトは None で、この場合全行が表示される。

    Returns:
    list or None: 指定された行の内容を含むリスト、または lineNumbers が None の場合は None。
    """
    fileName = ""
    if fileType == 0:
        fileName = f"developmentRecipeFile/developmentRecipeFile{fileIndex}.txt"
    elif fileType == 1:
        fileName = f"buildingRecipe/0.txt"
    elif fileType == 2:
        fileName = f"buildingRecipe/1.txt"
    else:
        print("不正なファイルタイプが指定されました。")
        return None

    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            if lineNumbers is None:
                print(f"ファイル {fileName} の全内容:")
                for line in file:
                    if not line.strip().startswith('#'):
                        print(line.strip())
                return None
            else:
                specificLines = []
                for i, line in enumerate(file, 1):  # 行番号を 1 から開始
                    if i in lineNumbers and not line.strip().startswith('#'):
                        specificLines.append(line.strip().split(','))  # 行をカンマで分割し、リストに追加
                return specificLines
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")
        return None
    except UnicodeDecodeError as e:
        print(f"ファイルの読み込み中にUnicodeDecodeErrorが発生しました: {e}")
        return None



def receiveNumber(upperLimit):
    """
    ユーザーから指定された上限値までの数字の入力を受け付ける。
    """
    while True:
        userInput = input(f"0から{upperLimit}の数字を入力してください: ")
        if userInput.isdigit() and 0 <= int(userInput) <= upperLimit:
            return int(userInput)
        else:
            print(f"0から{upperLimit}の数字で入力してください。")

def countDataInFile(fileIndex, fileType):
    """
    指定されたタイプのファイルが持っているデータ数をカウントする。
    """
    fileName = ""
    if fileType == 0:
        fileName = f"developmentRecipeFile/developmentRecipeFile{fileIndex}.txt"
    elif fileType == 1:
        fileName = f"buildingRecipe/0.txt"
    elif fileType == 2:
        fileName = f"buildingRecipe/1.txt"
    else:
        print("不正なファイルタイプが指定されました。")
        return 0

    count = 0
    try:
        with open(fileName, 'r', encoding='utf-8') as file:  # 'utf-8' エンコーディングを指定
            for line in file:
                if not line.startswith('#'):
                    count += 1
        return count
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")
        return 0
    except UnicodeDecodeError as e:
        print(f"ファイルの読み込み中にUnicodeDecodeErrorが発生しました: {e}")
        return 0

# 秘書艦を任命する関数
def secretaryShipAppointment(shipType):
    """
    秘書艦を任命する関数, 母港画面からスタートする前提
    shipType:秘書艦にする艦種
    """
    # 母港画面から編成をクリック
    importKancore.randomSleepAndMoveAndClick(300, 360, 0.2, 2, "編成をクリック")
    # 編成画面から旗艦の変更ボタンをクリック
    importKancore.randomSleepAndMoveAndClick(615, 475, 0.2, 2, "旗艦を変更")
    # 表示艦種をすべてオフに
    importKancore.randomSleepAndMoveAndClick(1130, 320, 0.2, 2, "表示艦種をすべてオンに")
    importKancore.randomSleepAndMoveAndClick(1130, 320, 0.2, 2, "表示艦種をすべてオフに")
    # 艦種部分をクリック
    if shipType == 0:
        x, y = 630, 320
    elif shipType == 1:
        x, y = 700, 320
    elif shipType == 2:
        x, y = 760, 320
    elif shipType == 3:
        x, y = 820, 320
    elif shipType == 4:
        x, y = 890, 320
    elif shipType == 5:
        x, y = 950, 320
    elif shipType == 6:
        x, y = 1020, 320
    else:  # shipTypeが他の値の場合、最後の座標を使用
        x, y = 1080, 320
    importKancore.randomSleepAndMoveAndClick(x, y, 0.2, 2, "艦種を表示")
    # 最も上の艦娘を選択
    importKancore.randomSleepAndMoveAndClick(750, 400, 0.2, 2, "一番上の艦娘を選択")
    # 選択
    importKancore.randomSleepAndMoveAndClick(1030, 830, 0.3, 2, "艦娘を選択")
    # 母港に戻る
    importKancore.ReturnHomePort()

# 建造スロットを指定してそこをクリックする関数
def buildingSlotClick(slotNumber):
    """
    建造スロットをクリックする
    slotNumber = 上から順に番号を振ってクリックするスロット選択(最初は0)
    """
    x = 930
    if slotNumber == 0:
        y = 430
    elif slotNumber == 1:
        y = 540
    elif slotNumber == 2:
        y = 660
    else:
        y = 790
    importKancore.randomSleepAndMoveAndClick(x, y, 0.3, 2, f"{slotNumber}番建造スロットを選択")
    # 獲得画面待機
    time.sleep(5)
    # 獲得画面スキップ
    importKancore.randomSleepAndMoveAndClick(315, 300, 0.5, 2, "画面スキップのクリック")


def cleanBuiledingSlot():
    """
    建造スロットすべてを開放していく。
    """
    for slotNumber in range(4):
        buildingSlotClick(slotNumber)

def developmentSelect():
    """
    工廠画面から開発をクリックする。
    その後渡されたレシピ番号に従いレシピを設定する
    """
    # 340, 660
    importKancore.randomSleepAndMoveAndClick(340, 660, 0.2, 2, "開発をクリック")
    developmentRecipe

"""
M       M   AAA   IIIII  N   N
MM     MM  A   A    I    NN  N
M M   M M  AAAAA    I    N N N
M  M M  M  A   A    I    N  NN
M   M   M  A   A  IIIII  N   N
"""

def main():
    global secretaryShipType, developmentRecipe, largeBuildCount, largeBuildRecipe, buildingRecipe

    # 秘書艦を決定
    secretaryShipType = selectSecretaryShip()

    # 開発レシピを決定
    readDevelopmentRecipe(secretaryShipType, 0)
    developmentRecipe = receiveNumber(countDataInFile(secretaryShipType, 0) - 1)

    # 大型建造の有無及び回数を決定
    print("大型建造の回数を入力してください")
    largeBuildCount = receiveNumber(4)

    # 大型建造を行う場合はレシピを聞く
    if largeBuildCount >= 1:
        readDevelopmentRecipe(secretaryShipType, 2)
        largeBuildRecipe = receiveNumber(countDataInFile(secretaryShipType, 2) - 1)

    # 通常の建造レシピを表示, 聞く
    print("通常建造の回数を入力してください")
    readDevelopmentRecipe(secretaryShipType, 1)
    buildingRecipe = receiveNumber(countDataInFile(secretaryShipType, 1) - 1)

    # 秘書艦を任命する
    secretaryShipAppointment(secretaryShipType)

    # 母港から任務画面に移動する
    importKancore.randomSleepAndMoveAndClick(850, 230, 0.4, 2, "任務画面に移動")
    importKancore.randomSleepAndMoveAndClick(315, 300, 0.5, 2, "画面スキップのクリック")

    # 遂行中任務に切り替え
    importKancore.missionSolt(1)
    # 任務を受注する前にすでに受注している任務を消す
    for _ in range(7):
        # すでに受注している任務を7回クリックする（要は全消し）
        importKancore.missionClick(0)

    # デイリー工廠任務を受注
    importKancore.missionSolt(2, 3)
    importKancore.missionClick(0)

    # 母港に戻る
    importKancore.ReturnHomePort()

    # 工廠を開くまで一度時間を置く
    time.sleep(2)

    importKancore.randomSleepAndMoveAndClick(410, 700, 0.2, 2, "工廠をクリック")
    # 建造スロットをすべて空にする
    cleanBuiledingSlot()

# 開発を行う

# 任務を受注する

# 建造を行う

# 任務を受注する

# 開発3を行う

# 任務を受注する

# 建造3を行う

# 任務を受注する


# cmdから起動時の処理
if __name__ == "__main__":
    main()

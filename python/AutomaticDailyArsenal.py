import pyautogui
import importFunction
import importKancore

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
# 変数宣言
secretaryShipType = -1  #秘書艦のタイプ
developmentRecipe = -1  #開発レシピ番号
buildingRecipe    = -1  #建造レシピ
largeBuildCount   = -1  #大型建造の回数
largeBuildRecipe  = [-1, -1, -1, -1]  #大型建造のレシピ
# 大型建造時のレシピ説明
descriptions = ["the first number", "the second number", "the third number", "the fourth number"]



"""
FFFFFFF U   U NN   NN CCCC TTTTTTTT IIIII OOOOO  NN   NN
FF      U   U NNN  NN C       TT      I   OO   OO NNN  NN
FFFFF   U   U NN N NN C       TT      I   OO   OO NN N NN
FF      U   U NN  NNN C       TT      I   OO   OO NN  NNN
FF       UUU  NN   NN CCCC    TT    IIIII  OOOOO  NN   NN
"""

def selectSecretaryShip():
    """
    ユーザーに秘書艦のタイプを選択させ、適切な入力があるまで繰り返す関数
    """
    while True:
        try:
            secretaryShipType = int(input("秘書艦の艦種を指定してください。\nBB = 0, CV = 1, CA = 2, CL = 3, DD = 5, DE = 6, SS = 7, AV = 8\n入力: "))
            if 0 <= secretaryShipType <= 8:
                return secretaryShipType
            else:
                print("\n無効な入力です。0から8の範囲で入力してください。\n")
        except ValueError:
            # 数字以外が入力された場合のエラーメッセージ
            print("\n数値を入力してください。\n")

def readDevelopmentRecipe(secretaryShipType):
    """
    開発レシピ用
    指定された秘書艦タイプに基づいて開発レシピを含むファイルを読み込む関数
    """
    fileName = f"developmentRecipeFile/developmentRecipeFile{secretaryShipType}.txt"
    try:
        with open(fileName, 'r') as file:
            print(f"ファイル {fileName} の内容:")
            for line in file:
                # データセットごとに改行して出力
                print(line.strip())
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")
        return # ファイルが見つからなかった場合はFalseを返す

def receiveNumber(upper_limit):
    """
    ユーザーから指定された上限値までの数字の入力を受け付けるプログラム。
    有効な数字が入力されると、その数字を返す。

    :param upper_limit: 許可される数字の上限値
    """
    while True:  # 無限ループを使用して入力を繰り返す
        user_input = input(f"0から{upper_limit}の数字を入力してください: ")
        if user_input.isdigit() and 0 <= int(user_input) <= upper_limit:  # 入力が 0 から upper_limit の数字かどうかをチェック
            return int(user_input)  # 有効な数字の場合はその数字を返す
        else:
            print(f"0から{upper_limit}の数字で入力してください")  # 不正な入力の場合はメッセージを表示


def countDataSetsInFile(fileIndex):
    """
    開発レシピ用
    指定された番号のファイルが何個のデータ(=レシピ)を持っているかを確認する関数
    """
    fileName = f"developmentRecipeFile/developmentRecipeFile{fileIndex}.txt"
    count = 0

    try:
        with open(fileName, 'r') as file:
            for line in file:
                count += 1
        return count
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")
        return 0

# 数字が4桁で下2桁が0かどうかをチェックする関数
def isValidInput(inputValue):
    return len(inputValue) == 4 and inputValue.isdigit() and inputValue.endswith("00")

# 大型建造のレシピを入力させる関数
def largeBuildRecipeAsk():
    for i in range(4):
        while True:
            userInput = input(f" {descriptions[i]}の使用量を決定してください: ")
            if isValidInput(userInput):
                largeBuildRecipe[i] = int(userInput)
                break
            else:
                print("不正な値です")

def PrintAll():
    print(f"秘書艦の艦種  :{secretaryShipType}")
    print(f"開発レシピ    :{developmentRecipe}")
    print(f"大型建造の回数:{largeBuildCount}")
    print(f"大型建造のレシピ:{largeBuildRecipe}")


"""
M       M   AAAA    IIIII  N   N
MM     MM   A  A      I    NN  N
M M   M M  AAAAAA     I    N N N
M  M M  M  A     A    I    N  NN
M   M   M  A     A  IIIII  N   N
"""

# メインプログラム

# 秘書艦を決定する
secretaryShipType = selectSecretaryShip()
# 開発レシピを決定する
    # 開発レシピを表示する
readDevelopmentRecipe(secretaryShipType)
    # 開発レシピの入力を受け付ける
developmentRecipe = receiveNumber(countDataSetsInFile(secretaryShipType) - 1)

# 大型建造の有無及び回数を聞く
print("大型建造の回数を入力してください")
largeBuildCount = receiveNumber(4)

if largeBuildCount >= 1:
    # 大型建造を行う場合
    largeBuildRecipeAsk()

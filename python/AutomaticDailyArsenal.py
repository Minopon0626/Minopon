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

def readDevelopmentRecipe(shipType):
    """
    指定された秘書艦タイプに基づいて開発レシピを含むファイルを読み込む。
    """
    fileName = f"developmentRecipeFile/developmentRecipeFile{shipType}.txt"
    try:
        with open(fileName, 'r') as file:
            print(f"ファイル {fileName} の内容（コメント除外）:")
            for line in file:
                if not line.strip().startswith('#'):
                    print(line.strip())
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")

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
        # fileName = f"buildingRecipe/{fileIndex}"
        fileName = f"buildingRecipe/0"
    elif fileType == 2:
        # fileName = f"largeConstructionRecipe/largeConstructionRecipe{fileIndex}.txt"
        fileName = f"buildingRecipe/1"
    else:
        print("不正なファイルタイプが指定されました。")
        return 0

    count = 0
    try:
        with open(fileName, 'r') as file:
            for line in file:
                if not line.startswith('#'):
                    count += 1
        return count
    except FileNotFoundError:
        print(f"ファイル {fileName} は存在しません。")
        return 0

def main():
    global secretaryShipType, developmentRecipe, largeBuildCount, largeBuildRecipe

    # 秘書艦を決定
    secretaryShipType = selectSecretaryShip()

    # 開発レシピを決定
    readDevelopmentRecipe(secretaryShipType)
    developmentRecipe = receiveNumber(countDataInFile(secretaryShipType, 0) - 1)

    # 大型建造の有無及び回数を決定
    print("大型建造の回数を入力してください")
    largeBuildCount = receiveNumber(4)

    # 大型建造を行う場合はレシピを聞く
    if largeBuildCount >= 1:
        print("noLargeBuild")

if __name__ == "__main__":
    main()

# 大型建造レシピ部分から開始

# 通常の建造レシピを表示, 聞く

# 秘書艦を任命する

# 任務を受注する

# 開発を行う

# 任務を受注する

# 建造を行う

# 任務を受注する

# 開発3を行う

# 任務を受注する

# 建造3を行う

# 任務を受注する

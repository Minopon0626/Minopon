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
# 以下の変数はプログラム全体で使用されるため、グローバル変数として宣言
global secretary_ship_type
global development_recipe
global building_recipe
global large_build_count
global large_build_recipe

# 変数全てに初期値-1を代入する
secretary_ship_type = -1
development_recipe = -1
building_recipe = -1
large_build_count = -1
large_build_recipe = -1

# 秘書艦のタイプを選択する関数
def select_secretary_ship():
    """
    ユーザーに秘書艦のタイプを選択させる。
    正しい入力が得られるまで繰り返す。
    """
    while True:
        try:
            ship_type = int(input("秘書艦の艦種を指定してください。\nBB = 0, CV = 1, CA = 2, CL = 3, DD = 5, DE = 6, SS = 7, AV = 8\n入力: "))
            if 0 <= ship_type <= 8:
                return ship_type
            else:
                print("\n無効な入力です。0から8の範囲で入力してください。\n")
        except ValueError:
            print("\n数値を入力してください。\n")

# 指定された秘書艦タイプに基づいて開発レシピを含むファイルを読み込む関数
def read_development_recipe(ship_type):
    """
    指定された秘書艦タイプに基づいて開発レシピを含むファイルを読み込む。
    """
    file_name = f"developmentRecipeFile/developmentRecipeFile{ship_type}.txt"
    try:
        with open(file_name, 'r') as file:
            print(f"ファイル {file_name} の内容（コメント除外）:")
            for line in file:
                if not line.strip().startswith('#'):
                    print(line.strip())
    except FileNotFoundError:
        print(f"ファイル {file_name} は存在しません。")

# ユーザーからの数値入力を受け付ける関数
def receive_number(upper_limit):
    """
    ユーザーから指定された上限値までの数字の入力を受け付ける。
    """
    while True:
        user_input = input(f"0から{upper_limit}の数字を入力してください: ")
        if user_input.isdigit() and 0 <= int(user_input) <= upper_limit:
            return int(user_input)
        else:
            print(f"0から{upper_limit}の数字で入力してください。")

# 指定されたファイルのデータ数をカウントする関数
def count_data_in_file(file_index, file_type):
    """
    指定されたタイプのファイルが持っているデータ数をカウントする。
    """
    file_name = ""
    if file_type == 0:
        file_name = f"developmentRecipeFile/developmentRecipeFile{file_index}.txt"
    elif file_type == 1:
        file_name = f"buildingRecipe/{file_index}"
    elif file_type == 2:
        file_name = f"largeConstructionRecipe/largeConstructionRecipe{file_index}.txt"
    else:
        print("不正なファイルタイプが指定されました。")
        return 0

    count = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if not line.startswith('#'):
                    count += 1
        return count
    except FileNotFoundError:
        print(f"ファイル {file_name} は存在しません。")
        return 0

# 数字が4桁で下2桁が0かどうかをチェックする関数
def is_valid_input(input_value):
    return len(input_value) == 4 and input_value.isdigit() and input_value.endswith("00")

# 大型建造のレシピを入力させる関数
def large_build_recipe_ask():
    descriptions = ["the first number", "the second number", "the third number", "the fourth number"]
    large_build_recipe = []
    for i in range(4):
        while True:
            user_input = input(f"{descriptions[i]}の使用量を決定してください: ")
            if is_valid_input(user_input):
                large_build_recipe.append(int(user_input))
                break
            else:
                print("不正な値です。")
    return large_build_recipe

# メインプログラム
def main():
    global secretary_ship_type, development_recipe, large_build_count, large_build_recipe

    # 秘書艦を決定
    secretary_ship_type = select_secretary_ship()

    # 開発レシピを決定
    read_development_recipe(secretary_ship_type)
    development_recipe = receive_number(count_data_in_file(secretary_ship_type, 0) - 1)

    # 大型建造の有無及び回数を決定
    print("大型建造の回数を入力してください")
    large_build_count = receive_number(4)

    # 大型建造を行う場合はレシピを聞く
    if large_build_count >= 1:
        large_build_recipe = large_build_recipe_ask()

    print("秘書艦の艦種  :", secretary_ship_type)
    print("開発レシピ    :", development_recipe)
    print("大型建造の回数:", large_build_count)
    print("大型建造のレシピ:", large_build_recipe)
    print("end")

if __name__ == "__main__":
    main()

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

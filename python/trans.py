import os
import sys
from googletrans import Translator, LANGUAGES

def translate_file(file_name):
    # プログラムが格納されているディレクトリを取得
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # 指定されたファイルのフルパスを生成
    file_path = os.path.join(current_directory, file_name)

    # ファイルが存在するか確認
    if not os.path.isfile(file_path):
        print(f"ファイル'{file_name}'が見つかりません。")
        return

    # ファイルを読み込む
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except IOError as e:
        print(f"ファイルの読み込み中にエラーが発生しました: {e}")
        return

    # 翻訳するテキストが空であるか確認
    if not file_content.strip():
        print("翻訳するテキストがファイルに含まれていません。")
        return

    # 翻訳器を初期化
    translator = Translator()

    # ファイルの内容を日本語に翻訳 (ここでは'en'から'ja'に翻訳すると仮定)
    try:
        translated_content = translator.translate(file_content, src='en', dest='ja').text
        # 翻訳結果が空でないことを確認
        if not translated_content.strip():
            raise ValueError("翻訳結果が空です。")
    except Exception as e:
        print(f"翻訳中にエラーが発生しました: {e}")
        return

    # 翻訳された内容を新しいファイルに保存
    output_file_name = f"japanese_{file_name}"
    output_file_path = os.path.join(current_directory, output_file_name)

    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_content)
    except IOError as e:
        print(f"ファイルの保存中にエラーが発生しました: {e}")
        return

    print(f"'{file_name}'が'{output_file_name}'として翻訳され、保存されました。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python translate.py ファイル名")
    else:
        file_name = sys.argv[1]
        translate_file(file_name)

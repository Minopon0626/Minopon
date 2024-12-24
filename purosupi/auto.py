import time
import pyautogui

print("自動化アルゴリズムを起動")

# 数秒待ってから処理開始（ユーザーがウィンドウをアクティブにするための猶予）
time.sleep(5)

# テキストの自動入力
text = "これは自動で入力されたテキストです。"
for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.05)  # 文字間隔を少しあける（任意）

# 特定のキーを押す例（Enterキー）
pyautogui.press('enter')

# 複数キーの同時押し（例：Ctrl+Sで保存）
pyautogui.hotkey('ctrl', 's')

def press_key_and_wait(key):
    # 特定のキーを押す
    pyautogui.press(key)
    
    # コンソールへ入力したキーの表示
    print(f"{key} を押しました")
    
    # 4秒待機
    time.sleep(4)

# 使用例
if __name__ == "__main__":
    # "enter"キーを入力後、4秒待機
    press_key_and_wait('enter')
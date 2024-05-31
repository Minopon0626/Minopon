import pyautogui
import time

print("5秒後のマウス位置を取得します")
# ユーザーがマウスを動かして位置を確認できるように少し待機
time.sleep(5)

# 現在のマウスの位置を取得
x, y = pyautogui.position()
print(f"現在のマウスの位置: x={x}, y={y}")

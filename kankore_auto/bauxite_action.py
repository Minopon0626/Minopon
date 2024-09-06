import pyautogui

def bauxite_click(current_task_label):
    # ラベルを「ボーキ処理中...」に更新
    current_task_label.config(text="ボーキ処理中...")
    
    # クリック処理を500ms（0.5秒）の遅延で実行
    current_task_label.after(500, perform_bauxite_click)

def perform_bauxite_click():
    # 仮に座標 (100, 100) をクリック
    pyautogui.click(100, 100)
    print("ボーキクリック完了")

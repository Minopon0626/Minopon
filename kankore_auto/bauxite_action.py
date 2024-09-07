from utility_functions import delayed_click

def bauxite_click(root, current_task_label):
    # ラベルを「ボーキ処理中...」に更新
    current_task_label.config(text="ボーキ処理中...")
    # 3秒遅延でマウス移動し、さらに2秒後にクリック
    delayed_click(root, 100, 100)
    
    current_task_label.config(text="ボーキ完了")

from utility_functions import delayed_click, delayed_update

def bauxite_click(root, current_task_label):
    # ラベルを「ボーキ処理中...」に更新
    #current_task_label.config(text="ボーキ処理中...")
    delayed_update(root, current_task_label, 0, "ボーキ処理中...")
    # 3秒遅延でマウス移動し、さらに2秒後にクリック
    delayed_click(root, 300, 360)
    
    # 5秒後に「ボーキ完了」に更新する
    delayed_update(root, current_task_label, 5000, "ボーキ完了")